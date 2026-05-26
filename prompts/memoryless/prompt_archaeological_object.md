# Memoryless CQbyCQ Prompt — Archaeological Object Ontology

> Adapted from [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) (Lippolis et al., ESWC 2025)

## Usage

This prompt is used for the **Memoryless CQbyCQ** strategy. Each competency question is processed independently with an empty RDF context. No ontology memory is carried across CQs.

### Variables

| Variable | Description |
|---|---|
| `{story}` | Archaeological domain narrative (see below) |
| `{CQ}` | The current competency question to model |

### Temperature guidance

| Temperature | Style | Effect |
|---|---|---|
| **0.3** | Conservative | Max CIDOC CRM reuse, minimal new classes, flat hierarchies, no restrictions unless essential |
| **0.5** | Balanced | Moderate new classes, some restrictions, standard CRM alignment, reification where justified |
| **0.7** | Creative | Deep class hierarchies, reification pivot classes, extensive restrictions, disjointness axioms |

---

## Prompt Template

```
Your task is to contribute to creating a well-structured ontology for the archaeological domain by reading information from the given story, requirements, and restrictions. The ontology must be compatible with CIDOC CRM v7.3.2, CRMarchaeo v2.1.1, and the broader CIDOC CRM family (CRMsci, CRMinf, CRMhs).

You are working on this competency question: "{CQ}"

Read the given Turtle RDF (which is the current ontology state — it is empty at the beginning). Then produce the OWL ontology fragment that answers this competency question. Your output should be valid OWL 2 Turtle (.ttl) format. Solve only this question — do not address future questions.

## Namespace Prefixes

You MUST use these exact prefixes in every output:

```turtle
@prefix arqo: <http://www.ontologyARQ.org/archaeological-object/> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix crmarchaeo: <http://www.cidoc-crm.org/crmarchaeo/> .
@prefix crmsci: <http://www.cidoc-crm.org/crmsci/> .
@prefix crminf: <http://www.cidoc-crm.org/crminf/> .
@prefix crmhs: <http://www.cidoc-crm.org/crmhs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
```

## Ontology Design Principles

### 1. CIDOC CRM Alignment

Before creating any new class or property, ALWAYS check if CIDOC CRM or CRMarchaeo already provides it:

- **Physical objects:** `crm:E19_Physical_Object`
- **Human-made objects:** `crm:E22_Human-Made_Object`
- **Structures:** `crm:E24_Physical_Human-Made_Thing`
- **Events/Activities:** `crm:E5_Event`, `crm:E7_Activity`, `crm:E12_Production`
- **Transformations:** `crm:E81_Transformation`
- **Movement:** `crm:E9_Move`
- **Materials:** `crm:E57_Material`
- **Places:** `crm:E53_Place`
- **Time-spans:** `crm:E52_Time-Span`
- **Actors:** `crm:E39_Actor`
- **Types:** `crm:E55_Type`
- **Classifications:** `crm:E17_Type_Assignment`
- **Dimensions:** `crm:E54_Dimension`
- **Condition states:** `crm:E3_Condition_State`
- **Stratigraphic units:** `crmarchaeo:A8_Stratigraphic_Unit`
- **Stratigraphic genesis:** `crmarchaeo:A4_Stratigraphic_Genesis`
- **Excavation process:** `crmarchaeo:A1_Excavation_Process_Unit`
- **Stratigraphic modification:** `crmarchaeo:A5_Stratigraphic_Modification_Event`
- **Stratigraphic interface:** `crmarchaeo:A3_Stratigraphic_Interface`
- **Scientific observation:** `crmsci:S4_Observation`
- **Measurement:** `crmsci:S21_Measurement`
- **Sample:** `crmsci:S18_Sample`
- **Encounter:** `crmsci:S19_Encounter`

New classes should extend these CRM classes using `rdfs:subClassOf` whenever possible.

### 2. Class Naming

- Custom archaeological classes use the `arqo:` prefix
- Class names are CamelCase (e.g., `arqo:ArchaeologicalObject`)
- Do NOT use `Cl_` prefix — that convention does not apply
- Every class MUST have `rdfs:label` and `rdfs:comment`

### 3. Property Modeling

**Object properties** connect two classes. Always specify `rdfs:domain` and `rdfs:range`. Use `rdfs:label` and `rdfs:comment`.

**Data properties** connect a class to an xsd datatype. Common datatypes:
- `xsd:string`, `xsd:integer`, `xsd:decimal`, `xsd:dateTime`, `xsd:date`, `xsd:time`, `xsd:boolean`, `xsd:duration`

### 4. Reification (Pivot Classes)

When a relationship involves more than two entities or a combination of entity + datatype + entity, use a **pivot class** (reification). The pivot class acts as an intermediary.

**Archaeological reification patterns:**

**Pattern A — Type Assignment:** When assigning a classification (material, type, function, period) to an object, do NOT use a direct property. Instead, create a pivot class extending `crm:E17_Type_Assignment`:

```turtle
arqo:TypologicalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "TypologicalAssignment"@en .

arqo:classifiedUnder a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TypologicalAssignment ;
    rdfs:label "classifiedUnder"@en .
```

**Pattern B — Observation:** When recording a scientific observation or measurement with metadata (technique, date, observer), create a pivot class:

```turtle
arqo:AnalyticalEncounter a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "AnalyticalEncounter"@en .

arqo:wasSampledIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalyticalEncounter ;
    rdfs:label "wasSampledIn"@en .
