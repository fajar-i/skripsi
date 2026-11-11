Tracing Mathematical Proficiency Through Problem-Solving Processes
|     |             |                           | JungyangPark1,2* |             |             | SuhoKang3* |                                           | JaewooPark1 |             |     |     |     |
| --- | ----------- | ------------------------- | ---------------- | ----------- | ----------- | ---------- | ----------------------------------------- | ----------- | ----------- | --- | --- | --- |
|     | JaehongKim2 |                           |                  | JaewooShin2 |             |            | SeonjoonPark2                             |             | YoungjaeYu3 |     |     |     |
|     |             | 1YonseiUniversity         |                  |             | 2Mathpresso |            | 3SeoulNationalUniversity                  |             |             |     |     |     |
|     |             | wjddid000624@yonsei.ac.kr |                  |             |             |            | youngjaeyu@snu.ac.kr                      |             |             |     |     |     |
|     |             | Abstract                  |                  |             |             |            | KnowledgeTracing(BKT)(CorbettandAnderson, |             |             |     |     |     |
1994)andItemResponseTheory(IRT)(GreenJr,
| Knowledge | Tracing |     | (KT) aims | to  | model | stu- |     |     |     |     |     |     |
| --------- | ------- | --- | --------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
6202 peS 7  ]GL.sc[  3v11300.2152:viXra 1951),introducedinterpretableprobabilisticframe-
dent’sknowledgestateandpredictfutureper-
|          |           |     |              |          |     |     | works | but struggled | to represent |     | complex | learn- |
| -------- | --------- | --- | ------------ | -------- | --- | --- | ----- | ------------- | ------------ | --- | ------- | ------ |
| formance | to enable |     | personalized | learning |     | in  |       |               |              |     |         |        |
ingbehaviorduetosimplifyingassumptions(e.g.
| Intelligent | Tutoring |     | Systems. | However, |     | tra- |                      |     |     |        |                   |     |
| ----------- | -------- | --- | -------- | -------- | --- | ---- | -------------------- | --- | --- | ------ | ----------------- | --- |
|             |          |     |          |          |     |      | , skill independence |     | and | coarse | latent dynamics). |     |
ditionalKTmethodsfacefundamentallimita-
tions in explainability, as they rely solely on Withtheadventofneuralnetworks,deeplearning-
basedKT(DLKT)modelshavedemonstratedno-
| the response |     | correctness, | neglecting |     | the rich |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
information embedded in students’ problem- table improvements by employing architectures
| solvingprocesses. |     | Toaddressthisgap,wepro- |     |     |     |     |         |           |        |          |        |         |
| ----------------- | --- | ----------------------- | --- | --- | --- | --- | ------- | --------- | ------ | -------- | ------ | ------- |
|                   |     |                         |     |     |     |     | such as | recurrent | neural | networks | (Piech | et al., |
poseKnowledgeTracingLeveragingProblem-
|     |     |     |     |     |     |     | 2015; Nagatani |     | et al., 2019) | and | attention | mech- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | --------- | ----- |
SolvingProcess(KT-PSP),whichincorporates
|     |     |     |     |     |     |     | anisms | (Pandey | and Karypis, | 2019; | Ghosh | et al., |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------ | ----- | ----- | ------- |
students’problem-solvingprocessestocapture
|     |     |     |     |     |     |     | 2020). | Beyond | architectural | innovations, |     | subse- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------------- | ------------ | --- | ------ |
themultidimensionalaspectsofmathematical
proficiency. We also introduce KT-PSP-25, quent studies have further enriched KT models
|       |         |              |     |          |     |     | byintegratingdiversecontextualsignals, |     |     |     |     | suchas |
| ----- | ------- | ------------ | --- | -------- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ------ |
| a new | dataset | specifically |     | designed | for | KT- |                                        |     |     |     |     |        |
PSP.Buildingonthis,wepresentStatusKT,a item difficulty (Yeung, 2019; Chen et al., 2023),
KTframeworkthatemploysateacher-student- andknowledgeconceptstructure(Suetal.,2021),
| teacher   | three-stage  |     | LLM pipeline |     | to extract |     |         |           |       |             |     |            |
| --------- | ------------ | --- | ------------ | --- | ---------- | --- | ------- | --------- | ----- | ----------- | --- | ---------- |
|           |              |     |              |     |            |     | thereby | enhancing | their | performance |     | and inter- |
| students’ | Mathematical |     | Proficiency  |     | (MP)       | as  |         |           |       |             |     |            |
pretability.
| intermediate | representation. |     |     | In this | pipeline, |     |          |     |                 |     |            |       |
| ------------ | --------------- | --- | --- | ------- | --------- | --- | -------- | --- | --------------- | --- | ---------- | ----- |
|              |                 |     |     |         |           |     | Although |     | KT has advanced |     | in various | ways, |
theteacherLLMfirstextractsproblem-specific
mostapproachesrelyheavilyonoutcome-centric
proficiencyindicators,thenastudentLLMgen-
supervision(e.g.,Correctness)andlimitedcontex-
eratesresponsesbasedonthestudent’ssolution
process, and a teacher LLM evaluates these tualmetadata(e.g.,KnowledgeConcepts(KCs),
responses to determine mastery of each indi- problem-responsetime,anddifficulty),whichof-
cator. TheexperimentalresultsonKT-PSP-25 tenfailtoreflectstudents’underlyingunderstand-
| demonstrate | that | StatusKT |     | improves | the pre- |     |     |     |     |     |     |     |
| ----------- | ---- | -------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
ing(WangandHeffernan,2012;Tschisgaleetal.,
| diction | performance |     | of existing | KT  | methods. |     |                                 |     |     |     |             |     |
| ------- | ----------- | --- | ----------- | --- | -------- | --- | ------------------------------- | --- | --- | --- | ----------- | --- |
|         |             |     |             |     |          |     | 2025;Yeung,2019;Liuetal.,2024). |     |     |     | Incontrast, |     |
Moreover,StatusKTprovidesinterpretableex-
asshowninFigure1(b),real-worldteachersevalu-
planationsforitspredictionsbyexplicitlymod-
atestudents’understandingthroughtheproblem-
| elingstudents’mathematicalproficiency. |     |     |     |     | Code |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
isavailablehere. solvingprocess(Chiuetal.,2022;Tschisgaleetal.,
|                |     |     |     |     |     |     | 2025;Kleinmanetal.,2022).                   |     |     | Nevertheless,despite |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | -------------------- | --- | --- |
| 1 Introduction |     |     |     |     |     |     | theimportanceofthesolutionprocess,currentKT |     |     |                      |     |     |
approachesanddatasetsremainunderexploredfor
KnowledgeTracing(KT)isatechniquethatmodels
incorporatingit(Fengetal.,2009;Liuetal.,2023b;
alearner’sevolvingknowledgestateovertime(Cor-
Kimetal.,2025).
| bettandAnderson,1994;Liuetal.,2025). |     |     |     |     |     | Since |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Toaddressthislimitation,weproposeKNOWL-
| the true knowledge |     | state | cannot | be  | observed | di- |              |     |                      |     |     |      |
| ------------------ | --- | ----- | ------ | --- | -------- | --- | ------------ | --- | -------------------- | --- | --- | ---- |
|                    |     |       |        |     |          |     | EDGE TRACING |     | WITH PROBLEM-SOLVING |     |     | PRO- |
rectly,KTinsteadpredictsfuturecorrectnessfrom
|     |     |     |     |     |     |     | CESS (KT-PSP), |     | a new | formulation |     | of the KT |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----------- | --- | --------- |
historicalinteractiondata,asillustratedinFigure
taskthatexplicitlyincorporatesstudents’problem-
| 1 (a). Early | KT  | approaches, |     | such | as Bayesian |     |         |           |       |          |             |     |
| ------------ | --- | ----------- | --- | ---- | ----------- | --- | ------- | --------- | ----- | -------- | ----------- | --- |
|              |     |             |     |      |             |     | solving | processes | (PSP) | into the | interaction | se- |
*EqualContribution. quence. TofacilitateresearchonKT-PSP,wein-
1

lationthatincorporatesstudents’PSPintothe
interactionsequence,enablingprocess-aware
modelingofknowledge.
|     |     |     |     |     | • Werelease |     | KT-PSP-25,anewmathematical |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --- | -------------------------- | --- | --- | --- | --- |
KTdatasetcontainingreal-worldPSPforeach
student-probleminteraction.
|     |     |     |     |     | • We | propose | STATUSKT, |     | a novel | KT  | frame- |
| --- | --- | --- | --- | --- | ---- | ------- | --------- | --- | ------- | --- | ------ |
workthatextractsMPsignalsfromstudents’
|     |     |     |     |     | PSP | through | teacher-student-teacher |     |     |     | LLM |
| --- | --- | --- | --- | --- | --- | ------- | ----------------------- | --- | --- | --- | --- |
pipelineandintegratesthemasauxiliaryrep-
resentationsforKT.
|     |     |     |     |     | • Experimentson |     | KT-PSP-25 |     |     | showthat | STA- |
| --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | --- | -------- | ---- |
TUSKTconsistentlyimprovespredictionper-
formanceoverDLKTbaselineswhileprovid-
inginterpretableMP-alignedsignals.
2 RelatedWorks
| Figure 1:     | (a) Conventional |                   | KT utilizes | limited meta- |     |     |     |     |     |     |     |
| ------------- | ---------------- | ----------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| data, lacking |                  | interpretability. | (b) By      | incorporating |     |     |     |     |     |     |     |
2.1 KnowledgeTracing
problemcontext,students’reasoning,andteachercom-
ments, STATUSKT capturesgranularproficiencysig- KTplaysacrucialroleinintelligenttutoringsys-
nalsalignedwithteachers’assessment
temsbyestimatingstudents’evolvingknowledge
|     |     |     |     |     | states from | their | interaction |     | histories. |     | A com- |
| --- | --- | --- | --- | --- | ----------- | ----- | ----------- | --- | ---------- | --- | ------ |
troduce KT-PSP-25,anoveldatasetthatcontains
monlineofworkinfersconceptmasteryinanau-
| real-world | PSPfor | each | student-probleminterac- |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
toregressivemannerusingpastquestion-response
tion.
data(Piechetal.,2015;YeungandYeung,2018;
| Building | upon | this | dataset, we introduce | STA- |          |         |       |     |         |       |      |
| -------- | ---- | ---- | --------------------- | ---- | -------- | ------- | ----- | --- | ------- | ----- | ---- |
|          |      |      |                       |      | Nagatani | et al., | 2019; | Guo | et al., | 2021; | Zhou |
TUSKT,aprocess-awareKTframeworkthatusesa
|     |     |     |     |     | etal.,2025). | Memory-augmentedmodelsfurther |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | ----------------------------- | --- | --- | --- | --- | --- |
three-stageLLMpipelinetoextractstudents’Math-
|     |     |     |     |     | encode concepts |     | using | a static | key | memory | for |
| --- | --- | --- | --- | --- | --------------- | --- | ----- | -------- | --- | ------ | --- |
ematicalProficiency(MP)fromtheirPSPanduse
|            |                                    |        |              |         | soft attention    |     | and a dynamic |       | value  | memory | to      |
| ---------- | ---------------------------------- | ------ | ------------ | ------- | ----------------- | --- | ------------- | ----- | ------ | ------ | ------- |
| it as an   | intermediate                       | signal | for modeling | student |                   |     |               |       |        |        |         |
|            |                                    |        |              |         | update students’  |     | knowledge     |       | states | (Zhang | et al., |
| knowledge. | InspiredbyEl-Sharaetal.(2025),STA- |        |              |         |                   |     |               |       |        |        |         |
|            |                                    |        |              |         | 2017; Abdelrahman |     | and           | Wang, | 2019). |        | Graph-  |
TUSKT adoptsateacher-student-teacherstructure:
|     |     |     |     |     | based approaches |     | (Nakagawa |     | et al., | 2019; | Yang |
| --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | ------- | ----- | ---- |
ateacherLLMderivesproblem-specificMPindi-
|     |     |     |     |     | et al., 2020) | capture |     | the structural |     | relations | be- |
| --- | --- | --- | --- | --- | ------------- | ------- | --- | -------------- | --- | --------- | --- |
cators,astudentLLManswersthembasedonthe
|     |     |     |     |     | tween questions |     | and KCs, | propagating |     | historical |     |
| --- | --- | --- | --- | --- | --------------- | --- | -------- | ----------- | --- | ---------- | --- |
students’writtenPSP,andateacherLLMevaluates
|               |     |            |             |          | information | via | graph | updates. | Attention-based |     |     |
| ------------- | --- | ---------- | ----------- | -------- | ----------- | --- | ----- | -------- | --------------- | --- | --- |
| these answers |     | to produce | MP signals. | These MP |             |     |       |          |                 |     |     |
KTapproaches(PandeyandKarypis,2019;Choi
| signals | are then | integrated | into the | KT backbone |     |     |     |     |     |     |     |
| ------- | -------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
etal.,2020a;Ghoshetal.,2020;Liuetal.,2023a;
asauxiliaryinputstoimprovepredictiveaccuracy
|                      |     |                        |     |     | Li etal., | 2024) | improve | predictionby |     | selectively |     |
| -------------------- | --- | ---------------------- | --- | --- | --------- | ----- | ------- | ------------ | --- | ----------- | --- |
| andinterpretability. |     | ExperimentsonKT-PSP-25 |     |     |           |       |         |              |     |             |     |
focusingoninformativepastinteractions.
demonstrateconsistentimprovementsoverstrong
Despitetheseadvances,KTmodelsremainsen-
DLKTbaselinesandfurtheralleviatethecold-start
|     |     |     |     |     | sitive to | noisy | behavioral | traces. |     | Therefore, | re- |
| --- | --- | --- | --- | --- | --------- | ----- | ---------- | ------- | --- | ---------- | --- |
problembyprovidinginformativeMPsignalseven
|                      |     |                            |     |     | cent studies | have | separated |     | stable | cognitive | pat- |
| -------------------- | --- | -------------------------- | --- | --- | ------------ | ---- | --------- | --- | ------ | --------- | ---- |
| inearlyinteractions. |     | Inadditiontoahigherpredic- |     |     |              |      |           |     |        |           |      |
ternsfromanomalousoutcomes,suchasslips(Guo
| tive accuracy, |     | STATUSKT | provides | interpretable |                |          |     |     |              |     |        |
| -------------- | --- | -------- | -------- | ------------- | -------------- | -------- | --- | --- | ------------ | --- | ------ |
|                |     |          |          |               | et al., 2025). | However, |     | key | determinants |     | remain |
proficiencysignalsthatofferfine-grainedinsights
underexplored,mostnotablystudents’PSPandthe
intostudents’learningprogress.
|     |     |     |     |     | MPtheyreveal. |     | Accordingly,weproposeamethod |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | ---------------------------- | --- | --- | --- | --- |
Themajorcontributionsofthispaperareasfol-
|     |     |     |     |     | that leverages |     | fine-grained | signals |     | from students’ |     |
| --- | --- | --- | --- | --- | -------------- | --- | ------------ | ------- | --- | -------------- | --- |
lows:
PSPtoinfertheirMP(Findelletal.,2001;Sullivan,
• Weintroduce KT-PSP,anewKTtaskformu- 2011),therebyenhancingknowledgetracing.
2

