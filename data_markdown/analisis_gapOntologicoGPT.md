ROL
Actúa como un arqueólogo senior especializado en teoría arqueológica, estratigrafía,
ontologías del patrimonio cultural y modelado semántico. Dominas CIDOC CRM, CRMsci,
CRMinf, CRMhs, ARIADNE-AO-Cat, OWL-Time, GeoSPARQL, PROV-O y la construcción de
extensiones OWL/RDFS.
OBJETIVO
Realiza un análisis crítico y técnico de CRMarchaeo v2.1.1 y propone una arquitectura
ontológica modular que amplíe su cobertura desde la excavación hacia el ciclo
arqueológico completo: objeto, contexto, análisis, inferencia, temporalidad, espacialidad,
provenance y contexto territorial.
FUENTES
Usa como base principal estas fuentes:
- CRMarchaeo v2.1.1: PDF, HTML y OWL
- CRMinf v1.2.1
- CRMsci v3.1
- CRMhs v1.2
- AO-Cat v1.2.2
REGLAS
1. No hagas una descripción genérica: analiza mecanismos ontológicos concretos.
2. Distingue explícitamente entre:
- observado
- interpretado
- inferido

- documentado
3. No inventes extensiones si un patrón existente resuelve el problema.
4. Si propones nuevas clases o propiedades, justifica:
- nombre
- propósito
- dominio
- rango
- alineación con ontologías existentes
- ejemplo de uso
5. Mantén compatibilidad con CIDOC CRM.
6. Explica redundancias evitadas.
7. Expón claramente qué parte del modelado pertenece a:
- hechos
- hipótesis
- inferencias
- trazabilidad del conocimiento
8. Incluye ejemplos formales: triples RDF/Turtle o pseudo-OWL.
ENTREGABLES
A. Análisis crítico de CRMarchaeo

- alcance conceptual real vs. declarado
- patrones ontológicos dominantes
- dependencias con CIDOC CRM, CRMsci, CRMinf, CRMhs y AO-Cat
- análisis de formalización
- separación entre observación e interpretación
- separación entre proceso físico y proceso cognitivo
- tratamiento de tiempo, espacio, materialidad e incertidumbre
B. Gaps ontológicos
Detecta lagunas en:
- objeto arqueológico
- análisis científico
- inferencia e interpretación
- espacio y GIS
- tiempo y cronología
- workflows y procedimientos
C. Propuesta de extensiones
Diseña módulos:
1. Objeto arqueológico

2. Análisis científico
3. Temporalidad avanzada
4. Espacialidad y geoespacialidad
5. Inferencia arqueológica
6. Contexto arqueológico ampliado
D. Integración externa
Evalúa integración con:
- OWL-Time
- PROV-O
- GeoSPARQL / OGC
- GeoSciML / TimeScale
- SOSA/SSN si aporta valor
- CRMinf, CRMhs y AO-Cat
E. Arquitectura ontológica
Define una arquitectura por capas:
- Core
- Extensiones arqueológicas
- Integración científica

- Infraestructura de tiempo/espacio/provenance
F. CQ y user stories
Reformula las preguntas de competencia aportadas, clasifícalas en:
- Simples
- Complejas
Para cada CQ proporciona:
- versión mejorada
- tipo
- user story
- módulos mínimos
- clases y propiedades mínimas
- riesgos de ambigüedad
- posible gold standard
Además, propone nuevas CQ para cubrir las lagunas detectadas.
FORMATO DE SALIDA
1. Resumen ejecutivo
2. Análisis crítico de CRMarchaeo
3. Gaps ontológicos

4. Propuesta de extensiones ontológicas
5. Integración con ontologías externas
6. Arquitectura ontológica
7. CQ y user stories
8. Conclusiones
9. Ejemplos de modelado
10. Anexo con clases y propiedades propuestas
CRITERIO DE CALIDAD
La salida debe parecer una propuesta técnica seria para una extensión oficial de CIDOC
CRM o para una infraestructura tipo ARIADNE.
Análisis crítico y propuesta de extensiones para
CRMarchaeo v2.1.1
1. Resumen ejecutivo
CRMarchaeo v2.1.1 constituye una de las extensiones más sólidas del ecosistema CIDOC
CRM para representar procesos arqueológicos estratigráficos. Su principal fortaleza reside
en la formalización de la excavación como secuencia de eventos y en la representación
explícita de relaciones estratigráficas mediante un patrón orientado a procesos.
Sin embargo, el modelo presenta limitaciones estructurales derivadas de su alcance
original. Aunque el nombre “CRMarchaeo” sugiere una ontología arqueológica general, su
cobertura real está centrada principalmente en:
• excavación arqueológica
• estratigrafía
• observación de contextos
• relaciones estratigráficas
• procesos de remoción y deposición
En consecuencia, quedan insuficientemente modelados:
• el ciclo de vida del artefacto

