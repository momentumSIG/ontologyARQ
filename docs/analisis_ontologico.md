# Semantic & Conceptual Extraction — Archaeological Object as Ontological Entity

> **Source:** 14 articles in `docs/objetoArqueologico/`
> **Purpose:** Support OWL ontology module design focused on archaeological objects and finds
> **Target ontologies:** CIDOC CRM, CRMarchaeo, CRMsci, CRMinf, CRMhs, ARIADNE AO-Cat

---

## Articles Analyzed

| # | File | Author(s) | Core Theme for Ontology |
|---|---|---|---|
| 1 | On Pastness | Holtorf | Pastness as interpretive construct vs intrinsic property |
| 2 | Things in the Eye of the Beholder | (humanistic perspective) | Object biography as narrative, not physical sequence |
| 3 | What do objects want? | Gosden | Object agency, form/genealogy/effect/source |
| 4 | csa_vol_23_2015_garcia-rovira | Garcia-Rovira | Process ontology, emergence, nature/culture entanglement |
| 5 | BF03376602 | (ceramic lifespans) | Use range ≠ manufacturing range, terminus post quem |
| 6 | rowe1959 | Rowe | Relative/absolute dating, seriation, cultural process |
| 7 | pollard2014 | Pollard | Object meaning, material culture as debate (tabua) |
| 8 | schwarcz2002 | Schwarcz | Chronometric methods (14C, U-series, K-Ar, Ar-Ar) |
| 9 | returning-archaeological-objects-to-italy | Gill | Repatriation, provenance chains, illicit trafficking |
| 10 | Maria_Filomena_Guerra_2003 | Guerra | Provenance determination, XRF, manufacturing techniques |
| 11 | Non-invasive studies | (multiple) | Non-destructive analysis of cultural heritage objects |
| 12 | sharing_conservation_decisions_2018 | ICCROM | Conservation decision-making, stakeholder values |
| 13 | Provenance Determination of Metal Objects | (Pernicka et al.) | Chemical provenance, lead isotopes, trace elements |
| 14 | 2949238 | (dating methods) | Overview of archaeological dating techniques |

---

# 1. Candidate Ontological Classes

For each class: label, definition, possible superclass, CIDOC CRM / CRMarchaeo alignment, and source evidence.

---

### Class: ArchaeologicalObject
**Definition:** Any physical object recovered from or studied within an archaeological context.  
**Superclass:** `crm:E19_Physical_Object`  
**Alignment:** `crm:E19_Physical_Object`  
**Evidence:** All articles — the central ontological entity of archaeological study. CRM already provides `E19_Physical_Object` as a perfect fit.

---

### Class: NaturalObject
**Definition:** Object of non-human origin found in archaeological context (ecofact).  
**Superclass:** `ArchaeologicalObject`  
**Alignment:** `crm:E19_Physical_Object`  
**Evidence:** Garcia-Rovira — discusses ecofacts and the nature/culture entanglement in archaeology. CRM does not distinguish natural from human-made at the `E19` level.

---

### Class: HumanMadeObject
**Definition:** Object created or modified by human agency.  
**Superclass:** `ArchaeologicalObject`  
**Alignment:** `crm:E22_Human-Made_Object`  
**Evidence:** All articles — CRM provides `E22_Human-Made_Object` for this distinction.

---

### Class: Artefact
**Definition:** Portable human-made object with functional purpose.  
**Superclass:** `HumanMadeObject`  
**Alignment:** `crm:E22_Human-Made_Object`  
**Evidence:** Gosden, Pollard — distinguishes portable functional objects from structures and symbolic objects.

---

### Class: AbioticObject
**Definition:** Non-living natural object (stone, mineral, sediment).  
**Superclass:** `NaturalObject`  
**Alignment:** `crm:E19_Physical_Object`  
**Evidence:** Garcia-Rovira — the nature/culture boundary requires distinguishing abiotic from biotic natural objects.

---

### Class: BioticObject
**Definition:** Living or once-living natural object (bone, shell, wood, plant remains).  
**Superclass:** `NaturalObject`  
**Alignment:** `crm:E19_Physical_Object`  
**Evidence:** Garcia-Rovira, BF03376602 — ecofacts include floral and faunal remains.

---

### Class: Structure
**Definition:** Non-portable human-made construction.  
**Superclass:** `HumanMadeObject`  
**Alignment:** `crm:E24_Physical_Human-Made_Thing`  
**Evidence:** Holtorf — discusses built heritage, buildings, monuments as objects with pastness.

---

### Class: ArtisticExpression
**Definition:** Human-made object with aesthetic or symbolic function rather than utilitarian.  
**Superclass:** `HumanMadeObject`  
**Alignment:** `crm:E22_Human-Made_Object`  
**Evidence:** Pollard — tabua (Fijian whale teeth) as objects whose value derives from meaning, not material.

---

### Class: ObjectBiography
**Definition:** Narrative sequence of events constituting the lifecycle of an archaeological object.  
**Superclass:** `crm:E5_Event` (container of biographical events)  
**Alignment:** No direct CRM class — needs extension.  
**Evidence:** "Things in the Eye of the Beholder" — object biography is a narrative construct told from a human perspective, not objective physical history. The biography changes depending on the interpreter. Kopytoff's "cultural biography of things."

---

### Class: ObjectLifecycle
**Definition:** Physical sequence of states and transitions an archaeological object undergoes from manufacture through deposition.  
**Superclass:** `crm:E5_Event` (container of lifecycle events)  
**Alignment:** No direct CRM class — needs extension.  
**Evidence:** BF03376602, Gosden — objects have measurable lifespans with identifiable phases: production, use, reuse, repair, discard. Distinct from biography (narrative) because lifecycle is the physical sequence of events.

---

### Class: ManufacturingEvent
**Definition:** Event of object production through specific technological procedures.  
**Superclass:** `crm:E12_Production`  
**Alignment:** `crm:E12_Production`  
**Evidence:** Guerra 2003, "Provenance Determination of Metal Objects" — manufacturing techniques identified through laboratory analysis (XRF, ICP-MS).

---

### Class: UseEvent
**Definition:** Event of object utilization in its original or assigned functional role.  
**Superclass:** `crm:E7_Activity`  
**Alignment:** `crm:E7_Activity`  
**Evidence:** BF03376602, Gosden — objects have active use-lives that may be substantially longer than their manufacturing date range.

---

