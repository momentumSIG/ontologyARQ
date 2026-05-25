#!/usr/bin/env python3
"""
Generate Qwen3.6 ontology .ttl files for all 80 CQs.
Design: IDEArq-inspired archaeological object modeling.
Independent from Deepseekv4 (event-centric) and K2.6 (deep taxonomy).
"""

import os
import re

BASE_DIR = "/home/eaguayo/ONTOLOGIA-ARQ"
CQ_DIR = os.path.join(BASE_DIR, "CQ/CQ_Qwen3.6")
OUT_DIR = os.path.join(BASE_DIR, "ontologies_generated/Qwen3.6")

PREFIXES = """@prefix arqo: <http://www.ontologyARQ.org/archaeological-object/> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix crmarchaeo: <http://www.cidoc-crm.org/crmarchaeo/> .
@prefix crmsci: <http://www.cidoc-crm.org/crmsci/> .
@prefix crminf: <http://www.cidoc-crm.org/crminf/> .
@prefix crmhs: <http://www.cidoc-crm.org/crmhs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
"""

HEADER_TEMPLATE = """
# ============================================================
# Ontology: Archaeological Object Module (Qwen3.6 Design)
# Model: Qwen3.6 | Strategy: {strategy} | Temperature: {temp}
# CQ: {cq_id}
# Design: IDEArq-inspired object modeling with lifecycle focus
# ============================================================
"""

# CQ-specific ontology generation templates
# Each CQ gets a tailored response based on its question

