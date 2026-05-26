# Ontogenia Metacognitive Procedure for Archaeological Ontology Design

This 9-step procedure guides the iterative design of an archaeological ontology module using metacognitive prompting. Adapted from Lippolis et al. (ESWC 2025) "Ontogenia: Ontology Generation with Metacognitive Prompting in LLMs".

---

## Step 1: Analyze the Competency Question

Read the competency question carefully. Identify its key ontological components:

- **Subject:** What is the primary entity being asked about? (object, place, event, actor)
- **Predicate:** What relationship or property is being queried?
- **Object:** What is the target of the query? (material, period, location, technique)
- **Context:** What archaeological module does this belong to? (Object, Spatial, Temporal, Stratigraphy)

**Archaeological example:**
- CQ: "What is the primary material composition of an archaeological object?"
- Subject: ArchaeologicalObject
- Predicate: hasMaterial
- Object: E57_Material
- Module: Object

---

## Step 2: Identify the Context

Define the scope and domain of the ontology for this CQ:

- **Module:** Which of the 4 thematic blocks does this CQ belong to?
  - Archaeological Object
  - Spatial
  - Temporal
  - Stratigraphy
- **CRM alignment:** Which CRM/CRMarchaeo classes already cover this concept?
- **Reuse priority:** Check these ontologies before creating new terms:
  1. CIDOC CRM (crm:)
  2. CRMarchaeo (crmarchaeo:)
  3. CRMsci (crmsci:)
  4. CRMinf (crminf:)
  5. CRMhs (crmhs:)
  6. GeoSPARQL (geo:)
  7. OWL-Time (time:)
  8. PROV-O (prov:)

**Principle:** Never create a new class if a CRM class already models the concept.

---

## Step 3: Decompose the Competency Question

Break down the CQ into its constituent semantic parts and map them to ontological constructs:

1. **Subject → owl:Class** (e.g., "archaeological object" → `arqo:ArchaeologicalObject`)
2. **Predicate → owl:ObjectProperty or owl:DatatypeProperty** (e.g., "is made of" → `arqo:hasMaterial`)
3. **Object → owl:Class or xsd:datatype** (e.g., "material" → `crm:E57_Material`)

**Reification check:** If the relationship involves more than 2 entities or a combination of entity + datatype + entity, use a pivot class (reification). Examples:
- "What material and functional interpretation have researchers assigned to an object?" → reify as `arqo:MaterialInterpretation` or `arqo:FunctionalInterpretation` (subclass of `crm:E17_Type_Assignment`)
- "Where do the raw materials of an object originate geologically?" → reify as `arqo:RawMaterialSource` linked via `arqo:derivesFromSource`

---

## Step 4: Determine Subclass Relationships

Establish hierarchical relationships using `rdfs:subClassOf`. Always anchor new classes in the CRM hierarchy:

```
arqo:ArchaeologicalObject rdfs:subClassOf crm:E19_Physical_Object
arqo:NaturalObject rdfs:subClassOf arqo:ArchaeologicalObject
arqo:HumanMadeObject rdfs:subClassOf arqo:ArchaeologicalObject
```

**CRM alignment hierarchy:**
- `crm:E19_Physical_Object` for physical things
- `crm:E22_Human-Made_Object` for artifacts
- `crm:E24_Physical_Human-Made_Thing` for structures
- `crm:E5_Event` for events and processes
- `crm:E53_Place` for locations
- `crm:E52_Time-Span` for temporal extents
- `crmarchaeo:A8_Stratigraphic_Unit` for stratigraphic contexts
- `crmarchaeo:A4_Stratigraphic_Genesis` for depositional events

If creating a subclass hierarchy (e.g., NaturalObject → AbioticObject, BioticObject), ensure the hierarchy is semantically justified and not artificially deep.

---

## Step 5: Extend the Ontology with Restrictions

Apply OWL restrictions where archaeologically meaningful:

**Value restrictions:**
- `owl:allValuesFrom` — when the object of a property MUST belong to a specific class
- `owl:someValuesFrom` — when the object of a property MUST include at least one instance of a specific class
- `owl:hasValue` — when a property MUST have a specific individual value

**Cardinality:**
- `owl:minCardinality` — minimum number of values (e.g., an archaeological object has at least one material)
- `owl:maxCardinality` — maximum number of values
- `owl:cardinality` — exact number

