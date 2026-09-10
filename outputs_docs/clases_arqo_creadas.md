# Clases arqo: Creadas en el Piloto

**Total:** 59 clases nuevas

> **Audiencia:** Investigadores principales del proyecto (perfil arqueológico e informático).

---

## ¿Qué es una clase "arqo"?

La ontología se construye con dos tipos de piezas:

- **Clases** — los *tipos de cosas* que existen en el dominio (p. ej. "objeto arqueológico", "evento de producción", "estado de fragmentación").
- **Propiedades** — las *relaciones* entre esas cosas (p. ej. "está hecho de", "fue producido por").

Cuando decimos que una clase es **`arqo:`**, significa que es **nueva, creada por el proyecto**, no heredada de los estándares internacionales. El prefijo `arqo:` es el espacio de nombres propio de esta ontología (`http://www.ontologyARQ.org/archaeological-object/`).

Las clases nuevas **siempre extienden una clase del estándar** cuando existe una adecuada. Por ejemplo:

```turtle
arqo:ProcurementEvent  rdfs:subClassOf  crm:E9_Move
```

Esto se lee: *"un evento de aprovisionamiento (nuevo) ES UN TIPO DE movimiento (estándar CIDOC CRM)"*. Así, la ontología añade detalle arqueológico sin romper la compatibilidad con los estándares.

---

## Comparación con Qwen 3.6

Este documento compara las clases nuevas creadas por el **piloto actual (Qwen 3.7-plus)** con las creadas por el **experimento anterior (Qwen 3.6 con patrones)**.

### Cuántas clases creó cada modelo

| Experimento | Clases arqo | Cómo se generaron |
|---|---|---|
| **Qwen 3.6 — patrón eventos (P1)** | 63 | Modelando las 50 CQs bajo el patrón de eventos |
| **Qwen 3.6 — patrón estados (P2)** | 34 | Modelando las 50 CQs bajo el patrón de estados |
| **Qwen 3.6 — patrón asignaciones (P4)** | 31 | Modelando las 50 CQs bajo el patrón de asignaciones |
| **Qwen 3.7-plus (piloto)** | **59** | Modelando 38 CQs en un corpus coherente |

> **Cómo leer esta tabla:** Qwen 3.6 generó tres ontologías *separadas* (una por patrón), cada una modelando las mismas 50 preguntas desde un ángulo distinto. Qwen 3.7-plus generó *una sola ontología coherente* que integra los tres patrones.

### Qué clases coinciden entre ambos

| Categoría | N.º de clases |
|---|---|
| Clases **comunes** (creadas por ambos modelos) | **3** |
| Clases **solo en Qwen 3.6** | 41 |
| Clases **solo en Qwen 3.7-plus** (nuevas del piloto) | 56 |

**Las 3 clases comunes son:**

- `arqo:DepositionEvent` — evento de deposición
- `arqo:InterpretiveHypothesis` — hipótesis interpretativa
- `arqo:RecoveryEvent` — evento de recuperación

> **Por qué solo coinciden 3:** los dos experimentos partieron de corpus y briefs distintos. Qwen 3.6 trabajó desde el análisis de lagunas y un set de 50 CQs; Qwen 3.7-plus trabajó desde un brief del dominio mucho más detallado (con sección de extensión §7) y 38 CQs. El enfoque resultante es distinto, no necesariamente peor.

### Enfoque de cada modelo

**Qwen 3.6 — centrado en eventos y procesos**
- Modela el ciclo de vida como una cadena de **eventos** (producción, uso, recirculación, exhibición, repatriación, custodia…)
- Genera clases como `ManufacturingEvent`, `CirculationEvent`, `CustodyEvent`, `SamplingEvent`, `ExhibitionEvent`, `RepatriationEvent`
- Los estados se modelan como clases separadas (`CorrosionState`, `PatinaState`, `DepositedState`…)
- **Ventaja:** muy detallado en eventos específicos
- **Limitación:** poca alineación con los estándares en los patrones de estados y asignaciones (0 clases CRMarchaeo)