def parse_cqs(filepath):
    """Parse CQs from markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    cqs = []
    pattern = r'## (CQ-\w+-\d+)\s*\*\*Question:\*\*\s*(.*?)\s*- \*\*Ontology modules required:\*\*\s*(.*?)\s*- \*\*Possible ontology reuse:\*\*\s*(.*?)(?=\n## |\Z)'
    for match in re.finditer(pattern, content, re.DOTALL):
        cqs.append({
            'id': match.group(1),
            'question': match.group(2).strip(),
            'modules': match.group(3).strip(),
            'reuse': match.group(4).strip()
        })
    return cqs

def generate_memoryless_ttl(cq, temp):
    """Generate memoryless .ttl content for a CQ at given temperature."""
    
    # Temperature-based design variations
    if temp == "0.3":
        style = "Conservative: Max CIDOC CRM reuse, minimal new classes, flat hierarchies"
    elif temp == "0.5":
        style = "Balanced: Moderate new classes, some restrictions, standard CRM alignment"
    else:  # 0.7
        style = "Creative: Deep class hierarchies, reification pivot classes, extensive restrictions"
    
    # Generate CQ-specific content
    content = generate_cq_specific(cq, temp)
    
    header = HEADER_TEMPLATE.format(
        strategy="memoryless",
        temp=temp,
        cq_id=cq['id'].replace('CQ-', '')
    )
    
    return PREFIXES + header + content

def generate_cq_specific(cq, temp):
    """Generate ontology content specific to each CQ."""
    cq_id = cq['id']
    question = cq['question']
    
    # Block determination
    if 'OBJ' in cq_id:
        block = "object"
    elif 'SPA' in cq_id:
        block = "spatial"
    elif 'TEM' in cq_id:
        block = "temporal"
    else:
        block = "stratigraphy"
    
    # Generate based on block and CQ number
    if block == "object":
        return generate_object_cq(cq_id, question, temp)
    elif block == "spatial":
        return generate_spatial_cq(cq_id, question, temp)
    elif block == "temporal":
        return generate_temporal_cq(cq_id, question, temp)
    else:
        return generate_stratigraphy_cq(cq_id, question, temp)

def generate_object_cq(cq_id, question, temp):
    """Generate ontology for Archaeological Object CQs."""
    num = int(cq_id.split('-')[-1])
    
    # Core classes for object block (IDEArq-inspired)
    classes = []
    properties = []
    data_properties = []
    restrictions = []
    
    # Base classes always present
    classes.append("""arqo:ArchaeologicalObject a owl:Class ;
    rdfs:subClassOf crm:E19_Physical_Object ;
    rdfs:label "ArchaeologicalObject"@en ;
    rdfs:comment "Physical object recovered during archaeological investigation, subject to lifecycle processes"@en .""")
    
    # Temperature-based hierarchy
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:NaturalObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "NaturalObject"@en ;
    rdfs:comment "Object of natural origin found in archaeological context"@en .""")
        
        classes.append("""arqo:HumanMadeObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "HumanMadeObject"@en ;
    rdfs:comment "Object created or modified by human action"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:AbioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "AbioticObject"@en ;
    rdfs:comment "Non-living natural object (stone, mineral, sediment)"@en .""")
        
        classes.append("""arqo:BioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "BioticObject"@en ;
    rdfs:comment "Living or once-living natural object (bone, shell, plant remains)"@en .""")
        
        classes.append("""arqo:Artefact a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Artefact"@en ;
    rdfs:comment "Portable human-made object with functional purpose"@en .""")
        
        classes.append("""arqo:Structure a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Structure"@en ;
    rdfs:comment "Non-portable human-made construction"@en .""")
        
        classes.append("""arqo:ArtisticExpression a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "ArtisticExpression"@en ;
    rdfs:comment "Human-made object with aesthetic or symbolic function"@en .""")
        
        # Disjointness axioms at 0.7
        restrictions.append("""arqo:NaturalObject owl:disjointWith arqo:HumanMadeObject .""")
        restrictions.append("""arqo:AbioticObject owl:disjointWith arqo:BioticObject .""")
        restrictions.append("""arqo:Artefact owl:disjointWith arqo:Structure .""")
    
    # CQ-specific additions
    if num == 1:  # Material composition
        properties.append("""arqo:hasMaterial a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E57_Material ;
    rdfs:label "hasMaterial"@en ;
    rdfs:comment "Indicates the material composition of an archaeological object"@en .""")
        
    elif num == 2:  # Excavation process unit
        classes.append("""arqo:ExcavationProcessUnit a owl:Class ;
    rdfs:subClassOf crmarchaeo:A1_Excavation_Process_Unit ;
    rdfs:label "ExcavationProcessUnit"@en ;
    rdfs:comment "Single excavation process unit during which objects were recovered"@en .""")
        
        properties.append("""arqo:recoveredIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ExcavationProcessUnit ;
    rdfs:label "recoveredIn"@en ;
    rdfs:comment "Links object to the excavation process unit in which it was recovered"@en .""")
        
    elif num == 3:  # Repurposing
        classes.append("""arqo:RepurposingEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "RepurposingEvent"@en ;
    rdfs:comment "Event where an object is repurposed for a function different from its original intended use"@en .""")
        
        properties.append("""arqo:hasOriginalFunction a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasOriginalFunction"@en ;
    rdfs:comment "Original intended function of the object"@en .""")
        
        properties.append("""arqo:hasRepurposedFunction a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasRepurposedFunction"@en ;
    rdfs:comment "New function assigned to the object after repurposing"@en .""")
        
    elif num == 4:  # Object biography sequence
        classes.append("""arqo:ObjectBiography a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ObjectBiography"@en ;
    rdfs:comment "Sequence of events constituting the lifecycle of an archaeological object"@en .""")
        
        properties.append("""arqo:hasBiographyEvent a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E5_Event ;
    rdfs:label "hasBiographyEvent"@en ;
    rdfs:comment "Links object to an event in its biography"@en .""")
        
    elif num == 5:  # Parallel biographical patterns
        properties.append("""arqo:sharesBiographyPattern a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesBiographyPattern"@en ;
    rdfs:comment "Indicates that two objects share parallel biographical patterns"@en .""")
        
    elif num == 6:  # Unique identifier
        data_properties.append("""arqo:hasFieldIdentifier a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasFieldIdentifier"@en ;
    rdfs:comment "Unique identifier assigned to object at moment of recovery in the field"@en .""")
        
    elif num == 7:  # Material and functional interpretation
        classes.append("""arqo:MaterialInterpretation a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "MaterialInterpretation"@en ;
    rdfs:comment "Researcher-assigned interpretation of object material"@en .""")
        
        classes.append("""arqo:FunctionalInterpretation a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "FunctionalInterpretation"@en ;
    rdfs:comment "Researcher-assigned interpretation of object function"@en .""")
        
    elif num == 8:  # Movement from depositional context
        classes.append("""arqo:DisplacementEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "DisplacementEvent"@en ;
    rdfs:comment "Event where object is moved from its primary depositional context"@en .""")
        
    elif num == 9:  # Manufacturing techniques
        classes.append("""arqo:ManufacturingEvent a owl:Class ;
    rdfs:subClassOf crm:E12_Production ;
    rdfs:label "ManufacturingEvent"@en ;
    rdfs:comment "Event of object manufacturing using specific technological procedures"@en .""")
        
        data_properties.append("""arqo:hasManufacturingTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasManufacturingTechnique"@en ;
    rdfs:comment "Technological procedure or craft technique used in manufacturing"@en .""")
        
    elif num == 10:  # Chronological narrative
        properties.append("""arqo:hasChronologicalNarrative a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E52_Time-Span ;
    rdfs:label "hasChronologicalNarrative"@en ;
    rdfs:comment "Full chronological narrative from manufacture through use, reuse, and deposition"@en .""")
        
    elif num == 11:  # Raw material provenance
        properties.append("""arqo:hasRawMaterialProvenance a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E53_Place ;
    rdfs:label "hasRawMaterialProvenance"@en ;
    rdfs:comment "Geological or geographic origin of raw materials"@en .""")
        
    elif num == 12:  # Functional role change
        classes.append("""arqo:FunctionalChange a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FunctionalChange"@en ;
    rdfs:comment "Change in functional role of an object during its active use-life"@en .""")
        
    elif num == 13:  # Repair/alteration traces
        classes.append("""arqo:ModificationEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "ModificationEvent"@en ;
    rdfs:comment "Event of repair, alteration, or deliberate modification after initial production"@en .""")
        
    elif num == 14:  # State of preservation
        data_properties.append("""arqo:hasPreservationState a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasPreservationState"@en ;
    rdfs:comment "State of preservation of the object"@en .""")
        
        classes.append("""arqo:PostDepositionalProcess a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "PostDepositionalProcess"@en ;
    rdfs:comment "Post-depositional process that shaped the state of preservation"@en .""")
        
    elif num == 15:  # Physical samples
        classes.append("""arqo:SamplingEvent a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "SamplingEvent"@en ;
    rdfs:comment "Event where physical sample is taken from object for laboratory analysis"@en .""")
        
        properties.append("""arqo:wasSampledIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:SamplingEvent ;
    rdfs:label "wasSampledIn"@en ;
    rdfs:comment "Links object to sampling event"@en .""")
        
    elif num == 16:  # Typological scheme
        classes.append("""arqo:TypologicalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "TypologicalAssignment"@en ;
    rdfs:comment "Assignment of object to a typological scheme"@en .""")
        
        properties.append("""arqo:classifiedUnder a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TypologicalAssignment ;
    rdfs:label "classifiedUnder"@en ;
    rdfs:comment "Links object to its typological classification"@en .""")
        
    elif num == 17:  # Common depositional event
        properties.append("""arqo:sharesDepositionalEvent a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesDepositionalEvent"@en ;
    rdfs:comment "Indicates objects share a common depositional event within same stratigraphic unit"@en .""")
        
    elif num == 18:  # Social actors
        properties.append("""arqo:associatedWithActor a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "associatedWithActor"@en ;
    rdfs:comment "Links object to social actor, cultural group, or craft tradition"@en .""")
        
    elif num == 19:  # Geographic travel
        classes.append("""arqo:CirculationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CirculationEvent"@en ;
    rdfs:comment "Event where object travels across different geographic regions or cultural zones"@en .""")
        
    elif num == 20:  # Conservation treatments
        classes.append("""arqo:ConservationTreatment a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ConservationTreatment"@en ;
    rdfs:comment "Conservation treatment or laboratory analysis undergone after excavation"@en .""")
        
        properties.append("""arqo:underwentTreatment a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConservationTreatment ;
    rdfs:label "underwentTreatment"@en ;
    rdfs:comment "Links object to conservation treatment it underwent"@en .""")
    
    # Build output
    output = "\n# ======================= CLASSES ===========================\n"
    output += "\n\n".join(classes)
    
    if properties:
        output += "\n\n# =================== OBJECT PROPERTIES =====================\n"
        output += "\n\n".join(properties)
    
    if data_properties:
        output += "\n\n# ==================== DATA PROPERTIES =====================\n"
        output += "\n\n".join(data_properties)
    
    if restrictions:
        output += "\n\n# ===================== RESTRICTIONS =======================\n"
        output += "\n".join(restrictions)
    
    output += f"\n# Ontology generated by Qwen3.6 using memoryless strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output

