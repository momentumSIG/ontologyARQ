# AGENTS.md

# Project Overview

This project focuses on ontology engineering for archaeology and cultural heritage using Large Language Models (LLMs).

The main objective is to identify ontological gaps in CRMarchaeo and design compatible ontology extensions centered on archaeological finds and archaeological objects recovered during excavation processes.

The project combines:
- ontology engineering
- competency-question-driven design
- CIDOC CRM interoperability
- experimental ontology generation with LLMs
- evaluation of prompting strategies

The ontology must remain semantically compatible with:
- CIDOC CRM
- CRMarchaeo
- CRMsci
- CRMinf
- CRMhs
- ARIADNE AO-Cat
- GeoSPARQL
- OWL-Time
- PROV-O
- GeoSciML
- SKOS


---

# Current Research Focus

The current ontology engineering work focuses primarily on the following sections of the previous CRMarchaeo gap analysis (which you can read at /docs/analisis.docx):

## Section 3 — Ontological Extension Design

Priority subsections:
- 3.1 Archaeological Object Module
- 3.4 Spatial and Geospatial Module
- 3.5. Temporal Module

## Section 4 — External Ontology Integration

Priority subsections:
- 4.1 UML comparison with IDEArq conceptual model
- 4.3 GeoSPARQL / OGC integration and PeriodO alignment
- 4.4 OWL-Time and GeosciMl integration 
- PROV-O integration and provenance modeling

---

# Main Ontological Goal

The primary objective is to create a new archaeological object ontology module that complements CRMarchaeo.

CRMarchaeo mainly models:
- excavation processes
- stratigraphy
- stratigraphic relationships
- stratigraphic genesis
- archaeological observation

The new ontology module must extend these capabilities toward:
- archaeological finds
- artifact lifecycle
- object biography
- materiality
- use and reuse
- deposition
- archaeological interpretation

The ontology should connect archaeological objects wit these sections but in the future, not now:
- excavation events
- stratigraphic units
- depositional events
- spatial entities
- temporal entities
- archaeological interpretations

An archaelogical experts thinks that a physical object can be a superclass of natural objects and E22human-made object or E24Physical Human-Made Thing (we are not sure). Natural objects can be divided into abiotic and biotic objects, and human-made objects into artifacts, structures, and artistic expressions.
In this moment we only want to module the object per se.
---

# Project Documentation Sources

The following sources are authoritative references for ontology generation and analysis.

## External Ontologies

- CIDOC CRM
- CRMarchaeo
- CRMsci
- CRMinf
- CRMhs
- ARIADNE AO-Cat
- GeoSPARQL
- OWL-Time
- PROV-O
- GeoSciML
- SKOS

---

# Internal Documentation

The folder:

ontologies_docs/

contains:
- OWL ontologies
- TTL ontologies
- HTML ontologies
- PDF ontologies
- ontology specifications
- PDF conceptual documentation

These files are authoritative conceptual references.

---

# UML Reference Model

The file:

idearq_v3b.pdf

contains the UML conceptual model for IDEArq.

This UML model must be analyzed to:
- identify archaeological object entities
- identify object attributes
- identify contextual relationships
- identify missing semantics
- identify implicit ontology patterns
- derive competency questions

The UML model must NOT be translated directly into OWL.

Instead:
- reinterpret UML semantics conceptually
- align concepts with CIDOC CRM
- avoid ontology anti-patterns
- preserve semantic interoperability

---

# Competency Question Strategy

Competency Questions (CQ) are the central ontology engineering methodology.

CQ generation is inspired by:
- Ontogenia
- ontologyLLM.pdf in the folder /docs
- CQ-driven ontology engineering

CQ must be grouped into four thematic blocks.

---

# CQ Block 1 — Archaeological Object

Target topics:
- object biography
- materiality
- typology
- function
- reuse
- deposition
- conservation
- manufacturing
- human agency

Target amount:
- 20 CQ

---

# CQ Block 2 — Spatial

Target topics:
- excavation context
- GIS integration
- geometry
- landscape
- territory
- inter-site relations
- spatial uncertainty
- spatial precision
- 3D geometry
- GeoSPARQL alignment

Target amount:
- y 20 CQ

---

# CQ Block 3 — Temporal

Target topics:
- relative chronology
- absolute chronology
- archaeological periods
- geological periods
- temporal uncertainty
- temporal intervals
- OWL-Time integration
- GeoSciML TimeScale alignment
- hybrid chronologies

Target amount:
- 20 CQ

---

# CQ Block 4 — Stratigraphy

