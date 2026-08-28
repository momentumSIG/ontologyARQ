# Clases arqo: Creadas en el Piloto

**Total:** 59 clases nuevas

---

## Objeto y Materialidad (7)

### arqo:ArchaeologicalObject

**Label:** ArchaeologicalObject

**Superclase:** crm:E19_Physical_Object

**Descripción:** Physical object recovered during archaeological investigation

---

### arqo:ComponentPart

**Label:** ComponentPart

**Superclase:** crm:E19_Physical_Object

**Descripción:** Physical component of a composite archaeological object, such as a handle, lid, blade, shaft, inlay, or attachment

---

### arqo:MaterialAgencyAttribution

**Label:** MaterialAgencyAttribution

**Superclase:** crminf:I4_Proposition_Set

**Descripción:** Interpretive attribution of material agency to an object: the capacity of its form, material properties, or cultural associations to channel, constrain, or enable human actions (Gibson affordances, Hodder entanglement)

---

### arqo:MaterialComponent

**Label:** MaterialComponent

**Superclase:** crm:E57_Material

**Descripción:** Material constituent of an archaeological object

---

### arqo:MaterialRelation

**Label:** MaterialRelation

**Superclase:** crm:E1_CRM_Entity

**Descripción:** Reified relationship between material components (Knappett)

---

### arqo:ObjectBiography

**Label:** ObjectBiography

**Superclase:** crm:E5_Event

**Descripción:** Ordered sequence of biographical events

---

### arqo:RawMaterialSource

**Label:** RawMaterialSource

**Superclase:** crm:E53_Place

**Descripción:** Geological or geographic source of raw materials

---

## Biografía y Ciclo de Vida (2)

### arqo:SocialPersona

**Label:** SocialPersona

**Superclase:** crm:E89_Propositional_Object

**Descripción:** Culturally attributed identity of an object

---

### arqo:SocialPersonaTransition

**Label:** SocialPersonaTransition

**Superclase:** crm:E5_Event

**Descripción:** Change of object social persona

---

## Eventos de Producción (3)

### arqo:CraftTradition

**Label:** CraftTradition

**Superclase:** crm:E74_Group

**Descripción:** Community of practice sharing technical knowledge

---

### arqo:ProcurementEvent

**Label:** ProcurementEvent

**Superclase:** crm:E9_Move

**Descripción:** Event of raw material extraction, acquisition, or collection

---

### arqo:TechnicalAction

**Label:** TechnicalAction

**Superclase:** crm:E7_Activity

**Descripción:** Individual step within a chaîne opératoire

---

## Eventos de Uso y Reuso (8)

### arqo:DeFactoRefuse

**Label:** DeFactoRefuse

**Superclase:** arqo:DiscardEvent

**Descripción:** Abandonment without intentional discard

---

### arqo:LateralCyclingEvent

**Label:** LateralCyclingEvent

**Superclase:** arqo:ReuseEvent

**Descripción:** Reuse in different social context without function change

---

### arqo:MaintenanceEvent

**Label:** MaintenanceEvent

**Superclase:** crm:E11_Modification

**Descripción:** Preventive care or repair during active use-life

---

### arqo:PrimaryRefuse

**Label:** PrimaryRefuse

**Superclase:** arqo:DiscardEvent

**Descripción:** Discard at place of use

---

### arqo:RecyclingEvent

**Label:** RecyclingEvent

**Superclase:** crm:E81_Transformation

**Descripción:** Re-entry into manufacturing process

---

### arqo:RefuseDistributionState

**Label:** RefuseDistributionState

**Superclase:** crm:E3_Condition_State

**Descripción:** Spatial-distributional condition of an object in the archaeological record: primary refuse (at place of use), secondary refuse (transported to disposal area), or de facto refuse (abandoned in situ)

---

### arqo:ReuseEvent

**Label:** ReuseEvent

**Superclase:** crm:E7_Activity

**Descripción:** Event of object reuse after initial use phase

---

### arqo:SecondaryRefuse

**Label:** SecondaryRefuse

**Superclase:** arqo:DiscardEvent

**Descripción:** Discard transported to refuse area

---

## Eventos de Deposición (5)

### arqo:CasualAbandonment

**Label:** CasualAbandonment

**Superclase:** arqo:DepositionEvent

**Descripción:** Unstructured loss or abandonment

---

### arqo:DepositionEvent

**Label:** DepositionEvent

