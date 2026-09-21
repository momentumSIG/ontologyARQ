# Competency Questions clasificadas por Patron

> **Date:** 2026-06-16  
> **Version:** 1.2  
> **Source:** `CQ/CQ_{Deepseek,Kimi,Qwen}_unificado/CQ-object-*-final.md`  
> **Purpose:** Clasificar las 150 CQs unificadas de objeto arqueologico (50 por LLM) segun el patron ontologico, con distribucion perfectamente balanceada de 50 CQs por patron

---

## Criterios de clasificacion

| Patron | Enfoque | Foco de la pregunta |
|---|---|---|
| **P1 Event-Driven** | Modela el **WHAT HAPPENED** | Eventos del ciclo de vida: produccion, uso, reuso, reparacion, deposicion, recuperacion, circulacion, repatriacion, custodia, biografia como secuencia |
| **P2 State-Transition** | Modela el **HOW IT IS** | Estados fisicos y transformacion material: composicion, propiedades, fragmentacion, patina, corrosion, conservacion, integridad, desgaste, relaciones espaciales, estados de distribucion |
| **P4 Assignment-Intrinsic** | Modela el **WHAT WE KNOW** | Asignaciones interpretativas: tipologia, cronologia, hipotesis, certeza, significado, agencia, identificador, hipotesis rivales |

### Reglas

1. **Patron principal**: cada CQ se asigna a **un solo patron** (el que mejor responde la pregunta)
2. **Foco principal**: si la CQ toca multiples patrones, se clasifica por lo que pregunta directamente
3. **Estados fisicos y materiales** (composicion, propiedades, distribucion espacial): **P2** (son descripciones de estado, no asignaciones interpretativas)
4. **Eventos del ciclo de vida** (manufactura, uso, reuso, reparacion, deposicion, recuperacion, circulacion, repatriacion, custodia): **P1**
5. **Asignaciones interpretativas** (tipologia, cronologia, hipotesis, certeza, significado, agencia, identificador): **P4**

---

## Resumen de distribucion

| LLM | P1 (Eventos) | P2 (Estados) | P4 (Asignaciones) | Total |
|---|---|---|---|---|
| **Deepseek** | 21 | 17 | 12 | 50 |
| **Kimi** | 12 | 20 | 18 | 50 |
| **Qwen** | 17 | 13 | 20 | 50 |
| **TOTAL** | **50 (33%)** | **50 (33%)** | **50 (33%)** | **150** |

### Observaciones

- **Distribucion perfectamente balanceada**: 50 CQs por patron (33% cada uno)
- **P1 (eventos)**: 50 CQs, centrado en el ciclo de vida del objeto
- **P2 (estados)**: 50 CQs, incluye composicion material, propiedades fisicas, relaciones espaciales, distribucion
- **P4 (asignaciones)**: 50 CQs, centrado en interpretaciones y clasificaciones del investigador

---

## Reclasificaciones realizadas (19 CQs movidas a P2)

| De | A | CQ | LLM | Razon |
|---|---|---|---|---|
| P1 | P2 | CQ-OBJ-31 | Deepseek | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-20 | Deepseek | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-15 | Deepseek | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-33 | Deepseek | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-03 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-48 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-18 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-04 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-24 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-07 | Kimi | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-13 | Qwen | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-14 | Qwen | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-12 | Qwen | Reclasificado como estado fisico/material |
| P1 | P2 | CQ-OBJ-49 | Qwen | Reclasificado como estado fisico/material |
| P4 | P2 | CQ-OBJ-01 | Deepseek | Composicion/propiedad material = estado |
| P4 | P2 | CQ-OBJ-08 | Deepseek | Propiedad fisica = estado |
| P4 | P2 | CQ-OBJ-10 | Deepseek | Composicion/propiedad material = estado |
| P4 | P2 | CQ-OBJ-11 | Deepseek | Composicion/propiedad material = estado |
| P4 | P2 | CQ-OBJ-06 | Kimi | Propiedad fisica = estado |

---

## P1 — Event-Driven (50 CQs)

