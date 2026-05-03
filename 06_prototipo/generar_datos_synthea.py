#!/usr/bin/env python3
"""
HCU Colombia — Cargador de Datos Sintéticos
Genera pacientes sintéticos compatibles con los perfiles FHIR colombianos
y los carga al servidor HAPI FHIR para pruebas del prototipo.

Requisito previo: Tener Synthea instalado y haber generado datos.
  - Descargar Synthea: https://github.com/synthetichealth/synthea
  - Ejecutar: ./run_synthea -p 100 Colombia

Autor: Isael De Jesús Quintero Fuentes | Abril 2026
"""

import json
import os
import sys
import glob
from typing import List, Dict, Any, Optional

import requests
from fhir.resources.patient import Patient
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.condition import Condition
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.observation import Observation


# ============================================================
# CONFIGURACIÓN
# ============================================================

FHIR_SERVER_URL = "http://localhost:8080/fhir"
SYNTHEA_OUTPUT_DIR = "./synthea_output/fhir"


# ============================================================
# FUNCIONES DE CARGA
# ============================================================


def cargar_archivos_fhir(directorio: str) -> List[Dict[str, Any]]:
    """
    Lee todos los archivos JSON de un directorio de salida de Synthea.

    Args:
        directorio: Ruta a la carpeta con archivos FHIR JSON.

    Returns:
        Lista de recursos FHIR como diccionarios.
    """
    archivos: List[str] = glob.glob(
        os.path.join(directorio, "**", "*.json"), recursive=True
    )
    recursos: List[Dict[str, Any]] = []

    for archivo in archivos:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data: Dict[str, Any] = json.load(f)

                # Un archivo puede contener un Bundle o un recurso individual
                if data.get("resourceType") == "Bundle":
                    for entry in data.get("entry", []):
                        recursos.append(entry.get("resource", {}))
                else:
                    recursos.append(data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️  Error leyendo {archivo}: {e}")

    return recursos


def subir_recurso_fhir(
    recurso: Dict[str, Any], tipo_recurso: str
) -> bool:
    """
    Sube un recurso FHIR individual al servidor HAPI.

    Args:
        recurso: Diccionario con el recurso FHIR.
        tipo_recurso: Tipo de recurso (Patient, Condition, etc.).

    Returns:
        True si se subió correctamente, False en caso contrario.
    """
    url: str = f"{FHIR_SERVER_URL}/{tipo_recurso}"

    try:
        response: requests.Response = requests.put(
            f"{url}/{recurso.get('id', '')}",
            json=recurso,
            headers={"Content-Type": "application/fhir+json"},
            timeout=15,
        )

        if response.status_code in [200, 201]:
            print(f"   ✅ {tipo_recurso}/{recurso.get('id', 'desconocido')}")
            return True
        else:
            print(
                f"   ❌ {tipo_recurso}/{recurso.get('id', 'desconocido')}: "
                f"({response.status_code}) {response.text[:100]}"
            )
            return False

    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error de conexión al subir {tipo_recurso}: {e}")
        return False


def construir_resumen_emergencia(
    paciente_id: str, recursos: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Construye el Resumen Digital de Atención (RDA) mínimo para urgencias.

    Corresponde al "núcleo mínimo vital" definido en la propuesta HCU Colombia:
    alergias, condiciones crónicas activas, medicamentos activos,
    grupo sanguíneo y últimos eventos de urgencias.

    Args:
        paciente_id: ID FHIR del paciente.
        recursos: Lista de todos los recursos FHIR disponibles.

    Returns:
        Diccionario con el resumen mínimo de urgencias.
    """
    rda: Dict[str, Any] = {
        "paciente_id": paciente_id,
        "alergias": [],
        "condiciones_cronicas": [],
        "medicamentos_activos": [],
        "grupo_sanguineo": None,
        "ultimas_urgencias": [],
    }

    for recurso in recursos:
        # Alergias
        if recurso.get("resourceType") == "AllergyIntolerance":
            if (
                recurso.get("patient", {})
                .get("reference", "")
                .endswith(paciente_id)
            ):
                rda["alergias"].append(
                    {
                        "codigo": recurso.get("code", {}).get("text", ""),
                        "criticidad": recurso.get("criticality", ""),
                    }
                )

        # Condiciones
        elif recurso.get("resourceType") == "Condition":
            if (
                recurso.get("subject", {})
                .get("reference", "")
                .endswith(paciente_id)
                and recurso.get("clinicalStatus", {})
                .get("coding", [{}])[0]
                .get("code", "")
                == "active"
            ):
                rda["condiciones_cronicas"].append(
                    {
                        "diagnostico": recurso.get("code", {}).get("text", ""),
                    }
                )

        # Medicamentos
        elif recurso.get("resourceType") == "MedicationRequest":
            if (
                recurso.get("subject", {})
                .get("reference", "")
                .endswith(paciente_id)
                and recurso.get("status") == "active"
            ):
                rda["medicamentos_activos"].append(
                    {
                        "medicamento": recurso.get(
                            "medicationCodeableConcept", {}
                        ).get("text", ""),
                    }
                )

        # Grupo sanguíneo (Observation tipo blood group)
        elif recurso.get("resourceType") == "Observation":
            codigo = (
                recurso.get("code", {}).get("coding", [{}])[0].get("code", "")
            )
            if codigo in ["882-1", "34532-2", "883-9"]:
                rda["grupo_sanguineo"] = (
                    recurso.get("valueString", "")
                    or recurso.get("valueCodeableConcept", {})
                    .get("text", "")
                )

    return rda


def main() -> None:
    """
    Flujo principal:
    1. Lee archivos FHIR generados por Synthea.
    2. Sube los recursos al servidor HAPI FHIR.
    3. Reporta estadísticas de carga.
    """
    print("\n🏥 HCU COLOMBIA — CARGADOR DE DATOS SINTÉTICOS")
    print("=" * 55)

    # Verificar que el servidor responda
    print("\n🔍 Verificando conexión al servidor FHIR...")
    try:
        resp = requests.get(f"{FHIR_SERVER_URL}/metadata", timeout=5)
        if resp.status_code == 200:
            print("   ✅ Servidor HAPI FHIR en línea.\n")
        else:
            print(f"   ❌ Servidor respondió con código {resp.status_code}")
            print(
                "   Verifica que docker-compose esté corriendo: "
                "docker-compose up -d\n"
            )
            sys.exit(1)
    except requests.exceptions.RequestException:
        print("   ❌ No se puede conectar al servidor FHIR.")
        print(
            "   Asegúrate de ejecutar primero: docker-compose up -d\n"
        )
        sys.exit(1)

    # Verificar directorio de Synthea
    if not os.path.isdir(SYNTHEA_OUTPUT_DIR):
        print(f"⚠️  Directorio no encontrado: {SYNTHEA_OUTPUT_DIR}")
        print("   Ejecuta Synthea primero:")
        print("   ./run_synthea -p 100 -m Colombia\n")
        # Crear datos mínimos de ejemplo
        print("   Creando datos de ejemplo mínimos para prueba...\n")
        with open("pacientes_ejemplo.json", "w") as f:
            json.dump(
                [
                    {
                        "resourceType": "Patient",
                        "id": "ejemplo-001",
                        "identifier": [
                            {
                                "system": "http://www.registraduria.gov.co",
                                "value": "1001234567",
                            }
                        ],
                        "name": [
                            {
                                "use": "official",
                                "family": "Rodríguez",
                                "given": ["María", "Elena"],
                            }
                        ],
                        "gender": "female",
                        "birthDate": "1978-05-14",
                    }
                ],
                f,
                indent=2,
            )
            print(
                "   ✅ Creado pacientes_ejemplo.json. "
                "Súbelo manualmente con POST a /fhir/Patient\n"
            )
        sys.exit(0)

    # Cargar recursos
    print(f"📂 Leyendo archivos FHIR desde: {SYNTHEA_OUTPUT_DIR}\n")
    recursos = cargar_archivos_fhir(SYNTHEA_OUTPUT_DIR)

    if not recursos:
        print("   ❌ No se encontraron recursos FHIR.\n")
        sys.exit(1)

    print(f"   📊 Total de recursos encontrados: {len(recursos)}\n")

    # Estadísticas
    stats: Dict[str, int] = {
        "Patient": 0,
        "AllergyIntolerance": 0,
        "Condition": 0,
        "MedicationRequest": 0,
        "Observation": 0,
        "subidos": 0,
        "fallidos": 0,
    }

    print("📤 Subiendo recursos al servidor HAPI FHIR...\n")
    for recurso in recursos:
        tipo: str = recurso.get("resourceType", "Unknown")
        if tipo in stats:
            stats[tipo] += 1
        else:
            stats[tipo] = 1

        if subir_recurso_fhir(recurso, tipo):
            stats["subidos"] += 1
        else:
            stats["fallidos"] += 1

    # Reporte final
    print(f"\n{'=' * 55}")
    print("📊 REPORTE DE CARGA")
    print(f"{'=' * 55}")
    print(f"  Pacientes          : {stats.get('Patient', 0)}")
    print(f"  Alergias           : {stats.get('AllergyIntolerance', 0)}")
    print(f"  Condiciones        : {stats.get('Condition', 0)}")
    print(f"  Medicamentos       : {stats.get('MedicationRequest', 0)}")
    print(f"  Observaciones      : {stats.get('Observation', 0)}")
    print(f"  ─────────────────")
    print(f"  ✅ Subidos exitosos : {stats['subidos']}")
    print(f"  ❌ Fallidos         : {stats['fallidos']}")
    print(f"{'=' * 55}\n")

    if stats["subidos"] > 0:
        print("✅ CARGA COMPLETA.")
        print("   Ahora puedes ejecutar el visor:")
        print("   python paciente_visor.py\n")


if __name__ == "__main__":
    main()