# Brief: Dominio Objeto Arqueológico

## 1. Conceptos Fundamentales

### 1.1 Objeto arqueológico — dualidad ontológica
El objeto arqueológico es simultáneamente **portador material** y **entidad proposicional**. No se define solo por su sustancia, sino por su *pastness* (pasado-idad): la cualidad experiencial de ser "del pasado" que emerge de pistas materiales (desgaste, pátina, corrosión). Un mismo portador físico puede transitar por múltiples identidades sociales a lo largo de su biografía (herramienta → reliquia → espécimen de museo).

### 1.2 Biografía del objeto (Object Biography)
Cadena de eventos y estados por los que un objeto pasa desde su producción hasta su recuperación e interpretación. Fases del ciclo de vida (modelo Schiffer):
- **Procurement** (aprovisionamiento de materia prima)
- **Manufacture** (fabricación)
- **Use** (uso primario)
- **Maintenance** (mantenimiento/reparación)
- **Discard** (descarte → refuse)
- **Post-depositional / taphonomic** (transformaciones naturales)
- **Recovery** (excavación/recuperación)
- **Conservation** (intervención post-recuperación)

Reutilización: *recycling* (retorno a manufactura) y *lateral cycling* (circulación entre contextos sociales sin cambio de función).

### 1.3 Materialidad
Concepto relacional y procesual que supera la dicotomía mente/materia. Cubre cuatro propiedades (Knappett 2012): dependiente (relaciones materiales), codependiente (relaciones sociales), independiente (vital), interdependiente (plural). Oscila entre "objeto" (categoría consciente) y "cosa" (entidad Heideggeriana con *readiness-to-hand* y *presence-at-hand*).

### 1.4 Contexto sistémico vs. contexto arqueológico (Schiffer 1972)
- **Systemic context**: condición de un elemento que participa en un sistema behavioral.
- **Archaeological context**: condición de materiales que han atravesado un sistema cultural y son objeto de investigación.
- **Refuse**: estado post-descarte. Distinguir *primary refuse* (descartado en lugar de uso), *secondary refuse* (transportado a otro lugar), *de facto refuse* (abandono sin descarte intencional).

### 1.5 Tipología y clasificación
- Agrupaciones monotéticas vs. análisis de sistemas de atributos (cluster analysis).
- Datación basada en *rasgos significativos* (significant features) en vez de tipos amplios.
- Grupos compositivos (*Leitlegierungen*) para objetos metálicos.
- Clasificación funcional vs. simbólica.

### 1.6 Agencia material y affordances
Las propiedades formales de un objeto "establecen reglas de uso" y "canalizan intenciones humanas" (Gibson: affordances; Hodder: entanglement). El objeto no es pasivo: estructura la interacción social.

### 1.7 Pasado-idad (pastness) y autenticidad
Cualidad experiencial que emerge de pistas materiales (huellas de desintegración). Emancipa la autenticidad de la edad medible. Puede ser "fingida" en el presente y seguir funcionando como signo autentificador.

### 1.8 Relojes internos (internal clocks)
Propiedades físicas o químicas medibles dentro de la sustancia del objeto que indican su edad relativa o grado de transformación (ej. pérdida de arsénico en cobre, oxidación). El tiempo como cambio físico interno, no solo como fecha absoluta externa.

### 1.9 Archivo arqueológico
Conjunto de registros (papel, digital, medios) conceptualizado como objeto arqueológico en sí mismo: es el nodo donde la inferencia humana transforma materia en evidencia.

---

## 2. Clases CIDOC CRM Relevantes

| URI | Descripción |
|-----|-------------|
| `crm:E1_CRM_Entity` | Raíz de todas las clases CIDOC CRM. |
| `crm:E2_Temporal_Entity` | Entidades con extensión temporal (eventos, períodos). |
| `crm:E4_Period` | Períodos históricos y arqueológicos (Edad del Bronce, etc.). |
| `crm:E5_Event` | Eventos discretos con inicio y fin (producción, uso, deposición). |
| `crm:E7_Activity` | Actividades humanas intencionales. |
| `crm:E12_Production` | Eventos de fabricación/creación de objetos. |
| `crm:E13_Attribute_Assignment` | Asignación de atributos (tipología, función, material). |
| `crm:E16_Measurement` | Mediciones cuantitativas (peso, dimensiones, composición). |
| `crm:E17_Type_Assignment` | Asignación de tipos (clasificación tipológica). |
| `crm:E18_Physical_Thing` | Cualquier entidad material persistente. |
| `crm:E19_Physical_Object` | Objetos físicos discretos y delimitados. |
| `crm:E20_Biological_Object` | Objetos con origen biológico. |
| `crm:E22_Human-Made_Object` | Objetos físicos producidos intencionalmente por humanos (artefactos portables). |
| `crm:E24_Physical_Human-Made_Thing` | Cualquier cosa material hecha por humanos (incluye estructuras, rasgos). |
| `crm:E25_Human-Made_Feature` | Rasgos producidos por humanos (cut, foso, muro). |
| `crm:E26_Physical_Feature` | Rasgos físicos observables (desgaste, pátina, decoración). |
| `crm:E27_Site` | Sitios arqueológicos como volúmenes 3D. |
| `crm:E44_Place_Appellation` | Nombres/lugares de referencia espacial. |
| `crm:E52_Time-Span` | Extensiones temporales (fechas, intervalos). |
| `crm:E53_Place` | Ubicaciones espaciales conceptuales. |
| `crm:E55_Type` | Tipos, categorías, clases (tipología, material, función). |
| `crm:E57_Material` | Materiales (cobre, cerámica, obsidiana, hueso). |
| `crm:E73_Information_Object` | Objetos de información (archivos, registros digitales). |
| `crm:E78_Curated_Holding` | Colecciones curadas (museos, depósitos). |
| `crm:E89_Propositional_Object` | Entidades proposicionales (hipótesis, biografías, narrativas). |

