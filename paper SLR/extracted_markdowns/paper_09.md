Guiding, Not Solving: Agentic Scaffolding for LLM
Programming Tutors
YuchenWang1,*, ChiraagSinghAnand1 and CheeWeiTan1,*
1NanyangTechnologicalUniversity,Singapore
Abstract
TherapidadvancementofLargeLanguageModels(LLMs)hasintroducedpowerfulcode-generationcapabilities
intoprogrammingeducation.Whilethesemodelscanactasreactivesolvers,deliveringdirectanswerstocomplex
problems,thisapproachoftendiminisheslearneragencyandbypassestheproductivestruggleessentialfor
computationalthinking. ThispaperpresentsSHARP(SocraticHintingforAI-ReinforcedProgramming),an
agentictutoringmoduledesignedtoorchestratehumanandAIagencyincompetitiveprogrammingcontexts.
Ratherthanrevealingsolutions,SHARPutilizesmilestone-drivenprogressestimationandknowledgetracingto
providecontext-aware,indirectscaffolding. WeimplementedSHARPwithinaweb-basedlearningplatform,
AskCodey,andevaluateditspedagogicalvaluethroughamixed-methodsapproach.Acontrolledsystemvalidation
experimentdemonstratesthatSHARPeffectivelybalancestasksuccesswithinteractionefficiency,outperforming
baselinepromptingstrategiesonmulti-bugdebuggingtasks.Furthermore,aformativein-the-wildpilotstudy
with42secondaryschoolstudentsrevealsthatlearnersvaluetheagency-preservingnatureofthescaffolding,
whilealsohighlightingtheneedfordynamicnegotiationofpacingwhencognitiveloadishigh.Ourfindings
offerdesignimplicationsfordevelopingAIteammatesthatprioritizelearnerautonomyoverautomatedtask
completion.
Keywords
Human-AIAgency,IntelligentTutoringSystems,SocraticScaffolding,CompetitiveProgramming,Knowledge
Tracing
1. Introduction
RecentbreakthroughsinLargeLanguageModels(LLMs)haverevealedremarkableabilitiesinalgorith-
micproblemsolvingandcodegeneration. Top-tiermodelsconsistentlymatchhuman-levelperformance
oncompetitiveprogrammingbenchmarks,asshownbytheircapacitytoindependentlytacklecomplex
tasksliketheAdventofCode[1,2,3]. Thiscreatesasignificantpedagogicaldilemmainprogramming
education: althoughthesepowerfulmodelsofferuniquepossibilitiesforpersonalizedassistance,their
defaultroleasimmediate“solvers”risksshort-circuitingtheverycognitiveprocessestheyareintended
tofoster. WhenanAIinstantlydeliversacompleteandcorrectsolution,itskipsoverthe“productive
struggle”thatisessentialforbuildingcomputationalthinkingandindependentproblem-solvingskills
[4,5].
ThistensionisatthecoreofcoordinatinghumanandAIagency(HAI-Agency)withineducational
technology. As the field moves beyond reactive tools toward proactive, agentic ecosystems, a key
challengearises: howcanwecreateAItutorsthataremoreautonomouswithoutundermininglearner
agency?
Totacklethischallenge,wepresentSHARP(SocraticHintingforAI-ReinforcedProgramming),an
agentic tutoring module crafted specifically to preserve and support learner agency in competitive
programmingeducation. Insteadofactingasadirectsolver,SHARPredefinestheAI’sroleasaproactive
teammate.Itdoesthisthroughamulti-modelarchitecturethatintegratesanadaptivehintschedulerwith
adynamicSocratichintgenerator. Bybreakingdowncomplexproblemsintopedagogicalmilestones
andusingknowledgetracingtoassessthestudent’smastery,SHARPdeliverscontext-aware,indirect
HAI-Agency:WorkshoponOrchestratingHumanandAIAgencyforProactiveandReflectiveLearning,co-locatedwiththe27th
InternationalConferenceonArtificialIntelligenceinEducation(AIED2026),Seoul,Korea,June27-July3,2026.
*Correspondingauthor.
$yuchen011@e.ntu.edu.sg(Y.Wang);chiraagsinghanand@gmail.com(C.S.Anand);cheewei.tan@ntu.edu.sg(C.W.Tan)
(cid:26)0000-0002-5183-1248(Y.Wang);0009-0009-9578-4277(C.S.Anand);0000-0002-6624-9752(C.W.Tan)
©2026Copyrightforthispaperbyitsauthors.UsepermittedunderCreativeCommonsLicenseAttribution4.0International(CCBY4.0).
CEUR
W Pr o o r c k e s e h d o in p gs ISSN c 1 e 6 u 1 r- 3 w -0 s 0 .o 7 r 3 g
published 2026-08-27

