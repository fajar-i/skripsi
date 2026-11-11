Leveraging LLM and Multiscale Knowledge States to Improve
Knowledge Tracing in Programming Tasks
MingxingShao TianchengZhang∗ YifangYin
2301935@stu.neu.edu.cn tczhang@mail.neu.edu.cn yin_yifang@a-star.edu.sg
SchoolofComputerScienceand SchoolofComputerScienceand InstituteforInfocommResearch,
Engineering,NortheasternUniversity Engineering,NortheasternUniversity A*STAR
Shenyang,110819,China Shenyang,110819,China Singapore
WenhuiWu ZikaiLi MingheYu
wuwh3@mails.neu.edu.cn 2301903@stu.neu.edu.cn yuminghe@mail.neu.edu.cn
SchoolofComputerScienceand SchoolofComputerScienceand CollegeofSoftware,Northeastern
Engineering,NortheasternUniversity Engineering,NortheasternUniversity University
Shenyang,110819,China Shenyang,110819,China Shenyang,110819,China
FanglingLeng GeYu
lengfangling@mail.neu.edu.cn yuge@mail.neu.edu.cn
SchoolofComputerScienceand SchoolofComputerScienceand
Engineering,NortheasternUniversity Engineering,NortheasternUniversity
Shenyang,110819,China Shenyang,110819,China
Abstract phases of learning, forgetting/reinforcement, and applica-
KnowledgeTracing(KT)isacoretaskinintelligenttutoringsys- tion.Extensiveexperimentsonthreedatasetsdemonstratethat
tems,designedtomodelthedynamicevolutionofstudents’knowl- MIE+MLPKTconsistentlyoutperforms18baselinemethods.Our
edgestatesbypredictingtheirperformanceonspecificproblems. codeisavailableat:https://anonymous.4open.science/r/MIE-MLPKT-
However,existingKTmodels,primarilydevelopedfortraditional D654.
subjectdomains,exhibitpoorgeneralizationtoprogrammingtasks
duetoseveraldistinctchallenges.First,studentresponsesinpro- CCSConcepts
gramming tasks are characterized by high uncertainty. Second, •Socialandprofessionaltopics→Studentassessment;•Com-
programmingtaskstypicallyprovidecontinuousscoresbasedon putingmethodologies→Neuralnetworks;•Informationsys-
theproportionofpassedtestcases,incontrasttothebinarycor- tems→Datamining.
rectnessassumedbytraditionalKTmodels,withthesetest-case-
based scores often being noisy. Third, most KT models rely ex- Keywords
clusivelyontheunderstandingofknowledgeconceptsforperfor-
Programmingknowledgetracing,dataminingenhancedbyllm,
manceprediction,whereassuccessinprogrammingtasksisheav-
knowledgestaterepresentation
ilycontingentuponlogicalreasoningandproblem-specificcom-
prehension.Toaddresstheseissues,weproposeanLLM-driven ACMReferenceFormat:
InteractionEnrichmentFramework(MIE)tomitigatehighun- MingxingShao,TianchengZhang,YifangYin,WenhuiWu,ZikaiLi,Minghe
certaintyandproblematiclabeling,andintroducetheMulti-Level Yu,FanglingLeng,andGeYu.2026.LeveragingLLMandMultiscaleKnowl-
ProgrammingKnowledgeTracing(MLPKT)modeltocapture edge States to Improve Knowledge Tracing in Programming Tasks. In
students’knowledgestatesacrossmultipledimensions.MLPKT Proceedings of the ACM Web Conference 2026 (WWW ’26), April 13–17,
conductsmulti-layeranalysisofstudentsubmissionstoidentify 2026,Dubai,UnitedArabEmirates.ACM,NewYork,NY,USA,12pages.
https://doi.org/10.1145/3774904.3792525
therootcausesoferrorsandassignsemanticallymeaningfulfine-
grainedlabels.Additionally,weproposeathree-level,three-phase
KTarchitecturethatcapturesknowledgedynamicsacrossthree 1 Introduction
dimensions—problems,concepts,andlogicalskills—throughthe
Withtherapiddevelopmentofthecomputerscienceindustry,on-
lineprogrammingeducationplatformsinmajoruniversitieshave
∗Correspondingauthor.
proliferated,accumulatingvastamountsofeducationalrecords.In
onlinejudge(OJ)platforms,trackingstudents’knowledgestatesto
recommendappropriatelearningmaterialsiscrucialforenhancing
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. learningefficiency.Althoughvariousknowledgetracing(KT)meth-
WWW’26,Dubai,UnitedArabEmirates odshavebeenproposedtomonitorstudents’knowledgestates,
©2026Copyrightheldbytheowner/author(s).
thesemethodsareprimarilydesignedforsubject-specificknowl-
ACMISBN979-8-4007-2307-0/2026/04
https://doi.org/10.1145/3774904.3792525 edgetracingtasks,suchasmathematicsandEnglish.Asillustrated
7378

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
inFigure1,comparedtosubject-specificknowledgetracingtasks, exceedingthethreshold,along-intervalforgettingmodulesimu-
programmingtaskdataexhibitsthefollowingcharacteristics: latestheforgettingprocess.
(1)Highuncertainty:Ateachtimestep,studentssubmitcode Applicationphase:Syntax,logic,andproblem-specificabilities
ratherthansimpleselections,leadingtogreaterinteractionuncer- relatedtothecurrentproblemareinputintoamulti-levelstudent
tainty.Forinstance,intimestep3ofFigure1,astudentnearly abilityapplicationmoduletopredictthestudent’sscore.Toenhance
completestheprogramcorrectlybutfailsduetoanoversightin modelinterpretability,wedesignamulti-levelabilityintegration
omittingasemicolon(’;’)after“returna+b”.TraditionalKTmodels modulethatmakesitapplicabletothe2-parameteritemresponse
struggletodistinguisherrorscausedbyinsufficientabilityfrom theory(IRT)[28].
thoseduetocarelessness. Overall,ourcontributionsareasfollows:
(2)Continuouslabels:Inprogrammingtasks,scorelabelsare • Motivation:Weoutlinethedifferencesbetweentraditional
continuousratherthanbinary.Scoresarecalculatedbasedonthe
subject-specificknowledgetracingtasksandprogramming
proportionoftestcasespassedbythestudent’ssubmittedcodeand
tracingtasks,identifythekeychallenges,andexplainwhy
theirweights.However,currentscoringmethodshavelimitations:
existingKTmodelsstruggleinprogramminglearningtasks.
theyrequiremeticulouslydesignedbackendtestcasesandcannot • Method:WeproposeanLLM-DrivenInteractionEnrich-
reasonablyevaluatecodethatfailstocompile.
mentFramework(MIE)totacklehighuncertaintyandun-
(3)Compositeabilities:Assessingstudents’knowledgestates
reasonablelabelingproblems,andfurtherintroduceMLPKT
involves not only evaluating the correctness of code syntax or
(Multi-LevelProgrammingKnowledgeTracing)tomodel
masteryofspecificconceptsbutalsoconsideringstudents’ability
students’knowledgestatesacrossmultiplelevels.MLPKT
tointegratetheseelements.Furthermore,whenstudentsrepeat-
conductsmulti-layeranalysisofstudentsubmissionstoiden-
edlyattemptthesameproblem,theirunderstandingshoulddeepen
tifyrootcausesoferrorsandassignsemanticallymeaningful
progressively.
fine-grainedlabels,whileintroducingathree-level,three-
ThesecharacteristicsrendertraditionalKTmodelsineffective
phaseknowledgetracingapproachthatcapturesknowledge
forprogrammingtasks.
dynamicsacrossproblems,concepts,andlogicalskills.
Toaddressthesechallenges,weproposeanovelprogramming • Experiments:Throughcomparisonswith18baselinemod-
knowledgetracingmodelenhancedbyLLMs.First,totacklethe
elsacross3datasets,wedemonstrateMLPKT’sapplicability
highuncertaintyandcontinuouslabelsinprogrammingtaskdata,
in programming tasks and validate its ability to produce
wedesignanLLM-DrivenInteractionEnrichmentFramework
accurateknowledgetracingresults.
(MIE)thatperformsreasonablescoreevaluationanddomain-specific • Datasets:Wealsoreleaseallannotatedprogrammingdatasets
erroranalysis.Inreasonablescoreevaluation,weestablishscoring
toassistfutureresearch.
criteriaandpromptstoevaluatestudentsubmissions,servingas
newinteractionlabels.Indomain-specificerroranalysis,weem- 2 RelatedWork
ploycauseanalysispromptswheretheLLMidentifieserrorcauses
2.1 KnowledgeTracing
atdifferentlevels,suchascarelesssyntaxerrorsorlogicalerrors.
Theerrorclassificationhierarchycanbeadaptedinpracticalappli- SinceJohnR.Andersonproposedtheconceptofknowledgetrac-
cationsbasedonthetargetaudience.Sincethispaperisoriented ing(KT)[7],KTresearchcanberoughlydividedintotwophases.
towardnoviceprogrammers,wecategorizeerrorsintotwodistinct The first phase centers on Bayesian Knowledge Tracing (BKT),
levels:thesyntacticconceptlevelandthelogicalabilitylevel. whichisbasedonBayesianprobabilityformulasandenhancesBKT
Toaddressthecompositeabilitiesinprogrammingtasks,we byincorporatingadditionalinformation[7,20,21,34].Although
proposeathree-level,three-phaseknowledgetracingframework thesemethodsofferacertaindegreeofinterpretability,theirperfor-
inspiredbyLPKTandGRKT[8,23].Thisframeworkintegrates manceisoftenlimited.Inthesecondphase,researchersbeganto
LLM-extractedscoresanderrorcausestoaccuratelymodelstudents’ adoptdeeplearning-basedKTmethods,utilizingrecurrentneural
knowledgestatesfromtheirlearningprocesses.Wedividethelearn- networks(RNNs)[18,22,31]andself-attentionnetworks[27]to
ingprocessintothreephases:learning,forgetting/enhancement, trackstudents’knowledgestates[9,12,15,16,19].Deeplearning
andapplication,whiletracingabilitiesacrossthreelevels:syntax, knowledgetracing(DLKT)methodstypicallyachievesuperiorre-
logic,andproblem-specific. sults;however,duetotheinherentblack-boxnatureofdeepneural
Learningphase:Thestudent’ssubmittedproblem,relatedcon- networks,thesemethodsoftenlackinterpretabilityintheirout-
cepts,andscoresareinputintoamulti-levelabilitycomputation comes.Toenhanceinterpretability,somescholarshaveattemptedto
moduletocalculatechangesinstudents’abilitiesatlogic,syntax, modelknowledgestatesfromtheperspectiveofstudents’learning
andproblem-specificlevels.Forproblem-specificabilitychanges, processes[8,23,30],therebydevelopingapproachesthatbalance
wedesignanexponentialenhancementfunctiontomodelthegrad- interpretabilityandaccuracy.
ualdeepeningofunderstandingduringrepeatedattempts.Basedon Nevertheless,theaforementionedmethodsprimarilytargetknowl-
LLM-extractedsyntaxandlogicerrorsorcorrectness,wedetermine edgetracingtasksinspecificdisciplines,suchasmathematicsand
thedirectionofchangesinlogicandsyntaxabilities. English,whichemphasizeconceptmastery.Incontrast,duringthe
Forgetting/enhancementphase:Thisphasedynamicallyse- programminglearningprocess,studentssubmitcoderatherthan
lectsenhancementorforgettingbasedoninteractionintervals.For simplemultiple-choiceortrue/falseanswers;OnlineJudge(OJ)plat-
interactionswithintervalsbelowathreshold,ashort-intervalen- formstypicallyhaveaccesstostudents’codesubmissions,which
hancementmodulesimulatesthelearningprocess;forintervals hold significant value for assessing students’ knowledge states.
7379

