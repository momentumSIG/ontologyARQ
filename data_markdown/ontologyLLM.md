Ontology Generation using
Large Language Models
Anna Sofia Lippolis 1,2,∗, Mohammad Javad Saeedizade 3,∗,
Robin Keskisärkkä3, Sara Zuppiroli2, Miguel Ceriani2, Aldo Gangemi1,2,
Eva Blomqvist3, and Andrea Giovanni Nuzzolese2
1 University of Bologna, Italy
annasofia.lippolis2@unibo.it, aldo.gangemi@unibo.it
2 ISTC-CNR, Italy
andrea.nuzzolese@cnr.it,sara.zuppiroli@istc.cnr.it,miguel.ceriani@cnr.it
3 Linköping University, Sweden
javad.saeedizade@liu.se, robin.keskisarkka@liu.se, eva.blomqvist@liu.se
Abstract. Theontologyengineeringprocessiscomplex,time-consuming,
and error-prone, even for experienced ontology engineers. In this work,
weinvestigatethepotentialofLargeLanguageModels(LLMs)toprovide
effectiveOWLontologydraftsdirectlyfromontologicalrequirementsde-
scribedusinguserstoriesandcompetencyquestions.Ourmaincontribu-
tionisthepresentationandevaluationoftwonewpromptingtechniques
for automated ontology development: Memoryless CQbyCQ and Onto-
genia. We also emphasize the importance of three structural criteria for
ontology assessment, alongside expert qualitative evaluation, highlight-
ing the need for a multi-dimensional evaluation in order to capture the
qualityandusabilityofthegeneratedontologies.Ourexperiments,con-
ducted on a benchmark dataset of ten ontologies with 100 distinct CQs
and 29 different user stories, compare the performance of three LLMs
using the two prompting techniques. The results demonstrate improve-
mentsoverthecurrentstate-of-the-artinLLM-supportedontologyengi-
neering.Morespecifically,themodelOpenAI o1-previewwithOntogenia
produces ontologies of sufficient quality to meet the requirements of on-
tology engineers, significantly outperforming novice ontology engineers
in modelling ability. However, we still note some common mistakes and
variabilityofresultquality,whichisimportanttotakeintoaccountwhen
usingLLMsforontologyauthoringsupport.Wediscusstheselimitations
and propose directions for future research.
Keywords: Ontology·LargeLanguageModels·OntologyEngineering
1 Introduction
Ontologies play an important role in the success of Knowledge Graphs (KGs),
asacrucialcomponentintherecentadvancementsofexplainableAIandneuro-
* Equal contribution.
5202
raM
7
]IA.sc[
1v88350.3052:viXra

2 A. S. Lippolis et al.
symbolic integration. Today, ontologies are extensively used to facilitate se-
mantic interoperability, e.g., describing datasets and standardised terminolo-
gies. However, ontology engineering (OE) is a complex task that requires skills
in knowledge representation, logic, and computational linguistics. So far, many
OE methodologies have emerged in the scientific literature to provide struc-
tured frameworks that assist ontology engineers in navigating the complexities
ofknowledgemodeling.ExamplesareMethontology [14],theNeOnmethod-
ology [32], eXtreme Design (XD) [7], and more recently the Linked Open Terms
[27]. In any case, OE requires access to significant domain expertise combined
with knowledge engineering and modelling skills, posing a significant barrier to
entry for many professionals. Moreover, even when expertise is available, the
creation, curation, and validation of ontological elements are complex tasks,
which are cognitively costly and mostly manual. Instead, Large Language Mod-
els (LLMs) have proven to be able to assist humans in a variety of tasks, rang-
ing from programming co-pilots to data cleaning and statistical analysis. These
advancements highlight the growing need to benchmark common semantic web
tasksfromtheperspectiveofLLMs,transformingthiseffortfromanidealintoan
essentialrequirementandemphasizingthecriticalimportanceofresearchinthis
area [1,3,29,25,34]. Furthermore, prompting techniques, defined as an approach
tocarefullyformulatinginputprompts,canbeleveragedtoelicitthepre-trained
knowledgeofLLMstoperformspecifictaskswithoutadditionaltrainingorfine-
tuning. Advanced strategies such as decomposed prompting, where the task is
split into several pieces, have been shown to enhance LLM performance across
a wide range of tasks [21]. In this work, we assume that LLMs can also be ben-
eficial for ontology design by reducing manual labour for experienced ontology
engineers, as well as assisting novice ontology engineers.
Accordingly, the research questions driving this work are: (i) To what ex-
tent can LLMs be used to support the generation of ontologies that meet a
predefined set of requirements? (ii) What evaluation criteria are suitable for
evaluating LLM-generated ontologies? (iii) What are the strengths and weak-
nesses of ontologies generated using LLMs? To answer these questions, we pro-
vide a framework to assess LLM-pipelines with prompting techniques focused
on OE, as well as the LLM-generated minimal ontology modules themselves. In
particular, expanding previous research [30], we leverage a dataset of ontology
requirements and a set of reference minimal ontology modules to evaluate two
prompting techniques for supporting OE: Memoryless CQbyCQ and Ontoge-
nia1. We further evaluate the performance of these prompting techniques, using
state-of-the-art LLMs, and propose a set of evaluation criteria for comparing
and evaluating different pipeline setups.
The paper is organized as follows: Section 2 reviews relevant literature; Sec-
tion 3 clarifies the terminology used in this paper; Section 4 details our research
methodology; Section 5 outlines the evaluation criteria used to assess our ap-
1 The supplementary materials are available at https://github.com/dersuchendee/
Onto-Generation.

Ontology Generation using Large Language Models 3
proach;Section6presentsourfindingswithdetailedanalysis;Section7discusses
the implications of the results. Finally, Section 8 summarizes the main findings.
2 Related Work
Thissectionpresentsrelatedworkaboutontologyengineeringmethods,ontology
generation methods, and prompting techniques for ontology generation.
Ontology engineering methods. Several methodologies have been devel-
oped for ontology engineering, e.g., Methontology [14] and NeOn [33]. Agile
methodologies focusing on the re-use of Ontology Design Patterns [8,16], like
those surveyed in [6,24,31], have become increasingly popular, reflecting real-
world needs by maximizing the cognitive soundness, logical correctness, and
effectiveness of ontological artefacts. The LOT methodology [27] was presented
as a compilation of experiences from many projects, methodologies, and tools.
While some methods have explicit tool support, e.g., NeOn [33], most are still
entirelymanual.Ontologyengineersoftenmustmatchthemodellingproblemto
requirements, which is generally complex and time-consuming.
Ontology generation with LLMs With the advent of LLMs, much research
hasbeenfocusedonthepossibilityofgeneratingontologies,ortheirspecificele-
ments, from natural language. The increased interest in this area is exemplified
by the announcement of several special tracks in the semantic web conferences
dedicatedtotheseissues2.DespiteLLMs’well-knowndrawbacks,suchashalluci-
nations, studies show they have the potential to perform efficiently in numerous
tasks, with only a handful of examples and a well-designed prompt [2,18]. In
[17] the authors survey the tasks currently addressed by approaches for LLM-
supported ontology engineering, and while some approaches focusing on the ac-
tual tasks of generating the OWL files themselves have been proposed, this is
still an area that needs much further investigation.The LLMs4OL approach [4]
used LLMs to extract relations among ontology classes or instances, but only
among entities, not addressing the complete generation of an ontology. Other
preliminary work [23] has used fine-tuned GPT models to translate restricted
natural language sentences into DL axioms. However, such specific sentences
do not represent realistic ontology requirements or scenarios, as targeted in our
work. Furthermore, tools are appearing to support the practical integration of
OWLwithLLMs,e.g.[19],whilenotprovidinganyspecificguidancefortheon-
tologygenerationtask.Onerecentworksimilartoourproposedapproachisthe
NeOn-GPT pipeline proposed by Fathallah et al. [12]. However, that work only
evaluates one single complex prompting technique, and evaluates the pipeline
only on one single ontology generation example. In LLMs4Life[13], the NeOn-
GPTapproachisextendedtothelifesciencesdomain.However,implementation
2 E.g. see ESWC https://2024.eswc-conferences.org/, EKAW https://event.
cwi.nl/ekaw2024/cfp.html and ISWC https://iswc2024.semanticweb.org/

4 A. S. Lippolis et al.
details remain unclear, especially for what concerns the evaluation criteria. In
Lippolisetal.andSaeeizadeandBlomqvist[22,30],differentmethodsandontol-
ogy evaluation approaches for ontology generation from requirements have been
tested, obtaining results which are at least comparable to the quality of human
novicemodellers:thesetwoworksarethestartingpointofourcurrentinvestiga-
tion. Our multi-dimensional assessment implements the proposal of Rebboud et
al.,[29],whereontologyconceptualizationisproposedtobeevaluatedaccording
to ontology evaluation criteria such as accuracy, completeness, and conciseness
ofthegeneratedontologyaswellaslogicalconsistency.Furthermore,theauthors
propose the only existing benchmark for this task. However, it comprises entire
ontologies rather than minimal ontology modules, making it harder to evaluate
the outputs LLMs at a wider granularity, and often lacks ontology stories.
Promptingtechniquesforontologygeneration. Promptengineeringstands
out for its simplicity in implementation and adaptability, in contrast to finetun-
ing, offering an approach for enhancing knowledge engineering processes while
avoidingtheneedforlargelabelleddatasetsanddedicatedfinetunedmodels.Re-
quiringmodestefforttoimplement,itprovidessubstantialflexibilityforupdates
and modifications. In Lippolis et al. and Saeeizade and Blomqvist [22,30], the
authorshaveexploredandevaluatedvariouspromptingtechniquesandidentified
several techniques that appear suitable for different aspects of ontology genera-
tion.Ourresearchontheonehandexploressubtask-decomposedprompting,i.e.,
inthiscasethepromisingCQbyCQmethodfromSaeedizadeandBlomqvist[30],
as well another prompting technique based on Chain Of Thought (CoT) [37].
CoT is known for the specific ability to successfully improve the performance
of different tasks and decreasing hallucinations [11]. A particular case of CoT is
MetacognitivePrompting(MP)[22],inspiredbyhumanintrospectiveprocesses.
It encourages self-evaluation through the introduction of a series of steps, im-
proving performance over CoT. Starting from the studies of Brown et al.,[10],
Wei et al.[37], and Wang et al. [35,36], which demonstrated significant improve-
ments in LLM response abilities when using CoT or, more effectively, MP, our
study examines the performance of various prompting strategies in ontology
generation, comparing CoT with subtask-decomposed prompting approaches.
3 Preliminaries
In this section, we clarify and define terminology that will be used throughout
this paper. These definitions are essential for understanding the concepts dis-
cussed in subsequent sections and provide details on the specific ways in which
we interpret and employ these notions within the context of our research.
Ontology. In this work, ontology O is defined as a set of classes, object prop-
erties, data properties and axioms.
Validation Competency Question. As defined in Keet and Khan [20], we
can say a CQ is of the validation type if it ensures it adequately reflects the

Ontology Generation using Large Language Models 5
domain it represents by validating the ontology’s content while it aligns with its
intended meaning and representation. For simplicity, we refer to this as CQ.
Modelled Competency Question. Given an ontology O and a validation
competency question CQ , if O includes all necessary elements—such as classes
i
or properties—needed to write a validation SPARQL query to verify CQ (CQ
i
verification [9]), we say that CQ is modelled in O regardless of the quality of
i
the modelling, whether it follows good or bad modelling practices.
Superfluous Element. For an ontology O, a set of competency questions and
a set of validation SPARQL queries , if a named class, object property or data
property is not used in any SPARQL queries, it is considered a superfluous
element of O. An example is in Appendix 9.1.
Minimal Ontology Module.GivenanontologyOandacompetencyquestion
CQ , O is a minimal ontology module for CQ if we remove all superfluous
i i i
elements of O with respect to CQ .
i
Minor Issue.ForanontologyO andacompetencyquestionCQ ,ifO includes
i
all necessary elements except for only one object property or only one data
property, and adding this single element to O would make CQ modelled, this
i
is considered a minor issue in modelling CQ .
i
4 Methodology
The initial phase of our work involved manually creating a benchmark dataset
using available ontologies accompanied by their corresponding requirements for
CQverification[9].Weintroducedtwomethodsforontologygeneration,namely
Independent Ontology Generation and Incremental Ontology Generation, and
adapted existing prompting techniques in our experiments to guide LLMs in
generatingontologies.Inthisstudy,weprimarilyemployGPT-4,identifiedasthe
best-performing LLM in earlier comparative analyses [15,30]. Additionally, we
independently compare GPT-4 with OpenAI o1-preview and Llama-3.1-405B-
instruct-16b using the dataset proposed in Saeedizade and Blomqvist [30].
4.1 Dataset creation
InordertoevaluatethegeneratedontologiesusingCQverification[9],adataset
of CQs and user stories was developed, along with their corresponding minimal
ontologymodules.Theprocessinvolvedselectingasetofontologiesforthestudy,
extractingCQsandstories,andsubsequentlyextractingmodulesfromthesecho-
sen ontologies in order to have minimal units for easier evaluation and possible
future extensions of the work. The dataset combines two main types of sources:
extracteddatasetsandmanuallycreateddatasets.Theextracteddatasetsconsist
of CQs and stories derived from existing resources, where superfluous elements
were removed to identify minimal modules. In contrast, the manually created
datasets were created as a part of a controlled module engineering process. In
this case, we include the dataset present in [30] called “SemanticWebCourse”,

6 A. S. Lippolis et al.
wheremaster’sstudentswithacomputersciencebackgroundbutnopriorontol-
ogy design experience were tasked with creating semantic web solutions. Each
studentgroupsubmittedaninitialsolution,reviseditbasedonteacherfeedback,
and resubmitted a final version to pass the assignment, resulting in two distinct
solutions per group. However, as previous work questioned the generalisability
oftheLLMsgeneratingontologies[30],inthiswork,wegaveprioritytodifferent
ontology sources, primarily real-world ones.
An ontology was included in the dataset according to the following criteria:
The ontology includes (i) a set of competency questions and (ii) a set of cor-
responding user stories. These criteria were motivated by the eXtreme Design
methodology [28], which takes into consideration CQs and user stories as fun-
damental building blocks of ontologies. As a result, we selected a total of ten
ontologies,with100distinctCQs,and29differentuserstoriesfromfourreal-life
semantic web projects and three educational ones. More specifically, these on-
tologies have CQs assigned to specific minimal ontology modules with different
user story distributions.
Minimal ontology module partitioning. The main goal of developing the
dataset was to support the generation of ontologies using LLMs. The CQs and
user stories provide inputs for prompting techniques in the ontology generation
process.Theminimalontologymodulescontainedinthedatasetsprovideontol-
ogists with a gold standard for the expected output of the LLMs and are used
to assist the ontologists’ assessment, proving useful to be used in future work
to fine-tune LLMs. We followed a few steps to create minimal ontology modules
for each CQ. First, we manually checked to see if there were duplicate CQs and
removed them. Then, from the ontologies, we removed superfluous elements so
each module contains the minimum necessary classes and properties to effec-
tively model the CQ concerning the ontology story. Finally, these modules were
cross-checked and evaluated independently by two of the authors of this study.
Dataset composition. The dataset is composed of simple and complex
CQs. These have been divided into four categories as defined in Saeedizade and
Blomqvist [30]: Data Property Modelling (10 CQs) and Object Property Mod-
elling (25 CQs) are Simple CQs, while Reification (62 CQs) and Restrictions
(3 CQs) are Complex CQs. The CQs, stories and corresponding ontologies are
takenfromPolifonia3,Onto-DESIDE4,WHOW5,IKS6 andthedatasetusedin
Saeedizade and Blomqvist [30] consisting of three ontology stories and 15 CQs
each. As an additional baseline for the experiments in this paper we used the
same set of student solutions of the “SemanticWebCourse” as in [30]. In Saeed-
izade and Blomqvist, [30], the baseline for evaluation was the first submission
3 https://polifonia-project.eu/
4 https://ontodeside.eu
5 https://whowproject.eu/
6 https://cordis.europa.eu/project/id/231527

Ontology Generation using Large Language Models 7
and the last submissions of student groups, and because it is the current state
of the art in ontology generation, we use the same baseline in this paper for
comparison. The intuition behind using this baseline is to compare the mod-
elling abilities of LLMs to novice ontology engineers, with and without expert
feedback7.
4.2 Prompting Techniques
In the study by Saeedizade and Blomqvist [30], the performance of CQbyCQ,
a technique based on sub-task decomposition prompting [21], was found to be
similar to that of students in ontology development. In this prompting tech-
nique, an LLM models only one CQ at a time, and the output is merged with
the previously generated ontology. Due to its success, we incorporated two vari-
ations of this prompt to design our prompting techniques. Furthermore, in the
study of Lippolis et al.[22], Metacognitive Prompting has proven an effective
technique,especiallywhenOntologyDesignPatternswereprovided,togenerate
richer pattern-based ontology formalizations. The previous methodologies were
therefore refined and tested on the benchmark dataset.
Memoryless CQbyCQ. Memoryless CQbyCQ processes one CQ at a time,
utilizing the ontology story to guide the LLM with a prompt in generating an
ontology model for each CQ. It then merges the outputs into a single ontology.
Memoryless CQbyCQ is a variation of CQbyCQ [30] that does not provide
the LLM with the current state of ontology development. Unlike the CQbyCQ
method, the LLM does not have access to previously generated ontologies and
other CQs while modelling a specific CQ, which reduces the input context size
of the LLM by ∼60%. In fact, in Saeedizade and Blomqvist [30] it was shown
that long context can result in distraction of the LLM. Hence, the intuition
for removing the memory part is that slight overlaps between partial solutions
will be easier to resolve and correct by even a novice ontology engineer, than
completely irrelevant or inconsistent solutions, which could be the result of dis-
tractingthemodel.Asaresult,eachCQisindependentlymodelled,andthenall
the resulting models, representing CQs, are merged at the end. This prompting
technique guides an LLM, gives it an ontologist persona, and introduces Turtle
syntax for defining classes, properties, reifications, and other ontology engineer-
ing features. It also includes a story section that outlines ontology requirements
and a CQ, followed by common pitfalls in ontology development using LLMs,
such as producing an empty output or engaging in conversation.
Ontogenia technique. Ontogeniawasfirstdefinedin[22]andhasbeenfurther
refinedforthiswork.LiketheCQbyCQmethod,thispromptingtechniqueguides
anLLMbyinstructingittobeanontologyengineer,anddefinesbasicguidelines
foreffectiveontologyformalization.ThemodelprocessesoneCQatatime.When
7 We did not compare the original Ontogenia paper as, given its shortcomings, the
technique has been revisited for the decomposed prompting technique.

8 A. S. Lippolis et al.
prompted to model a set of CQs, it models and merges the generated ontology
ateachstepandprovidesitinthecontext.Theinputsforthepromptare:auser
story, which was not available in the previous work, a set of ODPs and possibly
previous output. The main idea was to transpose the Metacognitive Prompting
asdescribedinfivestepsinWangetal.[36]withtheXDmethodology[7],which
required (i) the use of pre-selected CQs and user stories; (ii) selection, reuse,
and integration of selected Ontology Design Patterns8; and (iii) iterative re-
evaluationtoverifycoverageofinitialrequirements.Intheinitialstage,theLLM
interpretsandcontextualizesrequirements,identifyingthecontextandbreaking
down the CQs into logical elements to support the systematic identification of
classes and properties. The next phase involves reflecting on the CQs to extend
the ontology by incorporating relevant rules and restrictions. Once the ontology
isdeveloped,thedecisionconfirmationstageensuresthefinaloutputisvalidated
withaclearexplanationofthereasoningprocess.Finally,theLLMevaluatesthe
ontology’sreasoning,creatingtestcaseswithinstancestovalidatethecorrectness
ofthegeneratedontology.Theresultingprocedure,mappedtothefiveMPsteps
isshownintheGithubrepository,alongwithmoredetailsaboutthistechnique.
Similarities and differences between Memoryless CQbyCQ and Onto-
genia. Although the methods are similar in nature, and use the same testing
setuptoensurecomparability,therearealsosomenotabledifferences.Ontogenia
explicitlyrequeststoprovidelabels,comments,inverserelationshipsandindivid-
uals.Furthermore,OntogeniarequirestheinjectionofOntologyDesignPatterns
fromtheODPrepository[8]andmakesuseoftheMetacognitivePromptingtech-
nique. Also, Ontogenia originally did not include scenarios in the prompt [22],
unlikeCQbyCQ[30].UnlikeOntogenia,MemorylessCQbyCQincludescommon
pitfallstoensuretheyareavoidedintheontologyoutputandattemptstoreduce
thecontextsize.Figure1showsanoverviewofthesetwopromptingtechniques.
Fig.1. Illustration of Memoryless CQbyCQ (top part) and Ontogenia (bottom part).
4.3 Ontology Generation Methods
Here, we present the two ontology generation methods used in our experiments,
as shown in Figure 5: Independent and Incremental Ontology Generation.
8 http://ontologydesignpatterns.org/

Ontology Generation using Large Language Models 9
Independent Ontology Generation In this method, each CQ with its cor-
responding ontology story is fed into an LLM using a prompting technique to
generate the corresponding ontology. This ensures that each CQ is treated as
a standalone unit, allowing for a focused assessment of the ontology generation
process on a per-question basis. By isolating each CQ, it becomes possible to
analyze the performance of the prompting techniques without interference from
interdependencies or complexities that may arise in multi-CQ contexts.
Incremental Ontology Generation Here, similar to CQbyCQ [30], all CQs
of a story are fed to an LLM at once, and a single OWL ontology is expected as
output. Unlike the independent approach, where each CQ is modelled in isola-
tion, this technique integrates solutions to multiple CQs to produce a cohesive
minimal ontology module representing the complete story and its requirements.
This method can be carried out either by merging the outputs for each CQ into
asingleontology(MemorylessCQbyCQ)orbyincorporatingtheoutputofeach
CQ incrementally into the prompt and joining it at each iteration (Ontogenia).
5 Evaluation Setup
Experimental Setup. The experiment consisted in running the Independent
OntologyGenerationmethodwithGPT-4-1106 withbothpromptingtechniques
across the entire dataset. For the Incremental Ontology Generation method, we
usedbothMemorylessCQbyCQandOntogeniawiththreedifferentLLMs(GPT-
4 1106,o1-preview,andLlama-3.1-405-Instruct-16b)solelyonthedatasetintro-
duced in Saeedizade and Blomqvist[30] of three semantic web course stories and
45 CQs.As a baseline for comparison we used their results [30], i.e. their best
solutions produced using GPT-4 with CQbyCQ, and the recorded scores of the
students’ submissions. In order to provide a comprehensive evaluation, each of
the solutions produced through these methods for the Independent and Incre-
mental Ontology Generation experiments has been evaluated by the proportion
of modelled CQs, with two ontology engineers cross-checking each other’s judg-
ments.Intheeventofanyconflictingassessment,theyengagedindiscussionsto
resolvethedisagreement.InthecaseoftheIncrementalOntologyEvaluationex-
periment, also standard ontology metrics through the OntOlogy Pitfall Scanner
(OOPS!) [26], as well as a structural analysis to evaluate the rate of superfluous
elements and a qualitative expert evaluation, were carried out. Due to lack of
resourcesandtime,wewerenotabletoperformthisevaluationonthecomplete
result set. For the LLMs, we used the default hyperparameters of o1-preview
andLlama-3.1-405-Instruct-16b;forGPT-4,temperatureandpenaltyaresetto
zero as recommended in Saeedizade and Blomqvist [30]. Figure 5 illustrates the
three evaluation steps.
Standard Ontology Metrics. The first step in evaluating the generated on-
tologies is applying standard evaluation metrics. We chose the OntOlogy Pitfall

| 10 A. | S. Lippolis et | al. |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- |
Fig.2.Illustrationofthetwoontologygenerationsettings(top)andthefourevaluation
steps for assessing the generated ontologies (bottom). The top setup generates an
ontology concerning only one CQ, which is evaluated individually. The second setup
generates an ontology covering multiple CQs associated with one story, which is then
evaluated.Atthebottom,thefourontologyevaluationsettingsareshown:OOPS!,the
proportion of modelled CQs, statistics of superfluous elements and expert evaluation.
Scanner (OOPS!)[26], due to its coverage of common modelling mistakes and
bestpractices.Intheresults,wereportonlythenumberofcriticalissuesrelated
to each method, as they are the only ones crucial to correct, while other pitfalls
| are not certain | to actually | represent modelling | flaws         | in the   | domain [26]. |          |
| --------------- | ----------- | ------------------- | ------------- | -------- | ------------ | -------- |
| Proportion      | of Modelled | CQs.                | In this step, | for each | CQ, we       | evaluate |
whether it is modelled in accordance with the definition provided in Section 3.
Additionally, we adopt a relaxed interpretation of this criterion by disregarding
minor issues, as outlined in Section 3. Finally, the proportion of CQs deemed
to be modelled, both with and without accounting for minor issues, is used to
compute an overall score representing the proportion of the total list of CQs
| being sufficiently | covered.  |             |           |      |                |       |
| ------------------ | --------- | ----------- | --------- | ---- | -------------- | ----- |
| Structural         | Analysis. | We manually | evaluated | each | OWL file using | three |
novel criteria with respect to superfluous elements 3, i.e., superfluous named
classes, object properties, and data properties. We reported the rate of super-
fluous elements by dividing the number of superfluous elements by the total of
that element and compared them to the rates in Saeedizade and Blomqvist [30].
| Expert | Qualitative | Analysis. The | expert | qualitative | analysis was | con- |
| ------ | ----------- | ------------- | ------ | ----------- | ------------ | ---- |
ducted by two experienced knowledge engineers, not involved in the practical
ontologygenerationtask,whocarefullyandindependentlyevaluatedtheoutputs
generatedbythebestperformingopen-andclosed-sourceLLMs,Llama-3.1-405-
Instruct-16b, and OpenAI o1-preview. The experts were instructed to assess the
LLM-generatedontologyfilesasiftheywerestudents’coursesubmissionsandto
provide feedback accordingly. Therefore, they focused on: (i) assessing the gen-
eral quality of the output with dedicated comments on usability, completeness,
andaccuracyoftheproducedoutput,andmentioninganyontologyerrorsfound;
and (ii) assessing the ontology with respect to the adequacy of the modelling
CQ9,
| solutions | for each | with a substantial | agreement | (Cohen’s | kappa: | 0.61). |
| --------- | -------- | ------------------ | --------- | -------- | ------ | ------ |
9 The “not adequate” assessment combines two judgments by the KE experts, i.e. a
| clear“no” | wheretheCQisnotmodelled,anda“maybe” |     |     | categorywheretheontology |     |     |
| --------- | ----------------------------------- | --- | --- | ------------------------ | --- | --- |
simplydoesnotallowforaccurateassessmentoftheCQ,forinstance,duetousability
| issues, | naming etc. |     |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- | --- |

Ontology Generation using Large Language Models 11
6 Results
In this section, we start by examining the results of the OOPS! resource on
the incrementally generated ontologies. Then, we compare the two prompting
techniques introduced in this paper by going in-depth into the modelling results
with respect to the assessment of the proposed ontology generation methods.
Morespecifically,wemeasuretheproportionofmodelledCQsforallexperiments
and analyze the structure of the generated ontologies concerning superfluous
elements. For the Incremental Ontology Generation method, we focus on the
“SemanticWebCourse” datasetsinceitcontains15CQsassociatedwithonestory
while others have ∼2 on average and choose the best performing open- and
closed-source LLMs to compare across both previous work [30] and the results
of Independent CQ Generation. In this way, we can test the LLMs’ capability
to generate an ontology incrementally. Finally, we present the results of the
assessment by the two KE experts who analyzed the outputs.
Standard Ontology Metrics. After running OOPS! on the ontologies gener-
atedbytheIncrementalmethodforthe“SemanticWebCourse” stories(Hospital,
Music, and Theatre), the resulting pitfalls are shown in Table 1. Overall, there
are a few critical pitfalls for specific combinations of LLMs and prompting tech-
niques.Themostcommonflawishavingmultipledomainsorranges,whichisin
linewithourotherresultsdiscussedfurtherinthefollowingsections(seeSection
7).Inthiscase,thedomainorrange(orboth)ofaproperty(objectordataprop-
erty) is defined by more than one rdfs:domain or rdfs:range axiom. In OWL,
multiple rdfs:domain or rdfs:range axioms are allowed, but are interpreted as a
conjunction.Therefore,theyareequivalenttotheconstructowl:intersectionOf,
which could generate many unwanted inferences or even inconsistencies in the
ontology. Some issues with inverse relations are also noted, as well as missing
declarationsofnamespaces.Lastly,OpenAIo1-preview producedthefewestcriti-
calissueswhenusingMemorylessCQbyCQ,whereasLlama-3.1-405-instruct-16b
generated, with both methods, files with the most critical pitfalls.
Table 1. Pitfalls after OOPS! pitfall scanning for Incremental Ontology Generation.
Resultsaremergedbythethreestoriesinthe“SemanticWebCourse”.Llama*refersto
Llama-3.1-405-instruct-16b. For the CQbyCQ method, only GPT-4 was used [30].
CQbyCQMemorylessCQbyCQ Ontogenia
GPT-4 GPT-4Llama* o1 GPT-4Llama*o1
P05Wronginverserelationships 0 1 25 0 2 7 5
P06Cyclesinaclasshierarchy 0 0 2 0 5 0 11
P19Multipledomainsorranges 0 23 32 1 4 15 0
P29Wrongtransitiverelationship 0 0 0 1 0 0 0
P37Ontologynotavailable 3 2 0 0 0 0 0
P39Ambiguousnamespace 3 2 0 1 1 0 0

12 A. S. Lippolis et al.
Independent Ontology Generation Results. The evaluation of the Memo-
rylessCQbyCQandOntogeniatechniquesonGPT-4 showsthattheproportion
of correctly modelled CQs was 0.91 and 0.84, respectively (0.94 and 0.89 by
ignoring minor issues), with significantly lower scores for complex CQs (0 and
0.66 respectively). These results show that by overlooking minor issues both
prompting techniques are effective for modelling single CQs in isolation.
Incremental Ontology Generation Results. The results of the Incremen-
tal Ontology Generation are presented in Figure 3. Ontogenia with OpenAI
o1-preview is the best-performing combination with respect to this evaluation
criterion. Compared to the students’ submissions for the “SemanticWebCourse”,
Ontogenia and Memoryless CQbyCQ with any LLM exceeded the proportion
of CQs being modelled by students by a noticeable margin. Also, Memory-
less CQbyCQ performed better than the CQbyCQ technique in Saeedizade and
Blomqvist[30], possibly suggesting that using partially generated ontology mod-
elsasdata“inmemory” forLLMs,whichincludespreviouslygeneratedresponses
toCQmodelling,actuallymaydiminishtheirperformance.Thisresulthighlights
the importance of reducing the input context size for LLMs, which is consistent
with the findings in Saeedizade and Blomqvist[30]. The proportion of correctly
modelled CQs is analyzed across four categories: datatype property (DP), ob-
ject property (OP), reification (Reif.), and restrictions (Rest.) for the Theatre,
Music, and Hospital Story. We compared GPT-4, Llama-3.1-405B-instruct-bf16
and OpenAI o1-preview. The evaluation shows that Ontogenia with OpenAI o1-
preview achieves the highest number of correctly modelled CQs. Overall, both
OntogeniaandMemorylessCQbyCQsurpassthestudents’lastsubmissionsand
the state of the art in ontology generation [30]. Moreover, Llama-3.1 in both
prompting techniques had shortcomings in modelling reification CQs.
Fig.3. Scoresfor“SemanticWebCourse” fromtheoutputsforthedifferentprompting
techniquescomparedwithstudents’submissionsaccordingtotheproportionoftheCQs
that were accurately modelled. ‘IG’ indicates results when minor issues are ignored.
Llama⋆ refers to Llama-3.1-405B-instruct-bf16.
Structural Analysis. Table 2 presents our structural analysis regarding the
superfluous elements. The results, compared to those in Section 6, show that

|     |     |     | Ontology | Generation | using | Large | Language | Models | 13  |
| --- | --- | --- | -------- | ---------- | ----- | ----- | -------- | ------ | --- |
the Memoryless CQbyCQ and Ontogenia, despite their performance measured
in other criteria, yield a significant number of superfluous elements within the
ontology. This underscores the importance of applying additional criteria for
evaluating ontologies constructed using LLMs. CQbyCQ with GPT-4 produces
the fewest superfluous elements compared to our newly introduced prompting
techniques, while the Memoryless CQbyCQ approach yields comparable results.
Conversely, Llama-3.1-405B-instruct-bf16 generates numerous superfluous ele-
mentsacrossbothtechniquesandallstories,witharatecloseto40%,indicating
| that this | model | tends | to produce | many | superfluous | classes | and | properties. |     |
| --------- | ----- | ----- | ---------- | ---- | ----------- | ------- | --- | ----------- | --- |
Table 2.Comparisonofthethreepromptingtechniques,usingtheIncrementalOntol-
ogy Generation method, for generating superfluous elements across different ontology
domains(Theatre,Music,andHospital).Eachcellrepresentstheproportionofsuper-
fluous elements relative to the total number of elements of that type (%). CQbyCQ
was only tested with GPT-4 due to its low CQ-coverage. Rates under 15% are bolded
| (best performance), |     | and | rates | over 50%         | are in red                                     | (worst performance). |     |     |     |
| ------------------- | --- | --- | ----- | ---------------- | ---------------------------------------------- | -------------------- | --- | --- | --- |
|                     |     |     |       | Superflu.Classes | Superflu.Obj.PropertiesSuperflu.DataProperties |                      |     |     |     |
PromptingTechnique
|                  |     |     | TheatreMusicHospitalTheatreMusic |             |      | Hospital  | TheatreMusic | Hospital  |     |
| ---------------- | --- | --- | -------------------------------- | ----------- | ---- | --------- | ------------ | --------- | --- |
| CQbyCQ(GPT-4)    |     |     |                                  | 14.3        |      |           |              | 28.5 18   |     |
|                  |     |     |                                  | 0 8.6       | 0    | 4.2 6.6   | 12.5         |           |     |
| Ontogenia(GPT-4) |     |     |                                  | 0 19.2 13.5 | 4    | 38.9 29.6 | 45.5         | 55.5 22.2 |     |
| Ontogenia(Llama) |     |     | 47.1                             | 32.1 37.5   | 40.6 | 45.9 38.3 | 16.7         | 0 100     |     |
| Ontogenia(o1)    |     |     | 16.7                             | 27.3        | 29.4 | 55.2 37   | 28.6         | 66.7 45.5 |     |
12.5
| MemorylessCQbyCQ(GPT-4) |     |     | 25.7 | 31.2 38.9 | 17.4 | 20.9 16.2 | 48  | 40.9 46.1 |     |
| ----------------------- | --- | --- | ---- | --------- | ---- | --------- | --- | --------- | --- |
| MemorylessCQbyCQ(Llama) |     |     | 45.6 | 42.3 23.9 | 20.5 | 25.6 41.7 | 60  | 60.7      |     |
13.6
| MemorylessCQbyCQ(o1) |     |     | 29.3 | 50 28.6 | 14.8 | 0 7.4 | 10  | 0 28.6 |     |
| -------------------- | --- | --- | ---- | ------- | ---- | ----- | --- | ------ | --- |
Expert Qualitative Analysis. After analyzing the results presented in Ta-
bles 1 and 2 and bar charts in Figure 3, we conclude that OpenAI o1-preview,
especially with Ontogenia, seems to produce less errors overall than GPT-4,
and provides a better trade-off between different error types, notwithstanding
all the generated files showed incorrect domains and ranges. Therefore, Llama-
3.1-405B-instruct-bf16 and OpenAI o1-preview are confirmed as the best open-
source and closed-source LLMs, respectively, across both previous experiments
[30] and the ones proposed in this work. The former’s performance was not im-
pressive: the ontologies generated by Llama-3.1-405B-instruct-bf16 show struc-
tural flaws, including inconsistent naming, redundant classes, and overlapping
domains/ranges. The taxonomy shows circular references and poor property or-
ganization. Key issues include malformed cardinality restrictions, lack of com-
ments/labels,andmisalignednamespaces.Apartfromsuperfluouselements,flat
propertyhierarchies,andinconsistentaxiomatisation,arevisible.Table3shows,
foreachselectedstory,theresultingpercentagescoresfromtheadequacyassess-
ment of the qualitative evaluation. Different results are calculated as an average
| between | the two. | The | full qualitative |     | analysis can | be seen | on  | Github. |     |
| ------- | -------- | --- | ---------------- | --- | ------------ | ------- | --- | ------- | --- |

| 14 A. S. | Lippolis | et al. |     |     |     |     |     |
| -------- | -------- | ------ | --- | --- | --- | --- | --- |
Table3.AdequateCQmodelling(%)byLlamaando1modelsfortheselectedstories.
|     | Story   | Model            |     | Llama-3.1-405 |      | o1-preview |      |
| --- | ------- | ---------------- | --- | ------------- | ---- | ---------- | ---- |
|     |         | MemorylessCQbyCQ |     |               | 0.6  |            | 0.9  |
|     | Music   | Ontogenia        |     |               | 0.86 |            | 0.96 |
|     | Theatre | MemorylessCQbyCQ |     |               | 0.66 |            | 0.73 |
|     |         | Ontogenia        |     |               | 0.63 |            | 1.0  |
|     |         | MemorylessCQbyCQ |     |               | 0.63 |            | 0.73 |
Hospital
|     |     | Ontogenia |     |     | 0.66 |     | 1.0 |
| --- | --- | --------- | --- | --- | ---- | --- | --- |
7 Discussion
| In this section, | we present | a   | discussion | of  | the results. |     |     |
| ---------------- | ---------- | --- | ---------- | --- | ------------ | --- | --- |
Overallresults.Accordingtothefindings,andsimilarlytopreviouswork[30],
the use of an LLM yields promising results in supporting ontology engineering
processes. In the Independent Ontology Generation, Memoryless CQbyCQ and
OntogeniaperformwellwithSingleDataPropertyCQsandSingleObjectProp-
erty CQs, but worse on generating Reifications and Restrictions. For the Incre-
mentalOntologyGenerationmethod,OntogeniaandMemorylessCQbyCQout-
performed previous methods, including the students’ solutions, with Ontogenia
combined with OpenAI o1-preview yielding the highest percentage of modelled
CQs.However,thestructuralanalysisrevealsthatwithrespecttopreviouswork,
thetwopromptingtechniquesgeneratemoresuperfluouselementsandyieldcrit-
ical pitfalls according to OOPS!. These structural issues are also noted by the
experts in their evaluation, which found many flaws in the Llama-generated on-
tologies related to the usability and understandability of the solutions, while
o1-generated ontologies are overall comparable to a student in the case of Mem-
| orylessCQbyCQ    | and | even better | in  | the case | of Ontogenia.    |     |                   |
| ---------------- | --- | ----------- | --- | -------- | ---------------- | --- | ----------------- |
| Multidimensional |     | evaluation. |     | Our      | multidimensional |     | evaluation demon- |
strates that expert assessments align closely with both the standard and struc-
tural metrics used in this study. This suggests that experts, perhaps implicitly,
rely on similar criteria when evaluating ontologies, resulting in evaluations that
comprehensively address most aspects. At the same time, we still need qualita-
| tive evaluation | for a     | holistic | assessment | of    | LLM-generated |               | ontologies.    |
| --------------- | --------- | -------- | ---------- | ----- | ------------- | ------------- | -------------- |
| Superfluous     | elements. |          | An issue   | noted | in            | LLM-generated | ontologies in- |
volves the creation of superfluous properties with the same domain and range
or multiple classes and properties that could be considered equal. For example,
employedSinceand employmentStartDatearegenerated forthesame CQ,but
onlyoneisneeded.Thisraisesquestionsaboutsuperfluouselements:theirnum-
ber, why they are generated by the LLM, and their consequences. At the same
time,havingsuperfluouselements(inmoderatenumbers)maybeconsideredless
important than having an unmodeled CQs or more complex errors. Thus, our
prompting techniques can be considered more complete and more usable than
previous work [30], which was less accurate (Table 2), but more concise. In our
envisionedsettingofafutureontologyengineeringco-pilot,superfluouselements
canbeidentified,e.g.throughOOPS!,andmanuallyremovedoravoidedwithan
evenmoreelaborateprompt.Asourapproachaimstoassistratherthanreplace
| ontology engineers, | we  | believe | this is | acceptable. |     |     |     |
| ------------------- | --- | ------- | ------- | ----------- | --- | --- | --- |

Ontology Generation using Large Language Models 15
8 Conclusion
In this paper, we introduced two novel and improved prompting techniques
for ontology generation, Memoryless CQbyCQ and Ontogenia, assessing them
through a multi-dimensional evaluation and with a new dataset with respect to
previous studies. The results show the proposed prompting techniques proved
promising to support the generation of ontologies that meet a predefined set of
requirements, improving the proportion of modelled CQs, surpassing previous
approachesandnoviceontologymodellers.However,challengeslikemultipledo-
mains or ranges and other pitfalls were highlighted both by the OOPS! pitfall
scanner and the expert evaluation. Both prompting techniques often generated
superfluous elements, which (in low numbers) are not detrimental to ontology
usability, compared to other major errors involving wrong axiomatisation and
mistakes in the taxonomy. Returning to our research questions, regarding (i) to
whatextentLLMscanbeusedtosupportthegenerationofontologiesthatmeet
a predefined set of requirements, we conclude that current commercial models,
such as OpenAI o1, can certainly perform on par with non-experts, at least
when using a carefully selected prompt. Regarding (ii) what evaluation criteria
are suitable for evaluating LLM-generated ontologies, we conclude that it is not
sufficient to use one single criteria, nor simple automated evaluation metrics to
detecterrorsandcompareperformance.Instead,ratherelaboratemanualmeth-
ods are needed, e.g. to detect the amount of superfluous classes and properties.
Finally,regarding(iii)whatthestrengthsandweaknessesofontologiesgenerated
using LLMs are, we believe that if cost is not an issue and commercial models
can be used, then certainly novice ontology engineers could benefit from such
draft ontologies generated by those LLMs. These drafts can increase modelling
quality, and considerably reduce the effort and time to kick-start the modelling.
However,certainweaknessesareobservedacrossalltheexperiments,suchaser-
roneous domain and range restrictions, erroneous inverse property axioms, and
superfluous or overlapping classes and properties.
Acknowledgments. This project has received funding from the European Union’s
HorizonEuroperesearchandinnovationprogrammeundergrantagreementsno.101058682
(Onto-DESIDE) and 101070588 (HACID), and is supported by the strategic research
areaSecurityLink.Thestudentsolutionsusedintheresearchwerecollectedaspartof
amaster’scoursetaughtbyAssoc.Prof.BlomqvistwhileemployedatJönköpingUni-
versity.AdditionalfinancialsupporttothisprojectwasprovidedbyNextGenerationEU
underNRRPGrantagreementn.MURIR0000008-FOSSR(CUPB83C22003950001).
This work was also supported by the PhD scholarship “Discovery, Formalisation and
Re-use of Knowledge Patterns and Graphs for the Science of Science”, funded by
CNR-ISTC through the WHOW project (EU CEF programme - grant agreement no.
INEA/CEF/ICT/A2019/2063229).FinallywethankOpenAI’sResearcherAccessPro-
gram Grant for the API credits.
Disclosure of Interests. The authors have no competing interests to declare that
are relevant to the content of this article.

16 A. S. Lippolis et al.
References
1. Alharbi, R., de Berardinis, J., Grasso, F., Payne, T., Tamma, V.: Characteristics
and desiderata for competency question benchmarks. In: The Semantic Web –
ISWC 2024: 23rd International Semantic Web Conference, Baltimore, MD, USA,
November 11–15, 2024, Proceedings (2024)
2. Ali, R., Tang, O.Y., Connolly, I.D., Fridley, J.S., Shin, J.H., Zadnik Sullivan,
P.L., Cielo, D., Oyelese, A.A., Doberstein, C.E., Telfeian, A.E., Gokaslan, Z.L.,
Asaad, W.F.: Performance of chatgpt, gpt-4, and google bard on a neurosurgery
oral boards preparation question bank. Neurosurgery 93(5), 1090–1098 (2023).
https://doi.org/10.1227/neu.0000000000002551
3. Allen,B.,Groth,P.:Abenchmarkforthedetectionofmetalinguisticdisagreements
between llms and knowledge graphs. In: The Semantic Web – ISWC 2024: 23rd
International Semantic Web Conference, Baltimore, MD, USA, November 11–15,
2024, Proceedings (2024)
4. Babaei Giglou, H., D’Souza, J., Auer, S.: Llms4ol: Large language models for on-
tologylearning.In:Payne,T.R.,Presutti,V.,Qi,G.,Poveda-Villalón,M.,Stoilos,
G., Hollink, L., Kaoudi, Z., Cheng, G., Li, J. (eds.) The Semantic Web – ISWC
2023. pp. 408–427. Springer Nature Switzerland, Cham (2023)
5. Balloccu, S., Schmidtová, P., Lango, M., Dusek, O.: Leak, cheat, repeat: Data
contamination and evaluation malpractices in closed-source LLMs. In: Graham,
Y.,Purver,M.(eds.)Proceedingsofthe18thConferenceoftheEuropeanChapter
of the Association for Computational Linguistics (Volume 1: Long Papers). pp.
67–93.AssociationforComputationalLinguistics,St.Julian’s,Malta(Mar2024),
https://aclanthology.org/2024.eacl-long.5
6. Blomqvist, E., Hammar, K., Presutti, V.: Engineering ontologies with patterns-
the extreme design methodology. In: Ontology Engineering with Ontology Design
Patterns. IOS Press (2016)
7. Blomqvist, E., Presutti, V., Daga, E., Gangemi, A.: Experimenting with extreme
design.In:Cimiano,P.,Pinto,H.S.(eds.)KnowledgeEngineeringandManagement
bytheMasses.pp.120–134.SpringerBerlinHeidelberg,Berlin,Heidelberg(2010)
8. Blomqvist,E.,Sandkuhl,K.:Patternsinontologyengineering:Classificationofon-
tologypatterns.In:ProceedingsoftheSeventhInternationalConferenceonEnter-
priseInformationSystems-Volume3:ICEIS,.pp.413–416.INSTICC,SciTePress
(2005). https://doi.org/10.5220/0002518804130416
9. Blomqvist, E., Seil Sepour, A., Presutti, V.: Ontology testing-methodology and
tool. In: Knowledge Engineering and Knowledge Management: 18th International
Conference, EKAW 2012, Galway City, Ireland, October 8-12, 2012. Proceedings
18. pp. 216–226. Springer (2012)
10. Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Nee-
lakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A.,
Krueger,G.,Henighan,T.,Child,R.,Ramesh,A.,Ziegler,D.,Wu,J.,Winter,C.,
Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark, J., Berner,
C., McCandlish, S., Radford, A., Sutskever, I., Amodei, D.: Language models are
few-shotlearners.In:Larochelle,H.,Ranzato,M.,Hadsell,R.,Balcan,M.,Lin,H.
(eds.)AdvancesinNeuralInformationProcessingSystems.vol.33,pp.1877–1901.
CurranAssociates,Inc.(2020),https://proceedings.neurips.cc/paper_files/
paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf
11. Chu, Z., Chen, J., Chen, Q., Yu, W., He, T., Wang, H., Peng, W., Liu, M., Qin,
B.,Liu,T.:Asurveyofchainofthoughtreasoning:Advances,frontiersandfuture.
arXiv preprint arXiv:2309.15402 (2023)

Ontology Generation using Large Language Models 17
12. Fathallah, N., Das, A., De Giorgis, S., Poltronieri, A., Haase, P., Kovriguina, L.:
Neon-gpt:Alargelanguagemodel-poweredpipelineforontologylearning.In:Pro-
ceedings of the ESWC2024 Special Track: Large Language Models for Knowledge
Engineering (to appear) (2024)
13. Fathallah, N., Staab, S., Algergawy, A.: Llms4life: Large language models for on-
tology learning in life sciences. (2024)
14. Fernández, M., Gómez-Pérez, A., Juristo, N.: Methontology: from ontological art
towardsontologicalengineering.In:ProceedingsoftheAAAI97SpringSymposium
Series on Ontological Engineering (1997)
15. Frey,J.,Meyer,L.P.,Brei,F.,Grunder-Fahrer,S.,Martin,M.:Assessingtheevolu-
tionofllmcapabilitiesforknowledgegraphengineeringin2023.In:Proceedingsof
theESWC2024SpecialTrack:LargeLanguageModelsforKnowledgeEngineering
(to appear) (2024)
16. Gangemi,A.:Ontologydesignpatternsforsemanticwebcontent.In:TheSemantic
Web–ISWC 2005: 4th International Semantic Web Conference, ISWC 2005, Gal-
way, Ireland, November 6-10, 2005. Proceedings 4. pp. 262–276. Springer (2005)
17. Garijo,D.,Poveda-Villalón,M.,Amador-Domínguez,E.,Wang,Z.,Garía-Castro,
R.,Corcho,O.:Llmsforontologyengineering:Alandscapeoftasksandbenchmark-
ing challenges. In: The Semantic Web – ISWC 2024: 23rd International Semantic
WebConference.Baltimore,MD,USA(November11–152024),proceedingsofthe
23rd International Semantic Web Conference (ISWC 2024)
18. Hanna, E., Levic, A.: Comparative Analysis of Language Models: Hallucinations
in ChatGPT: Prompt Study. Master’s thesis, Linnaeus University (2023)
19. He,Y.,Chen,J.,Dong,H.,Horrocks,I.,Allocca,C.,Kim,T.,Sapkota,B.:Deep-
onto: A python package for ontology engineering with deep learning. (To appear
in the Semantic Web Journal) (2024)
20. Keet, C.M., Khan, Z.C.: On the roles of competency questions in ontology engi-
neering. In: International Conference on Knowledge Engineering and Knowledge
Management. pp. 123–132. Springer (2024)
21. Khot,T.,Trivedi,H.,Finlayson,M.,Fu,Y.,Richardson,K.,Clark,P.,Sabharwal,
A.: Decomposed prompting: A modular approach for solving complex tasks. In:
The Eleventh International Conference on Learning Representations, ICLR 2023,
Kigali, Rwanda, May 1-5, 2023 (2023)
22. Lippolis, A.S., Ceriani, M., Zuppiroli, S., Nuzzolese, A.G.: Ontogenia: Ontology
Generation with Metacognitive Prompting in Large Language Models. In: Poster
and demos track, Satellite proceedings of ESWC2024 (to appear) (2024)
23. Mateiu, P., Groza, A.: Ontology engineering with large language models. In: 2023
25thInternationalSymposiumonSymbolicandNumericAlgorithmsforScientific
Computing (SYNASC). pp. 226–229. IEEE (2023)
24. Peroni, S.: A simplified agile methodology for ontology development. In: OWL:
Experiences and Directions–Reasoner Evaluation, pp. 55–69. Springer (2016)
25. Plu, J., Escobar, O.M., Trouillez, E., Gapin, A., Troncy, R.: A comprehensive
benchmarkforevaluatingllm-generatedontologies.In:TheSemanticWeb–ISWC
2024:23rdInternationalSemanticWebConference,Baltimore,MD,USA,Novem-
ber 11–15, 2024, Proceedings (2024)
26. Poveda-Villalón,M.,Gómez-Pérez,A.,Suárez-Figueroa,M.C.:OOPS!(OntOlogy
Pitfall Scanner!): An On-line Tool for Ontology Evaluation. International Journal
on Semantic Web and Information Systems (IJSWIS) 10(2), 7–34 (2014)
27. Poveda-Villalón, M., Fernández-Izquierdo, A., Fernández-López, M., García-
Castro,R.:Lot:Anindustrialorientedontologyengineeringframework.Engineer-

| 18 A. S.         | Lippolis | et al.        |              |     |             |         |     |     |     |
| ---------------- | -------- | ------------- | ------------ | --- | ----------- | ------- | --- | --- | --- |
| ing Applications |          | of Artificial | Intelligence |     | 111, 104755 | (2022). |     |     |     |
https://doi.org/
https://doi.org/10.1016/j.engappai.2022.104755
28. Presutti, V., Daga, E., Gangemi, A., Blomqvist, E.: extreme design with content
| ontology | design | patterns. | In: Proc. | Workshop | on  | Ontology | Patterns. | pp. | 83–97. |
| -------- | ------ | --------- | --------- | -------- | --- | -------- | --------- | --- | ------ |
| CEUR-WS  | (2009) |           |           |          |     |          |           |     |        |
29. Rebboud, Y., Lisena, P., Tailhardat, L., Troncy, R.: Benchmarking llm-based on-
| tology conceptualization: |          |        | A proposal.     | In: | The Semantic |     | Web – ISWC    | 2024: | 23rd   |
| ------------------------- | -------- | ------ | --------------- | --- | ------------ | --- | ------------- | ----- | ------ |
| International             | Semantic |        | Web Conference, |     | Baltimore,   | MD, | USA, November |       | 11–15, |
| 2024, Proceedings         |          | (2024) |                 |     |              |     |               |       |        |
30. Saeedizade,M.J.,Blomqvist,E.:Navigatingontologydevelopmentwithlargelan-
| guage models. | In: | European | Semantic |     | Web Conference. |     | pp. 143–161. |     | Springer |
| ------------- | --- | -------- | -------- | --- | --------------- | --- | ------------ | --- | -------- |
(2024)
31. Shimizu,C.,Hammar,K.,Hitzler,P.:Modularontologymodeling.SemanticWeb
| 14(3), 459–489 | (2023). |     |     |     |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.3233/SW-222886
32. Suárez-Figueroa,M.C.,Gómez-Pérez,A.,Fernández-López,M.:Theneonmethod-
| ology for | ontology     | engineering. |        | In: Suárez-Figueroa, |             |     | M.C., Gómez-Pérez, |        | A., |
| --------- | ------------ | ------------ | ------ | -------------------- | ----------- | --- | ------------------ | ------ | --- |
| Motta,    | E., Gangemi, | A.           | (eds.) | Ontology             | Engineering | in  | a Networked        | World, | pp. |
9–34.SpringerBerlinHeidelberg,Berlin,Heidelberg(2012).https://doi.org/10.
1007/978-3-642-24794-1_2
33. Suárez-Figueroa, M., Gómez-Pérez, A., Motta, E., Gangemi, A. (eds.): Ontology
| Engineering | in a | Networked | World. | Springer | (2012) |     |     |     |     |
| ----------- | ---- | --------- | ------ | -------- | ------ | --- | --- | --- | --- |
34. Tsaneva, S., Herwanto, G.B., Sabou, M.: Benchmarking ontology validation capa-
| bilities of | llms. In: | The | Semantic | Web – | ISWC 2024: | 23rd | International |     | Semantic |
| ----------- | --------- | --- | -------- | ----- | ---------- | ---- | ------------- | --- | -------- |
WebConference,Baltimore,MD,USA,November11–15,2024,Proceedings(2024)
35. Wang, B., Min, S., Deng, X., Shen, J., Wu, Y., Zettlemoyer, L., Sun, H.: Towards
| understanding | chain-of-thought |         |     | prompting:      | An empirical |                   | study of | what        | matters. |
| ------------- | ---------------- | ------- | --- | --------------- | ------------ | ----------------- | -------- | ----------- | -------- |
| In: The       | 61st Annual      | Meeting | Of  | The Association |              | For Computational |          | Linguistics |          |
(2023)
36. Wang, Y., Zhao, Y.: Metacognitive prompting improves understanding in large
| language        | models.      | In: Duh,                                         | K.,            | Gomez, H.,    | Bethard,     | S.           | (eds.) Proceedings |       | of the   |
| --------------- | ------------ | ------------------------------------------------ | -------------- | ------------- | ------------ | ------------ | ------------------ | ----- | -------- |
| 2024 Conference |              | of the                                           | North American |               | Chapter      | of the       | Association        | for   | Compu-   |
| tational        | Linguistics: | Human                                            | Language       |               | Technologies | (Volume      | 1:                 | Long  | Papers). |
| pp. 1914–1926.  |              | Association                                      | for            | Computational |              | Linguistics, | Mexico             | City, | Mex-     |
| ico (Jun        | 2024).       | https://doi.org/10.18653/v1/2024.naacl-long.106, |                |               |              |              |                    |       |          |
https:
//aclanthology.org/2024.naacl-long.106
37. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou,
| D., et al.:  | Chain-of-thought |        | prompting   | elicits    | reasoning |     | in large language |     | models. |
| ------------ | ---------------- | ------ | ----------- | ---------- | --------- | --- | ----------------- | --- | ------- |
| In: Advances | in               | Neural | Information | Processing | Systems.  |     | pp. 24824–24837   |     | (2022)  |

|     |     |     | Ontology | Generation | using | Large | Language |     | Models | 19  |
| --- | --- | --- | -------- | ---------- | ----- | ----- | -------- | --- | ------ | --- |
9 Appendix
| 9.1 Examples |     | of  | Evaluation | Metrics |     |     |     |     |     |     |
| ------------ | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
Modelled CQ: In Figure 4, part A (top), a CQ such as “Who is the author of
abook?” isshowntobecorrectlymodelled,asalltheelementsrequiredtowrite
| a SPARQL | query  | are | present | in the model | (dotted  |     | box).  |          |            |     |
| -------- | ------ | --- | ------- | ------------ | -------- | --- | ------ | -------- | ---------- | --- |
| Minor    | Issue: | In  | part    | B, for the   | same CQ, | an  | object | property | to connect |     |
Book and Author (or either connecting it to Person or a new data property) is
missing. However, adding “authorOf” would resolve the issue. This is considered
| a minor     | error, | as the    | ontology | modeller  | can     | easily | add this | element. |           |      |
| ----------- | ------ | --------- | -------- | --------- | ------- | ------ | -------- | -------- | --------- | ---- |
| Superfluous |        | Elements: |          | In Figure | 4, part | A,     | for the  | given    | CQ, there | is a |
class “Person” and properties such as “name” or “wrote” that are not used in the
SPARQLquery(top-rightcorner).Sincethey(outsideofthedottedbox)donot
| appear | in the | SPARQL, | they | are referred | to  | as superfluous |     | elements. |     |     |
| ------ | ------ | ------- | ---- | ------------ | --- | -------------- | --- | --------- | --- | --- |
Fig.4. Analysis of an ontology for a CQ. Part A shows a correctly modelled CQ, en-
suringallnecessaryelementsforaSPARQLqueryarepresent,butcontainsuperfluous
| elements. | Part | B shows | a minor | issue where | a data | property | is  | missing. |     |     |
| --------- | ---- | ------- | ------- | ----------- | ------ | -------- | --- | -------- | --- | --- |
EachmetricevaluatesaspecificaspectoftheLLM-generatedontology,asno
single metric is sufficient to provide a comprehensive assessment. For instance,
Llamaproducesmanysuperfluouselements,henceitalsohasareasonablelikeli-
hood of randomly modelling certain simple CQs correctly. By penalizing super-
fluouselements,wepreventLLMsfromgeneratingtoomanyunnecessaryclasses
andproperties;however,thisapproachmayalsodiscouragethegenerationoftax-
onomies or more generalized modelling, which is a disadvantage. By combining
| all metrics,   | we  | can achieve |      | an holistic | evaluation | of  | ontology | generation. |     |     |
| -------------- | --- | ----------- | ---- | ----------- | ---------- | --- | -------- | ----------- | --- | --- |
| 9.2 Discussion |     | on          | LLMs |             |            |     |          |             |     |     |
Comparison of LLMs.BycomparingtheresultsoftheLLMsinSection6,we
canobservethato1-previewisthemostpromisingLLMforontologygeneration
andGPT-4mayserveasitsreplacement.However,whileLlamaexhibitssimilar
performance to GPT-4 in correctly modelling CQs, it produces a considerable
number of superfluous elements and critical OOPS! pitfalls and performs the

20 A. S. Lippolis et al.
worst according to the expert evaluation. Thus, it may still not be possible to
createanontologyengineeringco-pilotusingopenmodels,andhencetheissueof
costandtherisksrelatedtotheblack-boxnatureofproprietarymodels,remain.
Context size. Comparing the scores of Memoryless CQbyCQ with other
techniques shows that reducing the input context size of GPT-4 significantly
enhancestheoutputscoreofthismodeldespiteproducingsomesuperfluousele-
ments.Theseresultshighlightatrade-offbetweencomputationalefficiency,cost,
and output quality. If quality is a priority but resources are limited, Memory-
less CQbyCQ balances efficiency and speed, though it may require additional
post-processing to refine the output.
9.3 Limitations
Data leakage assessment A critical consideration in our ontology selection
criteria and dataset publication is the potential for data leakage [5], due to
the online accessibility of some of this material. Such exposure introduces risks,
namelythelikelihoodofevaluatingLLMsonthesamedatasetstheyweretrained
on.Also,thedatasetpublishedinthispaperasagoldstandardmightbeusedin
thetrainingdataoffutureLLMs.Ourselectedontologiesarepublishedwiththeir
CQs and user stories separately from their ontology models, which can mitigate
these risks. The ontologies from the courses (Music, Hospital and Theatre) date
back to 2008-2009, but only the stories and CQs have been published online,
not the solutions in OWL. Moreover, to further protect our dataset being used
in LLMs training data, we provide it in a zipped folder that is secured with a
password, ensuring controlled access and reducing the risk of data leakage for
future research in this field.
Additional Limitations Thisstudy’sscopeistoseetowhatextentLLMs
can serve in generating ontologies. There is a need for more evaluation criteria
to assess the utility and generalizability of generated ontologies. Our ontolo-
gies, drawn from different domains, are primarily single-module, limiting their
reusability across different systems. Moreover, our methods do not adequately
preventoreliminatesuperfluouselements,asshownbymodeloutputrepetitions.
OurMemorylessCQbyCQapproach,whichreducescontextsizetoenhanceper-
formance and reduce cost, is not suitable for history-dependent modelling tasks
thatheavilydependonthecommunicationhistorywithLLMs.Thistechniqueis
moreapplicabletomethodswhereeachpartoftheontologydevelopmentcanbe
performed independently in small parts and where there is an effective strategy
for merging these partial solutions by human-in-the-loop integration. Addition-
ally, further tests are needed to mitigate the potential leakage effect and bias in
LLMs. One way to achieve this is by applying the method to new use cases in
differentdomains.Futureworkwillinvolvemitigatingthelimitations,forexam-
ple, through manual re-engineering of the generated ontology draft. Potentially
the latter can be supported by user interfaces, e.g., in the form of a plugin.