(1) Adaptive Hint Scheduler
database and cache
code execution API
(3) Student Status
triggering events
Q&A via UI
(2) Socratic Hint Generator
problem description Socratic Questioning (SQ)
milestones context
(PD) hint
Figure1: SystemArchitectureof SHARP.Theadaptivescheduler(blue)monitorsstudentstatustotrigger
interventions,whiletheSocraticgenerator(red)utilizesmilestonesandcontexttoproduceagency-preserving
hints.
hints. These prompts are designed to share the cognitive burden of problem decomposition while
intentionallyleavingtheimplementationeffort—andthustheagency—tothestudent.
Tovalidateourapproach,weintegratedSHARPintoAskCodey,aweb-basedassistantforcompetitive
programming. Weconductedamixed-methodsevaluation,includingacontrolledsystemvalidation
experimentalongsideaformativein-the-wildpilotstudyinvolving42secondaryschoolstudents. Our
resultsshowthatSHARPnotonlyboostsdebuggingsuccessratesoverbaselinemethodsbutisalso
viewedbystudentsasahelpfulscaffoldthatpreservestheirsenseofagency.
2. Related Work
2.1. IntelligentTutoringSystemsandHintGeneration
IntelligentTutoringSystems(ITS)haveprogressedfromtraditionalrule-basedframeworkstodeep
learningapproachesthatenablemoresophisticatedusermodeling[6]. Intherealmofprogramming
education, tools like PyTutor [7] have shown how LLMs can deliver personalized feedback tailored
to beginners’ needs. Automated hint generation remains a crucial feature of these systems. Recent
researchhighlightsthesignificanceofhintgranularity—whileorientationhintshelpguidelearners,
“bottom-out” hints that reveal the exact code can actually hinder the learning process [8]. SHARP
leveragesthesefindingsbyexplicitlyoptimizingforindirectness,sothathintssupportthelearner’s
reasoningwithoutgivingawaythesolutionoutright.
2.2. SocraticDialogueandLearnerAgency
Socraticquestioningencourageslearnerstouncoverconceptsontheirown,andresearchshowsthis
approach, when delivered through AI, leads to higher engagement and better learning outcomes
compared to traditional teaching methods [9, 10]. That said, open-ended programming tasks pose
distinct challenges for sustaining coherent, stateful conversations. At the same time, incorporating
LLMsintoprogrammingeducation[11]bringsupconcernsabout"shortcutlearning,"wherestudents
mightrelytooheavilyontheAI.Toaddressthis,SHARPstructuresdialoguearoundinferredmilestones,
aimingtostrikeabalancebetweentheAI’sproactiveguidanceandthestudent’sneedforindependent
discovery.