2.2 KnowledgeTracingDataset students’ understanding (Ukobizaba et al., 2021;
Chiuetal.,2022;Tschisgaleetal.,2025;Kleinman
TheASSISTmentsdatasets(Fengetal.,2009;Par-
etal.,2022).
dosetal.,2014)servedasearlylarge-scaledatasets
Toovercomethelimitationsofbinaryoutcomes,
| forKTmodels. |     | Subsequentdatasets,suchasJunyi |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recentstudieshaveattemptedtoincorporateauxil-
| 2015                                    | (Chang | et  | al., 2015), | extended | this | line of |                                 |     |     |     |              |     |
| --------------------------------------- | ------ | --- | ----------- | -------- | ---- | ------- | ------------------------------- | --- | --- | --- | ------------ | --- |
|                                         |        |     |             |          |      |         | iaryinformationintotheKTmodels. |     |     |     | Forinstance, |     |
| researchbyleveragingonlinelearninglogs. |        |     |             |          |      | Inpar-  |                                 |     |     |     |              |     |
responsetimehasbeenwidelyusedtodistinguish
allel,researchersbegantoevaluatestudents’perfor-
manceratherthancorrectnessalone,asreflectedin between guessing and slipping behaviors (Wang
|     |     |     |     |     |     |     | and Heffernan, | 2012; |     | Chen et | al., 2022; | Huang |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | --- | ------- | ---------- | ----- |
initiativessuchastheKDDCup2010(KDD2010,
|     |     |     |     |     |     |     | etal.,2024). | Othershaveintegratedquestiondiffi- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------- | --- | --- | --- | --- |
2010). However,mostearlydatasetscontainedonly
cultyortextualcontenttobetterestimatetheprob-
simplequestion-answersequences,offeringlittle
|                       |     |        |                         |     |       |          | ability                         | of correctness |     | based on | item characteris- |     |
| --------------------- | --- | ------ | ----------------------- | --- | ----- | -------- | ------------------------------- | -------------- | --- | -------- | ----------------- | --- |
| auxiliaryinformation. |     |        | Overtime,KTdatasetshave |     |       |          |                                 |                |     |          |                   |     |
|                       |     |        |                         |     |       |          | tics(Yeung,2019;Liuetal.,2024). |                |     |          | Althoughthese     |     |
| expanded              |     | beyond | mathematics             | to  | other | domains, |                                 |                |     |          |                   |     |
approachesenrichthecontext,theylargelyrelyon
| such | as English, |     | computer | science, | engineering, |     |     |     |     |     |     |     |
| ---- | ----------- | --- | -------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
andearlychildhoodeducation(Choietal.,2020b; metadataorstaticattributes,treatingtheactualPSP
asablackbox.
Abdelrahmanetal.,2022;Kimetal.,2025),moti-
|     |     |     |     |     |     |     | Therefore,wepropose |     |     | KNOWLEDGE |     | TRACING |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --------- | --- | ------- |
vatingrichermultimodalandcross-domainlearn-
|              |     |                                   |     |     |     |     | WITH PROBLEM-SOLVING |     |     | PROCESS |     | (KT-PSP), |
| ------------ | --- | --------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | ------- | --- | --------- |
| ingdatasets. |     | RecenteffortsbyLiuetal.(2023b)in- |     |     |     |     |                      |     |     |         |     |           |
whichextendsthetraditionalKTparadigmbyin-
corporatedquestioncontent,answerexplanations,
corporatingstudents’PSPintotheinteractionhis-
| and                      | hierarchical |     | KC structures | to  | support | a more |               |     |     |     |     |     |
| ------------------------ | ------------ | --- | ------------- | --- | ------- | ------ | ------------- | --- | --- | --- | --- | --- |
|                          |              |     |               |     |         |        | torysequenceS |     | :   |     |     |     |
| comprehensiveevaluation. |              |     |               |     |         |        |               | new |     |     |     |     |
However,students’PSPremainslargelyabsent,
|     |     |     |     |     |     |     | S new = | {(q 1 ,c 1 | ,r 1 ,p | 1 ),...,(q | t ,c t ,r | t ,p t )}, (2) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------- | ---------- | --------- | -------------- |
particularlyinmathematicalproblems,whereitis
difficulttocaptureatscale. Tobridgethisgap,we where p denotes the detailed PSP for ques-
t
constructedthefirstdatasetthatexplicitlyrecorded
|     |     |     |     |     |     |     | tion q | , including | step-by-step |     | reasoning, | in- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ------------ | --- | ---------- | --- |
t
PSP.
|     |     |     |     |     |     |     | termediate                               | computations, |     | or other | process-level |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | ------------- | --- | -------- | ------------- | --- |
|     |     |     |     |     |     |     | traces. TheobjectiveremainsestimatingP(r |               |     |          |               | =   |
t+1
| 3   | KNOWLEDGE       |     | TRACING |         | WITH |     |       |         |          |     |            |      |
| --- | --------------- | --- | ------- | ------- | ---- | --- | ----- | ------- | -------- | --- | ---------- | ---- |
|     |                 |     |         |         |      |     | 1 | q | , c , S | ), while | now | leveraging | both |
|     |                 |     |         |         |      |     | t+1   | t+1     | new      |     |            |      |
|     | PROBLEM-SOLVING |     |         | PROCESS |      |     |       |         |          |     |            |      |
historicalperformanceandtheunderlyingproblem-
| KnowledgeTracing(KT)isataskineducational |     |     |     |     |     |     | solvingstrategies. |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
dataminingthataimstomodelastudent’sknowl-
|     |     |     |     |     |     |     | 4 Dataset |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
edgestateovertimebasedontheirhistoricallearn-
| ing | interactions. |      | The primary | goal | is to  | predict   | 4.1 License |                              |     |     |     |     |
| --- | ------------- | ---- | ----------- | ---- | ------ | --------- | ----------- | ---------------------------- | --- | --- | --- | --- |
| how | a student     | will | perform     | on a | future | question. |             |                              |     |     |     |     |
|     |               |      |             |      |        |           | KT-PSP-25   | isreleasedundertheCCBY-NC4.0 |     |     |     |     |
Formally,givenastudent’sinteractionhistoryse-
(CreativeCommonsAttribution-NonCommercial
| quenceS |     | :    |     |     |     |     |                           |     |     |                         |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | ------------------------- | --- | --- | ----------------------- | --- | --- |
|         |     | conv |     |     |     |     | 4.0International)license. |     |     | Thislicenserestrictsthe |     |     |
datasettononcommercialusewhileallowingmod-
S = {(q ,c ,r ),...,(q ,c ,r )}, (1) ificationsandsharingundersimilarterms. Under
|     | conv |     | 1 1 | 1   | t t t |     |               |        |     |                  |     |        |
| --- | ---- | --- | --- | --- | ----- | --- | ------------- | ------ | --- | ---------------- | --- | ------ |
|     |      |     |     |     |       |     | this license, | others | can | non-commercially |     | remix, |
where q denotes the question at time t, c is adapt, and build upon the work if they credit the
|     |     | t   |     |     |     | t   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the concept associated with q , and r ∈ {0,1} sourceandindicateifchangesweremade.
|     |     |     |     | t   | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representstheresponsecorrectness(1forcorrect,0
|                                           |     |     |     |     |     |     | 4.2 DataConstruction |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
| forincorrect),theobjectiveistoestimateP(r |     |     |     |     |     | =   |                      |     |     |     |     |     |
t+1
| 1|q | ,   | c , S | ).   |     |     |     | Wecurate22,289problem-solvingsessionsfrom |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
|     | t+1 | t+1   | conv |     |     |     |                                           |     |     |     |     |     |
However,relyingsolelyonresponsecorrectness an in-house tablet-based mathematics education
(r )createsasimplifiedproxyforstudents’under- platform. Eachsessioncorrespondstoasinglestu-
t
standing, often failing to capture the nuances of dent working on one problem, with interactions
their actual knowledge state. In real educational recordedbetweenNovember2024andJuly2025.
environments, students areevaluated notonly on To construct the dataset, we applied the follow-
thefinalanswerbutalsoontheirproblem-solving ingpreprocessingsteps: (1)removesessionswith
processes(PSP),whichprovidesricherinsightinto fewer than five handwritten lines and (2) discard
3

Figure2: AnexamplequestionfromKT-PSP-25(problemtextandKCtranslatedintoEnglish). Forshort-
answerquestions,noanswerchoicesareprovided.
|                      |        | basedonGPT-5(OpenAI,2025). |     | Afterinitialtran- |     |
| -------------------- | ------ | -------------------------- | --- | ----------------- | --- |
| Numberofinteractions | 22,289 |                            |     |                   |     |
scription,wefurtherleveragedGPTtoevaluateand
| Numberofstudents | 1,343 |     |     |     |     |
| ---------------- | ----- | --- | --- | --- | --- |
Numberofquestions 2,696 refinetheOCRoutputs,therebyimprovingbothpri-
NumberofKnowledgeComponents 490 vacyprotectionanddataquality. Detailedprompts
anddiscussionofOCRqualityareprovidedinAp-
| Averagesolutionlength(words) | 73.54 |     |     |     |     |
| ---------------------------- | ----- | --- | --- | --- | --- |
pendixD
| AveragePSPlength(words)       | 24.76 |                  |     |     |     |
| ----------------------------- | ----- | ---------------- | --- | --- | --- |
| Averagecorrectratioperstudent | 0.72  | 4.4 DataAnalysis |     |     |     |
| Averagesessionduration        | 60.36 |                  |     |     |     |
Thereare22,289interactions,and1,343students
|     |     | answered 2,696 | problems | from 490 KCs. | On av- |
| --- | --- | -------------- | -------- | ------------- | ------ |
Table1: Statisticsofourdataset
erage,thereferencesolutioncontains73.54words
|     |     | while the | students’ PSP | contains 24.76 | words, |
| --- | --- | --------- | ------------- | -------------- | ------ |
providingsubstantivereasoningtracesratherthan
| problemswithmissingtextualcontent. | Theresult- |     |     |     |     |
| ---------------------------------- | ---------- | --- | --- | --- | --- |
ing dataset, illustrated in Figure 2, encompasses shortanswer-onlylogs.
a wide range of information, including problem- Each record additionally stores both the start
levelattributes(problemID,associatedknowledge andcompletiontimes,enablingthecomputationof
|     |     | response durations | and temporal | analyses | across |
| --- | --- | ------------------ | ------------ | -------- | ------ |
concepts(KCs),problemtext,solutionexplanation,
ground-truthanswer,questiontype,anddifficulty) learning sessions. Questions are assigned to five
andstudentinteractionattributes(selectedanswer, difficulty levels, with most items concentrated
|     |     | around medium | difficulty | (level 50), while | very |
| --- | --- | ------------- | ---------- | ----------------- | ---- |
duration,PSP,andfinalcorrectness).
|     |     | easy (10) | and very hard (90) | items appear | infre- |
| --- | --- | --------- | ------------------ | ------------ | ------ |
4.3 DataPrivacy quently. Summarystatistics,includingtheprocess
length,duration,anddifficultybreakdown,arere-
Beyondtheseattributes,KT-PSP-25alsocontains
portedinTable1.
richrecordsofstudents’interactionsequences,in-
cludingstudentIDs,questionIDs,andhandwritten
5 Methodology
PSP.Sincesuchdatamayexposepersonalinforma-
tion,weimplementedprivacy-preservingmeasures. This section presents the details of the proposed
Student and question IDs were mapped to non- STATUSKT,asillustratedinFigure3. STATUSKT
reversible digital identifiers to ensure anonymity. enhancesknowledgetracingbyexplicitlymodeling
ForhandwrittenPSP,weappliedanOCRpipeline students’mathematicalproficiency(MP)through
4

