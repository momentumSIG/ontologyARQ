# CONTEXT — ONTOLOGIA-ARQ

Glossary of the experimental pipeline. No implementation details, no specs: terms and boundaries only.

## Core entities

- **Competency Question (CQ)** — A question the ontology must be able to answer. The atomic unit of the experiment: each CQ drives one ontology fragment (memoryless) or one iteration (ontogenia).

- **CQ Block** — A thematic grouping of CQs. Four canonical blocks: **object**, **spatial**, **temporal**, **stratigraphy**. This is the *subject-matter* axis.

- **CQ Pattern** — A modeling-style grouping of CQs, orthogonal to Block. Three canonical patterns:
  - **P1 Event-Driven** — models *what happened* (lifecycle events: production, use, deposition, recovery...).
  - **P2 State-Transition** — models *how it is* (physical/material states, composition, spatial relations).
  - **P4 Assignment-Intrinsic** — models *what we know* (interpretive assignments: typology, chronology, hypotheses, certainty).
  Orthogonal to CQ Block: a CQ belongs to exactly one Block and exactly one Pattern.

- **Generation Strategy** — The prompting workflow that turns CQs into ontology:
  - **memoryless** (CQbyCQ) — each CQ processed independently, RDF context always empty.
  - **ontogenia** — iterative, RDF context accumulates across CQs.
  This is the *prompting* axis.

- **Temperature** — Experimental variable over the generation strategy (0.3 conservative / 0.5 balanced / 0.7 creative). The third experimental axis.

- **LLM Model** — The model family under test (e.g. qwen3.8-max, deepseek-v4-pro). The fourth experimental axis, orthogonal to Strategy and Temperature.

- **Corpus** — The converted source material every model reads before generating (currently `data_markdown/`, mirrored from `data/`). Input, not artifact.

- **Generated Ontology** — The TTL artifact produced by one (Model × Strategy × Temperature) cell. Stored under `ontologies_generated/<model>/`.

- **Reference Ontology** — External standards used for alignment evaluation: CIDOC CRM, CRMarchaeo, CRMsci, CRMhs, AO-Cat, GeoSPARQL, OWL-Time, PROV-O, GeoSciML, SKOS. Never generated, never modified.

- **Evaluation Dimension** — One quality measure over generated ontologies (semantic consistency, drift, redundancy, CIDOC alignment, determinism, stability, hallucinated entities, CQ coverage, richness, generation efficiency).

## Boundary rules

- **Block ≠ Pattern**: a CQ's Block says *what subject it covers*; its Pattern says *how it models that subject*. Both apply to every CQ.
- **Strategy ≠ Model**: memoryless/ontogenia are prompting workflows; the LLM under test is independent of which workflow runs it.
- **Corpus ≠ Ontology**: converted source material is input; generated TTL is output. Never co-locate them.
- **Generated ≠ Reference**: one is produced by the experiment, the other is the standard it is measured against.