2.3. KnowledgeTracing
KnowledgeTracing(KT)aimstoestimatealearner’sknowledgestatebyanalyzingtheirinteraction
history. DeepKnowledgeTracing(DKT)[12]employsrecurrentneuralnetworkstomodelcomplex
temporalpatternsin thisdata. Morerecent approaches, suchas LLM-KT[13], align largelanguage
modelswithKTtasksthroughplug-and-playinstructiontechniques. SHARPbuildsonDKTbyinte-
gratingitintoitsSocratichintgenerator,enablingthesystemtoadjusttheexplicitnessofscaffolding
accordingtothestudent’spredictedmasteryofprerequisiteconcepts.
3. Methodology: The S Framework
HARP
3.1. ProblemFormulation
Givenaprogrammingproblem𝑃 withasetoftestcases𝑇𝐶,andastudent’scodesubmission𝑠 attime
𝑡
𝑡,ourgoalistogenerateahintℎ thatscaffoldsthestudent’slearningprocess. Thisprocessisframedby
𝑡
asequenceofpedagogicalmilestones𝑀 = {𝑚 ,...,𝑚 }. Let𝑚 betheestimatedcurrentmilestone
1 𝐾 𝑘*
achievedbythestudent. Theobjectiveistogenerateahintℎ thatguidesthestudenttowardthenext
𝑡
milestone,𝑚 .
𝑘*+1
Thecontextforhintgenerationatstep𝑡isdefinedas:
𝑐 = {𝑃,𝑇𝐶,𝑠 ,𝑚 ,𝑚 ,𝐻 }, (1)
𝑡 𝑡 𝑘* 𝑘*+1 :𝑡−1
where𝐻 isthehistoryofpreviouslygeneratedhints. Thehintgenerator𝒢 isastochasticpolicy
:𝑡−1
𝜋 (ℎ |𝑐 )parameterizedby𝜃. Aneffectivehintℎ mustsatisfycriteriaofvalidity,relevance(guiding
𝜃 𝑡 𝑡 𝑡
toward𝑚 withoutrevealingcode),andefficiency(avoidingrepetition).
𝑘*+1
3.2. SystemArchitecture
AsillustratedinFigure1,SHARPisamulti-modelframeworkconsistingofanadaptivehintscheduler
andadynamicSocratichintgenerator. Thescheduleroperateslocallytomonitorthestudent’sstate
andtriggerinterventions,whilethehintgeneratorleveragesacloud-basedLLMaugmentedwithlocal
context. Thishybridarchitecture,inspiredbytheCAMPframework[14],balancesthecomputational
powerofcloudmodelswiththelow-latency,context-awarebenefitsofalocalmodel.
3.3. AdaptiveHintScheduler
Theadaptivehintschedulerdetermineswhentoprovideahint. Itusesaprobabilisticmodeltotrigger
interventionsbasedonevidenceofstudentimpasse,balancingautomaticdetectionwithmanualstudent
requests. Animpasseisinferredifthetimeelapsedorthenumberofnon-productiveattemptssincethe
lastprogresseventexceedsadynamicthreshold.
Let𝐸 betheeventthatahintistriggeredattime𝑡. Theprobabilityofthiseventismodeledas:
𝑡
(︂ (︂time attempts )︂)︂
𝑃(𝐸 |state ) = 1−exp −𝜆· 𝑡 + 𝑡 , (2)
𝑡 𝑡 𝑇¯ 𝐴¯
𝑘* 𝑘*
wheretime andattempts arethetimeandnumberofattemptssincethelastmilestoneprogress,and
𝑡 𝑡
𝑇¯ and 𝐴¯ are the mean values for the current milestone 𝑚 derived from crowd-sourced data.
𝑘* 𝑘* 𝑘*
Therateparameter𝜆controlsthescheduler’ssensitivity. Thisprobabilisticapproachallowsformore
nuancedandlessintrusiveinterventionsthanfixed-thresholdrules.
3.4. SocraticHintGeneration
Whentriggered,theSocratichintgeneratorexecutesafour-stepprocess: (1)MilestoneDivision,(2)
MilestoneProgressEstimation,(3)ContextRetrieval,and(4)SocraticHintGeneration.