```

**Pattern C — Event Qualification:** When an object participates in an event that needs contextualization (when, where, by whom), use a pivot event class:

```turtle
arqo:ManufacturingEvent a owl:Class ;
    rdfs:subClassOf crm:E12_Production ;
    rdfs:label "ManufacturingEvent"@en .

arqo:wasProducedBy a owl:ObjectProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range arqo:ManufacturingEvent ;
    rdfs:label "wasProducedBy"@en .
```

### 5. Restrictions

Apply OWL restrictions where archaeologically meaningful:
- `owl:allValuesFrom` — property value must belong to a class
- `owl:someValuesFrom` — property must have at least one value from a class
- `owl:cardinality`, `owl:minCardinality`, `owl:maxCardinality` — count constraints

### 6. Object Classification Hierarchy

The archaeological object taxonomy follows this IDEArq-inspired pattern:

```
crm:E19_Physical_Object
└── arqo:ArchaeologicalObject
    ├── arqo:NaturalObject
    │   ├── arqo:AbioticObject  (stone, mineral, sediment)
    │   └── arqo:BioticObject   (bone, shell, wood, plant remains)
    └── arqo:HumanMadeObject
        ├── arqo:Artefact             (portable functional object)
        ├── arqo:Structure            (non-portable construction)
        └── arqo:ArtisticExpression   (aesthetic/symbolic object)
```

### 7. Lifecycle Events

Objects pass through lifecycle phases modeled as CRM-aligned events:

| Phase | Event class | CRM superclass |
|---|---|---|
| Manufacturing | `arqo:ManufacturingEvent` | `crm:E12_Production` |
| Use | `arqo:UseEvent` | `crm:E7_Activity` |
| Reuse | `arqo:ReuseEvent` | `crm:E7_Activity` |
| Repair | `arqo:RepairEvent` | `crm:E81_Transformation` |
| Circulation | `arqo:CirculationEvent` | `crm:E9_Move` |
| Deposition | `arqo:DepositionEvent` | `crmarchaeo:A4_Stratigraphic_Genesis` |
| Recovery | `arqo:RecoveryEvent` | `crmarchaeo:A1_Excavation_Process_Unit` |
| Conservation | `arqo:ConservationTreatment` | `crm:E7_Activity` |
| Sampling | `arqo:SamplingEvent` | `crmsci:S19_Encounter` |

### 8. Critical Distinctions

**Manufacturing date ≠ Use date:** The manufacturing date range of an object TYPE is not the same as the use date range of a specific object INSTANCE. An object can remain in use decades after its type ceased production. Always distinguish:
- `hasManufacturingDateStart` / `hasManufacturingDateEnd` on `ManufacturingEvent`
- `hasUseDateStart` / `hasUseDateEnd` on `UseEvent`

**Assignment vs Intrinsic Property:** Material, typology, chronology, and function are NOT intrinsic properties of objects — they are assignments made by researchers. Always model these through `crm:E17_Type_Assignment` pivot classes, not as direct data properties.

**Observation vs Interpretation:** Distinguish between measured observations and interpretative claims. Use `crmsci:S4_Observation` for what was observed/measured and `crminf:I4_Proposition_Set` or `crm:E17_Type_Assignment` for what was concluded.

## Common Mistakes to Avoid

### Class Extraction Mistakes
1. Not extracting all classes — read the CQ and story carefully for implicit classes
2. Creating classes for concepts that are data properties (e.g., "Date", "Weight" are data properties, not classes)
3. Extracting individuals (specific people/objects) as classes
4. Not anchoring new classes in the CRM hierarchy with rdfs:subClassOf

### Hierarchy Mistakes
1. Creating artificial deep hierarchies without semantic justification
2. Not aligning with CRM/CRMarchaeo class hierarchy
3. Creating classes already defined in CRM (e.g., don't create "Material" when `crm:E57_Material` exists)

### Property Mistakes
1. Using direct data properties where a reified assignment is needed (e.g., don't use `hasType: xsd:string` — create `TypologicalAssignment` extending `crm:E17_Type_Assignment`)
2. Not specifying domain and range for every object property
3. Creating object properties whose domain/range don't match their semantics

### Reification Mistakes
1. The pivot class connects to related classes by object properties, NOT by rdfs:subClassOf
2. Forgetting to create the pivot class before referencing it in properties
3. Direction of relations: from the primary entity TO the pivot class

### Archaeological Domain-Specific Mistakes
1. Conflating manufacturing date range (of the type) with use date range (of the instance)
2. Treating typological classification as an intrinsic property instead of as an assignment
3. Modeling provenance as a simple location property instead of as a forensic reconstruction chain
4. Forgetting that archaeological objects are predominantly recovered as fragments — model fragmentation explicitly
5. Not distinguishing between conservation treatment (post-recovery) and repair (pre-depositional)

## Output Format

Before writing OWL code, state whether the CQ is answerable by the previous RDF (it is always NOT answerable in Memoryless mode since RDF is empty).

Then produce the output as:

```turtle
# ============================================================
# Ontology: Archaeological Object Module
# Strategy: memoryless | CQ: {CQ_id}
# ============================================================

# ======================= CLASSES ===========================
[class definitions in Turtle]

# =================== OBJECT PROPERTIES =====================
[object property definitions in Turtle]

# ==================== DATA PROPERTIES =====================
[data property definitions in Turtle]

# ===================== RESTRICTIONS =======================
[restriction axioms in Turtle]
```

The output MUST be valid OWL 2 Turtle syntax. Do not include markdown code fences inside the output. Do not include explanatory comments besides the section headers.

## Archaeological Domain Story

Here is the archaeological domain context for this ontology:

---

{story}

---

## Current RDF

{rdf}
```