---

## 3. Clases CRMarchaeo Relevantes

| URI | Superclase | Descripción |
|-----|-----------|-------------|
| `crmarchaeo:A1_Excavation_Processing_Unit` | E12 + E64 + S1 + S4 | Unidad coherente de excavación (remoción + observación + documentación). |
| `crmarchaeo:A2_Stratigraphic_Volume_Unit` | A8 | Unidad de volumen estratigráfico (depósito con homogeneidad). Puede contener objetos. |
| `crmarchaeo:A3_Stratigraphic_Interface` | A8 | Superficie límite resultante de un evento de génesis/modificación estratigráfica. |
| `crmarchaeo:A4_Stratigraphic_Genesis` | A5 + S17 | Evento/proceso que produce unidades estratigráficas homogéneas (deposición, acumulación). |
| `crmarchaeo:A5_Stratigraphic_Modification` | S18 | Evento de modificación post-génesis de unidades estratigráficas (erosión, bioturbación). |
| `crmarchaeo:A6_Group_Declaration_Event` | E13 | Evento interpretativo que agrupa fragmentos dispersos como restos de una entidad física única. |
| `crmarchaeo:A7_Embedding` | A8 | Relación de embebido: objeto físico contenido dentro de una unidad de volumen con estabilidad relativa. |
| `crmarchaeo:A8_Stratigraphic_Unit` | S20 | Unidad estratigráfica: rasgo físico rígido resultante de un evento de génesis. |
| `crmarchaeo:A9_Archaeological_Excavation` | S4 | Excavación arqueológica coordinada (proyecto completo). |
| `crmarchaeo:A10_Excavation_Interface` | E25 + S20 | Superficie producida por una unidad de procesamiento de excavación (planum, perfil). |

---

## 4. Propiedades Relevantes

### 4.1 Propiedades CIDOC CRM

| URI | Dominio | Rango | Descripción |
|-----|---------|-------|-------------|
| `crm:P45_consists_of` | E18 | E57 | Un objeto está compuesto de un material. |
| `crm:P46_is_composed_of` | E18 | E18 | Una cosa física está compuesta de otras cosas físicas (partes). |
| `crm:P108_has_produced` | E12 | E24 | Un evento de producción ha creado un objeto. |
| `crm:P108i_was_produced_by` | E24 | E12 | Un objeto fue producido por un evento. |
| `crm:P12_occurred_in_the_presence_of` | E5 | E77 | Un evento ocurrió en presencia de un objeto. |
| `crm:P31_has_modified` | E11 | E24 | Una modificación alteró un objeto. |
| `crm:P141_assigned` | E13 | E1 | Una asignación atribuyó un valor a una cosa. |
| `crm:P2_has_type` | E1 | E55 | Una entidad tiene un tipo. |
| `crm:P44_has_condition` | E18 | E3 | Un objeto tiene un estado de conservación. |
| `crm:P45_consists_of` | E18 | E57 | Composición material. |
| `crm:P50_has_current_keeper` | E24 | E39 | Custodio actual del objeto. |
| `crm:P52_has_current_owner` | E24 | E39 | Propietario actual. |
| `crm:P53_has_former_or_current_location` | E18 | E53 | Ubicación actual o pasada. |
| `crm:P94_took_presence_of` | E4 | E2 | Un evento atestigua la existencia de una cosa. |
| `crm:P102_has_title` | E71 | E35 | Título/designación. |
| `crm:P127_has_broader_term` | E55 | E55 | Relación jerárquica entre tipos. |
| `crm:P128_carries` | E24 | E90 | Un objeto porta información/símbolo. |
| `crm:P130_shows_features_of` | E70 | E70 | Rasgos que muestran características de un período/tipo. |

