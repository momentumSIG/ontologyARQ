Aquí tienes la extracción conceptual y semántica centrada en el objeto arqueológico, adaptada
al español y el informe detallado de la metodología aplicada.

1. Candidate Ontological Classes

•  Class: Archaeological Object (E22 Man-Made Object / A8 Archaeological Object)

o  Definición: Una entidad material recuperada de un contexto arqueológico que
es simultáneamente un producto del pasado y un participante activo en el
presente, definida no solo por su sustancia material sino por su "pasado-idad"
(pastness) percibida.

o  Superclass: E24 Physical Man-Made Thing

o  Alignment: CIDOC CRM E22 / CRMarchaeo A8

o  Evidencia: El objeto se define como una "totalidad" o una "fusión entre

pasado y presente", donde su significado se negocia en el presente mediante
procesos de inferencia.

•  Class: Significant Feature

o  Definición: Cualquier característica o detalle observable de un objeto

(material, mano de obra o decoración) que permite realizar distinciones
cronológicas o culturales.

o  Superclass: E26 Physical Feature

o  Alignment: CIDOC CRM E26

o  Evidencia: A diferencia de los "tipos", que son agrupaciones amplias, los

rasgos son las unidades específicas de composición que definen la "gramática"
de un estilo.

•  Class: Social Persona (of an Object)

o  Definición: La identidad fluida o "persona" adscrita a un objeto basada en
cómo es percibido, usado y valorado por los humanos a lo largo de su
biografía.

o  Superclass: E89 Propositional Object

o  Alignment: CIDOC CRM E89

o  Evidencia: Los objetos sufren alteraciones fundamentales en sus personas
sociales cuando son recategorizados o reinterpretados por diferentes
generaciones.

•  Class: Archaeological Archive

o  Definición: El conjunto colectivo de registros (papel, digital, medios)

producidos durante y después de la investigación, conceptualizado como un
objeto arqueológico en sí mismo porque es donde "emerge el pasado".

o  Superclass: E73 Information Object

o  Alignment: CIDOC CRM E73 / E78 Collection

o  Evidencia: Los archivos no son solo representaciones de un sitio; son el

material primario a través del cual el pasado es conceptualizado por el ojo
arqueológico.

•  Class: Material Clue

o  Definición: Manifestaciones materiales perceptibles de desgaste, rotura,

decadencia o pátina que evocan la cualidad de "pasado" en un observador.

o  Superclass: E26 Physical Feature

o  Alignment: CIDOC CRM E26

o  Evidencia: La "pasado-idad" (pastness) deriva de pistas materiales que indican
desintegración, las cuales pueden ser creadas o "fingidas" en el presente
funcionando aún como un signo autentificador.

2. Candidate Object Properties

•  Property: belongs to stylistic universe

o  Domain: Archaeological Object

o  Range: Stylistic Universe (clase propuesta)

o  Definición: Relaciona un objeto individual con un corpus de objetos

relacionados que imponen reglas de forma y uso.

o  Evidencia: Los objetos están "limitados por los cánones del estilo", que

establecen universos independientes que canalizan las acciones humanas.

•  Property: possesses pastness

o  Domain: Archaeological Object

o  Range: E55 Type (Percepción de pasado)

o  Definición: Relaciona una cosa física con la cualidad experimentada de ser "del

pasado".

o  Evidencia: Los objetos auténticos se definen como aquellos que poseen

"pastness", una cualidad que emancipa la autenticidad de la edad medible.

•  Property: has curation value

o  Domain: Archaeological Object

o  Range: E55 Type (Categoría de valor)

o  Definición: El grado en que un objeto es manejado cuidadosamente o

almacenado en lugares protegidos, afectando su probabilidad de entrar en el
registro arqueológico.

o  Evidencia: "Los artículos con alto valor de curación aparecerán con menos

frecuencia en el registro arqueológico" porque se usan con menos frecuencia y
se manejan con más cuidado.

•  Property: exhibits internal clock

o  Domain: Archaeological Object

o  Range: E16 Measurement (Índice de tiempo relativo)

o  Definición: Una propiedad física o química medible dentro de la sustancia de
un objeto que indica su edad relativa o grado de transformación (ej. pérdida
de arsénico en el cobre).

o  Evidencia: Los "relojes internos" permiten a los arqueólogos inferir el flujo
interno del tiempo a través de aspectos medidos de los propios objetos.

3. Candidate Data Properties

•  Data Property: time lag duration

o  Domain: Archaeological Object

o  Datatype: xsd:duration

o  Significado: La diferencia temporal entre la fecha de fabricación y la fecha de

deposición final.

o  Evidencia: "Cada objeto tiene una vida útil... la fecha de fabricación... no

puede equipararse con la fecha de uso de un artefacto".

•  Data Property: isotope ratio fingerprint

o  Domain: Archaeological Object

o  Datatype: xsd:string (o matriz numérica compleja)

o  Significado: La firma química/isotópica (ej. isótopos de plomo) utilizada para

relacionar un objeto terminado con una fuente geológica.

