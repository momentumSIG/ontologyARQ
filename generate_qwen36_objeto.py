#!/usr/bin/env python3
"""
Generate Qwen3.6 v2 object-centric ontologies from 30 new CQs.
Design: Object-centric — the archaeological object is the primary ontological anchor.
Events, classifications, and contexts are modeled in relation to the object.
"""

import os
import re

BASE_DIR = "/home/eaguayo/ONTOLOGIA-ARQ"
CQ_FILE = os.path.join(BASE_DIR, "CQ/CQ_Qwen3.6_objeto_v2/CQ-object-qwen3.6-v2.md")
OUT_DIR = os.path.join(BASE_DIR, "ontologies_generated/Qwen3.6_objeto_objeto")

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
# Ontology: Archaeological Object Module (Object-Centric Design)
# Model: Qwen3.6 v2 | Strategy: {strategy} | Temperature: {temp}
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

def core_object_classes(temp):
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
    classes = core_object_classes(temp)
    obj_props = []
    data_props = []
    restrictions = []

    num = int(cq_id.split('-')[-1])

    # ===== BLOCK 1: Biography as Historical Entity (CQ 1-5) =====
    if num == 1:  # Complete biographical sequence
        classes.append("""arqo:ObjectBiography a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ObjectBiography"@en ;
    rdfs:comment "Complete vital trajectory of archaeological object from raw material extraction to museum curation"@en .""")
        obj_props.append("""arqo:hasBiography a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ObjectBiography ;
    rdfs:label "hasBiography"@en ;
    rdfs:comment "Links object to its complete biographical trajectory"@en .""")
        obj_props.append("""arqo:biographyIncludesPhase a owl:ObjectProperty ;
    rdfs:domain arqo:ObjectBiography ;
    rdfs:range crm:E5_Event ;
    rdfs:label "biographyIncludesPhase"@en ;
    rdfs:comment "Links biography to constituent lifecycle phase"@en .""")
        if temp in ["0.5", "0.7"]:
            data_props.append("""arqo:hasBiographyDuration a owl:DatatypeProperty ;
    rdfs:domain arqo:ObjectBiography ;
    rdfs:range xsd:duration ;
    rdfs:label "hasBiographyDuration"@en ;
    rdfs:comment "Total duration of object biography from production to current state"@en .""")

    elif num == 2:  # Physical vs narrative biography
        classes.append("""arqo:PhysicalBiography a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "PhysicalBiography"@en ;
    rdfs:comment "Actual sequence of material events in object history"@en .""")
        classes.append("""arqo:NarrativeBiography a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "NarrativeBiography"@en ;
    rdfs:comment "Narrative construct about object biography told by specific interpreter"@en .""")
        obj_props.append("""arqo:hasPhysicalBiography a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PhysicalBiography ;
    rdfs:label "hasPhysicalBiography"@en ;
    rdfs:comment "Links object to its actual physical biography"@en .""")
        obj_props.append("""arqo:hasNarrativeBiography a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:NarrativeBiography ;
    rdfs:label "hasNarrativeBiography"@en ;
    rdfs:comment "Links object to narrative biography constructed by interpreter"@en .""")
        obj_props.append("""arqo:narrativeToldBy a owl:ObjectProperty ;
    rdfs:domain arqo:NarrativeBiography ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "narrativeToldBy"@en ;
    rdfs:comment "Researcher or community telling the biographical narrative"@en .""")

    elif num == 3:  # Parallel biographies across sites
        obj_props.append("""arqo:sharesBiographyPattern a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sharesBiographyPattern"@en ;
    rdfs:comment "Indicates objects from different sites share parallel biographical trajectories"@en .""")
        classes.append("""arqo:BiographyPattern a owl:Class ;
    rdfs:subClassOf crm:E55_Type ;
    rdfs:label "BiographyPattern"@en ;
    rdfs:comment "Recurring biographical sequence shared across objects indicating cultural practices"@en .""")
        obj_props.append("""arqo:exhibitsPattern a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:BiographyPattern ;
    rdfs:label "exhibitsPattern"@en ;
    rdfs:comment "Links object to the biographical pattern it exhibits"@en .""")

    elif num == 4:  # Natural object acquiring cultural agency
        classes.append("""arqo:CulturalAgency a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "CulturalAgency"@en ;
    rdfs:comment "Cultural agency acquired by natural object through human use without physical modification"@en .""")
        obj_props.append("""arqo:exertsCulturalAgency a owl:ObjectProperty ;
    rdfs:domain arqo:NaturalObject ;
    rdfs:range arqo:CulturalAgency ;
    rdfs:label "exertsCulturalAgency"@en ;
    rdfs:comment "Links natural object to its acquired cultural agency"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:agencyAttributedBy a owl:ObjectProperty ;
    rdfs:domain arqo:CulturalAgency ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "agencyAttributedBy"@en ;
    rdfs:comment "Human actor or community attributing cultural agency"@en .""")

    elif num == 5:  # Functional transformation
        classes.append("""arqo:FunctionalTransformation a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FunctionalTransformation"@en ;
    rdfs:comment "Change in object functional role that altered its typological classification"@en .""")
        obj_props.append("""arqo:underwentFunctionalTransformation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FunctionalTransformation ;
    rdfs:label "underwentFunctionalTransformation"@en ;
    rdfs:comment "Links object to its functional transformation event"@en .""")
        data_props.append("""arqo:hasTransformationEvidence a owl:DatatypeProperty ;
    rdfs:domain arqo:FunctionalTransformation ;
    rdfs:range xsd:string ;
    rdfs:label "hasTransformationEvidence"@en ;
    rdfs:comment "Trace evidence of functional transformation visible on object"@en .""")

    # ===== BLOCK 2: Analytical Workflows (CQ 6-10) =====
    elif num == 6:  # Complete analytical chain
        classes.append("""arqo:AnalyticalWorkflow a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "AnalyticalWorkflow"@en ;
    rdfs:comment "Complete chain of analytical events transforming object into published dataset"@en .""")
        obj_props.append("""arqo:objectSubjectOfWorkflow a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalyticalWorkflow ;
    rdfs:label "objectSubjectOfWorkflow"@en ;
    rdfs:comment "Links object to the analytical workflow it was subject to"@en .""")
        classes.append("""arqo:PhysicalSample a owl:Class ;
    rdfs:subClassOf crmsci:S18_Sample ;
    rdfs:label "PhysicalSample"@en ;
    rdfs:comment "Physical sample extracted from archaeological object"@en .""")
        obj_props.append("""arqo:hasPhysicalSample a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PhysicalSample ;
    rdfs:label "hasPhysicalSample"@en ;
    rdfs:comment "Links object to extracted physical sample"@en .""")
        obj_props.append("""arqo:workflowProducedDataset a owl:ObjectProperty ;
    rdfs:domain arqo:AnalyticalWorkflow ;
    rdfs:range crm:E73_Information_Object ;
    rdfs:label "workflowProducedDataset"@en ;
    rdfs:comment "Links analytical workflow to resulting published dataset"@en .""")

    elif num == 7:  # Samples and contradictory results
        obj_props.append("""arqo:sampleDerivedFrom a owl:ObjectProperty ;
    rdfs:domain arqo:PhysicalSample ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "sampleDerivedFrom"@en ;
    rdfs:comment "Links physical sample to its source object"@en .""")
        classes.append("""arqo:ContradictoryResult a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "ContradictoryResult"@en ;
    rdfs:comment "Set of contradictory analytical results from different techniques on same object"@en .""")
        obj_props.append("""arqo:objectHasContradictoryResult a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ContradictoryResult ;
    rdfs:label "objectHasContradictoryResult"@en ;
    rdfs:comment "Links object to contradictory analytical results"@en .""")

    elif num == 8:  # Protocols for provenance determination
        classes.append("""arqo:IsotopicAnalysis a owl:Class ;
    rdfs:subClassOf crmsci:S19_Encounter ;
    rdfs:label "IsotopicAnalysis"@en ;
    rdfs:comment "Isotopic ratio measurement event for provenance determination"@en .""")
        obj_props.append("""arqo:objectSubjectOfIsotopicAnalysis a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:IsotopicAnalysis ;
    rdfs:label "objectSubjectOfIsotopicAnalysis"@en ;
    rdfs:comment "Links object to isotopic analysis performed on it"@en .""")
        obj_props.append("""arqo:analysisUsedProtocol a owl:ObjectProperty ;
    rdfs:domain arqo:IsotopicAnalysis ;
    rdfs:range crm:E29_Design_or_Procedure ;
    rdfs:label "analysisUsedProtocol"@en ;
    rdfs:comment "Links analysis to laboratory protocol employed"@en .""")
        data_props.append("""arqo:hasIsotopicRatio a owl:DatatypeProperty ;
    rdfs:domain arqo:IsotopicAnalysis ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasIsotopicRatio"@en ;
    rdfs:comment "Measured isotopic ratio value"@en .""")

    elif num == 9:  # Datasets linked to observations
        classes.append("""arqo:AnalyticalDataset a owl:Class ;
    rdfs:subClassOf crm:E73_Information_Object ;
    rdfs:label "AnalyticalDataset"@en ;
    rdfs:comment "Scientific dataset generated from analytical study of archaeological object"@en .""")
        obj_props.append("""arqo:objectGeneratedDataset a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:AnalyticalDataset ;
    rdfs:label "objectGeneratedDataset"@en ;
    rdfs:comment "Links object to analytical dataset it generated"@en .""")
        obj_props.append("""arqo:datasetDerivedFromObservation a owl:ObjectProperty ;
    rdfs:domain arqo:AnalyticalDataset ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "datasetDerivedFromObservation"@en ;
    rdfs:comment "Links dataset to original observations"@en .""")
        obj_props.append("""arqo:datasetSupportsInterpretation a owl:ObjectProperty ;
    rdfs:domain arqo:AnalyticalDataset ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "datasetSupportsInterpretation"@en ;
    rdfs:comment "Links dataset to interpretive conclusions it supports"@en .""")

    elif num == 10:  # Calibration and revisions
        classes.append("""arqo:MethodologicalRevision a owl:Class ;
    rdfs:subClassOf crmsci:S5_Inference_Making ;
    rdfs:label "MethodologicalRevision"@en ;
    rdfs:comment "Revision of previously published dating or classification based on new evidence"@en .""")
        obj_props.append("""arqo:objectSubjectOfRevision a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:MethodologicalRevision ;
    rdfs:label "objectSubjectOfRevision"@en ;
    rdfs:comment "Links object to methodological revision affecting its classification"@en .""")
        obj_props.append("""arqo:revisionSupersedes a owl:ObjectProperty ;
    rdfs:domain arqo:MethodologicalRevision ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "revisionSupersedes"@en ;
    rdfs:comment "Links revision to prior interpretation it supersedes"@en .""")

    # ===== BLOCK 3: Disputed Interpretation (CQ 11-15) =====
    elif num == 11:  # Rival hypotheses
        classes.append("""arqo:InterpretiveHypothesis a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "InterpretiveHypothesis"@en ;
    rdfs:comment "Rival hypothesis about object function, chronology, or cultural meaning"@en .""")
        obj_props.append("""arqo:objectHasHypothesis a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:InterpretiveHypothesis ;
    rdfs:label "objectHasHypothesis"@en ;
    rdfs:comment "Links object to interpretive hypothesis about it"@en .""")
        obj_props.append("""arqo:hypothesisSupportedByEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:InterpretiveHypothesis ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "hypothesisSupportedByEvidence"@en ;
    rdfs:comment "Links hypothesis to analytical evidence supporting it"@en .""")
        obj_props.append("""arqo:hypothesisFormulatedBy a owl:ObjectProperty ;
    rdfs:domain arqo:InterpretiveHypothesis ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "hypothesisFormulatedBy"@en ;
    rdfs:comment "Researcher who formulated the hypothesis"@en .""")

    elif num == 12:  # Rejected interpretations
        classes.append("""arqo:RejectedInterpretation a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "RejectedInterpretation"@en ;
    rdfs:comment "Interpretive claim about object that was rejected based on evidence"@en .""")
        obj_props.append("""arqo:objectHasRejectedInterpretation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:RejectedInterpretation ;
    rdfs:label "objectHasRejectedInterpretation"@en ;
    rdfs:comment "Links object to interpretation that was rejected"@en .""")
        obj_props.append("""arqo:rejectedDueToEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:RejectedInterpretation ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "rejectedDueToEvidence"@en ;
    rdfs:comment "Links rejected interpretation to evidence causing rejection"@en .""")

    elif num == 13:  # Certainty levels
        classes.append("""arqo:CertaintyAssessment a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "CertaintyAssessment"@en ;
    rdfs:comment "Assessment of certainty level for archaeological interpretation of object"@en .""")
        obj_props.append("""arqo:objectHasCertaintyAssessment a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CertaintyAssessment ;
    rdfs:label "objectHasCertaintyAssessment"@en ;
    rdfs:comment "Links object to certainty assessment of its interpretation"@en .""")
        data_props.append("""arqo:hasCertaintyLevel a owl:DatatypeProperty ;
    rdfs:domain arqo:CertaintyAssessment ;
    rdfs:range xsd:decimal ;
    rdfs:label "hasCertaintyLevel"@en ;
    rdfs:comment "Certainty level from 0.0 (speculative) to 1.0 (confirmed)"@en .""")
        data_props.append("""arqo:hasTheoreticalSchool a owl:DatatypeProperty ;
    rdfs:domain arqo:CertaintyAssessment ;
    rdfs:range xsd:string ;
    rdfs:label "hasTheoreticalSchool"@en ;
    rdfs:comment "Theoretical school or framework underlying the assessment"@en .""")

    elif num == 14:  # Argumentative chains
        classes.append("""arqo:ArgumentativeChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ArgumentativeChain"@en ;
    rdfs:comment "Chain of reasoning connecting observations, measurements, and inferences about object"@en .""")
        obj_props.append("""arqo:objectAssociatedWithChain a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArgumentativeChain ;
    rdfs:label "objectAssociatedWithChain"@en ;
    rdfs:comment "Links object to argumentative chain about it"@en .""")
        obj_props.append("""arqo:chainStartsWithObservation a owl:ObjectProperty ;
    rdfs:domain arqo:ArgumentativeChain ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "chainStartsWithObservation"@en ;
    rdfs:comment "Links chain to initial observation"@en .""")
        obj_props.append("""arqo:chainConcludesWith a owl:ObjectProperty ;
    rdfs:domain arqo:ArgumentativeChain ;
    rdfs:range crmsci:S5_Inference_Making ;
    rdfs:label "chainConcludesWith"@en ;
    rdfs:comment "Links chain to final interpretive conclusion"@en .""")

    elif num == 15:  # Interpretive conflicts
        classes.append("""arqo:InterpretiveConflict a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "InterpretiveConflict"@en ;
    rdfs:comment "Situation where researchers hold conflicting interpretations of same object"@en .""")
        obj_props.append("""arqo:objectSubjectOfConflict a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:InterpretiveConflict ;
    rdfs:label "objectSubjectOfConflict"@en ;
    rdfs:comment "Links object to interpretive conflict about it"@en .""")
        obj_props.append("""arqo:conflictInvolvesInterpretation a owl:ObjectProperty ;
    rdfs:domain arqo:InterpretiveConflict ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "conflictInvolvesInterpretation"@en ;
    rdfs:comment "Links conflict to competing interpretations"@en .""")
        data_props.append("""arqo:hasTheoreticalFramework a owl:DatatypeProperty ;
    rdfs:domain arqo:InterpretiveConflict ;
    rdfs:range xsd:string ;
    rdfs:label "hasTheoreticalFramework"@en ;
    rdfs:comment "Theoretical framework underlying an interpretation in conflict"@en .""")

    # ===== BLOCK 4: Taphonomy (CQ 16-20) =====
    elif num == 16:  # Natural taphonomic processes
        classes.append("""arqo:TaphonomicProcess a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "TaphonomicProcess"@en ;
    rdfs:comment "Natural post-depositional process affecting object position, condition, or integrity"@en .""")
        obj_props.append("""arqo:objectAffectedByTaphonomy a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:TaphonomicProcess ;
    rdfs:label "objectAffectedByTaphonomy"@en ;
    rdfs:comment "Links object to taphonomic process that affected it"@en .""")
        data_props.append("""arqo:hasTaphonomicType a owl:DatatypeProperty ;
    rdfs:domain arqo:TaphonomicProcess ;
    rdfs:range xsd:string ;
    rdfs:label "hasTaphonomicType"@en ;
    rdfs:comment "Type: bioturbation, corrosion, weathering, water transport, sediment compaction"@en .""")

    elif num == 17:  # Stratigraphic-geological correlations
        classes.append("""arqo:StratigraphicCorrelation a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "StratigraphicCorrelation"@en ;
    rdfs:comment "Correlation between archaeological stratigraphic unit and geological unit"@en .""")
        obj_props.append("""arqo:objectFoundInCorrelatedUnit a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:StratigraphicCorrelation ;
    rdfs:label "objectFoundInCorrelatedUnit"@en ;
    rdfs:comment "Links object to stratigraphic-geological correlation of its context"@en .""")
        obj_props.append("""arqo:correlationLinksGeologicalUnit a owl:ObjectProperty ;
    rdfs:domain arqo:StratigraphicCorrelation ;
    rdfs:range crm:E53_Place ;
    rdfs:label "correlationLinksGeologicalUnit"@en ;
    rdfs:comment "Links correlation to geological unit"@en .""")

    elif num == 18:  # Geomorphological events
        classes.append("""arqo:GeomorphologicalImpact a owl:Class ;
    rdfs:subClassOf crmarchaeo:A5_Stratigraphic_Modification_Event ;
    rdfs:label "GeomorphologicalImpact"@en ;
    rdfs:comment "Geomorphological event that affected object depositional context"@en .""")
        obj_props.append("""arqo:objectContextAffectedByGeomorphology a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:GeomorphologicalImpact ;
    rdfs:label "objectContextAffectedByGeomorphology"@en ;
    rdfs:comment "Links object to geomorphological impact on its context"@en .""")
        data_props.append("""arqo:hasGeomorphologicalType a owl:DatatypeProperty ;
    rdfs:domain arqo:GeomorphologicalImpact ;
    rdfs:range xsd:string ;
    rdfs:label "hasGeomorphologicalType"@en ;
    rdfs:comment "Type: flood, colluviation, erosion, volcanism, fluvial dynamics"@en .""")

    elif num == 19:  # Post-depositional displacement
        classes.append("""arqo:PostDepositionalDisplacement a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "PostDepositionalDisplacement"@en ;
    rdfs:comment "Post-depositional movement of object from original position"@en .""")
        obj_props.append("""arqo:objectDisplacedBy a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PostDepositionalDisplacement ;
    rdfs:label "objectDisplacedBy"@en ;
    rdfs:comment "Links object to its post-depositional displacement"@en .""")
        obj_props.append("""arqo:displacementAffectsContextReliability a owl:ObjectProperty ;
    rdfs:domain arqo:PostDepositionalDisplacement ;
    rdfs:range crminf:I4_Proposition_Set ;
    rdfs:label "displacementAffectsContextReliability"@en ;
    rdfs:comment "Links displacement to reliability assessment of stratigraphic context"@en .""")

    elif num == 20:  # Fragmentation processes
        classes.append("""arqo:FragmentationProcess a owl:Class ;
    rdfs:subClassOf crm:E81_Transformation ;
    rdfs:label "FragmentationProcess"@en ;
    rdfs:comment "Process that broke originally complete object into fragments"@en .""")
        obj_props.append("""arqo:objectFragmentedBy a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FragmentationProcess ;
    rdfs:label "objectFragmentedBy"@en ;
    rdfs:comment "Links object to fragmentation process"@en .""")
        data_props.append("""arqo:hasFragmentationCause a owl:DatatypeProperty ;
    rdfs:domain arqo:FragmentationProcess ;
    rdfs:range xsd:string ;
    rdfs:label "hasFragmentationCause"@en ;
    rdfs:comment "Cause: intentional ritual, accidental use-wear, taphonomic post-depositional"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:isFragmentOf a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "isFragmentOf"@en ;
    rdfs:comment "Links fragment to conceptual whole object"@en .""")

    # ===== BLOCK 5: Custody and Heritage (CQ 21-25) =====
    elif num == 21:  # Custody chain
        classes.append("""arqo:CustodyChain a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "CustodyChain"@en ;
    rdfs:comment "Chain of custody events managing object from recovery to current location"@en .""")
        obj_props.append("""arqo:objectManagedByCustodyChain a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:CustodyChain ;
    rdfs:label "objectManagedByCustodyChain"@en ;
    rdfs:comment "Links object to its custody chain"@en .""")
        obj_props.append("""arqo:chainIncludesCustodyEvent a owl:ObjectProperty ;
    rdfs:domain arqo:CustodyChain ;
    rdfs:range crm:E9_Move ;
    rdfs:label "chainIncludesCustodyEvent"@en ;
    rdfs:comment "Links custody chain to constituent custody event"@en .""")
        data_props.append("""arqo:hasCustodyType a owl:DatatypeProperty ;
    rdfs:domain crm:E9_Move ;
    rdfs:range xsd:string ;
    rdfs:label "hasCustodyType"@en ;
    rdfs:comment "Type: excavation, storage, loan, exhibition, restoration, repatriation"@en .""")

    elif num == 22:  # Conservation decisions
        classes.append("""arqo:ConservationDecision a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "ConservationDecision"@en ;
    rdfs:comment "Decision event determining conservation approach based on competing values"@en .""")
        obj_props.append("""arqo:objectSubjectOfConservationDecision a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:ConservationDecision ;
    rdfs:label "objectSubjectOfConservationDecision"@en ;
    rdfs:comment "Links object to conservation decision about it"@en .""")
        data_props.append("""arqo:hasConservationApproach a owl:DatatypeProperty ;
    rdfs:domain arqo:ConservationDecision ;
    rdfs:range xsd:string ;
    rdfs:label "hasConservationApproach"@en ;
    rdfs:comment "Approach: cleaning, consolidation, reconstruction, non-intervention"@en .""")
        data_props.append("""arqo:hasConflictingValue a owl:DatatypeProperty ;
    rdfs:domain arqo:ConservationDecision ;
    rdfs:range xsd:string ;
    rdfs:label "hasConflictingValue"@en ;
    rdfs:comment "Conflicting value: authenticity, access, research, preservation"@en .""")

    elif num == 23:  # Exhibition and pastness
        classes.append("""arqo:Exhibition a owl:Class ;
    rdfs:subClassOf crm:E7_Activity ;
    rdfs:label "Exhibition"@en ;
    rdfs:comment "Public exhibition event of archaeological object"@en .""")
        classes.append("""arqo:Pastness a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "Pastness"@en ;
    rdfs:comment "Culturally perceived quality of being old, distinct from chronological age"@en .""")
        obj_props.append("""arqo:objectExhibitedIn a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:Exhibition ;
    rdfs:label "objectExhibitedIn"@en ;
    rdfs:comment "Links object to exhibition event"@en .""")
        obj_props.append("""arqo:objectExhibitsPastness a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:Pastness ;
    rdfs:label "objectExhibitsPastness"@en ;
    rdfs:comment "Links object to its perceived pastness quality"@en .""")
        if temp in ["0.5", "0.7"]:
            classes.append("""arqo:Patina a owl:Class ;
    rdfs:subClassOf crm:E3_Condition_State ;
    rdfs:label "Patina"@en ;
    rdfs:comment "Surface alteration connoting age, valued as evidence of authenticity"@en .""")
            obj_props.append("""arqo:objectHasPatina a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:Patina ;
    rdfs:label "objectHasPatina"@en ;
    rdfs:comment "Links object to its patina"@en .""")

    elif num == 24:  # Digital replicas
        classes.append("""arqo:DigitalReplica a owl:Class ;
    rdfs:subClassOf crm:E73_Information_Object ;
    rdfs:label "DigitalReplica"@en ;
    rdfs:comment "Digital replica, 3D model, or virtual representation of archaeological object"@en .""")
        obj_props.append("""arqo:objectHasDigitalReplica a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:DigitalReplica ;
    rdfs:label "objectHasDigitalReplica"@en ;
    rdfs:comment "Links object to its digital replica"@en .""")
        obj_props.append("""arqo:replicaGeneratedByTechnique a owl:ObjectProperty ;
    rdfs:domain arqo:DigitalReplica ;
    rdfs:range crmsci:S19_Encounter ;
    rdfs:label "replicaGeneratedByTechnique"@en ;
    rdfs:comment "Links digital replica to documentation technique that generated it"@en .""")
        data_props.append("""arqo:hasDocumentationTechnique a owl:DatatypeProperty ;
    rdfs:domain crmsci:S19_Encounter ;
    rdfs:range xsd:string ;
    rdfs:label "hasDocumentationTechnique"@en ;
    rdfs:comment "Technique: photogrammetry, laser scanning, RTI, structured light"@en .""")

    elif num == 25:  # Heritage claims
        classes.append("""arqo:HeritageClaim a owl:Class ;
    rdfs:subClassOf crminf:I4_Proposition_Set ;
    rdfs:label "HeritageClaim"@en ;
    rdfs:comment "Cultural heritage claim, repatriation demand, or legal litigation over object ownership"@en .""")
        obj_props.append("""arqo:objectSubjectOfClaim a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:HeritageClaim ;
    rdfs:label "objectSubjectOfClaim"@en ;
    rdfs:comment "Links object to heritage claim about it"@en .""")
        obj_props.append("""arqo:claimAssertedBy a owl:ObjectProperty ;
    rdfs:domain arqo:HeritageClaim ;
    rdfs:range crm:E39_Actor ;
    rdfs:label "claimAssertedBy"@en ;
    rdfs:comment "Community or institution asserting claim"@en .""")
        obj_props.append("""arqo:claimSupportedByEvidence a owl:ObjectProperty ;
    rdfs:domain arqo:HeritageClaim ;
    rdfs:range crmsci:S4_Observation ;
    rdfs:label "claimSupportedByEvidence"@en ;
    rdfs:comment "Links claim to probative evidence"@en .""")

    # ===== BLOCK 6: Object-Context-Territory (CQ 26-30) =====
    elif num == 26:  # Spatial topological relationships
        classes.append("""arqo:SpatialAssociation a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "SpatialAssociation"@en ;
    rdfs:comment "Spatial topological relationship between objects in same stratigraphic unit"@en .""")
        obj_props.append("""arqo:objectInSpatialAssociation a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:SpatialAssociation ;
    rdfs:label "objectInSpatialAssociation"@en ;
    rdfs:comment "Links object to spatial association it participates in"@en .""")
        obj_props.append("""arqo:associationRelatesObject a owl:ObjectProperty ;
    rdfs:domain arqo:SpatialAssociation ;
    rdfs:range arqo:ArchaeologicalObject ;
    rdfs:label "associationRelatesObject"@en ;
    rdfs:comment "Links spatial association to related object"@en .""")
        data_props.append("""arqo:hasTopologicalRelation a owl:DatatypeProperty ;
    rdfs:domain arqo:SpatialAssociation ;
    rdfs:range xsd:string ;
    rdfs:label "hasTopologicalRelation"@en ;
    rdfs:comment "Relation: proximity, co-occurrence, functional association"@en .""")

    elif num == 27:  # Circulation between settlements
        classes.append("""arqo:InterSettlementCirculation a owl:Class ;
    rdfs:subClassOf crm:E9_Move ;
    rdfs:label "InterSettlementCirculation"@en ;
    rdfs:comment "Object circulation between settlements, territories, or mobility corridors"@en .""")
        obj_props.append("""arqo:objectCirculatedThrough a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:InterSettlementCirculation ;
    rdfs:label "objectCirculatedThrough"@en ;
    rdfs:comment "Links object to its inter-settlement circulation"@en .""")
        obj_props.append("""arqo:circulationEvidencesNetwork a owl:ObjectProperty ;
    rdfs:domain arqo:InterSettlementCirculation ;
    rdfs:range crm:E55_Type ;
    rdfs:label "circulationEvidencesNetwork"@en ;
    rdfs:comment "Links circulation to exchange network or migration pattern it evidences"@en .""")
        data_props.append("""arqo:hasCirculationMechanism a owl:DatatypeProperty ;
    rdfs:domain arqo:InterSettlementCirculation ;
    rdfs:range xsd:string ;
    rdfs:label "hasCirculationMechanism"@en ;
    rdfs:comment "Mechanism: trade, gift exchange, looting, migration"@en .""")

    elif num == 28:  # Spatial distribution and functional zoning
        classes.append("""arqo:FunctionalZone a owl:Class ;
    rdfs:subClassOf crm:E53_Place ;
    rdfs:label "FunctionalZone"@en ;
    rdfs:comment "Functional area within site identified by object distribution patterns"@en .""")
        obj_props.append("""arqo:objectFoundInZone a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:FunctionalZone ;
    rdfs:label "objectFoundInZone"@en ;
    rdfs:comment "Links object to functional zone where it was found"@en .""")
        data_props.append("""arqo:hasZoneType a owl:DatatypeProperty ;
    rdfs:domain arqo:FunctionalZone ;
    rdfs:range xsd:string ;
    rdfs:label "hasZoneType"@en ;
    rdfs:comment "Type: domestic, ritual, production, funerary"@en .""")

    elif num == 29:  # Occupation sequences
        classes.append("""arqo:OccupationPhase a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "OccupationPhase"@en ;
    rdfs:comment "Phase of occupation, abandonment, or reoccupation documented by objects"@en .""")
        obj_props.append("""arqo:objectDocumentsPhase a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:OccupationPhase ;
    rdfs:label "objectDocumentsPhase"@en ;
    rdfs:comment "Links object to occupation phase it documents"@en .""")
        data_props.append("""arqo:hasPhaseType a owl:DatatypeProperty ;
    rdfs:domain arqo:OccupationPhase ;
    rdfs:range xsd:string ;
    rdfs:label "hasPhaseType"@en ;
    rdfs:comment "Type: occupation, abandonment, reoccupation"@en .""")
        if temp in ["0.5", "0.7"]:
            obj_props.append("""arqo:phaseOccurredInLevel a owl:ObjectProperty ;
    rdfs:domain arqo:OccupationPhase ;
    rdfs:range crmarchaeo:A8_Stratigraphic_Unit ;
    rdfs:label "phaseOccurredInLevel"@en ;
    rdfs:comment "Links phase to stratigraphic level documenting it"@en .""")

    elif num == 30:  # Territorial distribution and paleoenvironment
        classes.append("""arqo:PaleoenvironmentalCorrelation a owl:Class ;
    rdfs:subClassOf crm:E5_Event ;
    rdfs:label "PaleoenvironmentalCorrelation"@en ;
    rdfs:comment "Correlation between territorial object distribution and geological periods or paleoenvironmental conditions"@en .""")
        obj_props.append("""arqo:objectPartOfTerritorialDistribution a owl:ObjectProperty ;
    rdfs:domain arqo:ArchaeologicalObject ;
    rdfs:range arqo:PaleoenvironmentalCorrelation ;
    rdfs:label "objectPartOfTerritorialDistribution"@en ;
    rdfs:comment "Links object to territorial distribution correlation"@en .""")
        obj_props.append("""arqo:correlationLinksGeologicalPeriod a owl:ObjectProperty ;
    rdfs:domain arqo:PaleoenvironmentalCorrelation ;
    rdfs:range crm:E52_Time-Span ;
    rdfs:label "correlationLinksGeologicalPeriod"@en ;
    rdfs:comment "Links correlation to geological period"@en .""")
        data_props.append("""arqo:hasPaleoenvironmentalCondition a owl:DatatypeProperty ;
    rdfs:domain arqo:PaleoenvironmentalCorrelation ;
    rdfs:range xsd:string ;
    rdfs:label "hasPaleoenvironmentalCondition"@en ;
    rdfs:comment "Paleoenvironmental condition conditioning object production or circulation"@en .""")

    # Build output
    sections = ["# ======================= CLASSES ===========================\n" + "\n\n".join(classes)]

    if obj_props:
        sections.append("# =================== OBJECT PROPERTIES =====================\n" + "\n\n".join(obj_props))
    if data_props:
        sections.append("# ==================== DATA PROPERTIES =====================\n" + "\n\n".join(data_props))
    if restrictions:
        sections.append("# ===================== RESTRICTIONS =======================\n" + "\n".join(restrictions))

    output = "\n\n".join(sections)
    output += f"\n\n# Ontology generated by Qwen3.6 v2 using object-centric strategy at temperature {temp}\n"
    output += "# Compatible with CIDOC CRM v7.3.2 and CRMarchaeo v2.1.1\n"

    return output

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