Target topics:
- stratigraphic units
- depositional processes
- stratigraphic correlation
- formation processes
- geoarchaeology
- sedimentary interpretation
- stratigraphic uncertainty

Target amount:
- 20 CQ

---

# CQ Requirements

Each competency question must include:
- competency question
- ontology modules required
- possible ontology reuse
- complexity classification (block of the CQ)
- which language model generated the CQ
---

# Gold Standard Extraction

For each CQ:
- identify minimal ontology modules required
- identify required classes
- identify required properties
- identify required alignments

These extracted modules act as gold standards for LLM ontology evaluation.

---

# Ontology Generation Strategies

The project compares two ontology generation workflows.

## Strategy 1 — Memoryless CQbyCQ

Characteristics:
- each CQ processed independently
- no ontology memory
- RDF context remains empty
- reduced context size

Reference:
https://github.com/dersuchendee/Onto-Generation

---

## Strategy 2 — Ontogenia

Characteristics:
- iterative ontology extension
- ontology memory accumulation
- RDF context persists across iterations
- semantic reuse encouraged
- incremental ontology construction

Reference:
https://github.com/dersuchendee/Onto-Generation

---

# Temperature Evaluation

Temperature is treated as an experimental variable.

Suggested evaluation temperatures:
- 0.3
- 0.5
- 0.7

Evaluation dimensions:
- semantic consistency
- ontology drift
- redundancy generation
- CIDOC CRM alignment
- determinism
- ontology stability
- hallucinated ontology entities
- CQ coverage

Generated ontologies must be stored separately by:
- prompting strategy
- temperature
- iteration

Example structure:

generated_ontologies/
├── memoryless/
│   ├── temp_0_3/
│   ├── temp_0_5/
│   └── temp_0_7/
│
├── ontogenia/
│   ├── temp_0_3/
│   ├── temp_0_5/
│   └── temp_0_7/

---

# Blank Node Guidelines

Blank nodes are allowed ONLY when semantically justified.

Potential valid scenarios:
- qualified relations
- observations
- measurements
- provenance chains
- temporal qualification
- uncertain attribution
- analytical events
- inferential statements

Prefer explicit ontology classes when:
- entities require identity
- entities require provenance
- entities require reuse
- entities require independent querying

Avoid unnecessary blank node proliferation.

---

# Archaeological Object Modeling Principles

Archaeological objects must NOT be modeled as static isolated entities.

The ontology must support:
- lifecycle
- biography
- transformation
- reuse
- deposition
- excavation recovery
- sampling
- laboratory analysis
- interpretation
- post-excavation analysis

---

# Spatial Modeling Principles

Use:
- GeoSPARQL
- OGC standards
- WKT geometries

Support:
- 2D geometry
- 3D geometry
- multiscale spatial representation
- uncertainty
- precision metadata

---

# Temporal Modeling Principles

Use:
- OWL-Time
- PeriodO
- GeoSciML TimeScale

Support:
- relative chronology
- absolute chronology
- archaeological periods
- geological periods
- uncertain dates
- hybrid temporal systems

---

# Inference Modeling Principles

Use:
- CRMinf
- PROV-O

Explicitly separate:
- observation
- interpretation
- inference
- hypothesis

Represent:
- evidence chains
- confidence
- competing interpretations
- provenance of knowledge

---

# Ontology Engineering Principles

Always:
- reuse ontology terms before creating new ones
- preserve CIDOC CRM compatibility
- maintain semantic interoperability
- preserve logical consistency
- prefer modular design
- preserve ontology traceability

Avoid:
- ontology redundancy
- artificial hierarchies
- unnecessary reification
- isolated ontology fragments
- UML-style data schemas disguised as ontologies

---

# Preferred Serialization

Preferred serialization:
- Turtle (.ttl)

Ontology requirements:
- OWL 2 compatible
- RDF valid
- SPARQL queryable
- reasoner compatible
- CIDOC CRM aligned

---

# Evaluation Goals

The project evaluates:
- ontology quality
- semantic consistency
- ontology modularity
- CQ coverage
- interoperability
- ontology reuse
- reasoning capability
- archaeological semantic expressiveness

The final objective is to develop a CIDOC-CRM-aware archaeological ontology generation benchmark using LLMs.

---

# Workflow Executed — deepseek-v4-pro

This section documents the workflow already executed by deepseek-v4-pro on 2026-05-21. Use this as a reference to reproduce the same steps with another LLM.

## Step 1 — Competency Question Generation

80 CQs were generated across 4 thematic blocks (20 each). The CQs were sourced from:

| Source | Count | Description |
|---|---|---|
| `docs/PreguntasCompetencia.docx` | 36 | Original CQs generated by ChatGPT, filtered to exclude inference reasoning, translated to English |
| `docs/analisis.docx` gap analysis | 44 | New CQs generated by deepseek-v4-pro covering ontological gaps in CRMarchaeo |

### Blocks

| Block | File | Reused | New | Total |
|---|---|---|---|---|
| Archaeological Object | `CQ/CQ_Deepseekv4Pro/CQ-object-deepseek.md` | 8 | 12 | 20 |
| Spatial | `CQ/CQ_Deepseekv4Pro/CQ-spatial-deepseek.md` | 11 | 9 | 20 |
| Temporal | `CQ/CQ_Deepseekv4Pro/CQ-temporal-deepseek.md` | 9 | 11 | 20 |
| Stratigraphy | `CQ/CQ_Deepseekv4Pro/CQ-stratigraphy-deepseek.md` | 8 | 12 | 20 |

CQ format per question:
```markdown
## CQ-OBJ-01
**Question:** [question text]
- **Ontology modules required:** [modules]
- **Possible ontology reuse:** [ontologies and classes]
```

## Step 2 — Prompt Template Adaptation

Two prompting strategies from [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) (Lippolis et al., ESWC 2025) were adapted for the archaeological domain:

| Strategy | File | Description |
|---|---|---|
| Memoryless CQbyCQ | `prompts/memoryless/prompt_archaeological_object.md` | Each CQ processed independently. RDF context always empty. `{story}` = archaeological domain narrative. `{CQ}` = each CQ-OBJ-XX. |
| Ontogenia | `prompts/ontogenia/prompt_archaeological_object.md` | Iterative ontology extension with metacognitive prompting. 9-step procedure. `{previous_output}` = accumulated RDF. `{scenario}` = archaeological domain. |

Both templates include:
- Namespace prefixes (`arqo:`, `crm:`, `crmarchaeo:`, `crmsci:`, etc.)
- CRMarchaeo alignment rules
- Reification guidelines for pivot classes
- Common mistakes to avoid

## Step 3 — Ontology Generation

The Archaeological Object module was generated using both strategies at 3 temperatures.

### Directory structure

```
ontologies_generated/Deepseekv4/
├── memoryless/
│   ├── temp_0_3/          # 20 .ttl files (one per CQ)
│   ├── temp_0_5/          # 20 .ttl files
│   └── temp_0_7/          # 20 .ttl files
├── ontogenia/
│   ├── temp_0_3/          # 20 step files + cumulative.ttl
│   ├── temp_0_5/          # 20 step files + cumulative.ttl
│   └── temp_0_7/          # 20 step files + cumulative.ttl
└── README.md              # Full documentation
```

### File counts

| Category | Files |
|---|---|
| Memoryless CQbyCQ .ttl | 60 |
| Ontogenia step .ttl | 60 |
| Ontogenia cumulative .ttl | 3 |
| Prompt templates | 2 |
| CQ files | 4 |
| Documentation | 1 |
| **Total** | **130** |

### Temperature simulation strategy

When the LLM does not expose a temperature parameter, simulate it through output style:

| Temperature | Style | Effect |
|---|---|---|
| **0.3** | Conservative | Max CIDOC CRM reuse, minimal new classes, flat hierarchies, no restrictions unless essential, strict domain/range |
| **0.5** | Balanced | Moderate new classes, some restrictions, standard CRM alignment, reification where justified |
| **0.7** | Creative | Deep class hierarchies, reification pivot classes, extensive restrictions, exploratory alignments, disjointness axioms |

### Generated deliverables

| Temperature | Classes | Object Properties | Data Properties | Cumulative lines |
|---|---|---|---|---|
| 0.3 | 6 | 6 | 2 | 104 |
| 0.5 | 14 | 14 | 5 | 222 |
| 0.7 | 24 | 21 | 8 | 263 |

Full class and property inventory in `ontologies_generated/Deepseekv4/README.md`.

### Namespace

```
arqo: <http://www.ontologyARQ.org/archaeological-object/>
```

## Step 4 — CRMarchaeo Integration

The `arqo:` module extends CRMarchaeo through class subsumption and property ranges:

