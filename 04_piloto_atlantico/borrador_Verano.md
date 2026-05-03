# Documento de Enganche — Eduardo Verano de la Rosa
## Gobernador del Atlántico
### Proyecto HCU Colombia — Piloto Regional Atlántico

---

**Para:** Dr. Eduardo Verano de la Rosa, Gobernador del Atlántico
**De:** Isael Quintero — Consultor independiente, QuinCon TIC
**Fecha:** Mayo 2026
**Asunto:** Atlántico como territorio piloto de Historia Clínica Única interoperable — propuesta técnica

---

## El Atlántico puede liderar la transformación del sistema de salud colombiano

La fragmentación de los datos médicos es uno de los problemas más costosos y menos visibles del sistema de salud colombiano. Un paciente del Atlántico atendido en Soledad no lleva sus datos cuando es remitido al hospital de Barranquilla. Un trabajador de Sabanalarga que llega a urgencias en la capital del departamento es, para ese médico, un desconocido clínico.

Ese vacío tiene consecuencias directas: errores de medicación evitables, exámenes duplicados que desperdician recursos públicos, incapacidad para hacer vigilancia epidemiológica confiable en el departamento.

**La Ley 2015 de 2020 ya establece la solución. El Atlántico puede ser el primer departamento en implementarla.**

---

## La propuesta: piloto departamental de HCU

Un piloto técnico de Historia Clínica Única (HCU) interoperable en el Atlántico, usando el estándar internacional HL7 FHIR R4 — adoptado oficialmente por MinSalud.

### Principios del modelo
- **Arquitectura federada:** no una base de datos centralizada. Cada IPS y EPS conserva su sistema. Se implementan conectores de interoperabilidad sobre estándar abierto. Bajo costo, alta escalabilidad.
- **Propiedad del paciente:** la HC no pertenece a ninguna institución. Es un derecho del ciudadano.
- **Identidad única:** vinculada a la cédula o registro civil desde el nacimiento.

### Actores propuestos para el piloto
- Hospital Universidad del Norte (nodo técnico de alta complejidad)
- ESE Hospital Niño Jesús (red pública pediátrica)
- Cruz Roja Colombiana — Atlántico (prehospitalario)
- Red de IPS municipales del departamento
- Uninorte / UTBN (desarrollo de adaptadores FHIR y evaluación académica)
- 1-2 EPS con cobertura departamental

---

## Ángulo de política pública departamental

### Salud pública y epidemiología
Con una HC interoperable departamental, la Secretaría de Salud del Atlántico tendría por primera vez un mapa real y actualizado de las condiciones crónicas, enfermedades prevalentes y riesgos epidemiológicos de la población — por municipio, por edad, por estrato. Eso transforma la capacidad de respuesta ante brotes y emergencias sanitarias.

### Regalías e inversión CTI
Este piloto califica para financiamiento con recursos del **Sistema General de Regalías — Ciencia, Tecnología e Innovación (CTI)**. Un proyecto de innovación en salud digital con impacto departamental medible, respaldo técnico universitario y estándar internacional es exactamente el perfil que los comités de CTI priorizan.

### Posicionamiento del Atlántico
Un piloto exitoso convierte al Atlántico en el referente nacional de interoperabilidad en salud — con un caso documentado que el Congreso y MinSalud necesitan para acelerar la reglamentación nacional de la Ley 2015.

---

## Lo que ya existe — el prototipo funcional

No es una propuesta en papel. Existe un MVP técnico operativo que puede demostrarse en vivo:

- Servidor HAPI FHIR con dos instancias que simulan EPS e IPS del departamento.
- 100 pacientes ficticios con historiales clínicos en formato FHIR colombiano oficial.
- Visor de urgencias que demuestra el caso de éxito:

> Médico de urgencias → paciente remitido de otro municipio → busca por cédula → sistema alerta: *"Alérgico a penicilina — reacción severa documentada en IPS de origen"* → Se evitó un evento adverso grave.

**20 minutos de demostración en vivo** valen más que cualquier exposición de motivos.

---

## Financiamiento — opciones concretas

| Fuente | Mecanismo | Viabilidad |
|---|---|---|
| Regalías CTI | Proyecto CTI departamental — salud digital | Alta |
| MinSalud | Alianza técnica — implementación Ley 2015 | Media-Alta |
| Cooperación internacional | OPS/OMS tienen líneas de financiamiento para HCE | Media |
| Universidades | Convenios de investigación aplicada | Alta |

---

## Lo que solicitamos

1. Una reunión de trabajo con la Secretaría de Salud Departamental y el equipo de TIC de la Gobernación.
2. Demostración en vivo del prototipo técnico.
3. Exploración de la figura jurídica para el respaldo institucional de la Gobernación al piloto.

---

## Sobre el autor

**Isael Quintero** — Administrador de Empresas (UAC), consultor independiente en automatización de datos y procesos (QuinCon TIC). Desarrollador del prototipo técnico y la propuesta de reglamentación. Barranquillero.

Repositorio público: `github.com/IsaelDJQuinteroF-Dev/hcu-colombia`

---

*"El derecho a que mi historia clínica me salve la vida donde sea que yo caiga."*

---

*Mayo 2026 — Documento de enganche. Reservado para gestión del piloto regional.*