Figure3: STATUSKT FrameworkOverview. (b)AteacherLLManalyzesthetextandknowledgecomponentsof
eachproblemtoconstructMPindicators,whereasastudentLLMidentifieswhichitunderstandsandcanexplain.
Usingtheseresponses,theteacherLLMintegratestheresultstogenerateanMPratioquantifyingeachstudent’s
MathematicalProficiency(MP).(c)UsingtheMPratio,theKTmodelpredictsbothstudents’futureperformance
andproblem-levelMPratios,offeringastrongrationaleforproficiencyassessment.
interpretable signals derived from their problem- (Figure3(b))toautomaticallyextractMPfromthe
solving process (PSP). While conventional KT rawproblem-solvingprocesses:
models rely on binary correctness, our approach (i). Indicator Extraction(Teacher LLM).
incorporatesstructuredproficiencyevidencegen- Given the problem q and its associated concept
erated from the PSP. Although Findell et al. c, the first Teacher LLM generates a set of MP
| (2001)defineMPascomprisingfivekeystrands– |               |     |     |                 |     |        | indicators: |       |           |             |      |        |
| ----------------------------------------- | ------------- | --- | --- | --------------- | --- | ------ | ----------- | ----- | --------- | ----------- | ---- | ------ |
| conceptual                                | understanding |     |     | (CU), strategic |     | compe- |             |       |           |             |      |        |
|                                           |               |     |     |                 |     |        |             | I q = | f T (q,c) | = {I 1 ,··· | ,I K | }, (3) |
tence(SC),proceduralfluency(PF),adaptiverea-
soning(AR),andproductivedisposition(PD)–we
|     |     |     |     |     |     |     | where | each I | denotes | individual |     | indicators |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ------- | ---------- | --- | ---------- |
k
| focus on | four observable |     |     | dimensions, | excluding |     |         |               |     |           |            |        |
| -------- | --------------- | --- | --- | ----------- | --------- | --- | ------- | ------------- | --- | --------- | ---------- | ------ |
|          |                 |     |     |             |           |     | phrased | as a question |     | targeting | a specific | profi- |
PDbecauseitisdifficulttoassessreliablythrough ciencydimension. Theseindicatorsactasarubric
textualproblem-solvingprocesses. specifyingthereasoningelementsrequiredforthe
problem,guidingthesubsequentanalysis.
5.1 DerivingMPIndicatorsfrom
|     |     |     |     |     |     |     | (ii). | Response | Generation |     | (Student | LLM). |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---------- | --- | -------- | ----- |
Problem-SolvingProcesses
|     |     |     |     |     |     |     | Given | the MP | indicators | I   | and a | student’s |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---------- | --- | ----- | --------- |
q
| The input | to  | our | framework |     | includes | OCR- |     |     |     |     |     |     |
| --------- | --- | --- | --------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
problem-solvingprocessp,theStudentLLMgen-
| transcribed | handwritten |     | solution |     | processes | (Fig- |     |     |     |     |     |     |
| ----------- | ----------- | --- | -------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
eratesresponsesforeachindicator:
| ure 3 | (a)). These |     | traces | contain | interpretable |     |     |     |     |     |     |     |
| ----- | ----------- | --- | ------ | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
signals of students’ reasoning capabilities. Our R = f (I ,p). (4)
k S k
| pipeline | is inspired | by  | the | structured | assessment |     |      |               |          |     |           |        |
| -------- | ----------- | --- | --- | ---------- | ---------- | --- | ---- | ------------- | -------- | --- | --------- | ------ |
|          |             |     |     |            |            |     | This | step converts | implicit |     | reasoning | in the |
protocolinEl-Sharaetal.(2025),inwhichstudents
problem-solvingprocessintoexplicitevidencecor-
| respond | to a set | of predefined |     | MP  | indicators | and |     |     |     |     |     |     |
| ------- | -------- | ------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
respondingtoeachproficiencydimension.
masteryisdeterminedbasedonwhetherthosein-
(iii). ProficiencyAssessment(TeacherLLM).
| dicators | are satisfied. |     | Similarly, |     | our framework |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Finally,thesecondteacherLLMevaluateswhether
| adopts | an indicator-based |     |     | evaluation | paradigm. |     |     |     |     |     |     |     |
| ------ | ------------------ | --- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
eachresponsesatisfiesitscorrespondingindicator,
| However, | because | we  | cannot | rely | on fixed | indi- |     |     |     |     |     |     |
| -------- | ------- | --- | ------ | ---- | -------- | ----- | --- | --- | --- | --- | --- | --- |
producingabinarydecision:
| cators | or direct | student | interviews, |     | we employ | a   |     |     |     |     |     |     |
| ------ | --------- | ------- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
three-stageTeacher-Student-TeacherLLMpipeline E = f (I ,R ), E ∈ {0,1}. (5)
|     |     |     |     |     |     |     |     | k   | T k k | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
5

Basedontheseevaluations,wecomputetheMP • RQ1: Does STATUSKT outperform conven-
Ratioforeachproficiencydimensiondasthepro- tionalDLKTbaselinesandtext-embeddingpro-
| portionofsatisfiedindicators: |     |     |     |     |     | cessbaselines? |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
1
|     |     |     |      | (cid:88) |     | • RQ2:                   | DoesSTATUSKTimproverobustnessun- |     |     |     |     |
| --- | --- | --- | ---- | -------- | --- | ------------------------ | -------------------------------- | --- | --- | --- | --- |
|     | MP  | =   |      | E ,      | (6) |                          |                                  |     |     |     |     |
|     |     | d   | |I | | k        |     |                          |                                  |     |     |     |     |
|     |     |     | d    |          |     | dercold-startconditions? |                                  |     |     |     |     |
k∈I
d
whereI ⊆ I denotesthesubsetofindicators • RQ3: HowdoMPsignalsaffectKTpredictions–
d q
whendotheyhelp,whendotheyhurt,andwhy?
correspondingtodimensiond.
Inallthreestages,weutilizedGPT-5(OpenAI,
6.1 ExperimentSetting
| 2025) model. |              | The specific |             | prompts | used in the |                |     |     |     |     |     |
| ------------ | ------------ | ------------ | ----------- | ------- | ----------- | -------------- | --- | --- | --- | --- | --- |
| pipeline     | are provided |              | in Appendix | E.2,    | and the     | 6.1.1 Baseline |     |     |     |     |     |
humanevaluationprotocolandresultsaresumma- Weevaluatetheperformanceof STATUSKT with
rizedinAppendixE.1. KT models, including DKT (Piech et al., 2015),
DKT+(YeungandYeung,2018),DKVMN(Zhang
5.2 IntegratingMPRatioforInterpretable
|     |     |     |     |     |     | et al., 2017), | SKVMN | (Abdelrahman |     |     | and Wang, |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------ | --- | --- | --------- |
KnowledgeTracing
|     |     |     |     |     |     | 2019), | SAKT (Pandey |     | and | Karypis, | 2019), |
| --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | -------- | ------ |
ThecomputedMPratioservesasaninterpretable
|     |     |     |     |     |     | SAINT | (Choi et al., | 2020a), | AKT | (Ghosh | et al., |
| --- | --- | --- | --- | --- | --- | ----- | ------------- | ------- | --- | ------ | ------- |
intermediaterepresentationthatcomplementsthe
2020),SimpleKT(Liuetal.,2023a),StableKT(Li
traditional KT signals. As depicted in Figure 3 etal.,2024),RobustKT(Guoetal.,2025).
(c), the KT backbone utilizes these ratios to pre- Toisolatetheimpactofincorporatingproblem-
dictboth(i)students’futureperformanceonsub-
solvingprocessinformationwithoutMPmodeling,
sequentproblemsand(ii)problem-levelMPratios, we introduce an additional baseline. In this set-
enabling fine-grained proficiency tracking. This ting,theencodedtextualproblem-solvingprocess
auxiliaryMPpredictionencouragesthemodelto
isconcatenatedwiththeoriginalKTinputfeatures,
internalizeproficiency-relatedpatterns,enhancing
allowingthemodeltoaccessrawprocesssignals
boththepredictiveperformanceandinterpretability withoutexplicitMPreasoning.
beyondwhatcorrectnessaloneprovides.
To train the model to effectively capture these 6.1.2 ImplementationDetails
multidimensionalproficiencysignals,wedefined Thedatasetwassplitbystudentsinto80%fortrain-
a composite loss function. The total loss is a ing/validationand20%fortesting. Toobtainreli-
| weighted | sum | of the | correctness | prediction | loss |     |     |     |     |     |     |
| -------- | --- | ------ | ----------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
ableresultsgiventhelimiteddatasetsize,weper-
andproficiencyregressionloss: formed10-foldcross-validationonthetraining/val-
idationdataandselectedthebestmodelusingearly
(cid:88)
| L = BCE(r |     | ,r )+α |     | MSE(mg | t,mp red), |                                  |       |          |     |           |       |
| --------- | --- | ------ | --- | ------ | ---------- | -------------------------------- | ----- | -------- | --- | --------- | ----- |
|           | gt  | pred   |     |        |            | stoppingwithapatienceof10epochs. |       |          |     | Allmodels |       |
|           |     |        |     |        | i i        |                                  |       |          |     |           |       |
|           |     |        | i∈P |        |            | were trained                     | using | the ADAM |     | optimizer | (Adam |
(7)
etal.,2014)withabatchsizeof16.
| where P | = {CU,SC,PF,AR}, |     |     | r denotes | the re- |     |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
Forthetext-embeddingbaseline,weutilizedthe
sponsecorrectness,andmrepresentstheMPratio
sentence-transformers/all-mpnet-base-v2
| for dimension          |         | i. Hyperparameter |                        | α          | controls the |             |               |                 |                 |     |           |
| ---------------------- | ------- | ----------------- | ---------------------- | ---------- | ------------ | ----------- | ------------- | --------------- | --------------- | --- | --------- |
|                        |         |                   |                        |            |              | model       | to encode     | problem-solving |                 |     | processes |
| trade-off              | between | the               | correctness            | prediction | and          |             |               |                 |                 |     |           |
|                        |         |                   |                        |            |              | and project | the resulting |                 | representations |     | into a    |
| proficiencyestimation. |         |                   | Throughthisdualpredic- |            |              |             |               |                 |                 |     |           |
128-dimensionalvector.
| tionsetup, | STATUSKT |     | improvespredictiveaccu- |     |     |           |          |     |          |            |      |
| ---------- | -------- | --- | ----------------------- | --- | --- | --------- | -------- | --- | -------- | ---------- | ---- |
|            |          |     |                         |     |     | We follow | standard | KT  | training | practices; | full |
racywhileprovidinginterpretableproficiencyas-
hyperparametergridsandimplementationsettings
sessmentsthatalignwiththeestablishedtheories
arelistedinAppendixC.
ofmathematicallearning.
6.1.3 EvaluationMetrics
6 Experiments
|     |     |     |     |     |     | We evaluated | the | model | performance |     | using two |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ----------- | --- | --------- |
Inthissection, weconductedexperimentsonthe standardmetricsinknowledgetracing: (1)Accu-
KT-PSP-25 toevaluateourproposed STATUSKT racy(ACC),whichmeasurestheproportionofcor-
framework. Specifically, we aim to address the rectly predicted student responses, and (2) Area
followingresearchquestions: undertheROCCurve(AUC),whichcapturesthe
6

