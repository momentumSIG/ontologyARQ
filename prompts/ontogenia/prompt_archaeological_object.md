# Ontogenia Prompt — Archaeological Object Ontology

> Adapted from [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) (Lippolis et al., ESWC 2025)
> Metacognitive prompting technique for iterative ontology extension

## Usage

This prompt is used for the **Ontogenia** strategy. Each competency question is processed iteratively with the LLM receiving the accumulated RDF from all previous steps. The metacognitive procedure guides the LLM through a structured 9-step ontology design process.

### Variables

| Variable | Description |
|---|---|
| `{scenario}` | Archaeological domain narrative |
| `{CQ}` | The current competency question to model |
| `{procedure}` | The 9-step metacognitive procedure (see `procedure.md`) |
| `{previous_output}` | Accumulated RDF from all previous CQ steps (empty for step 1) |
| `{patterns_json}` | Ontology Design Patterns in Turtle format (see below) |
| `{ontology_elements}` | "Classes, Object Properties, Datatype Properties. Object properties need domain and range. All need rdfs:label and rdfs:comment. Add restrictions where justified. Prefer CIDOC CRM alignment. Reify assignments (E17_Type_Assignment pattern) and observations (S4_Observation pattern)."

### Temperature guidance

| Temperature | Style | Effect |
|---|---|---|
| **0.3** | Conservative | Max CIDOC CRM reuse, minimal new classes, flat hierarchies, no restrictions unless essential, strict domain/range, no disjointness |
| **0.5** | Balanced | Moderate new classes, some restrictions, standard CRM alignment, reification where justified, hierarchical classes appear |
| **0.7** | Creative | Deep class hierarchies (3 levels), reification pivot classes, extensive restrictions, exploratory alignments, disjointness axioms, full lifecycle event chain |

### Procedure File

Load `prompts/ontogenia/procedure.md` and pass its content as the `{procedure}` variable.

---

## Prompt Template

```
Following the previous output: '{previous_output}'

Read the following instructions: '{procedure}'

Based on the scenario: '{scenario}', design an ontology module that comprehensively answers the following competency question:

'{CQ}'

You can use the following ontology design patterns in OWL format:

{patterns_json}

Remember what are the ontology elements: {ontology_elements}

When you're done send me only the whole ontology you've designed in Turtle (.ttl) format, do not comment.

Your output MUST include the accumulated ontology from previous steps PLUS any new classes, properties, and restrictions needed to answer this competency question. Do not remove or duplicate previous content.

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

## Output Format

```turtle
# ============================================================
# Ontology: Archaeological Object Module
# Strategy: ontogenia | Step: {step_number}/{total_steps}
# CQ: {CQ_id}
# ============================================================

# ======================= CLASSES ===========================
[class definitions]

# =================== OBJECT PROPERTIES =====================
[object property definitions]

# ==================== DATA PROPERTIES =====================
[data property definitions]

# ===================== RESTRICTIONS =======================
[restriction axioms]
```
```
```

## Ontology Design Patterns (ODPs)

These patterns are passed as `{patterns_json}`. They provide concrete OWL Turtle examples of CIDOC CRM-aligned modeling patterns.

### Pattern 1: CRM Event Pattern

Models an event that occurred at a specific time and place, involving actors and physical objects.

```turtle
# Event class aligned with CIDOC CRM
arqo:ManufacturingEvent a owl:Class ;
    rdfs:subClassOf crm:E12_Production ;
    rdfs:label "ManufacturingEvent"@en ;
    rdfs:comment "Event of object production through specific technological procedures"@en .

# Object participation in event
arqo:wasProducedBy a owl:ObjectProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range arqo:ManufacturingEvent ;
    rdfs:label "wasProducedBy"@en ;
    rdfs:comment "Links an object to the manufacturing event that produced it"@en .

# Temporal qualification of event
arqo:hasManufacturingDateStart a owl:DatatypeProperty ;
    rdfs:domain arqo:ManufacturingEvent ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasManufacturingDateStart"@en .

# Actor participation in event
arqo:associatedWithActor a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "associatedWithActor"@en ;
    rdfs:comment "Links object to social actor, cultural group, or craft tradition"@en .
```

### Pattern 2: CRMarchaeo Stratigraphic Pattern

Models the stratigraphic context and deposition/recovery of archaeological objects.

```turtle
# Stratigraphic context aligned with CRMarchaeo
arqo:StratigraphicContext a owl:Class ;
    rdfs:subClassOf crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "StratigraphicContext"@en ;
    rdfs:comment "Stratigraphic unit providing context for archaeological finds"@en .

# Deposition event aligned with CRMarchaeo
arqo:DepositionEvent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis ;
    rdfs:label "DepositionEvent"@en ;
    rdfs:comment "Event of object entering the archaeological record"@en .