• la inferencia arqueológica compleja
• la multivocalidad interpretativa
• los workflows analíticos completos
• los procesos científicos de laboratorio
• la temporalidad híbrida
• la espacialidad avanzada GIS/3D
• la trazabilidad epistemológica
El presente análisis propone una arquitectura ontológica modular compuesta por:
1. Núcleo CRM + CRMarchaeo
2. Extensiones arqueológicas especializadas
3. Capa epistemológica basada en CRMinf
4. Capa científica basada en CRMsci y CRMhs
5. Infraestructura temporal y espacial basada en OWL-Time, GeoSPARQL y GeoSciML
6. Capa de interoperabilidad y publicación basada en AO-Cat
La propuesta mantiene compatibilidad total con CIDOC CRM y evita duplicaciones
semánticas mediante reutilización de patrones ontológicos ya existentes.
2. Análisis crítico de CRMarchaeo
2.1 Alcance conceptual real vs. declarado
Alcance declarado
CRMarchaeo se presenta como una extensión para describir:
• excavaciones arqueológicas
• estratigrafía
• procesos de deposición
• relaciones contextuales
• observaciones arqueológicas
Alcance real
El análisis de clases y propiedades demuestra que el alcance real está mucho más
restringido:
Área Cobertura
Excavación Alta
Estratigrafía Muy alta

Área Cobertura
Relaciones contextuales Alta
Observación arqueológica Media
Inferencia arqueológica Baja
Artefactos Baja
Cronología compleja Baja
GIS / 3D Muy baja
Laboratorio científico Muy baja
Paisaje arqueológico Muy baja
Multivocalidad Nula
CRMarchaeo debe entenderse más correctamente como:
una ontología de excavación y estratigrafía arqueológica basada en procesos.
No constituye una ontología arqueológica integral.
2.2 Patrones ontológicos dominantes
A. Event-centric
El modelo sigue claramente el patrón event-centric de CIDOC CRM.
Los hechos arqueológicos no se representan como entidades estáticas, sino como:
• eventos
• modificaciones
• procesos
• observaciones
• relaciones inferidas
Ejemplo:
• A1 Excavation Process Unit
• A5 Stratigraphic Modification Event
• A4 Stratigraphic Genesis
La excavación no se modela como “registro”, sino como transformación material del
contexto.
B. Stratigraphy-driven
La estratigrafía es el eje semántico principal.

Todo el modelo se organiza alrededor de:
• unidades estratigráficas
• génesis
• interfaces
• secuencias
• embedding
• relaciones estratigráficas
Este patrón domina incluso sobre el modelado del objeto.
C. Observation-driven
CRMarchaeo depende intensamente de CRMsci.
Muchos constructos derivan de:
• observación
• medición
• interpretación observacional
Ejemplo:
• A8 Stratigraphic Unit se interpreta mediante observaciones
• AP11 physical relation sirve como evidencia observada
D. Process-oriented
El modelo entiende la arqueología como una serie de transformaciones materiales.
Las entidades principales derivan de:
• deposición
• remoción
• erosión
• excavación
• modificación
Esto genera una fuerte coherencia estratigráfica, pero limita:
• objetos
• biografías
• persistencia temporal
• relaciones sociales

2.3 Dependencias ontológicas
CIDOC CRM
CRMarchaeo depende profundamente de CIDOC CRM.
Especialmente:
CRM Función
E18 Physical Thing base material
E19 Physical Object objetos
E53 Place espacialidad
E52 Time-Span temporalidad
E7 Activity procesos
E13 Attribute Assignment interpretaciones
E5 Event estructura event-centric
CRMarchaeo no redefine el núcleo CRM; lo especializa.
CRMsci
CRMsci es esencial.
Especialmente:
CRMsci Función
S4 Observation observación
S5 Inference Making inferencia
S21 Measurement medición
S18 Alteration cambio material
O8 observed relación observacional
CRMarchaeo reutiliza CRMsci para diferenciar:
• hecho observado
• inferencia arqueológica
Aunque esta separación no siempre queda completamente formalizada.

CRMinf
CRMinf no está integrado explícitamente en profundidad, pero es crítico para extender:
• hipótesis
• inferencias
• niveles de certeza
• razonamiento arqueológico
• Harris Matrix inferencial
Actualmente CRMarchaeo modela relaciones estratigráficas, pero no la epistemología del
razonamiento.
CRMhs
CRMhs resuelve una de las mayores debilidades del ecosistema arqueológico:
• laboratorio
• muestras
• protocolos
• datasets
• métodos científicos
Es especialmente útil para:
• isotopía
• ADN
• radiocarbono
• petrografía
• química
AO-Cat
AO-Cat actúa como capa de:
• descubrimiento
• agregación
• interoperabilidad
• publicación
No sustituye modelado arqueológico profundo.

Es una ontología de infraestructura de datos.
2.4 Separación entre observación e interpretación
Este es uno de los problemas centrales.
Fortalezas
CRMarchaeo reconoce la diferencia.
Ejemplo:
• AP11 = relación física observada
• AP13 = relación estratigráfica inferida
Esto es conceptualmente correcto.
Debilidades
La separación sigue incompleta.
A1 Excavation Process Unit mezcla:
• remoción física
• observación
• documentación
• producción de conocimiento
La propia documentación reconoce que A1 está “sobrecargada”.
Problema:
El mismo evento representa simultáneamente:
• proceso físico
• actividad cognitiva
• generación documental
• destrucción material
Esto viola parcialmente el principio de separación epistemológica.

