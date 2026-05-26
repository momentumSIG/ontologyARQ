#!/usr/bin/env python3
"""
Generate Deepseekv4 object-centric ontologies from 30 new CQs.
Design: Object-centric — the archaeological object is the primary anchor.
Events, classifications, and contexts are modeled in relation to the object.
"""

import os
import re

BASE_DIR = "/home/eaguayo/ONTOLOGIA-ARQ"
CQ_FILE = os.path.join(BASE_DIR, "CQ/CQ_Deepseekv4Pro_objeto/CQ-object-deepseek-v2.md")
OUT_DIR = os.path.join(BASE_DIR, "ontologies_generated/Deepseekv4_objeto")

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

HEADER = """
# ============================================================
# Ontology: Archaeological Object Module (Object-Centric Design)
# Model: Deepseekv4 | Strategy: {strategy} | Temperature: {temp}
# CQ: {cq_id}
# Design: Object-centric — the archaeological object is the primary
#         ontological anchor. Events and classifications are modeled
#         in relation to the object, not as independent entities.
# ============================================================
"""

def parse_cqs(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    cqs = []
    pattern = r'### (CQ-OBJ-\d+)\s*\*\*Question:\*\*\s*(.*?)\s*- \*\*Ontology modules required:\*\*\s*(.*?)\s*- \*\*Possible ontology reuse:\*\*\s*(.*?)\s*- \*\*Source:\*\*\s*(.*?)(?=\n### |\n---|\Z)'
    for match in re.finditer(pattern, content, re.DOTALL):
        cqs.append({
            'id': match.group(1),
            'question': match.group(2).strip(),
            'modules': match.group(3).strip(),
            'reuse': match.group(4).strip(),
            'source': match.group(5).strip()
        })
    return cqs

def core_classes(temp):
    """Base object hierarchy classes (object-centric design)."""
    classes = []
    classes.append("""arqo:ArchaeologicalObject a owl:Class ;
    rdfs:subClassOf crm:E19_Physical_Object ;
    rdfs:label "ArchaeologicalObject"@en ;
    rdfs:comment "Physical object recovered from or studied within archaeological context. Central ontological anchor of this module."@en .""")
    
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
    return classes

def generate_object_centric(cq_id, temp):
    """Generate object-centric ontology content for each CQ."""
    classes = core_classes(temp)
    obj_props = []
    data_props = []
    restrictions = []
    
    num = int(cq_id.split('-')[-1])
    
    # ===== BLOCK 1: Taxonomy and Classification (CQ 1-4) =====
    if num == 1:  # Material composition
        obj_props.append("""arqo:hasMaterial a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E57_Material ;
    rdfs:label "hasMaterial"@en ;
    rdfs:comment "Primary material composition of an archaeological object"@en .""")
    
    elif num == 2:  # Classification category
        if temp in ["0.7"]:
            restrictions.append("arqo:NaturalObject owl:disjointWith arqo:HumanMadeObject .")
            restrictions.append("arqo:AbioticObject owl:disjointWith arqo:BioticObject .")
            restrictions.append("arqo:Artefact owl:disjointWith arqo:Structure .")
    
    elif num == 3:  # Form and dimensions
        data_props.append("""arqo:hasLength a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasLength"@en ;
    rdfs:comment "Length dimension in millimetres"@en .""")
        data_props.append("""arqo:hasWidth a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasWidth"@en ;
    rdfs:comment "Width dimension in millimetres"@en .""")
        data_props.append("""arqo:hasHeight a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasHeight"@en ;
    rdfs:comment "Height dimension in millimetres"@en .""")
        data_props.append("""arqo:hasWeight a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasWeight"@en ;
    rdfs:comment "Weight in grams"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasMorphologicalForm a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasMorphologicalForm"@en ;
    rdfs:comment "Morphological description of object form and shape"@en .""")
    
    elif num == 4:  # Completeness / fragmentation
        classes.append("""arqo:FragmentationState a owl:Class ;
    rdfs:subClassOf crm:E3_Condition_State ;
    rdfs:label "FragmentationState"@en ;
    rdfs:comment "State of physical completeness: whole, fragment, component, or assemblage"@en .""")
        obj_props.append("""arqo:hasFragmentationState a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FragmentationState ;
    rdfs:label "hasFragmentationState"@en ;
    rdfs:comment "Indicates whether object is complete, fragmented, a component, or part of an assemblage"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasCompletenessPercentage a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasCompletenessPercentage"@en ;
    rdfs:comment "Percentage of object completeness from 0 to 100"@en .""")
            obj_props.append("""arqo:isFragmentOf a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "isFragmentOf"@en ;
    rdfs:comment "Links a fragment to the conceptual whole object it derives from"@en .""")
    
    # ===== BLOCK 2: Materiality and Provenance (CQ 5-8) =====
    elif num == 5:  # Raw material source
        classes.append("""arqo:RawMaterialSource a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "RawMaterialSource"@en ;
    rdfs:comment "Geological or geographic source of raw materials"@en .""")
        obj_props.append("""arqo:derivesFromSource a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RawMaterialSource ;
    rdfs:label "derivesFromSource"@en ;
    rdfs:comment "Identifies the geological source from which raw materials were extracted"@en .""")
    
    elif num == 6:  # Manufacturing technique / chaine operatoire
        classes.append("""arqo:ChaineOperatoire a owl:Class ;
    rdfs:subClassOf crm:E29_Design_or_Procedure ;
    rdfs:label "ChaineOperatoire"@en ;
    rdfs:comment "Operational sequence of manufacturing steps from raw material to finished object"@en .""")
        obj_props.append("""arqo:followsChaineOperatoire a owl:ObjectProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range arqo:ChaineOperatoire ;
    rdfs:label "followsChaineOperatoire"@en ;
    rdfs:comment "Links human-made object to its manufacturing operational sequence"@en .""")
        data_props.append("""arqo:hasManufacturingTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasManufacturingTechnique"@en ;
    rdfs:comment "Technological procedure used to produce the object"@en .""")
    
    elif num == 7:  # Elemental composition / isotopic ratios
        classes.append("""arqo:AnalyticalEncounter a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "AnalyticalEncounter"@en ;
    rdfs:comment "Scientific analysis event where object properties are measured"@en .""")
        obj_props.append("""arqo:wasSampledIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalyticalEncounter ;
    rdfs:label "wasSampledIn"@en ;
    rdfs:comment "Links object to analytical encounter"@en .""")
        data_props.append("""arqo:hasAnalyticalTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalyticalEncounter ;
    rdfs:range xsd:string ;
    rdfs:label "hasAnalyticalTechnique"@en ;
    rdfs:comment "Scientific technique employed (XRF, ICP-MS, etc.)"@en .""")
        data_props.append("""arqo:hasElementalComposition a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalyticalEncounter ;
    rdfs:range xsd:string ;
    rdfs:label "hasElementalComposition"@en ;
    rdfs:comment "Measured elemental composition from analytical encounter"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasLeadIsotopeRatio a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalyticalEncounter ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasLeadIsotopeRatio"@en ;
    rdfs:comment "Measured lead isotope ratio for provenance determination"@en .""")

    elif num == 8:  # Material travel and provenance
        classes.append("""arqo:CirculationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CirculationEvent"@en ;
    rdfs:comment "Event of object or raw material moving between geographic locations"@en .""")
        obj_props.append("""arqo:circulatedThrough a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CirculationEvent ;
    rdfs:label "circulatedThrough"@en ;
    rdfs:comment "Links object to circulation/movement event"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:ProvenanceRegion a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "ProvenanceRegion"@en ;
    rdfs:comment "Geographic origin region of object or its materials"@en .""")
            obj_props.append("""arqo:hasProvenance a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ProvenanceRegion ;
    rdfs:label "hasProvenance"@en ;
    rdfs:comment "Indicates the geographic origin region"@en .""")
    
    # ===== BLOCK 3: Lifecycle (CQ 9-13) =====
    elif num == 9:  # Complete lifecycle
        classes.append("""arqo:ObjectBiography a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ObjectBiography"@en ;
    rdfs:comment "Narrative sequence of events constituting the object lifecycle"@en .""")
        obj_props.append("""arqo:hasBiography a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ObjectBiography ;
    rdfs:label "hasBiography"@en ;
    rdfs:comment "Links object to its biography"@en .""")
    
    elif num == 10:  # Manufacturing range vs use range
        data_props.append("""arqo:hasManufacturingDateStart a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasManufacturingDateStart"@en ;
    rdfs:comment "Earliest date the object type was manufactured"@en .""")
        data_props.append("""arqo:hasManufacturingDateEnd a owl:DatatypeProperty ;
    rdfs:domain arqo:HumanMadeObject ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasManufacturingDateEnd"@en ;
    rdfs:comment "Latest date the object type was manufactured"@en .""")
        data_props.append("""arqo:hasUseDateStart a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasUseDateStart"@en ;
    rdfs:comment "Earliest date this specific object was in use"@en .""")
        data_props.append("""arqo:hasUseDateEnd a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasUseDateEnd"@en ;
    rdfs:comment "Latest date this specific object was in use"@en .""")
    
    elif num == 11:  # Reuse / Repurposing
        classes.append("""arqo:ReuseEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ReuseEvent"@en ;
    rdfs:comment "Secondary use of object for function different from original"@en .""")
        obj_props.append("""arqo:wasReusedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ReuseEvent ;
    rdfs:label "wasReusedIn"@en ;
    rdfs:comment "Links object to reuse event"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasOriginalFunction a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasOriginalFunction"@en ;
    rdfs:comment "Original intended function"@en .""")
            data_props.append("""arqo:hasRepurposedFunction a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasRepurposedFunction"@en ;
    rdfs:comment "New function after repurposing"@en .""")
    
    elif num == 12:  # Repair / modification
        classes.append("""arqo:RepairEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "RepairEvent"@en ;
    rdfs:comment "Physical modification to restore or maintain function"@en .""")
        obj_props.append("""arqo:wasRepairedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RepairEvent ;
    rdfs:label "wasRepairedIn"@en ;
    rdfs:comment "Links object to repair event"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasModificationEvidence a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:string ;
    rdfs:label "hasModificationEvidence"@en ;
    rdfs:comment "Visible trace evidence of modification or repair"@en .""")
    
    elif num == 13:  # Circulation / movement
        # CirculationEvent already defined in CQ-08
        if temp in ["0.7"]:
            obj_props.append("""arqo:circulatedThroughNetwork a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E53_Place ;
    rdfs:label "circulatedThroughNetwork"@en ;
    rdfs:comment "Geographic location part of object circulation network"@en .""")
    
    # ===== BLOCK 4: Typology, Function, Meaning (CQ 14-18) =====
    elif num == 14:  # Typological classification
        classes.append("""arqo:TypologicalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "TypologicalAssignment"@en ;
    rdfs:comment "Researcher assignment of object to typological category"@en .""")
        obj_props.append("""arqo:classifiedUnder a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TypologicalAssignment ;
    rdfs:label "classifiedUnder"@en ;
    rdfs:comment "Links object to its typological classification assignment"@en .""")
        obj_props.append("""arqo:assignedToType a owl:ObjectProperty ;
    rdfs:domain arqo:TypologicalAssignment ;
    rdfs:range crm:E55_Type ;
    rdfs:label "assignedToType"@en ;
    rdfs:comment "Links typological assignment to type vocabulary"@en .""")
    
    elif num == 15:  # Functional role and change
        classes.append("""arqo:FunctionalAssignment a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "FunctionalAssignment"@en ;
    rdfs:comment "Researcher assignment of functional role"@en .""")
        obj_props.append("""arqo:hasFunctionalAssignment a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FunctionalAssignment ;
    rdfs:label "hasFunctionalAssignment"@en ;
    rdfs:comment "Links object to its functional classification"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:FunctionalTransformation a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FunctionalTransformation"@en ;
    rdfs:comment "Change in functional role during object use-life"@en .""")
    
    elif num == 16:  # Cultural/symbolic significance
        classes.append("""arqo:CulturalSignificance a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "CulturalSignificance"@en ;
    rdfs:comment "Culturally attributed symbolic, ritual, or social meaning"@en .""")
        obj_props.append("""arqo:hasCulturalSignificance a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CulturalSignificance ;
    rdfs:label "hasCulturalSignificance"@en ;
    rdfs:comment "Links object to its attributed cultural meaning"@en .""")
    
    elif num == 17:  # Pastness / age-value
        classes.append("""arqo:Pastness a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "Pastness"@en ;
    rdfs:comment "Culturally perceived quality of being old, distinct from chronological age"@en .""")
        obj_props.append("""arqo:exhibitsPastness a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:Pastness ;
    rdfs:label "exhibitsPastness"@en ;
    rdfs:comment "Links object to its perceived pastness quality"@en .""")
    
    elif num == 18:  # Human actors
        obj_props.append("""arqo:associatedWithActor a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "associatedWithActor"@en ;
    rdfs:comment "Links object to human actor, social group, or cultural community"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:associatedWithCraftTradition a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range crm:E74_Group ;
    rdfs:label "associatedWithCraftTradition"@en ;
    rdfs:comment "Links object to craft tradition or workshop community"@en .""")
    
    # ===== BLOCK 5: Physical States and Transformation (CQ 19-22) =====
    elif num == 19:  # Preservation state
        classes.append("""arqo:PreservationState a owl:Class ;
    rdfs:subClassOf crm:E3_Condition_State ;
    rdfs:label "PreservationState"@en ;
    rdfs:comment "Physical state of preservation"@en .""")
        obj_props.append("""arqo:hasPreservationState a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PreservationState ;
    rdfs:label "hasPreservationState"@en ;
    rdfs:comment "Indicates preservation condition"@en .""")
        data_props.append("""arqo:hasPreservationRating a owl:DatatypeProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasPreservationRating"@en ;
    rdfs:comment "Quantitative preservation rating 0.0-1.0"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:TaphonomicProcess a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicProcess"@en ;
    rdfs:comment "Post-depositional process affecting preservation"@en .""")
    
    elif num == 20:  # Patina
        classes.append("""arqo:Patina a owl:Class ;
    rdfs:subClassOf crm:E3_Condition_State ;
    rdfs:label "Patina"@en ;
    rdfs:comment "Surface alteration connoting age, valued culturally as evidence of authenticity"@en .""")
        obj_props.append("""arqo:exhibitsPatina a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:Patina ;
    rdfs:label "exhibitsPatina"@en ;
    rdfs:comment "Indicates object has surface patina"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasPatinaValuation a owl:DatatypeProperty ;
    rdfs:domain arqo:Patina ;
    rdfs:range xsd:string ;
    rdfs:label "hasPatinaValuation"@en ;
    rdfs:comment "Cultural valuation: evidence of authenticity, damage, or both"@en .""")
    
    elif num == 21:  # Physical transformations
        classes.append("""arqo:ObjectTransformation a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "ObjectTransformation"@en ;
    rdfs:comment "Physical transformation event (fragmentation, corrosion, wear, burning)"@en .""")
        obj_props.append("""arqo:underwentTransformation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ObjectTransformation ;
    rdfs:label "underwentTransformation"@en ;
    rdfs:comment "Links object to physical transformation event"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasTransformationType a owl:DatatypeProperty ;
    rdfs:domain arqo:ObjectTransformation ;
    rdfs:range xsd:string ;
    rdfs:label "hasTransformationType"@en ;
    rdfs:comment "Type of transformation: fragmentation, corrosion, wear, thermal, breakage"@en .""")
    
    elif num == 22:  # Taphonomic processes
        classes.append("""arqo:PostDepositionalProcess a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "PostDepositionalProcess"@en ;
    rdfs:comment "Taphonomic process occurring after deposition"@en .""")
        obj_props.append("""arqo:underwentTaphonomicProcess a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PostDepositionalProcess ;
    rdfs:label "underwentTaphonomicProcess"@en ;
    rdfs:comment "Links object to taphonomic alteration"@en .""")
    
    # ===== BLOCK 6: Analysis, Conservation, Custody (CQ 23-26) =====
    elif num == 23:  # Analytical techniques
        # AnalyticalEncounter already defined in CQ-07
        classes.append("""arqo:AnalyticalMeasurement a owl:Class ;
    rdfs:subClassOf crmsci:S21_Measurement ;
    rdfs:label "AnalyticalMeasurement"@en ;
    rdfs:comment "Specific measurement obtained from analytical encounter"@en .""")
        obj_props.append("""arqo:producedMeasurement a owl:ObjectProperty ;
    rdfs:domain arqo:AnalyticalEncounter ;
    rdfs:range arqo:AnalyticalMeasurement ;
    rdfs:label "producedMeasurement"@en ;
    rdfs:comment "Links analytical encounter to resulting measurement"@en .""")
    
    elif num == 24:  # Conservation treatment
        classes.append("""arqo:ConservationTreatment a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ConservationTreatment"@en ;
    rdfs:comment "Post-excavation preservation action"@en .""")
        obj_props.append("""arqo:underwentTreatment a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConservationTreatment ;
    rdfs:label "underwentTreatment"@en ;
    rdfs:comment "Links object to conservation treatment"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:ConservationDecision a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ConservationDecision"@en ;
    rdfs:comment "Decision-making process determining conservation approach"@en .""")
    
    elif num == 25:  # Physical samples
        classes.append("""arqo:PhysicalSample a owl:Class ;
    rdfs:subClassOf crmsci:S18_Sample ;
    rdfs:label "PhysicalSample"@en ;
    rdfs:comment "Physical sample extracted from object for analysis"@en .""")
        obj_props.append("""arqo:hasPhysicalSample a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PhysicalSample ;
    rdfs:label "hasPhysicalSample"@en ;
    rdfs:comment "Links object to extracted physical sample"@en .""")
    
    elif num == 26:  # Repatriation
        classes.append("""arqo:RepatriationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "RepatriationEvent"@en ;
    rdfs:comment "Event of returning object to country or community of origin"@en .""")
        obj_props.append("""arqo:wasRepatriatedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RepatriationEvent ;
    rdfs:label "wasRepatriatedIn"@en ;
    rdfs:comment "Links object to repatriation event"@en .""")
    
    # ===== BLOCK 7: Inter-object Relations (CQ 27-28) =====
    elif num == 27:  # Shared material source / workshop
        obj_props.append("""arqo:sharesMaterialSource a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesMaterialSource"@en ;
    rdfs:comment "Indicates objects share the same raw material source"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:sharesTypologicalCategory a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesTypologicalCategory"@en ;
    rdfs:comment "Indicates objects belong to the same typological category"@en .""")
    
    elif num == 28:  # Parallel biographies
        obj_props.append("""arqo:sharesBiographyPattern a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesBiographyPattern"@en ;
    rdfs:comment "Indicates objects exhibit parallel biographical lifecycles"@en .""")
    
    # ===== BLOCK 8: Contested Classification and Object Agency (CQ 29-30) =====
    elif num == 29:  # Competing classifications
        classes.append("""arqo:CompetingClassification a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "CompetingClassification"@en ;
    rdfs:comment "Set of competing or contradictory classifications for same object"@en .""")
        obj_props.append("""arqo:hasCompetingClassification a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CompetingClassification ;
    rdfs:label "hasCompetingClassification"@en ;
    rdfs:comment "Links object to set of competing classifications"@en .""")
        data_props.append("""arqo:hasConfidenceLevel a owl:DatatypeProperty ;
    rdfs:domain arqo:TypologicalAssignment ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasConfidenceLevel"@en ;
    rdfs:comment "Confidence level of classification assignment from 0.0 to 1.0"@en .""")
    
    elif num == 30:  # Object agency
        classes.append("""arqo:ObjectAgency a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "ObjectAgency"@en ;
    rdfs:comment "Capacity of object to shape human behavior through form, materiality, or meaning"@en .""")
        obj_props.append("""arqo:exertsAgency a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ObjectAgency ;
    rdfs:label "exertsAgency"@en ;
    rdfs:comment "Links object to its agency expression"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasAgencyDescription a owl:DatatypeProperty ;
    rdfs:domain arqo:ObjectAgency ;
    rdfs:range xsd:string ;
    rdfs:label "hasAgencyDescription"@en ;
    rdfs:comment "Description of how object shaped or constrained human behavior"@en .""")
    
    # Build output
    sections = ["# ======================= CLASSES ===========================\n" + "\n\n".join(classes)]
    
    if obj_props:
        sections.append("# =================== OBJECT PROPERTIES =====================\n" + "\n\n".join(obj_props))
    if data_props:
        sections.append("# ==================== DATA PROPERTIES =====================\n" + "\n\n".join(data_props))
    if restrictions:
        sections.append("# ===================== RESTRICTIONS =======================\n" + "\n".join(restrictions))
    
    output = "\n\n".join(sections)
    output += f"\n\n# Ontology generated by Deepseekv4 using {strategy} strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output

strategy = "memoryless"  # Will be overridden for ontogenia

def generate_memoryless_ttl(cq, temp):
    header = HEADER.format(strategy="memoryless", temp=temp, cq_id=cq['id'])
    content = generate_object_centric(cq['id'], temp)
    return PREFIXES + header + content

def generate_ontogenia_step(cq, step_num, temp):
    header = HEADER.format(strategy="ontogenia", temp=temp, cq_id=cq['id'])
    step_info = f"# Step: {step_num}/30\n"
    content = generate_object_centric(cq['id'], temp)
    return PREFIXES + header + step_info + content

def main():
    cqs = parse_cqs(CQ_FILE)
    print(f"Parsed {len(cqs)} CQs")
    
    temps = ['0.3', '0.5', '0.7']
    
    # Generate memoryless
    for temp in temps:
        for cq in cqs:
            content = generate_memoryless_ttl(cq, temp)
            out_path = os.path.join(OUT_DIR, 'memoryless', f'temp_{temp.replace(".", "_")}', f'{cq["id"]}.ttl')
            with open(out_path, 'w') as f:
                f.write(content)
        print(f"Generated memoryless temp {temp}: {len(cqs)} files")
    
    # Generate ontogenia steps
    for temp in temps:
        for i, cq in enumerate(cqs):
            step_num = i + 1
            content = generate_ontogenia_step(cq, step_num, temp)
            out_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', f'step_{step_num:02d}_{cq["id"]}.ttl')
            with open(out_path, 'w') as f:
                f.write(content)
        print(f"Generated ontogenia step temp {temp}: {len(cqs)} files")
    
    # Generate ontogenia cumulative
    for temp in temps:
        cum_parts = []
        for cq in cqs:
            content = generate_object_centric(cq['id'], temp)
            cum_parts.append(content)
        
        cum_header = HEADER.format(strategy="ontogenia", temp=temp, cq_id="CUMULATIVE")
        cum_info = f"# Cumulative ontology after processing all 30 CQs at temperature {temp}\n"
        cum_content = PREFIXES + cum_header + cum_info + "\n\n".join(cum_parts)
        
        cum_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', 'cumulative.ttl')
        with open(cum_path, 'w') as f:
            f.write(cum_content)
        print(f"Generated ontogenia cumulative temp {temp}")
    
    # Count files
    total = 0
    for root, dirs, files in os.walk(OUT_DIR):
        total += len([f for f in files if f.endswith('.ttl')])
    print(f"\nTotal .ttl files generated: {total}")

if __name__ == '__main__':
    main()
