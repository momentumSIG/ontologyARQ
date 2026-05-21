# Ontogenia — Archaeological Object Module Prompt

Adapted from [Onto-Generation Ontogenia PromptingTechniques](https://github.com/dersuchendee/Onto-Generation/blob/main/PromptingTechniques/README.md).

---

## Metacognitive Prompting Procedure

Ontogenia is a technique for ontology generation using metacognitive prompting. The procedure merges five steps from metacognitive prompting with the eXtreme Design methodology.

---

### Procedure Definition

Follow these steps sequentially when designing each ontology fragment:

**Step 1: Analyze the Competency Question**
- Understand the CQ to identify key ontological components.
- What is being asked? What entities, relations, and attributes are involved?

**Step 2: Identify the Context**
- Define the scope and domain of the ontology fragment.
- Which CIDOC CRM / CRMarchaeo classes are relevant?
- What external ontologies should be considered?

**Step 3: Decompose the Competency Question**
- Break down the CQ into subject, predicate, object, and predicate nominative.
- Map these elements to ontological constructs (classes, object properties, data properties).

**Step 4: Determine Subclass Relationships**
- Establish subclass relationships using rdfs:subClassOf.
- Align new classes with existing CIDOC CRM / CRMarchaeo hierarchies.

**Step 5: Extend the Ontology with Restrictions**
- Apply restrictions: owl:allValuesFrom, owl:someValuesFrom, owl:hasValue.
- Define cardinality: owl:minCardinality, owl:exactCardinality, owl:maxCardinality.

**Step 6: Define Equivalent and Disjoint Classes**
- Use owl:equivalentClass for class equivalences.
- Use owl:disjointWith for mutually exclusive classes.

**Step 7: Integrate and Refine**
- Merge the new ontology fragment with the previous accumulated ontology.
- Ensure logical consistency — no contradictions with existing axioms.
- Check for duplicate semantics.

**Step 8: Validate and Explain**
- Confirm the ontology answers the current CQ and remains compatible with all previous CQs.
- Verify CIDOC CRM compatibility.

**Step 9: Evaluate Confidence and Test**
- Test the ontology with hypothetical instances.
- Assess whether the ontology elements are sufficient.

---

## Template

```text
Read the following instructions: '{procedure}'. 

Based on the scenario: '{scenario}', design an ontology module that comprehensively answers the following competency question: '{CQ}'.

Load the previous ontology state from: '{previous_output}'. You MUST PRESERVE all classes, properties, and restrictions from the previous state. You can ADD new classes, properties, and restrictions to satisfy the current CQ. Do NOT remove or modify existing axioms unless they conflict with the new CQ.

Remember what the ontology elements are: classes, object properties, datatype properties. Object properties need explicit domain and range. All elements need an rdfs:label with an explanation. You also need to add restrictions and subclasses for both classes and object properties when applicable.

Ontology Design Patterns to consider:
- **CIDOC CRM Event Pattern**: Model processes as subclasses of crm:E5_Event or crm:E7_Activity
- **CIDOC CRM Physical Object Pattern**: Model objects as subclasses of crm:E19_Physical_Object or crm:E22_Human-Made_Object
- **CRMarchaeo Stratigraphic Pattern**: Use crmarchaeo:A8_Stratigraphic_Unit for context and crmarchaeo:A4_Stratigraphic_Genesis for deposition
- **Reification Pattern**: When more than two entities are related, create a pivot class
- **Observation Pattern (CRMsci)**: Use crmsci:S4_Observation for analytical observations

When you're done, send me only the COMPLETE accumulated ontology in Turtle (.ttl) format. Include ALL elements from the previous state PLUS the new additions. Do not comment.
```

---

## Scenario

This ontology module focuses on **archaeological objects** — physical things recovered during archaeological excavation. Archaeological objects are NOT static isolated entities. The ontology must support their complete lifecycle:

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
- `crm:E19_Physical_Object` is a superclass of natural objects and human-made objects
- Natural objects include abiotic and biotic objects
- Human-made objects include artifacts, structures, and artistic expressions

---

## Accumulated Ontology

The Ontogenia strategy uses **ontology memory accumulation**. Each step receives the complete ontology from the previous step. The LLM must:

1. PRESERVE all existing classes, properties, and restrictions
2. ADD new elements needed for the current CQ
3. ENSURE the cumulative ontology remains consistent
4. NEVER remove existing axioms unless they contradict the new CQ
5. ALWAYS output the COMPLETE ontology (previous + new additions)

**Step progression:**
- Step 1: Empty → CQ-OBJ-01 → Ontology v1
- Step 2: Ontology v1 → CQ-OBJ-02 → Ontology v2
- Step 3: Ontology v2 → CQ-OBJ-03 → Ontology v3
- ...
- Step 20: Ontology v19 → CQ-OBJ-20 → Final cumulative ontology

---

## Namespace Prefixes

```turtle
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

---

## Alignment Rules

1. Always align new classes with CIDOC CRM superclasses
2. Never duplicate CIDOC CRM semantics
3. Never invent CRM entities — use the existing CRM class IDs
4. Align stratigraphic constructs with CRMarchaeo
5. Separate physical processes from cognitive processes
6. Avoid unnecessary reification
7. Prefer ontology reuse over ontology invention
8. Use explicit domain and range definitions
9. Avoid creating artificial classes without conceptual necessity

---

## Ontology Elements

- **Classes** (PascalCase, prefix arqo:)
- **Object Properties** (camelCase, prefix arqo:, with domain and range)
- **Data Properties** (camelCase, prefix arqo:, domain = class, range = XSD type)
- **Restrictions** (owl:allValuesFrom, owl:someValuesFrom, owl:cardinality)

## Common Mistakes

1. Forgetting to include ALL previous ontology elements in the output
2. Removing existing axioms without justification
3. Not adding rdfs:label annotations
4. Creating classes without CIDOC CRM alignment
5. Omitting domain/range on object properties
6. Using reification when simple binary relations suffice
7. Not updating cumulative.ttl with the complete merged result
```