### 4.2 Propiedades CRMarchaeo

| URI | Dominio | Rango | Descripción |
|-----|---------|-------|-------------|
| `crmarchaeo:AP1_produced` | A1 | S11 | Materia preservada de una excavación. |
| `crmarchaeo:AP2_discarded` | A1 | S11 | Materia descartada por excavación. |
| `crmarchaeo:AP3_investigated` | A9 | E27 | Sitio investigado por una excavación. |
| `crmarchaeo:AP4_produced_surface` | A1 | A10 | Superficie producida por excavación. |
| `crmarchaeo:AP5_removed_part_or_all_of` | A1 | A8 | Unidad estratigráfica removida por excavación. |
| `crmarchaeo:AP6_intended_to_approximate` | A1 | A3 | Interfaz estratigráfica que se pretendía aproximar. |
| `crmarchaeo:AP7_produced` | A4 | A8 | Unidad estratigráfica producida por génesis. |
| `crmarchaeo:AP8_disturbed` | A5 | A8 | Unidad estratigráfica perturbada por modificación. |
| `crmarchaeo:AP9_took_matter_from` | A4 | S10 | Materia incorporada desde un sustancial material. |
| `crmarchaeo:AP10_destroyed` | A1 | S22 | Segmento de materia destruido por excavación. |
| `crmarchaeo:AP11_has_physical_relation_to` | A8 | A8 | Relación física entre unidades estratigráficas (con AP11.1 has type: under, abuts, cuts, etc.). |
| `crmarchaeo:AP12_confines` | A3 | A2 | Interfaz que delimita un volumen estratigráfico. |
| `crmarchaeo:AP13_has_stratigraphic_relation_to` | A5 | A5 | Relación estratigráfica entre eventos (earlier, after, contemporary; con AP13.1 has type). |
| `crmarchaeo:AP15_is_or_contains_remains_of` | A2 | S10 | Volumen que es o contiene restos de un material. |
| `crmarchaeo:AP16_assigned_attribute_to` | A6 | E18 | Atribución en evento de declaración grupal. |
| `crmarchaeo:AP17_is_found_by` | A7 | S19 | Embebido encontrado en un encuentro. |
| `crmarchaeo:AP18_is_embedding_of` | A7 | E18 | Embebido contiene un objeto físico. |
| `crmarchaeo:AP19_is_embedding_in` | A7 | A2 | Embebido dentro de un volumen estratigráfico. |
| `crmarchaeo:AP21_contains` | A2 | E18 | Volumen contiene un objeto físico (atajo de AP18+AP19). |
| `crmarchaeo:AP22_is_equal_in_time_to` | E2 | E2 | Allen: equals. |
| `crmarchaeo:AP23_finishes` | E2 | E2 | Allen: finishes. |
| `crmarchaeo:AP24_starts` | E2 | E2 | Allen: starts. |
| `crmarchaeo:AP25_occurs_during` | E2 | E2 | Allen: during. |
| `crmarchaeo:AP26_overlaps_in_time_with` | E2 | E2 | Allen: overlaps. |
| `crmarchaeo:AP27_meets_in_time_with` | E2 | E2 | Allen: meets. |
| `crmarchaeo:AP28_occurs_before` | E2 | E2 | Allen: before. |
| `crmarchaeo:AP29_appears_in` | E55 | E4 | Tipo que aparece en un período (débil). |
| `crmarchaeo:AP30_restricted_to` | E55 | E4 | Tipo restringido exclusivamente a un período (fuerte). |
| `crmarchaeo:AP31_typical_for` | E55 | E4 | Tipo característico de un período (moderado). |
| `crmarchaeo:AP32_discarded_into` | A1 | S11 | Materia de excavación descartada en un montón. |

---

## 5. Patrones de Modelado

### 5.1 Event-centric pattern
Hechos arqueológicos como eventos, no como entidades estáticas. Cada fase de la vida del objeto es un evento (E5/E12/E7) con participantes, tiempo y lugar.

### 5.2 Stratigraphy-driven pattern
Eje semántico principal: unidades estratigráficas (A8), génesis (A4), interfaces (A3), secuencias (AP13). El objeto aparece subordinado al contexto.

### 5.3 Embedding pattern (A7)
Objeto embebido en volumen estratigráfico: `E18 → AP18i → A7 → AP19 → A2`. Shortcut: `A2 → AP21 → E18`.

### 5.4 Reification pattern
Para cualificar relaciones (material, función, tipología, cronología) se reifican como eventos de asignación (E13/E17) o como entidades proposicionales (E89). Permite capturar incertidumbre, multivocalidad y provenance del conocimiento.

### 5.5 Biography chain pattern
Cadena de eventos conectados al mismo objeto: `E22 → P108i → E12 (Production) → P12_occurred_in_the_presence_of → E22 → E7 (Use) → E9 (Move) → A4 (Deposition) → A1 (Recovery)`.

