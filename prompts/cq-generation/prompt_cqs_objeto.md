# Prompt de generación de CQs — Objeto Arqueológico Qwen3.7-plus


|                        |                                              |
| ---------------------- | -------------------------------------------- |
| Salida real del piloto | `CQ/CQ_Qwen3.7plus/CQ-object-qwen3.7plus.md` |


## Prompt_v1

```text
Eres un experto en teoría arqueológica, ingeniería de ontologías y diseño de
ontologías guiado por preguntas de competencia.

## Materiales de entrada

### A. Corpus de dominio (data_markdown/)
- data_markdown/articulosJuan/
- data_markdown/brief_objeto_arqueologico.md          
- data_markdown/analisis_gapOntologicoGPT.md
- data_markdown/Analisis-articulosObjeto.md
- data_markdown/INFORME modelo ontologico_ARIADNE.md
- data_markdown/ontologyLLM.md
- data_markdown/modelo idearq_v3b.md


### B. Ontologías de referencia (ontologies_docs/)
- ontologies_docs/owl/CRMarchaeo_v2.1.1.owl
- ontologies_docs/ttl/geosparql.ttl
- ontologies_docs/ttl/time-ontology.ttl

Especificaciones PDF:
- ontologies_docs/pdfs/cidoc_crm_version_7.3.2.pdf
- ontologies_docs/pdfs/CRMarchaeo_v2.1.1(site).pdf
- ontologies_docs/pdfs/CRMsci-v3.1.pdf
- ontologies_docs/pdfs/CRMhs_Ontology_Specification_v1.2.pdf
- ontologies_docs/pdfs/AO-Cat_V1.2.2.pdf
- ontologies_docs/pdfs/geosparql-v1.1.pdf
- ontologies_docs/html/OGC 16-008_ GeoSciML v4.1.htm


## Tarea

Genera un conjunto independiente de 30 Preguntas de Competencia (CQ) para el
dominio del Objeto Arqueológico.

Las preguntas deben ser nuevas y generadas desde cero. No reutilices preguntas
de conjuntos de CQs anteriores generados por otros LLM.

Organiza las 30 CQs en tres patrones de modelado ontológico:

1. P1 — Event-Driven: ¿qué ocurrió?
   Eventos de la biografía del objeto: aprovisionamiento, fabricación, uso,
   mantenimiento, reparación, reutilización, reciclaje, circulación, descarte,
   deposición, tafonomía, recuperación, conservación, trayectorias biográficas.

2. P2 — State-Transition: ¿cómo es el objeto?
   Estados físicos, materiales, espaciales y temporales: composición,
   materialidad, relojes internos, fragmentación, deterioro, pastness,
   affordances, morfometría, partonomía, color, preservación, cambios de estado.

3. P4 — Assignment-Intrinsic: ¿qué sabemos del objeto?
   Asignaciones interpretativas y epistémicas: tipología, cronología, función,
   asignación de material, rasgos significativos, grupos compositivos,
   significado cultural, agencia, universo estilístico, hipótesis, multivocalidad.

Genera exactamente:

- 10 CQs para P1
- 10 CQs para P2
- 10 CQs para P4

Cada CQ debe:

- Abordar un concepto arqueológico distinto.
- Ser respondible por una futura ontología compatible con CIDOC CRM.
- No ser una consulta de base de datos genérica.
- Reflejar la distinción entre objetos físicos, eventos, estados,
  observaciones, interpretaciones y asignaciones.
- Considerar la interoperabilidad con CIDOC CRM, CRMarchaeo, CRMsci,
  CRMinf, CRMhs, AO-Cat, GeoSPARQL, OWL-Time, GeoSciML, PROV-O y SKOS.
- Identificar cuándo un concepto requiere una extensión arqo: nueva en lugar
  de forzar la reutilización inadecuada de una clase CRM existente.

Para cada CQ, proporciona exactamente esta estructura:

## CQ-OBJ-NN

**Question:** [la pregunta de competencia]

- **Ontology modules required:** [módulos]
- **Possible ontology reuse:** [clases/propiedades relevantes de las
  ontologías de referencia]
- **Pattern:** P1 | P2 | P4


No generes código OWL/Turtle. Genera únicamente las preguntas de competencia
y sus metadatos.
```

## Prompt_v2 (14-09-26, rev. 16-09-26)

> **Revisión 16-09-26:** incorporada la corrección del arqueólogo. Se **elimina
> la oposición biótico/abiótico** en artefactos y ecofactos, y se fijan **tres
> dimensiones simétricas** para ambos: materialidad, morfología y funcionalidad.
> El origen biótico o abiótico pasa a ser un atributo de la **materialidad**, no
> una clase. El prompt mantiene **dos patrones** (P1 y P2): las asignaciones
> interpretativas y epistémicas se resuelven dentro de P2.

