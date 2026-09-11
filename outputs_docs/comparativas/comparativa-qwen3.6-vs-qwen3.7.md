# Comparativa Qwen 3.6 plus vs Qwen 3.7-plus

> **Fecha:** 10-09-2026
>
> **Revisión 2026-09-11 — trazabilidad de las mejoras.** Las ontologías del piloto Qwen 3.7-plus se generaron con la **versión 1** del prompt (`ALWAYS check`, sin balance guideline). La sección §7 del brief, las 8 CQs de extensión y el balance guideline se incorporaron después, **después del piloto y sin regenerarlo**. Por tanto, las mejoras descritas en §12 son solo propuestas pero **no se han ejecutado**: los resultados comparados aquí corresponden al prompt v1 y a las 30 CQs originales.

---

## 0. ¿Qué es una Competency Question (CQ)?

Una **pregunta de competencia** (en inglés, *Competency Question*) es una pregunta que la ontología debe ser capaz de responder. Es la forma estándar de definir **qué debe saber** una ontología antes de construirla.

En lugar de empezar diciendo "crearemos estas clases y estas relaciones", empezamos preguntando: **¿qué preguntas reales debe poder responder el sistema?** Cada pregunta se convierte después en una prueba de validación: si la ontología puede responderla, cumple su función.

**Ejemplo:**


| Pregunta de competencia                                 | Lo que exige de la ontología                                                       |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| "¿De qué material está hecho este objeto arqueológico?" | Que exista una entidad "objeto", una entidad "material" y una relación entre ambas |
| "¿En qué unidad estratigráfica fue hallado?"            | Que exista una entidad "unidad estratigráfica" y una relación de procedencia       |
| "¿Qué tipología se le ha asignado?"                     | Que exista una entidad "asignación tipológica" con autor y fecha                   |


### Los dos ejes de clasificación

Las preguntas se organizan en **dos ejes que se cruzan**:

**Eje 1 — Patrones de modelado** (qué tipo de conocimiento pide la pregunta)

- **Eje 2 — Bloques temáticos** (de qué habla la pregunta)


| Patrón                                         | Pregunta sobre...                         | Pregunta típica                              |
| ---------------------------------------------- | ----------------------------------------- | -------------------------------------------- |
| **P1 — Eventos** (*Event-Driven*)              | Lo que **pasó** — procesos y acciones     | "¿Qué eventos de producción tuvo el objeto?" |
| **P2 — Estados** (*State-Transition*)          | Lo que **es** — propiedades y condiciones | "¿Qué estado de conservación tiene?"         |
| **P4 — Asignaciones** (*Assignment-Intrinsic*) | Lo que **sabemos** — interpretaciones     | "¿Qué tipología se le ha asignado?"          |


> **Nota sobre la numeración:** los patrones se numeran P1, P2 y P4 (no hay P3) porque siguen la nomenclatura del análisis de lagunas original del proyecto, donde P3 correspondía a un patrón descartado (observación, mediciones).

### Qué significa cada estrategia de generación

Para cada pregunta, la ontología se genera con dos **estrategias** distintas:


| Estrategia                     | Objetivo                                                            |     |
| ------------------------------ | ------------------------------------------------------------------- | --- |
| **Memoryless** (*sin memoria*) | Cada pregunta se responde por separado, sin recordar las anteriores |     |
| **Ontogenia** (*con memoria*)  | Cada pregunta se responde teniendo en cuenta todo lo ya construido  |     |


### Qué es la temperatura

La **temperatura** controla cuán "conservador" o "creativo" es el modelo al generar la ontología:

- **0.3** — conservador: reutiliza al máximo los estándares, crea las mínimas clases nuevas
- **0.5** — equilibrado: crea algunas clases nuevas, mantiene la alineación con los estándares
- **0.7** — creativo: construye jerarquías más profundas, más clases nuevas y más reglas formales

---

## 1. Comparativa general


| Parámetro               | Qwen 3.6 plus                           | Qwen 3.7-plus (piloto)                       |
| ----------------------- | --------------------------------------- | -------------------------------------------- |
| **Fecha**               | 28-05-2026                              | 27-08-2026                                   |
| **Modelo**              | qwen3.6-plus                            | qwen3.7-plus                                 |
| **CQs totales**         | 50                                      | 30                                           |
| **CQs por patrón**      | 17 P1 + 13 P2 + 20 P4                   | 10 P1 + 10 P2 + 10 P4                        |
| **Estrategias**         | memoryless + ontogenia                  | memoryless + ontogenia                       |
| **Temperatura**         | 0.3, 0.5, 0.7                           | 0.5                                          |
| **Corpus**              | Gap analysis + ontologies_data (núcleo) | Núcleo + artículosJuan                       |
| **Brief del dominio**   | No                                      | Sí (sin §7; §7 se añadió después del piloto) |
| **Patrones explícitos** | Sí                                      | Sí                                           |
| **Carpeta experimento** | `Qwen3.6_objeto_patrones/`              | `Qwen3.7plus/`                               |


---

## 2. CQs por patrón — comparativa detallada

### Distribución original de Qwen 3.6


| Patrón                        | CQs    | Descripción                                                                             |
| ----------------------------- | ------ | --------------------------------------------------------------------------------------- |
| **P1 — Event-Driven**         | 17     | Eventos del ciclo de vida: producción, uso, reuso, reparación, deposición, recuperación |
| **P2 — State-Transition**     | 13     | Estados físicos y materiales: composición, propiedades, transformaciones                |
| **P4 — Assignment-Intrinsic** | 20     | Asignaciones interpretativas: tipología, cronología, hipótesis                          |
| **TOTAL**                     | **50** |                                                                                         |


### Distribución actual del piloto Qwen 3.7-plus


| Patrón                        | CQs originales | CQs adicionales | Total  |
| ----------------------------- | -------------- | --------------- | ------ |
| **P1 — Event-Driven**         | 10             | 0               | **10** |
| **P2 — State-Transition**     | 10             | 0               | **10** |
| **P4 — Assignment-Intrinsic** | 10             | 0               | **10** |
| **TOTAL**                     | **30**         | **0**           | **30** |


> **Nota:** El piloto original tiene exactamente 30 CQs (10 por patrón). Las 8 preguntas de extensión se conservan en `CQ-object-qwen3.7plus-extension.md` y pertenecen a una iteración posterior; no forman parte de este piloto ni de sus métricas.

### Comparativa lado a lado


| Patrón                    | Qwen 3.6-plus | Qwen 3.7-plus |     |
| ------------------------- | ------------- | ------------- | --- |
| P1 — Event-Driven         | 17            | 10            |     |
| 2 — State-Transition      | 13            | 10            |     |
| P4 — Assignment-Intrinsic | 20            | 10            |     |
| **Total**                 | **50**        | **30**        |     |


- El piloto original cumple exactamente el diseño solicitado: 10 preguntas por patrón
- Las preguntas de extensión posterior se analizan por separado y no alteran las métricas del piloto

### CQs de Qwen 3.6, clasificadas por patrón y subgrupo (50 CQs)

> Clasificación **oficial del proyecto** (archivo `CQ_por_patron.md`), con distribución 17 P1 + 13 P2 + 20 P4. Se añaden **subgrupos temáticos** (`P1.1`, `P1.2`…) homólogos a los del piloto Qwen 3.7-plus, para permitir la comparación directa y la detección de vacíos temáticos. Las preguntas están traducidas al español; entre paréntesis se conserva el original en inglés cuando aporta precisión.

#### P1 — Eventos (lo que pasó) — 17 CQs