### Class: ReuseEvent
**Definition:** Secondary use of an object for a function different from its original intended use.  
**Superclass:** `crm:E7_Activity`  
**Alignment:** `crm:E7_Activity`  
**Evidence:** "Things in the Eye of the Beholder" — objects accumulate multiple meanings through cycles of use and reuse over time.

---

### Class: RepairEvent
**Definition:** Physical modification of an object to restore its function or extend its use-life.  
**Superclass:** `crm:E81_Transformation`  
**Alignment:** `crm:E81_Transformation`  
**Evidence:** ICCROM "Sharing Conservation Decisions" — repair is a deliberate intervention. Distinguished from conservation in that repair occurred during use-life, not post-recovery.

---

### Class: DepositionEvent
**Definition:** Event of an object entering the archaeological record through intentional or accidental discard.  
**Superclass:** `crmarchaeo:A4_Stratigraphic_Genesis`  
**Alignment:** `crmarchaeo:A4_Stratigraphic_Genesis`  
**Evidence:** BF03376602 — deposition is the terminal event in the object lifecycle before post-depositional processes begin.

---

### Class: RecoveryEvent
**Definition:** Event of object being excavated or recovered from its depositional context.  
**Superclass:** `crmarchaeo:A1_Excavation_Process_Unit`  
**Alignment:** `crmarchaeo:A1_Excavation_Process_Unit`  
**Evidence:** BF03376602 — the transition from archaeological deposit to analyzed object.

---

### Class: ConservationTreatment
**Definition:** Post-recovery preservation action applied to an archaeological object.  
**Superclass:** `crm:E7_Activity`  
**Alignment:** `crm:E7_Activity`  
**Evidence:** ICCROM, "Non-invasive studies" — conservation is a post-excavation intervention distinct from both repair and scientific analysis.

---

### Class: AnalyticalEncounter
**Definition:** Scientific analysis event where physical or chemical properties of an object are measured.  
**Superclass:** `crmsci:S19_Encounter`  
**Alignment:** `crmsci:S19_Encounter`  
**Evidence:** Guerra 2003, "Non-invasive studies", Schwarcz — XRF, ICP-MS, radiocarbon dating, lead isotope analysis. Uses `crmsci` for scientific observation modeling.

---

### Class: ProvenanceChain
**Definition:** Traceable path from raw material source through production locus to findspot, reconstructed forensically.  
**Superclass:** `crm:E5_Event` (container for movement events)  
**Alignment:** No direct CRM class — needs extension.  
**Evidence:** Gill, Guerra, "Provenance Determination of Metal Objects" — provenance in archaeology is a forensic reconstruction from analytical evidence, not a directly observed sequence.

---

### Class: MaterialAssignment
**Definition:** Researcher's assertion about the material composition of an archaeological object.  
**Superclass:** `crm:E17_Type_Assignment`  
**Alignment:** `crm:E17_Type_Assignment`  
**Evidence:** Guerra, "Non-invasive studies" — material determination is a scientific interpretation, not an intrinsic property. Different techniques may yield different assignments.

---

### Class: TypologicalAssignment
**Definition:** Researcher's assignment of an object to a typological category based on diagnostic criteria.  
**Superclass:** `crm:E17_Type_Assignment`  
**Alignment:** `crm:E17_Type_Assignment`  
**Evidence:** Rowe 1959 — typology is the foundation of archaeological classification. `E17_Type_Assignment` correctly models this as a reified assignment rather than an intrinsic property.

---

### Class: ChronologicalAssignment
**Definition:** Researcher's assignment of an archaeological object or event to a temporal period.  
**Superclass:** `crm:E17_Type_Assignment`  
**Alignment:** `crm:E17_Type_Assignment`  
**Evidence:** Rowe, Schwarcz — chronologies are constructed, not given. Multiple dating techniques may produce conflicting assignments. Must be modeled as an assignment.

---

### Class: Pastness
**Definition:** Perceived quality of being from the past; a culturally constructed aesthetic and cognitive experience, not an intrinsic property of the object.  
**Superclass:** `crminf:I4_Proposition_Set`  
**Alignment:** No direct CRM class — needs extension via `crminf`.  
**Evidence:** Holtorf — "What they have taken away is the age of the paint." Pastness is experienced by audiences, not measured by instruments. It is a proposition about the object, not a property of the object.

---

### Class: Patina
**Definition:** Physical surface alteration of an object connoting age; valued culturally as evidence of authenticity, not merely damage.  
**Superclass:** `crm:E3_Condition_State`  
**Alignment:** `crm:E3_Condition_State` (with cultural significance extension)  
**Evidence:** Holtorf — Riegl's age-value and the "fantastic fascination of patina." Patina is a physical condition state that carries cultural meaning. Museums debate whether to clean/remove patina because it IS the evidence of pastness.

---

### Class: ObjectAgency
**Definition:** Capacity of an object to affect human behavior, actions, or perceptions independently of human intention.  
**Superclass:** None in CRM — new concept.  
**Alignment:** Needs extension. Maps conceptually to `crm:E5_Event` with object as participant-causation, but CRM is anthropocentric.  
**Evidence:** Gosden — "What do objects want?" Objects shape human behavior through their form, materiality, and cultural meanings. Not simple causality but a relational agency.

---

### Class: ProvenanceRegion
**Definition:** Geographic origin region of an object or its constituent materials.  
**Superclass:** `crm:E53_Place`  
**Alignment:** `crm:E53_Place`  
**Evidence:** Guerra, "Provenance Determination" — provenance regions are determined analytically (e.g., lead isotope ratios matching known geological sources).

---

### Class: RawMaterialSource
**Definition:** Geological or geographic source from which raw materials were extracted.  
**Superclass:** `crm:E53_Place`  
**Alignment:** `crm:E53_Place`  
**Evidence:** "Provenance Determination of Metal Objects" — mines, quarries, and clay sources are the origin of object materials. Distinguished from provenance region because objects may be manufactured far from their material source.

---

### Class: ChaineOperatoire
**Definition:** Operational sequence of manufacturing steps from raw material selection through object completion.  
**Superclass:** `crm:E29_Design_or_Procedure`  
**Alignment:** `crm:E29_Design_or_Procedure`  
**Evidence:** Garcia-Rovira — the chaine operatoire captures the technological process and cultural choices embedded in object manufacture.

---

