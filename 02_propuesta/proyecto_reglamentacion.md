# Proyecto de Reglamentación — Historia Clínica Única (HCU)

### Propuesta para complementar y acelerar la Ley 2015 de 2020

**Autor:** Isael Quintero  
**Fecha de elaboración:** Abril 2026  
**Versión:** 1.0  
**Estado:** Borrador para consulta política y técnica

\---

## Contexto y justificación

La Ley 2015 de 2020 y la Resolución 1888 de 2022 establecieron la Historia Clínica Electrónica Interoperable (HCEI) en Colombia. Sin embargo, cuatro años después de su promulgación, la implementación es fragmentaria, carece de plazos perentorios, no define sanciones ejecutables y deja por fuera a gran parte de los prestadores privados.

**Esta propuesta no crea una nueva ley. Reglamenta y le da dientes a la que ya existe**, estableciendo cronograma, arquitectura técnica, modelo de gobernanza y sanciones creíbles.

### El costo de no actuar

* Millones de exámenes duplicados anualmente por falta de acceso al historial del paciente.
* Eventos adversos graves y muertes evitables por decisiones clínicas sin información completa.
* Datos médicos retenidos por EPS e IPS como activo propio, no como derecho del ciudadano.
* Imposibilidad de construir epidemiología confiable para políticas públicas de salud.

\---

## Pilar 1 — Identidad única e inequívoca

### 1.1 Identificador único

La HCU se vinculará al número de identificación ciudadana:

* **Colombianos:** Cédula de ciudadanía, tarjeta de identidad o registro civil de nacido vivo.
* **Extranjeros:** Documento de identidad válido en Colombia (cédula de extranjería, pasaporte).

### 1.2 Creación automática al nacer

Todo nacido vivo registrado ante el DANE/Registraduría genera de inmediato su HCU.

* El sistema tomará los datos del Certificado de Nacido Vivo (CNV) para abrir el registro.
* El registro solo se cerrará con la inscripción del certificado de defunción.
* Integración automática con el Sistema Nacional de Registro Civil.

### 1.3 Continuidad vitalicia

La HCU acompañará al ciudadano a lo largo de toda su vida, independientemente de:

* El prestador que lo atienda (público o privado).
* La EPS a la que esté afiliado o si está en régimen subsidiado, contributivo o vinculado.
* El municipio, departamento o país donde se encuentre.

\---

## Pilar 2 — Propiedad, privacidad y acceso

### 2.1 El dueño es el paciente

La HCU no pertenece a ninguna EPS, IPS, profesional de la salud ni entidad del Estado.
Es un dato personalísimo del ciudadano, inalienable e imprescriptible.

### 2.2 Acceso bajo autorización explícita

* Todo acceso requiere consentimiento explícito del paciente.
* **Excepción de emergencia vital:** En situaciones de inconsciencia o urgencia extrema, el profesional de salud podrá acceder bajo el principio de *"autorización tácita por incapacidad temporal"*, quedando registrado el acceso con justificación clínica.

### 2.3 Log inmodificable de accesos

Cada consulta, actualización o lectura de la HCU debe quedar registrada en una bitácora inmodificable que incluya:

* Identidad del profesional o sistema que accedió.
* Fecha, hora y ubicación geográfica del acceso.
* Tipo de acción realizada (lectura, escritura, actualización).
* Justificación clínica cuando aplique.

Este log será visible para el paciente en tiempo real.

### 2.4 Datos sensibles con protección reforzada

Los siguientes tipos de información requerirán un segundo factor de autenticación o permiso especial explícito del paciente, incluso entre profesionales:

* Salud mental y psiquiatría.
* VIH/SIDA y enfermedades de transmisión sexual.
* Interrupción Voluntaria del Embarazo (IVE).
* Historial de adicciones.
* Datos genéticos.

### 2.5 Habeas data fortalecido

El paciente podrá en todo momento:

* Ver en tiempo real quién ha consultado su HCU.
* Descargar su HCU completa en formato estándar (FHIR/JSON o PDF).
* Solicitar correcciones documentadas ante errores de registro.
* Revocar autorizaciones de acceso no urgentes.

### 2.6 Prohibición expresa de uso discriminatorio

Los datos de la HCU **no podrán ser usados** por ninguna EPS para:

* Selección de riesgos o negación de servicios.
* Discriminación en la afiliación o en la UPC.
* Fines distintos a la atención clínica directa, salvo consentimiento anónimo y específico para investigación.

\---

## Pilar 3 — Arquitectura técnica y modelo de interoperabilidad