| Subgrupo                                       | CQ        | Pregunta                                                                                                                                                                     |
| ---------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P1.1 Producción y tecnología**               | CQ-OBJ-11 | ¿Mediante qué procedimientos tecnológicos y técnicas artesanales fue fabricado el objeto?                                                                                    |
| **P1.2 Biografía, trayectorias y actores**     | CQ-OBJ-01 | ¿Qué secuencia de eventos biográficos (producción, uso, reutilización, reparación, circulación, depósito, recuperación) constituye la trayectoria vital completa del objeto? |
|                                                | CQ-OBJ-03 | ¿Qué objetos de distintos sitios comparten trayectorias biográficas paralelas (secuencias similares de fabricación, uso, reutilización)?                                     |
|                                                | CQ-OBJ-08 | ¿Qué secuencia de eventos constituye la biografía del objeto?                                                                                                                |
|                                                | CQ-OBJ-09 | ¿Muestran objetos de sitios geográficamente distantes patrones biográficos paralelos?                                                                                        |
|                                                | CQ-OBJ-16 | ¿Qué actores sociales, grupos culturales o tradiciones artesanales se vinculan a la producción o uso del objeto?                                                             |
| **P1.3 Uso, reuso y transformación funcional** | CQ-OBJ-05 | ¿Qué objetos sufrieron transformaciones funcionales que cambiaron su clasificación tipológica original durante su vida útil?                                                 |
|                                                | CQ-OBJ-07 | ¿Ha sido reutilizado un objeto para una función distinta de la original?                                                                                                     |
| **P1.4 Depósito y recuperación**               | CQ-OBJ-06 | ¿Qué objetos se recuperaron como parte de una misma unidad de excavación?                                                                                                    |
|                                                | CQ-OBJ-15 | ¿Qué objetos comparten un mismo evento de deposición dentro de una unidad estratigráfica?                                                                                    |
| **P1.5 Circulación, custodia y patrimonio**    | CQ-OBJ-17 | ¿Viajó el objeto por distintas regiones geográficas o zonas culturales durante su existencia?                                                                                |
|                                                | CQ-OBJ-41 | ¿Qué cadena de custodia (excavación, almacenamiento, préstamo, exhibición, restauración, repatriación) ha gestionado el objeto?                                              |
|                                                | CQ-OBJ-45 | ¿Qué objetos son objeto de reclamaciones de patrimonio cultural, demandas de repatriación o litigios legales?                                                                |
|                                                | CQ-OBJ-47 | ¿Qué objetos circularon entre asentamientos, territorios o corredores de movilidad durante su vida útil activa?                                                              |
| **P1.6 Análisis, muestreo y conservación**     | CQ-OBJ-18 | ¿Qué cadena completa de eventos analíticos (muestreo, protocolo, medición, calibración, interpretación) transforma el objeto en dato?                                        |
|                                                | CQ-OBJ-26 | ¿Qué muestras físicas se han tomado del objeto para análisis de laboratorio?                                                                                                 |
|                                                | CQ-OBJ-27 | ¿Qué tratamientos de conservación o análisis de laboratorio ha recibido el objeto tras su excavación?                                                                        |

#### P2 — Estados (lo que es) — 13 CQs


| Subgrupo                                         | CQ        | Pregunta                                                                                                                            |
| ------------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **P2.1 Tafonomía y alteración**                  | CQ-OBJ-34 | ¿Qué procesos tafonómicos naturales (bioturbación, corrosión, meteorización, transporte hídrico, compactación) alteraron el objeto? |
|                                                  | CQ-OBJ-38 | ¿Qué procesos de fragmentación (intencional-ritual, accidental por uso o tafonómica) sufrió el objeto?                              |
|                                                  | CQ-OBJ-40 | ¿En qué estado de preservación se encuentra el objeto y qué procesos post-deposicionales lo conformaron?                            |
|                                                  | CQ-OBJ-14 | ¿Presenta el objeto huellas de reparación, alteración o modificación deliberada tras su producción inicial?                         |
| **P2.2 Desplazamiento post-deposicional**        | CQ-OBJ-37 | ¿Qué objetos muestran evidencia de desplazamiento post-deposicional y cómo afecta a su interpretación contextual?                   |
|                                                  | CQ-OBJ-39 | ¿Ha sido movido el objeto de su contexto deposicional primario por procesos naturales o humanos?                                    |
| **P2.3 Contexto deposicional y geoarqueología**  | CQ-OBJ-35 | ¿Qué correlaciones existen entre las unidades estratigráficas que contienen el objeto y las unidades geológicas?                    |
|                                                  | CQ-OBJ-36 | ¿Qué eventos geomorfológicos (inundaciones, coluvión, erosión, vulcanismo, dinámica fluvial) afectaron el contexto deposicional?    |
| **P2.4 Conservación y representación digital**   | CQ-OBJ-42 | ¿Qué decisiones de conservación (limpieza, consolidación, reconstrucción o no intervención) se aplicaron al objeto?                 |
|                                                  | CQ-OBJ-44 | ¿Qué réplicas digitales, modelos 3D o representaciones virtuales existen del objeto y qué documentan?                               |
| **P2.5 Estado funcional, narrativa y ocupación** | CQ-OBJ-12 | ¿Cuál es la narrativa cronológica completa del objeto, desde la fabricación hasta el depósito?                                      |
|                                                  | CQ-OBJ-13 | ¿Cambió el rol funcional del objeto durante su vida útil activa?                                                                    |
|                                                  | CQ-OBJ-49 | ¿Qué objetos de distintos niveles estratigráficos documentan secuencias de ocupación, abandono y reocupación?                       |

#### P4 — Asignaciones (lo que sabemos) — 20 CQs


| Subgrupo                                | CQ        | Pregunta                                                                                                                                             |
| --------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P4.1 Clasificación y tipología**      | CQ-OBJ-33 | ¿Bajo qué esquema tipológico se clasifica el objeto y qué vocabulario externo respalda esa clasificación?                                            |
| **P4.2 Composición y materialidad**     | CQ-OBJ-23 | ¿Cuál es la composición material primaria del objeto?                                                                                                |
| **P4.3 Función y significado**          | CQ-OBJ-24 | ¿Qué interpretación material y funcional han asignado los investigadores al objeto?                                                                  |
|                                         | CQ-OBJ-43 | ¿Qué objetos fueron exhibidos públicamente y cómo influyó su pátina o apariencia de antigüedad en la percepción?                                     |
| **P4.4 Agencia, ontología y narrativa** | CQ-OBJ-02 | ¿Cómo se distingue la biografía física real (secuencia de eventos materiales) de las biografías narrativas construidas por distintos investigadores? |
|                                         | CQ-OBJ-04 | ¿En qué momento de su biografía un objeto natural adquirió agencia cultural por uso humano sin transformarse físicamente?                            |
| **P4.5 Identificadores y procedencia**  | CQ-OBJ-10 | ¿Qué identificador único se asignó al objeto en el momento de su recuperación en el campo?                                                           |
|                                         | CQ-OBJ-20 | ¿Qué protocolos científicos, técnicas de laboratorio e instrumentos sustentan una determinación de procedencia?                                      |
|                                         | CQ-OBJ-25 | ¿De dónde proceden geológica o geográficamente las materias primas del objeto?                                                                       |
| **P4.6 Evidencia, datos y metodología** | CQ-OBJ-19 | ¿Qué muestras físicas derivan del mismo objeto y qué resultados analíticos contradictorios produjeron distintos laboratorios?                        |
|                                         | CQ-OBJ-21 | ¿Qué conjuntos de datos analíticos se generaron durante el estudio científico del objeto y cómo se documentan?                                       |
|                                         | CQ-OBJ-22 | ¿Qué procesos de calibración o correcciones metodológicas modificaron una datación o clasificación previamente publicada?                            |
|                                         | CQ-OBJ-31 | ¿Qué cadenas argumentativas conectan observaciones empíricas, mediciones de laboratorio e inferencias interpretativas?                               |
| **P4.7 Interpretación disputada**       | CQ-OBJ-28 | ¿Qué hipótesis interpretativas rivales existen sobre la función, cronología o significado cultural del objeto?                                       |
|                                         | CQ-OBJ-29 | ¿Qué interpretaciones funcionales o tipológicas fueron rechazadas y qué evidencia lo motivó?                                                         |
|                                         | CQ-OBJ-30 | ¿Qué niveles de certeza se asignan a las interpretaciones del objeto y cómo se justifican?                                                           |
|                                         | CQ-OBJ-32 | ¿Qué conflictos interpretativos existen entre distintos investigadores sobre la biografía, procedencia o significado del objeto?                     |
| **P4.8 Espacialidad y territorio**      | CQ-OBJ-46 | ¿Qué relaciones topológicas espaciales (proximidad, co-ocurrencia, asociación funcional) conectan el objeto con otros?                               |
|                                         | CQ-OBJ-48 | ¿Qué patrones de distribución espacial dentro de un sitio revelan una zonificación funcional (áreas domésticas, rituales)?                           |
|                                         | CQ-OBJ-50 | ¿Qué correlaciones existen entre la distribución territorial de objetos de un tipo cultural y los períodos geológicos?                               |

---

### CQs del piloto Qwen 3.7-plus, clasificadas por patrón y subgrupo (30 CQs)

Dentro de cada patrón, las preguntas se agrupan en **subgrupos temáticos** según el concepto que abordan.