Multi-LevelProgrammingKnowledgeTracingEnhancedbyLLM WWW’26,April13–17,2026,Dubai,UnitedArabEmirates
Figure1:DifferencesBetweenProgrammingKTTasksandSubject-SpecificKTTasks:HighUncertainty;ContinuousLabels;
andDiversityinAbilityRequirements.
Moreover,scoresinprogrammingtasksarenotsimplybinaryval- Althoughtheaforementionedmethodsapplyknowledgetracing
ues.ThesecharacteristicsindicatethattraditionalKTmethodsstill (KT)modelstoprogrammingtasks,theyoftenfocusexclusivelyon
havesubstantialroomforimprovementwhenappliedtoprogram- superficialcodefeatures,lackingfine-grainedmodelingofdeeper
minglearningtasks. attributessuchascodequalityanderrorpatterns.Additionally,the
datasetsemployedtypicallyutilizecoarse-grainedlabeling,which
2.2 ProgrammingKnowledgeTracing limitstheprecisionofknowledgestateassessments.
Researchonknowledgetracing(KT)forprogrammingtasksre-
3 ProblemFormulation
mainslimited.Earlystudiesemployedstatisticalanalysisofstudent
errorsandcommonstructures,subsequentlyapplyingtheBayesian Let Q denote the set of problems, L the original set of scores,
knowledgetracingalgorithm[6]tostructureddatatomodelthe C thesetofconcepts,andM thesetofcodessubmittedbystu-
learningprocessandestimatethefinalprogrammingknowledge dents.WefirstdesignpromptsusingthesetofproblemsQandthe
level.Wangetal.[26]inputembeddedprogramsubmissionsintoa setofstudents’codesM toenabletheLLMtoderivethesetof
recurrentneuralnetworkandtrainedittopredictstudents’success codelabelsLˆandthecorrespondingsetofreasonsR.Forstudent
orfailureinsubsequentprogrammingexercises.Buildingonthis, 𝑆 𝑖 ∈ S,theinteractiontuplespriortotimestep𝑡 aredenotedas
Code-DKT[24]utilizesthecode2vecmodel[2]tolearnmeaningful 𝐼 𝑡 = {(𝑞 1 ,𝑐 1 ,𝑙ˆ 1 ,𝑟 1 ),...,(𝑞 𝑡−1 ,𝑐 𝑡−1 ,𝑙ˆ 𝑡−1 ,𝑟 𝑡−1 )},where𝑞 ∈ Q repre-
representationsofstudentcode,thencombinesitwithdeepknowl- sentstheproblemidentifier,𝑐 ∈Crepresentsthemultipleconcept
edgetracingtotrackstudents’knowledgestates.Swamyetal.[25] identifiersassociatedwiththeproblem,𝑙ˆ∈Lˆrepresentsthestu-
computeTF-IDFscoresforeachstringtokeninthesourcecode dent’scodescoregradedbyLLM,and𝑟 ∈Rrepresentsthestudent’s
andusethesescorestoformrepresentationvectorsofthecode, errorcauses.Ourobjectiveistomodelthestudent’sknowledge
whichareconcatenatedwithotherauxiliaryfeaturesasinputtoan state𝑠
𝑡
𝑖
−1
basedontheinteractiontuples𝐼
𝑡−1
priortotimestep𝑡,
RNN.Zhuetal.[36]representstudentcodeparsedintosyntaxtrees andfurtherpredictthestudent’sscoreonproblem𝑞
𝑡
attimestep𝑡,
throughanattentionmechanismandcombineitwithDKTtotrack formulatedas𝑙 𝑡 =𝑓(𝑞 𝑡 ,𝑐 𝑡 |𝐼 𝑡−1 ).
students’knowledgestates.OKT[17]introducesacodegenera-
tionmethodthatcombineslanguagemodelsforprogramsynthesis 4 TheMIEFramework
withstudentknowledgetracing,enablingpredictionofstudents’
AsillustratedinFigure2,wedesignanLLM-DrivenInteraction
responsesinprogrammingtasksandpioneeringtheconceptof
EnrichmentFrameworktoprovidereasonablescorelabelsandcode
open-endedknowledgetracing.Wuetal.[29]proposeahetero-
analysisresultsforthethree-levelknowledgetracingframework.
geneous graph-based programming knowledge tracing method,
constructingaheterogeneousgraphofknowledgeconcepts,pro-
4.1 RationalScoreEvaluation
grammingproblems,andstudentcode,utilizinggraphstructure
learningandattentionmechanismstoenhancerepresentationsand Toadaptthelabelsinprogrammingdatasetsforknowledgetracing
evaluatemasterylevelsofknowledgeconcepts. models,forthecode𝑚𝑖 𝑡 ∈Msubmittedbystudent𝑆 𝑖attimestep𝑡,
7380

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
|     |     |     |     |     |     | resulting |     | in a score                                       | below | 50, it | is identified | as  | a logical | error, |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------------------------ | ----- | ------ | ------------- | --- | --------- | ------ |
|     |     |     |     |     |     | yielding𝑅 |     | 𝑖 = [0,1,0,0,1].Inanotherexample,iferrorsoccurin |       |        |               |     |           |        |
𝑡
𝑅 𝑖
|     |     |     |     |     |     | both | logical | and syntactic |     | aspects, | the | returned | vector | is 𝑡 = |
| --- | --- | --- | --- | --- | --- | ---- | ------- | ------------- | --- | -------- | --- | -------- | ------ | ------ |
[0,0,0,1,1].
Theaforementionedprocesscanbeformallyexpressedas:
|     |     |     |     |     |     | 𝑅 𝑖 =LLM(𝑃𝑟(Data(𝑚𝑖 |     |     | |𝑚ˆ | 𝑖 |𝑃𝐷 | 𝑖 |𝑙ˆ 𝑖) |Rules|Desc|Notes)).∀𝑆 |     |     | ∈S, |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ----- | ------------------------------- | --- | --- | --- |
|     |     |     |     |     |     | 𝑡                   |     |     | 𝑡   | 𝑡     | 𝑡 𝑡                             |     |     | 𝑖   |
(2)
|     |     |     |     |     |     | Where𝑅 | 𝑖   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡 ∈R.Thus,weobtainthecollectionofcodeanalysesRas
mentionedearlier.Thecompletecodescoringpromptandreason
analysispromptcanbefoundintheAppendixA.
|     |     |     |     |     |     | 5   | TheMLPKTFramework |           |     |       |         |           |          |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --------- | --- | ----- | ------- | --------- | -------- | --- |
|     |     |     |     |     |     | As  | illustrated       | in Figure | 3,  | MLPKT | employs | recursive | modeling |     |
throughoutathree-phaseprocess,comprisingthelearningphase,
enhancement/forgettingphase,andapplicationphase.Itisworth
notingthatthegenerationprocessofembeddingsrequiredbythe
Figure2:LLM-DrivenInteractionEnrichmentFramework: modelisdetailedinAppendixB.Foreaseofunderstanding,the
Featuring Rational Score Evaluation and Domain Causal notations mentioned in Appendix B and their meanings are as
showninTable1.
Analysis,withLLM-GeneratedInteractionsUltimatelyFed
intotheMLPKTFramework
Table1:NotationsandtheirmeaningsintheMLPKTmodel.
| withcorrespondingID𝑚ˆ𝑖 |     | andproblemdescription𝑃𝐷 |     | 𝑖,wedesign |     |          |     |             |     |     |     |     |     |     |
| ---------------------- | --- | ----------------------- | --- | ---------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|                        |     | 𝑡                       |     | 𝑡          |     | Notation |     | Description |     |     |     |     |     |     |
ascoringpromptdenotedas𝑃stoobtainthecodescoreatthistime H𝑡 Student’slogicalabilityvectorattime𝑡(∈R𝑑)
𝐿
step.AsshowninFigure2(a),itmainlyincludestheinherentdata H 𝑡 Student’sconceptualabilityvectorattime𝑡(∈R𝑑)
𝐶
inthedataset(Data),namelythestudent’scode𝑚𝑖 alongwithits H𝑡 Student’sproblem-solvingabilityvectorattime𝑡(∈R𝑑)
|     |     |     |     | 𝑡   |     |     | 𝑃   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑚 𝑖 𝑃 𝐷 𝑖 Q C Q u e s ti o n- c o n c e p t w ei g h t e d e m be d d in g f o rp r o blem𝑞 𝑡 (∈R𝑑)
| co r re sp o n | d in g I D | ˆ 𝑡 a n d t h e p r o b l e m | s t e m 𝑡 | ,s c o r i n | g cr i t e r ia |     | 𝑞𝑡  |          |               |            |                  |                  |       |     |
| -------------- | ---------- | ----------------------------- | --------- | ------------ | --------------- | --- | --- | -------- | ------------- | ---------- | ---------------- | ---------------- | ----- | --- |
|                |            |                               |           |              |                 | L𝑙𝑡 |     | Sc o r e | e m b e d d i | n g f or d | i sc r e ti z ed | s co r e 𝑙 ′ ( ∈ | R 𝑑 ) |     |
w i th 5 le v e ls ( Le v el ) , fa c to r s t o c o n s i d er d u r in g th e s c o r i n gp r o c e s s ′ 𝑡
|     |     |     |     |     |     | R𝑙𝑜𝑔,𝑡 |     | Logicalreasonembeddingattime𝑡(∈R𝑑) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
(Factors),andothernotes(Notes),suchasthereturnformat,etc.
|                                     |     |     |     |     |     | R   |       | C o n c e | p t u a l r e a | s o ne m  | b e d d i n g | a t ti m e 𝑡 (∈ | R𝑑) |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------------- | --------- | ------------- | --------------- | --- | --- |
| Theentireprocesscanberepresentedas: |     |     |     |     |     | 𝑐   | 𝑜 𝑛,𝑡 |           |                 |           |               |                 |     |     |
|                                     |     |     |     |     |     | Q   |       | Le a r n  | a b l e p r o b | l e m e m | b e d d i n g | fo r 𝑞 (∈ R 𝑑)  |     |     |
|                                     |     |     |     |     |     |     | 𝑞 𝑡   |           |                 |           |               | 𝑡               |     |     |
𝑙ˆ 𝑖 =LLM(𝑃s(Data(𝑚𝑖 |𝑃𝐷 𝑖 |𝑚ˆ 𝑖 ) |Level|Factors|Notes)),∀𝑆 ∈S C𝑐𝑡,𝑗 Learnableconceptembeddingforconcept𝑐 𝑡,𝑗(∈R𝑑)
| 𝑡                                |     | 𝑡 𝑡 𝑡 |     |     | 𝑖   |      |     |                                           |     |     |     |     |     |       |
| -------------------------------- | --- | ----- | --- | --- | --- | ---- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ----- |
|                                  |     |       |     |     |     | MC𝑞𝑡 |     | Weightedsumofconceptembeddingsforproblem𝑞 |     |     |     |     |     | (∈R𝑑) |
|                                  |     |       |     |     | (1) |      |     |                                           |     |     |     |     |     | 𝑡     |
| where|representscombinationand𝑙ˆ |     | 𝑖     |     |     |     |      |     |                                           |     |     |     |     |     |       |
∈Lˆ.Atthispoint,wehave
𝑡
obtainedthesetofscoresgeneratedbyLLMLˆ.
|     |     |     |     |     |     | 5.1 | Learningphase |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
4.2 DomainCausalAnalysis
Theprimaryobjectiveofthelearningphaseistomodeltheknowl-
AsshowninFigure2(b),tomitigatetheimpactofnoisearising
edgechangesresultingfromstudents’currentinteractions.
fromhighuncertaintyinprogrammingtasksontheassessment
ofstudents’knowledgestates,forstudent𝑆 5.1.1 LogicalAbilityUpdate. Giventhequestion-conceptembed-
𝑖 whosubmitscode
𝑖 𝑖 d in g Q C , sc o r e e m b e dd i n g L𝑙 ′ , a n d lo g i c a l-l e v e l a n a l y s is R
𝑚 ∈ M at t im e st e p 𝑡 , a lo n g w i t h i t s c o rr e s p on di n g ID 𝑚 ˆ 𝑡, p r o b l e m 𝑞 𝑡 − 1 𝑡 − 𝑙𝑜 𝑔 ,𝑡 −1
𝑡 of t he c u r r e n t in t e r a ct io n a t t im e s 1 t e p 𝑡 − 1 , t h e l o g ic a l s t a t e ch a n g e
| de sc ri ptio | n 𝑃 𝐷 𝑖, a n | d t h e c o d e s c o r e 𝑙 ˆ 𝑖 | o b t a in ed f | r om t h e | p r e v i o u s |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ------------------------------- | --------------- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               | 𝑡            | 𝑡                               |                 |            |                 |     |     |     |     |     |     |     |     |     |
step,wedesignareasoningprompt𝑃𝑟 obtainedbythestudentthroughthisinteractionshouldberelated
toguidetheLLMininferring
totheansweredquestion,theobtainedscore,andthelogical-level
| the correctness | at  | the logical level and | the correctness |     | or error |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------------- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analysis.Therefore,thelogicalchangeiscalculatedusingthefol-
| causes at | the syntactic | level. The resulting | analysis | is  | encoded |     |     |     |     |     |     |     |     |     |
| --------- | ------------- | -------------------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lowingformula:
| usinga5-dimensionalbinaryvector𝑅 |     |     | 𝑖 asfollows: |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡
|                                      |     |     |     |     |     |       | =𝜎(MLP | 𝐶   | ℎ𝑎𝑛𝑔𝑒 ([QC𝑞𝑡−1 |     | ⊕L𝑙 | ⊕R𝑙𝑜𝑔,𝑡−1 ]|3𝑑,𝑑,𝑑)), |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ----- | ------ | --- | -------------- | --- | --- | --------------------- | --- | --- |
| • Firstdimension:Logicalcorrectness. |     |     |     |     |     | LC𝑡−1 |        | 𝐿𝐶  |                |     | ′   |                       |     | (3) |
𝑡 −1
• Seconddimension:Syntacticcorrectness. denotesconcatenation,𝜎
|     |     |     |     |     |     | where | ⊕   |     |     |     | representstheSigmoidfunc- |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
• Thirddimension:Syntacticerrorsduetocarelessness.
tion,andallnotationsinthispaperfollowthisnamingconvention.
• Fourthdimension:Syntacticerrorsduetoinsufficientprofi-
Consideringthatnotalllogicalchangescanbeinternalizedbystu-
ciency. dents,wedesignagatingmechanismtosimulatethelossduring
• Fifthdimension:Logicalerrors.
thestudent’sknowledgeinternalizationprocess:
F or exa m p l e , if t h e L L M d e t er m in e s th a t t h e s ub m it t ed c od e 𝑡 − 1=𝜎(MLP 𝐺 𝑎𝑡𝑒([QC𝑞𝑡−1 ]|3𝑑,𝑑,𝑑)).
| 𝑚𝑖  |     |     |     |     |     | Gate | 𝐿 𝐶 |     | 𝐿𝐶  |     | ⊕L𝑙 ′ | ⊕R𝑙𝑜𝑔,𝑡−1 |     | (4) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ----- | --------- | --- | --- |
𝑡 ∈ M is l o g i ca ll y c o rr e ct b u t c on ta i ns s y n t a cti c e rro r s du e to 𝑡 −1
𝑖
carelessness,thereturnedvectoris𝑅 𝑡 =[1,0,1,0,0].Conversely, Toenhancetheinfluenceofthereasoninganalysisextractedby
ifthecodeisfreeofcompilationerrorsbutcontainslogicalflaws theLLMonthefinalresults,wemultiplytheobtainedknowledge
7381