### Class: ObjectForm
**Definition:** Morphological configuration of an object, including dimensions, shape, and surface characteristics.  
**Superclass:** `crm:E54_Dimension`  
**Alignment:** `crm:E54_Dimension`  
**Evidence:** Gosden — form is what objects present to the world. It determines function and cultural reading.

---

### Class: ConservationDecision
**Definition:** Decision-making process that determines what conservation treatment to apply, based on stakeholder values, technical constraints, and ethical considerations.  
**Superclass:** `crm:E5_Event`  
**Alignment:** No direct CRM class — needs extension.  
**Evidence:** ICCROM — conservation is not purely technical; it involves negotiating competing values (authenticity, access, research, preservation). The decision process itself needs modeling.

---

### Class: RepatriationEvent
**Definition:** Event of returning an archaeological object to its country or community of origin.  
**Superclass:** `crm:E9_Move`  
**Alignment:** `crm:E9_Move`  
**Evidence:** Gill — repatriation is a movement event but carries legal, ethical, and cultural dimensions not captured by `E9_Move` alone. Involves contested ownership, cultural patrimony law, and provenance investigation.

---

### Class: CirculationEvent
**Definition:** Event of an object moving between geographic locations or cultural zones during its use-life.  
**Superclass:** `crm:E9_Move`  
**Alignment:** `crm:E9_Move`  
**Evidence:** Gill, Guerra — objects travel through trade, gift exchange, migration, looting, and auction. CRM's `E9_Move` captures the movement; archaeological extension needed for the cultural significance.

---

### Class: ObjectTransformation
**Definition:** Deliberate or accidental change to an object's physical form, function, or meaning.  
**Superclass:** `crm:E81_Transformation`  
**Alignment:** `crm:E81_Transformation`  
**Evidence:** Garcia-Rovira — objects are always "becoming" rather than static. Transformations include fragmentation, repair, reuse, repurposing, ritual modification, and decay.

---

### Class: Fragmentation
**Definition:** Physical state where an object exists as multiple disconnected fragments rather than as a whole.  
**Superclass:** `crm:E3_Condition_State`  
**Alignment:** `crm:E3_Condition_State` (needs extension for part-whole modeling)  
**Evidence:** BF03376602 — archaeological ceramics are predominantly recovered as fragments (sherds). CRM models objects holistically; needs explicit part-whole modeling for fragmentation.

---

# 2. Candidate Object Properties

Semantic relationships between entities identified across the articles.

---

### Property: hasMaterial
**Domain:** `ArchaeologicalObject`  
**Range:** `crm:E57_Material`  
**Definition:** Indicates the material composition of an archaeological object.  
**Evidence:** All articles — foundational property linking objects to their constituent materials.

---

### Property: wasProducedBy
**Domain:** `HumanMadeObject`  
**Range:** `ManufacturingEvent`  
**Definition:** Links an object to the manufacturing event that produced it.  
**Evidence:** Guerra, Gosden, "Provenance Determination" — production is the origin event of every human-made object.

---

### Property: wasUsedIn
**Domain:** `ArchaeologicalObject`  
**Range:** `UseEvent`  
**Definition:** Links an object to an event in which it was actively used.  
**Evidence:** BF03376602 — objects have use-lives that are distinct from their manufacturing periods.

---

### Property: wasReusedIn
**Domain:** `ArchaeologicalObject`  
**Range:** `ReuseEvent`  
**Definition:** Links an object to a secondary use event after its original function ceased.  
**Evidence:** "Things in the Eye of the Beholder" — reuse transforms object meaning and extends biography.

---

### Property: wasRepairedIn
**Domain:** `ArchaeologicalObject`  
**Range:** `RepairEvent`  
**Definition:** Links an object to a repair intervention that restored or maintained its function.  
**Evidence:** ICCROM — repair is a pre-depositional modification distinct from post-excavation conservation.

---

### Property: wasDepositedIn
**Domain:** `ArchaeologicalObject`  
**Range:** `DepositionEvent`  
**Definition:** Links an object to the deposition event through which it entered the archaeological record.  
**Evidence:** BF03376602 — deposition is the terminal event of the object lifecycle.

---

### Property: wasRecoveredIn
**Domain:** `ArchaeologicalObject`  
**Range:** `RecoveryEvent`  
**Definition:** Links an object to the excavation or recovery event that removed it from its depositional context.  
**Evidence:** BF03376602 — the recovery event marks transition from archaeological deposit to analyzed object.

---

### Property: underwentTreatment
**Domain:** `ArchaeologicalObject`  
**Range:** `ConservationTreatment`  
**Definition:** Links an object to a conservation treatment applied after excavation.  
**Evidence:** ICCROM, "Non-invasive studies" — post-excavation intervention to stabilize or preserve the object.

---

### Property: wasSampledIn
**Domain:** `ArchaeologicalObject`  
**Range:** `AnalyticalEncounter`  
**Definition:** Links an object to a scientific sampling or analysis event.  
**Evidence:** Guerra, "Non-invasive studies", Schwarcz — non-invasive and micro-destructive analysis.

---

### Property: hasProvenance
**Domain:** `ArchaeologicalObject`  
**Range:** `ProvenanceRegion`  
**Definition:** Indicates the geographic region from which an object or its materials originated.  
**Evidence:** Gill, Guerra — provenance is a key archaeological research question.

---

### Property: derivesFromSource
**Domain:** `ArchaeologicalObject`  
**Range:** `RawMaterialSource`  
**Definition:** Identifies the geological or geographic source of the object's raw materials.  
**Evidence:** "Provenance Determination of Metal Objects" — lead isotopes and trace elements link objects to specific mines and quarries.

---

### Property: hasBiography
**Domain:** `ArchaeologicalObject`  
**Range:** `ObjectBiography`  
**Definition:** Links an object to its narrative biography — a human-constructed story of its lifecycle.  
**Evidence:** "Things in the Eye of the Beholder" — biography is a narrative interpretation, not the object's physical history.

---

### Property: hasLifecycle
**Domain:** `ArchaeologicalObject`  
**Range:** `ObjectLifecycle`  
**Definition:** Links an object to its physical lifecycle sequence of states and events.  
**Evidence:** Gosden, BF03376602 — distinct from biography, lifecycle is the actual physical trajectory.

---

### Property: hasTypologicalAssignment
**Domain:** `ArchaeologicalObject`  
**Range:** `TypologicalAssignment`  
**Definition:** Links an object to a researcher's typological classification.  
**Evidence:** Rowe — typology is the foundational archaeological classification method. Modeled as an assignment.

