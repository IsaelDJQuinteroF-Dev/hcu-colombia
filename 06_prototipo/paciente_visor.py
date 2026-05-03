#!/usr/bin/env python3
"""
HCU Colombia — Visor de Pacientes
Demuestra consulta de datos clínicos desde el servidor HAPI FHIR.
Caso de éxito: médico de urgencias accede a alergias y condiciones crónicas
de un paciente atendido previamente en otro prestador.

Autor: Isael De Jesús Quintero Fuentes | Abril 2026
"""

import json
import sys
from typing import Optional, List, Dict, Any

from fhirclient import client
from fhirclient.models.patient import Patient
from fhirclient.models.allergyintolerance import AllergyIntolerance
from fhirclient.models.condition import Condition
from fhirclient.models.medicationrequest import MedicationRequest
from fhirclient.models.observation import Observation
import fhirclient.models.fhirdate as fhirdate
import requests


# ============================================================
# CONFIGURACIÓN
# ============================================================

FHIR_SERVER_URL = "http://localhost:8080/fhir"

# Configuración del cliente SMART on FHIR (modo open, sin OAuth para desarrollo)
settings = {
    "app_id": "hcu-colombia-visor",
    "api_base": FHIR_SERVER_URL,
    "redirect_uri": "http://localhost:5000/callback",
}

# ============================================================
# CLASE PRINCIPAL
# ============================================================