Multi-LevelProgrammingKnowledgeTracingEnhancedbyLLM WWW’26,April13–17,2026,Dubai,UnitedArabEmirates
Figure3:TheMLPKTFramework:Inthelearningphase,thestudent’sinteractiontupleisprocessedthroughamulti-level
abilitycomputationmoduletoderivetheknowledgeupdatefromthecurrentinteraction.Intheenhancement/forgetting
phase,thestudent’sforgettingandlearningbehaviorsaremodeledseparatelyaccordingtothemagnitudeoftheinteraction
interval.Intheapplicationphase,basedontheupdatedstudentknowledgestate,themulti-layerabilityintegrationmodule
computesthestudent’soverallability,whichisthenfedintotheIRTpredictionheadforforecasting.
change with the reasoning embedding. The final logical ability Finally,weusetheLLM’sanalysisofthegrammaticalconceptlevel
changeis: forthisinteractiontodeterminethedirectionofconceptualability
⊙Gate 𝑡 − 1⊙R𝑙𝑜𝑔,𝑡−1 , change,thusobtainingthegrammaticalconceptchangefromthis
|     | L(cid:102)C𝑡−1 =LC𝑡−1 | 𝐿 𝐶 |     | (5) |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
interaction:
where ⊙ denotestheHadamardproduct.Theadvantageofthis
𝑡 − 1⊙R𝑐𝑜𝑛,𝑡−1 .
designisthatthedirectionofthisknowledgechangeiscompletely S(cid:102)C𝑡−1 =SC𝑡−1 ⊙Gate 𝑆 𝐶 (9)
determinedbyR𝑙𝑜𝑔,𝑡.Subsequently,weupdatethestudent’slogical
|     |     |     |     | Subsequently, | we update | the student’s | grammatical | conceptual |
| --- | --- | --- | --- | ------------- | --------- | ------------- | ----------- | ---------- |
ability:
abilityusingtheobtainedgrammaticalconceptchange:
H 𝑡 −1+ =H 𝑡 −1+L(cid:102)C𝑡−1 . (6) 𝑡−1+ =H 𝑡−1+S(cid:102)C𝑡−1 .
|     | 𝐿   | 𝐿   |     |     |     | H 𝐶 𝐶 |     | (10) |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- |
5.1.2 ConceptualAbilityUpdate. Thechangeinconceptualabil- 5.1.3 ProblemUnderstandingUpdate. Asthenumberoftimesa
ityisrelatedtotheknowledgeconceptsassociatedwithquestion studentinteractswithaparticularproblemincreases,thestudent’s
𝑞 ,thescoreobtainedforthisquestion,andtheLLM’sanalysis
| 𝑡−1 |     |     |     | understandingofthisproblemgraduallyimproves.Tomodelthis |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
ofthegrammaticalconceptlevel.Therefore,wefirstobtainthe process,wedesignanexponentialfunctiontosimulatethestudent’s
grammaticalchangefromthisinteractionthroughthefollowing continuouslyimprovingunderstandingofacertainproblem.First,
formula: weobtainproblem-levelunderstandingchangethroughthecurrent
|       |                         |               |            | in t er a c t io | n q u es t io n | a n d t h e s c o re o b t | a in e d f r o m | t h is i n t e r a c t io n . |
| ----- | ----------------------- | ------------- | ---------- | ---------------- | --------------- | -------------------------- | ---------------- | ----------------------------- |
| SC𝑡−1 | =𝜎(MLP 𝐶 ℎ𝑎𝑛𝑔𝑒 [C𝑐𝑡−1,𝑗 | ⊕L𝑙 ⊕R𝑐𝑜𝑛,𝑡−1 | ]|3𝑑,𝑑,𝑑). | (7)              |                 |                            |                  |                               |
|       | 𝑆𝐶                      | ′             |            |                  |                 |                            |                  |                               |
𝑡 −1 T h e i n s p ir at io n f o r th i s ap p r o a c h is t h a t h ig h - s c ori n g i n t e r a c t io n s
Similartothelogicalabilityupdate,wedesignanothergatingmech- mayrepresentthatthestudenthasgainedmoreunderstandingof
anismtosimulatetheknowledgelossduringthestudent’sinternal- theproblemthroughthislearningsession.Thecalculationmethod
| izationprocess: |                |     |     | forproblemunderstandingchangeisasfollows: |     |         |     |     |
| --------------- | -------------- | --- | --- | ----------------------------------------- | --- | ------- | --- | --- |
| 𝑡               | 𝐺 𝑎𝑡𝑒([C𝑐𝑡−1,𝑗 |     |     |                                           |     | 𝐶 ℎ𝑎𝑛𝑔𝑒 |     |     |
Gate − 1=𝜎(MLP ⊕L𝑙 ′ ⊕R𝑐𝑜𝑛,𝑡−1 ]|3𝑑,𝑑,𝑑)). (8) PC𝑡−1 =𝜎(MLP ([Q𝑞𝑡−1 ⊕L𝑙 ′ ]|2𝑑,𝑑,𝑑)), (11)
| 𝑆 𝐶 | 𝑆𝐶  | 𝑡 −1 |     |     |     | 𝑃𝐶  | 𝑡 −1 |     |
| --- | --- | ---- | --- | --- | --- | --- | ---- | --- |
7382

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
P(cid:99)C𝑡−1 =log(1+𝑛 𝑞𝑡−1 )·PC𝑡−1 , (12) 5.3.1 Multi-levelAbilityIntegrationModule. First,wemapthestu-
dent’sknowledgestatestoscalars:
w in h te e r r a e c 𝑛 te 𝑞 d 𝑡− w 1 r it e h pr b e y se th n e ts c t u h r e re n n u t m st b u e d r e o n f t. ti S m u e b s se p q r u o e b n le t m ly, 𝑞 s 𝑡 im −1 il h a a r s to be t e h n e LA𝑡 =𝜎(MLP𝐿(H 𝑡 𝐿 |𝑑,𝑑,1)), (20)
previoussections,wechoosetouseagatingmechanismtosimulate
thestudent’sinternalizationprocess:
CA𝑡 =𝜎(MLP𝐶(H
𝐶
𝑡 |𝑑,𝑑,1)), (21)
Gate 𝑡 𝑃 − 𝐶 1=𝜎(MLP 𝐺 𝑃𝐶 𝑎𝑡𝑒([QC𝑞𝑡−1 ⊕L𝑙 𝑡 ′ −1 ]|2𝑑,𝑑,𝑑)), (13) Subsequently P , A w 𝑡 e = ag 𝜎 g ( r M eg L a P t 𝑃 e ( t [ h H e 𝑡 𝑃 th ⊕ re Q e 𝑞 a 𝑡+ b 1 i ] li | t 2 i 𝑑 e , s 𝑑 t , h 1 r ) o ) u . ghweigh ( t 2 e 2 d )
scorestoformthestudent’scomprehensiveability:
P(cid:102)C𝑡−1 =P(cid:99)C𝑡−1 ·Gate 𝑡
𝑃
−
𝐶
1. (14)
OA𝑡 =𝜃
1
·LA𝑡 +𝜃
2
·CA𝑡 +𝜃
3
·PA𝑡 . (23)
Finally,thechangeinthestudent’sunderstandingoftheproblem
ismodeledas: Beforeformallycalculatingthecomprehensiveability,wenormalize
H 𝑡
𝑃
−1+ =H 𝑡
𝑃
−1+P(cid:102)C𝑡−1 . (15) thethreetrainableweightparameters𝜃 1 ,𝜃 2 ,𝜃 3 throughsoftmax.
5.3.2 IRTPredictionModule. Weusethetwo-parameterItemRe-
5.2 Enhancement/Forgettingphase sponseTheorytocalculatethestudent’sfinalscoringsituation.The
GiventheinteractiontimeintervalΔ𝑇
𝑡
betweenstudent’stime𝑡−1 finalstudentscorepredictionisasfollows:
a th n e d s t h im or e t- 𝑡 i , n a te n r d va g l iv le e a n rn tw in o g t m hr o e d s u h l o e ld a s n 𝜙 d 𝑓 l 𝑙 o 𝑜𝑜 n 𝑟 g- a i n n d te 𝜙 rv 𝑐𝑒 a 𝑖 l 𝑙, fo w r e ge a t p ti p n l g y 𝑙ˆ 𝑡 𝑝𝑟𝑒𝑑 = 1+𝑒−𝑎𝑡 1 (OA𝑡−𝑏𝑡) , (24)
modulerespectivelyaccordingtotherelationshipbetweenΔ𝑇 𝑡 and where𝑎isthediscriminationparameter,reflectingtheitem’s
the two thresholds. For brevity, we only illustrate the enhance-
abilitytodistinguishdifferentabilitylevels.Thelargerthisparame-
ment/forgettingphasemethodusingthestudent’slogicalability ter,thestrongertheitem’sabilitytodiscriminateabilitylevels.𝑏is
asanexample.Theenhancement/forgettingprocessesforstudent
thedifficultyparameter,representingtheabilitylevelrequiredto
conceptmasteryandproblemunderstandingabilityarecompletely
answertheitemcorrectly.Thelargerthevalue,themoredifficult
consistentwiththisapproach. theitem.Thediscrimination𝑎
𝑡
∈R1anddifficulty𝑏
𝑡
∈R1ofitem
5.2.1 Short-intervalLearningModule. ForthecasewhereΔ𝑇 𝑡 ≤ 𝑞 𝑡 canbothbeobtainedthroughsimpleembeddingmatrices.
𝜙 𝑓𝑙𝑜𝑜𝑟, the knowledge state change caused by student learning
5.4 ModelOptimization
duringtheintervaltimeisobtainedthroughthefollowingmethod:
TheknowledgetracinglossL measuresthediscrepancybetween
KT
ΔH 𝐺 𝐿 𝑎𝑖𝑛 =MLP 𝐺 𝐿 𝑎𝑖𝑛([H 𝑡 𝐿 −1+ ⊕Δ𝑇 𝑡]|𝑑+1,𝑑,𝑑/2,1), (16) predictedscores𝑙ˆ 𝑡 𝑝𝑟𝑒𝑑 ∈ [0,1]andtruelabels𝑙ˆ 𝑡 ∈ [0,1]over𝑇 time
steps.Weemploybinarycross-entropy:
H 𝑡 𝐿 =ΔH 𝐺 𝐿 𝑎𝑖𝑛+H 𝑡 𝐿 −1+, Δ𝑇 𝑡 ≤𝜙 𝑓𝑙𝑜𝑜𝑟 . (17) 𝑇
5.2.2 Long-intervalForgettingModule. ForthecasewhereΔ𝑇 𝑡 > L KT =− ∑︁(cid:16) 𝑙ˆ 𝑡log(𝑙ˆ 𝑡 𝑝𝑟𝑒𝑑 )+(1−𝑙ˆ 𝑡)log(1−𝑙ˆ 𝑡 𝑝𝑟𝑒𝑑 ) (cid:17) . (25)
𝜙 𝑓𝑙𝑜𝑜𝑟,toavoidabnormallylargevalues,wesetinteractioninter-
𝑡=1
valsgreaterthan𝜙 𝑐𝑒𝑖𝑙 to𝜙 𝑐𝑒𝑖𝑙,andfurtherconcatenatethecurrent WeutilizetheAdam[13]algorithmtooptimizethemodel.
statewiththeinteractionintervalanduseanMLPtoextractthe
proportionofstudentforgettingduringtimeΔ𝑇 𝑡+1 : 6 Experiments
Inthissection,weconductedextensiveexperimentstoanswerthe
ΔH 𝐿 𝐹𝑜𝑟𝑔𝑒𝑡 =𝜎(MLP 𝐿 𝐹𝑜𝑟𝑔𝑒𝑡 ([H 𝑡 𝐿 −1+ ⊕Δ𝑇 𝑡+1 ]|𝑑+1,𝑑,𝑑/2,1)). (18) followingquestions:
• Q1:IstheLLM’sscoringofcodereasonable?
Thestateafterforgettingisrepresentedas:
• Q2:HowistheperformanceofMIE+MLPKT?
H 𝑡 𝐿 =H 𝑡 𝐿 −1+ −ΔH 𝐿 𝐹𝑜𝑟𝑔𝑒𝑡 ·H 𝑡 𝐿 −1+, Δ𝑇 𝑡 >𝜙 𝑓𝑙𝑜𝑜𝑟 . (19) • Q3:WhatistheimpactofdifferentcomponentsinMIE+MLPKT?
CanthefeaturesextractedbyLLMimpactthemodel’seffect?
Weselectthe75thpercentileand90thpercentileofinteractiontime • Q4:HowdoesMIE+MLPKTtracktheprocessofstudents’
intervalsinthedatasetasthevaluesfor𝜙 𝑐𝑒𝑖𝑙 and𝜙 𝑓𝑙𝑜𝑜𝑟.Thesecan differentabilitylevels?(SeeAppendixC.3)
bedynamicallyselectedaccordingtothecharacteristicsofdifferent • Q5:Whatisthetrade-offbetweenthemodel’spredictionper-
datasets. formanceanditscomputationalefficiency?(SeeAppendix
C.4)
5.3 Applicationphase
6.1 ExperimentalSetup
Intheapplicationphase,giventhestudent’scurrentthree-level
abilitiesandtheproblemthestudentwillinteractwithatthenext 6.1.1 Datasets. Tovalidatetheapplicabilityofourproposedmethod
timestep,sinceconventionalIRTrequiresstudentabilitiesthat acrossstudentsofvaryingproficiencylevels,ourexperimentsuti-
are often single-leveled, we design a multi-level student ability lizedthreedatasets:Code-S,Code-F,BePKT.Thespecificintroduc-
integrationmoduletomakeItemResponseTheoryapplicableto tionofthedatasetcanbefoundinAppendixC.1.Table2presents
multi-layerstudentabilities. thestatisticalinformationforalldatasets.
7383

