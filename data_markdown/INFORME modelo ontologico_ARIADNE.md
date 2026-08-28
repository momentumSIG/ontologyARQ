Modelo ontológico IDEArq (integración ARIADNEplus)

1. Resumen del Enfoque

El presente modelo representa la infraestructura de datos IDEArq mediante un
enfoque híbrido. Utiliza la ontología AO-Cat V1.2.2 para la capa de descubrimiento
(catálogo europeo) y las ontologías CIDOC CRM, CRMarchaeo, GeoSPARQL 1.1 y OWL-
Time para la descripción científica profunda.

2. Arquitectura de colecciones

La raíz del modelo es la clase ao:AO_Collection.

•  Se ha implementado una jerarquía donde la colección general de IDEArq
contiene sub-colecciones temáticas (ej. C14) mediante la propiedad
ao:has_part.

•  Descubrimiento geográfico: Se utiliza ao:has_spatial_coverage para indicar
que la base de datos abarca España y Portugal, vinculándola a instancias de
ao:AO_Spatial_Region.

•  Sujetos ARIADNE: Se han asignado los "Sujetos" oficiales mediante

ao:has_ARIADNE_subject. Esto garantiza que el portal europeo clasifique los
datos de IDEArq bajo los filtros de Site/monument, Scientific analysis y Date.

3. Modelado espacial y geométrico (naranja y verde)

El modelo resuelve la ubicación de los yacimientos mediante dos vías
complementarias:

•

Jerarquía administrativa: Conecta el yacimiento con el Municipio, Provincia y
País mediante la relación crm:P89_falls_within.

•  Vía ARIADNE (Naranja): Implementa ao:AO_Spatial_Region_Point y Polygon.
•  Vía GeoSPARQL 1.1 (verde): Introduce la clase geosparql:Geometry. Esta es la

aportación más técnica, ya que permite declarar el CRS (Sistema de Referencia)
dentro del literal WKT (ej. <EPSG:25830>), asegurando la precisión métrica y la
interoperabilidad con sistemas GIS e INSPIRE.

4. Estratigrafía y contexto arqueológico

Se reutiliza la extensión CRMarchaeo para documentar la excavación.

•  El yacimiento físico es un ao:AO_Object.
•

Las estructuras (Tumba 52) se modelan como
crmarchaeo:A8_Structural_Feature.
Las unidades de excavación se modelan como
crmarchaeo:A2_Stratigraphic_Volume_Unit.

•

•  Se utiliza la relación inversa crm:P46i_forms_part_of para contextualizar los

hallazgos dentro de sus unidades y estructuras de forma ascendente.

5. Justificación técnica de atributos

Este es un punto clave del modelo: el uso de propiedades ao: dentro de clases crm:.

•  Validez de Dominio: Dado que las clases de ARIADNE son subclases de CIDOC

CRM (ej. ao:AO_Object es subclase de crm:E18), las propiedades definidas para
la superclase son lógicamente válidas para sus descendientes.

•  Mecanismo de "shortcuts": Siguiendo la sección 5 del PDF de AO-Cat,
propiedades como ao:has_title, ao:has_original_id y ao:has_type se
implementan como "atajos" documentados. Por ejemplo, ao:has_title sustituye
a la ruta compleja crm:P102 -> E35_Title.

•  Beneficio: Este enfoque permite que clases especializadas como

crm:E20_Biological_Object (no descritas explícitamente en el catálogo simple
de ARIADNE) hereden la capacidad de ser indexadas por el buscador europeo
sin perder su identidad científica original.

6. Caracterización de hallazgos (biológicos y manufacturados)

ARIADNE simplifica todo en ao:AO_Object:

•

crm:E22_Human-Made_Object (artefactos) y crm:E20_Biological_Object
(restos humanos/animales/vegetales).

•  Clasificación por conceptos: Se utiliza ao:has_type hacia múltiples instancias
de ao:AO_Concept. Esto permite registrar el sexo, la edad, la posición, el
material y el ritual (ej. Cremación)) de forma normalizada.

7. Cronología y datación (herencia múltiple)

Para las dataciones de C14, se ha diseñado una clase de herencia múltiple:

•

La clase de datación de IDEArq hereda simultáneamente de ao:AO_Event (para
el catálogo) y de crm:E16_Measurement (para la precisión científica).

•  Se integra OWL-Time mediante time:TimePosition para ofrecer la fecha en dos
formatos: BP (dato original) y Calendario Gregoriano (dato interoperable),
permitiendo cálculos computacionales sobre la cronología.

8. Alineación semántica

Todos los términos tipológicos y descriptivos se gestionan como ao:AO_Concept.
Mediante la propiedad skos:exactMatch, estos términos se vinculan a tesauros
internacionales (Getty AAT y PeriodO), lo que garantiza que los datos de IDEArq sean
multilingües y comparables con cualquier otra base de datos europea.

Apéndice: Linaje de Clases (Mapeo CIDOC CRM)

Clase en el Diagrama
ao:AO_Collection

Clase Padre en CIDOC CRM
crmpe:PE18_Dataset