### 5.6 Observation vs. interpretation pattern
Separación epistemológica: `AP11` (relación física observada) vs. `AP13` (relación estratigráfica inferida). Problema: A1 mezcla proceso físico + observación + documentación.

### 5.7 Type-to-period pattern
Tres niveles de fuerza para vincular tipos con períodos:
- AP29 (weak: aparece en)
- AP31 (moderate: típico de)
- AP30 (strong: restringido a)

### 5.8 Internal clock pattern
Tiempo como transformación física interna medible (isótopos, oxidación, pérdida de elementos volátiles). Complementa E52 Time-Span.

### 5.9 Social persona transition pattern
Un portador físico transita por múltiples identidades proposicionales (E89): herramienta → reliquia → objeto de museo → fragmento reciclado.

---

## 6. Términos Clave (Glosario bilingüe)

| Español | English | Definición breve |
|---------|---------|------------------|
| objeto arqueológico | archaeological object | Entidad material recuperada de un contexto arqueológico. |
| biografía del objeto | object biography | Cadena completa de eventos/estados del objeto. |
| materialidad | materiality | Propiedades relacionales y procesuales de la materia en contexto cultural. |
| pasado-idad | pastness | Cualidad experiencial de ser "del pasado". |
| contexto sistémico | systemic context | Condición de un elemento participando en un sistema cultural. |
| contexto arqueológico | archaeological context | Condición de materiales tras atravesar un sistema cultural. |
| desecho primario | primary refuse | Descarte en el lugar de uso. |
| desecho secundario | secondary refuse | Descarte transportado a otro lugar. |
| desecho de facto | de facto refuse | Abandono sin descarte intencional. |
| aprovisionamiento | procurement | Adquisición de materia prima. |
| manufactura | manufacture | Fabricación del objeto. |
| uso | use | Empleo primario del objeto. |
| mantenimiento | maintenance | Reparación, conservación durante la vida útil. |
| descarte | discard | Abandono del objeto al final de su vida útil. |
| reciclaje | recycling | Reenvío a manufactura del mismo u otro objeto. |
| circulación lateral | lateral cycling | Reutilización en otro contexto social sin cambio de función. |
| tafonomía | taphonomy | Procesos post-deposicionales (naturales y culturales). |
| reloj interno | internal clock | Indicador físico-químico de edad relativa dentro del objeto. |
| huella isotópica | isotope ratio fingerprint | Firma química para determinar procedencia. |
| rasgo significativo | significant feature | Característica diagnóstica para clasificación cronológica/cultural. |
| tipo | type | Agrupación amplia de objetos con atributos compartidos. |
| universo estilístico | stylistic universe | Corpus de objetos que impone reglas de forma y uso. |
| agencia material | material agency | Capacidad del objeto de canalizar acciones humanas. |
| affordance | affordance | Propiedad percibida del objeto que posibilita una acción (Gibson). |
| entanglement | entanglement | Enredo de cosas entre sí y con humanos (Hodder). |
| cadena operativa | chaîne opératoire | Secuencia completa de acciones técnicas de producción. |
| archivo arqueológico | archaeological archive | Conjunto de registros donde emerge el pasado como evidencia. |
| persona social | social persona | Identidad fluida adscrita a un objeto a lo largo de su biografía. |
| unidad estratigráfica | stratigraphic unit | Unidad resultante de un evento de génesis estratigráfica (A8). |
| embebido | embedding | Objeto contenido con estabilidad en un volumen estratigráfico (A7). |
| génesis estratigráfica | stratigraphic genesis | Evento que produce unidades de estratificación (A4). |
| interfaz estratigráfica | stratigraphic interface | Superficie límite entre unidades (A3). |
| inferencia arqueológica | archaeological inference | Razonamiento a partir de evidencia material hacia el pasado. |
| proceso de formación | formation process | Procesos culturales y naturales que generan el registro arqueológico. |
| multivocalidad | multivocality | Coexistencia de interpretaciones rivales sobre un mismo objeto/contexto. |
| incertidumbre temporal | temporal uncertainty | Grados de confianza en dataciones relativas o absolutas. |
| datación relativa | relative chronology | Secuencia temporal sin fechas absolutas. |
| datación absoluta | absolute chronology | Fecha calendárica (C14, dendrocronología, OSL). |

---

**Fuentes consultadas:**
- Schiffer 1972, 1975, 1976, 1983 (behavioral archaeology, formation processes)
- Materiality in Archaeological Theory (Knappett, Gosden, Hodder, Ingold)
- Archaeological Record (Shott)
- Processualism in Archaeological Theory (Binford)
- CRMarchaeo v2.1.1 OWL (FORTH-ICS 2024)
- Análisis gap ontológico GPT
- Análisis artículos objeto
