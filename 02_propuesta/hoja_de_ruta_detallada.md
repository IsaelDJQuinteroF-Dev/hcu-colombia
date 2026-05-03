# \# HOJA DE RUTA DETALLADA PARA EJECUTAR EL DESARROLLO EN PARALELO #



\## 🏗️ \*\*Fase 1: Arquitectura y Desarrollo del Prototipo Técnico (Próximas 2-3 semanas)\*\* ##

No necesitamos construir un sistema de salud completo. La meta es tener un "Producto Mínimo Viable" que demuestre el intercambio de datos entre dos sistemas diferentes, usando la guía oficial del Ministerio de Salud para el Resumen Digital de Atención (RDA).



\*\*1. Configurar entorno de desarrollo con HAPI FHIR (recomendado)\*\*



¿Por qué? Es el servidor FHIR de código abierto más robusto y usado globalmente. Nos permite simular un repositorio central de datos clínicos. Es la referencia en el sector para pruebas de interoperabilidad.



Acción: Clonar el repositorio de inicio rápido hapi-fhir-jpaserver-starter de GitHub y levantar el servidor localmente con Docker.



\*\*2. Generar datos de prueba con Synthea\*\*



¿Por qué? Synthea es un proyecto open-source que genera historiales clínicos sintéticos realistas, exportables directamente en formato FHIR.



Acción: Utilizar Synthea para crear una población de unos 100 pacientes ficticios y subirlos al servidor HAPI FHIR.



\*\*3. Construir un visor/cliente web simple\*\*



¿Por qué? Necesitamos una interfaz gráfica para demostrar las capacidades del sistema. Debe poder buscar un paciente y mostrar sus datos clínicos en formato FHIR.



Tecnología: Python (Streamlit o Flask) + la librería fhirclient.



Funcionalidad clave: Implementar el "caso de éxito" simulado: un módulo de "Alergias" o "Condiciones Crónicas" que se visualice de forma destacada en la pantalla de urgencias.



\*\*4. Simular la interoperabilidad federada\*\*



Acción: Ejecutar una segunda instancia de HAPI FHIR (simulando la "IPS" o una "EPS" diferente).



Demostración: La aplicación cliente debe ser capaz de consultar datos en una instancia y, mediante una orquestación simple, traer datos complementarios de la segunda instancia, como si estuviera consultando la plataforma de intercambio. Esto demuestra el "modelo federado" de la propuesta.



\## \*\*🗳️ Fase 2: Sincronización Política y Cabildeo (En Paralelo)\*\* ##

El prototipo debe ser el reflejo técnico del lobby político.



\*\*1. Estudiar a fondo la competencia legislativa\*\*



Actualmente, hay proyectos de ley en el Congreso buscando implementar una Historia Clínica Electrónica Única. Hay que leerlos al detalle y preparar un discurso que exponga por qué nuestro enfoque federado y con un plan de 2 años es superior a otras alternativas.



Guiones de ajuste: Afinar los guiones para los congresistas en el repositorio. El mensaje ahora puede ser: "Conozco el proyecto de ley que se discute, pero mi modelo federado y mi prototipo funcional resuelven los problemas de implementación que ese texto no aborda".



\*\*2. Buscar un "Padrino Técnico" en el sector público\*\*



Objetivo: Contactar a los equipos de la Agenda de Transformación Digital e Interoperabilidad del Sector Salud o a la Dirección de Gobierno Digital de MinTIC. Nuestra propuesta no es una idea aislada, sino la aceleración de los planes oficiales.



Discurso sugerido: "Tengo un prototipo funcional que demuestra cómo implementar el RDA de la Resolución 1888 de 2025 en un modelo federado. No vengo a criticar, vengo a contribuir a la agenda del Ministerio".



\*\*3. Preparar un "Demo Day" con un caso de éxito mediático\*\*



Ese caso documentado de cómo el prototipo evitó una muerte por alergia será la exposición de motivos más potente para el proyecto.







\## PASOS INMEDIATOS PARA ESTA SEMANA ##



1.- \*\*Técnico\*\*: Ir al repositorio oficial de la guía FHIR RDA de Minsalud (vulcano.ihcecol.gov.co) y descarga el paquete NPM o el .tgz de perfiles FHIR.



2.- \*\*Político\*\*: Buscar en la Gaceta del Congreso los proyectos de ley activos sobre "historia clínica electrónica única".



3.- \*\*Estratégico\*\*: Subir al repositorio un sub-módulo prototipo/ con la estructura inicial del servidor HAPI FHIR, demostrando que el proyecto ya tiene un corazón técnico palpitante detrás del papel.