**Class alignment:**
| arqo: class | Superclass | Temperature |
|---|---|---|
| `ArchaeologicalObject` | `crm:E19_Physical_Object` | 0.3+ |
| `ObjectBiography` | `crm:E5_Event` | 0.3+ |
| `ProductionEvent` | `crm:E12_Production` | 0.3+ |
| `UseEvent` | `crm:E7_Activity` | 0.3+ |
| `DepositionEvent` | `crmarchaeo:A4_Stratigraphic_Genesis` | 0.3+ |
| `RecoveryEvent` | `crmarchaeo:A1_Excavation_Process_Unit` | 0.3+ |
| `ReuseEvent` | `crm:E7_Activity` | 0.5+ |
| `RepairEvent` | `crm:E81_Transformation` | 0.5+ |
| `CirculationEvent` | `crm:E9_Move` | 0.5+ |
| `SamplingEvent` | `crmsci:S19_Encounter` | 0.5+ |
| `PostExcavationTreatment` | `crm:E7_Activity` | 0.5+ |
| `TaphonomicProcess` | `crmarchaeo:A5_Stratigraphic_Modification_Event` | 0.5+ |
| `FunctionalTransformation` | `crm:E81_Transformation` | 0.5+ |
| `ExcavationCampaign` | `crm:E7_Activity` | 0.5+ |
| `RecoveryContext` | `crm:E5_Event` | 0.7 |
| `MaterialAssignment` | `crm:E17_Type_Assignment` | 0.7 |
| `TypologicalAssignment` | `crm:E17_Type_Assignment` | 0.7 |
| `BiographyLink` | `crm:E5_Event` | 0.7 |
| `NaturalObject` | `crm:E19_Physical_Object` | 0.7 |
| `AbioticObject` | `arqo:NaturalObject` | 0.7 |
| `BioticObject` | `arqo:NaturalObject` | 0.7 |
| `Artifact` | `crm:E22_Human-Made_Object` | 0.7 |
| `Structure` | `crm:E24_Physical_Human-Made_Thing` | 0.7 |
| `ArtisticExpression` | `crm:E22_Human-Made_Object` | 0.7 |

**Property-to-CRMarchaeo alignment:**
| Property | Range |
|---|---|
| `depositedIn` | `crmarchaeo:A8_Stratigraphic_Unit` |
| `recoveredFrom` | `crmarchaeo:A8_Stratigraphic_Unit` |
| `locatedInStructure` | `crmarchaeo:A2_Stratigraphic_Volume_Unit` |

**Object properties (6 core + 8 intermediate + 7 advanced = 21 total):**
`hasMaterial`, `hasBiography`, `participatedInProduction`, `participatedInUse`, `depositedIn`, `recoveredFrom`, `participatedInReuse`, `repairedIn`, `circulatedThrough`, `wasSampledIn`, `underwentTreatment`, `underwentTaphonomicProcess`, `underwentTransformation`, `associatedWithActor`, `hasRecoveryContext`, `hasMaterialAssignment`, `hasTypologicalAssignment`, `hasBiographyLink`, `sharesBiographyWith`, `circulatedBetween`, `locatedInStructure`

**Data properties (2 core + 3 intermediate + 3 advanced = 8 total):**
`hasLocalIdentifier`, `hasConservationState`, `hasManufacturingTechnique`, `hasRawMaterialProvenance`, `hasObjectCategory`, `hasUsagePeriod`, `hasDepositionDate`, `hasRecoveryDate`

---

# How to Reproduce with Another LLM Model

Use these exact steps to generate the same deliverables with a different LLM.

## Prerequisites

1. Read `AGENTS.md` (this file) for project context, principles, and naming conventions
2. Read `docs/analisis.docx` for the CRMarchaeo gap analysis and ontology extension proposal
3. Read `docs/PreguntasCompetencia.docx` for the original CQ set
4. The LLM must be capable of generating valid OWL 2 Turtle (.ttl)

## Step 1 — Generate Competency Questions

Create `CQ/CQ_{model_name}/` with 4 subdirectories:

```
CQ/CQ_{model_name}/
├── object/competency_questions.md      # ~20 CQ, tag CQ-OBJ-01 to CQ-OBJ-20
├── spatial/competency_questions.md     # ~20 CQ, tag CQ-SPA-01 to CQ-SPA-20
├── temporal/competency_questions.md    # ~20 CQ, tag CQ-TEM-01 to CQ-TEM-20
└── stratigraphy/competency_questions.md # ~20 CQ, tag CQ-STR-01 to CQ-STR-20
```

Each file header:
```markdown
# Competency Questions — [Theme]
> **Generated by:** {model_name}
> **Date:** YYYY-MM-DD
> **Block:** [Block name]
> **Total CQs:** 20
```

Each CQ format:
```markdown
## CQ-XXX-NN
**Question:** [question text]
- **Ontology modules required:** [modules]
- **Possible ontology reuse:** [ontologies and classes]
```