2.5 Tratamiento del tiempo
Fortalezas
CRMarchaeo hereda:
• E52 Time-Span
• secuencialidad estratigráfica
• anterioridad relativa
La temporalidad relativa funciona bien.
Limitaciones
Falta:
• OWL-Time
• incertidumbre temporal formal
• cronologías híbridas
• escalas geológicas
• equivalencias cronológicas complejas
• temporalidad probabilística
No existe una integración adecuada con:
• PeriodO
• GeoSciML TimeScale
• Allen relations
2.6 Tratamiento del espacio
Fortalezas
El modelo reconoce:
• E53 Place
• spatial interfaces
• embedding
• contextos físicos

Debilidades
No existe:
• geometría explícita
• topología formal OGC
• soporte 3D
• incertidumbre espacial
• representación GIS compleja
El espacio sigue siendo principalmente conceptual.
2.7 Tratamiento de incertidumbre
La incertidumbre es uno de los puntos más débiles.
Existe implícitamente en:
• inferencias estratigráficas
• observaciones
• relaciones AP13
Pero no existen:
• niveles formales de confianza
• razonamiento probabilístico
• competing hypotheses
• provenance argumentativo
Aquí CRMinf resulta imprescindible.
3. Gaps ontológicos
3.1 Nivel artefactual
Problema principal
El objeto arqueológico aparece subordinado al contexto.
CRMarchaeo modela mejor:
• dónde aparece el objeto

que:
• qué es
• cómo evoluciona
• cómo circula
• cómo cambia
Gaps detectados
Falta de biografía del objeto
No se modela:
• producción
• uso
• reutilización
• reparación
• intercambio
• deposición secundaria
• recuperación moderna
Falta de agencia humana
No existen patrones claros para:
• intención
• práctica social
• uso ritual
• circulación cultural
Falta de persistencia histórica
El objeto aparece principalmente como:
• embedded find
• contenido estratigráfico
No como entidad histórica compleja.

3.2 Nivel analítico
Ausencia de workflows científicos completos
No existe modelado explícito de:
• muestreo
• laboratorio
• protocolos
• datasets
• calibración
• replicabilidad
Datación absoluta insuficiente
CRMarchaeo maneja bien cronología relativa.
Pero no:
• C14
• Bayesian modeling
• dendrocronología
• OSL
• isotopía
3.3 Nivel interpretativo
Problema epistemológico
El razonamiento arqueológico queda implícito.
No se modelan:
• hipótesis rivales
• argumentación
• revisión interpretativa
• grados de certeza
• evidencia contradictoria

3.4 Nivel espacial
Limitaciones GIS
No existe integración real con:
• GeoSPARQL
• CityGML
• BIM
• 3D stratigraphy
3.5 Nivel temporal
Problema de escalas múltiples
No se integran:
• tiempo geológico
• tiempo cultural
• tiempo histórico
• tiempo absoluto
3.6 Nivel procedimental
No se modelan:
• decisiones metodológicas
• estrategias de excavación
• protocolos
• workflows digitales
• reproducibilidad arqueológica
4. Propuesta de extensiones ontológicas
4.1 Módulo de objeto arqueológico
Objetivo
Convertir el objeto arqueológico en:

•  entidad histórica
•  entidad biográfica
•  entidad social
•  entidad material persistente

Nuevas clases propuestas
| Clase                                 | Descripción                 |     |
| ------------------------------------- | --------------------------- | --- |
| AOA1 Archaeological Object Biography  | secuencia vital del objeto  |     |
| AOA2 Use Event                        | evento de uso               |     |
| AOA3 Reuse Event                      | reutilización               |     |
| AOA4 Deposition Event                 | deposición                  |     |
| AOA5 Recovery Event                   | recuperación moderna        |     |
| AOA6 Functional Attribution           | asignación funcional        |     |

Nuevas propiedades
| Propiedad                          | Dominio  | Rango  |
| ---------------------------------- | -------- | ------ |
| aoa:has_biography                  | E19      | AOA1   |
| aoa:participated_in_use            | E19      | AOA2   |
| aoa:was_reused_in                  | E19      | AOA3   |
| aoa:was_deposited_by               | E19      | AOA4   |
| aoa:has_functional_interpretation  | E19      | AOA6   |

Ejemplo RDF
:axe_1 a crm:E22_Human-Made_Object ;
    aoa:has_biography :bio_1 .

:bio_1 a aoa:AOA1_Archaeological_Object_Biography .

4.2 Módulo de análisis científico
Integraciones
•  CRMsci
•  CRMhs

• PROV-O
Nuevas clases
Clase Descripción
AOS1 Laboratory Analysis análisis científico
AOS2 Sample Extraction toma de muestra
AOS3 Analytical Dataset dataset científico
AOS4 Calibration Process calibración
AOS5 Isotopic Measurement isotopía
AOS6 Radiocarbon Determination C14
Ejemplo RDF
:sample_14 a crm:E19_Physical_Object ;
crm:P46i_forms_part_of :bone_22 .
:analysis_1 a aos:AOS6_Radiocarbon_Determination ;
prov:used :sample_14 ;
crm:P141_assigned :date_1 .
4.3 Módulo temporal avanzado
Integraciones
• OWL-Time
• GeoSciML
• PeriodO
Nuevas clases
Clase Descripción
AOT1 Hybrid Chronology cronología híbrida
AOT2 Geological Correlation correlación geológica
AOT3 Temporal Uncertainty incertidumbre temporal

