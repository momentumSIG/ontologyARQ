# Archaeological Ontology Generation — Prompting Strategies

> Adapted from [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) (Lippolis et al., ESWC 2025)
> Domain: Archaeological object ontology compatible with CIDOC CRM and CRMarchaeo

---

## Overview

This directory contains prompt templates for generating archaeological OWL ontologies using Large Language Models. Two prompting strategies are provided, both adapted from the Onto-Generation framework for the archaeological domain.

| Strategy | Description | File |
|---|---|---|
| **Memoryless CQbyCQ** | Each CQ processed independently with empty RDF context. No ontology memory across CQs. | `memoryless/prompt_archaeological_object.md` |
| **Ontogenia** | Iterative ontology extension with metacognitive prompting. RDF accumulates across steps. 9-step procedure. | `ontogenia/prompt_archaeological_object.md` |

## Strategy Comparison

| Aspect | Memoryless CQbyCQ | Ontogenia |
|---|---|---|
| RDF context | Always empty | Accumulated from previous steps |
| Context size | Low | Grows with each step |
| Ontology coherence | Low (fragments may conflict) | High (semantic consistency enforced) |
| Reuse encouragement | Minimal | Maximum (accumulated classes/properties reused) |
| Procedure | Direct ontology generation | 9-step metacognitive procedure |
| Domain story | `{story}` — archaeological narrative | `{scenario}` — unified archaeological domain scenario |
| CQ handling | `{CQ}` — one at a time, isolated | `{CQ}` — one at a time, building on `{previous_output}` |
| Output | Independent OWL fragment per CQ | Cumulative OWL ontology per block |

## Directory Structure

```
prompts/
├── README.md                                  # This file
├── memoryless/
│   └── prompt_archaeological_object.md        # Memoryless CQbyCQ prompt
├── ontogenia/
│   ├── prompt_archaeological_object.md        # Ontogenia prompt with ODPs
│   └── procedure.md                           # 9-step metacognitive procedure
```

## Prompt Variables

### Memoryless CQbyCQ

| Variable | Content |
|---|---|
| `{story}` | Archaeological domain narrative (embedded in prompt) |
| `{CQ}` | Current competency question (e.g., "CQ-OBJ-01: What is the primary material composition...") |
| `{rdf}` | Always empty — no memory across CQs |

### Ontogenia

| Variable | Content |
|---|---|
| `{scenario}` | Archaeological domain narrative (embedded in prompt) |
| `{CQ}` | Current competency question |
| `{procedure}` | Content of `prompts/ontogenia/procedure.md` |
| `{previous_output}` | Accumulated RDF from all previous CQ steps |
| `{patterns_json}` | OWL Turtle ODPs (embedded in prompt) |
| `{ontology_elements}` | Description of expected ontology elements |

## Domain Adaptations from Upstream

The following adaptations were made to the original Onto-Generation prompts:

1. **Namespace prefixes:** Replaced generic `@prefix : <http://www.example.org/test#>` with archaeological namespaces (arqo:, crm:, crmarchaeo:, crmsci:, crminf:, crmhs:, owl:, rdf:, rdfs:, xsd:, skos:, geo:, time:, prov:)

2. **Naming convention:** Removed `Cl_` prefix convention. Uses CRM-aligned naming (e.g., `arqo:ArchaeologicalObject`)

3. **Domain narrative:** Replaced generic university/story domain with archaeological object lifecycle narrative covering materiality, biography, stratigraphy, chronology, spatial context, and scientific analysis

4. **Reification examples:** Replaced generic examples (user-resource-time) with archaeological reification patterns (object-material-observation, type assignment, biographical event)

5. **CRM alignment rules:** Added explicit CRM/CRMarchaeo class hierarchy reference and the principle of "prefer reuse over creation"

6. **Ontology Design Patterns:** Included 7 archaeological ODPs in Turtle format:
   - CRM Event Pattern
   - CRMarchaeo Stratigraphic Pattern
   - E17 Type Assignment Pattern
   - S4 Observation Pattern
   - PROV-O Provenance Chain Pattern
   - Lifecycle Phase Pattern
   - Object Classification Hierarchy Pattern

7. **Archaeological-specific mistakes:** Added domain-specific warnings (conflating manufacturing date with use date, treating classification as intrinsic, forgetting fragmentation)

8. **Temperature guidance:** Added temperature-specific behavior for archaeological domain (0.3 conservative, 0.5 balanced, 0.7 creative)

9. **9-step procedure:** Adapted metacognitive procedure with archaeological examples for each step

## How to Use

### Memoryless CQbyCQ

```
For each CQ in [CQ-OBJ-01 ... CQ-OBJ-20]:
    1. Set {story} = archaeological domain narrative
    2. Set {CQ} = current competency question
    3. Set {rdf} = empty
    4. Submit to LLM
    5. Save output as CQ-{ID}.ttl
```

### Ontogenia

```
Set {previous_output} = empty
Set {scenario} = archaeological domain scenario
Set {procedure} = content of procedure.md
Set {patterns_json} = ODPs from prompt

For each CQ in [CQ-OBJ-01 ... CQ-OBJ-20]:
    1. Set {CQ} = current competency question
    2. Submit to LLM with {previous_output}
    3. Save output as step_{NN}_{CQ-ID}.ttl
    4. Set {previous_output} = accumulated RDF from output
    
After all CQs processed:
    Save final {previous_output} as cumulative.ttl
```

## Temperature Evaluation

Temperature is treated as an experimental variable. Generate ontologies at three temperatures:

| Temperature | Behavior | Archeological effect |
|---|---|---|
| **0.3** | Conservative | Max CRM reuse, flat hierarchies, no disjointness, minimal restrictions |
| **0.5** | Balanced | Moderate extensions, standard CRM alignment, 2-level hierarchy, some restrictions |
| **0.7** | Creative | Deep hierarchies (3 levels), pivot classes, disjointness axioms, full lifecycle chains |

## References

- Lippolis, A.S. et al. (2025). *Ontology Generation using Large Language Models*. ESWC 2025.
- [Onto-Generation Repository](https://github.com/dersuchendee/Onto-Generation)
- [CIDOC CRM v7.3.2](https://www.cidoc-crm.org/)
- [CRMarchaeo v2.1.1](https://www.cidoc-crm.org/crmarchaeo/)