**Qwen 3.7-plus — centrado en conceptos teóricos y relaciones**
- Modela explícitamente **conceptos teóricos** del dominio arqueológico: materialidad relacional (Knappett), affordances y agencia material (Gibson, Hodder), pastness, modos de experiencia (Heidegger)
- Genera clases que reifican **relaciones** (no solo entidades): `MaterialRelation`, `TypeToPeriodRelationship`, `FeatureEvidenceLink`, `EmbeddingRelation`
- Reifica las **asignaciones interpretativas**: `TypologicalAssignment`, `FunctionalAssignment`, `CulturalSignificanceAssignment`, `CompositionalGroupAssignment`
- **Ventaja:** mejor alineación con los estándares y captura explícita de la teoría arqueológica
- **Limitación:** menos clases de eventos específicos que Qwen 3.6

### Resumen de la comparación

| Criterio | Ganador | Por qué |
|---|---|---|
| **Número de clases** | Qwen 3.6 P1 (63) | Más clases, pero en el patrón más prolífico |
| **Alineación con estándares** | **Qwen 3.7-plus** | Usa 4 ontologías de referencia (CRM, CRMarchaeo, CRMsci, CRMinf) vs 2 |
| **Coherencia interna** | **Qwen 3.7-plus** | Una ontología integrada vs tres corpus separados |
| **Cobertura teórica** | **Qwen 3.7-plus** | Captura materialidad, affordances, pastness explícitamente |
| **Detalle en eventos** | Qwen 3.6 | Más tipos de eventos específicos (exhibición, repatriación, custodia) |
| **Riqueza de propiedades** | **Qwen 3.7-plus** | 97 propiedades de objeto vs 54 máximo de Qwen 3.6 |

> **Conclusión:** Qwen 3.7-plus no gana por cantidad, sino por **calidad estructural**: menos clases pero mejor alineadas, mejor conectadas y teóricamente más ricas. Qwen 3.6 gana en detalle de eventos específicos, lo que sugiere una posible **mejora futura: incorporar los eventos de Qwen 3.6 al modelo de Qwen 3.7-plus**.

---

## Inventario completo de clases creadas por el piloto

## Objeto y Materialidad (7)

### arqo:ArchaeologicalObject

**Nombre:** ArchaeologicalObject

**Superclase:** `crm:E19_Physical_Object (objeto físico)`

**Descripción:** Objeto físico recuperado durante una investigación arqueológica.

<sub>Original (EN): Physical object recovered during archaeological investigation</sub>

---

### arqo:ComponentPart

**Nombre:** ComponentPart

**Superclase:** `crm:E19_Physical_Object (objeto físico)`

**Descripción:** Parte física de un objeto arqueológico compuesto (asa, tapa, hoja, vástago, incrustación o adhesivo).

<sub>Original (EN): Physical component of a composite archaeological object, such as a handle, lid, blade, shaft, inlay, or attachment</sub>

---

### arqo:MaterialAgencyAttribution

**Nombre:** MaterialAgencyAttribution

**Superclase:** `crminf:I4_Proposition_Set (conjunto proposicional (inferencia))`

**Descripción:** Atribución interpretativa de agencia material a un objeto: la capacidad de su forma, propiedades materiales o asociaciones culturales de canalizar, limitar o permitir acciones humanas (affordances de Gibson, entanglement de Hodder).

<sub>Original (EN): Interpretive attribution of material agency to an object: the capacity of its form, material properties, or cultural associations to channel, constrain, or enable human actions (Gibson affordances, Hodder entanglement)</sub>

---

### arqo:MaterialComponent

**Nombre:** MaterialComponent

**Superclase:** `crm:E57_Material (material)`

**Descripción:** Componente material de un objeto arqueológico.

<sub>Original (EN): Material constituent of an archaeological object</sub>

---

### arqo:MaterialRelation

**Nombre:** MaterialRelation