#### P1 — Eventos (lo que pasó) — 10 CQs


| Subgrupo                                        | CQs       | Pregunta (resumida)                                                     |
| ----------------------------------------------- | --------- | ----------------------------------------------------------------------- |
| **P1.1 Origen y fabricación**                   | CQ-OBJ-01 | ¿Qué eventos de aprovisionamiento de materia prima hubo?                |
|                                                 | CQ-OBJ-05 | ¿Cuál es la secuencia completa de la cadena operativa?                  |
| **P1.2 Vida útil y transformación**             | CQ-OBJ-02 | ¿Qué objetos sufrieron reutilización lateral vs reciclaje?              |
|                                                 | CQ-OBJ-06 | ¿Qué eventos de mantenimiento se realizaron durante la vida útil?       |
| **P1.3 Fin del ciclo: depósito y recuperación** | CQ-OBJ-03 | ¿Qué eventos de descarte llevaron el objeto al registro?                |
|                                                 | CQ-OBJ-08 | ¿Qué eventos de deposición (inhumación, ofrenda, abandono) lo situaron? |
|                                                 | CQ-OBJ-09 | ¿Qué unidades de excavación lo recuperaron y cómo se documentó?         |
| **P1.4 Actores y biografía**                    | CQ-OBJ-04 | ¿Por qué transiciones de persona social pasó durante su biografía?      |
|                                                 | CQ-OBJ-07 | ¿Qué actores, grupos o tradiciones participaron en su producción/uso?   |
|                                                 | CQ-OBJ-10 | ¿Dos o más objetos muestran secuencias biográficas paralelas?           |


#### P2 — Estados (lo que es) — 11 CQs


| Subgrupo                            | CQs       | Pregunta (resumida)                                                      |
| ----------------------------------- | --------- | ------------------------------------------------------------------------ |
| **P2.1 Composición y materialidad** | CQ-OBJ-11 | ¿Qué indicadores internos de datación (isótopos, oxidación) presenta?    |
|                                     | CQ-OBJ-12 | ¿Cuál es la composición material del objeto?                             |
| **P2.2 Alteración y forma**         | CQ-OBJ-16 | ¿Qué alteraciones superficiales (pátina, corrosión, desgaste) presenta?  |
|                                     | CQ-OBJ-17 | ¿Cuál es su estado de fragmentación y qué proporción se conserva?        |
|                                     | CQ-OBJ-18 | ¿Qué atributos morfométricos (dimensiones, peso, forma) tiene?           |
|                                     | CQ-OBJ-20 | ¿Qué valores de color Munsell y apariencia visual presenta?              |
| **P2.3 Contexto físico**            | CQ-OBJ-14 | ¿En qué estado de distribución de desecho se encuentra?                  |
|                                     | CQ-OBJ-15 | ¿En qué unidad de volumen estratigráfico está embebido?                  |
|                                     | CQ-OBJ-19 | ¿Qué partes componentes (asas, tapaderas, hojas) lo componen?            |
| **P2.4 Modo de experiencia**        | CQ-OBJ-13 | ¿Se experimenta como herramienta disponible o como espécimen de estudio? |


#### P4 — Asignaciones (lo que sabemos) — 17 CQs


| Subgrupo                          | CQs       | Pregunta (resumida)                                                     |
| --------------------------------- | --------- | ----------------------------------------------------------------------- |
| **P4.1 Clasificación**            | CQ-OBJ-21 | ¿Bajo qué esquema tipológico (monotético/politético) se clasifica?      |
|                                   | CQ-OBJ-22 | ¿Qué rasgos significativos apoyan su asignación cronológica/cultural?   |
|                                   | CQ-OBJ-23 | ¿Cuál es la fuerza de la relación tipo-período (débil/moderada/fuerte)? |
|                                   | CQ-OBJ-24 | ¿A qué grupo composicional (Leitlegierung) pertenece?                   |
|                                   | CQ-OBJ-29 | ¿A qué universo estilístico ha sido asignado?                           |
| **P4.2 Función**                  | CQ-OBJ-26 | ¿Qué interpretación funcional se le ha asignado?                        |
| **P4.3 Significado y agencia**    | CQ-OBJ-27 | ¿Qué significado cultural/simbólico/ritual se le atribuye?              |
|                                   | CQ-OBJ-28 | ¿Qué agencia material se le ha atribuido y bajo qué marco teórico?      |
| **P4.4 Conocimiento y evidencia** | CQ-OBJ-25 | ¿Qué registros de archivo (cuadernos, bases de datos) lo documentan?    |
|                                   | CQ-OBJ-30 | ¿Qué hipótesis interpretativas rivales existen sobre el objeto?         |


### CQs de extensión posterior

Las CQs 31–38 se conservan en `CQ-object-qwen3.7plus-extension.md`. Se añadieron después del piloto para reforzar los conceptos del brief §7.


| Tipo                    | CQs                   | Motivo                                        |
| ----------------------- | --------------------- | --------------------------------------------- |
| Concepto nuevo          | CQ-OBJ-31             | Materialidad relacional de Knappett           |
| Refuerzo o solapamiento | CQ-OBJ-32 a CQ-OBJ-38 | Refuerzan o reformulan conceptos ya cubiertos |


---

## 3. Conceptos que cubre cada patrón

### Qwen 3.6 — P1 (Event-Driven) — 63 clases arqo

**Conceptos clave:**

- Eventos del ciclo de vida: ManufacturingEvent, UseEvent, ReuseEvent, RepairEvent, CirculationEvent, DepositionEvent, RecoveryEvent, SamplingEvent, ExhibitionEvent, RepatriationEvent, CustodyEvent
- Tafonomía y transformación: TaphonomicAlterationEvent, FragmentationEvent, FunctionalTransformation, PostDepositionalDisplacement
- Análisis: AnalyticalEncounter, AnalyticalObservation, MeasurementEvent, CalibrationEvent, AnalyticalWorkflow
- Interpretación: InterpretiveHypothesis, InterpretiveConclusion, InterpretiveConflict, CompetingInterpretation, RejectedHypothesis, HeritageClaim, CertaintyAssessment
- Espacial: SpatialContext, SpatialCorrelationEvent, TerritorialDistribution, FunctionalZone, CirculationNetwork
- Biografía: ObjectBiography, ObjectLifecycle
- Taxonomía de objetos: ArchaeologicalObject, NaturalObject, HumanMadeObject, Artefact, Structure, ArtisticExpression, AbioticObject, BioticObject

**Clases CIDOC CRM utilizadas:** E5_Event, E7_Activity, E9_Move, E12_Production, E81_Transformation, E19_Physical_Object, E22_Human-Made_Object, E57_Material, E53_Place, E3_Condition_State, E17_Type_Assignment, E73_Information_Object

**Clases CRMarchaeo utilizadas:** A1_Excavation_Process_Unit, A4_Stratigraphic_Genesis, A5_Stratigraphic_Modification_Event

### Qwen 3.6 — P2 (State-Transition) — 34 clases arqo

**Conceptos clave:**

- Estados físicos: CorrosionState, PatinaState, WeatheringState, FragmentationState, IntegrityState, DisplacedState
- Estados de ciclo de vida: ProductionState, UseState, ReuseState, CirculationState, DepositedState, RecoveredState, SampledState, CustodyState, ExhibitionState
- Estados interpretativos: AcceptedState, AnalyzedState, CalibratedState, ConservedState, ContestedState, RejectedState, DigitalDocumentationState, OccupationState, SpatialState, ZoningState
- Transformación: ObjectTransformation

**Clases CIDOC CRM utilizadas:** E19_Physical_Object, E22_Human-Made_Object, E3_Condition_State, E81_Transformation

**Clases CRMarchaeo utilizadas:** Ninguna

### Qwen 3.6 — P4 (Assignment-Intrinsic) — 31 clases arqo

**Conceptos clave:**

- Asignaciones: ArchaeologicalAssignment, TypologicalAssignment, ChronologicalAssignment, FunctionalAssignment, MaterialAssignment, ProvenanceAssignment, SpatialAssignment, BiographyAssignment, LifecycleAssignment, CustodyAssignment, HeritageAssignment, TaphonomicAssignment, TerritorialAssignment, PreservationAssignment
- Interpretación: CertaintyAssessment, CompetingInterpretation, InterpretiveConclusion, InterpretiveConflict, RejectedHypothesis, HeritageClaim
- Estados físicos observables: Patina, Pastness