Method DKT DKT+ DKVMN SKVMN SAKT SAINT AKT simpleKT stableKT robustKT
AUC
Baseline 0.6165 0.6192 0.6049 0.5866 0.5819 0.6201 0.6524 0.6591 0.6735 0.6373
Baseline+PSP 0.6135 0.6169 0.6001 0.6037 0.6074 0.6230 0.6457 0.6465 0.6635 0.6443
STATUSKT 0.6197 0.6200 0.6220 0.6040 0.5854 0.6401 0.6629 0.6639 0.6773 0.6419
ACC
Baseline 0.7219 0.7226 0.7292 0.7189 0.7243 0.7234 0.7396 0.7393 0.7345 0.7370
Baseline+PSP 0.7209 0.7233 0.7359 0.7335 0.7385 0.7326 0.7330 0.7288 0.7219 0.7288
STATUSKT 0.7235 0.7247 0.7410 0.7257 0.7313 0.7377 0.7435 0.7459 0.7421 0.7394
Table2: Resultsofthemainexperiment. WecompareperformanceacrossdiverseKTarchitecturesunderthree
settings: (i)originalbaselines,(ii)text-embeddedPSPvariants(whichconcatenateanencodedproblem-solving
processwiththeKTinputswithoutexplicitMPreasoning),and(iii)theproposedSTATUSKTframework. Bold
indicatesthebestresult,andunderliningindicatesthesecondbest.
DKT DKT+ DKVMN SKVMN SAKT SAINT AKT simpleKT stableKT robustKT
Pairedt-test(p) 0.0003 0.4894 2.47e-07 0.0004 0.0843 9.84e-06 2.27e-05 0.0410 0.0018 0.0489
Cohen’sd 1.7888 0.2279 4.3331 1.7144 0.6135 2.7972 2.5221 0.7539 1.3873 0.7196
Table3: StatisticalsignificanceofAUCimprovements(BaselinevsSTATUSKT)across10-foldcross-validation.
rankingqualityofthepredictedcorrectnessprob- turedindicatorsthatcanbeeffectivelyintegrated
abilities. Following prior KT studies, the AUC withtheinteractionhistory.
was considered theprimary metric becauseof its To verify that these improvements are not ar-
| robustness    | to label | imbalance | across | the | student |                                               |                                  |               |     |     |           |
| ------------- | -------- | --------- | ------ | --- | ------- | --------------------------------------------- | -------------------------------- | ------------- | --- | --- | --------- |
|               |          |           |        |     |         | tifacts                                       | of fold-level                    | fluctuations, |     | we  | conducted |
| interactions. |          |           |        |     |         | pairedt-testsacrossthe10-foldsplits,comparing |                                  |               |     |     |           |
|               |          |           |        |     |         | STATUSKT                                      | witheachcorrespondingbaselineun- |               |     |     |           |
6.2 OverallPerformance(RQ1)
|     |     |     |     |     |     | derthesamedatapartitions. |          |        | Theresultsaresum- |         |          |
| --- | --- | --- | --- | --- | --- | ------------------------- | -------- | ------ | ----------------- | ------- | -------- |
|     |     |     |     |     |     | marized                   | in Table | 3. The | results           | confirm | that the |
Toaddressourfirstresearchquestion(RQ1)con-
|     |     |     |     |     |     | gainsarestatisticallysignificant(p |     |     |     | < 0.05)forthe |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------------- | --- |
cerningtheeffectivenessoftheSTATUSKTframe-
|         |           |     |                |          |     | majority               | of architectures, |     | with              | moderate | to large |
| ------- | --------- | --- | -------------- | -------- | --- | ---------------------- | ----------------- | --- | ----------------- | -------- | -------- |
| work on | KT-PSP-25 |     | with students’ | problem- |     |                        |                   |     |                   |          |          |
|         |           |     |                |          |     | effectsizes(Cohen’sd). |                   |     | Twomodels,DKT+and |          |          |
solvingprocesses,weappliedittoawiderangeof
SAKT,donotreachsignificance,whichalignswith
existingKTarchitectures.
|     |     |     |     |     |     | their relatively | low | baseline | AUC | where | the MP |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | --- | ----- | ------ |
TheexperimentalresultsaresummarizedinTa-
signalsofferlimitedadditionalleverage.
| ble 2. | Analysis | of both | AUC and | ACC | metrics |     |     |     |     |     |     |
| ------ | -------- | ------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Overall,thesefindingsaddressRQ1,indicating
revealsthatmerelyappendingrawtextembeddings
thatunprocessedPSPaloneisinsufficientforim-
| to the original | models |     | (Baseline+PSP) | does | not |     |     |     |     |     |     |
| --------------- | ------ | --- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
provingKTperformance,whereasourframework
| consistently | enhance | performance. |     | In several | ar- |              |          |             |     |              |     |
| ------------ | ------- | ------------ | --- | ---------- | --- | ------------ | -------- | ----------- | --- | ------------ | --- |
|              |         |              |     |            |     | consistently | delivers | performance |     | improvements |     |
chitectures,theperformancefluctuatesaroundthe
throughprincipledprocessmodeling.
baseline,suggestingthattheinclusionofprocess
| text may         | introduce | noise. | We  | hypothesize | that    |                                  |     |     |     |     |     |
| ---------------- | --------- | ------ | --- | ----------- | ------- | -------------------------------- | --- | --- | --- | --- | --- |
|                  |           |        |     |             |         | 6.3 PerformanceinCold-Start(RQ2) |     |     |     |     |     |
| this instability | stems     | from   | OCR | artifacts   | and the |                                  |     |     |     |     |     |
mismatchbetweenfree-formtextualtracesandthe Cold-start arises when models must predict per-
discrete KT objective, motivating our structured formance for unseen students with only a few
MP distillation. In contrast, models augmented early interactions. With such limited evidence,
withSTATUSKTachieveconsistentimprovements estimating learner’s latent knowledge states be-
overboththebaselineandBaseline+PSPformost comesunstableandoftendegradespredictiveper-
architectures. The enhancements are particularly formance(SlaterandBaker,2018;Bhattacharjee
notableinRNN-basedmodels(e.g.,DKT)andre- andWayllace,2025). Priorwork(Guoetal.,2024;
cent transformer-style approaches (e.g., SAINT, Baietal.,2025)introducesarchitecturalpriorsor
AKT), which exhibit higher AUC and ACC with external semantics, yet reliably estimating a stu-
ourmethod. ThesefindingssuggestthatourSTA- dent’s state from sparse correctness observations
TUSKT framework distills the process into struc- remains difficult. Our STATUSKT framework in-
7

DKT DKT+ DKVMN SKVMN SAKT SAINT AKT SimpleKT StableKT RobustKT
AUC
Baseline 0.6072 0.6093 0.5875 0.5758 0.5764 0.6228 0.6217 0.6406 0.6516 0.6196
STATUSKT 0.6031 0.6069 0.5843 0.5826 0.5818 0.6266 0.6352 0.6442 0.6541 0.6302
ACC
Baseline 0.7064 0.7107 0.7043 0.7207 0.7113 0.7350 0.7189 0.7219 0.7308 0.7330
STATUSKT 0.7146 0.7134 0.7083 0.7253 0.7230 0.7471 0.7278 0.7261 0.7538 0.7402
Table4: Cold-startperformance(t ≤ 5). WeevaluateeachKTarchitectureusingonlythefirstfiveobserved
interactionsperstudent. ModelsaugmentedwithSTATUSKTgenerallyachievehigherAUCandACC,indicating
thatMPsignalshelpestimatelearners’knowledgestatesevenunderlimitedearlyevidence.
Figure4: ExampleMPannotationandassessmentusedforcaseinspection. (a)Problemtextandstudent’sPSP.
(b)ExtractedMPindicators. (c)Rationale-basedevaluationofMPscope.
steadleveragesprocess-derivedMPsignals,which andthestudent’sPSPwiththecorrespondingMPs.
begin appearing even within the first few interac- Wefocusonthreepatterns: (i)MP-helpinstances
tionsandthusofferricherearlyinformation. Toex- where adding MP flips an incorrect prediction to
aminewhetherMPsignalsmitigatecold-start,we correct, (ii) confidence-gap analysis within MP-
evaluate models under a strict student-level hold- helpcasestounderstandwhypredictedprobabili-
outprotocolandrestricteachsequencetothefirst tiescandifferevenwhenthemodeliscorrect,and
five interactions (t ≤ 5). As reported in Table 4, (iii)MP-hurtinstancesthatrevealrecurringfailure
incorporatingSTATUSKTframeworkconsistently modeswhenMPdegradespredictionquality.
improvesACCacrossallarchitecturesandyields
6.4.1 MP-HelpCases
competitive or higher AUC in most cases. These
gainsindicatethatMPsignalsprovideinformative InMP-helpinstances,theMPindicatorsalignwith
priorsthatstabilizestateestimationwhenearlydata theskillsrequiredtosolvetheproblem(e.g.,rec-
arescarce,supportingourhypothesisthatprocess ognizingthattheiteminvolvespartialsumsofan
modelingisparticularlybeneficialinlow-evidence arithmetic sequence). Student responses to these
regimes. indicatorsprovideitem-relevantevidenceofmas-
tery, enabling the model to associate correctness
withtheappropriateunderlyingproficiency.
6.4 AnalysisofMPEffectsonKT(RQ3)
6.4.2 ConfidenceGapAnalysis
ToexaminewhetherMPsprovideausefulrepresen-
tationforKT,weconductacase-baseddiagnostic WecompareanMP-correctlow-scorecase(≈ 0.5)
analysisthatcontrastspredictionsmadewithand andahigh-scorecase(> 0.7). MPsaresimilarly
without MP. Following the template in Figure 4, wellscopedinboth,butconfidenceislowerforthe
weinspecteachcasebyaligningtheproblemtext harderitem(difficulty70)thanfortheeasierone
8

(difficulty30),suggestingdifficulty-drivenuncer- the proposed framework would transfer to other
taintyevenwhenMPisadequate. subjectsortoproblem-solvingcontexts. Because
rawstudentproblem-solvingprocesses(PSP)could
6.4.3 MP-HurtCases
|     |     |     |     | not be released | as  | images, | we  | relied | on OCR to |
| --- | --- | --- | --- | --------------- | --- | ------- | --- | ------ | --------- |
InMP-hurtinstances,wefindascope-relatedfail- extract the text. This step introduces occasional
ure mode: MP can include non-essential, over- recognition errors and removes visual reasoning
enrichedstatements(e.g.,optionalalternativemeth- elements,suchasdiagramsandgraphs,whichmay
ods)ormisalignedwiththeitemrequirementsre-
carryimportantcognitivesignals.
flectedinthestudent’sPSP.Suchover-enrichment Additionally,thecurrentpipelinereliesonGPT-
may inflate the perceived skill requirements and 5forallthreeLLMstages,whichintroducesnon-
leadtoanincorrectpredictionevenwhenthestu- trivial computational cost and latency compared
| dent answers | correctly. | This suggests | that MP |                |      |            |     |          |       |
| ------------ | ---------- | ------------- | ------- | -------------- | ---- | ---------- | --- | -------- | ----- |
|              |            |               |         | to lightweight | DLKT | baselines. |     | Although | indi- |
scope and granularity matter for reliable integra- cator extraction is problem-specific and can be
tion,andmotivatesscope-controlledMP(e.g.,sep- pre-computedoffline,twoLLMcallsperstudent-
aratingcorevs.enrichedindicators)asfuturework.
|     |     |     |     | problem          | interaction | are                          | still | required | during the |
| --- | --- | --- | --- | ---------------- | ----------- | ---------------------------- | ----- | -------- | ---------- |
|     |     |     |     | evaluationstage. |             | Ourprimarycontributionliesin |       |          |            |
7 Conclusion
establishingempiricalevidencethatprocess-level
|                      |            |           |           | signals provide | consistent |        | modeling |         | gains across |
| -------------------- | ---------- | --------- | --------- | --------------- | ---------- | ------ | -------- | ------- | ------------ |
| This work            | introduced | KNOWLEDGE | TRACING   |                 |            |        |          |         |              |
|                      |            |           |           | architectures.  | In         | future | work,    | we plan | to explore   |
| WITH PROBLEM-SOLVING |            | PROCESS   | (KT-PSP), |                 |            |        |          |         |              |
distillationandtask-specificsmallermodelstore-
anewformulationthatincorporatesstudents’solu-
ducetherelianceonlarge-scaleLLMinference.
tionprocessesintoknowledgetracing,addressing
| thelimitationofoutcome-centricKTmethods. |     |     | To  |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9 Acknowledgments
| support | this direction, | we constructed | KT-PSP- |     |     |     |     |     |     |
| ------- | --------------- | -------------- | ------- | --- | --- | --- | --- | --- | --- |
25,thefirstmathematicalKTdatasetthatprovides ThisworkwaspartlysupportedbyQANDA(Math-
real-world,OCR-transcribedproblem-solvingpro- presso Inc.), Institute of Information & com-
cessesalongwithrichinteractionmetadata. Build- munications Technology Planning & Evaluation
| ing on | this foundation, | we proposed | STATUSKT, |              |        |     |            |            |     |
| ------ | ---------------- | ----------- | --------- | ------------ | ------ | --- | ---------- | ---------- | --- |
|        |                  |             |           | (IITP) grant | funded | by  | the Korean | Government |     |
a KT framework that employs a teacher-student- (MSIT) (No. RS-2021-II211343, Artificial In-
teacherLLMpipelinetoextractinterpretablemath- telligence Graduate School Program (Seoul Na-
ematicalproficiency(MP)ratios. TheseMPratios tional University)), the National Research Foun-
serve as meaningful intermediate representations dation of Korea(NRF) grant funded by the Ko-
that enrich KT models with process-level infor- reagovernment(MSIT)(No.RS-2024-00354218),
mation beyond correctness. Experiments on KT- andtheTechnologyInnovationProgram(RS-2025-
PSP-25demonstratethatSTATUSKTconsistently
25456760,Developmentofahumanoidrobotspe-
improvespredictionperformancewhileproviding cialized in chemical processes based on AI foun-
interpretableproficiencysignals. Ourstudyhigh- dation model) funded By the Ministry of Trade,
lightsthatincorporatingthereasoningreflectedin
|     |     |     |     | Industry | and Resources(MOTIR, |     |     | Korea). | We ex- |
| --- | --- | --- | --- | -------- | -------------------- | --- | --- | ------- | ------ |
students’problem-solvingprocessesisessentialfor press special thanks to KAIT GPU project. The
advancingKTtowardmoreaccurate,interpretable, ICTatSeoulNationalUniversityprovidesresearch
| andpedagogicallymeaningfulmodeling. |     |     |     | facilitiesforthisstudy. |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
8 Limitations
References
| This work | may introduce | potential | risks related |     |     |     |     |     |     |
| --------- | ------------- | --------- | ------------- | --- | --- | --- | --- | --- | --- |
GhodaiAbdelrahman,SherifAbdelfattah,QingWang,
| toeducationalbias. |     | Sincethedatasetiscollected |     |                |     |           |     |                   |     |
| ------------------ | --- | -------------------------- | --- | -------------- | --- | --------- | --- | ----------------- | --- |
|                    |     |                            |     | andYuLin.2022. |     | Dbe-kt22: |     | Aknowledgetracing |     |
fromaspecificplatformandstudentpopulation,the
|     |     |     |     | dataset | based on | online | student | evaluation. | arXiv |
| --- | --- | --- | --- | ------- | -------- | ------ | ------- | ----------- | ----- |
modelmayreflectbiasthatdonotgeneralizeacross
preprintarXiv:2208.12651.
| diverselearners. | Ourdatasetislimitedinscale,as |          |               |                                    |     |     |     |     |        |
| ---------------- | ----------------------------- | -------- | ------------- | ---------------------------------- | --- | --- | --- | --- | ------ |
|                  |                               |          |               | GhodaiAbdelrahmanandQingWang.2019. |     |     |     |     | Knowl- |
| the number       | of participating              | students | is relatively |                                    |     |     |     |     |        |
edgetracingwithsequentialkey-valuememorynet-
small,whichmayconstrainthegeneralizabilityof
|              |              |            |               | works. | In Proceedings |     | of the | 42nd | international |
| ------------ | ------------ | ---------- | ------------- | ------ | -------------- | --- | ------ | ---- | ------------- |
| the results. | In addition, | the domain | is restricted |        |                |     |        |      |               |
ACMSIGIRconferenceonresearchanddevelopment
to mathematics, and it remains unclear how well ininformationretrieval,pages175–184.
9