### 3.1 Modelo federado (no centralización gigante)

La HCU **no es una única base de datos en servidores del Gobierno**. Es un ecosistema federado compuesto por:

* Un **Repositorio Central de Índices (RCI):** sabe dónde están los datos de cada paciente, pero no los almacena todos.
* **Plataforma Nacional de Interoperabilidad (PNI):** capa de intercambio que conecta los sistemas existentes mediante APIs estandarizadas. Modelo Health Information Exchange (HIE).
* **Bases de datos locales de los operadores:** cada EPS e IPS puede conservar su sistema actual, siempre que publique y consuma datos en FHIR a través de la PNI.

Este modelo elimina la principal resistencia política: nadie pierde su inversión en sistemas ni "regala" sus datos.

### 3.2 Estándar obligatorio: HL7 FHIR R4

* Lenguaje común de intercambio entre todos los actores.
* El Ministerio de Salud publicará los **Perfiles Colombianos FHIR** (adaptaciones nacionales del estándar).
* El Estado proveerá **adaptadores/APIs gratuitos** para sistemas legados y consultorios sin plataforma, eliminando la barrera económica para pequeños prestadores.

### 3.3 Núcleo mínimo vital centralizado

Una base de datos centralizada solo contendrá la información mínima necesaria para una urgencia sin conectividad o sin autorización del sistema origen:

* Alergias graves documentadas.
* Grupo sanguíneo y factor RH.
* Condiciones crónicas activas.
* Medicamentos activos y dosis.
* Últimos tres eventos de atención de urgencias.
* Contacto de emergencia.

### 3.4 Seguridad y soberanía de datos

* Servidores en territorio colombiano o bajo acuerdos de nivel de servicio equivalentes con garantías legales de soberanía.
* Cifrado en tránsito (TLS 1.3) y en reposo (AES-256).
* Doble factor de autenticación para todos los profesionales de la salud.
* Certificación digital del talento humano en salud (firma electrónica avanzada vinculada al RETHUS).
* Auditorías de seguridad semestrales por entidad certificada independiente.

\---

## Pilar 4 — Plan de transición en dos años

### Fase 1: Fundamentos (Meses 0–6)

**Responsable principal:** MinSalud + MinTIC

|Hito|Plazo|
|-|-|
|Expedición de la reglamentación técnica completa|Mes 2|
|Creación de la Agencia/Unidad de HCU dentro de Supersalud|Mes 3|
|Publicación de Perfiles Colombianos FHIR y guías de implementación|Mes 4|
|Lanzamiento del sandbox de pruebas para desarrolladores|Mes 4|
|Afiliación obligatoria de todos los actores al sistema|Mes 6|
|Lanzamiento del piloto regional (mínimo una región)|Mes 6|

**Consecuencia automática de incumplimiento:** Si al mes 6 no se ha expedido la reglamentación técnica, los recursos del Fondo HCU quedan congelados hasta su emisión.

### Fase 2: Grandes prestadores (Meses 6–18)

**Responsable principal:** EPS grandes + IPS de alta complejidad

|Hito|Criterio de aplicación|
|-|-|
|Integración de sistemas a la PNI|EPS con más de 500.000 afiliados e IPS de alta complejidad|
|Volcado de información retrospectiva (mínimo últimos 5 años)|Mismos actores|
|Todo nuevo episodio clínico registrado en el nuevo modelo|Todos los actores habilitados|
|Interoperabilidad obligatoria para urgencias y ambulancias|Todo el territorio nacional|

### Fase 3: Universalización (Meses 18–24)

|Hito|Descripción|
|-|-|
|Incorporación de todos los prestadores restantes|Incluyendo consultorios independientes y medicina prepagada|
|HCU obligatoria para toda atención|A partir del mes 24, sin excepción|
|Programa de digitalización de registros en papel|Financiamiento mixto Estado-operadores|
|Indexación de metadatos de documentos históricos|Para saber que existen y dónde, aunque no estén digitalizados|

\---

## Pilar 5 — Gobierno, financiación y sanciones

### 5.1 Estructura de gobierno

|Entidad|Rol|
|-|-|
|**MinSalud**|Define políticas, estándares y perfiles FHIR colombianos|
|**Superintendencia de Salud**|Vigila cumplimiento, impone sanciones|
|**Oficina Técnica PNI** (dentro de MinSalud o MinTIC)|Desarrolla y mantiene la plataforma nacional de interoperabilidad|
|**ADRES**|Coordina integración con flujos de financiamiento del sistema|
|**SIC (Superindustria)**|Valida diseño de privacidad y protección de datos|