Multi-LevelProgrammingKnowledgeTracingEnhancedbyLLM WWW’26,April13–17,2026,Dubai,UnitedArabEmirates
Table2:Statisticalinformationofthedatasets expertscoresonthetestsetforfinalevaluationofmodelperfor-
mance.AsshowninFigure4,theresultsdemonstratethatLLM-
Code-S Code-F BePKT basedscoringsignificantlyenhancesmodelperformance.Aconsis-
#Student 413 506 1,638 tentpatternemergesacrossallexaminedmethods:bothMLPKT
#Question 50 50 606 andthefourbaselineapproachesexhibitmarkedlyimprovedper-
#Concept 18 18 106 formanceontheexpert-scoredtestsetwhentrainedandvalidated
| #Interaction | 69,627 125,571 | 76,657 |     |     |     |     |
| ------------ | -------------- | ------ | --- | --- | --- | --- |
usingLLM-generatedscores,asopposedtorawscorelabels.This
empiricalevidencecorroboratesthesoundnessofourproposedMIE
scoringmechanismfromtheperspectiveofdownstreammodelper-
formance.
6.1.2 Baselines. To evaluate the performance of our proposed Thus,fromboththedataandmodelperspectives,wedemon-
method on the programming knowledge tracing (KT) task, we stratetherationalityoftheproposedMIEframeworkforevaluating
compareditagainst18state-of-the-artmethods:AKT[9],DTrans-
studentcodesubmissions.
former[32],EXKT[16],FlucKT[11],FoLiBiKT[12],LefoAKT[5],
SAKT[19],StableKT[15],ATKT[10],CSKT[4],DKT[22],DKVMN
Table3:ErrorMetricsComparisonAcrossModels
[35],SKVMN[1],GRKT[8],LPKT[23].DKT+[26],Code-DKT[24],
ECKT[33].Adetaileddescriptionoftheaforementionedmodels
|     |     |     | ModelName | MAE MRE(%) | MedianAE | StdAE RMSE |
| --- | --- | --- | --------- | ---------- | -------- | ---------- |
willbeprovidedintheAppendixC.2.
|                              |                               |     | deepseek-v3.1 | 3.94 16.65 | 3.00 | 4.08 5.67 |
| ---------------------------- | ----------------------------- | --- | ------------- | ---------- | ---- | --------- |
|                              |                               |     | llama-4-scout | 6.09 26.50 | 4.00 | 5.58 8.26 |
| 6.1.3 ImplementationDetails. | Toensureafaircomparisonacross |     |               |            |      |           |
|                              |                               |     | deepseek-v3.0 | 6.10 26.39 | 4.00 | 4.92 7.84 |
allbaselinemodels,westandardizedthesequencelengthto200and
|     |     |     | llama-3.1-70b-instruct | 8.64 39.61 | 7.00 | 6.29 10.69 |
| --- | --- | --- | ---------------------- | ---------- | ---- | ---------- |
thebatchsizeto24.Additionally,wesettheembeddingdimension
|     |     |     | raw-score | 26.87 98.59 | 23.74 | 10.41 28.82 |
| --- | --- | --- | --------- | ----------- | ----- | ----------- |
to256forallbaselines,withadropoutrateof0.05.Allexperiments
wereimplementedusingPyTorchinPythonandconductedona
deviceequippedwithanNVIDIAA800GPU.
|     |     |     | RMSE Performance Comparison |     | MAE Performance Comparison |     |
| --- | --- | --- | --------------------------- | --- | -------------------------- | --- |
Sincethelabelsarecontinuousvaluesrangingfrom0to1,we
|     |     |     | (Lower is Better) |     | (Lower is Better) |     |
| --- | --- | --- | ----------------- | --- | ----------------- | --- |
employedRootMeanSquareError(RMSE)andMeanAbsoluteError 0.40 0.350
|     |     |     |     | DKT |     | DKT |
| --- | --- | --- | --- | --- | --- | --- |
(MAE)astheevaluationmetricsforthemodels.Furthermore,inthe GRKT 0.325 GRKT
|     |     |     | 0.35 |      | 0.300 |      |
| --- | --- | --- | ---- | ---- | ----- | ---- |
|     |     |     |      | LPKT |       | LPKT |
performancecomparison,toadditionallyvalidatetheperformance ESMR StableKT 0.275 StableKT
|     |     |     | 0.30 | MIE+MLPKT | EAM 0.250 | MIE+MLPKT |
| --- | --- | --- | ---- | --------- | --------- | --------- |
ofMLPKTontraditionalclassificationtasks,thescoresprovidedby
0.225
theLLMwerebinarized(wherescores>=0.5areassigned1,and0 0.25 0.200
otherwise),basedonwhichtheAreaUndertheCurve(AUC)and 0.175
|     |     |     | 0.20 |     | 0.150 |     |
| --- | --- | --- | ---- | --- | ----- | --- |
Accuracy(ACC)werecalculated.
|     |     |     | Raw Score | LLM Score | Raw Score | LLM Score |
| --- | --- | --- | --------- | --------- | --------- | --------- |
6.2 ReasonablenessofLLMDataScoring(Q1) Figure4:PerformanceComparisonofKnowledgeTracking
ModelswithDifferentLabelTypes
WeselectedtheCode-Sdatasetandconductedexperimentsfrom
twoperspectivestovalidatetherationalityofscoringbasedon
largelanguagemodels(LLMs).First,fromtheperspectiveofthe
6.3 PerformanceComparison(Q2)
dataitself,weengagedexpertstoevaluate10,000codesubmissions.
The expert scores were compared with scores from four LLMs Table4presentsthepredictiveperformanceofourMIE+MLPKT
andtheinitialtest-case-basedscoringbycomputingtheaverage modelcomparedwithotherbaselinemethodsacrossfourdatasets.
errorrate.Specifically,weemployedmetricssuchasMeanAbso-
Toensurethereliabilityoftheexperimentalresults,weemployed
luteError(MAE),MeanRelativeError(MRE),MedianAbsolute
a5-foldcross-validationstrategy,reportingtheaveragevaluesfor
Error(MedianAE),StandardAbsoluteError(StdAE),andRoot allmetrics.Thebestresultsarehighlightedin bluebackground,
MeanSquareError(RMSE)toassessthediscrepanciesbetween
|     |     |     | whilethesecond-bestresultsaremarkedin |     | greenbackground. |     |
| --- | --- | --- | ------------------------------------- | --- | ---------------- | --- |
modelscoresandexpertscores.Theresults,aspresentedinTable
3,demonstratethatLLM-basedscoresforcodesubmissionsare Asobserved,theMIE+MLPKTframeworkconsistentlyachievesthe
significantlyclosertoexpertscorescomparedtotest-case-based highestperformanceamongallmodels,demonstratingthesuperi-
orityofourproposedapproachinprogrammingknowledgetracing
scores.Notably,thescoresfromdeepseek-v3.1outperformother
tasks.
LLMsintermsofproximitytoexpertscores,surpassingbothother
modelsandthetest-case-basedraw_score.Consequently,thisstudy
6.4 AblationStudy(Q3)
adoptsthedeepseek-v3.1scoresasthereferencelabels.
Subsequently,wevalidatedtherationalityofourapproachfrom Tovalidateourdesignphilosophyofdecomposingstudentabil-
themodelperspective.Specifically,weevaluatedperformanceon ityintomultiplelevels,wecomparedthecompleteMIE+MLPKT
programmingknowledgetrackingtasksusingStableKT[15],DKT modelwiththreevariantmodels—lackingconcept-levelability(wo
[22],LPKT[23],GRKT[8],andMIE+MLPKT.WeusedLLMScore /con),logical-levelability(wo/log),andproblem-levelability(wo
andRawScoreaslabelsfortrainingandvalidation,whileemploying /pro)—ontheCode-Sdataset.AsshowninFigure5,theresults
7384

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
Table4:ModelPerformanceMetricsonCode-S,Code-F,andBePKTDatasets(WithProgrammingKTIndicator)
|       |     |     |               |      |     | Code-S  |      |     | Code-F  |      | BePKT       |
| ----- | --- | --- | ------------- | ---- | --- | ------- | ---- | --- | ------- | ---- | ----------- |
| Model |     |     | ProgrammingKT |      |     |         |      |     |         |      |             |
|       |     |     |               | RMSE | MAE | AUC ACC | RMSE | MAE | AUC ACC | RMSE | MAE AUC ACC |
AKT ✗ 0.2588 0.2212 0.6893 0.6832 0.2634 0.2224 0.6486 0.6901 0.2257 0.1767 0.6822 0.6971
DTransformer ✗ 0.2034 0.1582 0.8637 0.8285 0.2160 0.1693 0.8398 0.8176 0.2189 0.1768 0.6860 0.7020
EXKT ✗ 0.2591 0.2210 0.6861 0.6828 0.2635 0.2233 0.6440 0.6900 0.2269 0.1764 0.6762 0.6885
✗
FlucKT 0.2568 0.2217 0.6874 0.6835 0.2636 0.2236 0.6465 0.6896 0.2252 0.1765 0.6771 0.6895
✗
FoLiBiKT 0.2590 0.2219 0.6887 0.6825 0.2660 0.2250 0.6442 0.6892 0.2263 0.1769 0.6749 0.6918
LefoKT-AKT ✗ 0.2589 0.2218 0.6913 0.6833 0.2618 0.2248 0.6492 0.6905 0.2654 0.2121 0.6746 0.6748
SAKT ✗ 0.2209 0.1880 0.7474 0.7003 0.2464 0.2009 0.7108 0.7110 0.2327 0.1825 0.6633 0.6635
StableKT ✗ 0.2068 0.1598 0.8501 0.8182 0.2186 0.1722 0.8368 0.8156 0.2098 0.1675 0.7246 0.7197
ATKT ✗ 0.2067 0.1571 0.8684 0.8239 0.2168 0.1657 0.8446 0.8112 0.2274 0.1783 0.6703 0.6908
CSKT ✗ 0.1976 0.1486 0.8751 0.8432 0.2097 0.1614 0.8560 0.8250 0.2104 0.1667 0.6997 0.7040
✗
DKT 0.2109 0.1563 0.8588 0.8203 0.2219 0.1654 0.8422 0.8079 0.2370 0.1879 0.6571 0.6730
✗
DKVMN 0.1978 0.1506 0.8782 0.8348 0.2100 0.1624 0.8584 0.8193 0.1981 0.1558 0.7612 0.7421
SKVMN ✗ 0.2186 0.1818 0.7067 0.7006 0.2467 0.2003 0.6920 0.6981 0.2445 0.1997 0.5652 0.6546
GRKT ✗ 0.1987 0.1504 0.8688 0.8339 0.2123 0.1645 0.8436 0.8212 0.1793 0.1388 0.8258 0.8256
LPKT ✗ 0.2043 0.1583 0.8600 0.8217 0.2180 0.1739 0.8357 0.8165 0.1863 0.1472 0.8150 0.8152
Code-DKT ✓ 0.1952 0.1512 0.8845 0.8440 0.2108 0.1628 0.8565 0.8260 0.1852 0.1447 0.8225 0.8210
✓
ECKT 0.2060 0.1580 0.8510 0.8195 0.2175 0.1690 0.8375 0.8158 0.2185 0.1760 0.7020 0.7015
✓
DKT+ 0.2105 0.1637 0.8545 0.8205 0.2274 0.1803 0.8150 0.8010 0.2111 0.1639 0.7180 0.7130
✓
MIE+MLPKT-DK-V31 0.1904 0.1430 0.8926 0.8451 0.2015 0.1521 0.8738 0.8305 0.1735 0.1319 0.8380 0.8408
| demonstratethatthecompleteMIE+MLPKTmodeloutperforms |     |     |     |     |     |     |     |     |     |     | 0.1455 |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
RMSE
allthreevariantsthatlackspecificabilitylevels,confirmingthe
|     |     |     |     |     |     |     |     | 0.1928 |     |     | MAE |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
necessityofourapproachtomodelingstudentabilityacrossthree 0.1450
0.1926
distinctlevels.
|                                   |          |                                   |          |                                   |          |       |     | ESMR 0.1924 |     |     | 0.1445 EAM |
| --------------------------------- | -------- | --------------------------------- | -------- | --------------------------------- | -------- | ----- | --- | ----------- | --- | --- | ---------- |
|                                   | Code-S   |                                   | Code-F   |                                   |          | BePKT |     |             |     |     |            |
|                                   | RRMMSSEE | MAE                               | RRMMSSEE | MAE 0.160                         | RRMMSSEE | MAE   |     | 0.1922      |     |     |            |
|                                   | 0.196    | 0.150                             | 0.208    |                                   | 0.184    | 0.145 |     |             |     |     |            |
|                                   |          |                                   |          | 0.155                             | 0.182    | 0.140 |     |             |     |     | 0.1440     |
| ESMR                              | 0.194    | 0.145 EAM ESMR                    | 0.206    | EAM ESMR                          | 0.180    | EAM   |     | 0.1920      |     |     |            |
|                                   |          | 0.140                             | 0.204    | 0.150                             |          | 0.135 |     |             |     |     |            |
|                                   | 0.192    |                                   |          |                                   | 0.178    | 0.130 |     |             |     |     |            |
|                                   |          | 0.135                             | 0.202    | 0.145                             | 0.176    | 0.125 |     | 0.1918      |     |     | 0.1435     |
|                                   | 0.190    |                                   |          |                                   | 0.174    |       |     |             |     |     |            |
|                                   |          | 0.130                             | 0.200    | 0.140                             | 0.172    | 0.120 |     |             |     |     |            |
| MIE+MLPKTwo/conwo/logwo/prowo/rea |          | MIE+MLPKTwo/conwo/logwo/prowo/rea |          | MIE+MLPKTwo/conwo/logwo/prowo/rea |          |       |     | 0.1916      |     |     |            |
Models Models Models deepseek-v3.1 llama-4-scout llama-3.1-70b-instruct deepseek-v3.0
Models
Figure5:PerformanceofMIE+MLPKTandVariantsonThree
Figure6:AblationStudy:ImpactofDifferentLLMsonEr-
Datasets
rorReasonExtractionandModelPerformanceonCode-S
Dataset
Additionally,toinvestigatewhetherthereasonvectorsextracted
bythelargelanguagemodel(LLM)contributetomodelperfor-
mance,wealsopresentedtheperformanceofthemodelwithout
addressthesechallenges,weproposetheMIE+MLPKTframework.
reasonvectors(wo/rea)inFigure5.Theresultsindicatethatthe
TheMIEcomponentleveragescarefullydesignedpromptstoelicit
LLM-generatedreasonvectorscanenhancemodelperformance.
Furthermore,toexaminetheimpactofreasonsextractedbydif- fromlargelanguagemodels(LLMs)reasonablescoringlabelsalong-
ferentLLMsontheresults,weuseddeepseek-v3.0,llama-3.1-70b- sidemulti-levelerrorcauseanalyses,therebymitigatingissuesof
labelcontinuityandirrationalitywhilefurtheralleviatinghighun-
instruct,andllama-4-scouttoextracterrorreasonsfromtheCode-S
certainty.Concurrently,toaccommodatethemulti-layerednature
datasetandcomparedthemwiththebaselinedeepseek-v3.1.The
ofstudentproficiencyrequirementsinprogrammingtasks,wein-
resultsareshowninFigure6.Althoughdeepseek-v3.1’sscoring
resultsweretheclosesttoexpertratings,thereasonanalysisfrom troduceMLPKT,athree-tieredknowledgetracingframeworkthat
deepseek-v3.0demonstratedagreaterenhancementtomodelper- integratestheerroranalysisvectorsextractedbyMIE.Extensive
formance. experimentsacrossthreedatasetsand18baselinessubstantiatethe
efficacyofourproposedframework.Infuturework,weplanto
7 Conclusion evaluateMIE+MLPKTinauthenticeducationalsettings.
Thispaperelucidatesthreedistinctivecharacteristicsofprogram-
Acknowledgments
| ming | knowledge | tracing | tasks compared | to  | traditional | subject- |     |     |     |     |     |
| ---- | --------- | ------- | -------------- | --- | ----------- | -------- | --- | --- | --- | --- | --- |
basedknowledgetracing,whichoftenresultinsuboptimalperfor- ThisresearchwasfundedbytheNationalNaturalScienceFounda-
manceofexistingKTmodelsonprogrammingbenchmarks.To tionofChina(Nos.62272093,62137001)
7385