Ejemplo RDF
:event_1 time:hasBeginning :tp1 .
:event_1 aot:has_cultural_period :bronze_age .
4.4 Módulo espacial y geoespacial
Integraciones
• GeoSPARQL
• OGC
Nuevas clases
Clase Descripción
AOG1 Stratigraphic Geometry geometría estratigráfica
AOG2 Spatial Uncertainty incertidumbre espacial
AOG3 Excavation Volume volumen excavado
Ejemplo RDF
:su_12 geo:hasGeometry :geom_12 .
:geom_12 geo:asWKT "POLYHEDRALSURFACE Z (...)"^^geo:wktLiteral .
4.5 Módulo de inferencia arqueológica
Objetivo
Formalizar:
• hipótesis
• razonamiento
• certeza
• Harris Matrix
• evidencia

Integraciones
• CRMinf
• PROV-O
• CRMsci
Nuevas clases
Clase Descripción
AOI1 Archaeological Hypothesis hipótesis
AOI2 Stratigraphic Argument argumento estratigráfico
AOI3 Certainty Assessment evaluación de certeza
AOI4 Competing Interpretation interpretación alternativa
Ejemplo RDF
:hyp1 a aoi:AOI1_Archaeological_Hypothesis ;
crminf:J2_concluded_that :propSet_1 .
4.6 Módulo de contexto ampliado
Objetivo
Extender el análisis más allá del sitio.
Nuevas clases
Clase Descripción
AOL1 Archaeological Landscape paisaje
AOL2 Settlement Network red de asentamientos
AOL3 Territory territorio
AOL4 Mobility Corridor corredor de movilidad

5. Integración con ontologías externas
OWL-Time
Función
Formalización temporal avanzada.
Problemas que resuelve
• intervalos
• relaciones temporales
• incertidumbre
• escalas múltiples
PROV-O
Función
Trazabilidad del conocimiento.
Problemas que resuelve
• provenance
• workflows
• reproducibilidad
• atribución científica
GeoSPARQL
Función
Formalización espacial interoperable.
Problemas que resuelve
• geometrías
• topología
• GIS
• consultas espaciales

GeoSciML / TimeScale
Función
Escalas geológicas.
Problemas que resuelve
• sedimentología
• geoarqueología
• correlaciones estratigráficas
6. Arquitectura ontológica propuesta
Capa 1 — Core
• CIDOC CRM
• CRMarchaeo
Función:
• eventos
• estratigrafía
• contexto básico
Capa 2 — Extensiones arqueológicas
Incluye:
• biografía del objeto
• inferencia
• tipología
• paisaje
Capa 3 — Integración científica
Incluye:
• CRMsci
• CRMhs
• PROV-O

Capa 4 — Infraestructura semántica
Incluye:
• OWL-Time
• GeoSPARQL
• GeoSciML
7. CQ y user stories
7.1 Revisión y mejora de CQ existentes
CQ-S1
Pregunta
¿Qué subcolecciones temáticas integran la infraestructura IDEArq?
Tipo
Simple
User story
Como gestor de datos arqueológicos quiero identificar las colecciones temáticas
disponibles para organizar recursos interoperables.
Módulos mínimos
• AO-Cat
Clases mínimas
• ao:AO_Collection
Propiedades mínimas
• ao:has_part
CQ-S2
Pregunta
¿En qué unidad estratigráfica y estructura fue recuperado un objeto arqueológico?

Tipo
Simple
User story
Como arqueólogo quiero reconstruir el contexto exacto de hallazgo de un objeto.
Módulos mínimos
• CRMarchaeo
• CIDOC CRM
Clases mínimas
• A8 Stratigraphic Unit
• A2 Stratigraphic Volume Unit
CQ-C1
Pregunta
¿Qué inferencias estratigráficas justifican la interpretación cronológica de una unidad?
Tipo
Compleja
User story
Como especialista estratigráfico quiero justificar formalmente las relaciones cronológicas
inferidas entre unidades.
Módulos mínimos
• CRMarchaeo
• CRMinf
• CRMsci
Requisitos
• reificación
• provenance
• evidencia
• inferencia

CQ-C2
Pregunta
¿Qué hipótesis alternativas existen sobre la función ritual de una estructura funeraria y
qué evidencia sustenta cada una?
Tipo
Compleja
Módulos mínimos
• inferencia arqueológica
• provenance
• tipología
7.2 Nuevas CQ propuestas
CQ-S3
Pregunta
¿Qué materiales están documentados en los objetos recuperados de una unidad
estratigráfica?
Tipo
Simple
User story
Como investigador quiero identificar materiales asociados a contextos concretos para
realizar análisis comparativos.
Módulos mínimos
• CIDOC CRM
• AO-Cat
CQ-S4
Pregunta
¿Qué objetos fueron recuperados en una campaña de excavación específica?

