# Memoryless CQbyCQ — Archaeological Object Module Prompt

Adapted from [Onto-Generation PromptingTechniques](https://github.com/dersuchendee/Onto-Generation/blob/main/PromptingTechniques/README.md).

---

## Template

```text
Your task is to contribute to creating a piece of well-structured ontology for the archaeological domain by reading information that appeared in the given scenario, requirements, and restrictions.

The way you approach this is: pick this competency question "{CQ}" and read the given Turtle RDF to know what is the current ontology till this stage (it will always be EMPTY for this strategy since we process each CQ independently — Memoryless CQbyCQ). Then you add the RDF so it can answer this competency question. Your output at each stage must be a complete, valid OWL 2 Turtle (.ttl) ontology fragment. Do NOT repeat previous content since there is none.

You are designing an ontology module for archaeological objects that extends CIDOC CRM and CRMarchaeo. The ontology must be semantically compatible with:
- CIDOC CRM v7.3.2
- CRMarchaeo v2.1.1
- CRMsci v3.1
- CRMhs v1.2

## Ontology Elements
You need to model:
1. **Classes** — Using PascalCase with prefix arqo: for new classes. New classes should be subclasses of existing CIDOC CRM / CRMarchaeo classes whenever possible. Do NOT invent CIDOC CRM concepts.
2. **Object Properties** — Using camelCase with prefix arqo:. Must have rdfs:domain and rdfs:range. Connect classes meaningfully.
3. **Data Properties** — Using camelCase with prefix arqo:. Domain is a class, range is an XSD datatype.
4. **Restrictions** — Apply owl:Restriction, owl:allValuesFrom, owl:someValuesFrom, owl:cardinality when semantically justified.
5. **Hierarchies** — Use rdfs:subClassOf for class hierarchies and rdfs:subPropertyOf for property hierarchies.

## Reification (Pivot Classes)
When facing complex scenarios involving more than two entities or a combination of entities and datatypes, apply reification. Create a pivot class to act as an intermediary. For example, when modeling "an object was recovered from a stratigraphic unit during an excavation campaign", create a pivot class like arqo:RecoveryContext linking the object, stratigraphic unit, and excavation campaign, rather than directly connecting all three with binary relations.

## Alignment Rules
- Always align new classes with CIDOC CRM superclasses (e.g., subClassOf crm:E19_Physical_Object, crm:E5_Event, crm:E7_Activity)
- Never duplicate CIDOC CRM semantics
- Never invent CRM entities — use the existing CRM class IDs (E5, E7, E19, etc.)
- Align stratigraphic constructs with CRMarchaeo (A1, A4, A5, A8)
- Separate physical processes from cognitive processes
- Avoid unnecessary reification

## Namespace Prefixes
```
@prefix arqo: <http://www.ontologyARQ.org/archaeological-object/> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix crmarchaeo: <http://www.cidoc-crm.org/crmarchaeo/> .
@prefix crmsci: <http://www.cidoc-crm.org/crmsci/> .
@prefix crmhs: <http://www.cidoc-crm.org/crmhs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
```

## Scenario

This ontology module focuses on archaeological objects — physical things recovered during archaeological excavation. Archaeological objects are NOT static isolated entities. The ontology must support their complete lifecycle:

- **Production**: manufacturing techniques, raw materials, geological provenance
- **Use**: functional attribution, human agency, social practice
- **Reuse**: modification, repair, functional transformation
- **Circulation**: movement between sites, cultural areas, exchange
- **Deposition**: stratigraphic context, depositional events, taphonomic processes
- **Recovery**: excavation campaigns, sampling, recording
- **Post-excavation**: laboratory analysis, conservation, classification
- **Biography**: complete lifecycle sequence, similar trajectories across sites

CRMarchaeo mainly models excavation processes, stratigraphy, and stratigraphic relationships. This module extends those capabilities toward archaeological finds, artifact lifecycle, object biography, materiality, and analytical processes.

The archaeological expert consensus is that:
- A physical object (`crm:E19_Physical_Object`) is a superclass of natural objects (`crm:E19_Physical_Object`) and human-made objects (`crm:E22_Human-Made_Object`)
- Natural objects can be divided into abiotic and biotic objects
- Human-made objects can be divided into artifacts, structures, and artistic expressions

## Important Rules

1. **Before writing the OWL code**: assess whether the CQ is answerable by an empty ontology. It is NOT answerable (100% of the time for an empty RDF). State "This CQ is NOT answerable by the current (empty) RDF. Proceeding to model it."

2. **Output format**: Turtle (.ttl) only. No comments, no explanations in the output OWL.

3. **Class naming**: Classes must have arqo: prefix. Use PascalCase. Example: `arqo:ArchaeologicalObject`, `arqo:ObjectBiography`.

4. **Property naming**: Properties must have arqo: prefix. Use camelCase. Example: `arqo:hasMaterial`, `arqo:producedBy`.

5. **Do not repeat**: Each file is independent. Do not assume previous content exists.

6. **Restrictions**: Add owl:Restriction where justified. Use owl:equivalentClass for strong restrictions and rdfs:subClassOf for necessary-but-not-sufficient conditions.

## Common Mistakes to Avoid

- Forgetting to add prefixes at the beginning of the code
- Forgetting to create pivot (reification) classes when needed
- Extracting classes like 'Date', 'integer' as OWL classes — these are data properties
- Not using RDF reification for relations between more than two classes
- The pivot class MUST be connected via object properties, NOT via rdfs:subClassOf
- Creating individuals in the text as classes

## Competency Question

**{CQ}**

## Current RDF

**EMPTY** (Memoryless CQbyCQ — each CQ processed independently with no prior ontology state)

## Output

Generate ONLY valid OWL 2 Turtle (.ttl) code. No markdown, no explanations.
```