---

### Property: hasChronologicalAssignment
**Domain:** `ArchaeologicalObject`  
**Range:** `ChronologicalAssignment`  
**Definition:** Links an object to a researcher's temporal period assignment.  
**Evidence:** Rowe, Schwarcz — multiple dating methods may produce conflicting chronologies.

---

### Property: exhibitsPastness
**Domain:** `ArchaeologicalObject`  
**Range:** `Pastness`  
**Definition:** Links an object to the culturally perceived quality of being from the past.  
**Evidence:** Holtorf — pastness is not intrinsic age but experienced authenticity.

---

### Property: hasPatina
**Domain:** `ArchaeologicalObject`  
**Range:** `Patina`  
**Definition:** Indicates the physical surface alteration that connotes age and authenticity.  
**Evidence:** Holtorf — patina is both a physical condition state and a cultural value marker.

---

### Property: exertsAgency
**Domain:** `ArchaeologicalObject`  
**Range:** `ObjectAgency`  
**Definition:** Expresses the object's capacity to affect human behavior and perceptions.  
**Evidence:** Gosden — objects are not passive; their form and materiality shape human action.

---

### Property: hasForm
**Domain:** `ArchaeologicalObject`  
**Range:** `ObjectForm`  
**Definition:** Describes the morphological configuration of an object.  
**Evidence:** Gosden — form is the primary mode through which objects interact with humans.

---

### Property: followsChaineOperatoire
**Domain:** `HumanMadeObject`  
**Range:** `ChaineOperatoire`  
**Definition:** Links an object to its manufacturing operational sequence.  
**Evidence:** Garcia-Rovira — the chaine operatoire captures technological process and cultural choices.

---

### Property: wasRepatriatedIn
**Domain:** `ArchaeologicalObject`  
**Range:** `RepatriationEvent`  
**Definition:** Links an object to a repatriation event returning it to its country or community of origin.  
**Evidence:** Gill — repatriation is a contested movement with legal and ethical dimensions.

---

### Property: hasConservationDecision
**Domain:** `ArchaeologicalObject`  
**Range:** `ConservationDecision`  
**Definition:** Links an object to the decision-making process that determined its conservation treatment.  
**Evidence:** ICCROM — conservation decisions involve stakeholder negotiation and value assessment.

---

### Property: circulatedThrough
**Domain:** `ArchaeologicalObject`  
**Range:** `CirculationEvent`  
**Definition:** Links an object to a movement event during its active lifecycle.  
**Evidence:** Gill, Guerra — objects travel through trade, gift, migration, or looting.

---

### Property: underwentTransformation
**Domain:** `ArchaeologicalObject`  
**Range:** `ObjectTransformation`  
**Definition:** Links an object to a physical or functional transformation event.  
**Evidence:** Garcia-Rovira — objects are always in process, never static.

---

### Property: isFragmentedInto
**Domain:** `ArchaeologicalObject`  
**Range:** `ArchaeologicalObject`  
**Definition:** Links a whole object to its constituent fragments.  
**Evidence:** BF03376602 — fragmentary recovery is the archaeological norm, not the exception.

---

### Property: sharesProvenanceChain
**Domain:** `ArchaeologicalObject`  
**Range:** `ArchaeologicalObject`  
**Definition:** Indicates that two objects share the same provenance trajectory.  
**Evidence:** Gill — provenance investigation links objects through shared dealers, auctions, or looting events.

---

# 3. Candidate Data Properties

Attributes, measurements, and classifications identified in the articles.

---

### Data Property: hasManufacturingDateStart
**Domain:** `ManufacturingEvent`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The earliest date at which the object type was manufactured.  
**Evidence:** BF03376602 — manufacturing range must be distinguished from use range.

---

### Data Property: hasManufacturingDateEnd
**Domain:** `ManufacturingEvent`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The latest date at which the object type was manufactured.  
**Evidence:** BF03376602 — the terminus of production for the type, not the individual object.

---

### Data Property: hasUseDateStart
**Domain:** `UseEvent`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The earliest date at which a specific object was in active use.  
**Evidence:** BF03376602 — ceramic vessels can remain in use 15+ years after their type ceases to be manufactured.

---

### Data Property: hasUseDateEnd
**Domain:** `UseEvent`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The latest date at which a specific object was in active use.  
**Evidence:** BF03376602 — end of use-life, potentially decades after manufacturing ceased.

---

### Data Property: hasDepositionDate
**Domain:** `DepositionEvent`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The date at which the object entered the archaeological record.  
**Evidence:** BF03376602, Schwarcz — deposition is the key chronological anchor for archaeological stratigraphy.

---

### Data Property: hasTerminusPostQuem
**Domain:** `ArchaeologicalObject`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The earliest possible date for an object or context (date after which it must have been deposited).  
**Evidence:** BF03376602 — TPQ is "the cornerstone of all archaeological dating." Described as the most reliable chronological anchor.

---

### Data Property: hasTerminusAnteQuem
**Domain:** `ArchaeologicalObject`  
**Datatype:** `xsd:dateTime`  
**Meaning:** The latest possible date for an object or context (date before which it must have been deposited).  
**Evidence:** BF03376602 — TAQ provides the upper bound for archaeological dating.

---

### Data Property: hasRadiocarbonAge
**Domain:** `ChronologicalAssignment`  
**Datatype:** `xsd:decimal`  
**Meaning:** Uncalibrated radiocarbon age in years Before Present (BP).  
**Evidence:** Schwarcz — 14C is the most widely used absolute dating method.

---

### Data Property: hasCalibratedAgeInterval
**Domain:** `ChronologicalAssignment`  
**Datatype:** `xsd:string`  
**Meaning:** Calibrated calendar age range resulting from radiocarbon measurement.  
**Evidence:** Schwarcz — calibration converts radiocarbon years to calendar years with an uncertainty interval.

---

### Data Property: hasDatingMethod
**Domain:** `ChronologicalAssignment`  
**Datatype:** `xsd:string`  
**Meaning:** The analytical technique used to produce the chronological assignment (14C, U-series, K-Ar, Ar-Ar, TL, OSL).  
**Evidence:** Schwarcz, "2949238" — multiple chronometric methods exist with different precision and applicability.

---

### Data Property: hasLifespanDuration
**Domain:** `ObjectLifecycle`  
**Datatype:** `xsd:duration`  
**Meaning:** The total duration of an object's lifecycle from manufacture to deposition.  
**Evidence:** BF03376602 — ceramic lifespans of 15+ years documented in household contexts.