CQs must cover the topics defined in the CQ Block sections above (~20 per block). Sources:
- **Reused**: translate from `docs/PreguntasCompetencia.docx`, filter out inference CQs
- **New**: derive from `docs/analisis.docx` gap analysis sections 3.1-3.6

## Step 2 — Create Prompt Templates

Create `prompts/{strategy}/prompt_archaeological_object.md` for each strategy.

Template source: [https://github.com/dersuchendee/Onto-Generation/tree/main/PromptingTechniques](https://github.com/dersuchendee/Onto-Generation/tree/main/PromptingTechniques)

### Memoryless CQbyCQ template adaptation:
- Replace `{story}` with the archaeological domain scenario (object lifecycle, materiality, biography, CRMarchaeo context)
- Replace `{CQ}` with each competency question
- Set `{rdf}` to always empty
- Add prefixes: `arqo:`, `crm:`, `crmarchaeo:`, `crmsci:`, `crmhs:`, `owl:`, `rdf:`, `rdfs:`, `xsd:`
- Add CRMarchaeo alignment rules
- Add archaeological object modeling principles

### Ontogenia template adaptation:
- Replace `{scenario}` with the archaeological domain narrative
- Replace `{CQ}` with each competency question
- Replace `{previous_output}` with the accumulated RDF from the previous step
- Include the 9-step metacognitive procedure
- Add ontology design patterns (CIDOC CRM Event, Physical Object, CRMarchaeo Stratigraphic, Reification, Observation)

## Step 3 — Generate Ontologies

Generate OWL 2 Turtle (.ttl) files under `ontologies_generated/{model_name}/`.

### Directory structure to create:

```
ontologies_generated/{model_name}/
├── memoryless/
│   ├── temp_0_3/     # 20 files: CQ-OBJ-01.ttl ... CQ-OBJ-20.ttl
│   ├── temp_0_5/     # 20 files
│   └── temp_0_7/     # 20 files
├── ontogenia/
│   ├── temp_0_3/     # step_01 to step_20 + cumulative.ttl
│   ├── temp_0_5/     # step_01 to step_20 + cumulative.ttl
│   └── temp_0_7/     # step_01 to step_20 + cumulative.ttl
└── README.md         # Documentation (see Step 4)
```

### Each .ttl file header:
```turtle
# Model: {model_name}
# Strategy: memoryless | ontogenia
# Temperature: 0.3 | 0.5 | 0.7
# CQ: OBJ-XX
# Step: XX/20  (ontogenia only)
```

### Memoryless CQbyCQ:
- Each CQ generates an independent OWL fragment
- RDF context is always empty
- Only model what is needed for that specific CQ

### Ontogenia:
- Step 1 receives an empty RDF
- Step N receives the complete RDF from step N-1
- Each step adds new classes, properties, restrictions
- The `cumulative.ttl` is the final state (all 20 CQs answered)

### Temperature guidance:
- **0.3**: Minimal new classes, maximum CIDOC CRM reuse, no restrictions unless essential
- **0.5**: Moderate extensions, some restrictions, standard CRM alignment
- **0.7**: Deep hierarchies, reification, extensive restrictions, disjointness axioms

### Required namespace:
```
arqo: <http://www.ontologyARQ.org/archaeological-object/>
```

## Step 4 — Document Results

Create `ontologies_generated/{model_name}/README.md` with:

1. **Project Inventory**: file counts per strategy and temperature
2. **CQ Attribution**: which are reused vs new, with source
3. **CRMarchaeo Integration Map**: class subsumption and property alignment tables
4. **Class Inventory**: all classes with superclass and temperature activation
5. **Property Inventory**: object and data properties with domain/range and temperature activation
6. **Temperature Comparison**: side-by-side of the same CQ at different temperatures
7. **File Index**: complete directory tree with recuentos

---

# CQ Generation — Qwen 3.6 (2026-05-21)

A second independent set of 80 CQs was generated by Qwen 3.6, stored at `CQ/CQ_qwen3.6/`. These CQs are **fully independent** from the deepseek-v4-pro set — they were generated from scratch with no reuse of previous CQs, covering the same 4 thematic blocks derived from the CRMarchaeo gap analysis in `docs/analisis.docx`.

| Block | File | CQs |
|---|---|---|
| Archaeological Object | `CQ/CQ_qwen3.6/CQ-object-qwen3.6.md` | 20 |
| Spatial | `CQ/CQ_qwen3.6/CQ-spatial-qwen3.6.md` | 20 |
| Temporal | `CQ/CQ_qwen3.6/CQ-temporal-qwen3.6.md` | 20 |
| Stratigraphy | `CQ/CQ_qwen3.6/CQ-stratigraphy-qwen3.6.md` | 20 |

This allows comparison of CQ generation approaches between LLM models. The ontology generation for these CQs follows the same process documented in the "How to Reproduce" section.

---

# CQ Generation — K2.6 (2026-05-21)

A third independent set of 80 CQs was generated by K2.6, stored at `CQ/CQ_K2.6/`. These CQs are **fully independent** from all previous sets, generated from scratch with no reuse of prior questions, covering the same 4 thematic blocks.

| Block | File | CQs |
|---|---|---|
| Archaeological Object | `CQ/CQ_K2.6/CQ-object-k2.6.md` | 20 |
| Spatial | `CQ/CQ_K2.6/CQ-spatial-k2.6.md` | 20 |
| Temporal | `CQ/CQ_K2.6/CQ-temporal-k2.6.md` | 20 |
| Stratigraphy | `CQ/CQ_K2.6/CQ-stratigraphy-k2.6.md` | 20 |

This third set provides additional material for comparing CQ diversity and coverage across different LLM architectures. The ontology generation for these CQs follows the same prompting and temperature strategy documented in the "How to Reproduce" section.

---

# Workflow Executed — K2.6

This section documents the ontology generation workflow executed by K2.6 on 2026-05-21, using the same prompting strategies and temperature settings as deepseek-v4-pro but with an independent object-centric design approach.

## Step 1 — Competency Question Generation

80 CQs were generated across 4 thematic blocks (20 each). **All 80 CQs are new** — none were reused from `PreguntasCompetencia.docx` or from previous LLM sets.

| Block | File | CQs | Source |
|---|---|---|---|
| Archaeological Object | `CQ/CQ_K2.6/CQ-object-k2.6.md` | 20 | New — object taxonomy, partonomy, physical attributes |
| Spatial | `CQ/CQ_K2.6/CQ-spatial-k2.6.md` | 20 | New — distances, orientation, geomorphology, viewshed |
| Temporal | `CQ/CQ_K2.6/CQ-temporal-k2.6.md` | 20 | New — intervals, cross-dating, dendrochronology, Bayesian |
| Stratigraphy | `CQ/CQ_K2.6/CQ-stratigraphy-k2.6.md` | 20 | New — sequences, contacts, Munsell, negative features, paleosols |

## Step 2 — Ontology Generation

The Archaeological Object module was generated using both strategies at 3 temperatures with an **object-centric** design philosophy.

### Directory structure

```
ontologies_generated/K2.6/
├── memoryless/
│   ├── temp_0_3/          # 20 .ttl files (one per CQ)
│   ├── temp_0_5/          # 20 .ttl files
│   └── temp_0_7/          # 20 .ttl files
├── ontogenia/
│   ├── temp_0_3/          # 20 step files + cumulative.ttl
│   ├── temp_0_5/          # 20 step files + cumulative.ttl
│   └── temp_0_7/          # 20 step files + cumulative.ttl
└── README.md              # Module documentation
```

### File counts

| Category | Files |
|---|---|
| Memoryless CQbyCQ .ttl | 60 |
| Ontogenia step .ttl | 60 |
| Ontogenia cumulative .ttl | 3 |
| Prompt templates | 2 (reused) |
| CQ files | 4 |
| Documentation | 1 |
| **Total** | **126** |

### Generated deliverables

| Temperature | Classes | Object Properties | Data Properties | Cumulative lines |
|---|---|---|---|---|
| 0.3 | 5 | 3 | 4 | 92 |
| 0.5 | 17 | 11 | 7 | 206 |
| 0.7 | 28 | 18 | 7 | 277 |

### Key design differences from Deepseekv4

| Aspect | Deepseekv4 | K2.6 |
|---|---|---|
| **Philosophy** | Event-centric | Object-centric |
| **Core entities** | Events (Production, Use, Deposition, Recovery) | Objects (NaturalObject, HumanMadeObject, Artefact, Structure) |
| **Hierarchy depth** | 1-2 levels | 3 levels |
| **Reification** | 4 pivot classes | 2 partonomy properties |
| **Physical attributes** | Minimal | Extensive (morphometry, weight, completeness, Munsell color) |
| **Disjointness axioms** | None | NaturalObject disjointWith HumanMadeObject; AbioticObject disjointWith BioticObject |

Full class and property inventory in `ontologies_generated/K2.6/README.md`.

## Step 3 — CRMarchaeo Integration

The K2.6 module extends CRMarchaeo through class subsumption and property ranges:

**Class alignment (selected):**
| arqo: class | Superclass | Temperature |
|---|---|---|
| `ArchaeologicalObject` | `crm:E19_Physical_Object` | 0.3 |
| `NaturalObject` | `arqo:ArchaeologicalObject` | 0.3 |
| `HumanMadeObject` | `arqo:ArchaeologicalObject` | 0.3 |
| `AbioticObject` | `arqo:NaturalObject` | 0.5 |
| `BioticObject` | `arqo:NaturalObject` | 0.5 |
| `Artefact` | `arqo:HumanMadeObject` | 0.3 |
| `Structure` | `arqo:HumanMadeObject` | 0.5 |
| `ArtisticExpression` | `arqo:HumanMadeObject` | 0.5 |
| `StratigraphicSequence` | `crmarchaeo:A8_Stratigraphic_Unit` | 0.3 |
| `StratigraphicContact` | `crmarchaeo:A3_Stratigraphic_Interface` | 0.5 |
| `NegativeFeature` | `crm:E25_Man-Made_Feature` | 0.5 |
| `Paleosol` | `crmarchaeo:A8_Stratigraphic_Unit` | 0.7 |
| `ConstructionElement` | `crm:E24_Physical_Human-Made_Thing` | 0.7 |

**Property-to-CRMarchaeo alignment:**
| Property | Range |
|---|---|
| `hasStratigraphicContact` | `crmarchaeo:A3_Stratigraphic_Interface` |
| `hasNegativeFeature` | `crm:E25_Man-Made_Feature` |
| `containsPaleosol` | `crmarchaeo:A8_Stratigraphic_Unit` |
| `hasConstructionElement` | `crm:E24_Physical_Human-Made_Thing` |

---

# Updated Directory Structure

```
ONTOLOGIA-ARQ/
├── AGENTS.md                          # This file
├── .gitignore
├── ontologyARQ/                       # GitHub repository root
│   ├── README.md
│   └── LICENSE
├── CQ/
│   ├── CQ_Deepseekv4Pro/              # CQs generated by deepseek-v4-pro
│   │   ├── CQ-object-deepseek.md
│   │   ├── CQ-spatial-deepseek.md
│   │   ├── CQ-temporal-deepseek.md
│   │   └── CQ-stratigraphy-deepseek.md
│   ├── CQ_qwen3.6/                    # CQs generated by Qwen 3.6 (independent set)
│   │   ├── CQ-object-qwen3.6.md
│   │   ├── CQ-spatial-qwen3.6.md
│   │   ├── CQ-temporal-qwen3.6.md
│   │   └── CQ-stratigraphy-qwen3.6.md
│   ├── CQ_K2.6/                       # CQs generated by K2.6 (independent set)
│   │   ├── CQ-object-k2.6.md
│   │   ├── CQ-spatial-k2.6.md
│   │   ├── CQ-temporal-k2.6.md
│   │   └── CQ-stratigraphy-k2.6.md
│   └── {model_name}/                  # CQs from other LLMs (future)
├── prompts/
│   ├── memoryless/
│   │   └── prompt_archaeological_object.md
│   └── ontogenia/
│       └── prompt_archaeological_object.md
├── ontologies_generated/
│   ├── README.md                      # Master index: all modules + comparison
│   ├── Deepseekv4/                    # Ontologies from deepseek-v4-pro
│   │   ├── memoryless/temp_0_{3,5,7}/
│   │   ├── ontogenia/temp_0_{3,5,7}/
│   │   └── ...
│   ├── K2.6/                          # Ontologies from K2.6
│   │   ├── memoryless/temp_0_{3,5,7}/
│   │   ├── ontogenia/temp_0_{3,5,7}/
│   │   └── README.md
│   └── {model_name}/                  # Ontologies from other LLMs (future)
├── docs/
│   ├── analisis.docx                  # CRMarchaeo gap analysis
│   ├── PreguntasCompetencia.docx       # Original CQ set
│   ├── ontologyLLM.pdf                # OntologyLLM research paper
│   └── modelo idearq_v3b.pdf          # IDEArq UML model
├── ontologies_docs/                   # Reference ontologies (renamed from ONTOLOGIAS)
│   ├── owl/                           # CRMarchaeo v2.1.1
│   ├── ttl/                           # GeoSPARQL, OWL-Time
│   ├── html/
│   └── pdfs/
├── evaluation/                        # Evaluation framework (future)
└── generated_ontologies/              # (legacy)
```

---

# Workflow Executed — Kimi-2.6

This section documents the ontology generation workflow executed by Kimi-2.6 on 2026-05-26, using the same prompting strategies and temperature settings as previous LLMs but with an independent event-centric design approach and 30 new competency questions.

## Step 1 — Competency Question Generation

30 CQs were generated across 6 thematic blocks (5 each). **All 30 CQs are new** — none were reused from `PreguntasCompetencia.docx` or from previous LLM sets. The CQs were designed from scratch with an **event-centric** grammatical structure (the event is the subject of each question).

| Block | Theme | CQs | Source Articles |
|---|---|---|---|
| 1 | Production and manufacturing events | 5 | Garcia-Rovira, Guerra, Pernicka et al. |
| 2 | Use, reuse, and functional transformation events | 5 | BF03376602, Gosden, ICCROM, "Things in the Eye of the Beholder" |
| 3 | Circulation, exchange, and provenance events | 5 | Gill, Guerra, Pernicka et al. |
| 4 | Deposition and post-depositional events | 5 | BF03376602, Holtorf, ICCROM |
| 5 | Scientific analysis and dating events | 5 | Guerra, Schwarcz, "Non-invasive studies", "2949238" |
| 6 | Conservation, interpretation, and meaning events | 5 | ICCROM, Holtorf, Rowe, Pollard |

File: `CQ/CQ_Kimi2.6_objeto/CQ-object-kimi2.6.md`

## Step 2 — Ontology Generation

The Archaeological Object module was generated using both strategies at 3 temperatures with an **event-centric** design philosophy.

### Directory structure

```
ontologies_generated/Kimi2.6_objeto/
├── memoryless/
│   ├── temp_0_3/          # 30 .ttl files (one per CQ)
│   ├── temp_0_5/          # 30 .ttl files
│   └── temp_0_7/          # 30 .ttl files
├── ontogenia/
│   ├── temp_0_3/          # 30 step files + cumulative.ttl
│   ├── temp_0_5/          # 30 step files + cumulative.ttl
│   └── temp_0_7/          # 30 step files + cumulative.ttl
└── README.md              # Module documentation
```

### File counts

| Category | Files |
|---|---|
| Memoryless CQbyCQ .ttl | 90 |
| Ontogenia step .ttl | 90 |
| Ontogenia cumulative .ttl | 3 |
| Prompt templates | 2 (reused) |
| CQ files | 1 |
| Documentation | 1 |
| **Total** | **187** |

### Generated deliverables

| Temperature | Classes | Object Properties | Data Properties | Cumulative lines |
|---|---|---|---|---|
| 0.3 | 32 | 52 | 39 | 634 |
| 0.5 | 56 | 67 | 41 | 818 |
| 0.7 | 121 | 73 | 54 | 1269 |

### Key design characteristics

| Aspect | Kimi-2.6 Event-centric |
|---|---|
| **Core entities** | Events (ManufacturingEvent, UseEvent, CirculationEvent, DepositionEvent, etc.) |
| **Object role** | Participant in events, not primary anchor |
| **Hierarchy depth** | 1 level (0.3) → 2 levels (0.5) → 3-4 levels (0.7) |
| **Disjointness axioms** | 0 (0.3) → 2-4 per file (0.5) → 4-8 per file (0.7) |
| **Reification** | Minimal (0.3) → Moderate (0.5) → Extensive (0.7) |
| **Cultural concepts** | PastnessEvent, ObjectAgencyEvent, CulturalSignificanceAssignmentEvent |

## Step 3 — CRMarchaeo Integration

The Kimi-2.6 module extends CRMarchaeo through class subsumption:

**Class alignment (selected):**
| arqo: class | Superclass | Temperature |
|---|---|---|
| `ManufacturingEvent` | `crm:E12_Production` | 0.3+ |
| `UseEvent` | `crm:E7_Activity` | 0.3+ |
| `DepositionEvent` | `crmarchaeo:A4_Stratigraphic_Genesis` | 0.3+ |
| `RecoveryEvent` | `crmarchaeo:A1_Excavation_Process_Unit` | 0.3+ |
| `PostDepositionalAlterationEvent` | `crmarchaeo:A5_Stratigraphic_Modification_Event` | 0.3+ |
| `AnalyticalEncounterEvent` | `crmsci:S19_Encounter` | 0.3+ |
| `ObjectBiographyEvent` | `crminf:I4_Proposition_Set` | 0.5+ |
| `PastnessEvent` | `crminf:I4_Proposition_Set` | 0.5+ |
| `TypologicalAssignmentEvent` | `crm:E17_Type_Assignment` | 0.3+ |
| `RepatriationEvent` | `crm:E9_Move` | 0.5+ |

Full inventory in `ontologies_generated/Kimi2.6_objeto/README.md`.