**Example:**
```turtle
arqo:HumanMadeObject rdfs:subClassOf [
    rdf:type owl:Restriction ;
    owl:onProperty arqo:wasProducedBy ;
    owl:someValuesFrom arqo:ManufacturingEvent
] .
```

**Archaeological restriction patterns:**
- Every HumanMadeObject was produced in at least one ManufacturingEvent
- Every ArchaeologicalObject deposited in a stratigraphic unit was deposited through a DepositionEvent
- Every ChronologicalAssignment was produced by at least one DatingTechnique

---

## Step 6: Define Equivalent and Disjoint Classes

**Equivalent classes:** Use `owl:equivalentClass` when two classes are semantically identical. Rare in archaeological domain — prefer `rdfs:subClassOf`.

**Disjoint classes:** Use `owl:disjointWith` when classes are mutually exclusive:

| Disjoint pair | Justification |
|---|---|
| `arqo:NaturalObject` ⊥ `arqo:HumanMadeObject` | An object cannot be both natural and human-made in origin |
| `arqo:AbioticObject` ⊥ `arqo:BioticObject` | A natural object is either non-living or living in origin |
| `arqo:Artefact` ⊥ `arqo:Structure` | Portable vs non-portable are mutually exclusive |

**Note:** Disjointness is temperature-dependent. Apply only at temperature 0.7 (creative). At 0.3 (conservative), avoid explicit disjointness.

---

## Step 7: Integrate and Refine

Review the ontology for:

1. **CRMarchaeo compatibility:** Every property range that points to a stratigraphic concept MUST point to a `crmarchaeo:` class
2. **Semantic consistency:** No duplicated classes, no contradictory restrictions
3. **Modularity:** Is this CQ introducing concepts that belong to another thematic block?
4. **Integration:** Does this ontology fragment connect to the accumulated previous ontology?

**Cross-module integration rules:**
- Object properties linking to spatial concepts should use `crm:E53_Place` as range, not new classes
- Object properties linking to temporal concepts should use `crm:E52_Time-Span` as range
- Object properties linking to stratigraphic concepts should use `crmarchaeo:A8_Stratigraphic_Unit` as range

---

## Step 8: Validate and Explain

Confirm that:

1. The ontology fragment CAN answer the competency question
2. Every class has an `rdfs:label` and `rdfs:comment`
3. Every object property has a `domain` and `range`
4. Every data property has a `domain` and `xsd:` range
5. No CRM classes are duplicated with different IRIs
6. All prefixes are declared at the top of the file

**Self-check questions:**
- "Can I write a SPARQL query using this ontology that answers the CQ?"
- "Is there a CIDOC CRM class that already models this concept?"
- "Did I use E17_Type_Assignment for classifications instead of a direct property?"
- "Did I distinguish between observation (S4_Observation) and interpretation?"

---

## Step 9: Evaluate Confidence and Test

Test the ontology with archaeological instances:

1. **Instance test:** Create a sample object (e.g., a Bronze Age ceramic vessel) and verify all properties can be populated
2. **Query test:** Write a SPARQL query that answers the CQ using the ontology
3. **Coverage assessment:** What percentage of the CQ's information need is satisfied?

**Confidence assessment:**
- **High:** CRM native class used, clear domain/range, all properties present
- **Medium:** New class created but well-aligned with CRM hierarchy
- **Low:** New class with no CRM alignment, or complex reification needed

**Temperature effect on confidence:**
- At 0.3, prefer high-confidence (CRM-native) solutions
- At 0.5, accept medium-confidence (aligned extensions)
- At 0.7, explore low-confidence (novel concepts) where justified

---

## Procedure Variables

When using this procedure in a prompt template, the following variables are available:

- `{CQ}` — The current competency question (e.g., "CQ-OBJ-01: What is the primary material composition of an archaeological object?")
- `{scenario}` — The archaeological domain narrative (see prompt template)
- `{previous_output}` — The accumulated RDF from previous steps (empty for step 1)
- `{ontology_elements}` — "Classes, Object Properties, Datatype Properties. Object properties need domain and range. All need rdfs:label and rdfs:comment. Add restrictions where justified. Prefer CIDOC CRM alignment. Reify assignments and observations."