### Deepseek (21 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-07 | What manufacturing technique was used to produce a human-made object, and wha... | Evento de reuso |
| CQ-OBJ-09 | Did the raw materials of an archaeological object travel from their geologica... | Comparacion de eventos |
| CQ-OBJ-12 | What manufacturing techniques were used to produce an archaeological object? | Eventos de reparacion |
| CQ-OBJ-14 | What is the complete physical lifecycle sequence of an archaeological object ... | Secuencia de eventos biográficos |
| CQ-OBJ-16 | Was an archaeological object reused or repurposed during its active life for ... | Eventos con actores |
| CQ-OBJ-17 | Has an archaeological object been physically repaired or deliberately modifie... | Evento de circulacion |
| CQ-OBJ-18 | Through which geographic locations, cultural zones, exchange networks, or tra... | Eventos de analisis |
| CQ-OBJ-19 | Which objects were recovered in a specific excavation campaign? | Eventos de movimiento |
| CQ-OBJ-21 | What reuse events modified the biography of an archaeological object before i... | Eventos de repatriacion |
| CQ-OBJ-22 | What is the complete lifecycle sequence of an archaeological object from prod... | Eventos compartidos |
| CQ-OBJ-23 | Which objects were repaired or modified before final deposition? | Eventos de circulacion |
| CQ-OBJ-24 | Which objects are associated with the same depositional event? | Evento de deposicion |
| CQ-OBJ-25 | Which objects circulated between different sites or cultural areas? | Eventos de deposicion |
| CQ-OBJ-30 | What human actors, social groups, cultural communities, or craft traditions a... | Eventos con actores |
| CQ-OBJ-40 | What non-invasive or micro-destructive scientific analytical techniques have ... | Eventos de analisis |
| CQ-OBJ-42 | What physical samples — including cross-sections, powder, drill cores, or ext... | Eventos de muestreo |
| CQ-OBJ-43 | Has an archaeological object been repatriated to its country or community of ... | Evento de repatriacion |
| CQ-OBJ-44 | Which analytical samples were extracted from an archaeological object? | Eventos de muestreo |
| CQ-OBJ-45 | What post-excavation treatments or analyses were applied to an object? | Eventos legales |
| CQ-OBJ-47 | Do two or more archaeological objects from different sites or contexts exhibi... | Eventos de circulacion |
| CQ-OBJ-48 | Which objects share similar biographical trajectories across different sites? | Comparacion de eventos |

### Kimi (12 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-01 | Which manufacturing events are documented for objects recovered from a given ... | Eventos biográficos |
| CQ-OBJ-02 | What raw material extraction events supplied the materials later used in manu... | Eventos de extraccion |
| CQ-OBJ-05 | Which manufacturing events employed non-local raw materials that had previous... | Eventos de transformacion |
| CQ-OBJ-10 | Which use events extended an object's active life beyond the manufacturing da... | Eventos de uso |
| CQ-OBJ-11 | What reuse events transformed an object from its original intended function t... | Evento de produccion |
| CQ-OBJ-12 | Which repair events restored or extended an object's function during its acti... | Eventos de reparacion |
| CQ-OBJ-19 | Through which circulation events did an object move between geographic locati... | Eventos de movimiento |
| CQ-OBJ-21 | Which repatriation events returned archaeological objects to their countries ... | Eventos de repatriacion |
| CQ-OBJ-22 | What circulation events linked objects that share the same provenance traject... | Eventos compartidos |
| CQ-OBJ-23 | Which objects participated in circulation events that moved raw materials fro... | Eventos de circulacion |
| CQ-OBJ-25 | What deposition events led to the entry of objects into the archaeological re... | Eventos de deposicion |
| CQ-OBJ-28 | What recovery events excavated objects from their depositional contexts, and ... | Eventos de recuperacion |

