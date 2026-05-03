# BRIEFING MAESTRO — Proyecto HCU Colombia
### Documento de continuidad para nuevas sesiones de trabajo

**Autor del proyecto:** Isael Quintero — Barranquilla, Atlántico, Colombia
**Perfil:** Administrador de negocios (UAC), 30+ años experiencia comercial/operativa, Python, SQL, Excel avanzado, consultor independiente QuinCon TIC. Pensionado. Buscando empleo remoto en paralelo.
**Última actualización:** Mayo 2026

---

## 1. QUÉ ES Y PARA QUÉ SIRVE

### El problema
Los datos médicos de un colombiano están fragmentados en cada EPS, clínica o consultorio. No viajan con el paciente. Un médico de urgencias no sabe si su paciente es alérgico a la penicilina si fue atendido en otro prestador. Eso cuesta vidas y dinero (exámenes duplicados, errores médicos, imposibilidad de hacer epidemiología confiable).

### La propuesta
**No es una nueva ley.** Es la reglamentación con dientes de la **Ley 2015 de 2020** (Historia Clínica Electrónica Interoperable), que ya existe pero carece de plazos perentorios, sanciones ejecutables, modelo de gobernanza y financiamiento estructurado.

### Los cinco pilares
1. **Identidad única:** HC vinculada a la cédula. Se abre al nacer (desde el certificado de nacido vivo DANE/Registraduría), se cierra al morir.
2. **Propiedad del paciente:** La HC no pertenece a ninguna EPS ni IPS. Es un dato personalísimo del ciudadano con log inmodificable de accesos.
3. **Arquitectura federada + HL7 FHIR R4:** No una base de datos centralizada gigante. Un ecosistema interoperable donde cada prestador conserva su sistema pero publica/consume datos via APIs FHIR estándar. MinSalud ya publicó perfiles FHIR colombianos oficiales (RDA — Resumen Digital de Atención) en `fhir.minsalud.gov.co`.
4. **Plan de dos años en 3 fases:** Con hitos, cronograma y consecuencias automáticas por incumplimiento.
5. **Gobierno, financiación y sanciones:** MinSalud define, Supersalud vigila y sanciona. Multas diarias, suspensión de habilitación, incentivos positivos para quienes migren antes.

### Estrategia política central
- No competir con la reforma a la salud — ser su **brazo técnico**.
- Framing ciudadano: *"El derecho a que mi historia clínica me salve la vida donde sea que yo caiga."*
- Tema de consenso transversal: no es de izquierda ni de derecha.
- **No hacer la ley — reglamentar la que ya existe.**

---

## 2. QUÉ HAY HECHO

### Repositorio GitHub (privado)
`github.com/IsaelDJQuinteroF-Dev/hcu-colombia`

```
├── README.md                          ← Portada (recién corregida, pendiente subir)
├── LICENSE.md                         ← CC BY-NC-SA 4.0
├── 01_marco_legal/
│   ├── analisis_vacios_ley2015.md     ← 10 vacíos documentados de la ley vigente
│   └── referencias_normativas.md      ← Marco jurídico + derecho comparado
├── 02_propuesta/
│   └── proyecto_reglamentacion.md     ← Documento técnico completo (5 pilares)
├── 03_comunicaciones/
│   ├── borrador_Presidente_De_La_Espriella.md
│   ├── borrador_Senadora_Hurtado.md   ← URGENTE — ponente PL 410
│   ├── borrador_Senadora_Blel.md
│   ├── borrador_Senador_Henriquez.md
│   ├── borrador_Senador_Escaff.md
│   ├── borrador_Representante_Mondragon.md
│   ├── borrador_Dra_Valencia.md
│   ├── borrador_Senadora_Corcho.md    ← Última opción
│   └── registro_contactos.md
├── 04_piloto_atlantico/
│   └── propuesta_piloto_regional.md
└── 05_referencias/
    ├── estandar_hl7_fhir.md
    └── experiencias_internacionales.md
```

**Pendiente subir al repo:** carpeta `prototipo/` con los 5 archivos técnicos.