# Object to context relationship
arqo:excavatedFrom a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "excavatedFrom"@en ;
    rdfs:comment "Links object to stratigraphic unit from which it was excavated"@en .
```

### Pattern 3: E17 Type Assignment (Reification) Pattern

Models classifications as reified assignments rather than intrinsic properties. Foundational archaeological pattern.

```turtle
# Typological assignment as reified class
arqo:TypologicalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "TypologicalAssignment"@en ;
    rdfs:comment "Researcher assignment of object to typological category"@en .

# Object links to assignment
arqo:classifiedUnder a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TypologicalAssignment ;
    rdfs:label "classifiedUnder"@en .

# Assignment links to type vocabulary
arqo:assignedToType a owl:ObjectProperty ;
    rdfs:domain arqo:TypologicalAssignment ;
    rdfs:range crm:E55_Type ;
    rdfs:label "assignedToType"@en .

arqo:MaterialAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "MaterialAssignment"@en ;
    rdfs:comment "Researcher assertion about object material composition"@en .

arqo:ChronologicalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "ChronologicalAssignment"@en ;
    rdfs:comment "Researcher assignment of object to temporal period"@en .
```

### Pattern 4: S4 Observation (Scientific Analysis) Pattern

Models scientific observations and measurements as distinct from interpretations.

```turtle
# Analytical encounter aligned with CRMsci
arqo:AnalyticalEncounter a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "AnalyticalEncounter"@en ;
    rdfs:comment "Scientific analysis event where object properties are measured"@en .

# Object participates in analysis
arqo:wasSampledIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalyticalEncounter ;
    rdfs:label "wasSampledIn"@en .

# Analysis technique
arqo:hasAnalyticalTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalyticalEncounter ;
    rdfs:range xsd:string ;
    rdfs:label "hasAnalyticalTechnique"@en ;
    rdfs:comment "Scientific technique employed (XRF, ICP-MS, SEM-EDS, etc.)"@en .

# Conservation treatment
arqo:ConservationTreatment a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ConservationTreatment"@en ;
    rdfs:comment "Post-recovery preservation action applied to archaeological object"@en .

arqo:underwentTreatment a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConservationTreatment ;
    rdfs:label "underwentTreatment"@en .
```

### Pattern 5: PROV-O Provenance Chain Pattern

Models the forensic reconstruction of object provenance and movement.

```turtle
# Provenance chain as reconstructed trajectory
arqo:ProvenanceChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ProvenanceChain"@en ;
    rdfs:comment "Forensically reconstructed path from source to findspot"@en .

# Circulation event
arqo:CirculationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CirculationEvent"@en ;
    rdfs:comment "Event of object moving between locations or cultural zones"@en .

arqo:circulatedThrough a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CirculationEvent ;
    rdfs:label "circulatedThrough"@en .

# Raw material source
arqo:RawMaterialSource a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "RawMaterialSource"@en ;
    rdfs:comment "Geological or geographic source of raw materials"@en .

arqo:derivesFromSource a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RawMaterialSource ;
    rdfs:label "derivesFromSource"@en .

# Provenance region
arqo:ProvenanceRegion a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "ProvenanceRegion"@en ;
    rdfs:comment "Geographic origin region of object or materials"@en .

arqo:hasProvenance a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ProvenanceRegion ;
    rdfs:label "hasProvenance"@en .
```

### Pattern 6: Lifecycle Phase Pattern

Models sequential lifecycle phases of archaeological objects.

```turtle
# Object biography as event container
arqo:ObjectBiography a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ObjectBiography"@en ;
    rdfs:comment "Narrative sequence of events constituting object lifecycle"@en .

arqo:hasBiography a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ObjectBiography ;
    rdfs:label "hasBiography"@en .

# Lifecycle phases as CRM-aligned events
arqo:UseEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "UseEvent"@en ;
    rdfs:comment "Event of object utilization in its functional role"@en .

arqo:ReuseEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ReuseEvent"@en ;
    rdfs:comment "Secondary use after original function ceased"@en .

arqo:RepairEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "RepairEvent"@en ;
    rdfs:comment "Physical modification to restore function"@en .
```

### Pattern 7: Object Classification Hierarchy Pattern

Models the archaeological object taxonomy inspired by IDEArq.

```turtle
# Root archaeological object class
arqo:ArchaeologicalObject a owl:Class ;
    rdfs:subClassOf crm:E19_Physical_Object ;
    rdfs:label "ArchaeologicalObject"@en ;
    rdfs:comment "Physical object recovered during archaeological investigation"@en .

# Natural vs Human-made distinction
arqo:NaturalObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "NaturalObject"@en ;
    rdfs:comment "Object of natural origin found in archaeological context"@en .

arqo:HumanMadeObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "HumanMadeObject"@en ;
    rdfs:comment "Object created or modified by human action"@en .

# Natural object subtypes
arqo:AbioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "AbioticObject"@en ;
    rdfs:comment "Non-living natural object (stone, mineral, sediment)"@en .