---

### Data Property: hasConservationState
**Domain:** `ArchaeologicalObject`  
**Datatype:** `xsd:string`  
**Meaning:** Qualitative description of the object's preservation condition.  
**Evidence:** ICCROM, Holtorf — conservation state determines treatment decisions and research potential.

---

### Data Property: hasPreservationRating
**Domain:** `ArchaeologicalObject`  
**Datatype:** `xsd:decimal`  
**Meaning:** Quantitative rating of preservation completeness (0.0 to 1.0).  
**Evidence:** ICCROM — standardized assessment for conservation prioritization.

---

### Data Property: hasAnalyticalTechnique
**Domain:** `AnalyticalEncounter`  
**Datatype:** `xsd:string`  
**Meaning:** The specific scientific technique employed (XRF, ICP-MS, SEM-EDS, XRD, Raman spectroscopy).  
**Evidence:** Guerra, "Non-invasive studies", "Provenance Determination" — technique determines what information can be extracted.

---

### Data Property: hasElementalComposition
**Domain:** `MaterialAssignment`  
**Datatype:** `xsd:string`  
**Meaning:** Elemental composition of the object determined analytically.  
**Evidence:** Guerra, "Provenance Determination" — elemental fingerprints link objects to sources.

---

### Data Property: hasLeadIsotopeRatio
**Domain:** `MaterialAssignment`  
**Datatype:** `xsd:decimal`  
**Meaning:** Measured lead isotope ratio (e.g., 206Pb, 207Pb, 208Pb vs 204Pb) used for provenance.  
**Evidence:** "Provenance Determination of Metal Objects" — lead isotope ratios are the gold standard for metal provenance.

---

### Data Property: hasRepatriationDate
**Domain:** `RepatriationEvent`  
**Datatype:** `xsd:date`  
**Meaning:** Date on which the object was formally returned to its country or community of origin.  
**Evidence:** Gill — repatriation dates are legally and politically significant.

---

### Data Property: hasCulturalSignificance
**Domain:** `ArchaeologicalObject`  
**Datatype:** `xsd:string`  
**Meaning:** Qualitative assessment of the object's cultural, symbolic, or ritual importance.  
**Evidence:** Pollard, Holtorf — cultural significance is distinct from functional role or material value.

---

### Data Property: hasObjectAgeValue
**Domain:** `Pastness`  
**Datatype:** `xsd:string`  
**Meaning:** The culturally assessed age-value of the object (not its chronological age).  
**Evidence:** Holtorf — Riegl's age-value: "what has been willed becomes, without intention" — value derives from perceived age, not measured age.

---

### Data Property: hasManufacturingTechnique
**Domain:** `HumanMadeObject`  
**Datatype:** `xsd:string`  
**Meaning:** The technological procedure used to manufacture the object (casting, hammering, wheel-throwing, etc.).  
**Evidence:** Guerra, "Provenance Determination" — technique affects elemental composition and isotopic signature.

---

# 4. Object Lifecycle Phases

The articles collectively describe the following lifecycle model for archaeological objects:

```
RAW MATERIAL EXTRACTION → MANUFACTURE (Chaine Operatoire) →
DISTRIBUTION / CIRCULATION → PRIMARY USE →
[REUSE] → [REPAIR] → DISCARD / DEPOSITION →
POST-DEPOSITIONAL PROCESSES → ARCHAEOLOGICAL RECOVERY →
CONSERVATION → LABORATORY ANALYSIS → INTERPRETATION →
MUSEUM CURATION / STORAGE → [REPATRIATION]
```

Bracketed phases are optional paths.

### Key transitions identified:

| Transition | Trigger Event | Articles |
|---|---|---|
| Use → Reuse | `ReuseEvent` — functional transformation | "Things in the Eye of the Beholder", BF03376602 |
| Use → Repair | `RepairEvent` — restoration intervention | ICCROM, BF03376602 |
| Use → Deposition | `DepositionEvent` — intentional or accidental discard | BF03376602 |
| Manufacture → Circulation | `CirculationEvent` — trade, exchange, migration | Gill, Guerra |
| Recovery → Conservation | `ConservationTreatment` — post-excavation intervention | ICCROM, "Non-invasive studies" |
| Conservation → Analysis | `AnalyticalEncounter` — laboratory examination | Guerra, Schwarcz |
| Museum → Repatriation | `RepatriationEvent` — return to origin | Gill |
| Post-deposition → Recovery | `RecoveryEvent` — excavation | BF03376602 |

### Lifecycle modeling insight (BF03376602):

**Critical ontological distinction:** The *manufacturing date range* of an object **type** is NOT the same as the *use date range* of a specific object **instance**. An object can remain in use for decades after its type ceases to be manufactured. This temporal gap between type and instance dating is poorly modeled in CRM.

---

# 5. Archaeological Processes

Processes identified across the articles, organized by domain.

---

### Cultural Processes (human-driven)

| Process | Description | Articles |
|---|---|---|
| **Production** | Manufacturing objects through technological procedures (chaine operatoire) | Guerra, Garcia-Rovira |
| **Use** | Active utilization of objects in daily/ritual practice | Gosden, BF03376602 |
| **Reuse/Recycling** | Secondary use after original function ends | "Things in the Eye of the Beholder" |
| **Repair** | Physical intervention to restore function | ICCROM |
| **Circulation** | Movement between geographic/cultural zones | Gill, Guerra |
| **Exchange/Gift** | Transfer of objects between social actors | Gosden, Pollard, "Things/Beholder" |
| **Ritualization** | Transformation of profane object to sacred status | Pollard (tabua), Holtorf |
| **Deposition** | Intentional or accidental entry into archaeological record | BF03376602 |
| **Conservation** | Post-recovery preservation intervention | ICCROM |
| **Interpretation** | Assignment of meaning, function, chronology | Rowe, Holtorf |

### Natural/Taphonomic Processes

| Process | Description | Articles |
|---|---|---|
| **Patination** | Surface chemical alteration over time | Holtorf |
| **Weathering** | Physical degradation from environmental exposure | Holtorf, ICCROM |
| **Fragmentation** | Physical breakage into component pieces | BF03376602 |
| **Bioturbation** | Biological disturbance of depositional context | BF03376602 |
| **Corrosion** | Chemical degradation of metals | "Provenance Determination" |

