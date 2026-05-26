#!/usr/bin/env python3
"""
Generate Deepseekv4 event-centric ontologies from the same 30 CQs.
Design: Event-centric — events are the primary ontological anchor.
Objects participate in events. Lifecycle = chain of events.
"""

import os

BASE_DIR = "/home/eaguayo/ONTOLOGIA-ARQ"
CQ_FILE = os.path.join(BASE_DIR, "CQ/CQ_Deepseekv4Pro_objeto/CQ-object-deepseek-v2.md")
OUT_DIR = os.path.join(BASE_DIR, "ontologies_generated/Deepseekv4_objeto_eventos")

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
# Ontology: Archaeological Object Module (Event-Centric Design)
# Model: Deepseekv4 | Strategy: {strategy} | Temperature: {temp}
# CQ: {cq_id}
# Design: Event-centric — events are the primary ontological anchor.
#         Objects participate in events. Lifecycle = event chain.
# ============================================================
"""

import re

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

def base_classes(temp):
    """Event-centric base classes — events first, objects secondary."""
    classes = []
    
    # Core object class — exists but events are primary
    classes.append("""arqo:ArchaeologicalObject a owl:Class ;
    rdfs:subClassOf crm:E19_Physical_Object ;
    rdfs:label "ArchaeologicalObject"@en ;
    rdfs:comment "Physical object recovered from archaeological investigation. Participates in lifecycles modelled as event chains."@en .""")
    
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:NaturalObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "NaturalObject"@en ;
    rdfs:comment "Object of natural origin"@en .""")
        classes.append("""arqo:HumanMadeObject a owl:Class ;
    rdfs:subClassOf arqo:ArchaeologicalObject ;
    rdfs:label "HumanMadeObject"@en ;
    rdfs:comment "Object created or modified by human action"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:AbioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "AbioticObject"@en .""")
        classes.append("""arqo:BioticObject a owl:Class ;
    rdfs:subClassOf arqo:NaturalObject ;
    rdfs:label "BioticObject"@en .""")
        classes.append("""arqo:Artefact a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Artefact"@en .""")
        classes.append("""arqo:Structure a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "Structure"@en .""")
        classes.append("""arqo:ArtisticExpression a owl:Class ;
    rdfs:subClassOf arqo:HumanMadeObject ;
    rdfs:label "ArtisticExpression"@en .""")
    
    # Core event classes (event-centric anchor)
    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:ProductionEvent a owl:Class ;
    rdfs:subClassOf crm:E12_Production ;
    rdfs:label "ProductionEvent"@en ;
    rdfs:comment "Event where an object is produced. Anchors the beginning of the object lifecycle."@en .""")
        classes.append("""arqo:UseEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "UseEvent"@en ;
    rdfs:comment "Event where an object is actively used"@en .""")
        classes.append("""arqo:DepositionEvent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis ;
    rdfs:label "DepositionEvent"@en ;
    rdfs:comment "Event where an object enters the archaeological record"@en .""")
    
    if temp == "0.7":
        classes.append("""arqo:RecoveryEvent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A1_Excavation_Process_Unit ;
    rdfs:label "RecoveryEvent"@en ;
    rdfs:comment "Event where an object is excavated or recovered"@en .""")
        classes.append("""arqo:ReuseEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ReuseEvent"@en ;
    rdfs:comment "Event where an object is reused for a new function"@en .""")
        classes.append("""arqo:RepairEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "RepairEvent"@en ;
    rdfs:comment "Event where an object is repaired or modified"@en .""")
        classes.append("""arqo:CirculationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CirculationEvent"@en ;
    rdfs:comment "Event where an object moves between locations"@en .""")
        classes.append("""arqo:TransformationEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "TransformationEvent"@en ;
    rdfs:comment "Event where an object undergoes physical change"@en .""")
        classes.append("""arqo:ConservationEvent a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ConservationEvent"@en ;
    rdfs:comment "Event where conservation treatment is applied"@en .""")
        classes.append("""arqo:SamplingEvent a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "SamplingEvent"@en ;
    rdfs:comment "Event where a sample is extracted for analysis"@en .""")
        classes.append("""arqo:RepatriationEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "RepatriationEvent"@en ;
    rdfs:comment "Event where an object is returned to its origin"@en .""")
    
    return classes


def generate_event_centric(cq_id, temp):
    """Generate event-centric ontology content for each CQ."""
    classes = base_classes(temp)
    obj_props = []
    data_props = []
    restrictions = []
    
    num = int(cq_id.split('-')[-1])
    
    # BLOCK 1: Taxonomy (1-4)
    if num == 1:  # Material composition
        obj_props.append("""arqo:usesMaterial a owl:ObjectProperty ;
    rdfs:domain arqo:ProductionEvent ;
    rdfs:range crm:E57_Material ;
    rdfs:label "usesMaterial"@en ;
    rdfs:comment "Material consumed in the production event"@en .""")
        obj_props.append("""arqo:participatedInProduction a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ProductionEvent ;
    rdfs:label "participatedInProduction"@en ;
    rdfs:comment "Object produced by this production event"@en .""")
    
    elif num == 2:  # Classification
        if temp == "0.7":
            restrictions.append("arqo:NaturalObject owl:disjointWith arqo:HumanMadeObject .")
            restrictions.append("arqo:AbioticObject owl:disjointWith arqo:BioticObject .")
    
    elif num == 3:  # Form / dimensions
        classes.append("""arqo:MeasurementEvent a owl:Class ;
    rdfs:subClassOf crmsci:S21_Measurement ;
    rdfs:label "MeasurementEvent"@en ;
    rdfs:comment "Event where object dimensions are measured"@en .""")
        obj_props.append("""arqo:wasMeasuredIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:MeasurementEvent ;
    rdfs:label "wasMeasuredIn"@en .""")
        data_props.append("""arqo:hasLengthValue a owl:DatatypeProperty ;
    rdfs:domain arqo:MeasurementEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasLengthValue"@en .""")
        data_props.append("""arqo:hasWeightValue a owl:DatatypeProperty ;
    rdfs:domain arqo:MeasurementEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasWeightValue"@en .""")
    
    elif num == 4:  # Fragmentation
        classes.append("""arqo:FragmentationEvent a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FragmentationEvent"@en ;
    rdfs:comment "Event where an object becomes fragmented"@en .""")
        obj_props.append("""arqo:wasFragmentedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FragmentationEvent ;
    rdfs:label "wasFragmentedIn"@en .""")
    
    # BLOCK 2: Materiality/Provenance (5-8)
    elif num == 5:  # Raw material source
        classes.append("""arqo:ExtractionEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ExtractionEvent"@en ;
    rdfs:comment "Event where raw materials are extracted from geological source"@en .""")
        obj_props.append("""arqo:extractedFrom a owl:ObjectProperty ;
    rdfs:domain arqo:ExtractionEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "extractedFrom"@en ;
    rdfs:comment "Geological source of extraction"@en .""")
        obj_props.append("""arqo:providedMaterialFor a owl:ObjectProperty ;
    rdfs:domain arqo:ExtractionEvent ;
    rdfs:range arqo:ProductionEvent ;
    rdfs:label "providedMaterialFor"@en ;
    rdfs:comment "Extraction event supplies materials to production"@en .""")
    
    elif num == 6:  # Chaine operatoire
        classes.append("""arqo:ManufacturingStep a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ManufacturingStep"@en ;
    rdfs:comment "Single step in the manufacturing chain"@en .""")
        obj_props.append("""arqo:follows a owl:ObjectProperty ;
    rdfs:domain arqo:ManufacturingStep ;
    rdfs:range arqo:ManufacturingStep ;
    rdfs:label "follows"@en ;
    rdfs:comment "Step ordering in chaine operatoire"@en .""")
        data_props.append("""arqo:hasStepDescription a owl:DatatypeProperty ;
    rdfs:domain arqo:ManufacturingStep ;
    rdfs:range xsd:string ;
    rdfs:label "hasStepDescription"@en .""")
    
    elif num == 7:  # Elemental analysis
        classes.append("""arqo:AnalysisEvent a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "AnalysisEvent"@en ;
    rdfs:comment "Scientific analysis event"@en .""")
        obj_props.append("""arqo:analysedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalysisEvent ;
    rdfs:label "analysedIn"@en .""")
        data_props.append("""arqo:hasAnalyticalTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalysisEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasAnalyticalTechnique"@en .""")
        data_props.append("""arqo:hasElementalResult a owl:DatatypeProperty ;
    rdfs:domain arqo:AnalysisEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasElementalResult"@en .""")
    
    elif num == 8:  # Material travel
        classes.append("""arqo:TransportEvent a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "TransportEvent"@en ;
    rdfs:comment "Event transporting materials between locations"@en .""")
        obj_props.append("""arqo:movedThrough a owl:ObjectProperty ;
    rdfs:domain arqo:TransportEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "movedThrough"@en .""")
    
    # BLOCK 3: Lifecycle (9-13)
    elif num == 9:  # Complete lifecycle
        classes.append("""arqo:LifecycleChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "LifecycleChain"@en ;
    rdfs:comment "Ordered chain of lifecycle events"@en .""")
        obj_props.append("""arqo:hasLifecyclePhase a owl:ObjectProperty ;
    rdfs:domain arqo:LifecycleChain ;
    rdfs:range crm:E5_Event ;
    rdfs:label "hasLifecyclePhase"@en .""")
    
    elif num == 10:  # Manufacturing vs use date
        data_props.append("""arqo:hasProductionDateStart a owl:DatatypeProperty ;
    rdfs:domain arqo:ProductionEvent ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasProductionDateStart"@en .""")
        data_props.append("""arqo:hasProductionDateEnd a owl:DatatypeProperty ;
    rdfs:domain arqo:ProductionEvent ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasProductionDateEnd"@en .""")
        data_props.append("""arqo:hasUseDateStart a owl:DatatypeProperty ;
    rdfs:domain arqo:UseEvent ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasUseDateStart"@en .""")
        data_props.append("""arqo:hasUseDateEnd a owl:DatatypeProperty ;
    rdfs:domain arqo:UseEvent ;
    rdfs:range xsd:dateTime ;
    rdfs:label "hasUseDateEnd"@en .""")
    
    elif num == 11:  # Reuse
        obj_props.append("""arqo:participatedInReuse a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ReuseEvent ;
    rdfs:label "participatedInReuse"@en .""")
    
    elif num == 12:  # Repair
        obj_props.append("""arqo:participatedInRepair a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RepairEvent ;
    rdfs:label "participatedInRepair"@en .""")
    
    elif num == 13:  # Circulation
        obj_props.append("""arqo:participatedInCirculation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CirculationEvent ;
    rdfs:label "participatedInCirculation"@en .""")
    
    # BLOCK 4: Typology/Function/Meaning (14-18)
    elif num == 14:  # Typological classification
        classes.append("""arqo:ClassificationEvent a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "ClassificationEvent"@en ;
    rdfs:comment "Event where a researcher assigns a typological classification"@en .""")
        obj_props.append("""arqo:wasClassifiedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ClassificationEvent ;
    rdfs:label "wasClassifiedIn"@en .""")
        obj_props.append("""arqo:assignedType a owl:ObjectProperty ;
    rdfs:domain arqo:ClassificationEvent ;
    rdfs:range crm:E55_Type ;
    rdfs:label "assignedType"@en .""")
    
    elif num == 15:  # Functional role
        obj_props.append("""arqo:performedFunctionIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:UseEvent ;
    rdfs:label "performedFunctionIn"@en ;
    rdfs:comment "Object performed a function in this use event"@en .""")
        data_props.append("""arqo:hasFunctionRole a owl:DatatypeProperty ;
    rdfs:domain arqo:UseEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasFunctionRole"@en .""")
    
    elif num == 16:  # Cultural significance
        classes.append("""arqo:CulturalAttributionEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "CulturalAttributionEvent"@en ;
    rdfs:comment "Event where cultural significance is attributed"@en .""")
        obj_props.append("""arqo:attributedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CulturalAttributionEvent ;
    rdfs:label "attributedIn"@en .""")
    
    elif num == 17:  # Pastness
        classes.append("""arqo:PastnessAssessment a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "PastnessAssessment"@en ;
    rdfs:comment "Event where pastness is perceived and assessed"@en .""")
        obj_props.append("""arqo:assessedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PastnessAssessment ;
    rdfs:label "assessedIn"@en .""")
    
    elif num == 18:  # Human actors
        obj_props.append("""arqo:involvedActor a owl:ObjectProperty ;
    rdfs:domain crm:E5_Event ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "involvedActor"@en ;
    rdfs:comment "Actor involved in this event"@en .""")
    
    # BLOCK 5: Physical states (19-22)
    elif num == 19:  # Preservation
        classes.append("""arqo:ConditionAssessment a owl:Class ;
    rdfs:subClassOf crmsci:S4_Observation ;
    rdfs:label "ConditionAssessment"@en ;
    rdfs:comment "Event where object condition is assessed"@en .""")
        obj_props.append("""arqo:conditionAssessedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConditionAssessment ;
    rdfs:label "conditionAssessedIn"@en .""")
        data_props.append("""arqo:hasConditionRating a owl:DatatypeProperty ;
    rdfs:domain arqo:ConditionAssessment ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasConditionRating"@en .""")
    
    elif num == 20:  # Patina
        classes.append("""arqo:PatinaFormationEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "PatinaFormationEvent"@en ;
    rdfs:comment "Event where patina forms on object surface"@en .""")
        obj_props.append("""arqo:developedPatinaIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PatinaFormationEvent ;
    rdfs:label "developedPatinaIn"@en .""")
    
    elif num == 21:  # Physical transformations
        obj_props.append("""arqo:underwentTransformation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TransformationEvent ;
    rdfs:label "underwentTransformation"@en .""")
        data_props.append("""arqo:hasTransformationType a owl:DatatypeProperty ;
    rdfs:domain arqo:TransformationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasTransformationType"@en .""")
    
    elif num == 22:  # Taphonomic processes
        classes.append("""arqo:TaphonomicEvent a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicEvent"@en ;
    rdfs:comment "Event where taphonomic process alters the object"@en .""")
        obj_props.append("""arqo:alteredBy a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TaphonomicEvent ;
    rdfs:label "alteredBy"@en .""")
    
    # BLOCK 6: Analysis/Conservation (23-26)
    elif num == 23:  # Analytical techniques
        obj_props.append("""arqo:wasAnalysedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalysisEvent ;
    rdfs:label "wasAnalysedIn"@en .""")
    
    elif num == 24:  # Conservation treatment
        obj_props.append("""arqo:participatedInConservation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConservationEvent ;
    rdfs:label "participatedInConservation"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:ConservationDecisionEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ConservationDecisionEvent"@en ;
    rdfs:comment "Event where conservation decisions are made"@en .""")
    
    elif num == 25:  # Sampling
        obj_props.append("""arqo:participatedInSampling a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:SamplingEvent ;
    rdfs:label "participatedInSampling"@en .""")
    
    elif num == 26:  # Repatriation
        obj_props.append("""arqo:participatedInRepatriation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RepatriationEvent ;
    rdfs:label "participatedInRepatriation"@en .""")
    
    # BLOCK 7: Inter-object (27-28)
    elif num == 27:  # Shared provenance
        obj_props.append("""arqo:sharesProductionEvent a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesProductionEvent"@en ;
    rdfs:comment "Both objects produced in the same event"@en .""")
    
    elif num == 28:  # Parallel biographies
        obj_props.append("""arqo:sharesLifecycleChain a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesLifecycleChain"@en ;
    rdfs:comment "Both objects follow similar lifecycle chains"@en .""")
    
    # BLOCK 8: Classification/Agency (29-30)
    elif num == 29:  # Competing classifications
        classes.append("""arqo:ReclassificationEvent a owl:Class ;
    rdfs:subClassOf crm:E17_Type_Assignment ;
    rdfs:label "ReclassificationEvent"@en ;
    rdfs:comment "Event where a previous classification is overridden"@en .""")
        obj_props.append("""arqo:overrides a owl:ObjectProperty ;
    rdfs:domain arqo:ReclassificationEvent ;
    rdfs:range arqo:ClassificationEvent ;
    rdfs:label "overrides"@en ;
    rdfs:comment "New classification overrides previous one"@en .""")
        data_props.append("""arqo:hasConfidenceLevel a owl:DatatypeProperty ;
    rdfs:domain arqo:ClassificationEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasConfidenceLevel"@en .""")
    
    elif num == 30:  # Object agency
        classes.append("""arqo:AgencyExpressionEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "AgencyExpressionEvent"@en ;
    rdfs:comment "Event where object agency shapes human behavior"@en .""")
        obj_props.append("""arqo:expressedAgencyIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AgencyExpressionEvent ;
    rdfs:label "expressedAgencyIn"@en .""")
        obj_props.append("""arqo:affectedActor a owl:ObjectProperty ;
    rdfs:domain arqo:AgencyExpressionEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "affectedActor"@en ;
    rdfs:comment "Actor whose behavior was shaped by object agency"@en .""")
    
    # Build output
    sections = ["# ======================= CLASSES ===========================\n" + "\n\n".join(classes)]
    
    if obj_props:
        sections.append("# =================== OBJECT PROPERTIES =====================\n" + "\n\n".join(obj_props))
    if data_props:
        sections.append("# ==================== DATA PROPERTIES =====================\n" + "\n\n".join(data_props))
    if restrictions:
        sections.append("# ===================== RESTRICTIONS =======================\n" + "\n".join(restrictions))
    
    output = "\n\n".join(sections)
    output += f"\n\n# Ontology generated by Deepseekv4 using event-centric strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"
    
    return output


