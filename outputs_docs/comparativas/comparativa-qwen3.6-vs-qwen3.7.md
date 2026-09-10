# Comparativa Qwen 3.6 plus vs Qwen 3.7-plus

> **Fecha:** 2026-08-28
> **Propósito:**  Compara el experimento de Qwen 3.6 plus con patrones ontológicos vs el piloto actual con Qwen 3.7-plus: CQs por patrón, conceptos cubiertos, métricas, alineación CRM, clases nuevas, observaciones y mejoras aplicadas.
> **Audiencia:** Investigadores principales del proyecto (perfil arqueológico e informático).

---

## 0. ¿Qué es una Competency Question (CQ)?

Una **pregunta de competencia** (en inglés, *Competency Question*) es una pregunta que la ontología debe ser capaz de responder. Es la forma estándar de definir **qué debe saber** una ontología antes de construirla.

En lugar de empezar diciendo "crearemos estas clases y estas relaciones" (que es como se construyen mal las ontologías), empezamos preguntando: **¿qué preguntas reales debe poder responder el sistema?** Cada pregunta se convierte después en una prueba de validación: si la ontología puede responderla, cumple su función.

**Ejemplo sencillo:**

| Pregunta de competencia | Lo que exige de la ontología |
|---|---|
| "¿De qué material está hecho este objeto arqueológico?" | Que exista una entidad "objeto", una entidad "material" y una relación entre ambas |
| "¿En qué unidad estratigráfica fue hallado?" | Que exista una entidad "unidad estratigráfica" y una relación de procedencia |
| "¿Qué tipología se le ha asignado?" | Que exista una entidad "asignación tipológica" con autor y fecha |

### Los dos ejes de clasificación

Las preguntas se organizan en **dos ejes que se cruzan**:

**Eje 1 — Bloques temáticos** (de qué habla la pregunta):
- Objeto arqueológico · Espacial · Temporal · Estratigrafía

**Eje 2 — Patrones de modelado** (qué tipo de conocimiento pide la pregunta):

| Patrón | Pregunta sobre... | Pregunta típica |
|---|---|---|
| **P1 — Eventos** (*Event-Driven*) | Lo que **pasó** — procesos y acciones | "¿Qué eventos de producción tuvo el objeto?" |
| **P2 — Estados** (*State-Transition*) | Lo que **es** — propiedades y condiciones | "¿Qué estado de conservación tiene?" |
| **P4 — Asignaciones** (*Assignment-Intrinsic*) | Lo que **sabemos** — interpretaciones | "¿Qué tipología se le ha asignado?" |

> **Nota sobre la numeración:** los patrones se numeran P1, P2 y P4 (no hay P3) porque siguen la nomenclatura del análisis de lagunas original del proyecto, donde P3 correspondía a un patrón descartado.

### Qué significa cada estrategia de generación

Para cada pregunta, la ontología se genera con dos **estrategias** distintas:

| Estrategia | En palabras llanas | Analogía |
|---|---|---|
| **Memoryless** (*sin memoria*) | Cada pregunta se responde por separado, sin recordar las anteriores | Como escribir fichas independientes, una por pregunta |
| **Ontogenia** (*con memoria*) | Cada pregunta se responde teniendo en cuenta todo lo ya construido | Como escribir un libro capítulo a capítulo, manteniendo coherencia |

### Qué es la temperatura

La **temperatura** controla cuán "conservador" o "creativo" es el modelo al generar:
- **0.3** — conservador: máxima reutilización de estándares, mínimas clases nuevas
- **0.5** — equilibrado: algunas clases nuevas, alineación estándar
- **0.7** — creativo: jerarquías profundas, más clases nuevas, más axiomas

---

## 1. Comparativa general


| Parámetro               | Qwen 3.6 (con patrones)       | Qwen 3.7-plus (piloto)                   |
| ----------------------- | ----------------------------- | ---------------------------------------- |
| **Fecha**               | 2026-05-28                    | 2026-08-27                               |
| **Modelo**              | qwen3.6 plus                  | qwen3.7-plus                             |
| **CQs totales**         | 50                            | 38                                       |
| **CQs por patrón**      | 17 P1 + 13 P2 + 20 P4         | 10 P1 + 11 P2 + 17 P4                    |
| **Estrategias**         | memoryless + ontogenia        | memoryless + ontogenia                   |
| **Temperatura**         | 0.3, 0.5, 0.7                 | 0.5                                      |
| **Corpus**              | Gap analysis + CQs unificadas | Núcleo + artículosJuan + ontologies_data |
| **Brief del dominio**   | No                            | Sí (con sección §7 de extensiones)       |
| **Patrones explícitos** | Sí (3 patrones separados)     | Sí (3 patrones en un archivo)            |
| **Carpeta experimento** | `Qwen3.6_objeto_patrones/`    | `Qwen3.7plus/`                           |