**Superclase:** crmarchaeo:A4_Stratigraphic_Genesis

**Descripción:** Event placing object into stratigraphic record

---

### arqo:DiscardEvent

**Label:** DiscardEvent

**Superclase:** crm:E5_Event

**Descripción:** Event of discard leading to archaeological record entry

---

### arqo:IntentionalBurial

**Label:** IntentionalBurial

**Superclase:** arqo:DepositionEvent

**Descripción:** Deliberate burial of an object

---

### arqo:RitualOffering

**Label:** RitualOffering

**Superclase:** arqo:DepositionEvent

**Descripción:** Votive or ritual placement

---

## Eventos de Recuperación (3)

### arqo:RecoveryDocumentation

**Label:** RecoveryDocumentation

**Superclase:** crm:E31_Document

**Descripción:** Documentation produced during recovery

---

### arqo:RecoveryEvent

**Label:** RecoveryEvent

**Superclase:** crmarchaeo:A1_Excavation_Process_Unit

**Descripción:** Excavation unit that recovered the object

---

### arqo:RecoveryObservation

**Label:** RecoveryObservation

**Superclase:** crmsci:S4_Observation

**Descripción:** Observation during recovery

---

## Contexto y Embebido (1)

### arqo:EmbeddingRelation

**Label:** EmbeddingRelation

**Superclase:** crmarchaeo:A7_Embedding

**Descripción:** Physical containment of an archaeological object within a stratigraphic volume unit with relative stability, following the CRMarchaeo embedding pattern (E18 - AP18i - A7 - AP19 - A2)

---

## Tipología y Clasificación (4)

### arqo:ClassificationMethod

**Label:** ClassificationMethod

**Superclase:** crm:E29_Design_or_Procedure

**Descripción:** Method employed for typological classification: monothetic (single diagnostic attribute) or polythetic (cluster analysis of multiple attributes)

---

### arqo:CompositionalGroup

**Label:** CompositionalGroup

**Superclase:** crm:E55_Type

**Descripción:** Group of metallic objects sharing characteristic elemental ratios or alloy signatures (Leitlegierung)

---

### arqo:CompositionalGroupAssignment

**Label:** CompositionalGroupAssignment

**Superclase:** crm:E17_Type_Assignment

**Descripción:** Assignment of a metallic object to a compositional group (Leitlegierung) defined by diagnostic elemental ratios or alloy signatures

---

### arqo:TypeToPeriodRelationship

**Label:** TypeToPeriodRelationship

**Superclase:** crm:E1_CRM_Entity

**Descripción:** Reified relationship between a typological type and a chronological period, with explicit strength level following CRMarchaeo AP29 (weak), AP31 (moderate), AP30 (strong)

---

## Análisis y Medición (2)

### arqo:InternalClockIndicator

**Label:** InternalClockIndicator

**Superclase:** crm:E26_Physical_Feature

**Descripción:** Measurable physical-chemical property serving as age indicator

---

### arqo:InternalClockMeasurement

**Label:** InternalClockMeasurement

**Superclase:** crmsci:S21_Measurement

**Descripción:** Scientific measurement of an internal clock indicator

---

## Interpretación y Significado (5)

### arqo:ArchaeologicalArchiveRecord

**Label:** ArchaeologicalArchiveRecord

**Superclase:** crm:E73_Information_Object

**Descripción:** Record within the archaeological archive documenting an object: field notebooks, digital databases, photographic archives, drawing collections, or published reports. Archive records function as archaeological objects in their own right.

---

### arqo:ArchiveCollection

**Label:** ArchiveCollection

**Superclase:** crm:E78_Curated_Holding

**Descripción:** Curated collection of archaeological archive records maintained by a research institution

---

### arqo:CulturalSignificanceAssignment

**Label:** CulturalSignificanceAssignment

**Superclase:** crm:E13_Attribute_Assignment

**Descripción:** Attribution of cultural, symbolic, or ritual significance to an object by researchers, descendant communities, or institutional narratives

---

### arqo:InterpretiveHypothesis

**Label:** InterpretiveHypothesis

**Superclase:** crminf:I4_Proposition_Set

**Descripción:** Competing or contradictory interpretive proposition regarding the identity, chronology, function, or cultural meaning of an archaeological object

---

### arqo:PastnessQuality

**Label:** PastnessQuality

**Superclase:** crm:E1_CRM_Entity