**Superclase:** `crm:E1_CRM_Entity (entidad (raíz del estándar))`

**Descripción:** Relación reificada entre componentes materiales (Knappett).

<sub>Original (EN): Reified relationship between material components (Knappett)</sub>

---

### arqo:ObjectBiography

**Nombre:** ObjectBiography

**Superclase:** `crm:E5_Event (evento)`

**Descripción:** Secuencia ordenada de eventos biográficos.

<sub>Original (EN): Ordered sequence of biographical events</sub>

---

### arqo:RawMaterialSource

**Nombre:** RawMaterialSource

**Superclase:** `crm:E53_Place (lugar)`

**Descripción:** Fuente geológica o geográfica de materias primas.

<sub>Original (EN): Geological or geographic source of raw materials</sub>

---

## Biografía y Ciclo de Vida (2)

### arqo:SocialPersona

**Nombre:** SocialPersona

**Superclase:** `crm:E89_Propositional_Object (objeto proposicional (idea/afirmación))`

**Descripción:** Identidad culturalmente atribuida a un objeto.

<sub>Original (EN): Culturally attributed identity of an object</sub>

---

### arqo:SocialPersonaTransition

**Nombre:** SocialPersonaTransition

**Superclase:** `crm:E5_Event (evento)`

**Descripción:** Cambio de persona social de un objeto.

<sub>Original (EN): Change of object social persona</sub>

---

## Eventos de Producción (3)

### arqo:CraftTradition

**Nombre:** CraftTradition

**Superclase:** `crm:E74_Group (grupo)`

**Descripción:** Comunidad de práctica que comparte conocimiento técnico.

<sub>Original (EN): Community of practice sharing technical knowledge</sub>

---

### arqo:ProcurementEvent

**Nombre:** ProcurementEvent

**Superclase:** `crm:E9_Move (movimiento)`

**Descripción:** Evento de extracción, adquisición o recolección de materia prima.

<sub>Original (EN): Event of raw material extraction, acquisition, or collection</sub>

---

### arqo:TechnicalAction

**Nombre:** TechnicalAction

**Superclase:** `crm:E7_Activity (actividad)`

**Descripción:** Paso individual dentro de una cadena operativa.

<sub>Original (EN): Individual step within a chaîne opératoire</sub>

---

## Eventos de Uso y Reuso (8)

### arqo:DeFactoRefuse

**Nombre:** DeFactoRefuse

**Superclase:** `arqo:DiscardEvent`

**Descripción:** Abandono sin descarte intencional.

<sub>Original (EN): Abandonment without intentional discard</sub>

---

### arqo:LateralCyclingEvent

**Nombre:** LateralCyclingEvent

**Superclase:** `arqo:ReuseEvent`

**Descripción:** Reutilización en un contexto social diferente sin cambio de función.

<sub>Original (EN): Reuse in different social context without function change</sub>

---

### arqo:MaintenanceEvent

**Nombre:** MaintenanceEvent

**Superclase:** `crm:E11_Modification (modificación)`

**Descripción:** Cuidado preventivo o reparación durante la vida útil activa.

<sub>Original (EN): Preventive care or repair during active use-life</sub>

---

### arqo:PrimaryRefuse

**Nombre:** PrimaryRefuse

**Superclase:** `arqo:DiscardEvent`

**Descripción:** Descarte en el lugar de uso.

<sub>Original (EN): Discard at place of use</sub>

---

### arqo:RecyclingEvent

**Nombre:** RecyclingEvent

**Superclase:** `crm:E81_Transformation (transformación)`

**Descripción:** Reingreso en el proceso de fabricación.

<sub>Original (EN): Re-entry into manufacturing process</sub>

---

### arqo:RefuseDistributionState

**Nombre:** RefuseDistributionState

**Superclase:** `crm:E3_Condition_State (estado de condición)`

**Descripción:** Condición espacial-distribucional de un objeto en el registro arqueológico: desecho primario (en el lugar de uso), secundario (transportado a zona de desecho) o de facto (abandonado in situ).