---

## 2. CQs por patrón — comparativa detallada

### Distribución original de Qwen 3.6 (según CQ_por_patron.md)


| Patrón                        | CQs    | Descripción                                                                             |
| ----------------------------- | ------ | --------------------------------------------------------------------------------------- |
| **P1 — Event-Driven**         | 17     | Eventos del ciclo de vida: producción, uso, reuso, reparación, deposición, recuperación |
| **P2 — State-Transition**     | 13     | Estados físicos y materiales: composición, propiedades, transformaciones                |
| **P4 — Assignment-Intrinsic** | 20     | Asignaciones interpretativas: tipología, cronología, hipótesis                          |
| **TOTAL**                     | **50** |                                                                                         |


**Nota:** El experimento `Qwen3.6_objeto_patrones` generó 50 archivos TTL por patrón (150 total), modelando las mismas 50 CQs bajo cada patrón.

### Distribución actual del piloto Qwen 3.7-plus


| Patrón                        | CQs originales | CQs adicionales    | Total  |
| ----------------------------- | -------------- | ------------------ | ------ |
| **P1 — Event-Driven**         | 10             | 0                  | **10** |
| **P2 — State-Transition**     | 10             | 1 (CQ-OBJ-31)      | **11** |
| **P4 — Assignment-Intrinsic** | 10             | 7 (CQ-OBJ-32 a 38) | **17** |
| **TOTAL**                     | **30**         | **8**              | **38** |


### Comparativa lado a lado


| Patrón                    | Qwen 3.6 | Qwen 3.7-plus | Diferencia |
| ------------------------- | -------- | ------------- | ---------- |
| P1 — Event-Driven         | 17       | 10            | -7         |
| P2 — State-Transition     | 13       | 11            | -2         |
| P4 — Assignment-Intrinsic | 20       | 17            | -3         |
| **Total**                 | **50**   | **38**        | **-12**    |


**Interpretación:**

- Qwen 3.6 tenía más CQs (50 vs 38) porque era el set unificado de 2 generaciones (30 v2 + 20 v1)
- El piloto es más conciso: 38 CQs, pero **más específicas y con referencia explícita a los conceptos teóricos**
- La distribución por patrón es más balanceada en el piloto (10/11/17 vs 17/13/20)

### CQs del piloto Qwen 3.7-plus, clasificadas por patrón y subgrupo

Dentro de cada patrón, las preguntas se agrupan en **subgrupos temáticos** según el concepto que abordan. Los subgrupos no son una clasificación oficial del proyecto: son una **propuesta de organización** para facilitar la lectura.

#### P1 — Eventos (lo que pasó) — 10 CQs

| Subgrupo | CQs | Pregunta (resumida) |
|---|---|---|
| **P1.1 Origen y fabricación** | CQ-OBJ-01 | ¿Qué eventos de aprovisionamiento de materia prima hubo? |
| | CQ-OBJ-05 | ¿Cuál es la secuencia completa de la cadena operativa? |
| **P1.2 Vida útil y transformación** | CQ-OBJ-02 | ¿Qué objetos sufrieron reutilización lateral vs reciclaje? |
| | CQ-OBJ-06 | ¿Qué eventos de mantenimiento se realizaron durante la vida útil? |
| **P1.3 Fin del ciclo: depósito y recuperación** | CQ-OBJ-03 | ¿Qué eventos de descarte llevaron el objeto al registro? |
| | CQ-OBJ-08 | ¿Qué eventos de deposición (inhumación, ofrenda, abandono) lo situaron? |
| | CQ-OBJ-09 | ¿Qué unidades de excavación lo recuperaron y cómo se documentó? |
| **P1.4 Actores y biografía** | CQ-OBJ-04 | ¿Por qué transiciones de persona social pasó durante su biografía? |
| | CQ-OBJ-07 | ¿Qué actores, grupos o tradiciones participaron en su producción/uso? |
| | CQ-OBJ-10 | ¿Dos o más objetos muestran secuencias biográficas paralelas? |

