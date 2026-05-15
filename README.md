# HCU Colombia — Historia Clínica Única Electrónica Interoperable

> **"Ningún médico debería operar a ciegas. Ningún paciente debería ser invisible para el sistema de salud."**

[![FHIR R4](https://img.shields.io/badge/FHIR-R4%204.0.1-brightgreen)](https://hl7.org/fhir/R4/)
[![Ley 2015](https://img.shields.io/badge/Ley%202015-2020-blue)](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=117158)
[![License](https://img.shields.io/badge/license-Open%20Source-orange)](LICENSE)
[![Status](https://img.shields.io/badge/estado-Prototipo%20Operativo-brightgreen)]()

---

## ¿Qué es HCU Colombia?

**HCU Colombia** es la implementación técnica de la **Ley 2015 de 2020**, que ordenó la creación de la Historia Clínica Única Electrónica Interoperable en Colombia — una norma vigente hace seis años que sigue sin reglamentarse.

Este repositorio contiene el **portal web del prototipo**, construido sobre el estándar internacional **HL7 FHIR R4** — el mismo que usan la Unión Europea, Estados Unidos y Chile.

### El problema
Cada año, miles de colombianos llegan a urgencias sin que el médico pueda acceder a su historial clínico. A qué son alérgicos. Qué enfermedades padecen. Qué medicamentos toman. El médico decide **a ciegas**.

### La solución
Un repositorio federado de historias clínicas, interoperable entre IPS y EPS, basado en estándares abiertos, que permite a cualquier médico autorizado consultar el historial completo de su paciente en segundos — con trazabilidad inmodificable de cada acceso.

---

## Demo en vivo

🌐 **Portal:** https://isaeldjquinterof-dev.github.io/hcu-portal

### Cédulas de prueba disponibles

| Cédula | Paciente | Ciudad |
|---|---|---|
| `1140876543` | Carlos Andrés Martínez Pérez | Barranquilla |
| `32456789` | Valentina García Rodríguez | Barranquilla |
| `72345678` | Jorge Luis Herrera Blanco | Soledad |
| `45678901` | Luisa Fernanda Torres Gómez | Malambo |
| `1001234567` | María Elena Rodríguez | Barranquilla |

---

## Stack tecnológico

| Componente | Tecnología |
|---|---|
| Servidor FHIR | [HAPI FHIR JPA Server](https://hapifhir.io/) 8.8.0 |
| Estándar | HL7 FHIR R4 (4.0.1) |
| Base de datos | PostgreSQL 16 Alpine |
| Infraestructura | Docker + Docker Compose |
| Portal web | HTML5 / CSS3 / JavaScript vanilla |
| Identificación | Registraduría Nacional del Estado Civil (RNEC) |
| Marco legal | Ley 2015 de 2020 / Resolución 1888 de 2025 |

---

## Arquitectura

```
┌─────────────────────────────────────────────────┐
│  Portal HCU Colombia (GitHub Pages)              │
│  Validación CC → Registraduría RNEC             │
│  Búsqueda / Registro / Visitas / Recién nacidos  │
└────────────────────┬────────────────────────────┘
                     │ FHIR REST API
                     ▼
┌─────────────────────────────────────────────────┐
│  HAPI FHIR R4 Server (localhost:8080)            │
│  Recursos: Patient / AllergyIntolerance          │
│            Condition / MedicationStatement        │
│            Encounter / Coverage                  │
└────────────────────┬────────────────────────────┘
                     │ JDBC
                     ▼
┌─────────────────────────────────────────────────┐
│  PostgreSQL 16 (localhost:5432)                  │
│  Base: hapi_fhir                                 │
└─────────────────────────────────────────────────┘
```

**Modelo federado:** En producción, cada IPS/EPS mantiene su propia base de datos. El adaptador FHIR permite interoperabilidad sin migrar datos existentes.

---

## Levantar el prototipo localmente

### Prerrequisitos
- Docker Desktop 4.0+
- Python 3.10+
- WSL 2 (Windows)

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/IsaelDJQuinteroF-Dev/hcu-portal.git
cd hcu-portal

# 2. Configurar variables de entorno
echo "DB_PASSWORD=HCU_Demo_2026!" > .env

# 3. Levantar servidor FHIR + PostgreSQL
docker-compose up -d

# 4. Verificar que está corriendo
# Abrir: http://localhost:8080
```

### Cargar datos de prueba

```bash
pip install requests fhir.resources

# Pacientes sintéticos colombianos
python cargar_pacientes_sinteticos.py

# Usuarios demo para reuniones
python cargar_usuarios_demo.py
```

---

## Marco legal y normativo

| Norma | Descripción |
|---|---|
| **Ley 2015 de 2020** | Crea la Historia Clínica Única Electrónica Interoperable en Colombia |
| **Resolución 1888 de 2025** | Requisitos técnicos y operativos para la implementación |
| **Decreto 780 de 2016** | Normas comunes de Seguridad Social — RUAF |
| **Ley 23 de 1981** | Manejo, custodia y confidencialidad de la historia clínica |
| **Ley 1581 de 2012** | Protección de datos personales en salud |

---

## Piloto regional propuesto

**Atlántico — Barranquilla como primer departamento piloto**

Bogotá opera su HCEU distrital desde 2016 (BID — referente América Latina).
Méderi implementó en su red hospitalaria en 2025 (plataforma propietaria).
**Nadie lo ha hecho nacional con FHIR R4 de código abierto. Eso es HCU Colombia.**

### Fases del piloto

```
Fase 0 (Mes 1-2):   Diagnóstico IPS/EPS Atlántico — inventario de sistemas
Fase 1 (Mes 3-6):   3-5 IPS piloto con adaptadores FHIR instalados
Fase 2 (Mes 6-18):  Expansión departamental + SISBÉN/RUAF/ADRES
Fase 3 (Mes 18-36): Escalamiento nacional + reglamentación Ley 2015
```

---

## Integración con sistemas nacionales

| Sistema | Datos | Ruta de integración |
|---|---|---|
| **RNEC (Registraduría)** | Identidad, CC, fecha nacimiento | Convenio institucional |
| **SISBÉN / RSH (DNP)** | Grupo socioeconómico, caracterización hogar | rshterritorial@dnp.gov.co |
| **RUAF / SISPRO (MinSalud)** | EPS, pensión, ARL, cesantías | Acuerdo MinSalud |
| **ADRES** | Afiliación EPS activa, régimen | Acuerdo ADRES |

---

## Autor

**Isael De Jesús Quintero Fuentes**
Administrador de Empresas — Universidad Autónoma del Caribe
Barranquilla, Atlántico, Colombia

- Creador y desarrollador del prototipo HCU Colombia
- Registro de autoría: Dirección Nacional de Derecho de Autor (DNDA) — en trámite
- Marca: Superintendencia de Industria y Comercio (SIC) — en trámite

---

## Contacto

Para propuestas de piloto, alianzas institucionales o información técnica:

📧 isael.quinterof@gmail.com
🔗 github.com/IsaelDJQuinteroF-Dev

---

*HCU Colombia — Ley 2015 de 2020 · FHIR R4 · Código abierto · Piloto Atlántico-Barranquilla*