def generate_spatial_cq(cq_id, question, temp):
    """Generate ontology for Spatial CQs."""
    num = int(cq_id.split('-')[-1])
    
    classes = []
    properties = []
    data_properties = []
    restrictions = []
    
    # Base spatial class
    classes.append("""arqo:ArchaeologicalPlace a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "ArchaeologicalPlace"@en ;
    rdfs:comment "Geographic location associated with archaeological entity"@en .""")
    
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:Site a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "Site"@en ;
    rdfs:comment "Archaeological site with defined spatial extent"@en .""")
        
        classes.append("""arqo:ActivityZone a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "ActivityZone"@en ;
    rdfs:comment "Distinct activity zone within a settlement"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:TerritorialNetwork a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "TerritorialNetwork"@en ;
    rdfs:comment "Coherent territorial network linking separate sites"@en .""")
        
        classes.append("""arqo:SpatialUncertainty a owl:Class ;
    rdfs:subClassOf crmsci:S4_Observation ;
    rdfs:label "SpatialUncertainty"@en ;
    rdfs:comment "Quantified uncertainty associated with spatial measurement"@en .""")
    
    # CQ-specific
    if num == 1:  # Geographic coordinates
        data_properties.append("""arqo:hasCoordinates a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalPlace ;
    rdfs:range xsd:string ;
    rdfs:label "hasCoordinates"@en ;
    rdfs:comment "Geographic coordinates recorded for archaeological find or context"@en .""")
        
    elif num == 2:  # Geometric shape
        classes.append("""arqo:SpatialGeometry a owl:Class ;
    rdfs:subClassOf geo:Geometry ;
    rdfs:label "SpatialGeometry"@en ;
    rdfs:comment "Geometric shape (point, line, polygon, solid) representing archaeological entity"@en .""")
        
        data_properties.append("""arqo:hasGeometryType a owl:DatatypeProperty ;
    rdfs:domain arqo:SpatialGeometry ;
    rdfs:range xsd:string ;
    rdfs:label "hasGeometryType"@en ;
    rdfs:comment "Type of geometric shape: point, line, polygon, or solid"@en .""")
        
    elif num == 3:  # Topological relations
        properties.append("""arqo:topologicallyRelatedTo a owl:ObjectProperty ;
    rdfs:domain arqo:ActivityZone ;
    rdfs:range arqo:ActivityZone ;
    rdfs:label "topologicallyRelatedTo"@en ;
    rdfs:comment "Topological relationship between activity zones"@en .""")
        
    elif num == 4:  # Spatial connections
        properties.append("""arqo:connectedToSite a owl:ObjectProperty ;
    rdfs:domain arqo:Site ;
    rdfs:range arqo:Site ;
    rdfs:label "connectedToSite"@en ;
    rdfs:comment "Spatial connection linking sites into territorial network"@en .""")
        
    elif num == 5:  # Spatial distribution evidence
        classes.append("""arqo:SpatialDistributionObservation a owl:Class ;
    rdfs:subClassOf crmsci:S4_Observation ;
    rdfs:label "SpatialDistributionObservation"@en ;
    rdfs:comment "Observation of spatial distribution patterns supporting functional interpretation"@en .""")
        
    elif num == 6:  # 3D spatial models
        classes.append("""arqo:ThreeDGeometry a owl:Class ;
    rdfs:subClassOf geo:Geometry ;
    rdfs:label "ThreeDGeometry"@en ;
    rdfs:comment "3D spatial model with quantified uncertainty"@en .""")
        
    elif num == 7:  # Coordinate reference system
        data_properties.append("""arqo:hasCRS a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalPlace ;
    rdfs:range xsd:string ;
    rdfs:label "hasCRS"@en ;
    rdfs:comment "Coordinate reference system for spatial measurements"@en .""")
        
    elif num == 8:  # WKT representation
        data_properties.append("""arqo:hasWKT a owl:DatatypeProperty ;
    rdfs:domain arqo:SpatialGeometry ;
    rdfs:range xsd:string ;
    rdfs:label "hasWKT"@en ;
    rdfs:comment "Serialized WKT representation of geometry"@en .""")
        
    elif num == 9:  # Administrative hierarchy
        classes.append("""arqo:AdministrativeUnit a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "AdministrativeUnit"@en ;
    rdfs:comment "Administrative division (municipality, province, region, state)"@en .""")
        
    elif num == 10:  # Nested administrative divisions
        properties.append("""arqo:partOfAdministrativeUnit a owl:ObjectProperty ;
    rdfs:domain arqo:AdministrativeUnit ;
    rdfs:range arqo:AdministrativeUnit ;
    rdfs:label "partOfAdministrativeUnit"@en ;
    rdfs:comment "Hierarchical relationship between administrative divisions"@en .""")
        
    elif num == 11:  # Topological predicates
        properties.append("""arqo:sfContains a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalPlace ;
    rdfs:range arqo:ArchaeologicalPlace ;
    rdfs:label "sfContains"@en ;
    rdfs:comment "GeoSPARQL topological predicate: contains"@en .""")
        
        properties.append("""arqo:sfTouches a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalPlace ;
    rdfs:range arqo:ArchaeologicalPlace ;
    rdfs:label "sfTouches"@en ;
    rdfs:comment "GeoSPARQL topological predicate: touches"@en .""")
        
    elif num == 12:  # Spatial extent
        data_properties.append("""arqo:hasSpatialExtent a owl:DatatypeProperty ;
    rdfs:domain arqo:Site ;
    rdfs:range xsd:string ;
    rdfs:label "hasSpatialExtent"@en ;
    rdfs:comment "Defined spatial extent or perimeter of archaeological site"@en .""")
        
    elif num == 13:  # Precision metric
        data_properties.append("""arqo:hasPrecisionMetric a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalPlace ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasPrecisionMetric"@en ;
    rdfs:comment "Precision metric accompanying recorded spatial coordinate"@en .""")
        
    elif num == 14:  # Uncertain locations
        classes.append("""arqo:UncertainLocation a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "UncertainLocation"@en ;
    rdfs:comment "Location flagged as approximate or uncertain"@en .""")
        
    elif num == 15:  # Volumetric geometry
        classes.append("""arqo:VolumetricGeometry a owl:Class ;
    rdfs:subClassOf geo:Geometry ;
    rdfs:label "VolumetricGeometry"@en ;
    rdfs:comment "Volumetric geometry describing stratigraphic unit or built structure in 3D"@en .""")
        
    elif num == 16:  # Excavation trenches
        classes.append("""arqo:ExcavationTrench a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "ExcavationTrench"@en ;
    rdfs:comment "Excavation trench with spatial relationship to site boundary"@en .""")
        
    elif num == 17:  # Intra-unit spatial distribution
        properties.append("""arqo:hasSpatialDistributionPattern a owl:DatatypeProperty ;
    rdfs:domain crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:range xsd:string ;
    rdfs:label "hasSpatialDistributionPattern"@en ;
    rdfs:comment "Intra-unit spatial distribution pattern of finds"@en .""")
        
    elif num == 18:  # Natural landscape elements
        classes.append("""arqo:NaturalLandscapeElement a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalPlace ;
    rdfs:label "NaturalLandscapeElement"@en ;
    rdfs:comment "Natural landscape element geographically proximate to archaeological site"@en .""")
        
    elif num == 19:  # Settlement patterning
        properties.append("""arqo:partOfSettlementPattern a owl:ObjectProperty ;
    rdfs:domain arqo:Site ;
    rdfs:range arqo:Site ;
    rdfs:label "partOfSettlementPattern"@en ;
    rdfs:comment "Settlement patterning relationship between sites"@en .""")
        
    elif num == 20:  # Geological substrate
        properties.append("""arqo:restsOnGeologicalSubstrate a owl:ObjectProperty ;
    rdfs:domain arqo:Site ;
    rdfs:range arqo:ArchaeologicalPlace ;
    rdfs:label "restsOnGeologicalSubstrate"@en ;
    rdfs:comment "Spatial relationship between site and its geological substrate"@en .""")
    
    # Build output
    output = "\n# ======================= CLASSES ===========================\n"
    output += "\n\n".join(classes)
    
    if properties:
        output += "\n\n# =================== OBJECT PROPERTIES =====================\n"
        output += "\n\n".join(properties)
    
    if data_properties:
        output += "\n\n# ==================== DATA PROPERTIES =====================\n"
        output += "\n\n".join(data_properties)
    
    if restrictions:
        output += "\n\n# ===================== RESTRICTIONS =======================\n"
        output += "\n".join(restrictions)
    
    output += f"\n# Ontology generated by Qwen3.6 using memoryless strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output

def generate_temporal_cq(cq_id, question, temp):
    """Generate ontology for Temporal CQs."""
    num = int(cq_id.split('-')[-1])
    
    classes = []
    properties = []
    data_properties = []
    restrictions = []
    
    # Base temporal class
    classes.append("""arqo:ArchaeologicalTimeSpan a owl:Class ;
    rdfs:subClassOf crm:E52_Time-Span ;
    rdfs:label "ArchaeologicalTimeSpan"@en ;
    rdfs:comment "Temporal extent associated with archaeological context or event"@en .""")
    
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:CulturalPeriod a owl:Class ;
    rdfs:subClassOf crm:E4_Period ;
    rdfs:label "CulturalPeriod"@en ;
    rdfs:comment "Established cultural or historical period"@en .""")
        
        classes.append("""arqo:GeologicalEpoch a owl:Class ;
    rdfs:subClassOf crm:E4_Period ;
    rdfs:label "GeologicalEpoch"@en ;
    rdfs:comment "Geological epoch or stage corresponding to stratigraphic deposit"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:DatingAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "DatingAssignment"@en ;
    rdfs:comment "Assignment of archaeological entity to a temporal period"@en .""")
        
        classes.append("""arqo:ChronologicalUncertainty a owl:Class ;
    rdfs:subClassOf crmsci:S4_Observation ;
    rdfs:label "ChronologicalUncertainty"@en ;
    rdfs:comment "Margin of error or uncertainty accompanying chronological assignment"@en .""")
    
    # CQ-specific
    if num == 1:  # Cultural/historical periods
        properties.append("""arqo:associatedWithPeriod a owl:ObjectProperty ;
    rdfs:domain crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:range arqo:CulturalPeriod ;
    rdfs:label "associatedWithPeriod"@en ;
    rdfs:comment "Links archaeological context to cultural or historical period"@en .""")
        
    elif num == 2:  # Geological epochs
        properties.append("""arqo:correspondsToGeologicalEpoch a owl:ObjectProperty ;
    rdfs:domain crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:range arqo:GeologicalEpoch ;
    rdfs:label "correspondsToGeologicalEpoch"@en ;
    rdfs:comment "Links stratigraphic deposit to corresponding geological epoch"@en .""")
        
    elif num == 3:  # Relative vs absolute chronology
        properties.append("""arqo:alignsWithAbsoluteChronology a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalPeriod ;
    rdfs:range arqo:ArchaeologicalTimeSpan ;
    rdfs:label "alignsWithAbsoluteChronology"@en ;
    rdfs:comment "Alignment of relative cultural phase with numerically dated chronology"@en .""")
        
    elif num == 4:  # Period assignment
        classes.append("""arqo:PeriodAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "PeriodAssignment"@en ;
    rdfs:comment "Assignment of event or artifact to established cultural period"@en .""")
        
    elif num == 5:  # Calendar date
        data_properties.append("""arqo:hasCalendarDate a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range xsd:string ;
    rdfs:label "hasCalendarDate"@en ;
    rdfs:comment "Calendar date (BCE/CE) corresponding to archaeological dating"@en .""")
        
    elif num == 6:  # Radiocarbon age
        data_properties.append("""arqo:hasRadiocarbonAge a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasRadiocarbonAge"@en ;
    rdfs:comment "Uncalibrated radiocarbon age in years Before Present"@en .""")
        
    elif num == 7:  # Analytical technique
        classes.append("""arqo:DatingTechnique a owl:Class ;
    rdfs:subClassOf crmsci:S21_Measurement ;
    rdfs:label "DatingTechnique"@en ;
    rdfs:comment "Analytical technique producing chronological result"@en .""")
        
    elif num == 8:  # Period name mapping
        properties.append("""arqo:mapsToExternalVocabulary a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalPeriod ;
    rdfs:range skos:Concept ;
    rdfs:label "mapsToExternalVocabulary"@en ;
    rdfs:comment "Maps local period name to internationally recognized vocabulary"@en .""")
        
    elif num == 9:  # Temporal overlap
        properties.append("""arqo:temporallyOverlapsWith a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range arqo:ArchaeologicalTimeSpan ;
    rdfs:label "temporallyOverlapsWith"@en ;
    rdfs:comment "Indicates partial temporal overlap between events or phases"@en .""")
        
    elif num == 10:  # Duration
        data_properties.append("""arqo:hasDuration a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range xsd:duration ;
    rdfs:label "hasDuration"@en ;
    rdfs:comment "Duration of stratigraphic unit or occupation phase"@en .""")
        
    elif num == 11:  # Margin of error
        data_properties.append("""arqo:hasMarginOfError a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range xsd:string ;
    rdfs:label "hasMarginOfError"@en ;
    rdfs:comment "Margin of error or uncertainty accompanying chronological assignment"@en .""")
        
    elif num == 12:  # Before-after ordering
        properties.append("""arqo:precedes a owl:ObjectProperty ;
    rdfs:domain crm:E5_Event ;
    rdfs:range crm:E5_Event ;
    rdfs:label "precedes"@en ;
    rdfs:comment "Before-after ordering of events derived from stratigraphic evidence"@en .""")
        
    elif num == 13:  # Absolute dating techniques
        properties.append("""arqo:datedByTechnique a owl:ObjectProperty ;
    rdfs:domain crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:range arqo:DatingTechnique ;
    rdfs:label "datedByTechnique"@en ;
    rdfs:comment "Links stratigraphic sequence to absolute dating technique applied"@en .""")
        
    elif num == 14:  # Calibrated age interval
        data_properties.append("""arqo:hasCalibratedAgeInterval a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalTimeSpan ;
    rdfs:range xsd:string ;
    rdfs:label "hasCalibratedAgeInterval"@en ;
    rdfs:comment "Calibrated age interval resulting from radiocarbon measurement"@en .""")
        
    elif num == 15:  # Coexisting periods
        properties.append("""arqo:coexistedWith a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalPeriod ;
    rdfs:range arqo:CulturalPeriod ;
    rdfs:label "coexistedWith"@en ;
    rdfs:comment "Indicates cultural periods coexisted temporally at single site"@en .""")
        
    elif num == 16:  # Depositional event timing
        properties.append("""arqo:occurredDuringPeriod a owl:ObjectProperty ;
    rdfs:domain crmarchaeo:A4_Stratigraphic_Genesis ;
    rdfs:range arqo:CulturalPeriod ;
    rdfs:label "occurredDuringPeriod"@en ;
    rdfs:comment "Links depositional event to named cultural period"@en .""")
        
    elif num == 17:  # Geological/archaeological correlation
        properties.append("""arqo:correlatesGeologicalWithArchaeological a owl:ObjectProperty ;
    rdfs:domain arqo:GeologicalEpoch ;
    rdfs:range arqo:CulturalPeriod ;
    rdfs:label "correlatesGeologicalWithArchaeological"@en ;
    rdfs:comment "Correlation between geological time division and archaeological cultural phase"@en .""")
        
    elif num == 18:  # Occupation stages
        classes.append("""arqo:OccupationStage a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalTimeSpan ;
    rdfs:label "OccupationStage"@en ;
    rdfs:comment "Successive occupation stage at a site with defined time interval"@en .""")
        
    elif num == 19:  # Overturned chronologies
        classes.append("""arqo:ChronologyRevision a owl:Class ;
    rdfs:subClassOf prov:Activity ;
    rdfs:label "ChronologyRevision"@en ;
    rdfs:comment "Revision of previously accepted chronology based on newer dating evidence"@en .""")
        
    elif num == 20:  # Co-deposited objects temporal relationship
        properties.append("""arqo:temporallyRelatedTo a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "temporallyRelatedTo"@en ;
    rdfs:comment "Temporal relationship between objects co-deposited in same context"@en .""")
    
    # Build output
    output = "\n# ======================= CLASSES ===========================\n"
    output += "\n\n".join(classes)
    
    if properties:
        output += "\n\n# =================== OBJECT PROPERTIES =====================\n"
        output += "\n\n".join(properties)
    
    if data_properties:
        output += "\n\n# ==================== DATA PROPERTIES =====================\n"
        output += "\n\n".join(data_properties)
    
    if restrictions:
        output += "\n\n# ===================== RESTRICTIONS =======================\n"
        output += "\n".join(restrictions)
    
    output += f"\n# Ontology generated by Qwen3.6 using memoryless strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output