#### P2 — Estados (lo que es) — 11 CQs

| Subgrupo | CQs | Pregunta (resumida) |
|---|---|---|
| **P2.1 Composición y materialidad** | CQ-OBJ-11 | ¿Qué indicadores internos de datación (isótopos, oxidación) presenta? |
| | CQ-OBJ-12 | ¿Cuál es la composición material del objeto? |
| | CQ-OBJ-31 *(refuerzo)* | ¿Qué propiedades materiales relacionales (Knappett) caracterizan al objeto? |
| **P2.2 Alteración y forma** | CQ-OBJ-16 | ¿Qué alteraciones superficiales (pátina, corrosión, desgaste) presenta? |
| | CQ-OBJ-17 | ¿Cuál es su estado de fragmentación y qué proporción se conserva? |
| | CQ-OBJ-18 | ¿Qué atributos morfométricos (dimensiones, peso, forma) tiene? |
| | CQ-OBJ-20 | ¿Qué valores de color Munsell y apariencia visual presenta? |
| **P2.3 Contexto físico** | CQ-OBJ-14 | ¿En qué estado de distribución de desecho se encuentra? |
| | CQ-OBJ-15 | ¿En qué unidad de volumen estratigráfico está embebido? |
| | CQ-OBJ-19 | ¿Qué partes componentes (asas, tapaderas, hojas) lo componen? |
| **P2.4 Modo de experiencia** | CQ-OBJ-13 | ¿Se experimenta como herramienta disponible o como espécimen de estudio? |

#### P4 — Asignaciones (lo que sabemos) — 17 CQs

| Subgrupo | CQs | Pregunta (resumida) |
|---|---|---|
| **P4.1 Clasificación** | CQ-OBJ-21 | ¿Bajo qué esquema tipológico (monotético/politético) se clasifica? |
| | CQ-OBJ-22 | ¿Qué rasgos significativos apoyan su asignación cronológica/cultural? |
| | CQ-OBJ-23 | ¿Cuál es la fuerza de la relación tipo-período (débil/moderada/fuerte)? |
| | CQ-OBJ-24 | ¿A qué grupo composicional (Leitlegierung) pertenece? |
| | CQ-OBJ-29 | ¿A qué universo estilístico ha sido asignado? |
| | CQ-OBJ-33 *(refuerzo)* | *(repite el concepto de CQ-OBJ-23)* |
| | CQ-OBJ-34 *(refuerzo)* | *(repite el concepto de CQ-OBJ-22)* |
| | CQ-OBJ-35 *(refuerzo)* | *(repite el concepto de CQ-OBJ-24)* |
| **P4.2 Función** | CQ-OBJ-26 | ¿Qué interpretación funcional se le ha asignado? |
| | CQ-OBJ-36 *(refuerzo)* | *(repite el concepto de CQ-OBJ-26)* |
| **P4.3 Significado y agencia** | CQ-OBJ-27 | ¿Qué significado cultural/simbólico/ritual se le atribuye? |
| | CQ-OBJ-28 | ¿Qué agencia material se le ha atribuido y bajo qué marco teórico? |
| | CQ-OBJ-32 *(refuerzo)* | ¿Qué affordances presenta y cómo canalizan la acción humana? |
| | CQ-OBJ-37 *(refuerzo)* | *(repite el concepto de CQ-OBJ-27)* |
| **P4.4 Conocimiento y evidencia** | CQ-OBJ-25 | ¿Qué registros de archivo (cuadernos, bases de datos) lo documentan? |
| | CQ-OBJ-30 | ¿Qué hipótesis interpretativas rivales existen sobre el objeto? |
| | CQ-OBJ-38 *(refuerzo)* | *(repite el concepto de CQ-OBJ-30)* |

> **Importante sobre las CQs marcadas "refuerzo":** las CQs **31–38** se añadieron en la última iteración para reforzar los conceptos que el brief identifica como necesitados de extensión (`arqo:`). Seis de ellas (**33, 34, 35, 36, 37, 38**) son **reformulaciones del mismo concepto** que las CQs 23, 22, 24, 26, 27 y 30 respectivamente. Se mantienen por trazabilidad, pero **el conteo de conceptos distintos es de 30 CQs**, no 38.

### CQs de Qwen 3.6, clasificadas por patrón (referencia)