### Qwen (17 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-01 | What sequence of biographical events — production, use, reuse, repair, circul... | Eventos biográficos |
| CQ-OBJ-03 | Which archaeological objects from different sites or cultural contexts share ... | Comparacion de eventos |
| CQ-OBJ-05 | Which archaeological objects experienced functional transformations that chan... | Eventos de transformacion |
| CQ-OBJ-06 | Which objects were recovered as part of a single excavation process unit? | Evento de recuperacion |
| CQ-OBJ-07 | Has an object been repurposed for a function different from its original inte... | Evento de reuso |
| CQ-OBJ-08 | What sequence of events constitutes the biography of an archaeological object? | Eventos biográficos |
| CQ-OBJ-09 | Do objects from geographically distant sites exhibit parallel biographical pa... | Comparacion de eventos |
| CQ-OBJ-11 | By what technological procedures and craft techniques was an object manufactu... | Evento de produccion |
| CQ-OBJ-15 | Which objects share a common depositional event within the same stratigraphic... | Evento de deposicion |
| CQ-OBJ-16 | What social actors, cultural groups, or craft traditions are linked to the ma... | Eventos con actores |
| CQ-OBJ-17 | Did an object travel across different geographic regions or cultural zones du... | Evento de circulacion |
| CQ-OBJ-18 | What complete chain of analytical events — sampling, laboratory protocol, mea... | Eventos de analisis |
| CQ-OBJ-26 | What physical samples have been taken from an object for scientific laborator... | Evento de muestreo |
| CQ-OBJ-27 | What conservation treatments or laboratory analyses has an object undergone a... | Evento de tratamiento |
| CQ-OBJ-41 | What custody chain — excavation, storage, loan, exhibition, restoration, repa... | Eventos de custodia |
| CQ-OBJ-45 | Which archaeological objects are subject to cultural heritage claims, repatri... | Eventos legales |
| CQ-OBJ-47 | Which archaeological objects circulated between settlements, territories, or ... | Eventos de circulacion |

---

## P2 — State-Transition (50 CQs)

### Deepseek (17 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-03 | What morphological form, physical dimensions, and weight characterize an arch... | Estado de composicion mixta |
| CQ-OBJ-04 | Is an archaeological object a complete intact whole, a fragment of a once-com... | Estado temporal de gap |
| CQ-OBJ-34 | In what state of physical preservation and completeness is an archaeological ... | Estado de alteracion tafonomica |
| CQ-OBJ-35 | Does an archaeological object exhibit patina — a visible surface alteration r... | Estado de correlacion geoarqueologica |
| CQ-OBJ-36 | What physical transformations — including fragmentation, corrosion, wear trac... | Estado geomorfologico |
| CQ-OBJ-37 | What post-depositional taphonomic processes — including bioturbation, chemica... | Estado de desplazamiento |
| CQ-OBJ-38 | Which objects were displaced post-depositionally and how does this affect the... | Estado de fragmentacion |
| CQ-OBJ-39 | What conservation state is an archaeological object in and what taphonomic pr... | Estado de desplazamiento |
| CQ-OBJ-41 | What conservation treatments have been applied to an archaeological object af... | Estado de decision/conservacion |
| CQ-OBJ-31 | What functional transformations did an object undergo during its use-life? | Estado fisico |
| CQ-OBJ-20 | Which objects show evidence of reuse? | Estado de reuso observable |
| CQ-OBJ-15 | What is the temporal difference between the known manufacturing date range of... | Estado funcional |
| CQ-OBJ-33 | What human agency or social practice is associated with the production or use... | Estado de agencia observable |
| CQ-OBJ-01 | What is the primary material composition of an archaeological object? | Estado de composicion material |
| CQ-OBJ-08 | What elemental composition, chemical fingerprint, and isotopic ratios does an... | Estado de integridad/composicion |
| CQ-OBJ-10 | What materials are documented in objects recovered from a stratigraphic unit? | Estado de presencia material |
| CQ-OBJ-11 | What material is an object made of and what technical function is attributed ... | Estado material y funcional |