Multi-LevelProgrammingKnowledgeTracingEnhancedbyLLM WWW’26,April13–17,2026,Dubai,UnitedArabEmirates
References
Advancesinneuralinformationprocessingsystems28(2015).
[1] GhodaiAbdelrahmanandQingWang.2019.Knowledgetracingwithsequential [23] ShuanghongShen,QiLiu,EnhongChen,ZhenyaHuang,WeiHuang,YuYin,Yu
key-valuememorynetworks.InProceedingsofthe42ndinternationalACMSIGIR Su,andShijinWang.2021.Learningprocess-consistentknowledgetracing.In
conferenceonresearchanddevelopmentininformationretrieval.175–184. Proceedingsofthe27thACMSIGKDDconferenceonknowledgediscovery&data
[2] UriAlon,MeitalZilberstein,OmerLevy,andEranYahav.2018.Ageneralpath- mining.1452–1460.
basedrepresentationforpredictingprogramproperties.ACMSIGPLANNotices [24] YangShi,MinChi,TiffanyBarnes,andThomasPrice.2022. Code-dkt:A
53,4(2018),404–419. code-basedknowledgetracingmodelforprogrammingtasks. arXivpreprint
[3] UriAlon,MeitalZilberstein,OmerLevy,andEranYahav.2019.code2vec:Learn- arXiv:2206.03545(2022).
ingdistributedrepresentationsofcode.ProceedingsoftheACMonProgramming [25] VinitraSwamy,AllenGuo,SamuelLau,WiltonWu,MadelineWu,Zachary
Languages3,POPL(2019),1–29. Pardos,andDavidCuller.2018.Deepknowledgetracingforfree-formstudent
[4] YouhengBai,XueyiLi,ZitaoLiu,YayingHuang,TengGuo,MingliangHou,Feng codeprogression.InArtificialIntelligenceinEducation:19thInternationalConfer-
Xia,andWeiqiLuo.2025. csKT:Addressingcold-startprobleminknowledge ence,AIED2018,London,UK,June27–30,2018,Proceedings,PartII19.Springer,
tracingviakernelbiasandconeattention.ExpertSystemswithApplications266 348–352.
(2025),125988. [26] LisaWang,AngelaSy,LarryLiu,andChrisPiech.2017.Deepknowledgetracing
[5] YouhengBai,XueyiLi,ZitaoLiu,YayingHuang,MiTian,andWeiqiLuo.2025. onprogrammingexercises.InProceedingsofthefourth(2017)ACMconferenceon
Rethinkingandimprovingstudentlearningandforgettingprocessesforatten- learning@scale.201–204.
tionbasedknowledgetracingmodels.InProceedingsoftheAAAIConferenceon [27] AWaswani,NShazeer,NParmar,JUszkoreit,LJones,AGomez,LKaiser,andI
ArtificialIntelligence,Vol.39.27822–27830. Polosukhin.2017.Attentionisallyouneed.InNIPS.
[6] RyanSJdBaker,AlbertTCorbett,andVincentAleven.2008. Moreaccurate [28] KevinHWilson,YanKarklin,BojianHan,andChaitanyaEkanadham.2016.
studentmodelingthroughcontextualestimationofslipandguessprobabilities Backtothebasics:BayesianextensionsofIRToutperformneuralnetworksfor
inbayesianknowledgetracing.InIntelligentTutoringSystems:9thInternational proficiencyestimation.(2016).
Conference,ITS2008,Montreal,Canada,June23-27,2008Proceedings9.Springer, [29] YaqiangWu,HuiZhu,ChenyangWang,FujianSong,HaipingZhu,YanChen,
406–415. QinghuaZheng,andFengTian.2024.Programmingknowledgetracingbased
[7] AlbertTCorbettandJohnRAnderson.1994.Knowledgetracing:Modelingthe onheterogeneousgraphrepresentation.Knowledge-BasedSystems300(2024),
acquisitionofproceduralknowledge.Usermodelinganduser-adaptedinteraction 112161. doi:10.1016/j.knosys.2024.112161
4(1994),253–278. [30] BihanXu,ZhenyaHuang,JiayuLiu,ShuanghongShen,QiLiu,EnhongChen,
[8] JiajunCui,HongQian,BoJiang,andWeiZhang.2024.Leveragingpedagogical JinzeWu,andShijinWang.2023.Learningbehavior-orientedknowledgetracing.
theoriestounderstandstudentlearningprocesswithgraph-basedreasonable InProceedingsofthe29thACMSIGKDDconferenceonknowledgediscoveryand
knowledgetracing.InProceedingsofthe30thACMSIGKDDConferenceonKnowl- datamining.2789–2800.
edgeDiscoveryandDataMining.502–513. [31] Chun-KitYeungandDit-YanYeung.2018. Addressingtwoproblemsindeep
[9] AritraGhosh,NeilHeffernan,andAndrewSLan.2020.Context-awareattentive knowledgetracingviaprediction-consistentregularization.InProceedingsofthe
knowledgetracing.InSIGKDD.2330–2339. fifthannualACMconferenceonlearningatscale.1–10.
[10] XiaopengGuo,ZhijieHuang,JieGao,MingyuShang,MaojingShu,andJunSun. [32] YuYin,LeDai,ZhenyaHuang,ShuanghongShen,FeiWang,QiLiu,Enhong
2021.Enhancingknowledgetracingviaadversarialtraining.InProceedingsof Chen,andXinLi.2023.Tracingknowledgeinsteadofpatterns:Stableknowledge
the29thACMInternationalConferenceonMultimedia.367–375. tracingwithdiagnostictransformer.InWWW.855–864.
[11] MingliangHou,XueyiLi,TengGuo,ZitaoLiu,MiTian,RenqiangLuo,andWeiqi [33] YangYu,YingboZhou,YaokangZhu,YutongYe,LiangyuChen,andMingsong
Luo.2025.CognitiveFluctuationsEnhancedAttentionNetworkforKnowledge Chen.2024.Eckt:Enhancingcodeknowledgetracingvialargelanguagemodels.
Tracing.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39. InProceedingsoftheAnnualMeetingoftheCognitiveScienceSociety,Vol.46.
14265–14273. [34] MichaelVYudelson,KennethRKoedinger,andGeoffreyJGordon.2013.Individ-
[12] YoonjinIm,EunseongChoi,HeejinKook,andJongwukLee.2023.Forgetting- ualizedbayesianknowledgetracingmodels.InArtificialintelligenceineducation:
awareLinearBiasforAttentiveKnowledgeTracing.InCIKM.3958–3962. 16thinternationalconference,AIED2013,Memphis,TN,USA,July9-13,2013.
[13] DiederikP.KingmaandJimmyBa.2015.Adam:AMethodforStochasticOpti- proceedings16.Springer,171–180.
mization.In3rdInternationalConferenceonLearningRepresentations,ICLR2015, [35] JianiZhang,XingjianShi,IrwinKing,andDit-YanYeung.2017.Dynamickey-
SanDiego,CA,USA,May7-9,2015,ConferenceTrackProceedings,YoshuaBengio valuememorynetworksforknowledgetracing.InWWW.765–774.
andYannLeCun(Eds.). [36] MengxiaZhu,SiqiHan,PeisenYuan,andXuesongLu.2022. EnhancingPro-
[14] RuixinLi,YuYin,LeDai,ShuanghongShen,XinLin,YuSu,andEnhongChen. grammingKnowledgeTracingbyInteractingProgrammingSkillsandStudent
2022. PST:measuringskillproficiencyinprogrammingexerciseprocessvia Code.InLAK22:12thInternationalLearningAnalyticsandKnowledgeConference
programmingskilltracing.InProceedingsofthe45thinternationalacmsigir (Online,USA)(LAK22).AssociationforComputingMachinery,NewYork,NY,
conferenceonresearchanddevelopmentininformationretrieval.2601–2606. USA,438–443. doi:10.1145/3506860.3506870
[15] XueyiLi,YouhengBai,TengGuo,ZitaoLiu,YayingHuang,XiangyuZhao,
FengXia,WeiqiLuo,andJianWeng.2024.Enhancinglengthgeneralizationfor
attentionbasedknowledgetracingmodelswithlinearbiases.InIJCAI.5918– A PROMPTTEMPLATE
5926.
[16] XueyiLi,YouhengBai,TengGuo,YingZheng,MingliangHou,BojunZhan, Theratingpromptandthereasonanalysispromptmentionedin
YayingHuang,ZitaoLiu,BoyuGao,andWeiqiLuo.2024.ExtendingContext 4.2areshowninTable5andTable6.
WindowofAttentionBasedKnowledgeTracingModelsviaLengthExtrapolation.
InECAI.IOSPress,1479–1486.
[17] NaimingLiu,ZichaoWang,RichardBaraniuk,andAndrewLan.2022. Open- B EMBEDDINGGENERATION
endedknowledgetracingforcomputerscienceeducation.InProceedingsofthe
2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing. B.1 ScoreEmbedding
[18] KokiNagatani,QianZhang,MasahiroSato,Yan-YingChen,FrancineChen,
andTomokoOhkuma.2019. Augmentingknowledgetracingbyconsidering Scoreembeddingcapturestheimpactofstudentperformanceon
[19] f S o h r a g l e in tt i i P n a g n b d e e h y a a v n io d r. G I e n o T rg h e e K w a o r r y ld pi w s. i 2 d 0 e 1 w 9. eb A c S o e n l f f e - r A e t n t c e e n . t 3 iv 1 e 01 M – o 3 d 1 e 0 l 7 f . orKnowledge theirknowledgestate.Forthescore𝑙 𝑡 ∈ [0,1] attime𝑡,wedis-
Tracing.InProceedingsofthe12thInternationalConferenceonEducationalData cretizeitinto101integervaluesfrom0to100anddefineascore
Mining(EDM2019).Montréal,Canada,384–389. https://arxiv.org/abs/1907.06837 embeddingmatrixL∈R101×𝑑,where𝑑istheembeddingdimension.
arXiv:1907.06837.
Forconvenience,alldimensionsusedinthispaperareuniformly
[20] ZacharyAPardosandNeilTHeffernan.2010. Modelingindividualizationin
abayesiannetworksimplementationofknowledgetracing.InUserModeling, denotedas𝑑.Thescoreisscaledandconvertedtoanintegerindex
A Isl d a a n p d t , a H ti I o , n U , S a A nd ,J P u e n r e so 2 n 0 a -2 li 4 z , a 2 t 0 io 1 n 0 : . 1 P 8 ro th ce I e n d t i e n r g n s at 1 i 8 o . n S a p l r C in o g n e fe r, re 2 n 5 c 5 e – , 2 U 6 M 6. AP2010,Big as𝑙 𝑡 ′ =⌊𝑙 𝑡 ·100⌋.Theembeddingofthescoreiscalculatedas:
[21] ZacharyAPardosandNeilTHeffernan.2011. KT-IDEM:Introducingitem
d
so
i
n
ffi
a
c
li
u
z
l
a
ty
tio
t
n
o
:
t
1
h
9
e
th
kn
In
o
t
w
er
l
n
e
a
d
t
g
io
e
n
t
a
r
l
a
C
ci
o
n
n
g
fe
m
re
o
n
d
ce
e
,
l.
U
I
M
n
A
U
P
se
2
r
0
M
11
o
,
d
G
el
i
i
r
n
on
g,
a
A
,S
d
p
a
a
p
i
t
n
i
,
o
J
n
u
a
ly
nd
11
P
-
e
1
r
5
-
,
L𝑙𝑡 =Softplus(E𝑆(𝑙 𝑡 ′)), (26)
2011.Proceedings19.Springer,243–254.
[22] ChrisPiech,JonathanBassen,JonathanHuang,SuryaGanguli,MehranSahami, whereE𝑆 :{0,1,...,100}→R𝑑 isalearnableembeddingfunction
LeonidasJGuibas,andJaschaSohl-Dickstein.2015. Deepknowledgetracing.
thatmapstheintegerindextoavector.
7386

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
Table5:GradingCriteriaandInstructionsforProgrammingCodeAssessment
TaskDescription
Youareahelpfulassistant.Iwillprovideaprogrammingproblemdescription,apieceofcodewrittenbyastudent,andthecode’sID.Now,youneed
togradethiscodeonascalefrom0to50.
RawData
ProblemRequirements:{requirement}
CodeID:{code_id}
GradingCriteria
0-10points:Thestudenthasnotsolvedtheproblematall.
10-20points:Thestudenthasnotsuccessfullysolvedtheproblembutmadeareasonableattempt.
20-30points:Thestudenthasnotsuccessfullysolvedtheproblem,butthecodecontainslogicthatalignswiththerequirementsoftheproblem.
30-40points:Thestudenthasnotfullysolvedtheproblem,buttheirsolutionisveryclosetothecorrectanswer,withonlyminormissingsyntax
details.
40-50points:Thestudenthasfullysolvedtheproblemcorrectly.
ConsideringFactors
1.Codestyle,
2.Whethervariablenamesarereasonable,
3.Whetherthereareunusedvariables,
4.Whetherthereareunreachablecodeblocks.
OtherNotes
YourreturnformatmustbeinJSONformat,wherethekeyisthecodeIDandthevalueisthescoreforthecode!Yourresponseshouldbeasaccurate
aspossible(like21,24,31,38),ratherthansimplytakingtheminimum,middle,ormaximumvalueofeachlevel(like10,15,20...)!
Table6:PromptTemplateUsedinCodeAnalysisforGeneratingReasonVectors
TaskDescription
Youareacodeanalyzer.Ihaveaprogrammingproblemthatincludesthestudent’sanswer,thecorrectnessscoreofthestudent’sanswer(0-50),theID
oftheprogrammingproblem,andthenumberoferrorsinthecode.Youneedtoanalyzethestudent’ssubmittedcodefrombothlogicalandsyntactic
dimensionsbasedontheproblemdescriptionandgenerateareason_vector.
RawDatawithScore
CodeID:{id}
Requirement:{requirement}
Score:{score}
SubmittedCode:{code}
NumberofErrors:{error_num}
RulesforReasonVector
Thereason_vectorhasfivedimensions,withtwocorrectnessattributesandthreeerrorattributesinthefollowingorder:logicalcorrectness,syntactic
correctness,carelesssyntaxmistakes,syntaxerrorsduetolackofproficiency,andlogicalerrors.Thereason_vectorcantakethefollowingvalues:
1.Ifthecode’sscoreis50,thereason_vectormustbe:[1,1,0,0,0].
2.Ifthecode’sscoreisnot50andthenumberoferrorsinthecodeis0,thereason_vectormustbe:[0,1,0,0,1].
3.Ifneitheroftheaboveconditionsismet,youmustanalyzethestudent’serrorsanddeterminethereason,asfollows:
a.Ifyoubelievethestudent’scodeislogicallycorrectbuthassyntaxmistakesduetocarelessness,thereason_vectorshouldbe:[1,0,1,0,0].
b.Ifyoubelievethestudent’scodeislogicallycorrectbuthaserrorsduetolackofproficiencyinsyntax,thereason_vectorshouldbe:[1,0,0,1,0].
c.Ifyoubelievethestudent’scodehaslogicalerrorsandalsocarelesssyntaxmistakes,thereason_vectorshouldbe:[0,0,1,0,1].
d.Ifyoubelievethestudent’scodehaslogicalerrorsandsyntaxerrorsduetolackofproficiency,thereason_vectorshouldbe:[0,0,0,1,1].
OtherNotes
TheresponsemustbeinJSONformat:{{“id”:reason_vector}}(e.g.,{{“3”:[1,1,0,0,0]}})andnonewlineinthevector!
7387