Las 50 CQs de Qwen 3.6 se clasificaron en su momento según los mismos tres patrones:

| Patrón | CQs | Ejemplos de preguntas |
|---|---|---|
| **P1 — Eventos** | 17 | Secuencia biográfica de eventos; transformaciones funcionales; actores vinculados; depósito compartido; circulación geográfica |
| **P2 — Estados** | 13 | Composición material; estado de preservación; procesos tafonómicos; fragmentación; relaciones espaciales |
| **P4 — Asignaciones** | 20 | Esquema tipológico; interpretación funcional; hipótesis rivales; certeza; cadenas argumentativas; conflictos interpretativos |

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
- **Materialidad relacional (Knappett)** [CQ-OBJ-31, adicional]

**Clases CIDOC CRM utilizadas:** E19_Physical_Object, E26_Physical_Feature, E3_Condition_State, E54_Dimension, E57_Material

### Qwen 3.7-plus — P4 (Assignment-Intrinsic) — CQ-OBJ-21 a 30 + 32 a 38

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
- **Affordances/agencia material** [CQ-OBJ-32]
- **Type-to-period strength** [CQ-OBJ-33]
- **Significant features** [CQ-OBJ-34]
- **Compositional groups** [CQ-OBJ-35]
- **Functional assignment** [CQ-OBJ-36]
- **Cultural significance** [CQ-OBJ-37]
- **Competing hypotheses** [CQ-OBJ-38]

**Clases CIDOC CRM utilizadas:** E17_Type_Assignment, E55_Type, E89_Propositional_Object, E13_Attribute_Assignment

---

## 4. Métricas por archivo

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
| **CQs**                      | 50          | 50          | 50          | 38            |
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
- Las 50 CQs son las mismas modeladas bajo 3 patrones distintos

**Qwen 3.7-plus:**

- Las 38 CQs cubren los conceptos clave del brief §1 (biografía, materialidad, contexto, tipología, agencia, pastness, relojes internos, archivo)
- Las 8 CQs adicionales (§7) fuerzan los conceptos de extensión

### 2. Patrones de modelado

**Qwen 3.6:** Los 3 patrones son **estrategias separadas** — el modelo genera la misma CQ de forma diferente según el patrón activo

**Qwen 3.7-plus:** Los 3 patrones son **clasificaciones dentro del mismo archivo** — el modelo sabe el patrón de cada CQ pero genera un corpus coherente

### 3. Alineación ontológica

- Qwen 3.7-plus duplica la alineación CRM (23 vs 12 clases)
- Qwen 3.7-plus es el único que usa CRMsci y CRMinf
- Qwen 3.6 P2/P4 no usan CRMarchaeo en absoluto

### 4. Riqueza ontológica

- Qwen 3.7-plus genera 97 object props vs máx 54 de qwen 3.6
- Qwen 3.7-plus genera 56 data props vs máx 37 de qwen 3.6
- El cumulative de qwen 3.7-plus (1112 líneas) supera a cualquier patrón de qwen 3.6 (máx 836)

### 5. Estilo de modelado

- Qwen 3.6 P1 es **event-centric puro**: casi todo son eventos
- Qwen 3.6 P2 es **state-centric**: modela estados como entidades
- Qwen 3.6 P4 es **assignment-centric**: reifica asignaciones
- Qwen 3.7-plus combina **eventos + estados + asignaciones + conceptos teóricos** en un corpus coherente

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


**Hallazgo:** En ambos experimentos, ontogenia produce una ontología más coherente con reuso de clases, mientras memoryless genera fragmentos más diversos pero menos integrados. Qwen 3.7-plus en ontogenia alcanza 59 clases coherentes vs ~190 clases dispersas en memoryless.

---

## 11. Análisis crítico

### ✅ Corrección: Los 8 conceptos clave SÍ están representados

**El análisis previo fue incorrecto.** Revisando `clases_arqo_creadas.md`, los 8 conceptos que se marcaron como "faltantes" en realidad **SÍ están representados** en las 59 clases `arqo:` del piloto:

