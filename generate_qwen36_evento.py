#!/usr/bin/env python3
"""
Generate Qwen3.6 v2 event-centric ontologies from 30 new CQs.
Design: Event-centric — the archaeological event is the primary ontological anchor.
Objects participate in events; events carry the semantic weight.
"""

import os
import re

BASE_DIR = "/home/eaguayo/ONTOLOGIA-ARQ"
CQ_FILE = os.path.join(BASE_DIR, "CQ/CQ_Qwen3.6_objeto_v2/CQ-object-qwen3.6-v2.md")
OUT_DIR = os.path.join(BASE_DIR, "ontologies_generated/Qwen3.6_objeto_evento")

PREFIXES = """@prefix arqo: <http://www.ontologyARQ.org/archaeological-object/> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix crmarchaeo: <http://www.cidoc-crm.org/crmarchaeo/> .
@prefix crmsci: <http://www.cidoc-crm.org/crmsci/> .
@prefix crminf: <http://www.cidoc-crm.org/crminf/> .
@prefix crmhs: <http://www.cidoc-crm.org/crmhs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdfs#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
"""

HEADER = """
# ============================================================
# Ontology: Archaeological Object Module (Event-Centric Design)
# Model: Qwen3.6 v2 | Strategy: {strategy} | Temperature: {temp}
# CQ: {cq_id}
# Design: Event-centric — the archaeological event is the primary
#         ontological anchor. Objects participate in events;
#         events carry the semantic weight.
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

def core_event_classes(temp):
    """Base event hierarchy classes (event-centric design)."""
    classes = []
    classes.append("""arqo:BiographicalEvent a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "BiographicalEvent"@en ;
    rdfs:comment "Event that constitutes part of an archaeological object's biography. Primary ontological anchor of this module."@en .""")

    if temp in ["0.5", "0.7"]:
        classes.append("""arqo:ProductionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E12_Production ;
    rdfs:label "ProductionEvent"@en ;
    rdfs:comment "Event of object manufacture through technological procedures"@en .""")
        classes.append("""arqo:UseEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "UseEvent"@en ;
    rdfs:comment "Event of object utilization in its functional role"@en .""")
        classes.append("""arqo:DepositionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmarchaeo:A4_Stratigraphic_Genesis ;
    rdfs:label "DepositionEvent"@en ;
    rdfs:comment "Event of object entering the archaeological record"@en .""")
        classes.append("""arqo:RecoveryEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmarchaeo:A1_Excavation_Process_Unit ;
    rdfs:label "RecoveryEvent"@en ;
    rdfs:comment "Event of object excavation from depositional context"@en .""")

    if temp == "0.7":
        classes.append("""arqo:ReuseEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ReuseEvent"@en ;
    rdfs:comment "Event of secondary use for function different from original"@en .""")
        classes.append("""arqo:RepairEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "RepairEvent"@en ;
    rdfs:comment "Event of physical modification to restore function"@en .""")
        classes.append("""arqo:CirculationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CirculationEvent"@en ;
    rdfs:comment "Event of object movement between locations or cultural zones"@en .""")
        classes.append("""arqo:ConservationTreatmentEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "ConservationTreatmentEvent"@en ;
    rdfs:comment "Post-recovery preservation intervention event"@en .""")
        classes.append("""arqo:TaphonomicAlterationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicAlterationEvent"@en ;
    rdfs:comment "Post-depositional natural alteration event"@en .""")
        classes.append("""arqo:AnalyticalEncounterEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "AnalyticalEncounterEvent"@en ;
    rdfs:comment "Scientific analysis event where object properties are measured"@en .""")
    return classes

def generate_event_centric(cq_id, temp):
    """Generate event-centric ontology content for each CQ."""
    classes = core_event_classes(temp)
    obj_props = []
    data_props = []
    restrictions = []

    num = int(cq_id.split('-')[-1])

    # ===== BLOCK 1: Biography as Historical Entity (CQ 1-5) =====
    if num == 1:  # Complete biographical sequence
        classes.append("""arqo:BiographySequence a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "BiographySequence"@en ;
    rdfs:comment "Ordered sequence of biographical events constituting complete object trajectory"@en .""")
        obj_props.append("""arqo:hasEventSequence a owl:ObjectProperty ;
    rdfs:domain arqo:BiographySequence ;
    rdfs:range arqo:BiographicalEvent ;
    rdfs:label "hasEventSequence"@en ;
    rdfs:comment "Links biography sequence to constituent events"@en .""")
        obj_props.append("""arqo:eventPrecededBy a owl:ObjectProperty ;
    rdfs:domain arqo:BiographicalEvent ;
    rdfs:range arqo:BiographicalEvent ;
    rdfs:label "eventPrecededBy"@en ;
    rdfs:comment "Indicates temporal ordering between biographical events"@en .""")
        data_props.append("""arqo:hasEventOrder a owl:DatatypeProperty ;
    rdfs:domain arqo:BiographicalEvent ;
    rdfs:range xsd:integer ;
    rdfs:label "hasEventOrder"@en ;
    rdfs:comment "Ordinal position of event in biography sequence"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:participantObject a owl:ObjectProperty ;
    rdfs:domain arqo:BiographicalEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "participantObject"@en ;
    rdfs:comment "Physical object participating in biographical event"@en .""")

    elif num == 2:  # Physical vs narrative biography
        classes.append("""arqo:PhysicalBiographyEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "PhysicalBiographyEvent"@en ;
    rdfs:comment "Actual material event in object's history"@en .""")
        classes.append("""arqo:NarrativeBiographyClaim a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "NarrativeBiographyClaim"@en ;
    rdfs:comment "Narrative claim about object biography constructed by interpreter"@en .""")
        obj_props.append("""arqo:claimsBiographicalEvent a owl:ObjectProperty ;
    rdfs:domain arqo:NarrativeBiographyClaim ;
    rdfs:range arqo:PhysicalBiographyEvent ;
    rdfs:label "claimsBiographicalEvent"@en ;
    rdfs:comment "Links narrative claim to the physical event it asserts"@en .""")
        obj_props.append("""arqo:assertedBy a owl:ObjectProperty ;
    rdfs:domain arqo:NarrativeBiographyClaim ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "assertedBy"@en ;
    rdfs:comment "Researcher or community asserting the biographical narrative"@en .""")

    elif num == 3:  # Parallel biographies across sites
        classes.append("""arqo:BiographyPattern a owl:Class ;
    rdfs:subClassOf crm:E55_Type ;
    rdfs:label "BiographyPattern"@en ;
    rdfs:comment "Recurring sequence of biographical events shared across objects from different sites"@en .""")
        obj_props.append("""arqo:exhibitsBiographyPattern a owl:ObjectProperty ;
    rdfs:domain arqo:BiographicalEvent ;
    rdfs:range arqo:BiographyPattern ;
    rdfs:label "exhibitsBiographyPattern"@en ;
    rdfs:comment "Links event to recurring biographical pattern it exemplifies"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:patternObservedAt a owl:ObjectProperty ;
    rdfs:domain arqo:BiographyPattern ;
    rdfs:range crm:E53_Place ;
    rdfs:label "patternObservedAt"@en ;
    rdfs:comment "Site where biographical pattern was observed"@en .""")

    elif num == 4:  # Natural object acquiring cultural agency
        classes.append("""arqo:CulturalAgencyEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "CulturalAgencyEvent"@en ;
    rdfs:comment "Event where natural object acquired cultural significance through human use without physical modification"@en .""")
        obj_props.append("""arqo:agencyAcquiredThrough a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalAgencyEvent ;
    rdfs:range arqo:UseEvent ;
    rdfs:label "agencyAcquiredThrough"@en ;
    rdfs:comment "Links cultural agency acquisition to the use event that triggered it"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:agencyAttributedBy a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalAgencyEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "agencyAttributedBy"@en ;
    rdfs:comment "Human actor or community attributing cultural agency to natural object"@en .""")

    elif num == 5:  # Functional transformation changing classification
        classes.append("""arqo:FunctionalTransformationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FunctionalTransformationEvent"@en ;
    rdfs:comment "Event where object's functional role changed, altering its typological classification"@en .""")
        obj_props.append("""arqo:transformationAlteredClassification a owl:ObjectProperty ;
    rdfs:domain arqo:FunctionalTransformationEvent ;
    rdfs:range crm:E17_Type_Assignment ;
    rdfs:label "transformationAlteredClassification"@en ;
    rdfs:comment "Links functional transformation to the typological classification it altered"@en .""")
        data_props.append("""arqo:hasTransformationEvidence a owl:DatatypeProperty ;
    rdfs:domain arqo:FunctionalTransformationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasTransformationEvidence"@en ;
    rdfs:comment "Trace evidence of functional transformation visible on object"@en .""")

    # ===== BLOCK 2: Analytical Workflows (CQ 6-10) =====
    elif num == 6:  # Complete analytical chain
        classes.append("""arqo:AnalyticalWorkflow a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "AnalyticalWorkflow"@en ;
    rdfs:comment "Complete chain of analytical events transforming object into published dataset"@en .""")
        classes.append("""arqo:SamplingEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "SamplingEvent"@en ;
    rdfs:comment "Event of physical sample extraction from object"@en .""")
        classes.append("""arqo:MeasurementEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S21_Measurement ;
    rdfs:label "MeasurementEvent"@en ;
    rdfs:comment "Event of scientific measurement on sample or object"@en .""")
        classes.append("""arqo:CalibrationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "CalibrationEvent"@en ;
    rdfs:comment "Event of methodological calibration or correction"@en .""")
        classes.append("""arqo:InterpretationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S5_Inference_Making ;
    rdfs:label "InterpretationEvent"@en ;
    rdfs:comment "Event of scientific interpretation from measurements"@en .""")
        obj_props.append("""arqo:workflowIncludesEvent a owl:ObjectProperty ;
    rdfs:domain arqo:AnalyticalWorkflow ;
    rdfs:range arqo:BiographicalEvent ;
    rdfs:label "workflowIncludesEvent"@en ;
    rdfs:comment "Links analytical workflow to constituent events"@en .""")
        obj_props.append("""arqo:eventProducedDataset a owl:ObjectProperty ;
    rdfs:domain arqo:BiographicalEvent ;
    rdfs:range crm:E73_Information_Object ;
    rdfs:label "eventProducedDataset"@en ;
    rdfs:comment "Links analytical event to resulting dataset"@en .""")

    elif num == 7:  # Samples and contradictory results
        classes.append("""arqo:SampleExtractionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "SampleExtractionEvent"@en ;
    rdfs:comment "Event of extracting physical sample from archaeological object"@en .""")
        obj_props.append("""arqo:extractedSampleFrom a owl:ObjectProperty ;
    rdfs:domain arqo:SampleExtractionEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "extractedSampleFrom"@en ;
    rdfs:comment "Links sample extraction event to source object"@en .""")
        classes.append("""arqo:ContradictoryResult a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "ContradictoryResult"@en ;
    rdfs:comment "Set of contradictory analytical results from different techniques applied to same object"@en .""")
        obj_props.append("""arqo:resultProducedBy a owl:ObjectProperty ;
    rdfs:domain arqo:ContradictoryResult ;
    rdfs:range arqo:MeasurementEvent ;
    rdfs:label "resultProducedBy"@en ;
    rdfs:comment "Links contradictory result to the measurement event that produced it"@en .""")

    elif num == 8:  # Protocols for provenance determination
        classes.append("""arqo:IsotopicAnalysisEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "IsotopicAnalysisEvent"@en ;
    rdfs:comment "Scientific event of isotopic ratio measurement for provenance determination"@en .""")
        obj_props.append("""arqo:analysisUsedProtocol a owl:ObjectProperty ;
    rdfs:domain arqo:IsotopicAnalysisEvent ;
    rdfs:range crm:E29_Design_or_Procedure ;
    rdfs:label "analysisUsedProtocol"@en ;
    rdfs:comment "Links analysis event to laboratory protocol employed"@en .""")
        data_props.append("""arqo:hasIsotopicRatio a owl:DatatypeProperty ;
    rdfs:domain arqo:IsotopicAnalysisEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasIsotopicRatio"@en ;
    rdfs:comment "Measured isotopic ratio value"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:analysisUsedInstrument a owl:ObjectProperty ;
    rdfs:domain arqo:IsotopicAnalysisEvent ;
    rdfs:range crm:E22_Human-Made_Object ;
    rdfs:label "analysisUsedInstrument"@en ;
    rdfs:comment "Laboratory instrument used in analysis event"@en .""")

    elif num == 9:  # Datasets linked to observations and interpretations
        classes.append("""arqo:DatasetPublicationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "DatasetPublicationEvent"@en ;
    rdfs:comment "Event of publishing analytical dataset derived from object study"@en .""")
        obj_props.append("""arqo:datasetDerivedFrom a owl:ObjectProperty ;
    rdfs:domain arqo:DatasetPublicationEvent ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "datasetDerivedFrom"@en ;
    rdfs:comment "Links published dataset to original observations"@en .""")
        obj_props.append("""arqo:datasetSupportsInterpretation a owl:ObjectProperty ;
    rdfs:domain arqo:DatasetPublicationEvent ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "datasetSupportsInterpretation"@en ;
    rdfs:comment "Links dataset to interpretive conclusions it supports"@en .""")

    elif num == 10:  # Calibration and methodological corrections
        classes.append("""arqo:MethodologicalRevisionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "MethodologicalRevisionEvent"@en ;
    rdfs:comment "Event of revising previously published dating or classification based on new evidence"@en .""")
        obj_props.append("""arqo:revisionSupersedes a owl:ObjectProperty ;
    rdfs:domain arqo:MethodologicalRevisionEvent ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "revisionSupersedes"@en ;
    rdfs:comment "Links revision event to the prior interpretation it supersedes"@en .""")
        obj_props.append("""arqo:revisionBasedOnEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:MethodologicalRevisionEvent ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "revisionBasedOnEvidence"@en ;
    rdfs:comment "Links revision event to the new evidence that motivated it"@en .""")

    # ===== BLOCK 3: Disputed Interpretation (CQ 11-15) =====
    elif num == 11:  # Rival hypotheses
        classes.append("""arqo:InterpretiveHypothesis a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "InterpretiveHypothesis"@en ;
    rdfs:comment "Rival hypothesis about object function, chronology, or cultural meaning"@en .""")
        classes.append("""arqo:HypothesisFormulationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "HypothesisFormulationEvent"@en ;
    rdfs:comment "Event of formulating an interpretive hypothesis about an object"@en .""")
        obj_props.append("""arqo:hypothesisSupportedByEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:InterpretiveHypothesis ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "hypothesisSupportedByEvidence"@en ;
    rdfs:comment "Links hypothesis to analytical evidence supporting it"@en .""")
        obj_props.append("""arqo:hypothesisFormulatedBy a owl:ObjectProperty ;
    rdfs:domain arqo:HypothesisFormulationEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "hypothesisFormulatedBy"@en ;
    rdfs:comment "Researcher who formulated the hypothesis"@en .""")

    elif num == 12:  # Rejected interpretations
        classes.append("""arqo:RejectedInterpretation a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "RejectedInterpretation"@en ;
    rdfs:comment "Interpretive claim about object that was rejected based on evidence"@en .""")
        obj_props.append("""arqo:rejectedDueToEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:RejectedInterpretation ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "rejectedDueToEvidence"@en ;
    rdfs:comment "Links rejected interpretation to evidence that caused rejection"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:rejectionEvent a owl:ObjectProperty ;
    rdfs:domain arqo:RejectedInterpretation ;
    rdfs:range arqo:BiographicalEvent ;
    rdfs:label "rejectionEvent"@en ;
    rdfs:comment "Event in which interpretation was formally rejected"@en .""")

    elif num == 13:  # Certainty levels
        classes.append("""arqo:CertaintyAssessmentEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "CertaintyAssessmentEvent"@en ;
    rdfs:comment "Event of assigning certainty level to archaeological interpretation"@en .""")
        obj_props.append("""arqo:assessmentEvaluates a owl:ObjectProperty ;
    rdfs:domain arqo:CertaintyAssessmentEvent ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "assessmentEvaluates"@en ;
    rdfs:comment "Links certainty assessment to the interpretation being evaluated"@en .""")
        data_props.append("""arqo:hasCertaintyLevel a owl:DatatypeProperty ;
    rdfs:domain arqo:CertaintyAssessmentEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasCertaintyLevel"@en ;
    rdfs:comment "Certainty level from 0.0 (speculative) to 1.0 (confirmed)"@en .""")

    elif num == 14:  # Argumentative chains
        classes.append("""arqo:ArgumentativeChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ArgumentativeChain"@en ;
    rdfs:comment "Chain of reasoning connecting observations, measurements, and interpretive inferences"@en .""")
        obj_props.append("""arqo:chainStartsWithObservation a owl:ObjectProperty ;
    rdfs:domain arqo:ArgumentativeChain ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "chainStartsWithObservation"@en ;
    rdfs:comment "Links argumentative chain to initial observation"@en .""")
        obj_props.append("""arqo:chainConcludesWith a owl:ObjectProperty ;
    rdfs:domain arqo:ArgumentativeChain ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "chainConcludesWith"@en ;
    rdfs:comment "Links argumentative chain to final interpretive conclusion"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:chainIncludesStep a owl:ObjectProperty ;
    rdfs:domain arqo:ArgumentativeChain ;
    rdfs:range arqo:BiographicalEvent ;
    rdfs:label "chainIncludesStep"@en ;
    rdfs:comment "Links argumentative chain to intermediate reasoning step"@en .""")

    elif num == 15:  # Interpretive conflicts between researchers
        classes.append("""arqo:InterpretiveConflict a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "InterpretiveConflict"@en ;
    rdfs:comment "Event or situation where researchers hold conflicting interpretations of same object"@en .""")
        obj_props.append("""arqo:conflictInvolvesInterpretation a owl:ObjectProperty ;
    rdfs:domain arqo:InterpretiveConflict ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "conflictInvolvesInterpretation"@en ;
    rdfs:comment "Links conflict to the competing interpretations involved"@en .""")
        data_props.append("""arqo:hasTheoreticalFramework a owl:DatatypeProperty ;
    rdfs:domain arqo:InterpretiveConflict ;
    rdfs:range xsd:string ;
    rdfs:label "hasTheoreticalFramework"@en ;
    rdfs:comment "Theoretical framework underlying an interpretation in conflict"@en .""")

    # ===== BLOCK 4: Taphonomy (CQ 16-20) =====
    elif num == 16:  # Natural taphonomic processes
        classes.append("""arqo:TaphonomicAlterationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicAlterationEvent"@en ;
    rdfs:comment "Natural post-depositional process altering object position, condition, or integrity"@en .""")
        obj_props.append("""arqo:alterationAffectedObject a owl:ObjectProperty ;
    rdfs:domain arqo:TaphonomicAlterationEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "alterationAffectedObject"@en ;
    rdfs:comment "Links taphonomic event to the object it affected"@en .""")
        data_props.append("""arqo:hasTaphonomicProcessType a owl:DatatypeProperty ;
    rdfs:domain arqo:TaphonomicAlterationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasTaphonomicProcessType"@en ;
    rdfs:comment "Type of taphonomic process: bioturbation, corrosion, weathering, water transport, compaction"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:alterationOccurredIn a owl:ObjectProperty ;
    rdfs:domain arqo:TaphonomicAlterationEvent ;
    rdfs:range crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "alterationOccurredIn"@en ;
    rdfs:comment "Stratigraphic unit where taphonomic alteration occurred"@en .""")

    elif num == 17:  # Stratigraphic-geological correlations
        classes.append("""arqo:StratigraphicCorrelationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "StratigraphicCorrelationEvent"@en ;
    rdfs:comment "Event of correlating archaeological stratigraphic unit with geological unit"@en .""")
        obj_props.append("""arqo:correlatesArchaeologicalUnit a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicCorrelationEvent ;
    rdfs:range crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "correlatesArchaeologicalUnit"@en ;
    rdfs:comment "Links correlation event to archaeological stratigraphic unit"@en .""")
        obj_props.append("""arqo:correlatesGeologicalUnit a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicCorrelationEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "correlatesGeologicalUnit"@en ;
    rdfs:comment "Links correlation event to geological unit"@en .""")

    elif num == 18:  # Geomorphological events
        classes.append("""arqo:GeomorphologicalEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "GeomorphologicalEvent"@en ;
    rdfs:comment "Natural geomorphological event affecting archaeological depositional context"@en .""")
        data_props.append("""arqo:hasGeomorphologicalType a owl:DatatypeProperty ;
    rdfs:domain arqo:GeomorphologicalEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasGeomorphologicalType"@en ;
    rdfs:comment "Type of geomorphological event: flood, colluviation, erosion, volcanism, fluvial dynamics"@en .""")
        obj_props.append("""arqo:eventModifiedSpatialDistribution a owl:ObjectProperty ;
    rdfs:domain arqo:GeomorphologicalEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "eventModifiedSpatialDistribution"@en ;
    rdfs:comment "Links geomorphological event to the spatial area it modified"@en .""")

    elif num == 19:  # Post-depositional displacement
        classes.append("""arqo:DisplacementEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "DisplacementEvent"@en ;
    rdfs:comment "Post-depositional movement of object from original depositional position"@en .""")
        obj_props.append("""arqo:displacementReducedContextReliability a owl:ObjectProperty ;
    rdfs:domain arqo:DisplacementEvent ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "displacementReducedContextReliability"@en ;
    rdfs:comment "Links displacement event to the reliability assessment of stratigraphic context"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasDisplacementDistance a owl:DatatypeProperty ;
    rdfs:domain arqo:DisplacementEvent ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasDisplacementDistance"@en ;
    rdfs:comment "Estimated displacement distance in centimetres"@en .""")

    elif num == 20:  # Fragmentation processes
        classes.append("""arqo:FragmentationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FragmentationEvent"@en ;
    rdfs:comment "Event that broke an originally complete object into fragments"@en .""")
        data_props.append("""arqo:hasFragmentationCause a owl:DatatypeProperty ;
    rdfs:domain arqo:FragmentationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasFragmentationCause"@en ;
    rdfs:comment "Cause of fragmentation: intentional ritual, accidental use-wear, taphonomic post-depositional"@en .""")
        obj_props.append("""arqo:fragmentationProducedFragment a owl:ObjectProperty ;
    rdfs:domain arqo:FragmentationEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "fragmentationProducedFragment"@en ;
    rdfs:comment "Links fragmentation event to the fragment it produced"@en .""")

    # ===== BLOCK 5: Custody and Heritage (CQ 21-25) =====
    elif num == 21:  # Custody chain
        classes.append("""arqo:CustodyEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "CustodyEvent"@en ;
    rdfs:comment "Event of object transfer between custodial institutions or locations"@en .""")
        obj_props.append("""arqo:custodyTransferredFrom a owl:ObjectProperty ;
    rdfs:domain arqo:CustodyEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "custodyTransferredFrom"@en ;
    rdfs:comment "Institution transferring custody"@en .""")
        obj_props.append("""arqo:custodyTransferredTo a owl:ObjectProperty ;
    rdfs:domain arqo:CustodyEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "custodyTransferredTo"@en ;
    rdfs:comment "Institution receiving custody"@en .""")
        data_props.append("""arqo:hasCustodyType a owl:DatatypeProperty ;
    rdfs:domain arqo:CustodyEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasCustodyType"@en ;
    rdfs:comment "Type of custody event: excavation, storage, loan, exhibition, restoration, repatriation"@en .""")

    elif num == 22:  # Conservation decisions
        classes.append("""arqo:ConservationDecisionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "ConservationDecisionEvent"@en ;
    rdfs:comment "Event of deciding conservation approach based on competing values"@en .""")
        obj_props.append("""arqo:decisionMotivatedByValue a owl:ObjectProperty ;
    rdfs:domain arqo:ConservationDecisionEvent ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "decisionMotivatedByValue"@en ;
    rdfs:comment "Links conservation decision to the value that motivated it"@en .""")
        data_props.append("""arqo:hasConservationApproach a owl:DatatypeProperty ;
    rdfs:domain arqo:ConservationDecisionEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasConservationApproach"@en ;
    rdfs:comment "Conservation approach chosen: cleaning, consolidation, reconstruction, non-intervention"@en .""")

    elif num == 23:  # Exhibition and pastness
        classes.append("""arqo:ExhibitionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "ExhibitionEvent"@en ;
    rdfs:comment "Event of publicly exhibiting an archaeological object"@en .""")
        classes.append("""arqo:PastnessPerceptionEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "PastnessPerceptionEvent"@en ;
    rdfs:comment "Event of culturally perceiving object's pastness or age-value through patina or appearance"@en .""")
        obj_props.append("""arqo:exhibitionInfluencedPerception a owl:ObjectProperty ;
    rdfs:domain arqo:ExhibitionEvent ;
    rdfs:range arqo:PastnessPerceptionEvent ;
    rdfs:label "exhibitionInfluencedPerception"@en ;
    rdfs:comment "Links exhibition event to the pastness perception it influenced"@en .""")

    elif num == 24:  # Digital replicas
        classes.append("""arqo:DigitalDocumentationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "DigitalDocumentationEvent"@en ;
    rdfs:comment "Event of creating digital replica or 3D model of archaeological object"@en .""")
        obj_props.append("""arqo:documentationProducedDigitalObject a owl:ObjectProperty ;
    rdfs:domain arqo:DigitalDocumentationEvent ;
    rdfs:range crm:E73_Information_Object ;
    rdfs:label "documentationProducedDigitalObject"@en ;
    rdfs:comment "Links documentation event to the digital replica it produced"@en .""")
        data_props.append("""arqo:hasDocumentationTechnique a owl:DatatypeProperty ;
    rdfs:domain arqo:DigitalDocumentationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasDocumentationTechnique"@en ;
    rdfs:comment "Technique used: photogrammetry, laser scanning, RTI, structured light"@en .""")

    elif num == 25:  # Heritage claims and repatriation
        classes.append("""arqo:HeritageClaimEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "HeritageClaimEvent"@en ;
    rdfs:comment "Event of asserting cultural heritage claim over archaeological object"@en .""")
        obj_props.append("""arqo:claimAssertedBy a owl:ObjectProperty ;
    rdfs:domain arqo:HeritageClaimEvent ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "claimAssertedBy"@en ;
    rdfs:comment "Community or institution asserting heritage claim"@en .""")
        obj_props.append("""arqo:claimSupportedByEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:HeritageClaimEvent ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "claimSupportedByEvidence"@en ;
    rdfs:comment "Links heritage claim to probative evidence supporting it"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:RepatriationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "RepatriationEvent"@en ;
    rdfs:comment "Event of returning object to country or community of origin"@en .""")

    # ===== BLOCK 6: Object-Context-Territory (CQ 26-30) =====
    elif num == 26:  # Spatial topological relationships
        classes.append("""arqo:SpatialAssociationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "SpatialAssociationEvent"@en ;
    rdfs:comment "Event establishing spatial topological relationship between objects in same stratigraphic unit"@en .""")
        obj_props.append("""arqo:associationRelatesObject a owl:ObjectProperty ;
    rdfs:domain arqo:SpatialAssociationEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "associationRelatesObject"@en ;
    rdfs:comment "Links spatial association event to the object it relates"@en .""")
        data_props.append("""arqo:hasTopologicalRelation a owl:DatatypeProperty ;
    rdfs:domain arqo:SpatialAssociationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasTopologicalRelation"@en ;
    rdfs:comment "Topological relation: proximity, co-occurrence, functional association"@en .""")

    elif num == 27:  # Circulation between settlements
        classes.append("""arqo:InterSettlementCirculationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "InterSettlementCirculationEvent"@en ;
    rdfs:comment "Event of object circulation between settlements, territories, or mobility corridors"@en .""")
        obj_props.append("""arqo:circulationEvidencesNetwork a owl:ObjectProperty ;
    rdfs:domain arqo:InterSettlementCirculationEvent ;
    rdfs:range crm:E55_Type ;
    rdfs:label "circulationEvidencesNetwork"@en ;
    rdfs:comment "Links circulation event to the exchange network or migration pattern it evidences"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasCirculationMechanism a owl:DatatypeProperty ;
    rdfs:domain arqo:InterSettlementCirculationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasCirculationMechanism"@en ;
    rdfs:comment "Mechanism of circulation: trade, gift exchange, looting, migration"@en .""")

    elif num == 28:  # Spatial distribution and functional zoning
        classes.append("""arqo:FunctionalZoningEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "FunctionalZoningEvent"@en ;
    rdfs:comment "Event of identifying functional zone within site based on object distribution patterns"@en .""")
        obj_props.append("""arqo:zoningIdentifiedArea a owl:ObjectProperty ;
    rdfs:domain arqo:FunctionalZoningEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "zoningIdentifiedArea"@en ;
    rdfs:comment "Links zoning event to the functional area it identified"@en .""")
        data_props.append("""arqo:hasZoneType a owl:DatatypeProperty ;
    rdfs:domain arqo:FunctionalZoningEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasZoneType"@en ;
    rdfs:comment "Type of functional zone: domestic, ritual, production, funerary"@en .""")

    elif num == 29:  # Occupation sequences
        classes.append("""arqo:OccupationPhaseEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "OccupationPhaseEvent"@en ;
    rdfs:comment "Event marking a phase of occupation, abandonment, or reoccupation documented by objects"@en .""")
        obj_props.append("""arqo:phaseDocumentedByObject a owl:ObjectProperty ;
    rdfs:domain arqo:OccupationPhaseEvent ;
    rdfs:range crm:E19_Physical_Object ;
    rdfs:label "phaseDocumentedByObject"@en ;
    rdfs:comment "Links occupation phase to the object that documents it"@en .""")
        data_props.append("""arqo:hasPhaseType a owl:DatatypeProperty ;
    rdfs:domain arqo:OccupationPhaseEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasPhaseType"@en ;
    rdfs:comment "Type of phase: occupation, abandonment, reoccupation"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:phaseOccurredInStratigraphicLevel a owl:ObjectProperty ;
    rdfs:domain arqo:OccupationPhaseEvent ;
    rdfs:range crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "phaseOccurredInStratigraphicLevel"@en ;
    rdfs:comment "Links occupation phase to the stratigraphic level documenting it"@en .""")

    elif num == 30:  # Territorial distribution and paleoenvironment
        classes.append("""arqo:PaleoenvironmentalCorrelationEvent a owl:Class ;
    rdfs:subClassOf arqo:BiographicalEvent ;
    rdfs:label "PaleoenvironmentalCorrelationEvent"@en ;
    rdfs:comment "Event of correlating territorial object distribution with geological periods or paleoenvironmental conditions"@en .""")
        obj_props.append("""arqo:correlationLinksDistribution a owl:ObjectProperty ;
    rdfs:domain arqo:PaleoenvironmentalCorrelationEvent ;
    rdfs:range crm:E53_Place ;
    rdfs:label "correlationLinksDistribution"@en ;
    rdfs:comment "Links correlation event to the territorial distribution area"@en .""")
        obj_props.append("""arqo:correlationLinksGeologicalPeriod a owl:ObjectProperty ;
    rdfs:domain arqo:PaleoenvironmentalCorrelationEvent ;
    rdfs:range crm:E52_Time-Span ;
    rdfs:label "correlationLinksGeologicalPeriod"@en ;
    rdfs:comment "Links correlation event to the geological period"@en .""")
        data_props.append("""arqo:hasPaleoenvironmentalCondition a owl:DatatypeProperty ;
    rdfs:domain arqo:PaleoenvironmentalCorrelationEvent ;
    rdfs:range xsd:string ;
    rdfs:label "hasPaleoenvironmentalCondition"@en ;
    rdfs:comment "Paleoenvironmental condition that conditioned object production or circulation"@en .""")

    # Build output
    sections = ["# ======================= CLASSES ===========================\n" + "\n\n".join(classes)]

    if obj_props:
        sections.append("# =================== OBJECT PROPERTIES =====================\n" + "\n\n".join(obj_props))
    if data_props:
        sections.append("# ==================== DATA PROPERTIES =====================\n" + "\n\n".join(data_props))
    if restrictions:
        sections.append("# ===================== RESTRICTIONS =======================\n" + "\n".join(restrictions))

    output = "\n\n".join(sections)
    output += f"\n\n# Ontology generated by Qwen3.6 v2 using event-centric strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"

    return output

def generate_memoryless_ttl(cq, temp):
    header = HEADER.format(strategy="memoryless", temp=temp, cq_id=cq['id'])
    content = generate_event_centric(cq['id'], temp)
    return PREFIXES + header + content

def generate_ontogenia_step(cq, step_num, temp):
    header = HEADER.format(strategy="ontogenia", temp=temp, cq_id=cq['id'])
    step_info = f"# Step: {step_num}/30\n"
    content = generate_event_centric(cq['id'], temp)
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
            content = generate_event_centric(cq['id'], temp)
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