Kingma DP Ba J Adam and 1 others. 2014. A modelinganduser-adaptedinteraction,19(3):243–
| methodforstochasticoptimization. |     |     |     |     | arXivpreprint |     | 266. |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
arXiv:1412.6980,1412(6).
BradfordFindell,JaneSwafford,andJeremyKilpatrick.
YouhengBai,XueyiLi,ZitaoLiu,YayingHuang,Teng
|     |     |     |     |     |     |     | 2001. | Addingitup: | Helpingchildrenlearnmathe- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | -------------------------- | --- | --- | --- | --- |
Guo,MingliangHou,FengXia,andWeiqiLuo.2025.
|         |            |            |          |            |              |        | matics. | NationalAcademiesPress. |     |     |     |     |     |
| ------- | ---------- | ---------- | -------- | ---------- | ------------ | ------ | ------- | ----------------------- | --- | --- | --- | --- | --- |
| cskt:   | Addressing | cold-start |          | problem    | in knowledge |        |         |                         |     |     |     |     |     |
| tracing | via kernel | bias       | and cone | attention. |              | Expert |         |                         |     |     |     |     |     |
AritraGhosh,NeilHeffernan,andAndrewSLan.2020.
SystemswithApplications,266:125988.
|     |     |     |     |     |     |     | Context-awareattentiveknowledgetracing. |     |          |            |     |               | InPro- |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | -------- | ---------- | --- | ------------- | ------ |
|     |     |     |     |     |     |     | ceedings                                | of  | the 26th | ACM SIGKDD |     | international |        |
IndronilBhattacharjeeandChristabelWayllace.2025.
conferenceonknowledgediscovery&datamining,
| Coldstartproblem: |     | Anexperimentalstudyofknowl- |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pages2330–2339.
| edge | tracing | models | with new | students. |     | Preprint, |     |     |     |     |     |     |     |
| ---- | ------- | ------ | -------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2505.21517.
|            |        |           |     |      |         |       | BertFGreenJr.1951.                   |     | Ageneralsolutionforthelatent |     |     |           |     |
| ---------- | ------ | --------- | --- | ---- | ------- | ----- | ------------------------------------ | --- | ---------------------------- | --- | --- | --------- | --- |
|            |        |           |     |      |         |       | classmodeloflatentstructureanalysis. |     |                              |     |     | Psychome- |     |
| Haw-Shiuan | Chang, | Hwai-Jung |     | Hsu, | Kuan-Ta | Chen, |                                      |     |                              |     |     |           |     |
trika,16(2):151–166.
| and1others.2015. |     | Modelingexerciserelationships |     |     |             |     |                |      |           |      |                    |           |     |
| ---------------- | --- | ----------------------------- | --- | --- | ----------- | --- | -------------- | ---- | --------- | ---- | ------------------ | --------- | --- |
| ine-learning:    |     | Aunifiedapproach.             |     |     | InEDM,pages |     |                |      |           |      |                    |           |     |
| 532–535.         |     |                               |     |     |             |     | TengGuo,YuQin, |      | YubinXia, |      | MingliangHou,Zitao |           |     |
|                  |     |                               |     |     |             |     | Liu, Feng      | Xia, | and Weiqi | Luo. | 2025.              | Enhancing |     |
Jiahao Chen, Zitao Liu, Shuyan Huang, Qiongqiong knowledgetracingthroughdecouplingcognitivepat-
| Liu,andWeiqiLuo.2023. |            |           | Improvinginterpretability |         |        |      |           |             |     |       |                |     |        |
| --------------------- | ---------- | --------- | ------------------------- | ------- | ------ | ---- | --------- | ----------- | --- | ----- | -------------- | --- | ------ |
|                       |            |           |                           |         |        |      | tern from | error-prone |     | data. | In Proceedings |     | of the |
| of deep               | sequential | knowledge |                           | tracing | models | with |           |             |     |       |                |     |        |
ACMonWebConference2025,pages5108–5116.
| question-centric |     | cognitive | representations. |     |     | In Pro- |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ceedingsoftheAAAIconferenceonartificialintelli- XiaopengGuo,ZhijieHuang,JieGao,MingyuShang,
gence,volume37,pages14196–14204.
|        |       |             |       |     |         |       | MaojingShu,andJunSun.2021.         |     |     |     | Enhancingknowl- |               |     |
| ------ | ----- | ----------- | ----- | --- | ------- | ----- | ---------------------------------- | --- | --- | --- | --------------- | ------------- | --- |
|        |       |             |       |     |         |       | edgetracingviaadversarialtraining. |     |     |     |                 | InProceedings |     |
| Penghe | Chen, | Yu Lu, Yang | Pian, | Yan | Li, and | Yunbo |                                    |     |     |     |                 |               |     |
ofthe29thACMinternationalconferenceonmulti-
| Cao.2022. | Introducingresponsetimeintoguessing |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
media,pages367–375.
| andslippingforcognitivediagnosis. |     |               |              |     | InInternational |     |         |      |            |       |     |      |        |
| --------------------------------- | --- | ------------- | ------------ | --- | --------------- | --- | ------- | ---- | ---------- | ----- | --- | ---- | ------ |
| Conference                        |     | on Artificial | Intelligence |     | in Education,   |     |         |      |            |       |     |      |        |
|                                   |     |               |              |     |                 |     | Yuxiang | Guo, | Shuanghong | Shen, | Qi  | Liu, | Zhenya |
pages320–324.Springer.
Huang,LinboZhu,YuSu,andEnhongChen.2024.
|         |              |             |               |                 |            |         | Mitigating                  | cold-start |             | problems | in                | knowledge | trac-  |
| ------- | ------------ | ----------- | ------------- | --------------- | ---------- | ------- | --------------------------- | ---------- | ----------- | -------- | ----------------- | --------- | ------ |
| Barbara | Chiu,        | Christopher | Randles,      |                 | and Stefan | Irby.   |                             |            |             |          |                   |           |        |
|         |              |             |               |                 |            |         | ingwithlargelanguagemodels: |            |             |          | Anattribute-aware |           |        |
| 2022.   | Analyzing    | student     |               | problem-solving |            | with    |                             |            |             |          |                   |           |        |
|         |              |             |               |                 |            |         |                             |            | Proceedings | of       | the 33rd          | ACM       | Inter- |
| match.  | In Frontiers |             | in Education, |                 | volume     | 6, page | approach.                   | In         |             |          |                   |           |        |
769042.FrontiersMediaSA. nationalConferenceonInformationandKnowledge
Management,CIKM’24,page727–736,NewYork,
Youngduck Choi, Youngnam Lee, Junghyun Cho, Ji- NY,USA.AssociationforComputingMachinery.
neonBaek,ByungsooKim,YeongminCha,Dong-
minShin,ChanBae,andJaeweHeo.2020a. Towards TaoHuang,ShengzeHu,HualiYang,JingGeng,Zhifei
anappropriatequery,key,andvaluecomputationfor Li, Zhuoran Xu, and Xinjia Ou. 2024. Response
knowledge tracing. In Proceedings of the seventh speedenhancedfine-grainedknowledgetracing: A
ACMconferenceonlearning@scale,pages341–344. multi-tasklearningperspective. ExpertSystemswith
Applications,238:122107.
| Youngduck | Choi, | Youngnam |     | Lee, | Dongmin | Shin, |     |     |     |     |     |     |     |
| --------- | ----- | -------- | --- | ---- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Junghyun Cho, Seoyon Park, Seewoo Lee, Jineon KDD 2010. 2010. Kdd2010.
Baek, Chan Bae, Byungsoo Kim, and Jaewe Heo. https://kdd.org/kdd-cup/view/
2020b. Ednet: Alarge-scalehierarchicaldatasetin kdd-cup-2010-student-performance-evaluation.
| education. | InInternationalconferenceonartificial |     |     |     |     |     |           |       |     |     |     |     |     |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- |
|            |                                       |     |     |     |     |     | Accessed: | 2010. |     |     |     |     |     |
intelligenceineducation,pages69–73.Springer.
|                                      |     |                                    |     |     |     |        | Dohee Kim, | Unggi   | Lee,       | Sookbun   | Lee,    | Jiyeong      | Bae,     |
| ------------------------------------ | --- | ---------------------------------- | --- | --- | --- | ------ | ---------- | ------- | ---------- | --------- | ------- | ------------ | -------- |
| AlbertTCorbettandJohnRAnderson.1994. |     |                                    |     |     |     | Knowl- |            |         |            |           |         |              |          |
|                                      |     |                                    |     |     |     |        | Taekyung   | Ahn,    | Jaekwon    | Park,     | Gunho   |              | Lee, and |
| edgetracing:                         |     | Modelingtheacquisitionofprocedural |     |     |     |        |            |         |            |           |         |              |          |
|                                      |     |                                    |     |     |     |        | Hyeoncheol |         | Kim. 2025. | Es-kt-24: |         | A multimodal |          |
| knowledge.                           |     | Usermodelinganduser-adaptedinter-  |     |     |     |        |            |         |            |           |         |              |          |
|                                      |     |                                    |     |     |     |        | knowledge  | tracing | benchmark  |           | dataset | with         | educa-   |
action,4(4):253–278.
|         |              |     |       |            |     |       | tional   | game                                   | playing | video and | synthetic |     | text gen- |
| ------- | ------------ | --- | ----- | ---------- | --- | ----- | -------- | -------------------------------------- | ------- | --------- | --------- | --- | --------- |
|         |              |     |       |            |     |       | eration. | InInternationalConferenceonIntelligent |         |           |           |     |           |
| Ibrahim | AH El-Shara, |     | Ahmad | AS Tabieh, | and | Sahar |          |                                        |         |           |           |     |           |
TutoringSystems,pages259–273.Springer.
| YA Abu | Helu. | 2025. | The | effect | of using | matgpt |     |     |     |     |     |     |     |
| ------ | ----- | ----- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
onmathematicalproficiencyamongundergraduate
students. InternationalJournalofInformationand EricaKleinman,MurtuzaShergadwala,ZhaoqingTeng,
|     |     |     |     |     |     |     | Jennifer | Villareale, | Andy | Bryant, |     | Jichen | Zhu, and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | ------- | --- | ------ | -------- |
EducationTechnology,15(4).
|     |     |     |     |     |     |     | Magy | Seif | El-Nasr. | 2022. | Analyzing |     | students’ |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | -------- | ----- | --------- | --- | --------- |
MingyuFeng,NeilHeffernan,andKennethKoedinger. problem-solving sequences: A human-in-the-loop
2009. Addressing the assessment challenge with approach. Journaloflearninganalytics,9(2):138–
| an online | system | that | tutors | as it | assesses. | User | 160. |     |     |     |     |     |     |
| --------- | ------ | ---- | ------ | ----- | --------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
10