### Analytical Processes

| Process | Description | Articles |
|---|---|---|
| **Provenance determination** | Chemical/isotopic tracing of object origin | Guerra, "Provenance Determination" |
| **Chronometric dating** | Absolute dating via radiometric methods | Schwarcz, "2949238" |
| **Material characterization** | Identification of composition and structure | Guerra, "Non-invasive studies" |
| **Typological analysis** | Classification by diagnostic criteria | Rowe |
| **Seriation** | Relative chronological ordering by stylistic change | Rowe |
| **Non-invasive analysis** | Surface analysis without sampling | "Non-invasive studies" |
| **Provenance investigation** | Forensic reconstruction of object trajectory | Gill |

---

# 6. Typological and Classification Systems

Classification approaches identified in the articles:

| Classification Type | Basis | Articles |
|---|---|---|
| **Functional** | Object use and purpose | Gosden — objects classified by what they do/want |
| **Morphological** | Form, shape, dimensions | Gosden — object form determines reading |
| **Technological** | Manufacturing technique (chaine operatoire) | Garcia-Rovira |
| **Material** | Chemical composition, fabric | Guerra, "Provenance Determination" |
| **Cultural/Contextual** | Cultural affiliation, style zone | Rowe, Pollard |
| **Temporal** | Chronological period (seriation) | Rowe |
| **Stylistic** | Decorative motifs, artistic tradition | Pollard |
| **Typological** | Formal diagnostic criteria | Rowe — the foundation of archaeological classification |
| **Provenance-based** | Geographic origin | Gill, "Provenance Determination" |

### Key ontological insight (Rowe, BF03376602):

Archaeological classification is always an **assignment** (`crm:E17_Type_Assignment`), not an intrinsic property. The same object can receive different classifications from different researchers using different typological schemes. Classification must be modeled as a reified relationship, not a direct attribute.

---

# 7. Ontological Gaps in CIDOC CRM / CRMarchaeo

Concepts that are archaeologically important but poorly or not at all modeled in the target ontologies.

---

### Gap 1: Object biography as narrative (vs physical history)

**Description:** CRM models events as objective historical occurrences. But object biography — as discussed in "Things in the Eye of the Beholder" and Holtorf — is a *narrative construct* told from a human perspective. The same object can have multiple, competing biographies told by different interpreters. CRM has no mechanism for distinguishing the narrative account from the physical events.

**CRM deficiency:** `E5_Event` models what happened; it does not model stories told about what happened.

**Suggested extension:** `ObjectBiography` class as a narrative container (subclass of `crminf:I4_Proposition_Set`) that groups biographical claims, each of which is a proposition that may or may not correspond to actual events.

---

### Gap 2: Pastness as perceived quality (vs chronological age)

**Description:** Holtorf argues that "age" and "pastness" are fundamentally different concepts. Chronological age is a measurable temporal distance. Pastness is an aesthetic, emotional, cultural experience of antiquity that is NOT reducible to measured age. An object can be chronologically old but not feel old; or chronologically recent but feel ancient (the theme park problem).

**CRM deficiency:** `E52_Time-Span` models chronological extent. There is no class for the *experienced* quality of being old.

**Suggested extension:** `Pastness` class (subclass of `crminf:I4_Proposition_Set`) capturing the culturally constructed, audience-dependent quality. Connected to object via `exhibitsPastness` property.

---

### Gap 3: Object agency and material causation

**Description:** Gosden argues that objects "want" things — they shape human behavior through their form, materiality, and embedded cultural meanings. CRM is anthropocentric: all events are driven by human actors (`E39_Actor`). Objects participate in events (`E19_Physical_Object`) but cannot initiate or cause them.

**CRM deficiency:** No modeling of non-human causation. The "object acted on human" relationship has no home in CRM.

**Suggested extension:** `ObjectAgency` class or reification of the object-as-cause pattern. Could be modeled as a qualified relation linking object + effect + evidence.

---

### Gap 4: Manufacturing date range vs object use range

**Description:** BF03376602 demonstrates that the manufacturing range of an object *type* is systematically different from the use range of a specific object *instance*. Ceramics can remain in household use 15+ years after their type ceases manufacturing. Many archaeologists conflate type-date with object-date, producing misleading chronologies.

**CRM deficiency:** `E52_Time-Span` can model a temporal extent, but CRM has no pattern for distinguishing the temporal extent of a type from the temporal extent of an instance of that type.

**Suggested extension:** Separate temporal properties for manufacturing period and use period. `hasManufacturingDateStart/End` on `ManufacturingEvent` vs `hasUseDateStart/End` on `UseEvent`.

---

### Gap 5: Patina as cultural value (not just physical condition)

**Description:** Holtorf describes patina as both a physical surface condition AND a cultural value. CRM has `E3_Condition_State` for physical condition, but it does not capture the *cultural valuation* of condition states. A metal object's corrosion may be scientifically detrimental but culturally valued as evidence of authenticity.

**CRM deficiency:** `E3_Condition_State` models condition. No class models the *cultural meaning* of condition.

**Suggested extension:** `Patina` subclass of `E3_Condition_State` with additional properties capturing cultural significance, authenticity claims, and conservation debates. Separate technical assessment from cultural valuation.

---

### Gap 6: Provenance as forensic reconstruction (not observed chain)

**Description:** Gill, Guerra, and Pernicka all describe provenance determination as a *forensic reconstruction* working backwards from analytical evidence: lead isotopes → geological source → mining region → manufacturing locus → trade route → findspot. CRM's `E9_Move` models forward movement but not the backward reconstruction process.

**CRM deficiency:** No modeling of the evidentiary chain that supports provenance claims. The claim "object X came from region Y" is a scientific conclusion, not a directly observed fact.

**Suggested extension:** `ProvenanceChain` class that groups `E9_Move` events into a reconstructed trajectory, linked to `crmsci:S4_Observation` evidence that supports each link in the chain.

---

### Gap 7: Fragmentation and part-whole modeling

**Description:** Archaeological objects are predominantly recovered as fragments (sherds, broken tools, partial remains). CRM models objects as wholes (`E19_Physical_Object`) with `P46_is_composed_of` for components, but does not distinguish intentional components from accidental fragments. A potsherd is NOT a component — it is a fragment of a once-whole object.

**CRM deficiency:** No distinction between intentional part-whole (components of a composite) and accidental fragmentation (broken pieces of a once-whole object).