**Clases CIDOC CRM utilizadas:** E17_Type_Assignment, E19_Physical_Object, E22_Human-Made_Object, E39_Actor, E3_Condition_State

**Clases CRMarchaeo utilizadas:** Ninguna

### Qwen 3.7-plus — P1 (Event-Driven) — CQ-OBJ-01 a 10

**Conceptos clave:**

- Procurement (aprovisionamiento de materia prima)
- Lateral cycling vs recycling (Schiffer)
- Discard (primary/secondary/de facto refuse)
- Social persona transitions
- Chaîne opératoire
- Maintenance/repair
- Actor participation
- Deposition/recovery
- Biographical parallelism

**Clases CIDOC CRM utilizadas:** E12_Production, E7_Activity, E9_Move, E5_Event, E81_Transformation

### Qwen 3.7-plus — P2 (State-Transition) — CQ-OBJ-11 a 20 + 31

**Conceptos clave:**

- Internal clocks (relojes internos)
- Material composition
- Ontological modes (readiness-to-hand vs presence-at-hand)
- Refuse states
- Embedding pattern (A7)
- Surface alterations (patina, pastness)
- Fragmentation
- Morphometrics
- Partonomy
- Visual attributes (color Munsell)
- **Materialidad relacional (Knappett)** — documentada en la extensión posterior, no en las 30 CQs del piloto

**Clases CIDOC CRM utilizadas:** E19_Physical_Object, E26_Physical_Feature, E3_Condition_State, E54_Dimension, E57_Material

### Qwen 3.7-plus — P4 (Assignment-Intrinsic) — CQ-OBJ-21 a 30

**Conceptos clave:**

- Typological assignment
- Significant features
- Type-to-period strength (AP29/AP30/AP31)
- Compositional groups (Leitlegierungen)
- Archive records
- Functional interpretation
- Cultural significance
- Material agency
- Stylistic universes
- Competing hypotheses (multivocality)

**Clases CIDOC CRM utilizadas:** E17_Type_Assignment, E55_Type, E89_Propositional_Object, E13_Attribute_Assignment

---

## 4. Métricas por archivo

Para leer estas tablas: **Clases** = clases nuevas del proyecto; **Obj Props** = propiedades de relación (entre entidades); **Data Props** = propiedades de valor (entidad → valor). Ver Anexo B para más detalle.

### Qwen 3.6 — Patrón 1 (Event-Driven), memoryless temp_0_5


| Archivo       | Clases | Obj Props | Data Props |
| ------------- | ------ | --------- | ---------- |
| CQ-OBJ-01.ttl | ~5-8   | ~3-6      | ~2-4       |
| ...           | ...    | ...       | ...        |
| CQ-OBJ-50.ttl | ~5-8   | ~3-6      | ~2-4       |
| **Promedio**  | ~6     | ~4        | ~3         |


*(Muestra: los archivos memoryless de qwen 3.6 tienen ~6 clases, ~4 obj props, ~3 data props por archivo)*

### Qwen 3.7-plus — Memoryless temp_0_5


| Archivo       | Clases   | Obj Props | Data Props |
| ------------- | -------- | --------- | ---------- |
| CQ-OBJ-01.ttl | 6        | 5         | 2          |
| CQ-OBJ-02.ttl | 5        | 5         | 2          |
| CQ-OBJ-03.ttl | 7        | 5         | 2          |
| CQ-OBJ-04.ttl | 6        | 6         | 2          |
| CQ-OBJ-05.ttl | 7        | 7         | 2          |
| **Promedio**  | **~6.2** | **~5.6**  | **~2**     |


### Métricas por patrón (cumulative ontogenia temp_0_5)


| Experimento       | Clases arqo | Obj Props | Data Props | Líneas |
| ----------------- | ----------- | --------- | ---------- | ------ |
| **Qwen 3.6 P1**   | 63          | 54        | 37         | 836    |
| **Qwen 3.6 P2**   | 34          | 29        | 20         | 401    |
| **Qwen 3.6 P4**   | 31          | 24        | 15         | 346    |
| **Qwen 3.7-plus** | 59          | 97        | 56         | 1112   |


---

## 5. Patrones ontológicos implementados

### Qwen 3.6 — Patrón P1 (Event-Driven)

**Clases CIDOC CRM usadas:** E5_Event, E7_Activity, E9_Move, E12_Production, E81_Transformation, E19_Physical_Object, E22_Human-Made_Object, E57_Material, E53_Place, E3_Condition_State, E17_Type_Assignment, E73_Information_Object

**Clases CRMarchaeo usadas:** A1_Excavation_Process_Unit, A4_Stratigraphic_Genesis, A5_Stratigraphic_Modification_Event

**Conceptos clave:** eventos del ciclo de vida, tafonomía, análisis, interpretación, espacial, biografía

### Qwen 3.6 — Patrón P2 (State-Transition)

**Clases CIDOC CRM usadas:** E19_Physical_Object, E22_Human-Made_Object, E3_Condition_State, E81_Transformation

**Clases CRMarchaeo usadas:** Ninguna

**Conceptos clave:** estados físicos (corrosión, pátina, desgaste, fragmentación), estados de ciclo de vida, estados interpretativos

### Qwen 3.6 — Patrón P4 (Assignment-Intrinsic)

**Clases CIDOC CRM usadas:** E17_Type_Assignment, E19_Physical_Object, E22_Human-Made_Object, E39_Actor, E3_Condition_State

**Clases CRMarchaeo usadas:** Ninguna

**Conceptos clave:** asignaciones interpretativas (tipología, cronología, función, material, procedencia), certeza, hipótesis rivales

### Qwen 3.7-plus — Patrón P1 (Event-Driven)

**Clases CIDOC CRM usadas:** E12_Production, E7_Activity, E9_Move, E5_Event, E81_Transformation

**Conceptos clave:** procurement, cycling, discard, social persona, chaîne opératoire, maintenance, deposition, recovery

### Qwen 3.7-plus — Patrón P2 (State-Transition)

**Clases CIDOC CRM usadas:** E19_Physical_Object, E26_Physical_Feature, E3_Condition_State, E54_Dimension, E57_Material

**Clases CRMarchaeo usadas:** A7_Embedding

**Conceptos clave:** internal clocks, material composition, ontological modes, refuse states, embedding, fragmentation, morphometrics, partonomy, visual attributes

### Qwen 3.7-plus — Patrón P4 (Assignment-Intrinsic)

**Clases CIDOC CRM usadas:** E17_Type_Assignment, E55_Type, E89_Propositional_Object, E13_Attribute_Assignment

**Clases CRMinf usadas:** I4_Proposition_Set

**Clases CRMsci usadas:** S4_Observation, S21_Measurement

**Conceptos clave:** typological assignment, significant features, type-to-period strength, compositional groups, archive records, functional interpretation, cultural significance, material agency, stylistic universes, competing hypotheses

---

## 6. Alineación con ontologías de referencia

### Qwen 3.6 — Patrón 1 (Event-Driven)


| Ontología      | Clases usadas                                          | Grado de alineación |
| -------------- | ------------------------------------------------------ | ------------------- |
| **CIDOC CRM**  | E5, E7, E9, E12, E81, E19, E22, E57, E53, E3, E17, E73 | Alta (12 clases)    |
| **CRMarchaeo** | A1, A4, A5                                             | Media (3 clases)    |
| **CRMsci**     | No usa                                                 | Baja                |
| **CRMinf**     | No usa                                                 | Baja                |


### Qwen 3.6 — Patrón 2 (State-Transition)


| Ontología      | Clases usadas     | Grado de alineación |
| -------------- | ----------------- | ------------------- |
| **CIDOC CRM**  | E19, E22, E3, E81 | Media (4 clases)    |
| **CRMarchaeo** | Ninguna           | Baja                |


### Qwen 3.6 — Patrón 4 (Assignment-Intrinsic)


| Ontología      | Clases usadas          | Grado de alineación |
| -------------- | ---------------------- | ------------------- |
| **CIDOC CRM**  | E17, E19, E22, E39, E3 | Media (5 clases)    |
| **CRMarchaeo** | Ninguna                | Baja                |


### Qwen 3.7-plus (piloto)


| Ontología      | Clases usadas                                                                                               | Grado de alineación  |
| -------------- | ----------------------------------------------------------------------------------------------------------- | -------------------- |
| **CIDOC CRM**  | E1, E3, E4, E5, E7, E9, E11, E13, E17, E19, E26, E29, E31, E39, E52, E53, E55, E57, E73, E74, E78, E81, E89 | **Alta (23 clases)** |
| **CRMarchaeo** | A1, A2, A4, A7, A8                                                                                          | **Alta (5 clases)**  |
| **CRMsci**     | S4, S21                                                                                                     | Media (2 clases)     |
| **CRMinf**     | I4                                                                                                          | Media (1 clase)      |