### 5.2 Financiación

* Presupuesto General de la Nación (partida específica).
* Regalías para Ciencia, Tecnología e Innovación (CTI).
* Cooperación internacional: BID, Banco Mundial, PAHO/OPS.
* Contribución por transacción mínima a cargo de EPS (dentro de la UPC existente, sin costo adicional al paciente).
* **El pequeño consultorio no asume costo**: adaptadores y APIs estatales gratuitos.

### 5.3 Sanciones creíbles y automáticas

**Para incumplimiento de hitos:**

* Multas diarias escalonadas según tamaño del actor (calculadas sobre la UPC o los ingresos operacionales).
* Suspensión temporal de la habilitación para nuevos contratos públicos.
* Responsabilidad fiscal personal para representantes legales.

**Para violaciones de privacidad o uso discriminatorio:**

* Multas equivalentes a las previstas en la Ley 1581 de 2012 (Habeas Data), amplificadas por factor de sensibilidad médica.
* Exposición pública del infractor (name and shame).
* Cancelación de habilitación en casos graves.

### 5.4 Incentivos positivos

* Puntaje adicional en procesos de contratación pública para actores que migren antes del plazo.
* Reconocimiento público de "Prestador con HCU certificada".
* Acceso preferencial a financiamiento de modernización tecnológica.

\---

## Estrategia política

### 1\. Anclaje en el Congreso

Buscar un autor en la Comisión Séptima con peso específico. La iniciativa debe presentarse como:

* El **brazo tecnológico** de cualquier reforma a la salud, independiente del color político.
* Un tema de **consenso transversal**: la HC única no es de izquierda ni de derecha; es eficiencia y seguridad del paciente.

**Congresistas priorizados:**

1. Honorio Miguel Henríquez Pineda (Comisión VII, ángulo de eficiencia y ahorro)
2. Nadia Georgette Blel Scaff (peso político, Caribe)
3. Norma Hurtado Sánchez (ponente original de la Ley 2015)
4. Agmeth José Escaf Tijerino (perfil mediático, Caribe)
5. Alfredo Mondragón Garzón (Comisión VII Cámara)
6. Carolina Corcho (mayor peso técnico)

### 2\. Framing ciudadano, no industrial

**No:** "Un proyecto para que las EPS compartan datos."  
**Sí:** "El derecho a que mi historia clínica me salve la vida donde sea que yo caiga."

Aliados clave:

* Veedurías ciudadanas en salud.
* Asociaciones de pacientes (cáncer, enfermedades huérfanas, crónicos).
* Sociedades científicas: medicina de urgencias, medicina interna, pediatría.
* Defensor del Pueblo.

### 3\. Neutralización de la oposición anticipada

|Actor opositor|Argumento de resistencia|Respuesta técnica|
|-|-|-|
|EPS e IPS grandes|"Perderemos el control de 'nuestros' datos"|Modelo federado: conservan sus sistemas; los datos son del paciente, no los pierden|
|Asociaciones médicas|"Nos fiscalizarán con la HC"|Cláusula expresa: datos solo para fines asistenciales; no para negar servicios|
|MinTIC / SIC|"Problemas de privacidad"|SIC integrada desde el diseño para validar la arquitectura|
|Pequeños consultorios|"No tenemos plataforma ni presupuesto"|Adaptadores y APIs estatales gratuitos|

### 4\. Piloto regional como detonador

Antes de la aprobación legislativa, construir un **piloto en el departamento del Atlántico y Barranquilla** con:

* Una o dos EPS con presencia regional.
* La red de urgencias hospitalarias del departamento.
* Alcaldía de Barranquilla + Gobernación del Atlántico como avalistas.

**Objetivo del piloto:** Documentar al menos un caso donde la HCU interoperable evitó un evento adverso grave (ej: médico de urgencias accede a alergias documentadas antes de prescribir). Ese caso se convierte en el corazón de la exposición de motivos del proyecto de ley.

\---

## Perfil del autor

Isael Quintero  
Barranquilla, Atlántico, Colombia

* Profesional en Administración de Negocios — Universidad Autónoma del Caribe.
* 30+ años de experiencia en procesos comerciales, administrativos y operativos.
* Experiencia en gestión de inventarios, personal, datos y automatización (Python, SQL, Excel avanzado).
* Consultor independiente en automatización de datos — QuinCon TIC.
* Ninguna agenda partidista. Perfil técnico y de implementación.

\---

*Versión 1.0 — Abril 2025. Este documento puede evolucionar. Todas las versiones quedan registradas en el historial de commits de este repositorio.*