<sub>Original (EN): Spatial-distributional condition of an object in the archaeological record: primary refuse (at place of use), secondary refuse (transported to disposal area), or de facto refuse (abandoned in situ)</sub>

---

### arqo:ReuseEvent

**Nombre:** ReuseEvent

**Superclase:** `crm:E7_Activity (actividad)`

**Descripción:** Evento de reutilización de un objeto tras su fase de uso inicial.

<sub>Original (EN): Event of object reuse after initial use phase</sub>

---

### arqo:SecondaryRefuse

**Nombre:** SecondaryRefuse

**Superclase:** `arqo:DiscardEvent`

**Descripción:** Descarte transportado a la zona de desecho.

<sub>Original (EN): Discard transported to refuse area</sub>

---

## Eventos de Deposición (5)

### arqo:CasualAbandonment

**Nombre:** CasualAbandonment

**Superclase:** `arqo:DepositionEvent`

**Descripción:** Pérdida o abandono no estructurado.

<sub>Original (EN): Unstructured loss or abandonment</sub>

---

### arqo:DepositionEvent

**Nombre:** DepositionEvent

**Superclase:** `crmarchaeo:A4_Stratigraphic_Genesis (génesis estratigráfica)`

**Descripción:** Evento que sitúa un objeto en el registro estratigráfico.

<sub>Original (EN): Event placing object into stratigraphic record</sub>

---

### arqo:DiscardEvent

**Nombre:** DiscardEvent

**Superclase:** `crm:E5_Event (evento)`

**Descripción:** Evento de descarte que conduce a la entrada en el registro arqueológico.

<sub>Original (EN): Event of discard leading to archaeological record entry</sub>

---

### arqo:IntentionalBurial

**Nombre:** IntentionalBurial

**Superclase:** `arqo:DepositionEvent`

**Descripción:** Enterramiento deliberado de un objeto.

<sub>Original (EN): Deliberate burial of an object</sub>

---

### arqo:RitualOffering

**Nombre:** RitualOffering

**Superclase:** `arqo:DepositionEvent`

**Descripción:** Colocación votiva o ritual.

<sub>Original (EN): Votive or ritual placement</sub>

---

## Eventos de Recuperación (3)

### arqo:RecoveryDocumentation

**Nombre:** RecoveryDocumentation

**Superclase:** `crm:E31_Document (documento)`

**Descripción:** Documentación producida durante la recuperación.

<sub>Original (EN): Documentation produced during recovery</sub>

---

### arqo:RecoveryEvent

**Nombre:** RecoveryEvent

**Superclase:** `crmarchaeo:A1_Excavation_Process_Unit (unidad de proceso de excavación)`

**Descripción:** Unidad de excavación que recuperó el objeto.

<sub>Original (EN): Excavation unit that recovered the object</sub>

---

### arqo:RecoveryObservation

**Nombre:** RecoveryObservation

**Superclase:** `crmsci:S4_Observation (observación científica)`

**Descripción:** Observación durante la recuperación.

<sub>Original (EN): Observation during recovery</sub>

---

## Contexto y Embebido (1)

### arqo:EmbeddingRelation

**Nombre:** EmbeddingRelation

**Superclase:** `crmarchaeo:A7_Embedding (embebido estratigráfico)`

**Descripción:** Contención física de un objeto arqueológico dentro de una unidad de volumen estratigráfico con estabilidad relativa.

<sub>Original (EN): Physical containment of an archaeological object within a stratigraphic volume unit with relative stability, following the CRMarchaeo embedding pattern (E18 - AP18i - A7 - AP19 - A2)</sub>

---

## Tipología y Clasificación (4)

### arqo:ClassificationMethod

**Nombre:** ClassificationMethod

**Superclase:** `crm:E29_Design_or_Procedure (diseño o procedimiento)`

**Descripción:** Método empleado para la clasificación tipológica: monotético (un único atributo diagnóstico) o politético (análisis de conglomerados de múltiples atributos).

