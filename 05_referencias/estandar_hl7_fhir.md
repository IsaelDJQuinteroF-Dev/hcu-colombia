# Estándar HL7 FHIR — Guía de Referencia para el Proyecto HCU

### Fast Healthcare Interoperability Resources

**Compilado por:** Isael Quintero | Abril 2026
*Documento de referencia técnica, no una implementación de código.*

\---

## ¿Qué es HL7 FHIR?

**HL7 FHIR** (Fast Healthcare Interoperability Resources) es el estándar internacional más moderno para el intercambio de información clínica entre sistemas de salud. Fue desarrollado por Health Level Seven International (HL7) y su versión estable actual es **FHIR R4 (Release 4)**, publicada en 2019.

Es el estándar exigido en este proyecto como lenguaje común obligatorio para todos los actores del sistema de salud colombiano.

\---

## Por qué FHIR y no otro estándar

|Característica|HL7 FHIR R4|HL7 v2 (anterior)|CDA/HL7 v3|
|-|-|-|-|
|Basado en web (REST/JSON)|✅|❌|Parcial|
|Fácil de implementar|✅|Moderado|Complejo|
|Adoptado mundialmente|✅|Amplio pero obsoleto|Limitado|
|Soporte para móviles y apps|✅|❌|❌|
|Exigido por EE.UU., UE, Australia|✅|❌|❌|
|Permite perfiles nacionales|✅|Limitado|Sí|

FHIR es el estándar que ya exigen los sistemas de salud más avanzados del mundo. Adoptarlo elimina la fragmentación técnica sin obligar a nadie a reemplazar sus sistemas — solo a agregar una capa de interoperabilidad.

\---

## Conceptos clave para entender la propuesta

### Recurso FHIR

La unidad básica de información. Cada tipo de dato clínico es un "recurso":

|Recurso|Qué contiene|
|-|-|
|`Patient`|Datos del paciente (nombre, identificación, fecha de nacimiento)|
|`Condition`|Diagnósticos y condiciones crónicas|
|`MedicationRequest`|Medicamentos prescritos|
|`AllergyIntolerance`|Alergias documentadas|
|`Observation`|Signos vitales, resultados de laboratorio|
|`Encounter`|Episodio de atención (urgencia, consulta, hospitalización)|
|`DiagnosticReport`|Resultados de imágenes y exámenes|
|`Immunization`|Vacunas aplicadas|
|`Procedure`|Procedimientos realizados|

### Núcleo mínimo vital del proyecto HCU

Para la base de datos de emergencia (accesible sin conectividad completa), el proyecto propone almacenar:

* `AllergyIntolerance` — alergias graves
* `Condition` (crónicas activas) — condiciones permanentes
* `MedicationRequest` (activos) — medicamentos en curso
* `Observation` (grupo sanguíneo, RH) — datos inmutables
* `Encounter` (últimos 3) — eventos recientes de urgencias

### Perfiles Colombianos FHIR

Una adaptación nacional del estándar que define qué campos son obligatorios en Colombia, cómo se codifican los documentos de identidad colombianos, cómo se integra con el RETHUS (registro del talento humano en salud), y las terminologías locales requeridas.

El Ministerio de Salud deberá publicar estos perfiles como primer hito de la Fase 1 del proyecto.

\---

## Modelo de interoperabilidad propuesto

```
Prestador A          Prestador B          Prestador C
(EPS grande)         (Clínica privada)    (Consultorio)
     |                     |                   |
  Sistema              Sistema             Sistema
  propio               propio              propio
     |                     |                   |
  Adaptador            Adaptador           Adaptador
  FHIR R4              FHIR R4             FHIR R4
     |                     |                   |
     +---------------------+-------------------+
                           |
              Plataforma Nacional de
              Interoperabilidad (PNI)
              \[Health Information Exchange]
                           |
              Repositorio Central de Índices
              (sabe dónde están los datos,
               no los almacena todos)
                           |
                    Portal del Paciente
                  (acceso ciudadano a su HC)
```

**Principio clave:** cada prestador conserva su sistema. Solo agrega el adaptador FHIR. No hay migración forzada ni pérdida de inversión.

\---

## Recursos para profundización técnica

* Especificación oficial FHIR R4: https://hl7.org/fhir/R4/
* Guías de implementación FHIR: https://fhir.org/guides/registry/
* Perfiles FHIR para América Latina (PAHO/OPS): https://paciowg.github.io/
* Sandbox de pruebas público: https://hapi.fhir.org/

\---

*Este documento es una referencia conceptual. La implementación técnica detallada requiere participación de ingenieros de sistemas de salud certificados en FHIR.*

