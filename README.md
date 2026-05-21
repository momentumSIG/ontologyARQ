# ontologyARQ — Archaeological Object Ontology Module

> Ontology engineering for archaeology and cultural heritage using Large Language Models (LLMs).  
> CIDOC CRM / CRMarchaeo compatible. OWL 2 Turtle (.ttl) serialization.

---

## Project Status

| Deliverable | Count | Status |
|---|---|---|
| Competency Questions (CQs) | 80 (4 blocks × 20) | Done |
| Prompting strategies | 2 (Memoryless CQbyCQ + Ontogenia) | Done |
| Temperatures tested | 3 (0.3, 0.5, 0.7) | Done |
| OWL/Turtle files generated | 123 | Done |
| Classes defined | 24 | Done |
| Object properties | 21 | Done |
| Data properties | 8 | Done |
| CRMarchaeo alignment | Full class subsumption + property ranges | Done |
| LLM model | deepseek-v4-pro | Done |

---

## What this ontology does

CRMarchaeo models **excavation processes and stratigraphy** exceptionally well, but has limited coverage of **archaeological objects** — their lifecycle, materiality, biography, circulation, and analysis.

The `arqo:` module extends CRMarchaeo by providing:

- **Archaeological Object** — subclass of `crm:E19_Physical_Object`
- **Object biography** — from production through use, reuse, repair, deposition, recovery, and analysis
- **Materiality** — material composition, manufacturing techniques, raw material provenance
- **Typological classification** — aligned with Getty AAT, SKOS
- **Human agency** — actors associated with production and use
- **Taphonomy** — post-depositional processes, conservation state
- **Scientific sampling** — sample extraction events, laboratory analysis
- **Circulation** — movement between sites and cultural areas

See `ontologies_generated/Deepseekv4/README.md` for the full inventory.

---

## Repository Structure

```
.
├── AGENTS.md                           # Project principles, methodology, reproducibility guide
├── ontologyARQ/                        # This repo (GitHub: momentumSIG/ontologyARQ)
│   ├── README.md                       # This file
│   └── LICENSE
├── CQ/
│   └── CQ_Deepseekv4Pro/               # 80 competency questions (4 blocks × 20)
│       ├── CQ-object-deepseek.md       # Archaeological object (20 CQ)
│       ├── CQ-spatial-deepseek.md      # Spatial (20 CQ)
│       ├── CQ-temporal-deepseek.md     # Temporal (20 CQ)
│       └── CQ-stratigraphy-deepseek.md # Stratigraphy (20 CQ)
├── prompts/
│   ├── memoryless/
│   │   └── prompt_archaeological_object.md   # Memoryless CQbyCQ template
│   └── ontogenia/
│       └── prompt_archaeological_object.md   # Ontogenia metacognitive template
├── ontologies_generated/
│   └── Deepseekv4/                     # Generated OWL/Turtle ontologies
│       ├── memoryless/temp_0_{3,5,7}/  # 60 .ttl files (independent per CQ)
│       ├── ontogenia/temp_0_{3,5,7}/   # 60 .ttl step files + 3 cumulative
│       └── README.md                   # Full documentation
├── docs/
│   ├── analisis.docx                   # CRMarchaeo gap analysis
│   ├── PreguntasCompetencia.docx        # Original CQ set (ChatGPT)
│   ├── ontologyLLM.pdf                 # OntologyLLM paper (ESWC 2025)
│   └── modelo idearq_v3b.pdf           # IDEArq UML conceptual model
└── ONTOLOGIAS/
    ├── owl/                            # CRMarchaeo v2.1.1
    └── ttl/                            # GeoSPARQL, OWL-Time
```

---

## CRMarchaeo Integration

The `arqo:` module connects to CRMarchaeo through **class subsumption** and **property ranges**:

```turtle
# ── Class subsumption ───────────────────────────────────────
arqo:DepositionEvent       rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis .
arqo:RecoveryEvent         rdfs:subClassOf crmarchaeo:A1_Excavation_Process_Unit .
arqo:TaphonomicProcess     rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event .
arqo:ArchaeologicalObject  rdfs:subClassOf crm:E19_Physical_Object .

# ── Property ranges ─────────────────────────────────────────
arqo:depositedIn           rdfs:range crmarchaeo:A8_Stratigraphic_Unit .
arqo:recoveredFrom         rdfs:range crmarchaeo:A8_Stratigraphic_Unit .
arqo:locatedInStructure    rdfs:range crmarchaeo:A2_Stratigraphic_Volume_Unit .

# ── Object lifecycle chain ──────────────────────────────────
arqo:hasBiography          rdfs:range arqo:ObjectBiography .
arqo:participatedInProduction rdfs:range arqo:ProductionEvent .
arqo:participatedInUse     rdfs:range arqo:UseEvent .
arqo:participatedInReuse   rdfs:range arqo:ReuseEvent .
arqo:repairedIn            rdfs:range arqo:RepairEvent .
arqo:wasSampledIn          rdfs:range arqo:SamplingEvent .
arqo:underwentTreatment    rdfs:range arqo:PostExcavationTreatment .
```

See **§3 — CRMarchaeo Integration Map** in `ontologies_generated/Deepseekv4/README.md` for the complete alignment table.

---

## Prompting Strategies

| Strategy | Reference | Behaviour |
|---|---|---|
| **Memoryless CQbyCQ** | [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) | Each CQ processed independently. RDF context always empty. 60 files generated (20 CQ × 3 temps). |
| **Ontogenia** | [Ontogenia (Lippolis et al.)](https://github.com/dersuchendee/Onto-Generation) | Iterative ontology extension. 9-step metacognitive procedure. RDF accumulates across steps. 63 files (60 steps + 3 cumulative). |

Templates at: `prompts/memoryless/prompt_archaeological_object.md` and `prompts/ontogenia/prompt_archaeological_object.md`

---

## Temperature as Experimental Variable

| Temperature | Classes | Properties | Restrictions | Cumulative lines | Style |
|---|---|---|---|---|---|
| **0.3** | 6 | 8 | Minimal | 104 | Conservative — max CRM reuse |
| **0.5** | 14 | 19 | Moderate | 222 | Balanced |
| **0.7** | 24 | 29 | Extensive | 263 | Creative — deep hierarchy + reification |

---

## CQ Attribution

| Block | Reused (from Word) | New (from gap analysis) | Total |
|---|---|---|---|
| Archaeological Object | 8 | 12 | 20 |
| Spatial | 11 | 9 | 20 |
| Temporal | 9 | 11 | 20 |
| Stratigraphy | 8 | 12 | 20 |
| **Total** | **36 (45%)** | **44 (55%)** | **80** |

Detailed attribution table per CQ in `ontologies_generated/Deepseekv4/README.md` §2.

---

## How to Reproduce with Another LLM

See the **"How to Reproduce with Another LLM Model"** section in `AGENTS.md` for step-by-step instructions covering:
1. Generating CQs
2. Creating prompt templates
3. Generating OWL/Turtle ontologies
4. Documenting results

Each LLM model should produce its own directory under `CQ/CQ_{model_name}/` and `ontologies_generated/{model_name}/`.

---

## References

- **Onto-Generation** — Lippolis, A.S. et al. (2025). *Ontology Generation using Large Language Models*. ESWC 2025. [GitHub](https://github.com/dersuchendee/Onto-Generation)
- **CIDOC CRM v7.3.2** — [cidoc-crm.org](https://www.cidoc-crm.org/)
- **CRMarchaeo v2.1.1** — [cidoc-crm.org/crmarchaeo](https://www.cidoc-crm.org/crmarchaeo/)
- **Ontogenia** — Lippolis, A.S., Ceriani, M., Zuppiroli, S., Nuzzolese, A.G. *Ontogenia: Ontology Generation with Metacognitive Prompting in LLMs*
- **IDEArq** — UML conceptual model (`docs/modelo idearq_v3b.pdf`)

## License

[MIT License](LICENSE)