<sub>Original (EN): Method employed for typological classification: monothetic (single diagnostic attribute) or polythetic (cluster analysis of multiple attributes)</sub>

---

### arqo:CompositionalGroup

**Nombre:** CompositionalGroup

**Superclase:** `crm:E55_Type (tipo)`

**Descripción:** Grupo de objetos metálicos que comparten ratios elementales característicos o firmas de aleación (Leitlegierung).

<sub>Original (EN): Group of metallic objects sharing characteristic elemental ratios or alloy signatures (Leitlegierung)</sub>

---

### arqo:CompositionalGroupAssignment

**Nombre:** CompositionalGroupAssignment

**Superclase:** `crm:E17_Type_Assignment (asignación de tipo)`

**Descripción:** Asignación de un objeto metálico a un grupo composicional (Leitlegierung) definido por ratios elementales o firmas de aleación diagnósticas.

<sub>Original (EN): Assignment of a metallic object to a compositional group (Leitlegierung) defined by diagnostic elemental ratios or alloy signatures</sub>

---

### arqo:TypeToPeriodRelationship

**Nombre:** TypeToPeriodRelationship

**Superclase:** `crm:E1_CRM_Entity (entidad (raíz del estándar))`

**Descripción:** Relación reificada entre un tipo tipológico y un período cronológico, con nivel de fuerza explícito (débil/moderado/fuerte).

<sub>Original (EN): Reified relationship between a typological type and a chronological period, with explicit strength level following CRMarchaeo AP29 (weak), AP31 (moderate), AP30 (strong)</sub>

---

## Análisis y Medición (2)

### arqo:InternalClockIndicator

**Nombre:** InternalClockIndicator

**Superclase:** `crm:E26_Physical_Feature (rasgo físico)`

**Descripción:** Propiedad físico-química medible que sirve como indicador de edad.

<sub>Original (EN): Measurable physical-chemical property serving as age indicator</sub>

---

### arqo:InternalClockMeasurement

**Nombre:** InternalClockMeasurement

**Superclase:** `crmsci:S21_Measurement (medición científica)`

**Descripción:** Medición científica de un indicador de reloj interno.

<sub>Original (EN): Scientific measurement of an internal clock indicator</sub>

---

## Interpretación y Significado (5)

### arqo:ArchaeologicalArchiveRecord

**Nombre:** ArchaeologicalArchiveRecord

**Superclase:** `crm:E73_Information_Object (objeto de información)`

**Descripción:** Registro dentro del archivo arqueológico que documenta un objeto: cuadernos de campo, bases de datos digitales, archivos fotográficos, colecciones de dibujos o informes publicados.

<sub>Original (EN): Record within the archaeological archive documenting an object: field notebooks, digital databases, photographic archives, drawing collections, or published reports. Archive records function as archaeological objects in their own right.</sub>

---

### arqo:ArchiveCollection

**Nombre:** ArchiveCollection

**Superclase:** `crm:E78_Curated_Holding (colección curada)`

**Descripción:** Colección curada de registros de archivo arqueológico mantenida por una institución de investigación.

<sub>Original (EN): Curated collection of archaeological archive records maintained by a research institution</sub>

---

### arqo:CulturalSignificanceAssignment

**Nombre:** CulturalSignificanceAssignment

**Superclase:** `crm:E13_Attribute_Assignment (asignación de atributo)`

**Descripción:** Atribución de significado cultural, simbólico o ritual a un objeto por investigadores, comunidades descendientes o narrativas institucionales.

<sub>Original (EN): Attribution of cultural, symbolic, or ritual significance to an object by researchers, descendant communities, or institutional narratives</sub>

---

### arqo:InterpretiveHypothesis

**Nombre:** InterpretiveHypothesis

**Superclase:** `crminf:I4_Proposition_Set (conjunto proposicional (inferencia))`

**Descripción:** Proposición interpretativa competidora o contradictoria sobre la identidad, cronología, función o significado cultural de un objeto.

