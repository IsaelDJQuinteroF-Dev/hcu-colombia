# Documento de Enganche — Ana María Aljure
## Gerente de Ciudad — Alcaldía de Barranquilla
### Proyecto HCU Colombia — Piloto Regional Atlántico

---

**Para:** Dra. Ana María Aljure
**De:** Isael Quintero — Consultor independiente, QuinCon TIC
**Fecha:** Mayo 2026
**Asunto:** Propuesta de piloto técnico — Historia Clínica Única interoperable en Barranquilla

---

## El problema que podemos resolver juntos

Hoy, cuando un ciudadano barranquillero llega a urgencias inconsciente, el médico no sabe si es alérgico a la penicilina — a menos que lo haya atendido antes en esa misma IPS. Sus datos médicos están fragmentados entre la EPS, la clínica privada, el médico de cabecera y la red pública. No viajan con él.

Ese vacío cuesta vidas. Y cuesta dinero: exámenes duplicados, errores de medicación, imposibilidad de hacer epidemiología confiable en la ciudad.

**La buena noticia:** la ley ya existe. La Ley 2015 de 2020 establece la Historia Clínica Electrónica Interoperable. **Lo que falta es la reglamentación con dientes y un piloto que demuestre que funciona.**

---

## La propuesta

Convertir a Barranquilla en la **primera ciudad de Colombia con un piloto funcional de Historia Clínica Única (HCU) interoperable**, usando el estándar internacional HL7 FHIR R4 — el mismo que ya adoptó MinSalud oficialmente.

No es una nueva ley. Es la implementación técnica de lo que ya es obligatorio.

### Los cinco pilares
1. **Identidad única:** HC vinculada a la cédula. Se abre al nacer, se cierra al morir.
2. **Propiedad del paciente:** No pertenece a ninguna EPS ni IPS. Es un derecho personalísimo del ciudadano.
3. **Arquitectura federada:** No una base de datos centralizada. Cada prestador conserva su sistema pero comparte datos vía APIs FHIR estándar. Seguro, escalable, sin dependencia de un proveedor único.
4. **Plan de dos años:** Tres fases con hitos medibles y consecuencias automáticas por incumplimiento.
5. **Gobierno claro:** MinSalud define, Supersalud vigila, el paciente es el centro.

---

## Por qué Barranquilla — y por qué ahora

Barranquilla tiene el ecosistema perfecto para este piloto:

- **Hospital Universidad del Norte** — alta complejidad, capacidad técnica, nodo natural del piloto.
- **ESE Hospital Niño Jesús** — red pública pediátrica, alto volumen, impacto social visible.
- **Cruz Roja Colombiana Atlántico** — prehospitalario y ambulancias, el eslabón más crítico.
- **Uninorte / UTBN** — universidades con capacidad para desarrollar adaptadores FHIR.
- **Infraestructura digital** — Barranquilla ya lidera en gobierno digital en Colombia.

Un piloto exitoso aquí no es solo un logro local. Es el caso documentado que el Congreso necesita para acelerar la reglamentación nacional. **Es Barranquilla poniendo el estándar para el país.**

---

## Lo que ya existe — el prototipo funcional

No llegamos con una idea en PowerPoint. Existe un MVP técnico operativo que demuestra interoperabilidad real:

- Servidor **HAPI FHIR** levantado localmente, con dos instancias que simulan EPS e IPS.
- 100 pacientes ficticios con historiales clínicos realistas en formato FHIR colombiano.
- **Visor de urgencias**: un médico busca por cédula y recibe en segundos las alergias críticas, condiciones crónicas y medicamentos activos del paciente — aunque haya sido atendido en otra institución.

**El caso de éxito que el prototipo demuestra:**
```
Médico de urgencias → paciente inconsciente → busca por cédula
→ 🚨 ALERTA: "Alérgico a PENICILINA — reacción severa documentada"
→ Médico cambia prescripción
→ Se evitó una muerte
```

Ese momento en pantalla es la exposición de motivos del proyecto.
Podemos hacerle una demostración en vivo en 20 minutos.

---

## Lo que solicitamos

1. **Una reunión de 30 minutos** para demostración en vivo del prototipo.
2. **Apertura para explorar** la vinculación de la Alcaldía como promotor institucional del piloto regional.
3. **Contacto con las IPS de la red pública** para evaluar participación en la fase inicial.

---

## Impacto proyectado del piloto

| Indicador | Meta piloto (12 meses) |
|---|---|
| Pacientes con HC interoperable | 10,000 |
| IPS/EPS participantes | 5-7 |
| Eventos adversos evitados (estimado) | 50-100 |
| Exámenes duplicados evitados | 15-20% de la base piloto |
| Costo de implementación | Mínimo — infraestructura existente + estándar abierto |

---

## Sobre el autor

**Isael Quintero** — Administrador de Empresas (UAC), consultor independiente en automatización de datos y procesos (QuinCon TIC). Desarrollador del prototipo técnico y la propuesta de reglamentación. Barranquillero.

Repositorio público del proyecto: `github.com/IsaelDJQuinteroF-Dev/hcu-colombia`

---

*"El derecho a que mi historia clínica me salve la vida donde sea que yo caiga."*

---

*Documento preparado en mayo de 2026. Confidencial — para uso en gestión del piloto regional.*