**Suggested extension:** `Fragmentation` class (subclass of `E3_Condition_State`) with `isFragmentedInto` property linking the conceptual whole to its physical fragments.

---

### Gap 8: Repatriation as contested custodianship

**Description:** Gill describes repatriation as involving legal claims, provenance investigation, diplomatic negotiation, and cultural patrimony law. CRM's `E9_Move` captures the physical transfer but not the contested ownership, the legal framework, or the ethical dimension.

**CRM deficiency:** No modeling of custody, ownership, or the legal/cultural context of object possession.

**Suggested extension:** `RepatriationEvent` subclass of `E9_Move` with links to legal instruments, claimant communities, diplomatic processes, and provenance evidence that justified the return.

---

### Gap 9: Conservation decision-making as a process

**Description:** ICCROM's volume demonstrates that conservation decisions involve competing stakeholder values (authenticity vs access vs research vs preservation), risk assessment, technical constraints, and ethical frameworks. The decision process itself needs ontological modeling, not just the resulting treatment.

**CRM deficiency:** No modeling of how preservation decisions are reached, only that a treatment activity occurred (`E7_Activity`).

**Suggested extension:** `ConservationDecision` class capturing the decision process, stakeholders consulted, values prioritized, and alternatives considered.

---

### Gap 10: Object transformation states

**Description:** Garcia-Rovira emphasizes that objects are always in process, always "becoming." CRM has `E81_Transformation` for discrete transformation events, but objects undergo continuous, incremental change that is hard to model as discrete events.

**CRM deficiency:** Single `E81_Transformation` event does not easily capture gradual, continuous state change over time.

**Suggested extension:** `ObjectTransformation` class that can represent continuous transformation processes, with temporal extent and measurable state changes.

---

### Gap 11: Ecofact vs Artefact boundary

**Description:** Garcia-Rovira discusses the nature/culture entanglement. An unmodified stone used as a hammer is an ecofact in origin but an artefact in use. A bone with cut marks is both natural and cultural. The boundary is often ambiguous.

**CRM deficiency:** `E19_Physical_Object` collapses both natural and human-made objects. `E22_Human-Made_Object` requires intentional modification, but many archaeological objects occupy ambiguous positions.

**Suggested extension:** `NaturalObject` / `HumanMadeObject` distinction at the `ArchaeologicalObject` level. Allow objects to carry properties of both categories (e.g., a natural object that was used but not modified).

---

### Gap 12: Uncertain and contested classification

**Description:** Rowe demonstrates that classification is always provisional and often contested. CRM's `E17_Type_Assignment` models this correctly, but archaeologically, many objects are unclassifiable, ambiguously classified, or subject to competing classifications.

**CRM deficiency:** `E17_Type_Assignment` models one assignment at a time. No model for multiple competing assignments, or for the explicit declaration that an object is unclassifiable.

**Suggested extension:** Allow multiple `TypologicalAssignment` instances per object from different interpreters/taxonomies/dates. Add explicit "unclassifiable" state.

---

# 8. Potential Ontology Modules

Modules that could be developed from the extracted concepts.

---

### Module 1: Object Biography & Lifecycle

**Main concepts:** `ObjectBiography`, `ObjectLifecycle`, `ManufacturingEvent`, `UseEvent`, `ReuseEvent`, `RepairEvent`, `DepositionEvent`, `RecoveryEvent`, `CirculationEvent`  
**Main relations:** `hasBiography`, `hasLifecycle`, `wasProducedBy`, `wasUsedIn`, `wasReusedIn`, `wasDepositedIn`, `wasRecoveredIn`, `circulatedThrough`  
**Ontology reuse:** `crm:E5_Event`, `crm:E12_Production`, `crm:E7_Activity`, `crm:E9_Move`, `crm:E81_Transformation`, `crmarchaeo:A4_Stratigraphic_Genesis`, `crmarchaeo:A1_Excavation_Process_Unit`

---

### Module 2: Material Transformation

**Main concepts:** `ObjectTransformation`, `Fragmentation`, `Patina`, `RepairEvent`  
**Main relations:** `underwentTransformation`, `isFragmentedInto`, `hasPatina`, `wasRepairedIn`  
**Ontology reuse:** `crm:E81_Transformation`, `crm:E3_Condition_State`

---

### Module 3: Provenance & Circulation

**Main concepts:** `ProvenanceChain`, `ProvenanceRegion`, `RawMaterialSource`, `CirculationEvent`, `RepatriationEvent`  
**Main relations:** `hasProvenance`, `derivesFromSource`, `circulatedThrough`, `wasRepatriatedIn`, `sharesProvenanceChain`  
**Ontology reuse:** `crm:E53_Place`, `crm:E9_Move`

---

### Module 4: Classification & Typology

**Main concepts:** `TypologicalAssignment`, `ChronologicalAssignment`, `MaterialAssignment`, `ObjectForm`  
**Main relations:** `hasTypologicalAssignment`, `hasChronologicalAssignment`, `hasForm`  
**Ontology reuse:** `crm:E17_Type_Assignment`, `crm:E55_Type`, `crm:E54_Dimension`

---

### Module 5: Chronometric Framework

**Main concepts:** `ChronologicalAssignment`, `ManufacturingEvent`, `UseEvent`, `DepositionEvent`  
**Main relations:** `hasChronologicalAssignment`, `datedByMethod`, `hasTPQ`, `hasTAQ`  
**Data properties:** `hasManufacturingDateStart/End`, `hasUseDateStart/End`, `hasDepositionDate`, `hasRadiocarbonAge`, `hasCalibratedAgeInterval`, `hasDatingMethod`, `hasLifespanDuration`  
**Ontology reuse:** `crm:E52_Time-Span`, `crmsci:S21_Measurement`

---

### Module 6: Conservation & Post-Excavation

**Main concepts:** `ConservationTreatment`, `ConservationDecision`, `AnalyticalEncounter`  
**Main relations:** `underwentTreatment`, `hasConservationDecision`, `wasSampledIn`  
**Data properties:** `hasConservationState`, `hasPreservationRating`, `hasAnalyticalTechnique`, `hasElementalComposition`, `hasLeadIsotopeRatio`  
**Ontology reuse:** `crm:E7_Activity`, `crmsci:S19_Encounter`, `crmsci:S21_Measurement`

---

### Module 7: Object Meaning & Agency