**Conclusión de alineación:** El piloto qwen 3.7-plus tiene una **alineación significativamente mayor** con CIDOC CRM (23 clases vs 4-12 de qwen 3.6) y con CRMarchaeo (5 clases vs 0-3). También incorpora CRMsci y CRMinf, ausentes en el experimento con patrones de qwen 3.6.

---

## 7. Clases y propiedades nuevas

### Qwen 3.6 — Patrón 1 (Event-Driven) — 63 clases

**Eventos:** ManufacturingEvent, UseEvent, ReuseEvent, RepairEvent, CirculationEvent, DepositionEvent, RecoveryEvent, SamplingEvent, ExhibitionEvent, RepatriationEvent, CustodyEvent, CalibrationEvent, MeasurementEvent, GeomorphologicalEvent, SpatialCorrelationEvent, TaphonomicAlterationEvent, FragmentationEvent, PostDepositionalDisplacement

**Interpretación:** InterpretiveHypothesis, InterpretiveConclusion, InterpretiveConflict, CompetingInterpretation, RejectedHypothesis, HeritageClaim, CertaintyAssessment, ChronologicalAssignment, TypologicalAssignment

**Espacial:** SpatialContext, SpatialCorrelationEvent, TerritorialDistribution, FunctionalZone, CirculationNetwork, OccupationPhase, PaleoenvironmentalCorrelation, GeologicalCorrelation

**Objetos:** ArchaeologicalObject, NaturalObject, HumanMadeObject, Artefact, Structure, ArtisticExpression, AbioticObject, BioticObject

**Otros:** ObjectBiography, ObjectLifecycle, AnalyticalWorkflow, AnalyticalEncounter, AnalyticalObservation, AnalyticalDataset, ConservationDecision, ConservationTreatment, CustodyChain, DigitalReplica, FunctionalTransformation, TaphonomicProcess, Pastness, Patina, CorrosionState, DisplacedState, FragmentationState, IntegrityState, PatinaState, WeatheringState

**Propiedades:** 54 object props + 37 data props

### Qwen 3.6 — Patrón 2 (State-Transition) — 34 clases

**Estados:** ProductionState, UseState, ReuseState, CirculationState, DepositedState, RecoveredState, SampledState, CustodyState, ExhibitionState, AcceptedState, AnalyzedState, CalibratedState, ConservedState, ContestedState, RejectedState, DigitalDocumentationState, OccupationState, SpatialState, ZoningState, CorrosionState, PatinaState, WeatheringState, FragmentationState, IntegrityState, DisplacedState

**Otros:** ObjectTransformation

**Propiedades:** 29 object props + 20 data props

### Qwen 3.6 — Patrón 4 (Assignment-Intrinsic) — 31 clases

**Asignaciones:** ArchaeologicalAssignment, TypologicalAssignment, ChronologicalAssignment, FunctionalAssignment, MaterialAssignment, ProvenanceAssignment, SpatialAssignment, BiographyAssignment, LifecycleAssignment, CustodyAssignment, HeritageAssignment, TaphonomicAssignment, TerritorialAssignment, PreservationAssignment

**Interpretación:** CertaintyAssessment, CompetingInterpretation, InterpretiveConclusion, InterpretiveConflict, RejectedHypothesis, HeritageClaim

**Propiedades:** 24 object props + 15 data props

### Qwen 3.7-plus (piloto) — 59 clases

**Objeto y Materialidad:** ArchaeologicalObject, ComponentPart, MaterialAgencyAttribution, MaterialComponent, MaterialRelation, ObjectBiography, RawMaterialSource

**Biografía y Ciclo de Vida:** SocialPersona, SocialPersonaTransition

**Eventos de Producción:** CraftTradition, ProcurementEvent, TechnicalAction

**Eventos de Uso y Reuso:** DeFactoRefuse, LateralCyclingEvent, MaintenanceEvent, PrimaryRefuse, RecyclingEvent, RefuseDistributionState, ReuseEvent, SecondaryRefuse

**Eventos de Deposición:** CasualAbandonment, DepositionEvent, DiscardEvent, IntentionalBurial, RitualOffering

**Eventos de Recuperación:** RecoveryDocumentation, RecoveryEvent, RecoveryObservation

**Contexto y Embebido:** EmbeddingRelation

**Tipología y Clasificación:** ClassificationMethod, CompositionalGroup, CompositionalGroupAssignment, TypeToPeriodRelationship

**Análisis y Medición:** InternalClockIndicator, InternalClockMeasurement

**Interpretación y Significado:** ArchaeologicalArchiveRecord, ArchiveCollection, CulturalSignificanceAssignment, InterpretiveHypothesis, PastnessQuality

**Actores y Grupos:** CulturalCommunity

**Otros:** BiographicalParallelism, ChaineOperatoire, EmergencyCaching, FeatureEvidenceLink, FragmentationState, FunctionalAssignment, JoiningTechnique, ModeOfExperience, MorphometricAttribute, OntologicalShiftEvent, PresenceAtHand, ReadinessToHand, SignificantFeature, StylisticAssignment, StylisticUniverse, SurfaceAlteration, TypologicalAssignment, VisualAppearanceAttribute

**Propiedades:** 97 object props + 56 data props

---

## 8. Tabla de métricas comparativas


| Métrica                      | Qwen 3.6 P1 | Qwen 3.6 P2 | Qwen 3.6 P4 | Qwen 3.7-plus |
| ---------------------------- | ----------- | ----------- | ----------- | ------------- |
| **CQs**                      | 50          | 50          | 50          | 30            |
| **Clases arqo (cumulative)** | 63          | 34          | 31          | 59            |
| **Object Props**             | 54          | 29          | 24          | 97            |
| **Data Props**               | 37          | 20          | 15          | 56            |
| **Clases CRM usadas**        | 12          | 4           | 5           | 23            |
| **Clases CRMarchaeo usadas** | 3           | 0           | 0           | 5             |
| **Clases CRMsci**            | 0           | 0           | 0           | 2             |
| **Clases CRMinf**            | 0           | 0           | 0           | 1             |
| **Líneas cumulative**        | 836         | 401         | 346         | 1112          |
| **Archivos memoryless**      | 50          | 50          | 50          | 30            |
| **Temperaturas**             | 0.3/0.5/0.7 | 0.3/0.5/0.7 | 0.3/0.5/0.7 | 0.5           |
| **Validación TTL**           | 100%        | 100%        | 100%        | 100%          |


**Lectura clave:**

- Qwen 3.7-plus tiene **más propiedades** (97 obj + 56 data) que cualquier patrón individual de qwen 3.6 (máx 54 + 37)
- Qwen 3.7-plus tiene **mejor alineación CRM** (23 clases vs máx 12)
- Qwen 3.7-plus usa **4 ontologías de referencia** (CRM, CRMarchaeo, CRMsci, CRMinf) vs solo 2 de qwen 3.6
- Qwen 3.6 P1 es el más rico de los 3 patrones (63 clases) pero con menor alineación

---

## 9. Observaciones y hallazgos

### 1. Cobertura conceptual

**Qwen 3.6 con patrones:**

- P1 cubre eventos del ciclo de vida + tafonomía + interpretación + espacial
- P2 cubre estados físicos y de ciclo de vida
- P4 cubre asignaciones interpretativas

**Qwen 3.7-plus:**

- Las 30 CQs del piloto cubren los conceptos clave del brief §1 (biografía, materialidad, contexto, tipología, agencia, pastness, relojes internos, archivo)
- Las 8 CQs de extensión posterior se conservan aparte y no forman parte de estas métricas

### 2. Patrones de modelado

**Qwen 3.6:** Los 3 patrones son **estrategias separadas** — el modelo genera la misma CQ de forma diferente según el patrón activo

**Qwen 3.7-plus:** Los 3 patrones son **clasificaciones dentro del mismo archivo** — el modelo sabe el patrón de cada CQ pero genera un corpus coherente

### 3. Alineación ontológica

- Qwen 3.7-plus duplica la alineación CRM (23 vs 12 clases)
- Qwen 3.7-plus es el único que usa CRMsci y CRMinf
- Qwen 3.6 P2/P4 no usan CRMarchaeo

### 4. Riqueza ontológica