```text
Eres un experto en teoría arqueológica, ingeniería de ontologías y diseño de
ontologías guiado por preguntas de competencia.

## Materiales de entrada

### A. Corpus de dominio (data_markdown/)
- data_markdown/articulosJuan/
- data_markdown/brief_objeto_arqueologico.md          
- data_markdown/analisis_gapOntologicoGPT.md
- data_markdown/Analisis-articulosObjeto.md
- data_markdown/INFORME modelo ontologico_ARIADNE.md
- data_markdown/ontologyLLM.md
- data_markdown/modelo idearq_v3b.md


## Modelo conceptual del objeto arqueológico

Considera que el objeto arqueológico está caracterizado por el pasado y que vas
a modelar su esencia. Distingue dos clases fundamentales:

- **Artefacto** — objeto modificado o producido por acción humana. Incluye
  objetos mixtos que se comportan como artefactos (por ejemplo, productos
  textiles) y las pinturas rupestres.
- **Ecofacto** — objeto no modificado por acción humana pero con significado
  arqueológico. Incluye restos vegetales y animales (esqueleto completo o
  partes, semillas) y objetos minerales no modificados trasladados de su punto
  de origen.

### Regla: no distingas biótico / abiótico

**No crees clases ni subclases basadas en la oposición biótico/abiótico**, ni
para artefactos ni para ecofactos. Esa distinción es interna a cada clase y se
expresa a través de la materialidad: **es la materialidad la que da cuenta del
origen biótico o abiótico de la materia prima**.

- Una cuchara de hueso es un **artefacto de materia prima biótica**.
- Una piedra exótica es un **ecofacto de materia prima abiótica**.

Este criterio evita duplicar clases innecesariamente (navaja de Ockham) y
resuelve los casos mixtos sin ambigüedad: un puñal de cobre con enmangue de
hueso es un artefacto, y su doble origen se expresa en su materialidad, no en
clases distintas.

### Tres dimensiones simétricas

Las dimensiones de artefactos y ecofactos son **simétricas y se reducen a tres**:

1. **Materialidad** — materia prima, su origen (biótico o abiótico) y sus
   propiedades físicas y químicas.
2. **Morfología** — forma y dimensiones: longitud máxima, anchura máxima, peso.
   En ecofactos incluye la identificación anatómica (por ejemplo, "fragmento
   distal de tibia", "concha de caracol").
3. **Funcionalidad** — uso o función (por ejemplo, restos de cocina, decoración
   de un túmulo megalítico, pigmento rojo de uso funerario).

La **taxonomía** de un ecofacto (por ejemplo, "Oveja (Ovis aries)", "cuarcita
blanca", "Hematites (Fe₂O₃)") es la expresión clasificatoria de su morfología y
su materialidad. La **tipología** de un artefacto cumple el papel equivalente.
No constituyen una cuarta dimensión: se resuelven dentro de las tres anteriores.

## Tarea

Genera un conjunto independiente de 30 Preguntas de Competencia (CQ) para el
dominio del Objeto Arqueológico.

Las preguntas deben ser nuevas y generadas desde cero. No reutilices preguntas
de conjuntos de CQs anteriores generados por otros LLM.

Organiza las 30 CQs en dos patrones de modelado ontológico:

1. P1 — Event-Driven: ¿qué ocurrió?
   Eventos de la biografía del objeto: aprovisionamiento, fabricación, uso,
   mantenimiento, reparación, reutilización, reciclaje, circulación, descarte,
   deposición, tafonomía, recuperación, conservación, trayectorias biográficas.

2. P2 — State-Transition: ¿cómo es el objeto y qué sabemos de él?
   Estados físicos, materiales y morfológicos: materialidad y composición,
   morfología y dimensiones, identificación anatómica y taxonómica,
   fragmentación, deterioro, pátina, color, cambios de estado (relojes internos,
   corrosión, etc.) y preservación.
   Asignaciones interpretativas y epistémicas: tipología, función, asignación de
   material, rasgos significativos, grupos compositivos, significado cultural,
   cronología, asignación cronocultural, hipótesis rivales y multivocalidad.

Divide cada patrón en subgrupos temáticos. Cada CQ debe:

- Abordar un concepto arqueológico distinto.
- Poder ser respondida por una futura ontología compatible con CIDOC CRM.
- No ser una consulta de base de datos genérica.
- Reflejar la distinción entre objetos físicos, eventos, estados,
  observaciones, interpretaciones y asignaciones.
- Considerar la interoperabilidad con CIDOC CRM, CRMarchaeo, CRMsci,
  CRMinf, CRMhs, AO-Cat, GeoSPARQL, OWL-Time, GeoSciML, PROV-O y SKOS.
- Identificar cuándo un concepto requiere una extensión arqo: nueva en lugar
  de forzar la reutilización inadecuada de una clase CRM existente.
- No asumir clases biótico/abiótico: expresa el origen de la materia prima a
  través de la materialidad.

Para cada CQ, proporciona exactamente esta estructura:

## CQ-OBJ-NN

**Question:** [la pregunta de competencia]

- **Ontology modules required:** [módulos]
- **Possible ontology reuse:** [clases/propiedades relevantes de las
  ontologías de referencia]
- **Pattern:** P1 | P2


No generes código OWL/Turtle. Genera únicamente las preguntas de competencia
y sus metadatos.
```