XueyiLi,YouhengBai,TengGuo,ZitaoLiu,Yaying ChrisPiech,JonathanBassen,JonathanHuang,Surya
Huang, Xiangyu Zhao, Feng Xia, Weiqi Luo, and Ganguli, Mehran Sahami, Leonidas J Guibas, and
JianWeng.2024. Enhancinglengthgeneralization JaschaSohl-Dickstein.2015. Deepknowledgetrac-
forattentionbasedknowledgetracingmodelswith ing. Advancesinneuralinformationprocessingsys-
| linear biases. | In Proceedingsof |     | the thirty-thirdin- |     | tems,28. |     |     |     |     |     |
| -------------- | ---------------- | --- | ------------------- | --- | -------- | --- | --- | --- | --- | --- |
ternationaljointconferenceonartificialintelligence
(IJCAI-24),pages5918–5926. StefanSlaterandRyanS.Baker.2018. Degreeoferror
inBayesianknowledgetracingestimatesfromdiffer-
Guimei Liu, Huijing Zhan, and Jung-jae Kim. 2024. encesinsamplesizes. Behaviormetrika,45(2):475–
493.
| Questiondifficultyconsistentknowledgetracing. |     |     |     | In  |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ProceedingsoftheACMWebConference2024,pages
YuSu,ZeyuCheng,PengfeiLuo,JinzeWu,LeiZhang,
4239–4248.
|     |     |     |     |     | QiLiu,andShijinWang.2021. |     |     |     | Time-and-concept |     |
| --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---------------- | --- |
enhanceddeepmultidimensionalitemresponsethe-
| Zitao Liu, | Teng Guo, Qianru | Liang, | Mingliang | Hou, |                                      |     |     |     |     |            |
| ---------- | ---------------- | ------ | --------- | ---- | ------------------------------------ | --- | --- | --- | --- | ---------- |
|            |                  |        |           |      | oryforinterpretableknowledgetracing. |     |     |     |     | Knowledge- |
BojunZhan,JiliangTang,WeiqiLuo,andJianWeng.
BasedSystems,218:106819.
| 2025. Deep                       | learning | based | knowledge    | tracing: A |                     |     |                              |     |     |     |
| -------------------------------- | -------- | ----- | ------------ | ---------- | ------------------- | --- | ---------------------------- | --- | --- | --- |
| review,atoolandempiricalstudies. |          |       | IEEETransac- |            |                     |     |                              |     |     |     |
|                                  |          |       |              |            | PeterSullivan.2011. |     | Usingtheproficienciesfromthe |     |     |     |
tionsonKnowledgeandDataEngineering.
australianmathematicscurriculumtoenrichmathe-
|     |     |     |     |     | maticsteachingandassessment. |     |     |     | AustralianEduca- |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ---------------- | --- |
ZitaoLiu,QiongqiongLiu,JiahaoChen,ShuyanHuang,
tionReview,(59).
| and Weiqi | Luo. 2023a. | simplekt: | a   | simple but |     |     |     |     |     |     |
| --------- | ----------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
tough-to-beatbaselineforknowledgetracing. arXiv PaulTschisgale,MarcusKubsch,PeterWulff,Stefan
preprintarXiv:2302.06881.
|     |     |     |     |     | Petersen,andKnutNeumann.2025. |           |              |     | Exploringthe |          |
| --- | --- | --- | --- | --- | ----------------------------- | --------- | ------------ | --- | ------------ | -------- |
|     |     |     |     |     | sequential                    | structure | of students’ |     | physics      | problem- |
ZitaoLiu,QiongqiongLiu,JiahaoChen,ShuyanHuang,
|     |     |     |     |     | solving approaches |     | using | process | mining | and se- |
| --- | --- | --- | --- | --- | ------------------ | --- | ----- | ------- | ------ | ------- |
JiliangTang,andWeiqiLuo.2022. pykt: Apython quenceanalysis. PhysicalReviewPhysicsEducation
librarytobenchmarkdeeplearningbasedknowledge Research,21(1):010111.
| tracingmodels. | InThirty-sixthConferenceonNeural |     |     |     |     |     |     |     |     |     |
| -------------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InformationProcessingSystemsDatasetsandBench- Fidele Ukobizaba, Gabriel Nizeyimana, and Angel
marksTrack.
|     |     |     |     |     | Mukuka.                                        | 2021. | Assessment | strategies |     | for enhanc- |
| --- | --- | --- | --- | --- | ---------------------------------------------- | ----- | ---------- | ---------- | --- | ----------- |
|     |     |     |     |     | ingstudents’mathematicalproblem-solvingskills: |       |            |            |     | A           |
Zitao Liu, Qiongqiong Liu, Teng Guo, Jiahao Chen, reviewofliterature. EurasiaJournalofMathematics,
ShuyanHuang,XiangyuZhao,JiliangTang,Weiqi ScienceandTechnologyEducation,17(3).
| Luo,andJianWeng.2023b. |     | Xes3g5m:Aknowledge |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tracingbenchmarkdatasetwithauxiliaryinformation. YutaoWangandNeilTHeffernan.2012. Leveraging
firstresponsetimeintotheknowledgetracingmodel.
AdvancesinNeuralInformationProcessingSystems,
InternationalEducationalDataMiningSociety.
36:32958–32970.
YangYang,JianShen,YanruQu,YunfeiLiu,Kerong
KokiNagatani,QianZhang,MasahiroSato,Yan-Ying
Chen,FrancineChen,andTomokoOhkuma.2019. Wang,YaomingZhu,WeinanZhang,andYongYu.
|     |     |     |     |     | 2020. Gikt: | A   | graph-based | interaction |     | model for |
| --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----------- | --- | --------- |
Augmentingknowledgetracingbyconsideringfor-
|                  |                              |     |     |     | knowledgetracing. |     | Preprint,arXiv:2009.05991. |     |     |     |
| ---------------- | ---------------------------- | --- | --- | --- | ----------------- | --- | -------------------------- | --- | --- | --- |
| gettingbehavior. | InTheworldwidewebconference, |     |     |     |                   |     |                            |     |     |     |
pages3101–3107.
|     |     |     |     |     | Chun-Kit Yeung. | 2019. | Deep-irt: |     | Make | deep learn- |
| --- | --- | --- | --- | --- | --------------- | ----- | --------- | --- | ---- | ----------- |
ingbasedknowledgetracingexplainableusingitem
HiromiNakagawa,YusukeIwasawa,andYutakaMat-
|           |                              |     |     |        | responsetheory. |     | arXivpreprintarXiv:1904.11738. |     |     |     |
| --------- | ---------------------------- | --- | --- | ------ | --------------- | --- | ------------------------------ | --- | --- | --- |
| suo.2019. | Graph-basedknowledgetracing: |     |     | model- |                 |     |                                |     |     |     |
ingstudentproficiencyusinggraphneuralnetwork. Chun-Kit Yeung and Dit-YanYeung. 2018. Address-
InIEEE/WIC/aCMinternationalconferenceonweb
|     |     |     |     |     | ing two | problems | in deep | knowledge |     | tracing via |
| --- | --- | --- | --- | --- | ------- | -------- | ------- | --------- | --- | ----------- |
intelligence,pages156–163.
|               |       |        |                    |     | prediction-consistentregularization. |        |     |            | InProceedings |             |
| ------------- | ----- | ------ | ------------------ | --- | ------------------------------------ | ------ | --- | ---------- | ------------- | ----------- |
|               |       |        |                    |     | of the fifth                         | annual | ACM | conference | on            | learning at |
| OpenAI. 2025. | Gpt-5 | system | card. https://cdn. |     |                                      |        |     |            |               |             |
scale,pages1–10.
openai.com/gpt-5-system-card.pdf.
Accessed:
2025-09-24. Jiani Zhang, Xingjian Shi, Irwin King, and Dit-Yan
|                |            |           |          |         | Yeung.2017.          | Dynamickey-valuememorynetworks |     |                  |     |      |
| -------------- | ---------- | --------- | -------- | ------- | -------------------- | ------------------------------ | --- | ---------------- | --- | ---- |
| Shalini Pandey | and George | Karypis.  | 2019.    | A self- |                      |                                |     |                  |     |      |
|                |            |           |          |         | forknowledgetracing. |                                | In  | Proceedingsofthe |     | 26th |
| attentive      | model for  | knowledge | tracing. | arXiv   |                      |                                |     |                  |     |      |
internationalconferenceonWorldWideWeb,pages
| preprintarXiv:1907.06837. |     |     |     |     | 765–774. |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
ZacharyAPardos,RyanSJDBaker,MariaOCZSanPe- YiyunZhou,WenkangHan,andJingyuanChen.2025.
dro,SujithMGowda,andSupreethMGowda.2014. Revisiting applicable and comprehensive knowl-
Affectivestatesandstatetests: Investigatinghowaf- edge tracing in large-scale data. arXiv preprint
arXiv:2501.14256.
fectandengagementduringtheschoolyearpredict
| end-of-yearlearningoutcomes. |     |     | Journaloflearning |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Analytics,1(1):107–128.
11