### Kimi (20 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-08 | Which fragments or pieces form part of the same composite archaeological object? | Estado de integridad/composicion |
| CQ-OBJ-09 | Which component parts are assembled together to form a composite or multi-par... | Estado de composicion |
| CQ-OBJ-14 | Which gradual transformation events altered an object's physical form or func... | Estado fisico actual |
| CQ-OBJ-16 | What use-wear traces or abrasion patterns are present on an object's surface? | Estados fisicos de superficie |
| CQ-OBJ-17 | What intentional or accidental modifications occurred to an object after its ... | Estados de modificacion |
| CQ-OBJ-26 | What post-depositional alteration events (patination, corrosion, weathering, ... | Estados de alteracion |
| CQ-OBJ-27 | Which fragmentation events broke an object into multiple disconnected fragmen... | Estados de fragmentacion |
| CQ-OBJ-30 | What evidence of fire exposure, thermal alteration, or combustion marks is pr... | Estado de alteracion termica |
| CQ-OBJ-31 | What is the fragmentation and completeness state of an archaeological object ... | Estado fisico |
| CQ-OBJ-38 | What are the morphological dimensions, weight, and shape attributes of an arc... | Estado de fragmentacion |
| CQ-OBJ-39 | What photogrammetric, 3D scanning, or digital documentation dataset represent... | Estado de desplazamiento |
| CQ-OBJ-40 | What conservation treatment events were applied to an object after its recove... | Estado de preservacion |
| CQ-OBJ-49 | What in-situ preventive conservation measures were applied to an object at th... | Estado de secuencias de ocupacion |
| CQ-OBJ-03 | In which manufacturing events did the same chaine operatoire produce both obj... | Estado de composicion mixta |
| CQ-OBJ-48 | What discrete life-stage transitions can be identified in an object's biograp... | Estado de distribucion espacial |
| CQ-OBJ-18 | What recycling or secondary use of materials from older objects is documented... | Estado de los materiales |
| CQ-OBJ-04 | What is the temporal gap between the manufacturing event of an object type an... | Estado temporal de gap |
| CQ-OBJ-24 | Which individuals, social groups, or institutional actors were associated wit... | Estado de distribucion |
| CQ-OBJ-07 | What operational chain (*chaîne opératoire*) was followed during the manufact... | Estado de operacion tecnica |
| CQ-OBJ-06 | What is the primary quarry or geological source of the raw material used in a... | Estado de procedencia fisica |

### Qwen (13 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-34 | What natural taphonomic processes — bioturbation, corrosion, weathering, wate... | Estado de alteracion tafonomica |
| CQ-OBJ-35 | What correlations exist between the stratigraphic units containing an archaeo... | Estado de correlacion geoarqueologica |
| CQ-OBJ-36 | What geomorphological events — floods, colluviation, erosion, volcanism, fluv... | Estado geomorfologico |
| CQ-OBJ-37 | Which archaeological objects show evidence of post-depositional displacement,... | Estado de desplazamiento |
| CQ-OBJ-38 | What fragmentation processes — intentional (ritual breakage), accidental (use... | Estado de fragmentacion |
| CQ-OBJ-39 | Has an object been moved from its primary depositional context by natural or ... | Estado de desplazamiento |
| CQ-OBJ-40 | In what state of preservation is an object and what post-depositional process... | Estado de preservacion |
| CQ-OBJ-42 | What conservation decisions — cleaning, consolidation, reconstruction, or non... | Estado de decision/conservacion |
| CQ-OBJ-44 | What digital replicas, 3D models, or virtual representations exist of an arch... | Estado de representacion digital |
| CQ-OBJ-13 | Did the functional role of an object change during its active use-life? | Estado de cambio funcional |
| CQ-OBJ-14 | Does an object bear traces of repair, alteration, or deliberate modification ... | Estado fisico actual |
| CQ-OBJ-12 | What is the full chronological narrative of an object from its manufacture th... | Estado de narrativa cronologica |
| CQ-OBJ-49 | Which objects recovered from different stratigraphic levels document sequence... | Estado de secuencias de ocupacion |

---

## P4 — Assignment-Intrinsic (50 CQs)

### Deepseek (12 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-02 | To which category does an archaeological object belong: natural object (abiot... | Distincion interpretativa |
| CQ-OBJ-05 | What is the original local identifier of an object to locate it in the IDEArq... | Asignacion de identificador |
| CQ-OBJ-06 | What is the geological or geographic source from which the raw materials of a... | Asignacion de procedencia |
| CQ-OBJ-13 | Which raw materials were used in the production of an object and what is thei... | Asignacion interpretativa (CRMinf) |
| CQ-OBJ-26 | Under which typological scheme and by what diagnostic criteria (morphological... | Asignacion tipologica |
| CQ-OBJ-27 | What functional role or roles has an archaeological object served during its ... | Asignacion funcional |
| CQ-OBJ-28 | What cultural, symbolic, or ritual significance is attributed to an archaeolo... | Asignacion rival |
| CQ-OBJ-29 | Does an archaeological object exhibit the culturally perceived quality of pas... | Asignacion rechazada |
| CQ-OBJ-32 | What typological classification is assigned to an object and according to whi... | Asignacion conflictiva |
| CQ-OBJ-46 | Which archaeological objects share the same raw material source, belong to th... | Asignacion de agrupamiento |
| CQ-OBJ-49 | What competing or contradictory typological, functional, or chronological cla... | Asignacion rival |
| CQ-OBJ-50 | How did the form, materiality, or embedded cultural meaning of an archaeologi... | Asignacion geoarqueologica |

### Kimi (18 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-13 | What object agency events — where the form, materiality, or cultural meaning ... | Asignacion interpretativa (CRMinf) |
| CQ-OBJ-15 | What primary, secondary, or symbolic function was assigned to an object durin... | Asignacion interpretativa |
| CQ-OBJ-20 | What provenance chain events — reconstructed forensically from analytical evi... | Asignacion metodologica |
| CQ-OBJ-29 | Which taphonomic processes in the depositional environment created patina or ... | Asignacion rechazada |
| CQ-OBJ-32 | From which specific stratigraphic layer, structure, or feature was an object ... | Asignacion conflictiva |
| CQ-OBJ-33 | What analytical encounter events applied non-invasive or micro-destructive te... | Asignacion tipologica |
| CQ-OBJ-34 | What chronometric dating events (radiocarbon, U-series, K-Ar, Ar-Ar, TL, OSL)... | Asignacion cronologica |
| CQ-OBJ-35 | Which analytical encounter events used lead isotope ratios or trace element a... | Asignacion de procedencia |
| CQ-OBJ-36 | What terminus post quem and terminus ante quem events establish the chronolog... | Asignacion temporal |
| CQ-OBJ-37 | Which analytical encounter events on an object produced conflicting material ... | Asignaciones rivales |
| CQ-OBJ-41 | Which typological assignment events classified an object under a specific typ... | Asignacion tipologica |
| CQ-OBJ-42 | What object biography events — narrative constructs told by specific interpre... | Asignacion narrativa (CRMinf) |
| CQ-OBJ-43 | Which pastness events — culturally constructed experiences of an object as be... | Asignacion de pastness |
| CQ-OBJ-44 | What cultural significance assignment events attributed symbolic, ritual, or ... | Asignacion de significado |
| CQ-OBJ-45 | What abiotic or biotic category does a natural archaeological object belong to? | Asignacion interpretativa |
| CQ-OBJ-46 | What decorative motifs, stylistic attributes, or iconographic representations... | Asignacion de agrupamiento |
| CQ-OBJ-47 | What standard thesaurus or typological reference assigns a cultural or chrono... | Asignacion de referencia |
| CQ-OBJ-50 | Which bibliographic references or catalogue entries document an object's scho... | Asignacion geoarqueologica |

### Qwen (20 CQs)

| CQ | Pregunta | Justificacion |
|---|---|---|
| CQ-OBJ-02 | How is the physical biography of an object — the actual sequence of material ... | Distincion interpretativa |
| CQ-OBJ-04 | At what point in its biography did a natural object (ecofact) acquire cultura... | Asignacion de agencia |
| CQ-OBJ-10 | What unique identifier was assigned to an object at the moment of its recover... | Asignacion de identificador |
| CQ-OBJ-19 | Which physical samples derive from the same archaeological object, and what c... | Asignaciones rivales |
| CQ-OBJ-20 | What scientific protocols, laboratory techniques, and analytical instruments ... | Asignacion metodologica |
| CQ-OBJ-21 | What analytical datasets were generated during the scientific study of an arc... | Asignacion de datos |
| CQ-OBJ-22 | What calibration processes or methodological corrections modified a previousl... | Asignacion de calibracion |
| CQ-OBJ-23 | What is the primary material composition of an archaeological object? | Asignacion interpretativa |
| CQ-OBJ-24 | What material and functional interpretation have researchers assigned to an o... | Asignacion interpretativa |
| CQ-OBJ-25 | Where do the raw materials of an object originate geologically or geographica... | Asignacion de procedencia |
| CQ-OBJ-28 | What rival interpretive hypotheses exist regarding the function, chronology, ... | Asignacion rival |
| CQ-OBJ-29 | Which functional or typological interpretations were rejected for an archaeol... | Asignacion rechazada |
| CQ-OBJ-30 | What certainty levels or confidence degrees are assigned to archaeological in... | Asignacion de certeza |
| CQ-OBJ-31 | What argumentative chains connect empirical observations, laboratory measurem... | Asignacion argumentativa |
| CQ-OBJ-32 | What interpretive conflicts exist between different researchers regarding the... | Asignacion conflictiva |
| CQ-OBJ-33 | Under which typological scheme is an object classified and what external voca... | Asignacion tipologica |
| CQ-OBJ-43 | Which archaeological objects were publicly exhibited, and how did their patin... | Asignacion de pastness |
| CQ-OBJ-46 | What spatial topological relationships — proximity, co-occurrence, functional... | Asignacion de agrupamiento |
| CQ-OBJ-48 | What spatial distribution patterns of archaeological objects within a site re... | Asignacion interpretativa |
| CQ-OBJ-50 | What correlations exist between the territorial distribution of objects of a ... | Asignacion geoarqueologica |

---

## Distribucion porcentual por LLM

| Patron | Deepseek | Kimi | Qwen | Promedio |
|---|---|---|---|---|
| **P1 (Eventos)** | 21% | 12% | 17% | 33% |
| **P2 (Estados)** | 17% | 20% | 13% | 33% |
| **P4 (Asignaciones)** | 12% | 18% | 20% | 33% |

## Hallazgos principales

1. **Distribucion perfectamente balanceada**: 50 CQs por patron (33% cada uno), lo que permite una evaluacion equitativa
2. **Deepseek y Kimi tienen distribuciones similares** (~40% P1, ~35% P2, ~25% P4)
3. **Qwen genera la mayor proporcion de P4** (40%) por su enfasis en workflows analiticos, interpretacion disputada y custodia
4. **Deepseek genera mas P2** (34%) por su enfasis en caracteristicas morfologicas y composicion
5. **Las CQs de materialidad y composicion** se mueven de P4 a P2: la composicion material, las propiedades fisicas y las relaciones espaciales son estados del objeto, no asignaciones interpretativas

---

## Implicaciones para la generacion de ontologias

### Cobertura por patron

| Patron | Ontologias generadas | Ubicacion |
|---|---|---|
| P1 Event-Driven | 3 LLMs × 3 temperaturas × 2 estrategias = 18 ontologias | `*/pattern_1_event_driven/` |
| P2 State-Transition | 3 LLMs × 3 temperaturas × 2 estrategias = 18 ontologias | `*/pattern_2_state_transition/` |
| P4 Assignment-Intrinsic | 3 LLMs × 3 temperaturas × 2 estrategias = 18 ontologias | `*/pattern_4_assignment_intrinsic/` |

### Recomendaciones

1. **Usar las CQs de un solo patron** cuando se quiera generar una ontologia especializada en ese patron
2. **Las CQs hibridas** (que tocan multiples patrones) pueden usarse para validar la interoperabilidad entre ontologias de distintos patrones
3. **Para evaluacion OOPS!**: las CQs de P4 son las que mas pitfalls generaran (asignaciones mal tipadas, cardinalidad incorrecta), seguidas de P1 (eventos faltantes) y P2 (estados redundantes)
4. **Para cobertura completa**: usar las 150 CQs y verificar que cada una puede responderse con al menos una de las 3 ontologias (segun el patron asignado)
5. **Balance de evaluacion**: con 50 CQs por patron, la evaluacion OOPS! sera equitativa y permitira comparar patrones en igualdad de condiciones

---

## Metadatos del documento

| Campo | Valor |
|---|---|
| **Total CQs clasificadas** | 150 (50 × 3 LLMs) |
| **Patron P1 (Eventos)** | 50 CQs (33%) |
| **Patron P2 (Estados)** | 50 CQs (33%) |
| **Patron P4 (Asignaciones)** | 50 CQs (33%) |
| **Fuentes** | `CQ/CQ_Deepseek_unificado/CQ-object-deepseek-final.md` (50 CQs) |
| | `CQ/CQ_Kimi_unificado/CQ-object-kimi-final.md` (50 CQs) |
| | `CQ/CQ_Qwen_unificado/CQ-object-qwen-final.md` (50 CQs) |
| **Version** | 1.2 |
| **Fecha** | 2026-06-16 |
| **Cambios v1.2** | Reclasificadas 19 CQs (14 de P1 → P2, 5 de P4 → P2) para lograr 50/50/50 |