### Contactos realizados
| Destinatario | Estado |
|-------------|--------|
| Abelardo de la Espriella | ✅ Mensaje informal enviado (abril 2026). Sin respuesta aún. Si no responde esta semana → enviar borrador formal. |
| Norma Hurtado | ✅ Mensaje enviado (mayo 2026) referenciando PL 410 y prototipo. Pendiente respuesta. |
| Todos los demás | 📋 Pendiente |

### Estado legislativo crítico
Existe el **PL 410/2025 Senado — 312/2024 Cámara**: reforma integral al sistema de salud que incluye interoperabilidad de HC. **Norma Hurtado es la ponente coordinadora.** Fue archivado el 16 de diciembre de 2025 en Comisión VII pero está **apelado** — sigue vivo. Este es el vehículo legislativo más concreto. Isael no compite con este PL — lo complementa con la reglamentación técnica que le falta.

---

## 3. ESTRATEGIA PILOTO REGIONAL — ATLÁNTICO Y BARRANQUILLA

### Por qué el piloto
Un piloto exitoso = el mejor argumento político. Un caso documentado donde la HC interoperable evitó un evento adverso grave (ej: médico de urgencias detecta alergia crítica antes de prescribir) vale más que cualquier exposición de motivos.

### Actores políticos objetivo

| Actor | Cargo | Período | Contacto estratégico |
|-------|-------|---------|----------------------|
| **Alejandro Char Chaljub** | Alcalde de Barranquilla | 2023-2027 | Documento de alto nivel — político, breve, apela a legado |
| **Ana María Aljure** | Gerente de Ciudad — Alcaldía | 2023-2027 | **Contacto más firme.** Documento técnico-ejecutivo detallado. Es la precandidata más seria para la próxima alcaldía. |
| **Eduardo Verano** | Gobernador del Atlántico | 2023-2027 | Documento departamental — ángulo salud pública y regalías CTI |

**Pendiente:** Redactar los 3 documentos de enganche (Char, Aljure, Verano). Mismo formato que los borradores congresistas — personalizados por perfil.

### IPS/EPS objetivo para el piloto
- Hospital Universidad del Norte (alta complejidad, nodo técnico)
- ESE Hospital Niño Jesús (red pública pediátrica)
- Cruz Roja Colombiana — Atlántico (ambulancias, prehospitalario)
- 1-2 EPS con presencia regional (Sura, Nueva EPS, Coosalud — por definir)
- Apoyo universitario: Uninorte / UTBN (desarrollo adaptadores FHIR)

---

## 4. EL PROTOTIPO — TODO LO QUE HAY Y CÓMO EJECUTARLO

### Qué es
Un MVP (Producto Mínimo Viable) técnico que demuestra interoperabilidad real entre sistemas de salud usando HL7 FHIR R4. Está en la carpeta `prototipo/` del Drive de Isael.

### Archivos del prototipo

| Archivo | Qué hace |
|---------|----------|
| `docker-compose.yml` | Levanta servidor **HAPI FHIR** local (el servidor FHIR open-source más usado del mundo). Define dos instancias: una simula la EPS, otra simula la IPS — demostrando el modelo federado. |
| `hapi.application.yaml` | Configuración del servidor HAPI FHIR |
| `generar_datos_synthea.py` | Genera 100 pacientes ficticios con historiales clínicos realistas en formato FHIR y los carga al servidor. Usa nombres colombianos, cédulas ficticias, condiciones crónicas y alergias. |
| `requirements.txt` | Dependencias Python: `fhir.resources==8.0.1`, `fhirclient==4.1.0`, `requests==2.32.3`, `flask==3.1.0`, `pandas==2.2.3` |
| `paciente_visor.py` | App web Flask que simula la pantalla de urgencias. Busca paciente por cédula, muestra: alergias críticas (🚨 alerta roja), condiciones crónicas, medicamentos activos. Si hay alergia crítica → banner: *"El médico fue alertado ANTES de prescribir. Se evitó un evento adverso grave."* |

### El caso de éxito que demuestra
```
Médico de urgencias recibe paciente inconsciente
→ Busca por cédula en el visor
→ Sistema consulta HAPI FHIR (datos de otra IPS)
→ 🚨 ALERTA: "Paciente alérgico a PENICILINA — reacción severa documentada"
→ Médico cambia prescripción
→ Se evitó una muerte
```
**Ese momento en pantalla es la exposición de motivos del proyecto de ley.**