MilestoneDivision. Givenaproblem𝑃,weuseanLLMtodecomposeitintoasequenceofpeda-
gogicalmilestones𝑀 = {𝑚 ,...,𝑚 }. Eachmilestone𝑚 consistsofanaturallanguagedescription
|     | 1 𝐾 | 𝑘   |     |     |     |
| --- | --- | --- | --- | --- | --- |
ofasub-goal(𝑑 ),areferencecodesnippet(𝑟𝑠 ),andasetofspecifictestcases(𝑡𝑐 )thatvalidatethe
| 𝑘   |     | 𝑘   |     | 𝑘   |     |
| --- | --- | --- | --- | --- | --- |
achievementofthatsub-goal. Thisdecompositionisframedasaconstrainedoptimizationproblem:
∑︁ Cost(𝑚)
min
𝑀∈𝒞
𝑚∈𝑀
subjectto:
|     | ⋃︁  | Diversity(𝑀) |      |     |     |
| --- | --- | ------------ | ---- | --- | --- |
|     | 𝑚 = | 𝑈,           | ≥ 𝛿, |     |     |
𝑚∈𝑀
whereCost(𝑚)measuresthecognitivecomplexityofamilestone(e.g.,estimatedbyanLLMbasedon
thesub-problem’sdescription),andDiversity(𝑀)quantifiesthedistinctivenessamongmilestonesto
ensuremeaningfulprogression(e.g.,measuredbythesemanticdistancebetweenreferencesolutions).
AsthisisNP-hard,weusebeamsearchtofindaneffectiveapproximatesolution.
MilestoneProgressEstimation. Weestimatethestudent’scurrentmilestone𝑘* bycomparingtheir
solution𝑠 againstallreferencesolutionsin𝑀. Thisisformulatedasaclassificationproblemwhere
𝑡
wefindthemilestonethatmaximizesascoringfunction:
|     | (︂  |     | |passed(𝑠 | )︂  |     |
| --- | --- | --- | --------- | --- | --- |
,𝑡𝑐 )|
| 𝑘* = argmax | 𝑤 ·sim(𝜑(𝑠 | ),𝜑(𝑟𝑠 ))+𝑤 | ·   | 𝑡 𝑘 , | (3) |
| ----------- | ---------- | ----------- | --- | ----- | --- |
|             | 𝑠          | 𝑡 𝑘         | 𝑐   |       |     |
|             |            |             | |𝑡𝑐 | |     |     |
| 𝑘∈{1,..,𝐾}  |            |             | 𝑘   |       |     |
where𝜑(·)isacodeembeddingmodel(e.g.,CodeBERT),sim(·,·)iscosinesimilarity,andpassed(·,·)is
thesetofpassedtestcases. Theweights𝑤 and𝑤 arelearned. Theembeddingmodel𝜑isfine-tuned
𝑠 𝑐
usingatripletlossonadatasetofstudentsolutions,wherepositivepairsaresolutionsthatachievethe
samemilestoneandnegativepairsdonot.
Context Retrieval for Prompt Generation. After identifying the target milestone , we
𝑚 𝑘*+1
retrieve relevant context to construct a prompt for the hint-generating LLM. Following the RAG
approach[14],weretrieveinformationfromtheproblemdescription,thestudent’scode,andadatabase
ofcommonerrorsandsuccessfulsolutionpatterns. Theretrieverselectscontext𝑧 thatmaximizesthe
mutualinformationwiththetargetmilestone𝑚 ,ensuringthepromptishighlyrelevant.
𝑘*+1
Knowledge-TracedSocraticHinting. Tofurtherpersonalizethehints,weintegrateaKnowledge
Tracing(KT)component. WeuseaDeepKnowledgeTracing(DKT)model,specificallyanLSTM-based
network,tomaintainastudentknowledgestatevectorv R𝑁,where𝑁 isthenumberofknowledge
∈
𝑡
components(KCs)relevanttothecurriculum. TheDKTmodelupdatesthisvectorbasedonthestudent’s
performanceoneachmilestone:
|     |     | LSTM(v |     |     | (4) |
| --- | --- | ------ | --- | --- | --- |
|     | v = | ,x ;𝜃  | ),  |     |     |
|     | 𝑡   | 𝑡−1 𝑡  | 𝑑𝑘𝑡 |     |     |
where is an embedding of the student’s interaction with milestone (e.g., a one-hot vector
| x   |     |     | 𝑚   |     |     |
| --- | --- | --- | --- | --- | --- |
| 𝑡   |     |     |     | 𝑘*  |     |
indicatingthemilestoneandwhetheritwaspassed). TheoutputoftheDKTmodelisapredictionof
thestudent’sprobabilityofcorrectlyansweringfutureproblemsforeachKC.
Thisknowledgestatev isthenusedtoadaptthehintgenerationprocess. Specifically,theprompt
𝑡
forthehintgeneratorisaugmentedwithinformationaboutthestudent’sestimatedmasteryoftheKCs
requiredforthenextmilestone,𝑚 . Ourapproachisinspiredbythe‘plug-and-play‘instruction
𝑘*+1
mechanismproposedintheLLM-KTframework[13]. Thestudent’sknowledgestatevectorv ,derived
𝑡
fromtheDKTmodel,iseffectively’pluggedin’ascontextualinstructiontothepromptforourSocratic
hintgenerator,informingitofthestudent’sestimatedmasteryofprerequisiteconcepts. Thisallows
SHARP to move beyond reactive, in-the-moment feedback to a more proactive and pedagogically-
informedscaffoldingstrategy.

Figure2:UserinterfaceoftheAskCodeyplatformimplementingtheSHARPmodule.Thegeneratedhint(top
banner)suggestsaconceptualimprovementwithoutprovidingthedirectcodefix.
4. Implementation: AskCodey
Tovalidatethereal-worldapplicabilityofourframework,weimplementedtheSHARPmoduleasthe
core tutoring engine within AskCodey, a web-based competitive programming platform (Figure 2).
Thefront-endprovidesastandardcodingenvironmentwithintegratedtest-caseexecution,whilethe
SHARPmoduleoperatesasynchronouslytoprovidenon-blocking,banner-styleSocratichints.
Tosupportreproducibilityandcommunityengagement,thesourcecodeispubliclyavailable.1
ModelsandFrameworks. Forthecloud-basedSocratichintgenerator,weutilizethe‘gpt-4.1-mini‘
model. Thelocalcomponents,includingthemilestoneprogressestimator’sembeddingmodel,utilizea
fine-tuned‘CodeBERT-base‘[15]. TheDKTmodelisimplementedusingPyTorchwithasingle-layer
LSTM.TheentiresystemiscontainerizedusingDockerforportabilityandconsistentdeployment.
Crowd-SourcedDatabaseandCache. ThesystemreliesonaPostgreSQLdatabasestoringcrowd-
sourcedstudentmetrics—includingsolutiontimesandhintusage—todetectwhenlearnersarestuck
relative to peer performance. Problem milestones are pre-processed and cached via a CDN with a
three-hourrefreshcycle,ensuringlow-latencyaccesstofrequentlyqueriedmetadatawhilemaintaining
consistency.
CodeExecutionAPI. StudentsubmissionsareevaluatedusingPiston’ssandboxedcodeexecution,
supporting Python and C++ with TCR (test-case result) vector generation from runtime outputs,
including errors and debug prints. Piston was chosen for its scalability and optional Docker-based
self-hostingforhigherthroughput.
Feedback-DrivenOptimization. Thesystemiterativelyimprovesmilestoneclassificationandhint
generationbycollectingin-contextstudentfeedbackonaccuracyandusefulness. Thisdataperiodically
fine-tunes both the local milestone predictor and the cloud-based hint generator, closing the loop
betweenuserexperienceandmodelperformance.
1Sourcecode:https://github.com/Snail664/coding-tutor