Tipo
Simple
User story
Como arqueólogo quiero listar los hallazgos asociados a una campaña concreta.
Módulos mínimos
• CRMarchaeo
• CIDOC CRM
CQ-S5
Pregunta
¿Qué cronologías culturales están asociadas a un contexto arqueológico?
Tipo
Simple
User story
Como especialista cronológico quiero identificar periodizaciones culturales asociadas a
contextos.
Módulos mínimos
• OWL-Time
• AO-Cat
CQ-S6
Pregunta
¿Qué individuos fueron enterrados en una estructura funeraria determinada?
Tipo
Simple
User story
Como antropólogo físico quiero identificar individuos asociados a una tumba específica.

Módulos mínimos
• CIDOC CRM
• CRMarchaeo
CQ-S7
Pregunta
¿Qué método científico se utilizó para obtener una datación?
Tipo
Simple
User story
Como investigador quiero conocer el método analítico empleado en una cronología.
Módulos mínimos
• CRMsci
• CRMhs
CQ-S8
Pregunta
¿Qué geometría espacial representa un yacimiento arqueológico?
Tipo
Simple
User story
Como analista GIS quiero visualizar espacialmente los yacimientos.
Módulos mínimos
• GeoSPARQL
CQ-S9
Pregunta
¿Qué unidades estratigráficas forman parte de una estructura arqueológica?

Tipo
Simple
User story
Como arqueólogo quiero reconstruir la composición estratigráfica de una estructura.
Módulos mínimos
• CRMarchaeo
CQ-S10
Pregunta
¿Qué coordenadas geográficas tiene un contexto arqueológico?
Tipo
Simple
User story
Como investigador quiero integrar datos arqueológicos en plataformas GIS.
Módulos mínimos
• GeoSPARQL
CQ-S11
Pregunta
¿Qué muestras fueron extraídas de un individuo arqueológico?
Tipo
Simple
User story
Como bioarqueólogo quiero rastrear el origen de muestras analíticas.
Módulos mínimos
• CRMhs
• CRMsci

CQ-S12
Pregunta
¿Qué datasets analíticos fueron generados durante un análisis científico?
Tipo
Simple
User story
Como gestor de datos quiero identificar datasets derivados de procesos analíticos.
Módulos mínimos
• CRMhs
• PROV-O
CQ-S13
Pregunta
¿Qué instituciones participaron en una excavación arqueológica?
Tipo
Simple
User story
Como gestor patrimonial quiero conocer las entidades responsables de una intervención.
Módulos mínimos
• CIDOC CRM
CQ-S14
Pregunta
¿Qué técnicas de documentación se aplicaron durante una excavación?
Tipo
Simple

User story
Como arqueólogo quiero conocer las metodologías documentales empleadas.
Módulos mínimos
• PROV-O
• CRMarchaeo
CQ-S15
Pregunta
¿Qué relaciones topológicas existen entre dos estructuras arqueológicas?
Tipo
Simple
User story
Como analista espacial quiero evaluar relaciones espaciales entre entidades
arqueológicas.
Módulos mínimos
• GeoSPARQL
CQ-S16
Pregunta
¿Qué objetos presentan evidencias de reutilización?
Tipo
Simple
User story
Como especialista en cultura material quiero identificar patrones de reutilización.
Módulos mínimos
• Extensión objeto arqueológico

CQ-S17
Pregunta
¿Qué tipos funerarios están documentados en un yacimiento?
Tipo
Simple
User story
Como arqueólogo funerario quiero clasificar prácticas funerarias.
Módulos mínimos
• AO-Cat
• CIDOC CRM
CQ-S18
Pregunta
¿Qué protocolos científicos fueron aplicados en un análisis?
Tipo
Simple
User story
Como científico quiero reproducir procesos analíticos.
Módulos mínimos
• CRMhs
• PROV-O
CQ-S19
Pregunta
¿Qué periodos geológicos están asociados a una secuencia estratigráfica?
Tipo
Simple

User story
Como geoarqueólogo quiero correlacionar estratigrafía arqueológica y geológica.
Módulos mínimos
• GeoSciML
• OWL-Time
CQ-S20
Pregunta
¿Qué relaciones de superposición existen entre unidades estratigráficas?
Tipo
Simple
User story
Como especialista estratigráfico quiero reconstruir secuencias deposicionales.
Módulos mínimos
• CRMarchaeo
CQ-C3
Pregunta
¿Qué eventos de reutilización modificaron la biografía de un objeto arqueológico antes de
su deposición final?
Tipo
Compleja
User story
Como especialista en cultura material quiero reconstruir la historia completa de un objeto.
Módulos mínimos
• módulo objeto arqueológico
• CRMarchaeo
• CIDOC CRM

CQ-C4
Pregunta
¿Qué datasets analíticos y protocolos científicos sustentan una datación radiocarbónica?
Tipo
Compleja
User story
Como investigador quiero evaluar la reproducibilidad de una datación.
Módulos mínimos
• CRMhs
• PROV-O
• CRMsci
CQ-C5
Pregunta
¿Qué relaciones espaciales topológicas existen entre estructuras funerarias y áreas
domésticas en un paisaje arqueológico?
Tipo
Compleja
User story
Como arqueólogo espacial quiero analizar organización territorial y funcional.
Módulos mínimos
• GeoSPARQL
• módulo paisaje
CQ-C6
Pregunta
¿Qué hipótesis compiten sobre la cronología de una unidad estratigráfica y qué evidencia
soporta cada una?