- Qwen 3.7-plus genera 97 object props vs máx 54 de qwen 3.6
- Qwen 3.7-plus genera 56 data props vs máx 37 de qwen 3.6
- El cumulative de qwen 3.7-plus (1112 líneas) supera a cualquier patrón de qwen 3.6 (máx 836)

---

## 10. Memoryless vs Ontogenia

### Qwen 3.6 — Patrón 1 (Event-Driven)

**Memoryless:**

- 50 archivos independientes
- Cada CQ genera un fragmento autónomo
- Mayor diversidad, menor coherencia global

**Ontogenia:**

- 50 pasos acumulativos + cumulative.ttl
- 836 líneas finales
- 63 clases, 54 obj props, 37 data props
- Crecimiento controlado con reuso

### Qwen 3.6 — Patrón 2 (State-Transition)

**Memoryless:**

- 50 archivos independientes

**Ontogenia:**

- 401 líneas finales
- 34 clases, 29 obj props, 20 data props

### Qwen 3.6 — Patrón 4 (Assignment-Intrinsic)

**Memoryless:**

- 50 archivos independientes

**Ontogenia:**

- 346 líneas finales
- 31 clases, 24 obj props, 15 data props

### Qwen 3.7-plus

**Memoryless:**

- 30 archivos independientes (CQ-OBJ-01 a 30)
- ~6.2 clases, ~5.6 obj props, ~2 data props por archivo
- Total aprox: ~190 clases, ~140 obj props, ~70 data props

**Ontogenia:**

- 30 pasos acumulativos + cumulative.ttl
- 1112 líneas finales
- 59 clases, 97 obj props, 56 data props
- Crecimiento: step_01 = 4.1 KB → step_30 = 64 KB

### Comparativa de estrategias


| Aspecto                  | Memoryless                | Ontogenia                 |
| ------------------------ | ------------------------- | ------------------------- |
| **Contexto**             | Vacío en cada CQ          | Acumulado paso a paso     |
| **Diversidad de clases** | Mayor                     | Menor (reuso)             |
| **Coherencia global**    | Menor                     | Mayor                     |
| **Crecimiento**          | No aplica                 | Controlado (4 KB → 64 KB) |
| **Reuso de clases**      | Mínimo                    | Alto                      |
| **Resultado**            | Fragmentos independientes | Ontología coherente       |


**Hallazgo:** En ambos experimentos, ontogenia produce una ontología más coherente con reutilización de clases, mientras memoryless genera fragmentos más diversos pero menos integrados. Qwen 3.7-plus en ontogenia alcanza 59 clases coherentes vs ~190 clases dispersas en memoryless.

---

## 11. Análisis crítico

### Verificación de cobertura conceptual

Los 8 conceptos del dominio identificados como prioritarios en el brief (§7) **están representados** en las 59 clases `arqo:` del piloto:

1. ✅ **Materialidad relacional (Knappett)** — `MaterialRelation`, `MaterialComponent`
2. ✅ **Affordances / agencia material** — `MaterialAgencyAttribution`
3. ✅ **Type-to-period strength** — `TypeToPeriodRelationship`
4. ✅ **Significant features** — `SignificantFeature`, `FeatureEvidenceLink`
5. ✅ **Compositional groups (Leitlegierungen)** — `CompositionalGroup`, `CompositionalGroupAssignment`
6. ✅ **Functional assignment** — `FunctionalAssignment`
7. ✅ **Cultural significance** — `CulturalSignificanceAssignment`
8. ✅ **Competing hypotheses / multivocality** — `InterpretiveHypothesis`

Esta verificación confirma que los 8 conceptos están **cubiertos** en el piloto, pero **no** que las mejoras de §12 hayan tenido el efecto buscado.

> ⚠️ **La causalidad está invertida en versiones anteriores de este documento.** Las 8 clases ya existían en el `cumulative.ttl` del piloto, que se generó **antes** de que se creara la sección §7 y con la **versión 1** del prompt (`ALWAYS check`, sin balance guideline). Es decir: el modelo las creó por su cuenta a partir de las 30 CQs originales, no porque §7 ni el balance guideline las provocaran. Medir el efecto real de las mejoras exige regenerar las ontologías con la versión 2 del prompt y las CQs de extensión — propuesta 11 de §12.2, todavía no ejecutada.

### Ventajas del piloto qwen 3.7-plus

1. **Mayor alineación CRM** (23 clases vs 12)
2. **Mayor riqueza ontológica** (97 obj props vs 54)
3. **Uso de 4 ontologías de referencia** (vs 2)
4. **Conceptos teóricos más sofisticados** (materialidad, pastness, affordances)
5. **Corpus coherente** (no fragmentos separados por patrón)

> **Nota:** el piloto **no** se generó con el brief §7 ni con el balance guideline (se añadieron después; ver §12), por lo que la cobertura de esos 8 conceptos **no es atribuible** a esas mejoras.

### Limitaciones del piloto qwen 3.7-plus

1. **Menos CQs** (30 vs 50) — menor cobertura de eventos específicos
2. **Solo temperatura 0.5** — no hay comparación entre temperaturas
3. **Menos clases de eventos** que qwen 3.6 P1 (no modela Exhibition, Repatriation, Custody, Sampling como eventos)
4. **P1 con solo 10 CQs** — menor profundidad en eventos del ciclo de vida

### Limitaciones del experimento qwen 3.6 con patrones

1. **Las mismas 50 CQs modeladas 3 veces** (una por patrón) — no son CQs distintas
2. **Baja alineación CRM** en P2 y P4 (4-5 clases)
3. **Sin CRMsci/CRMinf**
4. **Patrones aislados** — cada patrón genera un corpus separado, sin integración

### Diferencias metodológicas


| Aspecto         | Qwen 3.6 con patrones      | Qwen 3.7-plus piloto                                                                         |
| --------------- | -------------------------- | -------------------------------------------------------------------------------------------- |
| **CQs**         | 50 unificadas              | 30 en el piloto + 8 en una extensión posterior                                               |
| **Patrones**    | 3 experimentos separados   | 1 corpus con 3 patrones                                                                      |
| **Temperatura** | 3 valores                  | 1 valor (0.5)                                                                                |
| **Brief**       | Sin sección de extensiones | Sin §7 (el piloto es anterior a §7)                                                          |
| **Prompt**      | v1 — `ALWAYS reuse CRM`    | v1 — `ALWAYS reuse CRM` (la v2 con balance guideline llegó después y no se aplicó al piloto) |


---

## 12. Mejoras propuestas e implementadas

### 12.1 Mejoras implementadas (2026-08-28)

> **Alcance real (revisión 2026-09-11).** Las mejoras de esta sección son **insumos del pipeline** (brief, CQs y prompts), incorporadas al repositorio en el commit `b04411f` (2026-09-01; trabajo fechado 2026-08-28).
>
> **Ninguna se ejecutó sobre el piloto.** Las ontologías de `Qwen3.7plus/` son del commit `9a827d9` (2026-08-28) y se generaron con la **versión 1** del prompt. No existe ningún `.ttl` generado para las CQs de extensión (CQ-OBJ-31 a 38). En consecuencia, los resultados comparados en este documento **no reflejan** estas mejoras; medirlas exige regenerar (ver §12.2, propuesta 11).

#### ✅ Mejora 1: Brief con sección de extensiones (§7)

**Problema:** El brief original listaba clases CRM/CRMarchaeo pero no indicaba qué conceptos requieren extensión `arqo:`.

**Solución implementada:** Se agregó la sección §7 "Conceptos que requieren extensión arqo:" con 8 conceptos:


| Concepto                               | Clases arqo requeridas                               |
| -------------------------------------- | ---------------------------------------------------- |
| Materialidad relacional (Knappett)     | `MaterialRelation`, `MaterialComponent`              |
| Affordances / agencia material         | `MaterialAgencyAttribution`                          |
| Type-to-period strength                | `TypeToPeriodRelationship`                           |
| Significant features                   | `SignificantFeature`, `FeatureEvidenceLink`          |
| Compositional groups (Leitlegierungen) | `CompositionalGroup`, `CompositionalGroupAssignment` |
| Functional assignment                  | `FunctionalAssignment`                               |
| Cultural significance                  | `CulturalSignificanceAssignment`                     |
| Competing hypotheses / multivocality   | `InterpretiveHypothesis`                             |


**Impacto esperado (no medido):** se espera que el generador sepa qué conceptos requieren extensiones `arqo:` en lugar de forzar reuso CRM. El piloto comparado no se regeneró, así que este efecto no está verificado.