Table1
ComparativePerformanceofSHARPvs.BaselineModelsAcrossVaryingBugComplexity
|           | Bugs Method        | SuccessRate |      | Turns/Bug | Indirectness | Relevance |
| --------- | ------------------ | ----------- | ---- | --------- | ------------ | --------- |
|           | NoGuidance         |             | 0.74 | NA        | NA           | NA        |
|           | BasicGuidance      |             | 0.88 | 3.20      | 1.0          | 4.86      |
|           | 1Bug TreeInstruct  |             | 0.84 | 1.42      | 1.0          | 4.78      |
|           | SHARP(w/oKT)       |             | 0.82 | 2.88      | 1.0          | 4.72      |
|           | SHARP(Full)        |             | 0.98 | 2.60      | 1.0          | 4.94      |
|           | NoGuidance         |             | 0.68 | NA        | NA           | NA        |
|           | BasicGuidance      |             | 0.82 | 2.55      | 1.0          | 4.68      |
|           | 2Bugs TreeInstruct |             | 0.72 | 1.57      | 1.0          | 4.32      |
|           | SHARP(w/oKT)       |             | 0.82 | 1.64      | 1.0          | 4.86      |
|           | SHARP(Full)        |             | 0.94 | 2.33      | 1.0          | 4.88      |
|           | NoGuidance         |             | 0.68 | NA        | NA           | NA        |
|           | BasicGuidance      |             | 0.66 | 2.19      | 1.0          | 4.68      |
|           | 3Bugs TreeInstruct |             | 0.72 | 1.04      | 1.0          | 4.80      |
|           | SHARP(w/oKT)       |             | 0.88 | 1.31      | 1.0          | 4.84      |
|           | SHARP(Full)        |             | 0.92 | 1.84      | 1.0          | 4.94      |
| 5. System | Validation         | Experiment  |      |           |              |           |
Toassessthetechnicalviabilityof SHARPandthecontributionofitsarchitecturalcomponents, we
conductedacontrolledbenchmarkexperiment. Thisexperimentservesasasystemvalidation,testing
whethertheframeworkbehavesasintendedwheninteractingwithasimulatednovice.
ExperimentalSetup. WeemployedanLLM(‘ministral-8b-2410‘)asaproxyforanoviceprogrammer,
selectedforitsmoderatebaselinecodingability. TheevaluationutilizedtheMULTI-DEBUGdataset
[16],comprising50programmingproblemswith1,2,or3injectedbugs. Wesimulatedamulti-turn
dialoguebetweenthe“student”modelandvarioustutoringconditionsuntilthebugswereresolvedora
turnlimitwasreached. WecomparedSHARP(Full)againstfourbaselines:No-Guidance,Basic-Guidance
(genericSocraticprompts),TreeInstruct[16],andanablationof SHARPwithouttheKnowledgeTracing
component.
Results. AsshowninTable1,SHARP(Full)consistentlyachievedthehighesttasksuccessrateacross
all bug complexity levels (98%, 94%, and 92%). The baseline consistently produced the
No Guidance
lowestsuccessrates,withperformancedecliningasbugcountincreased.
WhileTreeInstructrequiredfewerturnsperbug(e.g.,1.04inthe3-bugscenario),itsstatelessdesign
sacrificedoverallsuccess(72%). SHARPdemonstratedahighlyeffectivebalance,achievingsuperiortask
completionwithamoderateinteractionlength(1.84turns/bugfor3bugs). Theablationresultsconfirm
thatknowledgetracingcontributessignificantlytothesystem’sabilitytoguidetheproxymodelto
acorrectsolution. Allmodelsmaintainedperfectindirectness(1.0),confirmingtheyadheredtothe
constraintofnotrevealingdirectcode.
To understand the underlying reasons for this performance difference, we analyzed the dialogue
quality. TheTreeInstruct model’sstatelessdesigncanleadtoanunnaturalconversationflowwhere
correctstudentanswersarenotacknowledged. Incontrast,SHARP’sstateful,acknowledgment-driven
approachavoidssuchloopsandmaintainsamoreproductiveproblem-solvingflow.
As illustrated in Table 2, the difference in conversational flow is stark: while TreeInstruct moves
directlytothenextquestionwithoutacknowledgingcorrectanswers,SHARPprovidespositivefeedback
andbuildsuponthestudent’sobservationstoguidetheactualcodefix.
WealsoconductedanerroranalysisonthefailurecasesforthefullSHARPmodel. Themajorityof
failures(approx. 65%)occurredonproblemsrequiringcomplexalgorithmicshifts(e.g.,movingfrom

Figure3:Successratesandinteractionefficiencyofdifferentmodelson3-bugproblems.SHARP(Full)achieves
thehighestsuccessratewithamoderateandefficientnumberofinteractionturns.
abrute-forcetoadynamicprogrammingapproach),suggestingalimitationofthecurrentmilestone
representationandakeyareaforfuturework.
6. Formative In-the-Wild Pilot Study
To understand how learners negotiate agency with the SHARP system in a real-world setting, we
conductedaformativepilotstudywith42secondaryschoolstudents(ages15-17)usingtheAskCodey
platform.
ProcedureandDataCollection. ParticipantswereaskedtosolvetwoproblemsfromtheMULTI-
DEBUGdataset(onewith2bugs,onewith3)usingtheAskCodeyplatformovera90-minutesession.
Wecollecteddatafrommultiplesources: (1)systemlogs,includingtaskcompletiontimeandhintusage;
(2)apre-andpost-sessionsurveymeasuringself-reporteddebuggingconfidenceona7-pointLikert
scale;and(3)a15-minutesemi-structuredinterviewafterthesessiontoelicitqualitativefeedbackon
theirexperiencewiththeAIteammate.
QuantitativeFindings. Thepilotconfirmedthesystem’seffectivenessinareal-worldsetting. The
taskcompletionratewas78%,andweobservedasignificantincreaseinstudents’self-reporteddebugging
confidencefrompre-session(M=4.2,SD=1.1)topost-session(M=5.8,SD=0.9),𝑡(41) = 7.5,𝑝 < .001.
Hint utilization was positively correlated with success rates (Pearson’s 𝑟 = 0.72), suggesting that
studentswhoengagedwiththehintsfoundthemproductive.
QualitativeFindings. Weconductedathematicanalysisoftheinterviewtranscripts,whichrevealed
threemainthemesregardinghuman-AIorchestration:
• Valued Scaffolding without Spoilers: Students heavily appreciated the agency-preserving
natureoftheSocraticapproach.Oneparticipantnoted,"ItfeltlikeitwasaskingmethequestionsI
shouldhavebeenaskingmyself,whichiswaybetterthanjustgettingthesolution."Thisconfirms
thatstudentsrecognizeandvaluethepedagogicalintentofproductivestruggle.
• MilestoneTransparency:Themilestone-basedstructureprovidedasenseoforientation."Seeing
themilestonesmademefeellikeIwasmakingprogress,evenwhenIwasstuckononepart,"
indicatingthatexposingtheAI’sinternalprogressestimationhelpsmaintainlearnermotivation.