o  Evidencia: "Alguna característica química... proporciona una 'huella dactilar'

(fingerprint) que puede medirse en el objeto terminado".

4. Fases del Ciclo de Vida del Objeto

•  Producción/Fabricación: Fase T1, que incluye la extracción de materia prima (T1a),

salida del fabricante (T1b) y llegada al mayorista/minorista (T1f-h).

•  Adquisición: Fase T2, donde un objeto entra en un sistema doméstico, influenciado

por la elección del consumidor y la disponibilidad del mercado.

•  Vida de uso/Curación: El periodo de "vida normal", que puede incluir el estatus de

"reliquia" (heirloom) o el "reciclaje".

•  Transformación/Reparación: Modificación de la forma, como la refundición de

chatarra o la adición de motivos decorativos.

•  Deposición/Descarte: Fase T3, donde un objeto abandona el sistema cultural y entra

en el sistema natural/tafonómico.

•  Post-deposicional/Tafonómico: Cambios que ocurren después del uso y antes de la

excavación, como la corrosión o la meteorización química.

•  Recuperación/Excavación: Fase T4, la "invasión traumática" que extrae el objeto de su

equilibrio físico-químico.

•  Conservación/Restauración: Intervenciones post-recuperación que pueden cambiar la

forma material o restablecer una "presunta forma original".

5. Procesos Arqueológicos

•  Procesos Físicos:

o  Fundición y Refinado Metalúrgico: Transformación de minerales en metal y el

posterior tostado de sulfuros.

o  Refundición Oxidativa: Episodios de reciclaje que provocan la pérdida de

elementos traza volátiles (ej. el "reloj del arsénico").

o  Técnicas de Unión: Soldadura, dorado y difusión de cobre utilizados en la

fabricación.

•  Procesos Cognitivos/Analíticos:

o

o

Identificación de Huellas (Fingerprinting): Uso de patrones
elementales/isotópicos para determinar la procedencia.

Juicio Crítico: El doble acto de síntesis y juicio utilizado para interpretar
valores y decidir intervenciones de conservación.

o  Faseamiento (Phasing): Reconocimiento de clases de unidades distintivas

desde un punto de vista temporal.

6. Sistemas de Tipología y Clasificación

•  Agrupaciones Monotéticas: Clasificaciones tradicionales basadas en un conjunto

limitado de variables diagnósticas.

•  Análisis de Sistemas de Atributos: Una estrategia más compleja que utiliza múltiples
variables descubiertas mediante análisis estadístico de conglomerados (cluster
analysis).

•  Datación Basada en Rasgos (Features): Un sistema centrado en "rasgos significativos"

en lugar de "tipos", lo que permite una mayor precisión en la datación relativa.

•  Grupos Compositivos (Leitlegierungen): Clasificaciones de objetos metálicos basadas

en los principales tipos de aleaciones y patrones de impurezas.

•  Clasificación Funcional vs. Simbólica: Distinción de objetos por su uso previsto

(función original) frente a sus significados adquiridos.

7. Lagunas Ontológicas (Ontological Gaps)

•  Biografía del Objeto (Biografías Encadenadas): CIDOC CRM se centra en eventos

únicos, pero los objetos arqueológicos suelen tener "biografías encadenadas" donde
un objeto (ej. una moneda) se convierte en componente de otro.

•  Agencia Material: La capacidad de las propiedades formales de un objeto para

"establecer reglas de uso" y "canalizar las intenciones humanas" es difícil de modelar
como una propiedad simple.

•

"Pasado-idad" (Pastness) como Experiencia: La percepción de la autenticidad como
una interacción subjetiva entre un observador y las "pistas materiales" no está bien
resuelta en los modelos objetivos centrados en el material.

•  Actores Invisibles: El papel de los "elementos traza" o "isótopos" como actores

ontológicos que definen el origen del objeto independientemente del conocimiento
humano en el momento de la creación.

8. Módulos Ontológicos Potenciales

•  Módulo de Proveniencia (Provenance Module): Centrado en la hipótesis de

procedencia tradicional, vinculando las fuentes de materia prima con los artefactos
terminados mediante firmas de "huellas dactilares".

•  Módulo de Biografía y Transición: Modelado de las transiciones entre "personas

sociales", incluyendo fases como reliquia, fragmento reciclado o espécimen de museo.

•  Módulo de Decisión de Conservación: Modelado de la "ecología de las prácticas" y el

"juicio crítico" involucrado en la toma de decisiones compartida, incluyendo los valores
de los interesados (stakeholders).

•  Módulo de Reloj Interno: Centrado en los "relojes internos" de los materiales,

modelando el tiempo como un cambio físico en la sustancia.

9. Patrones Semánticos (Semantic Patterns)

•  Modelado del Tiempo Centrado en el Proceso: Cambio de la "edad medible" a "relojes
relativos internos", donde el tiempo está representado por transformaciones físicas
dentro del objeto.

•  Transición Objeto-Persona: Modelado de un objeto como un único portador físico que
transita por múltiples "Personas Proposicionales" (ej. de herramienta funcional a
reliquia sagrada a objeto de museo).