Tipo
Compleja
User story
Como especialista cronológico quiero comparar interpretaciones temporales alternativas.
Módulos mínimos
• CRMinf
• CRMsci
• OWL-Time
CQ-C7
Pregunta
¿Qué inferencias permiten asociar un objeto a una práctica ritual específica?
Tipo
Compleja
User story
Como arqueólogo quiero justificar interpretaciones rituales mediante evidencia formal.
Módulos mínimos
• CRMinf
• módulo inferencia
CQ-C8
Pregunta
¿Qué secuencia de eventos explica la formación de un depósito arqueológico complejo?
Tipo
Compleja
User story
Como geoarqueólogo quiero reconstruir procesos de formación estratigráfica.

Módulos mínimos
• CRMarchaeo
• CRMsci
CQ-C9
Pregunta
¿Qué relaciones estratigráficas fueron inferidas indirectamente y no observadas
físicamente?
Tipo
Compleja
User story
Como especialista estratigráfico quiero distinguir observación directa e inferencia.
Módulos mínimos
• CRMarchaeo
• CRMinf
CQ-C10
Pregunta
¿Qué workflows analíticos transformaron una muestra desde la extracción hasta la
publicación del resultado?
Tipo
Compleja
User story
Como científico quiero rastrear completamente el ciclo analítico de una muestra.
Módulos mínimos
• CRMhs
• PROV-O

CQ-C11
Pregunta
¿Qué evidencias sustentan la interpretación funcional de una estructura arqueológica?
Tipo
Compleja
User story
Como arqueólogo quiero justificar funcionalmente una estructura.
Módulos mínimos
• CRMinf
• módulo inferencia
CQ-C12
Pregunta
¿Qué conflictos interpretativos existen entre diferentes investigadores sobre un contexto
arqueológico?
Tipo
Compleja
User story
Como historiador de la arqueología quiero comparar interpretaciones académicas.
Módulos mínimos
• CRMinf
• PROV-O
CQ-C13
Pregunta
¿Qué niveles de incertidumbre espacial afectan a la delimitación de un yacimiento?
Tipo
Compleja

User story
Como analista GIS quiero evaluar precisión espacial de los datos.
Módulos mínimos
• GeoSPARQL
• módulo espacial
CQ-C14
Pregunta
¿Qué eventos naturales y antrópicos contribuyeron conjuntamente a la formación de una
secuencia estratigráfica?
Tipo
Compleja
User story
Como geoarqueólogo quiero diferenciar procesos naturales y culturales.
Módulos mínimos
• CRMarchaeo
• CRMsci
CQ-C15
Pregunta
¿Qué correlaciones existen entre cronologías culturales y cronologías absolutas?
Tipo
Compleja
User story
Como especialista cronológico quiero integrar periodización cultural y tiempo absoluto.
Módulos mínimos
• OWL-Time
• GeoSciML

CQ-C16
Pregunta
¿Qué objetos comparten trayectorias biográficas similares en diferentes yacimientos?
Tipo
Compleja
User story
Como investigador quiero detectar patrones de circulación cultural.
Módulos mínimos
• módulo objeto arqueológico
• CIDOC CRM
CQ-C17
Pregunta
¿Qué inferencias conectan un conjunto funerario con identidades sociales específicas?
Tipo
Compleja
User story
Como arqueólogo social quiero analizar construcción de identidades.
Módulos mínimos
• CRMinf
• módulo inferencia
CQ-C18
Pregunta
¿Qué relaciones espaciales multiescala existen entre sitios, territorios y corredores de
movilidad?
Tipo
Compleja

User story
Como arqueólogo espacial quiero estudiar conectividad territorial.
Módulos mínimos
• GeoSPARQL
• módulo paisaje
CQ-C19
Pregunta
¿Qué evidencia analítica contradice una interpretación cronológica previa?
Tipo
Compleja
User story
Como investigador quiero reevaluar cronologías existentes.
Módulos mínimos
• CRMinf
• CRMhs
CQ-C20
Pregunta
¿Qué relaciones de dependencia metodológica existen entre decisiones de excavación y
resultados interpretativos?
Tipo
Compleja
User story
Como metodólogo quiero evaluar el impacto de las estrategias de excavación.
Módulos mínimos
• PROV-O
• CRMarchaeo

CQ-C21
Pregunta
¿Qué secuencias de ocupación pueden inferirse a partir de relaciones estratigráficas y
cronologías absolutas?
Tipo
Compleja
User story
Como arqueólogo quiero reconstruir dinámicas de ocupación.
Módulos mínimos
• CRMarchaeo
• OWL-Time
• CRMinf
CQ-C22
Pregunta
¿Qué muestras derivan de un mismo individuo o contexto arqueológico?
Tipo
Compleja
User story
Como bioarqueólogo quiero correlacionar resultados analíticos procedentes del mismo
origen.
Módulos mínimos
• CRMhs
• CIDOC CRM
CQ-C23
Pregunta
¿Qué evidencias espaciales justifican la delimitación funcional de áreas dentro de un
asentamiento?