Table2
ComparativeDialogueAnalysis:TreeInstruct’sLinearQuestioningvs.SHARP’sStatefulDebugging
| TreeInstruct(Stateless) |      |             |           |           | SHARP(Stateful) |         |            |       |         |
| ----------------------- | ---- | ----------- | --------- | --------- | --------------- | ------- | ---------- | ----- | ------- |
|                         | What | type should |           | be if you |                 | What do | you notice | about | the way |
| Tutor:                  |      |             | nodes_sum |           | Tutor:          |         |            |       |         |
wanttoperformarithmeticoperationslikeaddi- nodes_sum isinitializedandhowitisthenused
| tionwithit? |           |                         |     |     | withintheloopforarithmeticoperations? |             |           |                 |     |
| ----------- | --------- | ----------------------- | --- | --- | ------------------------------------- | ----------- | --------- | --------------- | --- |
|             |           | shouldbeanintegertypeto |     |     |                                       | Inoticethat |           | isinitializedas |     |
| Student:    | nodes_sum |                         |     |     | Student:                              |             | nodes_sum |                 |     |
performarithmeticoperationslikeadditionwith ,whichmeansitwillraiseanerrorwhentry-
None
| it. |     |     |     |     | ingtoperformarithmeticoperationsonit. |     |     |     | Addi- |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----- |
Tutor: When you want to extract just the single tionally, the line l2 - l2.next is incorrect; it
| digitforthecurrentnodeinasum,whichoperator |     |     |     |     | shouldbe |     | .   |     |     |
| ------------------------------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
l2 = l2.next
wouldyouusetogettheremainderafterdividing Greatobservations!Now,canyoushowhow
Tutor:
| by10? |     |     |     |     | youwouldfixthebugrelatedto |     |     |     | ini- |
| ----- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ---- |
nodes_sum
tialization,aswellascorrectthemistakeonthe
l2
updateline(justtherelevantlinesofcode)?
| •   |     |     |     | Anotablesubsetofstudents(approx. |     |     | 15%)expressedfrustra- |     |     |
| --- | --- | --- | --- | -------------------------------- | --- | --- | --------------------- | --- | --- |
TheDesireforAdaptivePacing:
tionwhenencounteringsevereconceptualroadblocks. Inthesemomentsofhighcognitiveload,
thestrictadherencetoindirecthintsfeltrestrictive. "SometimesIjustneedalittlepush,nota
wholeconversation,"onestudentremarked.
| 7. Discussion |     | and | Future | Work |     |     |     |     |     |
| ------------- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- |
The findings from our system validation and pilot study offer several design implications for the
development of agentic AI in educational contexts, directly addressing the core themes of the HAI-
Agencyworkshop.
Our implementation of SHARP in AskCodey shows that AI can successfully shift from being a
reactiveproblemsolvertoaproactivescaffold. Bycoordinatinginterventionswithmilestone-based
progressestimates,theAIfunctionsasacollaborativepartner,sharingthecognitiveburdenofproblem
decompositionwhileallowingthestudenttohandletheactualimplementation. Thefavorableresponse
to“scaffoldingwithoutspoilers”supportstheapproachofdesigningAIsystemsthatemphasizelong-
termskilldevelopmentratherthanjustquicktaskcompletion.
Thefrustrationsomestudentsexpresshighlightsthatmaintaininglearneragencycannotbeachieved
through a strict pedagogical approach alone. When a student is genuinely stuck, an AI that is too
indirectmaycomeacrossasmoreofanobstaclethanacollaborator. GenuineHAI-Agencydemands
mechanismsfordynamicnegotiation.
Whileourresultsarepromising,weacknowledgeseverallimitationsthatprovidecleardirections
for future research. First, as our error analysis revealed, SHARP’s current milestone representation
strugglestoscaffoldhigh-levelconceptualshifts,suchasmovingfromabrute-forcetoamoreefficient
algorithmicparadigm. Thesystemiseffectiveatguidinglocalcodefixesbutlesssoatfosteringdeep
structuralchanges. Second,ourstudentproxymodelcannotfullycapturethediversityofrealstudent
misconceptions,learningstyles,andaffectivestates.
Buildingontheselimitations,weproposetwokeydirectionsforfuturework:
HierarchicalMilestoneRepresentation. Toaddressthechallengeofscaffoldinghigh-levelconcep-
tualchanges,weplantodevelopahierarchicalmilestonemodel. Thiswouldinvolvecreatinghigh-level
“conceptualmilestones”(e.g.,“Identifytheneedfordynamicprogramming”)thatsitabovethecurrent
implementation-focusedmilestones. ThetutorcouldthenprovideSocraticguidanceattheconceptual
levelbeforedrillingdowntotheimplementationdetails.