•  Ecología Actor-Objeto: Un patrón donde el conocimiento surge de la interacción de
"actantes humanos y no humanos" (ej. el arqueólogo, el paletín, el suelo y el clima).

•  Contexto como "Inter-Artefactual": Un patrón donde el contexto de un objeto no es

solo su estrato, sino su relación con un "universo estilístico" de otros objetos.

Informe de Extracción Semántica y Conceptual

Proyecto: Diseño de un Módulo de Ontología OWL para Objetos Arqueológicos Fecha: 26 de
mayo de 2026

1. Introducción y Metodología Este informe presenta los resultados de un análisis ontológico
profundo realizado sobre 14 fuentes académicas y técnicas relacionadas con la cultura
material, la arqueometría y la teoría arqueológica. El objetivo primordial ha sido identificar las

estructuras conceptuales necesarias para el desarrollo de un módulo OWL que se integre con
los estándares CIDOC CRM y CRMarchaeo.

La metodología se ha alejado del resumen descriptivo para adoptar un enfoque de ingeniería
de ontologías, identificando entidades, propiedades y procesos que a menudo permanecen
implícitos en el discurso arqueológico pero que son cruciales para la representación del
conocimiento computacional.

2. Hallazgos Clave para el Modelado

•  Dualidad del Objeto: Se ha identificado una distinción fundamental entre el objeto

como portador material y el objeto como entidad proposicional (Social Persona). Esto
sugiere un modelado donde una instancia física puede estar vinculada a múltiples
capas de identidad que cambian con el tiempo.

•  Reconceptualización del Tiempo: Las fuentes introducen el concepto de "relojes

internos" (Internal Clocks). Esto permite modelar la temporalidad no solo como fechas
absolutas externas (E52 Time-Span), sino como estados físicos internos resultantes de
procesos de transformación (ej. oxidación, pérdida de elementos volátiles).

•  El Papel del Archivo: Se propone elevar el Archivo Arqueológico al estatus de objeto
arqueológico, dado que es el nodo central donde la inferencia humana transforma la
materia en evidencia.

3. Recomendaciones para el Desarrollo OWL Se recomienda la creación de cuatro submódulos
específicos (Proveniencia, Biografía, Decisión de Conservación y Reloj Interno) que utilicen el
patrón de Reificación de Eventos de CIDOC CRM para capturar las transiciones de estado del
objeto. El enfoque debe ser proceso-céntrico, permitiendo que la historia del objeto sea una
cadena de eventos que modifican tanto su forma física como su valor social y arqueológico.

¿Por qué no usar E22_HumanMadeObject?

En realidad, sí he utilizado E22 (Human-Made Object) en mi respuesta anterior,
específicamente en el campo de Alignment (alineación) para la clase Archaeological Object,
vinculándola directamente con la entidad A8 Archaeological Object de CRMarchaeo, la cual
es, por definición, una subclase de E22.

Sin embargo, he optado por listar E24 (Physical Man-Made Thing) como la superclass
(superclase) general por las siguientes razones técnicas y teóricas extraídas de las fuentes:

•  Amplitud de la entidad arqueológica: Los autores analizados proponen una visión del
"objeto arqueológico" que trasciende la definición estricta de E22 (que en CIDOC CRM
se limita a objetos físicos discretos y generalmente portables). Las fuentes sugieren
que entidades como el archivo arqueológico o incluso los procesos del pasado pueden
ser conceptualizados como "objetos" de estudio. Al usar E24 como superclase,
permitimos que el modelo incluya tanto artefactos portables (E22) como elementos
inmuebles o rasgos físicos (E26 Physical Feature), los cuales son fundamentales para
distinguir un depósito arqueológico de uno meramente geológico.

•

•

Jerarquía de herencia: En la arquitectura de CIDOC CRM, E22 Human-Made Object es
una subclase de E24 Human-Made Thing. Al diseñar un módulo ontológico, referenciar
la clase superior (E24) asegura que cualquier instancia de "Objeto Arqueológico"
herede la propiedad esencial de ser una cosa material producida o modificada
intencionalmente por humanos, que es el criterio ontológico base mencionado en los
textos para definir la "pasado-idad" (pastness) de una pieza.

Inclusión de rasgos y huellas: Gran parte de la información diagnóstica de un objeto
no reside en el objeto como un todo (E22), sino en sus Significant Features (rasgos
significativos) o Material Clues (pistas materiales), como el desgaste, la pátina o la
técnica de manufactura. Estos elementos se alinean mejor con E26 (Physical Feature).
Dado que E24 es el ancestro común de E22 y E26, utilizarlo como superclase facilita un
modelado integrado donde el "objeto" puede ser un portador de múltiples rasgos
materiales e identidades sociales.

En resumen, E22 se usó para la alineación específica de artefactos, pero E24 se prefirió como
raíz jerárquica para dar cabida a la complejidad del registro arqueológico (que incluye
fragmentos, archivos y estructuras) descrita por los expertos.