Tipo
Compleja
User story
Como arqueólogo espacial quiero justificar zonificaciones funcionales.
Módulos mínimos
• GeoSPARQL
• CRMinf
CQ-C24
Pregunta
¿Qué interpretaciones fueron derivadas mediante razonamiento bayesiano aplicado a
dataciones?
Tipo
Compleja
User story
Como especialista cronológico quiero rastrear inferencias probabilísticas.
Módulos mínimos
• CRMinf
• CRMhs
• OWL-Time
CQ-C25
Pregunta
¿Qué entidades arqueológicas presentan geometrías 3D asociadas a incertidumbre
espacial?
Tipo
Compleja

User story
Como especialista GIS quiero gestionar modelos tridimensionales arqueológicos con
precisión variable.
Módulos mínimos
• GeoSPARQL
• módulo espacial
CQ-C26
Pregunta
¿Qué relaciones de contemporaneidad parcial existen entre eventos arqueológicos?
Tipo
Compleja
User story
Como arqueólogo quiero modelar simultaneidad temporal incompleta.
Módulos mínimos
• OWL-Time
• CRMinf
CQ-C27
Pregunta
¿Qué objetos fueron desplazados postdeposicionalmente y cómo afecta esto a su
contexto?
Tipo
Compleja
User story
Como geoarqueólogo quiero evaluar alteraciones tafonómicas.
Módulos mínimos
• CRMarchaeo
• módulo objeto arqueológico

CQ-C28
Pregunta
¿Qué procesos tafonómicos alteraron restos biológicos recuperados?
Tipo
Compleja
User story
Como bioarqueólogo quiero interpretar alteraciones postdeposicionales.
Módulos mínimos
• CRMsci
• CRMhs
CQ-C29
Pregunta
¿Qué relaciones argumentativas conectan observaciones, mediciones e interpretaciones?
Tipo
Compleja
User story
Como investigador quiero rastrear cadenas completas de razonamiento científico.
Módulos mínimos
• CRMinf
• CRMsci
• PROV-O
CQ-C30
Pregunta
¿Qué hipótesis fueron descartadas y por qué evidencia?

Tipo
Compleja
User story
Como investigador quiero documentar interpretaciones rechazadas y sus razones.
Módulos mínimos
• CRMinf
• PROV-O
8. Conclusiones
CRMarchaeo constituye una excelente ontología de excavación y estratigrafía, pero no
una ontología arqueológica integral.
Sus mayores fortalezas son:
• coherencia estratigráfica
• orientación a procesos
• compatibilidad con CIDOC CRM
• formalización de relaciones contextuales
Sus principales debilidades son:
• limitada epistemología
• escaso modelado artefactual
• baja integración científica
• ausencia de GIS avanzado
• ausencia de multivocalidad
• escasa formalización de incertidumbre
La arquitectura modular propuesta permite resolver estas limitaciones manteniendo:
• compatibilidad CIDOC CRM
• modularidad
• interoperabilidad
• extensibilidad

9. Ejemplos de modelado
Ejemplo de inferencia
:obs1 a crmsci:S4_Observation ;
crmsci:O8_observed :su_12 .
:infer1 a crmsci:S5_Inference_Making ;
crminf:J2_concluded_that :hyp1 .
Ejemplo espacial
:site1 geo:hasGeometry :geom1 .
:geom1 geo:asWKT "POLYGON((...))"^^geo:wktLiteral .
Ejemplo temporal híbrido
:event1 a crm:E5_Event ;
time:hasBeginning :tp1 ;
aot:has_cultural_period :bell_beaker .
10. Anexo — Nuevas clases propuestas
Clase Módulo
AOA1 Archaeological Object Biography objeto
AOS1 Laboratory Analysis científico
AOI1 Archaeological Hypothesis inferencia
AOG1 Stratigraphic Geometry espacial
AOT1 Hybrid Chronology temporal
AOL1 Archaeological Landscape paisaje
---------------
Tu caso no debería usar GeoSciML solo como “fuente de periodos geológicos”, sino como
una capa geoarqueológica estructural. Ahí está una de las claves fuertes del modelo que
estás construyendo.

GeoSciML no es únicamente una ontología de escalas temporales; es un estándar OGC
completo para modelar:
• unidades geológicas
• estratigrafía geológica
• geomorfología
• boreholes
• observaciones
• muestras
• estructuras geológicas
• escalas cronológicas geológicas
• relaciones estratigráficas geológicas
• metadatos analíticos (geosciml.org)
Y eso cambia bastante la arquitectura propuesta.
El punto importante es este:
CRMarchaeo modela estratigrafía arqueológica.
GeoSciML modela estratigrafía geológica.
La integración entre ambos permite construir una verdadera ontología geoarqueológica
multiescala.
Especialmente relevantes son:
• GeologicUnit
• GeologicTimescale
• GeochronologicEra
• GeochronologicBoundary
• Geomorphology (geosciml.org)
Lo que faltaba en la propuesta anterior era:
1. correlación explícita entre unidades estratigráficas arqueológicas y unidades
sedimentológicas/geológicas
2. procesos geomorfológicos

