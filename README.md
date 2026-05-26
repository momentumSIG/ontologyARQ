# Ontología del objeto arqueológico

> Compatible con CIDOC CRM · CRMarchaeo 

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![CIDOC CRM](https://img.shields.io/badge/CIDOC%20CRM-v7.3.2-green)](https://www.cidoc-crm.org/)
[![CRMarchaeo](https://img.shields.io/badge/CRMarchaeo-v2.1.1-green)](https://www.cidoc-crm.org/crmarchaeo/)
[![Methodology](https://img.shields.io/badge/Methodology-CQ--driven-orange)](ontologies_generated/)
[![LLMs](https://img.shields.io/badge/LLMs-3%20models-purple)](ontologies_generated/README.md)
[![Serialization](https://img.shields.io/badge/Serialization-OWL%202%20Turtle-lightgrey)](ontologies_generated/)

---

## ¿Qué es esto?

ONTOLOGIA-ARQ es un proyecto de ingeniería ontológica que utiliza **LLMs** para generar extensiones de CIDOC CRM centradas en el **objeto arqueológico**. CRMarchaeo modela muy bien la excavación y la estratigrafía, pero deja un vacío en el modelado del propio objeto — su ciclo de vida, materialidad, biografía, clasificación, análisis científico y significado cultural.

La metodología es **CQ-driven** (Competency Questions) con dos estrategias de prompting (Memoryless CQbyCQ y Ontogenia metacognitiva), evaluadas a 3 temperaturas (0.3, 0.5, 0.7). El diseño se inspira en 14 artículos académicos sobre teoría del objeto arqueológico y en el análisis de gaps de CRMarchaeo.

---

## Módulos generados

| Módulo | Modelo | Filosofía | CQs | Archivos | Clases |
|---|---|---|---|---|---|
| [Deepseekv4 v1](ontologies_generated/Deepseekv4/) | deepseek-v4-pro | **Event-centric** — los eventos son el ancla ontológica | 80 (4 bloques) | 123 | 24 |
| [Deepseekv4 v2](ontologies_generated/Deepseekv4_objeto/) | deepseek-v4-pro | **Object-centric** — el objeto es el ancla, basado en 14 artículos | 30 (objeto) | 183 | 33 |
| [Deepseekv4 v3](ontologies_generated/Deepseekv4_objeto_eventos/) | deepseek-v4-pro | **Event-centric** — mismas CQs que v2, modeladas desde eventos | 30 (objeto) | 183 | 17 |
| [K2.6](ontologies_generated/K2.6/) | K2.6 | **Object-centric** — jerarquía taxonómica profunda + atributos físicos | 80 (4 bloques) | 124 | 28 |
| [Qwen3.6](ontologies_generated/Qwen3.6/) | Qwen3.6 | **Objeto + eventos** — taxonomía del objeto + ciclo de vida explícito | 80 (4 bloques) | 493 | 30+ |

> Comparativa completa, inventario de clases/propiedades y mapas de alineación CRMarchaeo en [`ontologies_generated/README.md`](ontologies_generated/README.md).

---

## Filosofías de diseño comparadas

Las mismas preguntas de competencia pueden responderse desde filosofías ontológicas distintas:

| | Event-centric | Object-centric | Mixto |
|---|---|---|---|
| **Pregunta** | "¿Qué le pasó al objeto?" | "¿Qué es el objeto?" | "¿Qué es y qué le pasó?" |
| **Clases primarias** | `ProductionEvent`, `UseEvent`, `DepositionEvent` | `ArchaeologicalObject` → `NaturalObject`/`HumanMadeObject` → subtipos | Objeto + eventos de ciclo de vida |
| **Material** | `ProductionEvent` usa material | El objeto `hasMaterial` | El objeto `hasMaterial` |
| **Ciclo de vida** | Cadena de eventos | Objeto ancla eventos | `ObjectBiography` contiene eventos |
| **Clasificación** | `ClassificationEvent` | `TypologicalAssignment` (E17 pivot) | `TypologicalAssignment` |
| **Ejemplos** | Deepseekv4 v1, v3 | Deepseekv4 v2, K2.6 | Qwen3.6 |

El proyecto demuestra que el **mismo modelo** (Deepseekv4) produce ontologías radicalmente distintas con las **mismas CQs** cambiando solo la filosofía de diseño (v2 object-centric vs v3 event-centric).

---

## Estructura del repositorio

```
ONTOLOGIA-ARQ/
│
├── AGENTS.md                               # Principios, metodología, guía de reproducibilidad
├── README.md                               # Este archivo
├── LICENSE
│
├── CQ/
│   ├── CQ_Deepseekv4Pro/                   # 80 CQs originales event-centric (4 bloques × 20)
│   │   ├── CQ-object-deepseek.md
│   │   ├── CQ-spatial-deepseek.md
│   │   ├── CQ-temporal-deepseek.md
│   │   └── CQ-stratigraphy-deepseek.md
│   ├── CQ_Deepseekv4Pro_objeto/            # 30 nuevas CQs object-centric (basadas en artículos)
│   │   └── CQ-object-deepseek-v2.md
│   ├── CQ_K2.6/                            # 80 CQs independientes (4 bloques × 20)
│   └── CQ_Qwen3.6/                         # 80 CQs independientes (4 bloques × 20)
│
├── prompts/                                # Templates adaptados de Onto-Generation (ESWC 2025)
│   ├── README.md                           # Overview de estrategias y uso
│   ├── memoryless/
│   │   └── prompt_archaeological_object.md # Memoryless CQbyCQ (dominio arqueológico)
│   └── ontogenia/
│       ├── prompt_archaeological_object.md # Ontogenia con 7 ODPs y narrativa arqueológica
│       └── procedure.md                    # Procedimiento metacognitivo de 9 pasos
│
├── ontologies_generated/
│   ├── README.md                           # Master index: todos los módulos + comparativa unificada
│   ├── Deepseekv4/                         # v1 — event-centric original
│   │   ├── memoryless/temp_0_{3,5,7}/      # 60 .ttl
│   │   └── ontogenia/temp_0_{3,5,7}/       # 63 .ttl
│   ├── Deepseekv4_objeto/                  # v2 — object-centric
│   │   ├── memoryless/temp_0_{3,5,7}/      # 90 .ttl
│   │   └── ontogenia/temp_0_{3,5,7}/       # 93 .ttl
│   ├── Deepseekv4_objeto_eventos/          # v3 — event-centric (mismas CQs que v2)
│   │   ├── memoryless/temp_0_{3,5,7}/      # 90 .ttl
│   │   └── ontogenia/temp_0_{3,5,7}/       # 93 .ttl
│   ├── K2.6/                               # Object-centric con taxonomía profunda
│   │   ├── memoryless/temp_0_{3,5,7}/      # 60 .ttl
│   │   └── ontogenia/temp_0_{3,5,7}/       # 63 .ttl
│   └── Qwen3.6/                            # IDEArq-inspired lifecycle (4 bloques completos)
│       ├── memoryless/temp_0_{3,5,7}/      # 240 .ttl
│       └── ontogenia/temp_0_{3,5,7}/       # 252 .ttl
│
├── docs/
│   ├── analisis.docx                       # Análisis de gaps de CRMarchaeo
│   ├── PreguntasCompetencia.docx           # CQs originales (ChatGPT)
│   ├── ontologyLLM.pdf                     # Paper Onto-Generation (ESWC 2025)
│   ├── modelo idearq_v3b.pdf               # UML conceptual IDEArq
│   ├── objetoArqueologico/                 # 14 artículos sobre teoría del objeto arqueológico
│   │   └── analisis_ontologico.md          # Extracción semántica: 24 clases, 29 props, 8 módulos
│   └── ...
│
└── ontologies_docs/                        # Ontologías de referencia
    ├── owl/                                # CRMarchaeo v2.1.1
    ├── ttl/                                # GeoSPARQL, OWL-Time
    └── pdfs/                               # SKOS, PROV-O
```

---

## Metodología

### 1. Preguntas de competencia (CQs)

Cada modelo genera sus propias CQs a partir del análisis de gaps de CRMarchaeo (`docs/analisis.docx`). Las CQs se agrupan en 4 bloques temáticos: **Archaeological Object**, **Spatial**, **Temporal** y **Stratigraphy**.

La segunda generación de Deepseekv4 usa 30 CQs nuevas basadas en 14 artículos académicos sobre el objeto arqueológico, analizados en `docs/objetoArqueologico/analisis_ontologico.md`.

### 2. Estrategias de prompting

Adaptadas de [Onto-Generation](https://github.com/dersuchendee/Onto-Generation) (Lippolis et al., ESWC 2025):

| Estrategia | Descripción | Archivos/prompt |
|---|---|---|
| **Memoryless CQbyCQ** | Cada CQ se procesa independientemente. RDF vacío siempre. Sin memoria entre CQs. | `prompts/memoryless/` |
| **Ontogenia** | Extensión iterativa con prompting metacognitivo. 9 pasos. RDF se acumula entre pasos. | `prompts/ontogenia/` |

### 3. Temperatura como variable experimental

| Temp | Comportamiento | Efecto arqueológico |
|---|---|---|
| **0.3** | Conservador | Máxima reutilización de CRM, jerarquías planas, sin disjointness |
| **0.5** | Balanceado | Extensiones moderadas, alineación CRM estándar, jerarquía de 2 niveles |
| **0.7** | Creativo | Jerarquías profundas, clases pivote, disjointness, cadena completa de eventos |

### 4. Evaluación

Las ontologías generadas se evalúan en:
- Consistencia semántica
- Alineación con CIDOC CRM
- Cobertura de CQs
- Interoperabilidad
- Capacidad de razonamiento
- Redundancia ontológica

---

## CRMarchaeo — Integración

Todas las ontologías generadas extienden CRMarchaeo mediante **subsunción de clases** y **rangos de propiedades**:

```turtle
# Clases arqueológicas ancladas en CRM/CRMarchaeo
arqo:ArchaeologicalObject  rdfs:subClassOf crm:E19_Physical_Object .
arqo:DepositionEvent       rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis .
arqo:RecoveryEvent         rdfs:subClassOf crmarchaeo:A1_Excavation_Process_Unit .
arqo:TransformationEvent   rdfs:subClassOf crm:E81_Transformation .
arqo:ClassificationEvent   rdfs:subClassOf crm:E17_Type_Assignment .
arqo:AnalysisEvent         rdfs:subClassOf crmsci:S19_Encounter .
arqo:MeasurementEvent      rdfs:subClassOf crmsci:S21_Measurement .

# Propiedades que apuntan a entidades CRMarchaeo
arqo:depositedIn           rdfs:range crmarchaeo:A8_Stratigraphic_Unit .
arqo:recoveredFrom         rdfs:range crmarchaeo:A8_Stratigraphic_Unit .
arqo:underwentTaphonomic   rdfs:range crmarchaeo:A5_Stratigraphic_Modification_Event .
```

---

## Cómo reproducir con otro LLM

Ver la sección **"How to Reproduce with Another LLM Model"** en [`AGENTS.md`](AGENTS.md). El pipeline es:

1. Generar CQs propias (4 bloques × ~20 CQs)
2. Usar los prompts arqueológicos en `prompts/`
3. Generar ontologías en ambas estrategias a 3 temperaturas
4. Documentar en `ontologies_generated/{modelo}/`
5. Actualizar el master index

---

## Referencias

- **Onto-Generation** — Lippolis, A.S. et al. (2025). *Ontology Generation using Large Language Models*. ESWC 2025. [GitHub](https://github.com/dersuchendee/Onto-Generation)
- **CIDOC CRM v7.3.2** — [cidoc-crm.org](https://www.cidoc-crm.org/)
- **CRMarchaeo v2.1.1** — [cidoc-crm.org/crmarchaeo](https://www.cidoc-crm.org/crmarchaeo/)
- **Ontogenia** — Lippolis, A.S., Ceriani, M., Zuppiroli, S., Nuzzolese, A.G. *Ontogenia: Ontology Generation with Metacognitive Prompting in LLMs*

### Artículos de teoría del objeto arqueológico

14 artículos analizados en `docs/objetoArqueologico/analisis_ontologico.md`:
Holtorf (2013) — *On Pastness* · Gosden — *What do objects want?* · Garcia-Rovira (2015) · Rowe (1959) · Pollard (2014) · Gill (2018) · Guerra (2003) · Schwarcz (2002) · ICCROM (2018) · Pernicka et al. · BF03376602 · y otros.

---

## Licencia

[MIT License](LICENSE)