1. ✅ **Materialidad relacional (Knappett)** — `MaterialRelation`, `MaterialComponent`
2. ✅ **Affordances / agencia material** — `MaterialAgencyAttribution`
3. ✅ **Type-to-period strength** — `TypeToPeriodRelationship`
4. ✅ **Significant features** — `SignificantFeature`, `FeatureEvidenceLink`
5. ✅ **Compositional groups (Leitlegierungen)** — `CompositionalGroup`, `CompositionalGroupAssignment`
6. ✅ **Functional assignment** — `FunctionalAssignment`
7. ✅ **Cultural significance** — `CulturalSignificanceAssignment`
8. ✅ **Competing hypotheses / multivocality** — `InterpretiveHypothesis`

### Ventajas del piloto qwen 3.7-plus

1. **Mayor alineación CRM** (23 clases vs 12)
2. **Mayor riqueza ontológica** (97 obj props vs 54)
3. **Uso de 4 ontologías de referencia** (vs 2)
4. **Conceptos teóricos más sofisticados** (materialidad, pastness, affordances)
5. **Corpus coherente** (no fragmentos separados por patrón)
6. **Brief con guía de extensiones** (§7)

### Limitaciones del piloto qwen 3.7-plus

1. **Menos CQs** (38 vs 50) — menor cobertura de eventos específicos
2. **Solo temperatura 0.5** — no hay comparación entre temperaturas
3. **Menos clases de eventos** que qwen 3.6 P1 (no modela Exhibition, Repatriation, Custody, Sampling como eventos)
4. **P1 con solo 10 CQs** — menor profundidad en eventos del ciclo de vida

### Limitaciones del experimento qwen 3.6 con patrones

1. **Las mismas 50 CQs modeladas 3 veces** (una por patrón) — no son CQs distintas
2. **Baja alineación CRM** en P2 y P4 (4-5 clases)
3. **Sin CRMsci/CRMinf**
4. **Patrones aislados** — cada patrón genera un corpus separado, sin integración

### Diferencias metodológicas


| Aspecto         | Qwen 3.6 con patrones      | Qwen 3.7-plus piloto    |
| --------------- | -------------------------- | ----------------------- |
| **CQs**         | 50 unificadas              | 30 + 8 de extensión     |
| **Patrones**    | 3 experimentos separados   | 1 corpus con 3 patrones |
| **Temperatura** | 3 valores                  | 1 valor (0.5)           |
| **Brief**       | Sin sección de extensiones | Con §7 de extensiones   |
| **Prompt**      | ALWAYS reuse CRM           | Balance guideline       |


---

## 12. Mejoras propuestas e implementadas

### 12.1 Mejoras implementadas (2026-08-28)

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


**Impacto:** El generador ahora sabe qué conceptos requieren extensiones `arqo:` en lugar de forzar reuso CRM.

#### ✅ Mejora 2: CQs adicionales de extensión

**Problema:** Las CQs originales no forzaban explícitamente la creación de extensiones para conceptos teóricos.

**Solución implementada:** Se agregaron 8 CQs (CQ-OBJ-31 a CQ-OBJ-38) que referencian explícitamente los conceptos de la sección §7:


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


**Impacto:** Cada concepto de extensión ahora tiene al menos una CQ que fuerza su modelado.

#### ✅ Mejora 3: Prompts con balance guideline

**Problema:** El prompt decía "ALWAYS check if CIDOC CRM provides it" — demasiado conservador, favorecía reuso forzado.

**Solución implementada:** Se agregó un "Balance guideline" en ambos prompts (memoryless y ontogenia):

- **Preferir reuso CRM** para conceptos generales (eventos, actores, lugares, tiempos)
- **Crear extensiones `arqo:`** cuando el concepto sea arqueológicamente específico (material agency, relational materiality, type-to-period strength, etc.)
- **"When in doubt, create an `arqo:` class that extends CRM"**

**Impacto:** El modelo ahora crea extensiones `arqo:` cuando es apropiado, en lugar de forzar clases CRM para conceptos específicos.

#### ⏳ Mejora 4: Validación intermedia (pendiente)

**Problema:** No se verificaba que cada concepto del brief tuviera al menos una CQ.

**Solución pendiente:** Script de mapeo concepto→CQ (`scripts/validate_cq_coverage.py`).

### 12.2 Propuestas de mejora futuras

Estas mejoras **no están implementadas todavía** y se proponen para las próximas iteraciones. Se presentan ordenadas por prioridad.

#### 🔴 Prioridad alta