3. modelado sedimentario
4. eventos paleoambientales
5. estratigrafía geoarqueológica
6. vinculación formal entre cronología arqueológica y geológica
Y eso es crítico para:
• geoarqueología
• paleopaisajes
• tafonomía
• sedimentología arqueológica
• cuevas
• depósitos aluviales
• secuencias cuaternarias
• arqueología paleoambiental
La arquitectura correcta debería quedar así:
Infraestructura geoarqueológica
├── CIDOC CRM
├── CRMarchaeo
├── CRMsci
├── CRMinf
├── CRMhs
│
├── GeoSPARQL
├── OWL-Time
├── PROV-O
│

└── GeoSciML
├── GeologicUnit
├── Geomorphology
├── GeologicStructure
├── GeologicTimeScale
├── Borehole
└── EarthMaterial
La integración fuerte realmente debería hacerse en tres niveles:
1. Estratigrafía arqueológica ↔ estratigrafía geológica
Aquí está el núcleo conceptual.
A8 Stratigraphic Unit representa unidades arqueológicas.
Pero muchas veces esas unidades:
• están dentro de depósitos naturales
• forman parte de secuencias sedimentarias
• dependen de procesos geomorfológicos
Entonces necesitas alineaciones tipo:
:su_45 a crmarchaeo:A8_Stratigraphic_Unit ;
geoarch:is_correlated_with :alluvial_unit_3 .
:alluvial_unit_3 a gsml:GeologicUnit .
Eso es extremadamente importante para:
• cuevas
• terrazas fluviales
• depósitos lacustres
• geoarqueología cuaternaria

2. Procesos formativos
CRMarchaeo modela:
• deposición
• modificación
• excavación
Pero GeoSciML permite introducir:
• erosión
• sedimentación
• volcanismo
• coluvionamiento
• dinámica fluvial
• procesos geomorfológicos
Esto mejora muchísimo:
• tafonomía
• site formation processes
• postdepositional analysis
Ejemplo:
:formation_1 a crmarchaeo:A4_Stratigraphic_Genesis ;
geoarch:associated_geomorphic_process :flood_event_1 .
:flood_event_1 a gsml:GeomorphicProcess .
3. Temporalidad geológica
Aquí sí había mencionado GeoSciML, pero demasiado superficialmente.
GeoSciML TimeScale define:
• GeochronologicEra

• GeochronologicBoundary
• relaciones jerárquicas entre eras (geosciml.org)
Eso permite:
Pleistocene
└── Upper Pleistocene
└── MIS 3
y vincularlo con:
Bell Beaker
Early Bronze Age
Iron Age
Entonces puedes modelar cronologías híbridas:
:event_1 a crm:E5_Event ;
aot:has_geological_period :upper_pleistocene ;
aot:has_cultural_period :epipaleolithic .
Esto es muchísimo más potente que usar solo PeriodO.
4. GeoSciML + CRMsci
Aquí hay una sinergia muy fuerte que no habíamos explotado.
GeoSciML ya reutiliza patrones ISO19156 Observations & Measurements. (Open
Geospatial Consortium)
CRMsci hace algo parecido desde CIDOC CRM.
Eso significa que puedes crear un puente semántico elegante:
CRMsci S4 Observation
↕
GeoSciML Observation
Ideal para:
• geoquímica

• sedimentología
• micromorfología
• análisis de suelos
• paleoclima
5. Nueva capa propuesta: Geoarchaeology Module
Ahora sí añadiría un módulo explícito:
Geoarchaeology Module
Nuevas clases:
Clase Función
GEA1 Geoarchaeological Deposit depósito geoarqueológico
GEA2 Sedimentary Process proceso sedimentario
GEA3 Geomorphological Event evento geomorfológico
GEA4 Paleoenvironmental Context contexto paleoambiental
GEA5 Stratigraphic Correlation correlación estratigráfica
GEA6 Taphonomic Process proceso tafonómico
Nuevas propiedades:
Propiedad Dominio Rango
geoarch:correlates_with_geological_unit A8 gsml:GeologicUnit
geoarch:affected_by_geomorphic_process A8 GEA3
geoarch:has_sedimentary_origin A8 GEA2
geoarch:has_paleoenvironment A8 GEA4
geoarch:affected_by_taphonomy E18 GEA6
Impacto real en tus CQ

GeoSciML permite crear CQ muchísimo más interesantes:
Nueva CQ
Pregunta
¿Qué procesos geomorfológicos afectaron a las unidades estratigráficas asociadas a
ocupaciones humanas del Pleistoceno superior?
Tipo
Compleja
Módulos mínimos
• CRMarchaeo
• GeoSciML
• OWL-Time
• CRMinf
Nueva CQ
Pregunta
¿Qué correlaciones existen entre secuencias sedimentarias fluviales y contextos
arqueológicos ocupacionales?
Tipo
Compleja
Nueva CQ
Pregunta
¿Qué eventos tafonómicos naturales alteraron la distribución espacial original de los
hallazgos?
Tipo
Compleja
La conclusión importante es:

GeoSciML no debe aparecer como “ontología auxiliar”.
Debe convertirse en el núcleo de la capa geoarqueológica.
Eso transforma el proyecto desde:
• una extensión arqueológica convencional
a:
• una infraestructura semántica geoarqueológica multiescala interoperable con
OGC, INSPIRE y geociencias.
GeoSciML official site
(geosciml.org)