**Main concepts:** `Pastness`, `Patina`, `ObjectAgency`, `ArtisticExpression`  
**Main relations:** `exhibitsPastness`, `hasPatina`, `exertsAgency`, `hasCulturalSignificance`  
**Ontology reuse:** `crminf:I4_Proposition_Set`, `crm:E3_Condition_State`

---

### Module 8: Analytical Provenance

**Main concepts:** `AnalyticalEncounter`, `MaterialAssignment`, `ProvenanceChain`, `RawMaterialSource`  
**Main relations:** `wasSampledIn`, `hasProvenance`, `derivesFromSource`  
**Data properties:** `hasAnalyticalTechnique`, `hasElementalComposition`, `hasLeadIsotopeRatio`  
**Ontology reuse:** `crmsci:S19_Encounter`, `crmsci:S21_Measurement`, `crm:E53_Place`

---

# 9. Semantic Patterns

Recurring semantic structures identified across the articles.

---

### Pattern 1: Event-driven object biography

**Description:** Object lifecycle = sequence of ordered events (manufacture → use → reuse → repair → deposition). Each event is a discrete temporal entity with actors, places, and time-spans.

**CRM mapping:** Matches the CRM Event pattern. `E5_Event` subclasses provide the backbone. The archaeological extension adds specific event types not in CRM (ReuseEvent, CirculationEvent, RepatriationEvent).

---

### Pattern 2: Object-state transition

**Description:** Objects change state over time (from whole to fragmented, from pristine to patinated, from functional to discarded). State transitions are not always discrete events — some are gradual, continuous processes.

**CRM mapping:** `E81_Transformation` and `E3_Condition_State` provide partial support. Needs extension for continuous transformation processes.

---

### Pattern 3: Actor-Object-Event triad

**Description:** Articles consistently describe three-way relationships: a human actor (E39_Actor) performs an event (E5_Event) involving an object (E19_Physical_Object). However, Gosden inverts this: the object "acts" on the human.

**CRM mapping:** Standard CRM triad (Actor → Event → Object) captures most relationships. Object agency requires an extension that treats the object as a causal participant rather than passive participant.

---

### Pattern 4: Assignment vs intrinsic property

**Description:** Many archaeological "facts" — material composition, typology, chronology, function, provenance, cultural significance — are NOT intrinsic properties of objects. They are *assignments* made by researchers based on evidence and interpretation. They must be modeled as reified statements (`E17_Type_Assignment`), not direct attributes.

**CRM mapping:** CRM already provides `E17_Type_Assignment` for this pattern. The archaeological extension should model specific sub-types of assignment (TypologicalAssignment, ChronologicalAssignment, MaterialAssignment) and allow multiple competing assignments.

---

### Pattern 5: Forensic reconstruction chain

**Description:** Provenance and chronology in archaeology are reconstructed *backward* from analytical evidence. Lead isotope ratios → geological source; radiocarbon dates → calibrated calendar age; ceramic type → manufacturing region. The evidence chain goes from measurement → interpretation → conclusion.

**CRM mapping:** `crmsci:S4_Observation` and `crmsci:S21_Measurement` provide the evidence layer. `E17_Type_Assignment` provides the conclusion layer. The missing piece is the explicit chain linking measurements to conclusions.

---

### Pattern 6: Narrative-as-knowledge

**Description:** Holtorf and "Things in the Eye of the Beholder" both emphasize that object stories (biographies, provenances, chronologies) are *narratives told by humans*, not objective truths. The same object can have multiple competing biographies. This maps to the distinction between what happened (event) and what is believed to have happened (proposition).

**CRM mapping:** `crminf:I4_Proposition_Set` provides the foundation for modeling narratives as sets of propositions held by interpreters. The archaeological extension adds specific proposition types (biographical claim, provenance claim, chronological claim).

---

# 10. CIDOC CRM Compatibility Summary

| Archaeological Concept | CRM Alignment | Extension Needed? |
|---|---|---|
| Physical archaeological object | `crm:E19_Physical_Object` | No |
| Manufactured object | `crm:E22_Human-Made_Object` | No |
| Built structure | `crm:E24_Physical_Human-Made_Thing` | No |
| Object material | `crm:E57_Material` + `P45_consists_of` | No |
| Production event | `crm:E12_Production` | No |
| Use event | `crm:E7_Activity` | No |
| Object reuse/repair | `crm:E81_Transformation` | No |
| Movement/circulation | `crm:E9_Move` | No |
| Archaeological deposition | `crmarchaeo:A4_Stratigraphic_Genesis` | No |
| Excavation recovery | `crmarchaeo:A1_Excavation_Process_Unit` | No |
| Scientific analysis | `crmsci:S19_Encounter` + `S21_Measurement` | No |
| Typological classification | `crm:E17_Type_Assignment` | No |
| Time/chronology | `crm:E52_Time-Span` | No |
| Place/provenance | `crm:E53_Place` | No |
| Physical condition | `crm:E3_Condition_State` | No |
| Human actor | `crm:E39_Actor` | No |
| **Object biography as narrative** | None | **Yes** — needs `ObjectBiography` class |
| **Object lifecycle as physical sequence** | Partial | **Yes** — needs `ObjectLifecycle` class |
| **Pastness (perceived age)** | None | **Yes** — needs `Pastness` class via `crminf` |
| **Patina as cultural value** | `crm:E3_Condition_State` partial | **Yes** — needs cultural valuation extension |
| **Object agency** | None | **Yes** — new concept outside CRM |
| **Manufacturing date vs use date** | None | **Yes** — temporal nuance of type vs instance |
| **Provenance forensic chain** | Partial (`E9_Move` chain) | **Yes** — needs reconstruction/evidence modeling |
| **Fragmentation** | Partial (`E3_Condition_State`) | **Yes** — needs part-whole distinction |
| **Repatriation legal/cultural context** | `E9_Move` partial | **Yes** — needs legal/cultural dimensions |
| **Conservation decision process** | None | **Yes** — new concept |
| **Continuous transformation** | `E81_Transformation` partial | **Yes** — needs continuous process modeling |
| **Ecofact/artefact boundary** | None | **Yes** — needs `NaturalObject` / `HumanMadeObject` |
| **Multiple competing classifications** | `E17_Type_Assignment` partial | **Yes** — needs multi-assignment pattern |
| **Chaine operatoire** | `crm:E29_Design_or_Procedure` | No |
| **Object form** | `crm:E54_Dimension` | No |