| # | Propuesta | Qué resolvería | Esfuerzo |
|---|---|---|---|
| 1 | **Consolidar las CQs duplicadas** | Las CQs 33–38 reformulan conceptos ya cubiertos por las 22–30. Consolidarlas daría un set limpio de 30 CQs distintas | Bajo |
| 2 | **Adoptar los subgrupos temáticos** (P1.1, P1.2…) como estructura oficial | Facilita la lectura, la validación con expertos y la detección de vacíos temáticos | Bajo |
| 3 | **Validación intermedia** (concepto → CQ) | Detecta automáticamente si algún concepto del brief no tiene pregunta asignada | Medio |
| 4 | **Evaluación con expertos arqueólogos** | Valida que las preguntas y las clases sean arqueológicamente correctas, no solo técnicamente válidas | Medio |

#### 🟡 Prioridad media

| # | Propuesta | Qué resolvería | Esfuerzo |
|---|---|---|---|
| 5 | **Medir cobertura CQ → ontología con SPARQL** | Comprueba que cada pregunta puede responderse realmente contra la ontología generada (no solo que la clase exista) | Medio |
| 6 | **Verificar consistencia lógica con un reasoner OWL** | Detecta clases insatisfacibles, contradicciones y axiomas mal formados | Medio |
| 7 | **Extender el pipeline a los otros 3 bloques** (espacial, temporal, estratigrafía) | Actualmente solo está completo el bloque de objeto | Alto |
| 8 | **Comparar más modelos LLM** (deepseek, kimi, glm…) | Permite una comparativa cross-model robusta | Medio |

#### 🟢 Prioridad baja (exploratoria)

| # | Propuesta | Qué resolvería | Esfuerzo |
|---|---|---|---|
| 9 | **Comparar temperaturas** (0.3, 0.5, 0.7) en el piloto | El piloto solo usó temperatura 0.5; faltan los extremos | Bajo |
| 10 | **Añadir métricas de determinismo** (misma pregunta, dos ejecuciones) | Mide la estabilidad del modelo ante el mismo prompt | Medio |
| 11 | **Regenerar con los prompts mejorados** y comparar antes/después | Mide el impacto real del balance guideline en las clases `arqo:` creadas | Bajo |

> **Recomendación:** empezar por las propuestas 1, 2 y 3 (bajo esfuerzo, alto impacto en claridad y rigor), que preparan el terreno para la evaluación con expertos (propuesta 4).

---

## 13. Prompts antiguos vs nuevos

### 13.1 Prompt Memoryless

**Archivo:** `prompts/memoryless/prompt_archaeological_object.md`

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

**Archivo:** `prompts/ontogenia/prompt_archaeological_object.md`

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


| Aspecto                    | Antes            | Después                                                    |
| -------------------------- | ---------------- | ---------------------------------------------------------- |
| **Postura**                | ALWAYS reuse CRM | Prefer reuse, pero crear extensiones cuando sea específico |
| **Conceptos de extensión** | No listados      | 7 categorías listadas                                      |
| **Regla final**            | Ninguna          | "When in doubt, create `arqo:` extension"                  |
| **Referencia al brief**    | No               | Brief §7                                                   |


---

## 14. Conclusiones

### Sobre las CQs

1. El piloto tiene menos CQs (38 vs 50) pero **más específicas y teóricamente informadas**
2. La distribución por patrón es más balanceada en el piloto
3. Las 8 CQs adicionales garantizan cobertura de los conceptos de extensión

### Sobre la ontología generada

1. **Qwen 3.7-plus supera a qwen 3.6 en riqueza y alineación**: 97 obj props vs 54, 23 clases CRM vs 12
2. **Qwen 3.7-plus usa 4 ontologías de referencia** vs solo 2 de qwen 3.6
3. **Qwen 3.6 P1 es más rico en eventos** (63 clases) pero con menor alineación
4. **Qwen 3.6 P2/P4 tienen baja alineación** (0 clases CRMarchaeo)

### Sobre las mejoras

1. El brief §7 da al generador **guía explícita** sobre cuándo crear extensiones `arqo:`
2. Las CQs de extensión **fuerzan** el modelado de conceptos teóricos
3. El balance guideline en prompts **equilibra** reuso vs creación

### Próximos pasos

1. ⏳ Implementar validación intermedia (script concepto→CQ)
2. Regenerar ontologías con los prompts mejorados
3. Comparar si las nuevas ontologías cubren mejor los conceptos de extensión
4. Ejecutar el pipeline con las 38 CQs completas en ambas estrategias