arqo:BioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "BioticObject"@en ;
    rdfs:comment "Living or once-living natural object (bone, shell, plant remains)"@en .

# Human-made object subtypes
arqo:Artefact a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Artefact"@en ;
    rdfs:comment "Portable human-made object with functional purpose"@en .

arqo:Structure a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Structure"@en ;
    rdfs:comment "Non-portable human-made construction"@en .

arqo:ArtisticExpression a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "ArtisticExpression"@en ;
    rdfs:comment "Human-made object with aesthetic or symbolic function"@en .
```

## Archaeological Domain Scenario

This is the `{scenario}` passed to the prompt. It provides the unified archaeological narrative.

---

You are an archaeological ontologist designing an OWL 2 ontology extension for archaeological objects and finds. The ontology must be fully compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1.

### Domain Context

Archaeological objects are physical entities recovered through systematic excavation. They are studied to understand past human behavior, technology, culture, and environment. Unlike museum objects, archaeological objects carry contextual information from their depositional context — the stratigraphic unit, the associated finds, the spatial coordinates, and the temporal horizon.

### Object Classification

An archaeological expert has established that physical objects can be divided into natural objects (abiotic and biotic) and human-made objects (artefacts, structures, and artistic expressions).

Natural objects include:
- **Abiotic objects:** Stone tools (when unmodified by humans beyond use), mineral samples, sediment blocks, geological specimens
- **Biotic objects:** Animal bone, shell, wood, seeds, pollen, human remains, textile fibers

Human-made objects include:
- **Artefacts:** Portable objects with functional purpose — pottery vessels, metal tools, stone blades, glass beads, coins, figurines
- **Structures:** Non-portable constructions — walls, floors, hearths, kilns, tombs, buildings
- **Artistic expressions:** Objects whose primary value is aesthetic or symbolic — decorated ceramics, sculpture, rock art panels, ritual objects

### Object Lifecycle

Every archaeological object has a lifecycle that spans from raw material extraction through manufacturing, use, possible reuse/repair, circulation between places and cultures, eventual discard or deposition, post-depositional alteration, archaeological recovery, conservation treatment, laboratory analysis, and museum curation. Some objects may also be repatriated to their country or community of origin.

Key lifecycle principles:
1. The manufacturing date of an object TYPE is NOT the same as the use date of a specific object INSTANCE. Ceramics can remain in household use for 15+ years after their type ceased production.
2. Object biography is a narrative construct told from a human perspective. The physical events (lifecycle) are distinct from the stories told about them (biography).
3. Objects undergo transformation throughout their lifecycle — fragmentation, repair, patination, corrosion, functional change.

### Scientific Analysis

Archaeological objects are studied through:
- **Material characterization:** XRF, ICP-MS, SEM-EDS, XRD, Raman spectroscopy
- **Chronometric dating:** Radiocarbon (14C), U-series, K-Ar, Ar-Ar, TL, OSL
- **Provenance determination:** Lead isotope ratios, trace element analysis, petrography
- **Use-wear analysis:** Microscopic examination of surface traces
- **Conservation science:** Non-invasive and micro-destructive analysis to guide preservation

### Critical Ontological Distinctions

1. **Classification is an assignment, not an intrinsic property.** Material, typology, chronology, and function are determined by researchers based on evidence. Always model classifications through `crm:E17_Type_Assignment` pivot classes.

2. **Observation is separate from interpretation.** Scientific measurements (`crmsci:S4_Observation`) are distinct from the conclusions drawn from them. Multiple competing interpretations may exist for the same evidence.

3. **Pastness is not chronological age.** The perceived quality of being old (`Pastness`) is culturally constructed and distinct from measured chronological age (`crm:E52_Time-Span`).

4. **Manufacturing range ≠ Use range.** An object type's production period is systematically different from a specific object's use period. Always separate these temporally.

5. **Provenance is reconstructed forensically.** The path from raw material source to findspot is determined backwards from analytical evidence — it is not a directly observed sequence.

### Competency Question Blocks

The ontology must answer CQs from four thematic blocks:
1. **Archaeological Object:** Object biography, materiality, typology, function, reuse, manufacturing, conservation, laboratory analysis
2. **Spatial:** Excavation context, GIS integration, geometry, landscape, territory, spatial uncertainty
3. **Temporal:** Chronology, dating methods, archaeological/geological periods, temporal uncertainty
4. **Stratigraphy:** Stratigraphic units, depositional processes, Harris Matrix, formation processes, geoarchaeology

### Compatibility Requirements

- Must use CIDOC CRM classes as superclasses whenever possible
- Must align with CRMarchaeo for all stratigraphic concepts
- Must use CRMsci for observation and measurement
- Must support SPARQL querying
- Must be reasoner-compatible
- All classes and properties must have rdfs:label and rdfs:comment
```