#### ✅ Mejora 2: CQs adicionales de extensión

**Problema:** Las CQs originales no forzaban explícitamente la creación de extensiones para conceptos teóricos.

**Solución implementada:** Se creó un conjunto de extensión separado con 8 CQs (CQ-OBJ-31 a CQ-OBJ-38) que referencia explícitamente los conceptos de la sección §7. Estas preguntas no forman parte del piloto original de 30 CQs:


| CQ        | Concepto §7                          | Patrón |
| --------- | ------------------------------------ | ------ |
| CQ-OBJ-31 | Materialidad relacional (Knappett)   | P2     |
| CQ-OBJ-32 | Affordances / agencia material       | P4     |
| CQ-OBJ-33 | Type-to-period strength              | P4     |
| CQ-OBJ-34 | Significant features                 | P4     |
| CQ-OBJ-35 | Compositional groups                 | P4     |
| CQ-OBJ-36 | Functional assignment                | P4     |
| CQ-OBJ-37 | Cultural significance                | P4     |
| CQ-OBJ-38 | Competing hypotheses / multivocality | P4     |


**Impacto esperado (no medido):** cada concepto de extensión tiene al menos una CQ que fuerza su modelado, pero **no se ha generado ninguna ontología** con estas 8 CQs; permanecen archivadas en `CQ-object-qwen3.7plus-extension.md`.

#### ✅ Mejora 3: Prompts con balance guideline

**Problema:** El prompt decía "ALWAYS check if CIDOC CRM provides it" — demasiado conservador, favorecía reutilización forzada.

**Solución implementada:** Se agregó un "Balance guideline" en ambos prompts (memoryless y ontogenia):

- **Preferir reuso CRM** para conceptos generales (eventos, actores, lugares, tiempos)
- **Crear extensiones `arqo:`** cuando el concepto sea arqueológicamente específico (material agency, relational materiality, type-to-period strength, etc.)
- **"When in doubt, create an `arqo:` class that extends CRM"**

**Impacto esperado (no medido):** se espera que el modelo cree más extensiones `arqo:`. El piloto no se regeneró con esta versión, así que su efecto sobre las clases `arqo:` sigue sin medirse.

#### ⏳ Mejora 4: Validación intermedia (pendiente)

**Problema:** No se verificaba que cada concepto del brief tuviera al menos una CQ.

**Solución pendiente:** Script de mapeo concepto→CQ (`scripts/validate_cq_coverage.py`).

### 12.2 Propuestas de mejora futuras

Estas mejoras **no están implementadas todavía** y se proponen para las próximas iteraciones. Se presentan ordenadas por prioridad.

#### 🔴 Prioridad alta


| #   | Propuesta                                                                 | Qué resolvería                                                                                                                 | Esfuerzo |
| --- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| 1   | **Consolidar las CQs duplicadas**                                         | Las CQs 32–38 reformulan conceptos ya cubiertos por las 22–30. Consolidarlas daría un set limpio de **31 conceptos distintos** | Bajo     |
| 2   | **Adoptar los subgrupos temáticos** (P1.1, P1.2…) como estructura oficial | Facilita la lectura, la validación con expertos y la detección de vacíos temáticos                                             | Bajo     |
| 3   | **Validación intermedia** (concepto → CQ)                                 | Detecta automáticamente si algún concepto del brief no tiene pregunta asignada                                                 | Medio    |
| 4   | **Evaluación con expertos arqueólogos**                                   | Valida que las preguntas y las clases sean arqueológicamente correctas, no solo técnicamente válidas                           | Medio    |


#### 🟡 Prioridad media


| #   | Propuesta                                                                          | Qué resolvería                                                                                                     | Esfuerzo |
| --- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| 5   | **Medir cobertura CQ → ontología con SPARQL**                                      | Comprueba que cada pregunta puede responderse realmente contra la ontología generada (no solo que la clase exista) | Medio    |
| 6   | **Verificar consistencia lógica con un reasoner OWL**                              | Detecta clases insatisfacibles, contradicciones y axiomas mal formados                                             | Medio    |
| 7   | **Extender el pipeline a los otros 3 bloques** (espacial, temporal, estratigrafía) | Actualmente solo está completo el bloque de objeto                                                                 | Alto     |
| 8   | **Comparar más modelos LLM** (deepseek, kimi, glm…)                                | Permite una comparativa cross-model robusta                                                                        | Medio    |


#### 🟢 Prioridad baja (exploratoria)


| #   | Propuesta                                                             | Qué resolvería                                                           | Esfuerzo |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------- |
| 9   | **Comparar temperaturas** (0.3, 0.5, 0.7) en el piloto                | El piloto solo usó temperatura 0.5; faltan los extremos                  | Bajo     |
| 10  | **Añadir métricas de determinismo** (misma pregunta, dos ejecuciones) | Mide la estabilidad del modelo ante el mismo prompt                      | Medio    |
| 11  | **Regenerar con los prompts mejorados** y comparar antes/después      | Mide el impacto real del balance guideline en las clases `arqo:` creadas | Bajo     |


> **Recomendación:** empezar por las propuestas 1, 2 y 3 (bajo esfuerzo, alto impacto en claridad y rigor), que preparan el terreno para la evaluación con expertos (propuesta 4).

---

## 13. Prompts antiguos vs nuevos

> **Versiones archivadas.** La versión original (v1) y la nueva (v2, balance guideline) se conservan en el repositorio para comparación directa:
>
>
> | Estrategia | v1 — original                                                    | v2 — activa (balance guideline)                      |
> | ---------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
> | Memoryless | `prompts/memoryless/prompt_archaeological_object_v1_original.md` | `prompts/memoryless/prompt_archaeological_object.md` |
> | Ontogenia  | `prompts/ontogenia/prompt_archaeological_object_v1_original.md`  | `prompts/ontogenia/prompt_archaeological_object.md`  |
>
>
> El `procedure.md` de ontogenia **no cambió** entre versiones.
>
> **Aviso de aplicación:** el piloto comparado en este documento se generó con la **v1**. La **v2 nunca se ha ejecutado** para generar ontologías.

### 13.1 Prompt Memoryless

**Archivos:**

- v1 (antes): `prompts/memoryless/prompt_archaeological_object_v1_original.md`
- v2 (después, activa): `prompts/memoryless/prompt_archaeological_object.md`

#### Antes (cab6189):

```
### 1. CIDOC CRM Alignment

Before creating any new class or property, ALWAYS check if CIDOC CRM or CRMarchaeo already provides it:

- **Physical objects:** `crm:E19_Physical_Object`
- **Human-made objects:** `crm:E22_Human-Made_Object`
- ...
```

**Problema:** La palabra "ALWAYS" (siempre) era demasiado estricta. El modelo debía verificar primero si CRM lo proporciona, y solo crear nuevas clases si no existía — pero no había guía sobre cuándo un concepto específico merecía una extensión.

#### Después (b04411f):

```
### 1. CIDOC CRM Alignment

Before creating any new class or property, check if CIDOC CRM or CRMarchaeo already provides it:

- **Physical objects:** `crm:E19_Physical_Object`
- **Human-made objects:** `crm:E22_Human-Made_Object`
- ...

**Balance guideline:**
- **Prefer CIDOC CRM reuse** for general concepts (events, actors, places, time-spans)
- **Create `arqo:` extensions** when the concept is archaeologically specific and not adequately captured by CRM, such as:
  - Material agency and affordances (Gibson, Hodder)
  - Relational materiality (Knappett's four properties)
  - Type-to-period strength relationships
  - Compositional groups (Leitlegierungen)
  - Significant features and evidential links
  - Functional and cultural significance assignments
  - Competing interpretive hypotheses

When in doubt, create an `arqo:` class that extends CRM rather than forcing a CRM class to cover an archaeologically specific concept. See brief §7 "Conceptos que requieren extensión arqo:" for detailed guidance.
```

**Cambios clave:**

1. `ALWAYS check` → `check` (menos estricto)
2. Agregado "Balance guideline" con 2 reglas claras
3. Agregada lista de conceptos que requieren extensión
4. Agregada regla final: "When in doubt, create an `arqo:` class"

### 13.2 Prompt Ontogenia

**Archivos:**

- v1 (antes): `prompts/ontogenia/prompt_archaeological_object_v1_original.md`
- v2 (después, activa): `prompts/ontogenia/prompt_archaeological_object.md`
- Procedimiento: `prompts/ontogenia/procedure.md` (sin cambios entre versiones)