crm:E18_Physical_Thing
crm:E53_Place
crm:E5_Event

ao:AO_Object
ao:AO_Spatial_Region
ao:AO_Event
ao:AO_Temporal_Region crm:E52_Time-Span
ao:AO_Concept
crmarchaeo:A8
crm:E20 / E22

crm:E55_Type
crm:E19_Physical_Object
crm:E19_Physical_Object

•  ao:has_space_region (pág. 52, sección 5.46): Se usa para conectar un Objeto

(Los Millares) con su Región Espacial.

•  ao:has_spatial_coverage (pág. 47, sección 5.33): Se usa para conectar una

Colección con su área geográfica.

PREGUNTAS DE COMPETENCIA

1. Gestión

•  PC1: ¿Qué sub-colecciones temáticas (ej. C14, Pinturas) integran la

infraestructura de datos de IDEArq?

o  Respuesta vía: ao:AO_Collection y ao:has_part.

•  PC2: ¿Bajo qué categorías oficiales de ARIADNE (Sujetos) se deben filtrar los

datos de una colección específica?

o  Respuesta vía: ao:has_ARIADNE_subject y ao:AO_Concept.

•  PC3: ¿Cuál es el alcance geográfico general (países) que cubre la base de datos

de IDEArq?

o  Respuesta vía: ao:has_spatial_coverage y ao:AO_Spatial_Region.
•  PC4: ¿Cuál es el identificador original (ID local) de un objeto para poder

localizarlo en la web de IDEArq?

o  Respuesta vía: ao:has_original_id.

2. Localización y Geografía

•  PC5: ¿En qué municipio, provincia y comunidad autónoma se localiza

físicamente un yacimiento?

o  Respuesta vía: ao:has_space_region y la jerarquía crm:P89_falls_within.

•  PC6: ¿Cuál es la geometría exacta (punto o polígono) de un sitio arqueológico

en formato WKT?

o  Respuesta vía: geo:hasGeometry y geo:asWKT.

•  PC7: ¿En qué sistema de referencia de coordenadas (CRS) están expresadas las

coordenadas de IDEArq para asegurar su interoperabilidad con INSPIRE?

o  Respuesta vía: La declaración del CRS dentro del literal de geo:asWKT.
•  PC8: ¿A qué entidad política (país) pertenece una región administrativa según

el estándar de Wikidata?

o  Respuesta vía: ao:has_country vinculado a la URI de Wikidata.

3. Contexto arqueológico y estratigrafía

•  PC9: ¿En qué estructura específica (ej. Tumba 52) y en qué unidad estratigráfica

(nivel) se recuperó un objeto?

o  Respuesta vía: crmarchaeo:A8, crmarchaeo:A2 y la relación

crm:P46i_forms_part_of.

•  PC10: ¿Qué tipo de construcción arquitectónica o funeraria (ej. Megalito)

representa una estructura determinada?

o  Respuesta vía: ao:has_type vinculado a un ao:AO_Concept.

4. Objetos

Estas preguntas permiten realizar estudios estadísticos y tipológicos.

•  PC11: ¿Es un hallazgo concreto un objeto manufacturado (o un resto biológico
o  Respuesta vía: Herencia múltiple hacia crm:E22_Human-Made_Object o

crm:E20_Biological_Object.

•  PC12: ¿Cuál es el sexo biológico, el grupo de edad y la posición de un individuo

hallado en una tumba?

o  Respuesta vía: Múltiples flechas ao:has_type hacia instancias de

ao:AO_Concept.

•  PC13: ¿De qué material está fabricado un objeto y qué función técnica se le

atribuye?

o  Respuesta vía: ao:has_type hacia conceptos de material y función.

•  PC14: ¿Qué tipo de ritual funerario (ej. Inhumación o Cremación) se asocia al

evento de enterramiento de un individuo?

o  Respuesta vía: ao:AO_Event y su relación ao:has_type hacia el concepto

de ritual.

5. Cronología y datación

•  PC15: ¿Qué método científico se utilizó para obtener la cronología de una

muestra (ej. Carbono 14)?

o  Respuesta vía: ao:has_type (o ao:has_method) desde la clase de

datación hacia el concepto.

•  PC16: ¿Cuál es el valor numérico original en años BP (Before Present) de una

datación radiocarbónica?

o  Respuesta vía: time:TimePosition con el atributo time:hasTRS

apuntando a BP.

•  PC17: ¿A qué año del calendario gregoriano (BC/AD) equivale una fecha
determinada para permitir comparaciones con periodos históricos?

o  Respuesta vía: El segundo nodo de time:TimePosition con el TRS

gregoriano.

•  PC18: ¿A qué periodo cultural (ej. Edad del Cobre) se adscribe un evento o

hallazgo según el tesauro estándar de PeriodO?

o  Respuesta vía: ao:has_temporal_coverage hacia

ao:AO_Temporal_Region con skos:exactMatch a PeriodO.

•  PC19: ¿Están los términos locales de IDEArq alineados con estándares

internacionales como el Getty AAT?

o  Respuesta vía: skos:exactMatch dentro de cada ao:AO_Concept.

