# Propuesta de Piloto Regional — Historia Clínica Única

## Departamento del Atlántico y Distrito de Barranquilla

**Autor:** Isael Quintero | Barranquilla, Atlántico, Colombia  
**Versión:** 1.0 — Abril 2026

\---

## ¿Por qué un piloto antes de la ley?

Un piloto regional cumple tres funciones estratégicas simultáneas:

1. **Evidencia técnica:** Demuestra que el modelo federado con FHIR es implementable con la infraestructura existente.
2. **Argumento político:** Un caso documentado de evento adverso evitado gracias a la HC interoperable vale más que cualquier exposición de motivos.
3. **Presión legislativa:** Un piloto exitoso convierte a la Gobernación, la Alcaldía y las EPS participantes en aliados activos del proyecto de ley.

\---

## Alcance propuesto del piloto

### Población objetivo

* Pacientes atendidos en la red de urgencias del Área Metropolitana de Barranquilla y/o el departamento del Atlántico
* Fase inicial: mínimo 50.000 registros activos.

### Actores clave a vincular

|Actor|Rol en el piloto|
|-|-|
|**Gobernación del Atlántico**|Aval político, financiamiento parcial, coordinación institucional|
|**Alcaldía de Barranquilla**|Red de hospitales distritales y ESEs|
|**Hospital Universidad del Norte**|IPS de alta complejidad — nodo técnico principal|
|**ESE Hospital Niño Jesús**|Red pública de referencia pediátrica|
|**1-2 EPS con presencia regional**|(por definir: Sura, Nueva EPS, Coosalud)|
|**Cruz Roja Colombiana — Atlántico**|Red de ambulancias y atención prehospitalaria|
|**Uninorte / UTBN**|Soporte técnico universitario, desarrollo de adaptadores FHIR|

\---

## Objetivo principal del piloto

> Demostrar que un médico de urgencias en Barranquilla puede acceder, en tiempo real y con autorización, al historial clínico relevante de un paciente atendido previamente en cualquier prestador participante del piloto.

### Caso de éxito mínimo a documentar

Un evento donde el acceso a la HC interoperable evitó un evento adverso grave:

* Prescripción de un medicamento al que el paciente era alérgico.
* Duplicación de un procedimiento diagnóstico costoso e innecesario.
* Decisión clínica incorrecta por desconocimiento de condición crónica activa.

**Ese caso documentado se convierte en el corazón de la exposición de motivos del proyecto de ley.**

\---

## Arquitectura técnica del piloto

```
\[EPS Participante A]          \[Hospital Distrital B]
       |                              |
       |------- API FHIR R4 ----------|
                    |
          \[Plataforma de Intercambio Piloto]
          (Health Information Exchange local)
                    |
          \[Índice Central de Pacientes]
          (solo metadatos + núcleo mínimo vital)
                    |
          \[Portal del Paciente]
          (acceso web/móvil a su propia HC)
```

* Estándar: **HL7 FHIR R4**
* Adaptadores gratuitos para sistemas legados
* Log inmodificable de todos los accesos
* Cifrado en tránsito y en reposo

\---

## Plan de ejecución

|Fase|Duración|Actividades principales|
|-|-|-|
|**Diseño**|Mes 1-2|Firma de acuerdos, definición técnica, perfiles FHIR colombianos del piloto|
|**Desarrollo**|Mes 2-4|Integración de sistemas, adaptadores, portal del paciente|
|**Piloto controlado**|Mes 4-6|Red de urgencias de 3-4 IPS, grupo de \~5.000 pacientes, monitoreo continuo|
|**Expansión**|Mes 6-12|Incorporación de todos los actores firmantes, 50.000+ pacientes|
|**Evaluación y reporte**|Mes 12|Documento de resultados para el Congreso y MinSalud|

\---

## Indicadores de éxito

|Indicador|Meta al mes 12|
|-|-|
|Prestadores integrados|≥ 5|
|Pacientes con HC interoperable activa|≥ 50.000|
|Consultas exitosas entre prestadores|≥ 10.000|
|Eventos adversos documentados evitados|≥ 1 caso verificado|
|Reducción de exámenes duplicados en urgencias|≥ 15%|
|Satisfacción del profesional de salud con el sistema|≥ 70%|

\---

## Financiamiento estimado del piloto

|Rubro|Fuente sugerida|
|-|-|
|Plataforma de intercambio (desarrollo e infraestructura)|Gobernación + Alcaldía + cooperación técnica|
|Adaptadores FHIR para IPS|Regalías CTI del Atlántico|
|Soporte universitario (Uninorte/UTBN)|Convenio de investigación aplicada|
|Coordinación técnica del proyecto|Proponente (Isael Quintero — QuinCon TIC)|

\---

## Por qué el Atlántico es el lugar ideal

* Barranquilla concentra infraestructura hospitalaria de alta complejidad y una red de urgencias articulada.
* El departamento tiene antecedentes de adopción tecnológica en salud pública.
* Presencia de universidades con capacidad técnica en TI y salud (Uninorte, UTBN, CUC).
* Liderazgo político regional con proyección nacional — un éxito aquí tiene visibilidad nacional inmediata.
* El autor del proyecto es barranquillero, con redes locales y sin conflicto de interés con actores nacionales.

\---

## Próximos pasos para activar el piloto

1. Reunión inicial con la Secretaría de Salud del Atlántico.
2. Reunión inicial con la Secretaría Distrital de Salud de Barranquilla.
3. Identificar la EPS con mayor disposición y presencia regional.
4. Presentar el piloto al congresista o presidenciable que avale el proyecto como vitrina regional.
5. Gestionar cooperación técnica con BID/OPS para financiamiento parcial.

\---

*Ver propuesta legislativa completa en: `../02\_propuesta/proyecto\_reglamentacion.md`*

