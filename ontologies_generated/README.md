# Generated Ontologies

Este directorio contiene módulos de ontología generados independientemente por diferentes modelos de lenguaje (LLMs).

| Módulo | Modelo | Diseño | Archivos | Clases | Props |
|---|---|---|---|---|---|
| [Deepseekv4](Deepseekv4/) | deepseek-v4-pro | Event-centric | 123 | 24 | 29 |
| [K2.6](K2.6/) | K2.6 | Object-centric | 124 | 28 | 25 |

Cada módulo sigue la misma metodología CQ-driven (Memoryless CQbyCQ + Ontogenia a 3 temperaturas) pero con decisiones ontológicas de diseño independientes.

---

## Deepseekv4 — Diseño Event-centric

| Aspecto | Valor |
|---|---|
| **Enfoque** | Event-centric (biografía del objeto como secuencia de eventos) |
| **Clases core** | ArchaeologicalObject + ProductionEvent, UseEvent, ReuseEvent, DepositionEvent, RecoveryEvent |
| **Jerarquía** | Plana (1-2 niveles) |
| **Reificación** | 4 clases pivot (RecoveryContext, MaterialAssignment, TypologicalAssignment, BiographyLink) |
| **Atributos físicos** | Mínimos (conservation state, local ID) |
| **Estratigrafía** | Eventos (DepositionEvent, RecoveryEvent) |
| **Documentación** | Eventos (PostExcavationTreatment) |
| **CQs** | 36 reutilizadas + 44 nuevas |

[Ver documentación completa → Deepseekv4/README.md](Deepseekv4/)

---

## K2.6 — Diseño Object-centric

| Aspecto | Valor |
|---|---|
| **Enfoque** | Object-centric (objeto como entidad con atributos y taxonomía) |
| **Clases core** | ArchaeologicalObject → NaturalObject/HumanMadeObject → AbioticObject/BioticObject/Artefact/Structure/ArtisticExpression |
| **Jerarquía** | Profunda (3 niveles) |
| **Reificación** | Mínima (partonomía hasPart/isComponentOf) |
| **Atributos físicos** | Extensivos (morphometry, weight, Munsell color, grain size, completeness) |
| **Estratigrafía** | Entidades (StratigraphicSequence, NegativeFeature, Paleosol, ConstructionElement) |
| **Documentación** | Entidades (DigitalDocumentation, PhotogrammetricModel, ScholarlyReference) |
| **CQs** | 80 nuevas (0 reutilizadas) |

[Ver documentación completa → K2.6/README.md](K2.6/)

---

## Comparativa de diseños

| Dimensión | Deepseekv4 | K2.6 |
|---|---|---|
| **Filosofía** | Event-centric | Object-centric |
| **Entidades principales** | Eventos | Objetos (jerarquía taxonómica) |
| **Clases** | 24 | 28 |
| **Object properties** | 21 | 18 |
| **Data properties** | 8 | 7 |
| **Niveles de jerarquía** | 1-2 | 3 |
| **Reificación** | 4 pivot classes | 2 properties (partonomía) |
| **Atributos físicos** | Mínimos | Extensivos |

---

## Referencias

- **Onto-Generation** — Lippolis, A.S. et al. (2025). *Ontology Generation using Large Language Models*. ESWC 2025.
- **CIDOC CRM v7.3.2** — [cidoc-crm.org](https://www.cidoc-crm.org/)
- **CRMarchaeo v2.1.1** — [cidoc-crm.org/crmarchaeo](https://www.cidoc-crm.org/crmarchaeo/)