AdaptiveHintGranularityandPacing. Futureversionsofagentictutoringsystemsshouldinclude
adaptivepacingcontrols,allowinglearnerstoexplicitlyadjustthelevelofAIassistancethroughinterface
options (for example, a “Make it more direct” button). By granting students this meta-agency over
theAI’sbehavior,thesystemcanbetterrespondtovaryingaffectivestates,ensuringthatproductive
struggledoesnotspiralintounproductivefrustration.
8. Conclusion
In this paper, we introduced SHARP, a Socratic tutoring system that leverages a novel milestone-
drivenapproach,enhancedwithknowledgetracing,toprovidepersonalizedguidanceinprogramming
education. Ourworkaddressesacriticaltensionintheageofpowerfulcode-generatingLLMs: howto
providesupportthatscaffoldslearningwithoutunderminingthedevelopmentofrobustproblem-solving
skills. Throughamixed-methodsevaluation,wedemonstratedthatSHARPsignificantlyoutperforms
baselinemodelsintasksuccessbyprovidingstateful,context-awareguidance. Furthermore,ourin-the-
wildpilotstudyconfirmedthatstudentsfindtheSocratic,milestone-basedapproachtobetransparent,
motivating,andeffectiveatfosteringunderstanding. Bybalancingautomatedsupportwithpedagogical
principles,SHARPoffersapromisingmodelfordesigningthenextgenerationofAI-poweredlearning
toolsthataimnotjusttoprovideanswers,buttocultivateindependent,capablelearners.
Acknowledgments
ThisresearchissupportedbytheSingaporeMinistryofEducationAcademicResearchFund(MOE-
T2EP20224-0009)andNTUstartupfund.
Declaration on Generative AI
Theauthor(s)usedgenerativeAItools(ChatGPT,Grammarly)forgrammarcheckingandlanguage
polishingofthemanuscript.
References
[1] P.Norvig,Adventofcode2025withai,GitHubJupyterNotebook,2025.URL:https://github.com/
norvig/pytudes/blob/main/ipynb/Advent-2025-AI.ipynb,accessed: 2025-01-22.
[2] Y.Li,D.Choi,J.Chung,N.Kushman,J.Schrittwieser,R.Leblond,T.Eccles,J.Keeling,F.Gimeno,
A.DalLago,etal., Competition-levelcodegenerationwithalphacode, Science378(2022)1092–
1097.
[3] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda,
N.Joseph,G.Brockman,etal., Evaluatinglargelanguagemodelstrainedoncode, arXivpreprint
arXiv:2107.03374(2021).
[4] G.Jošt,V.Taneski,S.Karakatič, Theimpactoflargelanguagemodelsonprogrammingeducation
andstudentlearningoutcomes, AppliedSciences14(2024)4115.
[5] G. Pitts, A. P. Hridi, A. B. L. Narayanan, A survey of llm-based applications in programming
education: Balancingautomationandhumanoversight, in: ProceedingsoftheFourthWorkshop
onHuman-CenteredComputationalLinguistics,ACL,2025.
[6] J.Paladines,J.Ramirez, Asystematicliteraturereviewofintelligenttutoringsystemswithdialogue
innaturallanguage, IEEEAccess8(2020)164246–164267.
[7] A.C.-M.Yang,J.-Y.Lin,C.-Y.Lin,H.Ogata, Enhancingpythonlearningwithpytutor: Efficacyofa
chatgpt-basedintelligenttutoringsysteminprogrammingeducation, ComputersandEducation:
ArtificialIntelligence7(2024)100309.