**Descripción:** Culturally constructed experiential quality of being 'from the past' that emerges from material traces of disintegration on an object's surface

---

## Actores y Grupos (1)

### arqo:CulturalCommunity

**Label:** CulturalCommunity

**Superclase:** crm:E74_Group

**Descripción:** Social group sharing cultural practices and material traditions

---

## Otros (18)

### arqo:BiographicalParallelism

**Label:** BiographicalParallelism

**Superclase:** crminf:I4_Proposition_Set

**Descripción:** Assertion that objects share similar biographical sequences

---

### arqo:ChaineOperatoire

**Label:** ChaineOperatoire

**Superclase:** crm:E29_Design_or_Procedure

**Descripción:** Complete ordered sequence of technical actions

---

### arqo:EmergencyCaching

**Label:** EmergencyCaching

**Superclase:** arqo:DepositionEvent

**Descripción:** Hasty concealment in response to threat

---

### arqo:FeatureEvidenceLink

**Label:** FeatureEvidenceLink

**Superclase:** crm:E1_CRM_Entity

**Descripción:** Reified evidential link between a significant feature and the chronological or cultural period it supports, with explicit strength assessment

---

### arqo:FragmentationState

**Label:** FragmentationState

**Superclase:** crm:E3_Condition_State

**Descripción:** Physical state of an object regarding its completeness: complete, partially fragmented, or reduced to isolated fragments

---

### arqo:FunctionalAssignment

**Label:** FunctionalAssignment

**Superclase:** crm:E13_Attribute_Assignment

**Descripción:** Interpretive assignment of function to an archaeological object, distinguishing primary intended function, secondary acquired function, and researcher-attributed function

---

### arqo:JoiningTechnique

**Label:** JoiningTechnique

**Superclase:** crm:E29_Design_or_Procedure

**Descripción:** Technical procedure used to connect component parts of a composite object, such as riveting, soldering, adhesion, mortise-and-tenon, or lashing

---

### arqo:ModeOfExperience

**Label:** ModeOfExperience

**Superclase:** crm:E3_Condition_State

**Descripción:** Heideggerian ontological mode: readiness-to-hand or presence-at-hand

---

### arqo:MorphometricAttribute

**Label:** MorphometricAttribute

**Superclase:** crmsci:S21_Measurement

**Descripción:** Quantitative physical measurement of an archaeological object including dimensions, weight, volume, surface area, and shape descriptors

---

### arqo:OntologicalShiftEvent

**Label:** OntologicalShiftEvent

**Superclase:** crm:E5_Event

**Descripción:** Event causing transition between modes of experience

---

### arqo:PresenceAtHand

**Label:** PresenceAtHand

**Superclase:** arqo:ModeOfExperience

**Descripción:** Object experienced as detached specimen

---

### arqo:ReadinessToHand

**Label:** ReadinessToHand

**Superclase:** arqo:ModeOfExperience

**Descripción:** Object experienced as available tool

---

### arqo:SignificantFeature

**Label:** SignificantFeature

**Superclase:** crm:E26_Physical_Feature

**Descripción:** Diagnostically relevant physical attribute of an object identified through systematic analysis that supports chronological or cultural assignment

---

### arqo:StylisticAssignment

**Label:** StylisticAssignment

**Superclase:** crm:E17_Type_Assignment

**Descripción:** Assignment of an object to a stylistic universe based on formal, decorative, and cultural attributes

---

### arqo:StylisticUniverse

**Label:** StylisticUniverse

**Superclase:** crm:E55_Type

**Descripción:** Corpus of objects sharing formal rules, decorative conventions, and cultural associations that define a coherent aesthetic-cultural system

---

### arqo:SurfaceAlteration

**Label:** SurfaceAlteration

**Superclase:** crm:E26_Physical_Feature

**Descripción:** Physical modification of an object's surface including patina, corrosion layers, weathering rinds, use-wear polish, and oxidation films

---

### arqo:TypologicalAssignment

**Label:** TypologicalAssignment

**Superclase:** crm:E17_Type_Assignment

**Descripción:** Researcher assignment of an object to a typological category, using either monothetic or polythetic classification methods

---

### arqo:VisualAppearanceAttribute

**Label:** VisualAppearanceAttribute

**Superclase:** crm:E26_Physical_Feature

**Descripción:** Observable visual property of an archaeological object in its current state of preservation, including Munsell color, surface texture, and general appearance

---

