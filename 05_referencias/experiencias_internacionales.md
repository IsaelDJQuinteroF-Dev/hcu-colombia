# Experiencias Internacionales — Historia Clínica Única e Interoperable

### Casos de referencia para el Proyecto HCU Colombia

**Compilado por:** Isael Quintero | Abril 2026

\---

## Por qué mirar afuera

Colombia no está inventando la rueda. Más de 30 países han implementado sistemas de HC interoperable o única con resultados documentados. Conocer sus aciertos y errores acorta el camino y blinda la propuesta ante cuestionamientos técnicos.

\---

## Casos destacados

\---

### 🇪🇪 Estonia — El modelo más citado del mundo

**Sistema:** X-Road + Tervise infosüsteem (Sistema de Información de Salud)  
**Desde:** 2008  
**Cobertura:** \~1,3 millones de habitantes (toda la población)

**Lo que hicieron:**
Estonia construyó una infraestructura nacional de intercambio de datos (X-Road) que conecta todos los sistemas públicos y privados. La HC del paciente no está en un solo lugar: cada prestador conserva sus datos, pero X-Road sabe dónde están y los mueve bajo demanda con consentimiento.

**Resultados documentados:**

* El 99% de las recetas médicas se expide digitalmente.
* Un médico de urgencias accede al historial completo del paciente en segundos.
* El paciente puede ver en tiempo real quién ha consultado su HC.
* Ahorro estimado: el equivalente al 2% del PIB anual en eficiencia del sistema público.

**Lección para Colombia:** El modelo federado funciona incluso a escala nacional. No se necesita una base de datos gigante centralizada.

\---

### 🇦🇺 Australia — My Health Record

**Sistema:** My Health Record (anteriormente PCEHR)  
**Desde:** 2012 (relanzado 2018)  
**Cobertura:** \~23 millones de habitantes

**Lo que hicieron:**
Crearon un repositorio nacional opt-out (todos incluidos automáticamente, salvo que se excluyan). Cada australiano tiene un registro accesible por cualquier profesional de salud autorizado, en cualquier punto del territorio.

**Resultados documentados:**

* Reducción significativa de exámenes duplicados en urgencias.
* Acceso a alergias y medicamentos activos en emergencias.
* Usado en más del 85% de las consultas de médicos generales.

**Errores cometidos:**

* La primera versión (2012-2018) tuvo baja adopción por ser opt-in y tener interfaz difícil.
* Controversia por acceso de terceros sin consentimiento claro del paciente (resuelta en 2018 con reforma legal).

**Lección para Colombia:** El opt-out (todos incluidos desde el nacimiento) funciona mejor que el opt-in. La interfaz del paciente debe ser simple. La privacidad debe ser irrenunciable.

\---

### 🇩🇰 Dinamarca — Sundhed.dk

**Sistema:** Sundhed.dk (portal nacional de salud)  
**Desde:** 2003  
**Cobertura:** \~6 millones de habitantes

**Lo que hicieron:**
Un portal único donde el ciudadano accede a toda su información de salud: resultados de laboratorio, medicamentos, vacunas, derivaciones. Los profesionales acceden desde cualquier punto del sistema con autenticación fuerte.

**Resultados documentados:**

* 95% de los médicos de cabecera usan el sistema en cada consulta.
* El paciente puede ver cada consulta, resultado y prescripción en tiempo real.
* Reducción de errores de medicación documentada.

**Lección para Colombia:** El portal del paciente debe ser el producto visible y tangible del sistema. Es lo que genera apropiación ciudadana y apoyo político.

\---

### 🇦🇷 Argentina — Ley 27.706 de 2023

**Sistema:** Historia Clínica Electrónica Única Nacional (en implementación)  
**Desde:** Ley aprobada en 2023, implementación en curso

**Lo que hicieron:**
Argentina aprobó en 2023 una ley muy similar a lo que este proyecto propone para Colombia: HC única, propiedad del paciente, interoperable, con plazos de implementación. Es el caso latinoamericano más directo de referencia.

**Estado actual (2025):**
Implementación parcial. Los grandes prestadores del AMBA (Área Metropolitana de Buenos Aires) están avanzando; el interior del país va más lento.

**Errores en curso:**

* Los plazos iniciales ya se incumplieron sin consecuencias.
* Falta de financiamiento específico para pequeños prestadores.
* Sin estándar técnico único aprobado aún.

**Lección para Colombia:** Repetir exactamente los errores argentinos (plazos sin sanciones, sin financiamiento para pequeños) condena el proyecto al mismo resultado. La propuesta colombiana debe aprender de esto: hitos con consecuencias automáticas y adaptadores gratuitos para consultorios.

\---

### 🇺🇸 Estados Unidos — 21st Century Cures Act (2020)

**Sistema:** Interoperabilidad obligatoria + prohibición de "information blocking"  
**Desde:** 2020 (implementación escalonada hasta 2023)

**Lo que hicieron:**
La ley federal prohibió expresamente que los prestadores y EPS (payers) bloqueen el acceso del paciente a su información clínica. Obligó a todos los sistemas a publicar APIs FHIR R4 abiertas al paciente y a desarrolladores.

**Resultados documentados:**

* Hoy, cualquier app móvil certificada puede conectarse al sistema de salud de un paciente con su consentimiento.
* Multas millonarias a prestadores que bloquearon información.
* El mercado de aplicaciones de salud del paciente creció exponencialmente.

**Lección para Colombia:** La prohibición del "secuestro de datos" por parte de las EPS debe ser explícita en la norma, con sanciones tan claras como las estadounidenses. Eso es lo que blinda al paciente.

\---

## Tabla comparativa de modelos

|País|Modelo|Estándar|Cobertura|Propiedad del paciente|Sanción por incumplimiento|
|-|-|-|-|-|-|
|Estonia|Federado (X-Road)|Propio + HL7|100%|Sí, con log en tiempo real|Sí|
|Australia|Repositorio nacional opt-out|HL7 FHIR|95%+|Sí|Sí|
|Dinamarca|Portal único + datos distribuidos|Estándar nacional|100%|Sí|Sí|
|Argentina|Federado (en proceso)|En definición|Parcial|En norma, no en práctica|No efectiva|
|EE.UU.|APIs abiertas + prohibición de bloqueo|HL7 FHIR R4|Amplia|Sí, reforzada por ley|Sí, multas altas|
|**Colombia (propuesta)**|**Federado + índice central**|**HL7 FHIR R4**|**100% (meta 24 meses)**|**Sí, con log inmodificable**|**Sí, automáticas**|

\---

## Conclusión

El mundo ya tiene el camino trazado. Colombia puede llegar más rápido y mejor que Argentina porque:

1. Ya tiene la Ley 2015 como base.
2. Puede adoptar FHIR R4 directamente sin estándar intermedio.
3. Puede aprender de los errores ajenos (plazos sin dientes, financiamiento insuficiente, sin portal del paciente).

La propuesta HCU Colombia recoge lo mejor de Estonia (modelo federado), Australia (opt-out desde el nacimiento), Dinamarca (portal del paciente) y EE.UU. (prohibición del bloqueo de datos) — adaptado a la realidad jurídica, técnica y política colombiana.

\---

*Ver propuesta completa en: `../02\\\_propuesta/proyecto\\\_reglamentacion.md`*