[8] R. Xiao, et al., Exploring how multiple levels of gpt-generated programming hints support or
disappointnovices,in:ExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputing
Systems,ACM,2024.
[9] G.Kestin,etal., Aitutoringoutperformsin-classactivelearning, ScientificReports15(2025).
[10] L.Xi,Y.Zhang,Q.Wang, Investigatingtheeffectsofanllm-basedsocraticconversationalagent
onstudents’academicperformanceandreflectivethinkinginhighereducation, Computers&
Education(2025).
[11] R.Liu,C.Zenke,C.Liu,A.Holmes,P.Thornton,D.J.Malan, Teachingcs50withai: Leveraging
generativeartificialintelligenceincomputerscienceeducation, in: Proceedingsofthe55thACM
TechnicalSymposiumonComputerScienceEducation,ACM,2024,pp.750–756.
[12] C.Piech,J.Bassen,J.Huang,S.Ganguli,M.Sahami,L.J.Guibas,J.Sohl-Dickstein, Deepknowledge
tracing, in: AdvancesinNeuralInformationProcessingSystems,volume28,CurranAssociates,
Inc.,2015.
[13] Y.Zhang,etal., Llm-kt: Aligninglargelanguagemodelswithknowledgetracing, arXivpreprint
arXiv:2502.02945(2025).
[14] Y.Wang,S.Guo,C.W.Tan, Contextualaugmentedmulti-modelprogramming(camp): Alocal-
cloudcopilotsolution, in: 2025IEEEConferenceonArtificialIntelligence(CAI),IEEE,2025,pp.
675–681.
[15] Z.Feng,D.Guo,D.Tang,N.Duan,X.Feng,M.Gong,L.Shou,B.Qin,T.Liu,D.Jiang,M.Zhou,
Codebert: Apre-trainedmodelforprogrammingandnaturallanguages, in: FindingsoftheAsso-
ciationforComputationalLinguistics: EMNLP2020,AssociationforComputationalLinguistics,
2020,pp.1536–1547.doi: .
10.18653/v1/2020.findings-emnlp.139
[16] P.Kargupta,I.Agarwal,D.Hakkani-Tur,J.Han, Instruct,notassist:Llm-basedmulti-turnplanning
andhierarchicalquestioningforSocraticcodedebugging, arXivpreprintarXiv:2406.11709(2024).
URL:https://arxiv.org/abs/2406.11709v4.