## Prompt_v3 — Segunda vuelta, cobertura de lagunas (16-09-26)

> **Objetivo:** generar CQs **nuevas que se suman** a las 30 ya existentes, no un
> conjunto desde cero. El modelo analiza qué falta por preguntar y decide cuántas
> necesita en cada patrón. **No tiene que haber el mismo número en P1 y en P2**:
> pueden coincidir si sale así, pero no es un requisito.
> **Temperatura:** 0.1 (estabilidad y consistencia por encima de la exploración).

```text
Eres un experto en teoría arqueológica, ingeniería de ontologías y diseño de
ontologías guiado por preguntas de competencia.

## Materiales de entrada

### A. Corpus de dominio (data_markdown/)
- data_markdown/articulosJuan/
- data_markdown/brief_objeto_arqueologico.md          
- data_markdown/analisis_gapOntologicoGPT.md
- data_markdown/Analisis-articulosObjeto.md
- data_markdown/INFORME modelo ontologico_ARIADNE.md
- data_markdown/ontologyLLM.md
- data_markdown/modelo idearq_v3b.md

### B. CQs ya existentes (primera vuelta, 30 CQs)
- CQ/CQ_Qwen3.7plus/CQ-object-qwen3.7plus.md

Revisa ese archivo antes de generar nada. Bajo el modelo de dos patrones, ese
conjunto cubre:
- P1 — Event-Driven: 10 CQs (eventos de la biografía del objeto)
- P2 — State-Transition: 20 CQs (10 de estados físicos y materiales + 10 de
  asignaciones interpretativas y epistémicas)


## Modelo conceptual del objeto arqueológico

Considera que el objeto arqueológico está caracterizado por el pasado y que vas
a modelar su esencia. Distingue dos clases fundamentales:

- **Artefacto** — objeto modificado o producido por acción humana. Incluye
  objetos mixtos que se comportan como artefactos (por ejemplo, productos
  textiles) y las pinturas rupestres.
- **Ecofacto** — objeto no modificado por acción humana pero con significado
  arqueológico. Incluye restos vegetales y animales (esqueleto completo o
  partes, semillas) y objetos minerales no modificados trasladados de su punto
  de origen.

### Regla: no distingas biótico / abiótico

**No crees clases ni subclases basadas en la oposición biótico/abiótico**, ni
para artefactos ni para ecofactos. Esa distinción es interna a cada clase y se
expresa a través de la materialidad: **es la materialidad la que da cuenta del
origen biótico o abiótico de la materia prima**.

- Una cuchara de hueso es un **artefacto de materia prima biótica**.
- Una piedra exótica es un **ecofacto de materia prima abiótica**.

Este criterio evita duplicar clases innecesariamente (navaja de Ockham) y
resuelve los casos mixtos sin ambigüedad: un puñal de cobre con enmangue de
hueso es un artefacto, y su doble origen se expresa en su materialidad, no en
clases distintas.

### Tres dimensiones simétricas

Las dimensiones de artefactos y ecofactos son **simétricas y se reducen a tres**:

1. **Materialidad** — materia prima, su origen (biótico o abiótico) y sus
   propiedades físicas y químicas.
2. **Morfología** — forma y dimensiones: longitud máxima, anchura máxima, peso.
   En ecofactos incluye la identificación anatómica (por ejemplo, "fragmento
   distal de tibia", "concha de caracol").
3. **Funcionalidad** — uso o función (por ejemplo, restos de cocina, decoración
   de un túmulo megalítico, pigmento rojo de uso funerario).

La **taxonomía** de un ecofacto (por ejemplo, "Oveja (Ovis aries)", "cuarcita
blanca", "Hematites (Fe₂O₃)") es la expresión clasificatoria de su morfología y
su materialidad. La **tipología** de un artefacto cumple el papel equivalente.
No constituyen una cuarta dimensión: se resuelven dentro de las tres anteriores.


## Tarea

Ya existe un conjunto de 30 CQs para el dominio del Objeto Arqueológico.
Tu trabajo es **ampliarlo**, no reemplazarlo: genera CQs nuevas que se sumen a
las existentes.

### Paso 1 — Análisis de lagunas

Identifica qué conceptos arqueológicos del modelo conceptual **no están
cubiertos** por las 30 CQs existentes. Enumera las lagunas agrupadas por patrón
(P1 y P2), indicando en cada caso qué dimensión o aspecto queda sin preguntar.

### Paso 2 — Generación

Genera el conjunto nuevo de CQs que cubra esas lagunas. Requisitos:

- Decide tú cuántas hacen falta
  en cada patrón a partir de las lagunas detectadas, y **justifica el número
  elegido** en una frase.
- **No repitas** ninguna pregunta existente, ni la reformules con otras
  palabras. Si un concepto ya está cubierto, no genera otra CQ para él.
- Numera las nuevas CQs a partir de **CQ-OBJ-31**, continuando la serie.
- **Temperatura 0.1:** prioriza estabilidad y consistencia sobre la exploración
  creativa. Sé preciso y conservador; evita conceptos especulativos o
  redundantes.

Cada CQ debe:

- Abordar un concepto arqueológico distinto y no cubierto previamente.
- Poder ser respondida por una futura ontología compatible con CIDOC CRM.
- No ser una consulta de base de datos genérica.
- Reflejar la distinción entre objetos físicos, eventos, estados,
  observaciones, interpretaciones y asignaciones.
- Considerar la interoperabilidad con CIDOC CRM, CRMarchaeo, CRMsci,
  CRMinf, CRMhs, AO-Cat, GeoSPARQL, OWL-Time, GeoSciML, PROV-O y SKOS.
- Identificar cuándo un concepto requiere una extensión arqo: nueva en lugar
  de forzar la reutilización inadecuada de una clase CRM existente.
- No asumir clases biótico/abiótico: expresa el origen de la materia prima a
  través de la materialidad.

Los patrones son **dos**:

1. **P1 — Event-Driven:** ¿qué ocurrió? Eventos de la biografía del objeto:
   aprovisionamiento, fabricación, uso, mantenimiento, reparación,
   reutilización, reciclaje, circulación, descarte, deposición, tafonomía,
   recuperación, conservación, trayectorias biográficas.

2. **P2 — State-Transition:** ¿cómo es el objeto y qué sabemos de él?
   Estados físicos, materiales y morfológicos: materialidad y composición,
   morfología y dimensiones, identificación anatómica y taxonómica,
   fragmentación, deterioro, pátina, color, cambios de estado y preservación.
   Asignaciones interpretativas y epistémicas: tipología, función, asignación de
   material, rasgos significativos, grupos compositivos, significado cultural,
   cronología, asignación cronocultural, hipótesis rivales y multivocalidad.

### Subgrupos temáticos

Cada CQ nueva debe quedar ubicada en un subgrupo temático. Estos son los
subgrupos existentes del conjunto de 30 CQs:

**P1 — Event-Driven**
- P1.1 Origen y fabricación
- P1.2 Vida útil y transformación
- P1.3 Fin del ciclo: depósito y recuperación
- P1.4 Actores y biografía

**P2 — State-Transition**
- P2.1 Composición y materialidad
- P2.2 Alteración y forma
- P2.3 Contexto físico
- P2.4 Modo de experiencia
- P2.5 Clasificación
- P2.6 Función
- P2.7 Significado y agencia
- P2.8 Conocimiento y evidencia

**Regla:** incluye cada CQ nueva en el subgrupo existente que le corresponda.
Si alguna laguna no encaja en ningún subgrupo existente, puedes **crear un
subgrupo nuevo**, justificando por qué los existentes no la cubren.

Para cada CQ, proporciona exactamente esta estructura:

## CQ-OBJ-NN

**Question:** [la pregunta de competencia]

- **Ontology modules required:** [módulos]
- **Possible ontology reuse:** [clases/propiedades relevantes de las
  ontologías de referencia]
- **Pattern:** P1 | P2
- **Subgroup:** [subgrupo existente o nuevo]

### Resumen final

Termina con:

- Número total de CQs nuevas generadas.
- Número por patrón.
- Justificación del número elegido.
- Lista de lagunas detectadas y qué CQ las cubre.
- Lista de subgrupos utilizados y, si los hay, los de nueva creación.

No generes código OWL/Turtle. Genera únicamente las preguntas de competencia
y sus metadatos.
```