A BaselineModels
|                                         |        |         |        |     |       |      |                 | Question   |           | Question | Question  | Student’s |
| --------------------------------------- | ------ | ------- | ------ | --- | ----- | ---- | --------------- | ---------- | --------- | -------- | --------- | --------- |
|                                         |        |         |        |     |       |      | Dataset         | Difficulty | Timestamp |          | Text Type | PSP       |
|                                         |        |         |        |     |       |      |                 | ✓          |           | ✗        | ✗ ✗       | ✗         |
| • DKT                                   | (Piech | et al., | 2015): | The | first | RNN- | ASSISTments2009 |            |           |          |           |           |
|                                         |        |         |        |     |       |      | ASSISTments2014 | ✓          |           | ✗        | ✗ ✗       | ✗         |
| basedknowledgetracingmodelcapturingtem- |        |         |        |     |       |      |                 | ✓          |           | ✓        | ✗ ✗       | ✗         |
Junyi2015
porallearningpatterns.
|                                         |     |     |     |     |           |     | KDDcup2010 | ✗   |     | ✓   | ✗ ✗ | ✗   |
| --------------------------------------- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
|                                         |     |     |     |     |           |     | EdNet      | ✗   |     | ✓   | ✗ ✗ | ✗   |
| • DKT+(YeungandYeung,2018):             |     |     |     |     | Addsregu- |     | DBE-KT22   | ✓   |     | ✓   | ✓ ✗ | ✗   |
| larizationtoDKTtomitigateoverfittingand |     |     |     |     |           |     |            | ✗   |     | ✓   | ✓ ✓ | ✗   |
XES3G5M
| improveinterpretability.  |     |     |     |     |             |     | ES-KT-24        | ✗          |     | ✓           | ✓ ✓      | ✗    |
| ------------------------- | --- | --- | --- | --- | ----------- | --- | --------------- | ---------- | --- | ----------- | -------- | ---- |
|                           |     |     |     |     |             |     | KT-PSP-25(Ours) | ✓          |     | ✓           | ✓ ✓      | ✓    |
| • DKVMN(Zhangetal.,2017): |     |     |     |     | Introducesa |     |                 |            |     |             |          |      |
|                           |     |     |     |     |             |     | Table 5:        | Comparison | of  | educational | datasets | com- |
dynamickey-valuememorynetworktoexplic-
|     |     |     |     |     |     |     | monly | used in KT. | While | prior | datasets | do not in- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | ----- | -------- | ---------- |
itlymodelconcept-levelknowledgestates.
cludestudents’PSP,ourKT-PSP-25isthefirsttooffer
process-leveltextualtracesenablingprocess-awareKT
| • SKVMN |     | (Abdelrahman |     | and | Wang, | 2019): |     |     |     |     |     |     |
| ------- | --- | ------------ | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- |
modeling.
| Enhances |     | DKVMN                 | by  | disentangling |            | stu- |     |     |     |     |     |     |
| -------- | --- | --------------------- | --- | ------------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| dent     | and | skill representations |     |               | for better | in-  |     |     |     |     |     |     |
terpretability.
|                                |     |     |     |     |         |     | supporting  | more | interpretable |     | and process-aware |     |
| ------------------------------ | --- | --- | --- | --- | ------- | --- | ----------- | ---- | ------------- | --- | ----------------- | --- |
| • SAKT(PandeyandKarypis,2019): |     |     |     |     | Employs |     | KTresearch. |      |               |     |                   |     |
self-attentiontoidentifythemostrelevantpast
interactionsefficiently.
|       |        |     |             |     |              |     | C TrainingDetails |     |     |     |     |     |
| ----- | ------ | --- | ----------- | --- | ------------ | --- | ----------------- | --- | --- | --- | --- | --- |
| • AKT | (Ghosh | et  | al., 2020): |     | Incorporates |     |                   |     |     |     |     |     |
distance-aware exponential decay to model All experiments were conducted using the
learningandforgettingbehaviors.
|                             |     |     |     |     |               |     | pyKT          | library (Liu | et  | al., 2022),  | which     | is a      |
| --------------------------- | --- | --- | --- | --- | ------------- | --- | ------------- | ------------ | --- | ------------ | --------- | --------- |
|                             |     |     |     |     |               |     | PyTorch-based | framework    |     | for          | knowledge | trac-     |
| • SimpleKT(Liuetal.,2023a): |     |     |     |     | Simplifiesthe |     |               |              |     |              |           |           |
|                             |     |     |     |     |               |     | ing.          | We searched  |     | the learning |           | rate from |
attentionarchitectureforcomputationaleffi- 10−3, 10−3, 10−4, 10−4],
|     |     |     |     |     |     |     | [5 × | 1 × |     | 5 × | 1   | ×   |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
ciencywhilemaintainingaccuracy.
|                           |     |     |     |               |     |     |              | [0.5, | 0.3,       | 0.1, | 0.05],       | α    |
| ------------------------- | --- | --- | --- | ------------- | --- | --- | ------------ | ----- | ---------- | ---- | ------------ | ---- |
|                           |     |     |     |               |     |     | dropout      | from  |            |      | and          | from |
|                           |     |     |     |               |     |     | [0.01, 0.25, | 1.0,  | 1.5, 2.0]. | A    | fixed random | seed |
| • StableKT(Lietal.,2024): |     |     |     | Improvesmodel |     |     |              |       |            |      |              |      |
stability and generalization on long student (42)wasusedforthereproducibility. Allthetrain-
interactionsequences. ing was conducted using a single NVIDIA RTX
3090GPU.
| • RobustKT |     | (Guo | et al., 2025): |     | Enhances | ro- |     |     |     |     |     |     |
| ---------- | --- | ---- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
FortheLLM-basedcomponentsinthepipeline,
bustnessagainstnoisyorincompletestudent
weusedthegpt-5modelwiththetemperatureset
datathroughrobustoptimizationtechniques.
to0.0andtop-psetto1.0toensuredeterministic
|     |     |     |     |     |     |     | behavior. | Wedidnotimposeanexplicitmaximum |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------------- | --- | --- | --- | --- |
B DatasetComparison
|     |     |     |     |     |     |     | token limit, | allowing | the | model | to generate | com- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----- | ----------- | ---- |
Table 5 provides a summary of widely utilized pleteJSONoutputsasrequiredbytheprompt.
| knowledge | tracing | (KT) | datasets | and | the | types |     |     |     |     |     |     |
| --------- | ------- | ---- | -------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Thedetailedmodelconfigurationsforeachbase-
| of information |     | they encompass. |     | Earlier |     | bench- |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- |
linemodelaresummarizedinTable6
marks,predominantlyincludecorrectnesslogsand
| alimitedsetofcontextualattributes. |     |     |     |     | Morerecent |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
datasetsofferenhancedmetadata,suchasquestion Model FFNDim Heads Blocks AdditionalArchitectureDetails
|     |     |     |     |     |     |     | DKT | – – | –   |     | –   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
text or type, but they still lack explicit documen- DKT+ – – – λr=0.01,λw1=0.003,λw2=3.0
|     |     |     |     |     |     |     | DKVMN | – – | –   |     | memorysize=50 |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ------------- | --- |
tation ofthe methodsby which studentsarrive at SKVMN – – – memorysize=50
|               |     |           |                       |     |     |     | SAKT     | 256 8 | 1   |                                        | –   |     |
| ------------- | --- | --------- | --------------------- | --- | --- | --- | -------- | ----- | --- | -------------------------------------- | --- | --- |
| theiranswers. |     |           |                       |     |     |     | SAINT    | 256 8 | 4   |                                        | –   |     |
| Incontrast,   |     | KT-PSP-25 | incorporatesstudents’ |     |     |     | AKT      | 512 8 | 4   |                                        | –   |     |
|               |     |           |                       |     |     |     | simpleKT | 256 4 | 2   | start=50,num_layers=2,final_fc_dim=256 |     |     |
num_layers=2,r=0.5,γ=0.7
problem-solvingprocesses(PSP)astextualtraces stableKT 256 8 4
|                                    |     |     |     |     |              |     | robustKT | 512 8 | 4   |     | ks=5 |     |
| ---------------------------------- | --- | --- | --- | --- | ------------ | --- | -------- | ----- | --- | --- | ---- | --- |
| alongsideconventionalKTattributes. |     |     |     |     | Thisprocess- |     |          |       |     |     |      |     |
levelinformationenablesmodelsnotonlytopre- Table6: Modelconfigurationsforeachbaselinearchi-
tecture.
dictfutureperformancebutalsotoanalyzetherea-
sonsbehindstudents’successesorfailures,thereby
12

D OCRPipelineDetails
|     |     |     |     |     |     | • 0 — | unnecessary |     | or irrelevant |     | to solving | the |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ------------- | --- | ---------- | --- |
problem,
D.1 Prompts
Thepromptsusedinourdatasetcreationprocess • 1—conceptuallyvalidbutmisalignedwiththe
student’sfinalanswer,
wereasfollows:
• Figure5: ApromptforGPT-basedOCRtocon- • 2 — appropriate and consistent with both the
vertstudents’handwrittenproblem-solvingpro- solutionandtheanswer.
cessintotext.
|     |     |     |     |     |     | Overall, | 55.8% | of  | indicators | received |     | a score |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | ---------- | -------- | --- | ------- |
• Figure6: ApromptforrefiningGPT-basedOCR of2,indicatingthatslightlymorethanhalfofthe
outputstoimprovetranscriptionquality. generatedindicatorsaccuratelycapturedstudents’
|     |     |     |     |     |     | reasoning. | However,35.8%weredeemedpartially |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------------------------------- | --- | --- | --- | --- | --- |
D.2 OCRQualityEvaluation valid (score = 1), typically reflecting situations
|           |     |             |     |         |              | where the | reasoning | statement |     | itself | was | correct |
| --------- | --- | ----------- | --- | ------- | ------------ | --------- | --------- | --------- | --- | ------ | --- | ------- |
| To assess | the | reliability | of  | our OCR | pipeline, we |           |           |           |     |        |     |         |
manuallyinspectedarandomlyselectedsubsetof but did not correspond to the student’s final (of-
|                |     |            |     |         |         | tenincorrect)response. |     |     | Asmallerfraction(8.3%) |     |     |     |
| -------------- | --- | ---------- | --- | ------- | ------- | ---------------------- | --- | --- | ---------------------- | --- | --- | --- |
| 100handwritten |     | PSPsamples |     | fromthe | KT-PSP- |                        |     |     |                        |     |     |     |
consistedofredundantorclearlyunnecessaryindi-
| 25. Each | OCR       | output   | was | categorized           | as either |                  |     |     |     |     |     |     |
| -------- | --------- | -------- | --- | --------------------- | --------- | ---------------- | --- | --- | --- | --- | --- | --- |
| usable   | (i.e., it | retained | the | original mathematical |           | cators(score=0). |     |     |     |     |     |     |
meaning)orunusable(i.e.,itexhibitedsignificant When analyzed by proficiency dimension, no-
|             |      |     |         |            |           | table variation |     | was observed: |     | indicators |     | related |
| ----------- | ---- | --- | ------- | ---------- | --------- | --------------- | --- | ------------- | --- | ---------- | --- | ------- |
| distortions | such | as  | missing | operators, | collapsed |                 |     |               |     |            |     |         |
fractions,oromittedlines). Accordingtothiscrite- to conceptual understanding (CU; mean = 1.60)
rion,85%ofthesampledoutputsweredeemedus- and procedural fluency (PF; mean = 1.59) were
able,whereastheremaining15%containedmajor generally reliable, whereas adaptive reasoning
|                      |     |     |                           |     |     | (AR) achieved |     | the lowest |     | average | score | (1.13), |
| -------------------- | --- | --- | ------------------------- | --- | --- | ------------- | --- | ---------- | --- | ------- | ----- | ------- |
| transcriptionerrors. |     |     | Theinspectionwasconducted |     |     |               |     |            |     |         |       |         |
bytrainedannotatorswithexpertiseinmathematics with a comparatively large share of unnecessary
andAI,followingashortwrittenguidelinedescrib- statements. This suggests that generating meta-
|     |     |     |     |     |     | justifications | and | verification |     | steps | remains | chal- |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ----- | ------- | ----- |
ingthesecriteria.
|        |         |              |     |        |             | lengingforcurrentLLMs. |     |     | Furthercomparisonof |     |     |     |
| ------ | ------- | ------------ | --- | ------ | ----------- | ---------------------- | --- | --- | ------------------- | --- | --- | --- |
| In our | current | experiments, |     | we did | not explic- |                        |     |     |                     |     |     |     |
itly correct or filter unusable OCR cases, indicat- indicatorsbetweencorrectandincorrectresponses
ingthatsomeofthedownstreamnoiseinMPex- revealedthatforstudentresponsesmarkedascor-
|     |     |     |     |     |     | rect, 67.6% | of  | indicators | received |     | the maximum |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | -------- | --- | ----------- | --- |
tractionandKTpredictionlikelyoriginatedfrom
theOCRfailures. Nevertheless,weobservedthat score, compared to only 44.6% for incorrect re-
mostunusablecasesresultedfromstructuralbreak- sponses. Conversely, partially correct indicators
(score=1)weresubstantiallymorefrequentinin-
downsincomplexhandwrittenexpressionsrather
|                                         |     |     |     |     |      | correctcases(44.9%vs. |     |     | 26.1%). |     | Theseresultsin- |     |
| --------------------------------------- | --- | --- | --- | --- | ---- | --------------------- | --- | --- | ------- | --- | --------------- | --- |
| thanwidespreadsystematicmisrecognition. |     |     |     |     | Con- |                       |     |     |         |     |                 |     |
sequently,weregardOCRnoiseasamoderatebut dicatethatMPindicatorsconveymeaningfulinfor-
mationaboutthequalityandstabilityofstudents’
manageablelimitationofourpipeline,andwedefer
reasoning,beyondmerelytheirfinalanswers.
moresystematicrobustnessstudiesanddenoising
strategiestoaddressthisissueinfutureresearch.
E.2 Prompts
E MathematicalProficiencyExtraction
|     |     |     |     |     |     | The prompts | used | in  | our STATUSKT |     | for | extract- |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | ------------ | --- | --- | -------- |
Details
ingthemathematicalproficiency(MP)ratioareas
follows:
E.1 MathematicalProficiencyHuman
Evaluation
|     |     |     |     |     |     | • Figure | 7: A | prompt | to  | extract | MP indicators |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | --- | ------- | ------------- | --- |
Toevaluatethereliabilityoftheautomaticallygen-
|        |                |     |         |            |     | from  | problem | statement |     | and | curricular | unit |
| ------ | -------------- | --- | ------- | ---------- | --- | ----- | ------- | --------- | --- | --- | ---------- | ---- |
| erated | MP indicators, |     | a human | assessment | was | name. |         |           |     |     |            |      |
conductedon50randomlyselecteditems,compris-
ing25correctand25incorrectresponses. Intotal, • Figure 8: A prompt for student LLM, which
annotatorsevaluated590indicators. Eachindicator simulateshowastudentwouldrespondtoeach
wasassessedusingathree-levelrubric: ofthegeneratedindicators.
13

| • Figure | 9: A prompt | to evaluate whether | each |
| -------- | ----------- | ------------------- | ---- |
responsegeneratedbystudentLLMsatisfiesthe
intentofitscorrespondingindicator.
14

##RawPrompt:
"YouareaKoreanMathematicalOCRSpecialistwithlogicalsequencingcapability.
ExtracttextualcontentfromKoreanstudentmathwork,thenreorderitintologicalmathematicalsequence.
Ignoreallvisualelements(graphs,diagrams,shapes).OutputinLaTeXformatwithpropermathematicalflow."
##PromptCategories:
-Role&Identity:KoreanMathematicalOCRSpecialist+LogicSequencer
-OutputFormat:LaTeXMathematicalText(LogicallyOrdered)
-CognitiveBiasLever:Neutral
-Creativity/FidelityBalance:100%Fidelity+LogicEnhancement
##UserSettings:
-KoreanLanguageProcessing:true
-VisualElementFiltering:true(IGNOREallvisuals)
-FractionNormalization:true(vertical→\\frac{}{})
-ExtractTextOnly:true
-LaTeXOutput:true
-LogicSequencing:true
##CoreInstructions:
###Meta-CognitivePre-Check:
1."WhatmathematicaltextdoIsee?"
2."WhatvisualelementsmustIignore?"
3."HowdoIconvertfractionstoLaTeX?"
4."Whatisthelogicalmathematicalsequencehere?"
###Two-PhaseProcessing
####Phase1:RawExtraction
-**IGNORE**:graphs,figures,diagrams,arrows,connectinglines,numbersthatconsistsfigure
-**EXTRACT**:Koreantext,formulas,numbers,mathematicalsymbols
-**CONVERT**:verticalfractions→\\frac{numerator}{denominator}
-**SCAN**:ALLcontentregardlessofposition
####Phase2:LogicSequencing
-ANALYZE:analyzegivenproblemandrawextractedsolvingtraces
-IDENTIFY:problemstatementvs.solutionsteps
-DETECT:calculationflow(whichleadstowhich)
-REORDER:arrangeinlogicalmathematicalsequence
-**DONOT**changetheextractedtext
###LaTeXFormatting:
-fraction:\\frac{3}{4}
-exponent:xˆ{2}
-squareroot:\\sqrt{x}
-parentheses:()
##FINALINSTRUCTION:
First,extractallmathematicaltextcontent.Then,reorderintologicalmathematicalsequence.
OutputONLYtheextractedmathematicalcontentinLaTeXformat.
Nocommentary,noprocessdescriptions,nogivenproblem,onlythecomponentsingivenimage.
##PRESERVATIONMANDATE:YouareanOCRsystem,NOTamathtutor.Yourjobistoorganizestudentwork,not
tocorrectit.Preservealloriginalcontentexactlyasthestudentwroteit.
Onceagain,**Neveroutputthegivenproblem.**
Figure5: PromptusedforGPT-basedOCRtoconvertstudents’handwrittenproblem-solvingprocessesintotext.
15

| system_msg = (   |            |     |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- | --- |
| "You are a LaTeX | OCR fixer. | "   |     |     |     |     |
"Your sole job is to correct OCR-induced errors in LaTeX while preserving meaning."
)
| guardrails = (   |                 |     |     |     |     |     |
| ---------------- | --------------- | --- | --- | --- | --- | --- |
| "You are a LaTeX | OCR fixer.\n\n" |     |     |     |     |     |
"STRICT RULES:\n"
"1) Fix ONLY OCR-induced errors in the provided LaTeX. Do not change mathematical meaning
| beyond what | is necessary | to  | correct | OCR mistakes.\n" |     |     |
| ----------- | ------------ | --- | ------- | ---------------- | --- | --- |
(cid:44)→
"2) Do NOT add explanations, comments, opinions, or extra text. Output MUST be only the
| corrected | LaTeX code.\n" |     |     |     |     |     |
| --------- | -------------- | --- | --- | --- | --- | --- |
(cid:44)→
"3) Use the provided references (problem statement, choices, model answer) strictly to
resolve ambiguities and to choose the correct symbols/operators/numbers. Prefer the
(cid:44)→
| minimal | edit that matches | the | references.\n" |     |     |     |
| ------- | ----------------- | --- | -------------- | --- | --- | --- |
(cid:44)→
"4) **Do NOT** introduce new steps, reorder lines, simplify, expand, compute results, or
rename variables unless correcting an OCR error that conflicts with the references.\n"
(cid:44)→
"5) Preserve structure and line breaks of the input LaTeX unless required to fix syntax or
| OCR mistakes. | Keep environments |     | (inline/display) |     | as-is where | possible.\n" |
| ------------- | ----------------- | --- | ---------------- | --- | ----------- | ------------ |
(cid:44)→
"6) **Ensure** syntactic validity: balanced braces, valid commands, proper math mode,
correct subscripts/superscripts, properly paired \\left ... \\right, etc.\n"
(cid:44)→
| "7) If the input | is already | correct, | return | it unchanged.\n" |     |     |
| ---------------- | ---------- | -------- | ------ | ---------------- | --- | --- |
"8) If the input is irrecoverably ambiguous, return the minimally fixed version that
| compiles, | without adding | any | new content.\n" |     |     |     |
| --------- | -------------- | --- | --------------- | --- | --- | --- |
(cid:44)→
)
rails = (
"OUTPUT CONTRACT:\n"
"- Return **ONLY** a single fenced code block labeled 'latex' containing the corrected
LaTeX.\n"
(cid:44)→
"- No surrounding prose, no markdown outside the code block, no comments.\n"
)
inputs = {
| "problem_text":         | problem,   |           |     |     |     |     |
| ----------------------- | ---------- | --------- | --- | --- | --- | --- |
| "solution_explanation": |            | solution, |     |     |     |     |
| "ocr_latex":            | ocr_latex, |           |     |     |     |     |
}
user_msg = (
| ((user_prompt.strip() | + "\n\n")            |     | if user_prompt      | else | "") + |     |
| --------------------- | -------------------- | --- | ------------------- | ---- | ----- | --- |
| (guardrails.strip()   | + "\n\n")            | +   |                     |      |       |     |
| rails + "\n\n"        | +                    |     |                     |      |       |     |
| "INPUTS(JSON):\n"     | + json.dumps(inputs, |     | ensure_ascii=False) |      |       |     |
)
Figure 6: Prompt used for refining the GPT-based OCR outputs to improve the accuracy and consistency of
transcribedstudentsolutionsinourKT-PSP-25.
16

| You are Teacher | GPT. |     |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
Your task is to analyze a given math Problem and its Unit name, and then generate a step-by-step
set of indicators that describe the process a student should ideally follow to solve the problem.
###Guidelines:
- The indicators must be organized into the four categories of Mathematical Proficiency:
| - Conceptual | Understanding |      | (CU) |     |     |     |     |
| ------------ | ------------- | ---- | ---- | --- | --- | --- | --- |
| - Procedural | Fluency       | (PF) |      |     |     |     |     |
| - Strategic  | Competence    |      | (SC) |     |     |     |     |
| - Adaptive   | Reasoning     | (AR) |      |     |     |     |     |
- However, instead of just listing general skills, write the indicators as concrete *steps*
| that a student | would | naturally | take | while solving |     | the given | problem. |
| -------------- | ----- | --------- | ---- | ------------- | --- | --------- | -------- |
- Each indicator should be prefixed with its category code (e.g., "CU1", "PF1", "SC2", "AR3").
- The order of the indicators should roughly follow the logical order of problem solving
(from initial understanding → strategy selection → execution → justification).
| - Output format | must | be a | JSON dictionary: |     |     |     |     |
| --------------- | ---- | ---- | ---------------- | --- | --- | --- | --- |
{
| "mathematical_proficiency_indicators": |        |     |     | [   |     |     |     |
| -------------------------------------- | ------ | --- | --- | --- | --- | --- | --- |
| "CU1":                                 | "...", |     |     |     |     |     |     |
| "SC1":                                 | "...", |     |     |     |     |     |     |
| "CU2":                                 | "...", |     |     |     |     |     |     |
...
]
}
---
| ### One-shot | Example |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- |
**Input**
Problem:Solvethedifferentialequation$(\frac{dy}{dx}=2x)$withinitialcondition$(y(0)=1)$."
| Unit: Differential |     | Equations |     |     |     |     |     |
| ------------------ | --- | --------- | --- | --- | --- | --- | --- |
**Output**
{
| "mathematical\_proficiency\_indicators": |            |                  |          |              | [      |             |                  |
| ---------------------------------------- | ---------- | ---------------- | -------- | ------------ | ------ | ----------- | ---------------- |
| {"CU1":                                  | "Determine | the              | type     | and order of | this   | equation"}, |                  |
| {"SC1":                                  | "Rewrite   | the              | equation | in an easier | way"}, |             |                  |
| {"CU2":                                  | "Write     | the mathematical |          | idea you     | need   | to solve    | this equation"}, |
{"CU3": "Give an example of how this equation will be applied in real life"},
{"CU4": "Find another differential equation whose solution steps are similar"},
| {"SC2": | "Sort    | the necessary |     | data and ignore | the | redundant | ones"}, |
| ------- | -------- | ------------- | --- | --------------- | --- | --------- | ------- |
| {"PF2": | "Predict | a solution"}, |     |                 |     |           |         |
{"CU5": "Show the steps for solving the equation using a table, a figure and a diagram"},
| {"PF1": | "Summarize | the        | steps     | in the solution"}, |            |             |     |
| ------- | ---------- | ---------- | --------- | ------------------ | ---------- | ----------- | --- |
| {"PF3": | "Write     | a suitable | algorithm | to                 | solve this | equation"}, |     |
{"SC3": "Identify any special numerical cases used by this equation to generalize the
solution"},
| {"AR1": | "Describe | your | solution | in general"}, |     |     |     |
| ------- | --------- | ---- | -------- | ------------- | --- | --- | --- |
{"AR2": "Based on your knowledge of differential equations, interpret your solution"},
| {"AR3": | "According | to  | your solution, | draw | the | conclusions"} |     |
| ------- | ---------- | --- | -------------- | ---- | --- | ------------- | --- |
]
}
—————————————————————————————————-
Problem(inKorean):{Problem_text}
{problem_option_string}
Unit(inKorean):{curriculum_theme_title}
Figure7: PromptusedforextractingtheMPindicatorsfromthegivenprobleminSTATUSKT.Promptinputsare
boldfaced.
17

You are Student GPT.
You will receive:
1. A math problem statement.
2. A set of indicators generated by Teacher GPT.
3. A student's written solution attempt (from OCR).
Your task:
- Pretend you are the student who wrote the solution.
- For each indicator, provide an answer based **only on the student's written solution**.
- If the student's solution clearly contains the relevant information, restate it as the
answer.
- If a step is missing but can be reasonably inferred (e.g., a basic algebraic manipulation
or obvious arithmetic), you may state it as: "Not written, but likely ...".
- Keep the student's mistakes. **Do not** correct them.
- If step looks incomplete or skipped, you can imagine that step and answer to indicator.
- If there is no evidence in the solution for an indicator, answer with: "I don't know"
**Output format**
Return your answers as a dictionary, and indicators should be written in Korean.
Output:
{
"CU1": "...",
"SC1": "...",
"CU2": "...",
...
}
---
### One-shot Example
Input Indicators:
{
"CU1": "Determine the type and order of this equation",
"SC1": "Rewrite the equation in a simpler form",
"AD1": "Identify the conditions required to solve the equation",
"PF1": "Compute the values that satisfy the conditions"
}
Question: Find the value(s) of y that make the following expression equal to 0.
y^2 + 3y + 2
My solving process (OCR):
`y^2 + 3y' + 2y = 0`
`(r+1)(r+2)=0`
My answer: -1, -2
Output:
{
"CU1": "This is a quadratic equation.",
"SC1": "Rewrite the characteristic polynomial as (r+1)(r+2)=0.",
"AD1": "If one of the multiplied factors is zero, the result becomes zero.",
"PF1": "The values that satisfy the condition are -1 and -2.."
}
———————————————————————————–
InputIndicators:{indicator_text}
Problem(inKorean):{problem}
{problem_option_string}
Mysolvingprocess(OCR):{student_solving_trace}
Myanswer:{solution_answer_sets}
Figure8: PromptusedforgeneratingresponsescorrespondingtoeachMPindicatorinSTATUSKT.Promptinputs
areboldfaced.
18

YouareTeacherGPT.Yourtaskistoevaluateastudent'sresponses(answer_indicate)
againstthereferencemathematicalproficiencyindicators(mathematical_proficiency_indicators).
##EvaluationRules
1.Foreachindicator:
-Ifthestudent'sresponseis**"Idon'tknow"**,assign0.
-Ifthestudent'sresponseis**"Notwritten,butlikely..."**,treatit
asthestudent'sactualanswerandevaluatenormally.
-Iftheresponsedoesnotmatchorisirrelevanttotheindicator,assign0.
-Iftheresponsematchestheindicator'sintentandshowscorrectreasoning/application,
assign1.
2.OutputstrictlyinJSONformat,withindicatorkeysmappedto0or1.
3.Ensurethateveryindicatoriscarefullyevaluatedwithoutskippingoroverlookinganyofthem.
##Input
Problem:
{problem_text}
mathematical_proficiency_indicators:
{mathematical_proficiency_indicatorsJSON}
answer_indicate:
{answer_indicateJSON}
##Output
ProvidetheevaluationresultinthefollowingJSONformat:
{
"CU1":0or1,"CU2":0or1,"SC1":0or1,"SC2":0or1,"PF1":0or1,"PF2":0or1,"AR1":0or1,"PF3":0or1,"PF4":0or1,"AR2":0or1
}
##InputExample
Problem:Fortherationalfunction$y=\\dfrac{2x-3}{2x+5}$,howmanypointsonitsgraphhaveboth
$x$-and$y$-coordinatesasintegers?
Options:[{"index":1,"text":"$1$"},{"index":2,"text":"$2$"},{"index":3,"text":"$3$"},
{"index":4,"text":"$4$"},{"index":5,"text":"$5$"}]
mathematical_proficiency_indicators:[
{"CU1":"Interpretwhattheproblemisasking,andrecognizethatitisaboutfindingpointsonthegraphoftherationalfunction
y=(2x-3)/(2x+5)whosex-andy-valuesarebothintegers."},
{"CU2":"Identifythedomainrestriction2x+5isnot0,andobservethatwhenxisaninteger,2x+5isalwaysodd."},
{"SC1":"Chooseastrategytorewritetheequationinaformthatmakestheintegerconditionmoreexplicit,suchasexpressingitinterms
ofy-1."},
{"PF1":"Transformy=(2x-3)/(2x+5)intoy-1=[(2x-3)-(2x+5)]/(2x+5)=
-8/(2x+5)."},
{"SC2":"Sinceymustbeaninteger,-8/(2x+5)mustbeaninteger;thusreinterpretthisasthedivisibilitycondition2x+5|8."},
{"AR1":"Usethefactthat2x+5isoddtorestrictthecandidatestotheodddivisorsof8."},
{"PF2":"Listthepossibledenominators:2x+5\in{1,-1}."},
{"PF3":"Solveforxforeachcandidate:2x+5=1=>x=-2;2x+5=-1=>x=-3."},
{"PF4":"Foreachx,computeyusingy=1-8/(2x+5):forx=-2=>y=-7;forx=-3=>y=9."},
{"PF5":"Verifythatthepoints(-2,-7)and(-3,9)satisfytheoriginalequationy=(2x-3)/(2x+5)."},
{"AR2":"Providereasoningthatonly+±1or-1canoccur,sinceallodddivisorsof8havebeenfullycheckedandnoothersarepossible."},
{"SC3":"Alternativecheck:assumingyisnotequalto1,setx=-(5y+3)/(2(y-1)).Letd=y-1.Thenx=-5/2-4/d,and
xisanintegeronlywhend=±8,confirmingthetwosolutions(-2,-7)and(-3,9)."},
{"CU3":"Counttheintegerlatticepointsobtainedandselectthecorrespondingchoicefrom
theansweroptions."}
]
answer_indicate:[
{"CU1":"Althoughnotwrittenexplicitly,byrewritingy=(2x-3)/(2x+5)asy=-8/(2x+5)+1andlistingpossiblevaluesof2x+5
tofindintegerpairs(x,y),itappearsthestudentrecognizedthetaskasidentifyingintegerlatticepoints."},
{"CU2":"Thestudentdidnotmentionthecondition2x+5isnotequalto0ortheobservationthat2x+5mustbeoddwhenxisaninteger.
Instead,theylistedalldivisorsof8(1,2,4,8,-1,-2,-4,-8)."},
{"SC1":"Theyrewrotey=(2x-3)/(2x+5)asy=-8/(2x+5)+1."},
{"PF1":"Althoughintermediatealgebrastepswereomitted,thefinalexpressiony-1=-8/(2x+5)wasobtained."},
{"SC2":"Theyinterpretedtherequirementthat-8/(2x+5)mustbeanintegerbyconsideringalldivisorsof8,listing
2x+5=1,2,4,8,-1,-2,-4,-8."},
{"AR1":"Theydidnotusetheconstraintthat2x+5mustbeodd,whichwouldreducethecandidatestotheodddivisorsonly."},
{"PF2":"Theylisted2x+5\in{1,2,4,8,-1,-2,-4,-8}aspossiblecandidates."},
{"PF3":"Theysolvedonlysomecandidates:2x+5=1=>x=-2,and2x+5=-1=>x=-3.Theremainingcaseswereleftincomplete
ornotshown."},
{"PF4":"Forx=-2andx=-3,they-valueswereleftblank;butlikelyx=-2=>y=-7,andx=-3=>y=9."},
{"PF5":"Idon'tknow."},
{"AR2":"Idon'tknow."},
{"SC3":"Idon'tknow."},
{"CU3":"Thestudenteventuallyselectedchoice(2)."}
]
Output:
{
"CU1":1,"CU2":0,"SC1":1,"PF1":1,"SC2":1,"AR1":0,"PF2":1,"PF3":1,"PF4":1,"PF5":0,"AR2":0,"SC3":0,"CU3":1
}
———————————————————————————–
Problem(inKorean):{problem}
{problem_option_string}
MathematicalProficiencyIndicators:
{indicator_text}
AnswerIndicate:{answer_indicator_text}
Figure9: Promptusedforevaluatestheappropriatenessofeachgeneratedresponseforitscorrespondingindicator
inSTATUSKT.Promptinputsareboldfaced.
19