def main():
    cqs = parse_cqs(CQ_FILE)
    print(f"Parsed {len(cqs)} CQs")
    
    temps = ['0.3', '0.5', '0.7']
    
    for temp in temps:
        for cq in cqs:
            header = HEADER.format(strategy="memoryless", temp=temp, cq_id=cq['id'])
            content = generate_event_centric(cq['id'], temp)
            out_path = os.path.join(OUT_DIR, 'memoryless', f'temp_{temp.replace(".", "_")}', f'{cq["id"]}.ttl')
            with open(out_path, 'w') as f:
                f.write(PREFIXES + header + content)
        print(f"Generated memoryless temp {temp}: {len(cqs)} files")
    
    for temp in temps:
        for i, cq in enumerate(cqs):
            step_num = i + 1
            header = HEADER.format(strategy="ontogenia", temp=temp, cq_id=cq['id'])
            step_info = f"# Step: {step_num}/30\n"
            content = generate_event_centric(cq['id'], temp)
            out_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', f'step_{step_num:02d}_{cq["id"]}.ttl')
            with open(out_path, 'w') as f:
                f.write(PREFIXES + header + step_info + content)
        print(f"Generated ontogenia steps temp {temp}: {len(cqs)} files")
    
    for temp in temps:
        cum_parts = []
        for cq in cqs:
            cum_parts.append(generate_event_centric(cq['id'], temp))
        cum_header = HEADER.format(strategy="ontogenia", temp=temp, cq_id="CUMULATIVE")
        cum_info = f"# Cumulative ontology after processing all 30 CQs at temperature {temp}\n"
        cum_content = PREFIXES + cum_header + cum_info + "\n\n".join(cum_parts)
        cum_path = os.path.join(OUT_DIR, 'ontogenia', f'temp_{temp.replace(".", "_")}', 'cumulative.ttl')
        with open(cum_path, 'w') as f:
            f.write(cum_content)
        print(f"Generated cumulative temp {temp}")
    
    total = 0
    for root, dirs, files in os.walk(OUT_DIR):
        total += len([f for f in files if f.endswith('.ttl')])
    print(f"\nTotal .ttl files: {total}")

if __name__ == '__main__':
    main()