<sub>Original (EN): Competing or contradictory interpretive proposition regarding the identity, chronology, function, or cultural meaning of an archaeological object</sub>

---

### arqo:PastnessQuality

**Nombre:** PastnessQuality

**Superclase:** `crm:E1_CRM_Entity (entidad (raíz del estándar))`

**Descripción:** Cualidad experiencial culturalmente construida de ser “del pasado” que emerge de huellas materiales de desintegración en la superficie de un objeto.

<sub>Original (EN): Culturally constructed experiential quality of being 'from the past' that emerges from material traces of disintegration on an object's surface</sub>

---

## Actores y Grupos (1)

### arqo:CulturalCommunity

**Nombre:** CulturalCommunity

**Superclase:** `crm:E74_Group (grupo)`

**Descripción:** Grupo social que comparte prácticas culturales y tradiciones materiales.

<sub>Original (EN): Social group sharing cultural practices and material traditions</sub>

---

## Otros (18)

### arqo:BiographicalParallelism

**Nombre:** BiographicalParallelism

**Superclase:** `crminf:I4_Proposition_Set (conjunto proposicional (inferencia))`

**Descripción:** Afirmación de que objetos comparten secuencias biográficas similares.

<sub>Original (EN): Assertion that objects share similar biographical sequences</sub>

---

### arqo:ChaineOperatoire

**Nombre:** ChaineOperatoire

**Superclase:** `crm:E29_Design_or_Procedure (diseño o procedimiento)`

**Descripción:** Secuencia ordenada completa de acciones técnicas.

<sub>Original (EN): Complete ordered sequence of technical actions</sub>

---

### arqo:EmergencyCaching

**Nombre:** EmergencyCaching

**Superclase:** `arqo:DepositionEvent`

**Descripción:** Ocultación apresurada en respuesta a una amenaza.

<sub>Original (EN): Hasty concealment in response to threat</sub>

---

### arqo:FeatureEvidenceLink

**Nombre:** FeatureEvidenceLink

**Superclase:** `crm:E1_CRM_Entity (entidad (raíz del estándar))`

**Descripción:** Vínculo evidencial reificado entre un rasgo significativo y el período cronológico o cultural que sustenta.

<sub>Original (EN): Reified evidential link between a significant feature and the chronological or cultural period it supports, with explicit strength assessment</sub>

---

### arqo:FragmentationState

**Nombre:** FragmentationState

**Superclase:** `crm:E3_Condition_State (estado de condición)`

**Descripción:** Estado físico de un objeto en cuanto a su integridad: completo, parcialmente fragmentado o reducido a fragmentos aislados.

<sub>Original (EN): Physical state of an object regarding its completeness: complete, partially fragmented, or reduced to isolated fragments</sub>

---

### arqo:FunctionalAssignment

**Nombre:** FunctionalAssignment

**Superclase:** `crm:E13_Attribute_Assignment (asignación de atributo)`

**Descripción:** Asignación interpretativa de función a un objeto arqueológico, distinguiendo función primaria pretendida, función secundaria adquirida y función atribuida por el investigador.

<sub>Original (EN): Interpretive assignment of function to an archaeological object, distinguishing primary intended function, secondary acquired function, and researcher-attributed function</sub>

---

### arqo:JoiningTechnique

**Nombre:** JoiningTechnique

**Superclase:** `crm:E29_Design_or_Procedure (diseño o procedimiento)`

**Descripción:** Procedimiento técnico usado para conectar partes componentes de un objeto compuesto (remachado, soldadura, adhesión, ensamblaje machihembrado o atado).

<sub>Original (EN): Technical procedure used to connect component parts of a composite object, such as riveting, soldering, adhesion, mortise-and-tenon, or lashing</sub>

---

### arqo:ModeOfExperience

**Nombre:** ModeOfExperience

**Superclase:** `crm:E3_Condition_State (estado de condición)`

**Descripción:** Modo ontológico heideggeriano: disponibilidad (readiness-to-hand) o presencia (presence-at-hand).