class VisorHCU:
    """
    Visor de Historia Clínica Única.
    Simula la consulta que haría un médico de urgencias.
    """

    def __init__(self, fhir_url: str = FHIR_SERVER_URL) -> None:
        """
        Inicializa el visor con la URL del servidor FHIR.

        Args:
            fhir_url: URL base del servidor FHIR (por defecto local).
        """
        self.fhir_url: str = fhir_url
        self.smart: client.FHIRClient = client.FHIRClient(settings=settings)

    def buscar_paciente_por_documento(
        self, numero_documento: str
    ) -> Optional[Dict[str, Any]]:
        """
        Busca un paciente por número de documento (cédula colombiana).

        Args:
            numero_documento: Número de identificación del paciente.

        Returns:
            Diccionario con datos del paciente o None si no se encuentra.
        """
        try:
            search_url: str = (
                f"{self.fhir_url}/Patient"
                f"?identifier={numero_documento}"
            )
            response: requests.Response = requests.get(
                search_url, timeout=10
            )
            response.raise_for_status()
            bundle: Dict[str, Any] = response.json()

            if bundle.get("total", 0) > 0:
                return bundle["entry"][0]["resource"]

            return None

        except requests.exceptions.RequestException as e:
            print(f"ERROR: No se pudo conectar al servidor FHIR: {e}")
            return None

    def obtener_alergias(
        self, patient_id: str
    ) -> List[Dict[str, Any]]:
        """
        Obtiene las alergias documentadas de un paciente.

        Args:
            patient_id: ID FHIR del paciente.

        Returns:
            Lista de alergias.
        """
        try:
            search_url: str = (
                f"{self.fhir_url}/AllergyIntolerance"
                f"?patient={patient_id}"
                f"&clinical-status=active"
            )
            response: requests.Response = requests.get(
                search_url, timeout=10
            )
            response.raise_for_status()
            bundle: Dict[str, Any] = response.json()

            alergias: List[Dict[str, Any]] = []
            for entry in bundle.get("entry", []):
                recurso: Dict[str, Any] = entry["resource"]
                alergia_info: Dict[str, Any] = {
                    "codigo": recurso.get("code", {}).get("text", "No especificado"),
                    "categoria": recurso.get("category", ["sin categoría"])[0],
                    "criticidad": recurso.get("criticality", "unknown"),
                }
                alergias.append(alergia_info)

            return alergias

        except requests.exceptions.RequestException as e:
            print(f"ERROR al obtener alergias: {e}")
            return []

    def obtener_condiciones_cronicas(
        self, patient_id: str
    ) -> List[Dict[str, Any]]:
        """
        Obtiene las condiciones crónicas activas de un paciente.

        Args:
            patient_id: ID FHIR del paciente.

        Returns:
            Lista de condiciones crónicas activas.
        """
        try:
            search_url: str = (
                f"{self.fhir_url}/Condition"
                f"?patient={patient_id}"
                f"&clinical-status=active"
            )
            response = requests.get(search_url, timeout=10)
            response.raise_for_status()
            bundle = response.json()

            condiciones = []
            for entry in bundle.get("entry", []):
                recurso = entry["resource"]
                cond_info = {
                    "diagnostico": recurso.get("code", {}).get("text", "No especificado"),
                    "fecha_inicio": recurso.get("onsetDateTime", "Desconocida"),
                    "categoria": recurso.get("category", [{}])[0].get("coding", [{}])[0].get("code", "sin categoría") if recurso.get("category") else "sin categoría",
                }
                condiciones.append(cond_info)

            return condiciones

        except requests.exceptions.RequestException as e:
            print(f"ERROR al obtener condiciones: {e}")
            return []

    def obtener_medicamentos_activos(
        self, patient_id: str
    ) -> List[Dict[str, Any]]:
        """
        Obtiene los medicamentos activos prescritos a un paciente.

        Args:
            patient_id: ID FHIR del paciente.

        Returns:
            Lista de medicamentos activos con dosis.
        """
        try:
            search_url: str = (
                f"{self.fhir_url}/MedicationRequest"
                f"?patient={patient_id}"
                f"&status=active"
            )
            response = requests.get(search_url, timeout=10)
            response.raise_for_status()
            bundle = response.json()

            medicamentos = []
            for entry in bundle.get("entry", []):
                recurso = entry["resource"]
                med_info = {
                    "medicamento": (
                        recurso.get("medicationCodeableConcept", {})
                        .get("text", "No especificado")
                    ),
                    "dosis": (
                        recurso.get("dosageInstruction", [{}])[0]
                        .get("text", "No especificada")
                    ),
                }
                medicamentos.append(med_info)

            return medicamentos

        except requests.exceptions.RequestException as e:
            print(f"ERROR al obtener medicamentos: {e}")
            return []

    def generar_resumen_urgencias(
        self, numero_documento: str
    ) -> Optional[Dict[str, Any]]:
        """
        Genera el resumen clínico que vería un médico de urgencias:
        datos básicos, alergias, condiciones crónicas y medicamentos activos.

        Args:
            numero_documento: Número de identificación del paciente.

        Returns:
            Diccionario con el resumen completo listo para mostrar en pantalla.
        """
        # Paso 1: Buscar paciente
        paciente = self.buscar_paciente_por_documento(numero_documento)

        if not paciente:
            print(
                f"\n❌ PACIENTE NO ENCONTRADO: {numero_documento}\n"
                f"   El paciente no tiene HCU en este repositorio.\n"
                f"   Motivos posibles:\n"
                f"   - No ha sido atendido en ningún prestador conectado.\n"
                f"   - El documento ingresado es incorrecto.\n"
            )
            return None

        patient_id = paciente["id"]

        # Paso 2: Obtener nombre
        nombre = "No registrado"
        if paciente.get("name"):
            nombres_dados = paciente["name"][0].get("given", [])
            apellido = paciente["name"][0].get("family", "")
            nombre = f"{' '.join(nombres_dados)} {apellido}".strip()

        # Paso 3: Obtener datos clínicos relevantes para urgencias
        print(f"\n🔍 CONSULTANDO HCU de {nombre} (ID: {numero_documento})...\n")

        alergias = self.obtener_alergias(patient_id)
        condiciones = self.obtener_condiciones_cronicas(patient_id)
        medicamentos = self.obtener_medicamentos_activos(patient_id)

        # Paso 4: Construir resumen
        resumen: Dict[str, Any] = {
            "paciente": {
                "nombre": nombre,
                "documento": numero_documento,
                "genero": paciente.get("gender", "No registrado"),
                "fecha_nacimiento": paciente.get("birthDate", "No registrada"),
                "id_fhir": patient_id,
            },
            "alergias": alergias,
            "alergias_criticas": [
                a for a in alergias if a["criticidad"] == "high"
            ],
            "condiciones_cronicas": condiciones,
            "medicamentos_activos": medicamentos,
        }

        return resumen

    def mostrar_resumen(self, resumen: Dict[str, Any]) -> None:
        """
        Muestra el resumen clínico en consola con formato legible.

        Args:
            resumen: Diccionario con el resumen clínico generado.
        """
        p = resumen["paciente"]

        print("=" * 65)
        print("🏥 HCU COLOMBIA — RESUMEN DE ATENCIÓN DE URGENCIAS")
        print("=" * 65)
        print(f"\n📋 DATOS DEL PACIENTE")
        print(f"   Nombre          : {p['nombre']}")
        print(f"   Documento       : {p['documento']}")
        print(f"   Género          : {p['genero']}")
        print(f"   Fecha Nacimiento: {p['fecha_nacimiento']}")
        print(f"   ID FHIR         : {p['id_fhir']}")

        # ALERGIAS (sección crítica)
        print(f"\n⚠️  ALERGIAS")
        if resumen["alergias"]:
            for a in resumen["alergias"]:
                icono = "🔴" if a["criticidad"] == "high" else "🟡"
                print(
                    f"   {icono} {a['codigo']} "
                    f"(Criticidad: {a['criticidad']})"
                )
        else:
            print("   ✅ No se registran alergias documentadas.")

        # ALERTA si hay alergias críticas
        if resumen["alergias_criticas"]:
            print(f"\n   🚨 ¡ALERTA! El paciente tiene alergias críticas:")
            for a in resumen["alergias_criticas"]:
                print(f"      - {a['codigo']}")

        # CONDICIONES CRÓNICAS
        print(f"\n📌 CONDICIONES CRÓNICAS ACTIVAS")
        if resumen["condiciones_cronicas"]:
            for c in resumen["condiciones_cronicas"]:
                print(f"   • {c['diagnostico']} (Desde: {c['fecha_inicio']})")
        else:
            print("   ✅ No se registran condiciones crónicas activas.")

        # MEDICAMENTOS ACTIVOS
        print(f"\n💊 MEDICAMENTOS ACTIVOS")
        if resumen["medicamentos_activos"]:
            for m in resumen["medicamentos_activos"]:
                print(f"   • {m['medicamento']} — Dosis: {m['dosis']}")
        else:
            print("   ✅ No se registran medicamentos activos en curso.")

        # LEYENDA
        print(f"\n{'=' * 65}")
        print("📝 Este resumen se genera en tiempo real desde la HCU.")
        print("   Fuente: Repositorio Federado de Historia Clínica Única.")
        print("   Acceso registrado en bitácora inmodificable.")
        print(f"{'=' * 65}\n")


# ============================================================
# DEMOSTRACIÓN
# ============================================================

def main() -> None:
    """
    Punto de entrada del visor. Demuestra el caso de éxito:
    un médico de urgencias consulta la HCU de un paciente
    y evita un evento adverso gracias a la alerta de alergias.
    """
    visor = VisorHCU()

    # Documento de ejemplo (cédula colombiana)
    documento = "1001234567"

    print("\n🏥 HCU COLOMBIA — VISOR DE HISTORIA CLÍNICA ÚNICA")
    print("   Simulación: Médico de urgencias consulta HCU\n")

    # Generar resumen
    resumen = visor.generar_resumen_urgencias(documento)

    if resumen:
        visor.mostrar_resumen(resumen)

        # Verificar si el caso de éxito aplica
        if resumen["alergias_criticas"]:
            print("✅ CASO DE ÉXITO DEMOSTRADO:")
            print("   El médico de urgencias fue alertado sobre alergias críticas")
            print("   ANTES de prescribir. Se evitó un evento adverso grave.\n")
            print("   Este es el argumento central del proyecto de ley HCU.\n")


if __name__ == "__main__":
    main()