#### Antes (cab6189):

```
| `{ontology_elements}` | "Classes, Object Properties, Datatype Properties. Object properties need domain and range. All need rdfs:label and rdfs:comment. Add restrictions where justified. Prefer CIDOC CRM alignment. Reify assignments (E17_Type_Assignment pattern) and observations (S4_Observation pattern)."
```

#### Después (b04411f):

```
| `{ontology_elements}` | "Classes, Object Properties, Datatype Properties. Object properties need domain and range. All need rdfs:label and rdfs:comment. Add restrictions where justified. **Balance guideline:** Prefer CIDOC CRM reuse for general concepts, but create `arqo:` extensions when the concept is archaeologically specific and not adequately captured by CRM (e.g., material agency/affordances, relational materiality, type-to-period strength, compositional groups/Leitlegierungen, significant features, functional/cultural significance assignments, competing hypotheses). See brief §7 'Conceptos que requieren extensión arqo:' for detailed guidance. Reify assignments (E17_Type_Assignment pattern) and observations (S4_Observation pattern)."
```

**Cambios clave:**

1. `Prefer CIDOC CRM alignment` → balance guideline explícito
2. Agregada lista de conceptos que requieren extensión
3. Referencia al brief §7

### 13.3 Resumen de cambios en prompts


| Aspecto                    | Antes            | Después                                                       |
| -------------------------- | ---------------- | ------------------------------------------------------------- |
| **Postura**                | ALWAYS reuse CRM | Prefer reuse, pero crear extensiones cuando sea específico    |
| **Conceptos de extensión** | No listados      | 7 categorías listadas                                         |
| **Regla final**            | Ninguna          | "When in doubt, create `arqo:` extension"                     |
| **Referencia al brief**    | No               | Brief §7                                                      |
| **¿Usada en el piloto?**   | Sí (v1)          | **No** — la v2 se incorporó después y nunca generó ontologías |


---

## 14. Conclusiones

### Sobre las preguntas (CQs)

1. El piloto usa menos preguntas (30 vs 50) pero **más específicas y mejor fundamentadas teóricamente**
2. La distribución por patrón es más equilibrada en el piloto
3. El piloto tiene 30 preguntas originales; la extensión posterior añade 8 preguntas para trazabilidad y cobertura del brief, pero no altera las métricas del piloto

### Sobre la ontología generada

1. **El piloto supera al experimento anterior en riqueza y alineación**: 97 relaciones entre conceptos vs 54 como máximo, y 23 clases de estándar reutilizadas vs 12
2. **El piloto usa 4 ontologías de referencia** (CIDOC CRM, CRMarchaeo, CRMsci, CRMinf) frente a solo 2 del experimento anterior
3. **El experimento anterior era más rico en eventos específicos** (63 clases) pero con menor alineación con los estándares
4. **Los patrones de estados y asignaciones del experimento anterior apenas reutilizan CRMarchaeo** (0 clases)

### Sobre las mejoras aplicadas

1. La sección §7 del brief **pretende dar** al modelo instrucciones explícitas sobre cuándo crear clases nuevas propias del proyecto
2. Las preguntas de extensión **fuerzan** (por diseño) el modelado de conceptos teóricos que de otro modo se perderían
3. La guía de equilibrio en los prompts **pretende corregir** el sesgo hacia la reutilización forzada de estándares

> ⚠️ **Ninguna de estas mejoras está validada todavía.** Están implementadas como insumos (brief, CQs y prompts), pero el piloto que se compara se generó **antes** de ellas y con la **v1** del prompt. Las afirmaciones anteriores son hipótesis de diseño, **no resultados medidos**. La comprobación pendiente es la propuesta 11 de §12.2: regenerar y comparar antes/después.

### Próximos pasos

1. ⏳ Implementar la validación concepto → pregunta (detecta conceptos sin cobertura)
2. ⏳ **Regenerar las ontologías con la v2 de los prompts y las CQs de extensión**, y comparar antes/después (mide el impacto real del balance guideline)
3. Consolidar las preguntas duplicadas (32–38) para dejar un set limpio de **31 conceptos distintos**
4. Ejecutar el pipeline completo en ambas estrategias de generación

---

## Anexo A. Glosario de términos técnicos

Para facilitar la lectura a perfiles no informáticos.

### Conceptos de ontologías


| Término                 | En palabras llanas                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ontología**           | Representación formal y legible por máquina del conocimiento de un dominio. Define qué tipos de cosas existen y cómo se relacionan.                                                                                |
| **Clase**               | Un *tipo de cosa* del dominio (p. ej. "objeto arqueológico", "evento de producción").                                                                                                                              |
| **Propiedad**           | Una *relación* entre dos cosas, o entre una cosa y un valor (p. ej. "está hecho de", "tiene fecha").                                                                                                               |
| **Subclase**            | Relación "es un tipo de". Si `A` es subclase de `B`, toda `A` es también una `B`.                                                                                                                                  |
| **Reificar**            | Convertir una relación en una entidad con identidad propia, para poder darle atributos (autor, fecha, certeza). Ejemplo: "A está hecho de B" se convierte en "Asignación de material, hecha por X, con certeza Y". |
| **Propiedad de objeto** | Relación entre dos entidades (p. ej. "el objeto *fue producido por* el evento").                                                                                                                                   |
| **Propiedad de dato**   | Relación entre una entidad y un valor literal (p. ej. "el objeto *tiene peso* 250 gramos").                                                                                                                        |
| **Axioma**              | Regla formal que la ontología declara como verdadera (p. ej. "todo objeto arqueológico es un objeto físico").                                                                                                      |


### Estándares y formatos


| Término             | En palabras llanas                                                                                                                        |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CIDOC CRM**       | Estándar internacional para el patrimonio cultural. Define las clases y relaciones básicas (objetos, eventos, actores, lugares, tiempos). |
| **CRMarchaeo**      | Extensión de CIDOC CRM específica para excavación y estratigrafía.                                                                        |
| **CRMsci / CRMinf** | Extensiones de CIDOC CRM para observación científica (CRMsci) e inferencia y argumentación (CRMinf).                                      |
| **TTL / Turtle**    | Formato de archivo de texto en el que se escriben las ontologías. Es legible por humanos y por máquinas.                                  |
| **OWL**             | Lenguaje estándar para expresar ontologías con lógica formal.                                                                             |
| **SPARQL**          | Lenguaje de consulta para buscar información en ontologías.                                                                               |
| **Reasoner**        | Programa que verifica automáticamente la coherencia lógica de una ontología (detecta contradicciones).                                    |


### Nomenclatura del proyecto


| Término               | En palabras llanas                                                                                                                             |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `**arqo:**`           | Prefijo de las clases y propiedades **nuevas** creadas por el proyecto. Las heredadas de estándares usan prefijos como `crm:` o `crmarchaeo:`. |
| **Memoryless**        | Estrategia de generación "sin memoria": cada pregunta se responde por separado.                                                                |
| **Ontogenia**         | Estrategia de generación "con memoria": cada respuesta tiene en cuenta todo lo construido antes.                                               |
| **Temperatura**       | Parámetro que controla cuán conservador (0.3) o creativo (0.7) es el modelo al generar.                                                        |
| **Cumulative**        | Archivo final que acumula todo lo construido paso a paso en la estrategia ontogenia.                                                           |
| **Patrón (P1/P2/P4)** | Tipo de conocimiento que pide una pregunta: eventos (P1), estados (P2) o asignaciones (P4).                                                    |


> **Nota sobre los nombres de clases:** las clases se nombran en inglés (`ProcurementEvent`, `MaterialRelation`…) porque así lo exige la convención internacional de CIDOC CRM y porque facilita la interoperabilidad con otros proyectos. En el glosario de cada documento se ofrece su equivalente en español.

---

## Anexo B. Nota sobre el vocabulario de las tablas

Para leer las tablas de métricas de este documento:

- **"Clases arqo"** — número de clases **nuevas** creadas por el proyecto (con prefijo `arqo:`).
- **"Object Props" / "Obj Props"** — número de **propiedades de objeto** (relaciones entre entidades).
- **"Data Props"** — número de **propiedades de dato** (relaciones entre una entidad y un valor).
- **"Clases CRM usadas"** — número de clases del **estándar CIDOC CRM** que la ontología reutiliza (no crea, sino que aprovecha).
- **"Líneas cumulative"** — tamaño del archivo final acumulado, en líneas de texto.