### Cómo ejecutar el prototipo — paso a paso

**Prerequisitos a instalar (en orden):**

**1. Docker Desktop**
- Descargar: `https://www.docker.com/products/docker-desktop/`
- Instalar con todas las opciones por defecto
- Verificar: abrir CMD y ejecutar `docker --version`

**2. Python 3.11+** (Isael ya lo tiene o está en proceso)
- Verificar: `python --version`

**3. Dependencias Python**
```bash
pip install fhir.resources==8.0.1 fhirclient==4.1.0 requests==2.32.3 flask==3.1.0 pandas==2.2.3
```

**Secuencia de ejecución:**

```bash
# Paso 1: Ir a la carpeta del prototipo
cd ruta/a/prototipo

# Paso 2: Levantar el servidor HAPI FHIR (tarda ~2 min la primera vez)
docker-compose up -d

# Paso 3: Verificar que el servidor está corriendo
# Abrir navegador en: http://localhost:8080

# Paso 4: Cargar los 100 pacientes ficticios
python generar_datos_synthea.py

# Paso 5: Lanzar el visor web
python paciente_visor.py

# Paso 6: Abrir el demo
# Abrir navegador en: http://localhost:5000
```

### Perfiles FHIR colombianos oficiales (MinSalud)
MinSalud ya publicó la Guía RDA (Resumen Digital de Atención) con perfiles FHIR colombianos:
- Portal: `https://vulcano.ihcecol.gov.co/`
- Paquete: `https://fhir.minsalud.gov.co/rda/package.tgz`
- Guía Core Colombia: `https://co.fhir.guide/core/` (versión 0.1.0)
- Perfiles disponibles: `PatientCO`, `PractitionerCO`, `AllergyIntoleranceCO`, `ConditionCO`

Esto significa que el estándar técnico ya existe oficialmente — solo falta la obligatoriedad.

---

## 5. PENDIENTES EN ORDEN DE PRIORIDAD

| Prioridad | Tarea | Detalle |
|-----------|-------|---------|
| 🔴 1 | **Instalar Docker Desktop** | Prerequisito para levantar el prototipo |
| 🔴 2 | **Subir carpeta prototipo a GitHub** | Crea `06_prototipo/` en el repo |
| 🔴 3 | **Respuesta Norma Hurtado** | Si no hay respuesta en 1 semana → intentar por equipo Comisión VII |
| 🔴 4 | **Seguimiento Abelardo** | Si no hay respuesta esta semana → borrador formal |
| 🟡 5 | **Documentos enganche piloto** | Redactar 3 documentos: Char, Aljure, Verano |
| 🟡 6 | **Subir README corregido** | Reemplazar en GitHub (archivo ya generado) |
| 🟡 7 | **Subir registro_contactos actualizado** | Archivo ya generado, pendiente subir |
| 🟢 8 | **Demo Day** | Una vez el prototipo corre → grabar video del caso de éxito |
| 🟢 9 | **Documento ejecutivo 1 página** | Resumen para entregar en mano en reuniones |
| 🟢 10 | **Contactar MinSalud/MinTIC** | Como acelerador de su agenda, no como competidor |

---

## 6. CONTEXTO ADICIONAL IMPORTANTE

- **Isael no quiere hacer política** — quiere ser el técnico detrás de quien la hace.
- **Ideológicamente de derecha** — priorizar: Abelardo, Henríquez, Blel, Valencia. Corcho es última opción.
- **El proyecto es apartidista** por diseño — la HC única no tiene color político.
- **Barranquilla es la base** — el piloto regional en Atlántico/Barranquilla es estratégico también porque Isael tiene redes locales.
- **GitHub usuario:** `IsaelDJQuinteroF-Dev`
- **Drive:** carpeta `H C U Col` contiene todo. Subcarpeta `prototipo` tiene los 5 archivos técnicos.
- **Todos los archivos del proyecto también están en** `C:\Isael De Jesús\DESCARGAS\H C U Col\`

---

*Briefing generado en mayo 2026. Actualizar tras cada avance significativo.*