Multi-LevelProgrammingKnowledgeTracingEnhancedbyLLM WWW’26,April13–17,2026,Dubai,UnitedArabEmirates
B.2 ReasonEmbedding whereQ𝑞𝑡 ∈R𝑑,C𝑐𝑡 ∈R𝑑,QC𝑞𝑡 ∈R𝑑.Thus,weobtainaunified
Errorcauseembeddingscapturetheinfluenceofdifferenterror embeddingrepresentationfortheproblem-concept,incorporating
typesinstudentresponses,categorizedintofiveclasses:logical informationabouttheproblemitselfanditscoveredconcepts.
correctness,syntacticcorrectness,carelessness,lackofproficiency,
|     |     |     |     |     |     |     | C EXPERIMENTS |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
andlogicalerrors.Wedefinefivelearnableembeddingvectors,each
ofdimension𝑑:
|                           |     |     |     |                                 |     |     | C.1 Datasets |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------------- | --- | --- | ------------ | --- | --- | --- |
| • Logicalcorrectness:𝑅cor |     |     |     | ∈R𝑑,initializedwithpositiveval- |     |     |              |     |     |     |
WeevaluatedtheperformanceofMIE+MLPKTonfourcommonly
log
ues.
| Syntacticcorrectness:𝑅cor |     |     |     | R𝑑,initializedwithpositive |     |     | usedpublicdatasets:                             |     |     |     |
| ------------------------- | --- | --- | --- | -------------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| •                         |     |     |     | ∈                          |     |     |                                                 |     |     |     |
|                           |     |     | syn |                            |     |     | •                                               |     |     |     |
| values.                   |     |     |     |                            |     |     | SecondCSEDMDataChallenge:Thisisanotherchallenge |     |     |     |
• Carelessness:𝑅care ∈R𝑑,initializedasazerovector. datasetinthefieldofprogrammingeducation.Itcomprises
syn
proficiency:𝑅prof R𝑑, codesubmissionsfromstudentsaddressing50programming
| • Lack | of  |     |     | ∈   | initialized with | negative |                                                  |     |     |     |
| ------ | --- | --- | --- | --- | ---------------- | -------- | ------------------------------------------------ | --- | --- | --- |
|        |     |     | syn |     |                  |          | problems.Thedatasetincludesdatafrombothspringand |     |     |     |
values.
fallsemesters,witheachsemestercorrespondingtodistinct
| • Logicalerror:𝑅err |     |     | ∈R𝑑,initializedwithnegativevalues. |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
log
studentcohorts.Consequently,wedivideditintotwoinde-
| Fortheerrorcauseindicatortensorr𝑡 |     |     |     |     | ∈R5,whereeach𝑟 | ∈   |                                                   |     |     |     |
| --------------------------------- | --- | --- | --- | --- | -------------- | --- | ------------------------------------------------- | --- | --- | --- |
|                                   |     |     |     |     |                | 𝑡,𝑘 | pendentdatasets:Code-SandCode-F.Theproblemsinthis |     |     |     |
{0,1}(𝑘 =0to4)indicatesthepresenceofthe𝑘-therrortypein
datasetaregenerallystraightforward,andthus,weclassify
theaforementionedorder,thelogic-relatedandconcept-related Code-SandCode-Fasnovice-leveldatasets.
embeddingsarecomputedas: • BePKT:Thisisacomprehensivedatasetforprogramming
knowledgetracinginthefieldofprogrammingeducation.It
|     |     | =𝑟  | ·𝑅  | c o r+𝑟 | ·𝑅 e r r |     |     |     |     |     |
| --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- |
R log,𝑡 𝑡,0 l o g 𝑡,4 l o g (27) comprisesvariousonlinebehaviorsfromstudents,including
codesubmissions,compilations,andinteractionsinanonline
R =𝑟 ·𝑅 c o r +𝑟 ·𝑅 c a re+𝑟 ·𝑅 p r of (28) judgesystemacrossmultipleprogrammingproblems.The
|     | con,𝑡 | 𝑡,1 | s y n | 𝑡,2 s y | n 𝑡,3 s y n |     |     |     |     |     |
| --- | ----- | --- | ----- | ------- | ----------- | --- | --- | --- | --- | --- |
datasetcapturesdetailedstudentactivitiesfromalargeco-
B.3 Question-ConceptWeightedEmbedding hort.Givenitsfocusonbehavioralpatternsandknowledge
Problem-conceptweightedembeddingsintegrateproblemandcon- tracing,weclassifyBePKTasanadvanced-leveldataset.
ceptfeaturestoemphasizetheirassociations.Giventhelearnable
|                     |     | ∈R𝑑 |                               |     |     |     | C.2 DescriptionsofBaselines |     |     |     |
| ------------------- | --- | --- | ----------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
| problemembeddingQ𝑞𝑡 |     |     | fromtheproblemembeddingmatrix |     |     |     |                             |     |     |     |
andtheconceptembeddingC𝑐𝑡,𝑗 ∈ R𝑑 foreachrelatedconcept ThedetailedinformationoftheBaselinesmentionedinSection
| 𝑗 =1to𝐾 | (fromalearnableconceptembeddingmatrix,where𝐾 |     |     |     |     |     | 6.1.2isasfollows: |     |     |     |
| ------- | -------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
isthemaximumnumberofconceptsperproblem),theassociation • AKT[9]:Modelsstudentforgettingusingcontext-aware
|     | problem𝑞 |     |     | concept𝑐 |     |     |     |     |     |     |
| --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
score between 𝑡 and 𝑡,𝑗 is computed via dot attentionmechanisms.
product:
• DTransformer[32]:Employscontrastivelearningtotrack
stablestudentknowledgestates.
𝑑𝑝
|     |               |     |     | ∑︁   |             |      | • EXKT[16]:Extendsknowledgetracingwithenhancedques- |     |     |     |
| --- | ------------- | --- | --- | ---- | ----------- | ---- | --------------------------------------------------- | --- | --- | --- |
|     | raw_scores𝑡,𝑗 |     | =   | (Q𝑞𝑡 | )𝑖(C𝑐𝑡,𝑗 )𝑖 | (29) |                                                     |     |     |     |
tionandconceptmodeling.
𝑖=1
|                       |     |     |                               |     |     |     | • FlucKT | [11]: Captures cognitive | fluctuations | in student |
| --------------------- | --- | --- | ----------------------------- | --- | --- | --- | -------- | ------------------------ | ------------ | ---------- |
| Paddedconcepts(i.e.,𝑐 |     |     | =0)aremaskedtoavoidinfluence: |     |     |     |          |                          |              |            |
𝑡,𝑗
knowledgestates.
(cid:40)
if𝑐 ≠0 • FoLiBiKT[12]:Integratesforgettingandlearningbehaviors
|     |     |         |     | 1 𝑡,𝑗       |     |      |                       |     |     |     |
| --- | --- | ------- | --- | ----------- | --- | ---- | --------------------- | --- | --- | --- |
|     |     | mask𝑡,𝑗 | =   |             |     | (30) | intoknowledgetracing. |     |     |     |
|     |     |         |     | 0 otherwise |     |      |                       |     |     |     |
• LefoAKT[5]:RefinesAKTwithimprovedforgettingmodel-
ing.
′
| raw_scores𝑡 | ,𝑗 =raw_scores𝑡,𝑗·mask𝑡,𝑗+(1−mask𝑡,𝑗)·(−∞) |     |     |     |     | (31) | •   |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
SAKT[19]:Usesself-attentiontomodelstudent-concept
| Theassociationscoresarethennormalizedviasoftmax: |     |     |     |     |     |     | interactions. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
• StableKT[15]:Enhancesknowledgetracingforstableper-
|     |     |       | exp(raw_scores′ |     | )    |      |               |                              |     |     |
| --- | --- | ----- | --------------- | --- | ---- | ---- | ------------- | ---------------------------- | --- | --- |
|     |     |       |                 |     | 𝑡 ,𝑗 |      | f o rm an c e | a c r o s s d a t a se t s . |     |     |
|     | 𝑞𝑎  | 𝑡,𝑗 = |                 |     | .    | (32) |               |                              |     |     |
(cid:205)𝐾 exp(raw_scor s′ ) • A T KT [ 1 0 ] : I m p r o v e s g e n eralizationusingadversarialtrain-
|                                                        |     |     | 𝑘=1 |     | e 𝑡,𝑘 |     |      |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- |
| Theweightedconceptembeddingistheattention-weightedsum: |     |     |     |     |       |     | ing. |     |     |     |
• CSKT[4]:Combinescontrastivelearningwithstructural
|     |     |     | 𝐾   |     |     |     | knowledgetracing. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
∑︁
MC𝑞𝑡 = 𝑞𝑎 𝑡,𝑗 ·C𝑐𝑡,𝑗 . (33) • DKT[22]:TracksknowledgestatesusingLSTM-basedre-
|                                                     |     |     | 𝑗=1 |     |     |     | currentnetworks. |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
| Thefinalproblem-conceptembeddingcombinestheweighted |     |     |     |     |     |     | •                |     |     |     |
DKVMN[35]:Utilizesdynamickey-valuememoryforknowl-
| conceptembeddingandtheproblemembedding: |     |     |     |     |     |     | edgetracing. |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
• SKVMN[1]:EnhancesDKVMNwithstructuredknowledge
|     |     | QC𝑞𝑡 | =MC𝑞𝑡 | +Q𝑞𝑡 | ,   | (34) | modeling. |     |     |     |
| --- | --- | ---- | ----- | ---- | --- | ---- | --------- | --- | --- | --- |
7388

