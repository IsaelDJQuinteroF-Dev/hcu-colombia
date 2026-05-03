# 1. Paquete NPM / .tgz de perfiles FHIR colombianos 
El Ministerio de Salud publicó la Guía de Implementación FHIR RDA (Resumen Digital de Atención) en https://vulcano.ihcecol.gov.co/. #

Allí se encuentra el paquete NPM oficial con los perfiles:

## 1. Paquete NPM oficial: @minsalud/co.fhir.rda (disponible en https://fhir.minsalud.gov.co/rda/package.tgz) ##

Guía Core de Colombia (FHIR Core IG): https://co.fhir.guide/core/ (versión 0.1.0 - STU1). Esta guía contiene perfiles como PatientCO, PractitionerCO, AllergyIntoleranceCO, ConditionCO, etc.

Para descargar el .tgz directamente desde la terminal:

bash
wget https://fhir.minsalud.gov.co/rda/package.tgz
O, si prefieres usar npm:

bash
npm pack @minsalud/co.fhir.rda