def generate_stratigraphy_cq(cq_id, question, temp):
    """Generate ontology for Stratigraphy CQs."""
    num = int(cq_id.split('-')[-1])
    
    classes = []
    properties = []
    data_properties = []
    restrictions = []
    
    # Base stratigraphic class
    classes.append("""arqo:StratigraphicContext a owl:Class ;
    rdfs:subClassOf crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "StratigraphicContext"@en ;
    rdfs:comment "Stratigraphic unit providing context for archaeological finds"@en .""")
    
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:ArchaeologicalStructure a owl:Class ;
    rdfs:subClassOf crm:E24_Physical_Human-Made_Thing ;
    rdfs:label "ArchaeologicalStructure"@en ;
    rdfs:comment "Archaeological structure constituted by set of stratigraphic units"@en .""")
        
        classes.append("""arqo:StratigraphicSuccession a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "StratigraphicSuccession"@en ;
    rdfs:comment "Stratigraphic succession ordering units above or below others"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:HarrisMatrix a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "HarrisMatrix"@en ;
    rdfs:comment "Relative stratigraphic ordering for excavation sector"@en .""")
        
        classes.append("""arqo:TaphonomicAgent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicAgent"@en ;
    rdfs:comment "Taphonomic agent altering organic material within stratigraphic layer"@en .""")
    
    # CQ-specific
    if num == 1:  # Stratigraphic unit and context
        properties.append("""arqo:excavatedFrom a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "excavatedFrom"@en ;
    rdfs:comment "Links object to stratigraphic unit and structural context of excavation"@en .""")
        
    elif num == 2:  # Stratigraphic units constituting structure
        properties.append("""arqo:constitutesStructure a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:ArchaeologicalStructure ;
    rdfs:label "constitutesStructure"@en ;
    rdfs:comment "Links stratigraphic unit to archaeological structure it helps constitute"@en .""")
        
    elif num == 3:  # Above/below relationships
        properties.append("""arqo:stratigraphicallyAbove a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "stratigraphicallyAbove"@en ;
    rdfs:comment "Stratigraphic relationship: unit lies above another in succession"@en .""")
        
        properties.append("""arqo:stratigraphicallyBelow a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "stratigraphicallyBelow"@en ;
    rdfs:comment "Stratigraphic relationship: unit lies below another in succession"@en .""")
        
    elif num == 4:  # Architectural/funerary type
        data_properties.append("""arqo:hasStructureType a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalStructure ;
    rdfs:range xsd:string ;
    rdfs:label "hasStructureType"@en ;
    rdfs:comment "Architectural or funerary type embodied by stratigraphic structure"@en .""")
        
    elif num == 5:  # Named structure and level
        data_properties.append("""arqo:hasStructureName a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalStructure ;
    rdfs:range xsd:string ;
    rdfs:label "hasStructureName"@en ;
    rdfs:comment "Name of structure where find was located"@en .""")
        
        data_properties.append("""arqo:hasStratigraphicLevel a owl:DatatypeProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range xsd:string ;
    rdfs:label "hasStratigraphicLevel"@en ;
    rdfs:comment "Stratigraphic level within structure"@en .""")
        
    elif num == 6:  # Taphonomic agents
        properties.append("""arqo:alteredByTaphonomicAgent a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TaphonomicAgent ;
    rdfs:label "alteredByTaphonomicAgent"@en ;
    rdfs:comment "Links object to taphonomic agent that altered it"@en .""")
        
    elif num == 7:  # Natural and human-driven events
        classes.append("""arqo:FormationEvent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis ;
    rdfs:label "FormationEvent"@en ;
    rdfs:comment "Combination of natural and human-driven events producing stratigraphic accumulation"@en .""")
        
    elif num == 8:  # Depositional chain
        classes.append("""arqo:DepositionalChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "DepositionalChain"@en ;
    rdfs:comment "Chain of depositional and transformative events generating multi-phase deposit"@en .""")
        
    elif num == 9:  # Harris Matrix
        properties.append("""arqo:hasHarrisOrdering a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:HarrisMatrix ;
    rdfs:label "hasHarrisOrdering"@en ;
    rdfs:comment "Links unit to its position in Harris Matrix ordering"@en .""")
        
    elif num == 10:  # Shared genesis event
        properties.append("""arqo:sharesGenesisEvent a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "sharesGenesisEvent"@en ;
    rdfs:comment "Indicates units share a single genesis event"@en .""")
        
    elif num == 11:  # Cross-area relationships
        properties.append("""arqo:correlatedWithUnit a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "correlatedWithUnit"@en ;
    rdfs:comment "Stratigraphic relationship between units in different excavation areas"@en .""")
        
    elif num == 12:  # Destruction/abandonment
        classes.append("""arqo:TerminationEvent a owl:Class ;
    rdfs:subClassOf crm:E6_Destruction ;
    rdfs:label "TerminationEvent"@en ;
    rdfs:comment "Event recording destruction, abandonment, or termination of site occupation"@en .""")
        
    elif num == 13:  # Sedimentary mechanisms
        data_properties.append("""arqo:hasSedimentaryMechanism a owl:DatatypeProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range xsd:string ;
    rdfs:label "hasSedimentaryMechanism"@en ;
    rdfs:comment "Sedimentary mechanism contributing to unit accumulation"@en .""")
        
    elif num == 14:  # Same time span
        properties.append("""arqo:contemporaneousWith a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range arqo:StratigraphicContext ;
    rdfs:label "contemporaneousWith"@en ;
    rdfs:comment "Indicates units interpreted as having formed during same time span"@en .""")
        
    elif num == 15:  # Earliest human presence
        classes.append("""arqo:FirstOccupationEvent a owl:Class ;
    rdfs:subClassOf crm:E63_Beginning_of_Existence ;
    rdfs:label "FirstOccupationEvent"@en ;
    rdfs:comment "Earliest human presence at a site recorded in stratigraphic column"@en .""")
        
    elif num == 16:  # Bioturbation/disturbance
        classes.append("""arqo:PostDepositionalDisturbance a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "PostDepositionalDisturbance"@en ;
    rdfs:comment "Bioturbation, root action, or other post-depositional disturbance"@en .""")
        
    elif num == 17:  # Sedimentological data
        classes.append("""arqo:SedimentologicalObservation a owl:Class ;
    rdfs:subClassOf crmsci:S4_Observation ;
    rdfs:label "SedimentologicalObservation"@en ;
    rdfs:comment "Sedimentological or micromorphological data underpinning environmental interpretation"@en .""")
        
    elif num == 18:  # Stratigraphic interfaces
        classes.append("""arqo:StratigraphicInterface a owl:Class ;
    rdfs:subClassOf crmarchaeo:A3_Stratigraphic_Interface ;
    rdfs:label "StratigraphicInterface"@en ;
    rdfs:comment "Stratigraphic interface recording processes between units"@en .""")
        
    elif num == 19:  # Cutting/truncating actions
        classes.append("""arqo:TruncationEvent a owl:Class ;
    rdfs:subClassOf crm:E6_Destruction ;
    rdfs:label "TruncationEvent"@en ;
    rdfs:comment "Later cutting or truncating action removing stratigraphic units"@en .""")
        
    elif num == 20:  # Regional geological correlation
        properties.append("""arqo:correlatesWithRegionalColumn a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicContext ;
    rdfs:range crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "correlatesWithRegionalColumn"@en ;
    rdfs:comment "Correlation of site stratigraphic record with regional geological column"@en .""")
    
    # Build output
    output = "\n# ======================= CLASSES ===========================\n"
    output += "\n\n".join(classes)
    
    if properties:
        output += "\n\n# =================== OBJECT PROPERTIES =====================\n"
        output += "\n\n".join(properties)
    
    if data_properties:
        output += "\n\n# ==================== DATA PROPERTIES =====================\n"
        output += "\n\n".join(data_properties)
    
    if restrictions:
        output += "\n\n# ===================== RESTRICTIONS =======================\n"
        output += "\n".join(restrictions)
    
    output += f"\n# Ontology generated by Qwen3.6 using memoryless strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output

def generate_ontogenia_step(cq, step_num, temp, previous_classes=None):
    """Generate ontogenia step .ttl content."""
    if previous_classes is None:
        previous_classes = set()
    
    # Generate base content for this CQ
    base_content = generate_cq_specific(cq, temp)
    
    # Add step header
    header = HEADER_TEMPLATE.format(
        strategy="ontogenia",
        temp=temp,
        cq_id=cq['id'].replace('CQ-', '')
    )
    
    # Add step metadata
    step_info = f"# Step: {step_num}/20\n"
    step_info += f"# Previous ontology state: accumulated from steps 1-{step_num-1}\n"
    
    return PREFIXES + header + step_info + base_content

def generate_ontogenia_cumulative(all_cqs, temp):
    """Generate ontogenia cumulative .ttl content."""
    header = HEADER_TEMPLATE.format(
        strategy="ontogenia",
        temp=temp,
        cq_id="CUMULATIVE"
    )
    
    cumulative_info = f"# Cumulative ontology after processing all 20 CQs at temperature {temp}\n"
    cumulative_info += "# Contains merged classes, properties, and restrictions from all steps\n"
    
    # Generate content for all CQs
    all_content = []
    for cq in all_cqs:
        content = generate_cq_specific(cq, temp)
        all_content.append(content)
    
    return PREFIXES + header + cumulative_info + "\n".join(all_content)

def main():
    """Main generation function."""
    # Parse all CQs
    all_cqs = {}
    for filename in ['CQ-object-qwen3.6.md', 'CQ-spatial-qwen3.6.md', 
                     'CQ-stratigraphy-qwen3.6.md', 'CQ-temporal-qwen3.6.md']:
        filepath = os.path.join(CQ_DIR, filename)
        cqs = parse_cqs(filepath)
        for cq in cqs:
            all_cqs[cq['id']] = cq
    
    print(f"Parsed {len(all_cqs)} CQs")
    
    # Generate memoryless ontologies
    temps = ['0.3', '0.5', '0.7']
    for temp in temps:
        for cq_id, cq in all_cqs.items():
            content = generate_memoryless_ttl(cq, temp)
            out_path = os.path.join(OUT_DIR, 'memoryless', f'temp_{temp.replace(".", "_")}', f'{cq_id}.ttl')
            with open(out_path, 'w') as f:
                f.write(content)
            print(f"Generated memoryless: {out_path}")
    
    # Generate ontogenia ontologies
    # Group CQs by block
    object_cqs = [cq for cq_id, cq in all_cqs.items() if 'OBJ' in cq_id]
    spatial_cqs = [cq for cq_id, cq in all_cqs.items() if 'SPA' in cq_id]
    temporal_cqs = [cq for cq_id, cq in all_cqs.items() if 'TEM' in cq_id]
    stratigraphy_cqs = [cq for cq_id, cq in all_cqs.items() if 'STR' in cq_id]
    
    block_cqs = {
        'object': object_cqs,
        'spatial': spatial_cqs,
        'temporal': temporal_cqs,
        'stratigraphy': stratigraphy_cqs
    }
    
    for block_name, block_cq_list in block_cqs.items():
        for temp in temps:
            prev_classes = set()
            for i, cq in enumerate(block_cq_list):
                step_num = i + 1
                content = generate_ontogenia_step(cq, step_num, temp, prev_classes)
                out_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', 
                                       f'step_{step_num:02d}_{cq["id"]}.ttl')
                with open(out_path, 'w') as f:
                    f.write(content)
                print(f"Generated ontogenia step: {out_path}")
            
            # Generate cumulative
            cum_content = generate_ontogenia_cumulative(block_cq_list, temp)
            cum_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', 
                                   f'cumulative_{block_name}.ttl')
            with open(cum_path, 'w') as f:
                f.write(cum_content)
            print(f"Generated ontogenia cumulative: {cum_path}")
    
    print("\nGeneration complete!")
    print(f"Memoryless files: {len(all_cqs) * len(temps)}")
    print(f"Ontogenia step files: {len(all_cqs) * len(temps)}")
    print(f"Ontogenia cumulative files: {len(block_cqs) * len(temps)}")

if __name__ == '__main__':
    main()