WWW’26,April13–17,2026,Dubai,UnitedArabEmirates MingxingShaoetal.
• GRKT[8]:Leveragesgraph-basedstructuresforknowledge Table7:ComparisonofInferenceTimeandPerformance
SignificanceonCode-SDataset
propagation.
| • LPKT | [23]: Models learning | progress with | fine-grained |     |     |     |     |     |     |
| ------ | --------------------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- |
knowledgetracing. Model TestTime(ms/batch) RMSE p-value(vsOurs) AUC
• DKT+[26]:Usesabstractsyntaxtrees(AST)[3,14]torepre- LPKT 106.43 0.2043 1.83×10−6 0.8600
sentprogramsandusesrecurrentneuralnetworkstotrack Code-DKT 410.21 0.1952 2.59×10−5 0.8845
|     |     |     |     | GRKT |     | 1112.41 | 0.1987 | 1.54×10−5 | 0.8688 |
| --- | --- | --- | --- | ---- | --- | ------- | ------ | --------- | ------ |
learners’knowledgestates.
|     |     |     |     | MIE+MLPKT(Ours) |     | 1049.21 | 0.1904 |     | - 0.8926 |
| --- | --- | --- | --- | --------------- | --- | ------- | ------ | --- | -------- |
• Code-DKT[24]:ConstructstheASTandadoptsbothnode
| embedding | and path embedding | to effectively | model the |                 |     |     |             |     |                 |
| --------- | ------------------ | -------------- | --------- | --------------- | --- | --- | ----------- | --- | --------------- |
|           |                    |                |           | ★ Logic Correct |     | ★   | Logic Error | ●   | Careless Syntax |
problemtext.
• ECKT[33]:Integratescodefeatureswithquestions’knowl- ● Syntax Correct × Lack of Proficiency
Student 1
| edgeconceptsanddescriptionsgeneratedbyanLLMfrom |     |     |     | 5   |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Logic Ability
Syntax Concept Ability
codes.Duetolimitationsintheimplementationmethod,we
4 Problem Ability
| solelyutilizetheconceptsandquestionIDsfromtheoriginal |     |     |     | ytilibA tnedutS | Overall Ability |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --------------- | --------------- | --- | --- | --- | --- |
| datasetsforgeneratingembeddings.                      |     |     |     | 3               |                 |     |     |     |     |
★ ΔT=1.93
|     |     |     |     | 2   | ΔT=0.47 |     |         |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     |     |     |     |         |     | ΔT=0.25 |     | ●   |
|     |     |     |     |     | ★       |     | ★       |     |     |
C.3 CaseStudy(Q4)
|     |     |     |     | 1   | ×   |     | ●   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Q37 |     | Q37 |     | Q37 |
ToinvestigatetheefficacyoftheMIE+MLPKTframeworkintrack-
0
ing students’ knowledge states, we visualized the experimental Student 2
5
| resultsofMIE+MLPKTmonitoringtheknowledgestatechanges |     |     |     |     | Logic Ability |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
Syntax Concept Ability
| of two students | across three | time steps, as illustrated | in Figure | 4   | Problem Ability |     |     |     |     |
| --------------- | ------------ | -------------------------- | --------- | --- | --------------- | --- | --- | --- | --- |
Overall Ability
|                                                        |     |     |     | ytilibA tnedutS |         |     |     |     | ★   |
| ------------------------------------------------------ | --- | --- | --- | --------------- | ------- | --- | --- | --- | --- |
| 7.Thefollowingobservationscanbedrawnfromtheresults:(1) |     |     |     | 3               |         |     | ★   |     |     |
|                                                        |     |     |     |                 | ΔT=0.55 |     |     |     | ×   |
SyntacticConceptAbility:Whenthefirststudent,atthefirst ● ΔT=0.27
ΔT=2.73
| timestep,commitsanerrorduetoinsufficientsyntacticproficiency |     |     |     | 2   |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (denotedbya×inFigure7),themodel’sassessmentoftheirsyn-       |     |     |     |     | ★   |     |     |     |     |
1
tacticabilitydecreases.Conversely,whenthefirststudentmakes × Q24 Q24
Q24
anerrorduetocarelessnessatthesecondtimestep(indicatedbya 0 Performance Score Comparison
●inFigure7),theirsyntacticconceptproficiencyimproves.This
|     |     |     |     | 1.0 | Student 1 Predicted | Student 2 Predicted |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | ------------------- | --- | --- | --- |
isattributedtothefactthaterrorsstemmingfromcarelessnessare Student 1 True Student 2 True
0.8
typicallyrectifiedquickly,leadingthemodeltointerpretthisinter-
actionascontributingtoanenhancementinthestudent’ssyntactic
erocS 0.6
concepts.Furthermore,whenthefirststudentcorrectlyanswers
| questionQ37(markedbya●inFigure7),theirsyntacticconcept |     |     |     | 0.4 |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proficiencyexhibitsasignificantimprovement.(2)ProblemUn-
0.2
derstandingAbility:Asbothstudentsrepeatedlyengagewiththe
sameproblem,theirunderstandingofthatproblemprogressively T1 T2 T3
Timestep
increases.(3)LogicalAbility:WhentheMIEframeworkevaluates
aninteractionaslogicallycorrect(indicatedbya★inFigure7), Figure7:TheProcessofMIE+MLPKTinTrackingStudents’
KnowledgeStates
themodel’sassessmentofthestudent’slogicalreasoningability
typicallyimproves.Incontrast,whenaninteractionisevaluated
aslogicallyincorrect(denotedbya★inFigure7),themodel’s
|     |     |     |     | it is notably | more | efficient | than the complex | graph-based | base- |
| --- | --- | --- | --- | ------------- | ---- | --------- | ---------------- | ----------- | ----- |
assessmentofthestudent’slogicalreasoningabilitydecreases.(4)
lineGRKT(1112.41ms).Consideringthesubstantialimprovement
ImpactofTimeIntervals:Whenthetimeintervalislessthan inpredictiveaccuracy(RMSEreducedto0.1904),webelievethis
𝜙 =2.57,students’variousabilitiestendtoimproveduringthat
floor computationalcostisacceptableforreal-worldapplications.
| period.Conversely,whenthetimeintervalexceeds𝜙 |     |     | ,students’ |                                                         |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ---------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                               |     |     | floor      | SignificanceandRobustness:Tofurthervalidatethereliabil- |     |     |     |     |     |
abilitiesarelikelytodeclineduringthatperiod.
ityoftheseperformancegains,weconductedsignificancetests.As
presentedinTable7,thelowp-valuesconfirmthatourimprove-
mentsarestatisticallysignificant.Additionally,weintroducedthe
C.4 EfficiencyandRobustnessAnalysis(Q5)
AUCmetric(binarizedat0.5),whereourmodelachieved0.8926,
Toevaluatethepracticaldeployabilityofourmethod,weconducted
consistentlyoutperformingallbaselines.
acomparativeanalysisofinferencetimeandperformancetrade-
offs,asshowninTable7.
InferenceEfficiency:Theresultsindicatethattheinference
timeofMIE+MLPKTis1049.21ms/batch.Whileourmodelrequires
morecomputationtimethanlightweightmodelslikeCode-DKT
(410.21ms)andLPKT(106.43ms)duetoitsmulti-levelarchitecture,
7389