<sub>Original (EN): Heideggerian ontological mode: readiness-to-hand or presence-at-hand</sub>

---

### arqo:MorphometricAttribute

**Nombre:** MorphometricAttribute

**Superclase:** `crmsci:S21_Measurement (medición científica)`

**Descripción:** Medición física cuantitativa de un objeto arqueológico: dimensiones, peso, volumen, área superficial y descriptores de forma.

<sub>Original (EN): Quantitative physical measurement of an archaeological object including dimensions, weight, volume, surface area, and shape descriptors</sub>

---

### arqo:OntologicalShiftEvent

**Nombre:** OntologicalShiftEvent

**Superclase:** `crm:E5_Event (evento)`

**Descripción:** Evento que causa la transición entre modos de experiencia.

<sub>Original (EN): Event causing transition between modes of experience</sub>

---

### arqo:PresenceAtHand

**Nombre:** PresenceAtHand

**Superclase:** `arqo:ModeOfExperience`

**Descripción:** Objeto experimentado como espécimen separado.

<sub>Original (EN): Object experienced as detached specimen</sub>

---

### arqo:ReadinessToHand

**Nombre:** ReadinessToHand

**Superclase:** `arqo:ModeOfExperience`

**Descripción:** Objeto experimentado como herramienta disponible.

<sub>Original (EN): Object experienced as available tool</sub>

---

### arqo:SignificantFeature

**Nombre:** SignificantFeature

**Superclase:** `crm:E26_Physical_Feature (rasgo físico)`

**Descripción:** Atributo físico diagnóstico de un objeto identificado mediante análisis sistemático que apoya su asignación cronológica o cultural.

<sub>Original (EN): Diagnostically relevant physical attribute of an object identified through systematic analysis that supports chronological or cultural assignment</sub>

---

### arqo:StylisticAssignment

**Nombre:** StylisticAssignment

**Superclase:** `crm:E17_Type_Assignment (asignación de tipo)`

**Descripción:** Asignación de un objeto a un universo estilístico basada en atributos formales, decorativos y culturales.

<sub>Original (EN): Assignment of an object to a stylistic universe based on formal, decorative, and cultural attributes</sub>

---

### arqo:StylisticUniverse

**Nombre:** StylisticUniverse

**Superclase:** `crm:E55_Type (tipo)`

**Descripción:** Conjunto de objetos que comparten reglas formales, convenciones decorativas y asociaciones culturales que definen un sistema estético-cultural coherente.

<sub>Original (EN): Corpus of objects sharing formal rules, decorative conventions, and cultural associations that define a coherent aesthetic-cultural system</sub>

---

### arqo:SurfaceAlteration

**Nombre:** SurfaceAlteration

**Superclase:** `crm:E26_Physical_Feature (rasgo físico)`

**Descripción:** Modificación física de la superficie de un objeto: pátina, capas de corrosión, costras de meteorización, brillo por uso o películas de oxidación.

<sub>Original (EN): Physical modification of an object's surface including patina, corrosion layers, weathering rinds, use-wear polish, and oxidation films</sub>

---

### arqo:TypologicalAssignment

**Nombre:** TypologicalAssignment

**Superclase:** `crm:E17_Type_Assignment (asignación de tipo)`

**Descripción:** Asignación por el investigador de un objeto a una categoría tipológica, usando clasificación monotética o politética.

<sub>Original (EN): Researcher assignment of an object to a typological category, using either monothetic or polythetic classification methods</sub>

---

### arqo:VisualAppearanceAttribute

**Nombre:** VisualAppearanceAttribute

**Superclase:** `crm:E26_Physical_Feature (rasgo físico)`

**Descripción:** Propiedad visual observable de un objeto arqueológico en su estado actual de conservación: color Munsell, textura superficial y apariencia general.

<sub>Original (EN): Observable visual property of an archaeological object in its current state of preservation, including Munsell color, surface texture, and general appearance</sub>

---

