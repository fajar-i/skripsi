Remembering is Not Applying: Interpretable Knowledge Tracing
for Problem-solving Processes
TaoHuang XinjiaOu HualiYang∗
CentralChinaNormalUniversity CentralChinaNormalUniversity WuhanTextileUniversity
Wuhan,Hubei,China Wuhan,Hubei,China Wuhan,Hubei,China
NingxiaNormalUniversity ouxinjia@mails.ccnu.edu.cn yanghuali@mail.ccnu.edu.cn
Guyuan,Ningxia,China
tmht@mail.ccnu.edu.cn
ShengzeHu JingGeng JunjieHu
CentralChinaNormalUniversity JianghanUniversity CentralChinaNormalUniversity
Wuhan,Hubei,China Wuhan,Hubei,China Wuhan,Hubei,China
hsz666@mails.ccnu.edu.cn gengjing@mails.ccnu.edu.cn jjboy23366@mails.ccnu.edu.cn
ZhuoranXu
CentralChinaNormalUniversity
Wuhan,Hubei,China
xuzhuoran@mails.ccnu.edu.cn
Abstract attributeslearnerperformancetosubjectiveproblems(difficulty,
KnowledgeTracing(KT)isacriticalserviceindistanceeducation, discrimination),objectiveknowledge(knowledgeacquisitionand
predictingstudents’futureperformancebasedontheirresponses application),andbehavior(guessingandslipping).Experimental
tolearningresources.Thereasonableassessmentoftheknowledge resultsshowPSKT’sadvantagesinpredictionaccuracy,reasonable
state,alongwithaccurateresponseprediction,iscrucialforKT. knowledgestateassessment,andlearningprocessexplanation.The
However,existingKTmethodsprioritizefittingresultsandover- codeisavailableathttps://github.com/Oia-10/PSKT.
lookattentiontotheproblem-solvingprocess.Theyequatethe
CCSConcepts
knowledgestudentsmemorizebeforeproblem-solvingwiththe
knowledgethatcanbeacquiredorappliedduringproblem-solving, •Appliedcomputing→Education;Distancelearning.
leadingtodramaticfluctuationsinknowledgestatesbetweenmas-
teryandnon-mastery,withlowinterpretability.Thispaperexplores Keywords
knowledgetransformationinproblem-solvingandproposesanin-
DistanceEducation,KnowledgeTracing,ProblemSolving
terpretable model, Problem-solving Knowledge Tracing (PSKT).
Specifically,wefirstpresentaknowledge-centeredproblemrepre- ACMReferenceFormat:
sentationthatenhancesitsexpressionbyadjustingproblemvariabil- TaoHuang,XinjiaOu,HualiYang,ShengzeHu,JingGeng,JunjieHu,
andZhuoranXu.2024.RememberingisNotApplying:InterpretableKnowl-
ity.Then,wemeticulouslydesignedaSequentialNeuralNetwork
edgeTracingforProblem-solvingProcesses.InProceedingsofthe32ndACM
(SNN)withthreestages:(1)Beforeproblem-solving,wemodelstu-
InternationalConferenceonMultimedia(MM’24),October28-November
dents’personalizedproblemspaceandsimulatetheiracquisitionof
1, 2024, Melbourne, VIC, Australia. ACM, New York, NY, USA, 9 pages.
problem-relatedknowledgethroughagatingmechanism.(2)Dur-
https://doi.org/10.1145/3664647.3681049
ingproblem-solving,weevaluateknowledgeapplicationandcalcu-
lateresponsewithafour-parameterIRT.(3)Afterproblem-solving,
1 Introduction
wequantifystudentknowledgeinternalizationandforgettingusing
anincrementalindicator.TheSNN,inspiredbyproblem-solving Digitalmultimediatechnologyenablesthecreationanddelivery
andconstructivistlearningtheories,isaninterpretablemodelthat ofhigh-qualityeducationalcontentinvariousdigitalformats,pro-
motingdistanceeducation’spopularization.Consequently,online
∗CorrespondingAuthor. teachingmodesrepresentedbyMOOCs,micro-courses,andblended
learninghaveemerged[12,13].Thephenomenonofknowledgere-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
versaloccurswheninstructionalprocedureseffectiveforbeginners
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation areineffectiveforexperts[17].Therefore,educatorsmustbeable
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe tocontinuouslyassessandmonitorlearners’knowledgemastery
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
duringthelearningprocesstodynamicallydetermineappropriate
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. teachingresources,especiallyinonlinelearningscenarios.
MM’24,October28-November1,2024,Melbourne,Australia Knowledgetracing(KT)isaninfluentialresearchareaindistance
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
education,whichcanautomaticallytrackstudents’knowledgelev-
ACMISBN979-8-4007-0686-8/24/10
https://doi.org/10.1145/3664647.3681049 elsatvariousstagesandhasbeenwidelyusedinadaptivelearning
3151

MM’24,October28-November1,2024,Melbourne,Australia TaoHuangetal.
Problem Solving Process
|     | P1 P2 | P3 P4 |      |     |     |     | known     |     |     |     |
| --- | ----- | ----- | ---- | --- | --- | --- | --------- | --- | --- | --- |
|     |       |       | 105o |     |     |     | condition |     |     |     |
130o
|     |     |     | 80o | po target |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |

|     |     |     | know n   co n d | it io n |     | 2   | ta rg e t |     |     |     |
| --- | --- | --- | --------------- | ------- | --- | --- | --------- | --- | --- | --- |
U n d er s ta n d ing  Knowledge retrieval   W r i te   down the  Feedback Improvement
|     |     |                 |             |                        |                  |     | Finding a so lu ti o n | an s w e r |                       |     |
| --- | --- | --------------- | ----------- | ---------------------- | ---------------- | --- | ---------------------- | ---------- | --------------------- | --- |
|     |     |                 | the problem |                        | and organization |     |                        |            |                       |     |
|     |     |                 |             | Before Problem Solving |                  |     | During Problem Solving |            | After Problem Solving |     |
|     |     | d i f f i c u l | t y         |                        |                  |     |                        |            |                       |     |
P4 d i s c r i m i nation s t e p 1 :   T h e   su m   o f   t h e   i n t e r ior  Internalized
|     |                       |             |     |     |     |     | a n g l e s   o f  a   q u a | d ri l a t e r a l   i s  ? |              |       |
| --- | --------------------- | ----------- | --- | --- | --- | --- | ---------------------------- | --------------------------- | ------------ | ----- |
|     | What is the size of a | n g l e   p | ？   |     |     | 5   |                              |                             |              | 1     |
|     |                       |             |     |     | 6   |     |                              |                             | 1            |       |
|     |                       |             |     |     |     |     | s t e p 2 :       3 6 0 - 1  | 0 5 - 8 0 - 1 3 0 = ?       |              |       |
|     | 1 0 5                 | o 130o      |     |     | 3   |     |   p                          |                             |  Forgot t  e | n5  2 |
|     |                       |             |     |     |     | 1   | step 3:         is ?         | 2                           |              |       |
8 0 o po
Remembered Knowledge  A4cqui re d   K2nowledge A p p l i e d  Knowledge U p dated Knowle dg e
|     |     |     |     |     |     |     |     |     |     | 4 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Knowledge Transformation
Figure1:Profilingthestudent’sproblem-solvingprocessinvolvescomprehendingtheproblembasedonmemorizedknowledge,
acquiringrelevantknowledge,applyingittofindasolution,andwritedowntheanswer.Feedbackthenhelpsinternalizethe
knowledge.Additionally,memorizedknowledgemaybeforgottenovertime.
systems [2, 19]. The goal of KT involves two stages. Firstly, as- shortperiod.Previouswork[33,42]hasnotedthisirrationalityand
sessingthedevelopmentofstudents’knowledgestatesaccording mitigatedthefluctuationsbydesigningapunishmentmechanism,
torecords,andsecondly,predictingtheirperformanceonspecific albeitatthecostofsacrificingthemodel’sperformance.
problemsusingtheassessedknowledgestates.Therefore,KToffers Toaddresstheirrationalityofknowledgestateassessment,en-
twokeyapplicationsforintelligenteducationalservices:dynamic hancemodelinterpretability,andimproveperformance,wedecon-
adjustmentofteachingstrategiesbasedonassessmentstatesand structstudents’learningprocessesfromtheperspectiveofhuman
personalizedresourcerecommendationbasedonpredictionresults. problem-solving.Engaginginexercisesisatypicalproblem-solving
EarlyKTmodels,suchasBayesianKnowledgeTracing(BKT) process.AsillustratedinFigure1,studentsenhancetheirunder-
[6,43]basedonHiddenMarkovModels,andPerformanceFactor standingofproblemsthroughdeepthinking,continuouslyexplore
Analysis[29]basedonlogisticfunctions,usededucationalparam- solutions,andultimatelyachieveconsolidationofknowledge.The
eters to estimate students’ mastery probabilities. These models entireproblem-solvingprocessinvolvestheacquisition,applica-
werecharacterizedbyhighinterpretabilitybutlowprecisionin tion,internalization,andforgettingofmemorizedknowledgeinthe
prediction.Assmarteducationprogresses,deeplearning-basedap- brain.However,existingKTmethodsoverlooklearners’problem-
proaches(DLKT)havebecomemainstream,significantlyimproving solvingprocesses,equatingmemorizedknowledgewithacquired
theperformanceofKTtasks[11,25,30,34,44].However,duetothe orappliedknowledge,leadingtodrasticfluctuationsinknowledge
black-boxnatureofdeeplearning,thesemodelshavelowertrans- states.Accordingtoproblem-solvingtheory[3,8,9,26],knowledge
parencyandinterpretability.Similartohowgoodteachersneed acquisitioninvolveslearnersorganizingimplicitandexplicitknowl-
tounderstandstudents,agoodKTmodelshouldprovidehigher- edgerelevanttoproblems,whileknowledgeapplicationinvolves
valueeducationalservices,suchasattributionanalysis,whichhelps applyingthisknowledgetoseekasolution.Rememberingdoesnot
understandthe’why’-notjustthe’what’. equalapplying.Familiaritywithdiscreteknowledgeconcepts(KCs)
Fortunately,manyDLKTmethodsareaddressingthisissueby doesnotimplythatstudentscaneffectivelyorganizethemorcon-
enhancingtheinterpretabilityoftheirmodels.MethodslikeDeep- vertabstractknowledgeintospecificapplicationswhenanswering
IRT [41] and Deep-IRTw [37] combine KT with Item Response problems.Thecommonsayingthatknowingthepathandwalking
Theory(IRT).SAKT[27]andAKT[11]useattentionweightsto thepatharetwodifferentthingsreflectsthisphenomenon.Therefore,
explainrelationshipsbetweenhistoricalinteractions.IKT[22]sets ourworkdelvesintovariousstagesofproblem-solving,reproduc-
knowledgemastery,learningtransferability,andproblemdifficulty ingthelearningprocessbyanalyzinghowstudentsunderstand
asthreeeducationallymeaningfulparameters.RCKT[7]andCMKT problems,acquire,apply,internalize,andforgetknowledge.
[46]enhancemodelinterpretabilitythroughcausalinference. Inthispaper,consideringtheeffectsofknowledgetransforma-
However,theaforementionedmethodsprimarilyfocusonpredic- tion mentioned above, we propose an interpretable knowledge
tionandoverlookthelearningprocess,leadingtoanunreasonable tracingapproachforproblem-solvingprocesses(PSKT).InPSKT,
assessmentofknowledgemasterypatterns.LPKT[32]recognized wefirstenhancetherepresentationofknowledge-centeredprob-
thelimitationsofpreviousmodels,whichassumedthatlearners’ lems by learning the rich attributes of the problem. Then, we
knowledgestateswoulddeclineoncetheyansweredincorrectly. presentaSequentialNeuralNetwork(SNN)tosimulateknowledge
LPKTappliedknowledgegaintomeasurethevalueoferrorinter- transformationintheproblem-solvingprocess.Beforeproblem-
actions.Fromacognitiveperspective,learners’knowledgemastery solving,PSKTmodelsstudents’personalizedproblemspaceand
| curve | is relatively | stable | and does not | fluctuate | drastically | in a |     |     |     |     |
| ----- | ------------- | ------ | ------------ | --------- | ----------- | ---- | --- | --- | --- | --- |
3152

RememberingisNotApplying:InterpretableKnowledgeTracingforProblem-solvingProcesses MM’24,October28-November1,2024,Melbourne,Australia
knowledgeacquisitiondegree.Duringtheproblem-solvingpro- knowledgemastery.[11,16,27]useattentionmechanismtomodel
cess,PSKTcaptureslearners’goal-orientedknowledgeapplication therelationshipbetweeninteractionhistories,and[25,35,39]apply
andattributeslearners’responsethrougheducationalparameters, graphneuralnetworkstomodelthegraphstructurebetweenKCs.
namelyproblemfactors(difficulty,discrimination),learnerknowl- Recentresearchhasemphasizedtheimportanceofmodelingthe
edgefactors(knowledgeacquisitionandapplication),andlearner learningprocess.LPKT[32]andFKT[15]finelymodellearning
behaviorfactors(guessing,slipping).Afterproblem-solving,PSKT andforgettingbyincorporatingresponsetimeandintervaltime.
designs an update indicator to measure the degree of learners’ LBKT[38]highlightedtheimpactofansweringspeed,prompts,
knowledgeinternalizationandmodelstheforgettingeffectover andotherbehaviors.However,thesemodelssufferfrompoorinter-
time. Finally, we conducted extensive experiments on five real- pretabilityandcontrollability.Incontrast,ourprimaryfocusison
worlddatasets,demonstratingtheeffectivenessofPSKT.Addition- providingreasonablepredictiveexplanationsfromaneducational
ally,PSKTshowedoutstandingperformanceinmodelingreasonable perspective.Wedisaggregatestudents’problem-solvingprocesses
knowledgestates,explainingprediction,andlearningreliableprob- tomakemultifacetedattributionsofansweringresponses,rather
lemdifficulty.Themaincontributionsofourpaperaresummarized thanfocusingonadditionalfeaturesofthelearningprocess.
asfollows:
• Wequantifythelearner’sknowledgetransformationbyde- 3 ProblemDefinition
constructing the process of solving a particular problem, Supposethatinanonlinelearningplatform,thereisasetofstudents
ensuringthatknowledgestatechangingisreasonableness. 𝑆 = (cid:8)𝑠 1 ,𝑠 2 ,...,𝑠 |𝑆| (cid:9) ,asetofproblems𝑃 = (cid:8)𝑝 1 ,𝑝 2 ,...,𝑝 |𝑃| (cid:9) ,anda
• WeproposeanovelSequentialNeuralNetwork(SNN).The setofknowledgeconcepts𝐾 = (cid:8)𝑘 1 ,𝑘 2 ,...,𝑘 |𝐾| (cid:9) .Wedenotetheex-
designoftheSNNfollowstheproblem-solvingtheoryand erciserecordsofastudentas𝑋 𝑁 ={𝑋 1 ,𝑋 2 ,...,𝑋 𝑁},where𝑁 rep-
theactiveconstructionprincipleofconstructivistlearning resentsthetotalnumberofexercises.𝑋
𝑛
=(𝑡𝑠
𝑛
,𝑝
𝑛
,𝑘
𝑛
,𝑟 𝑛),𝑛∈𝑁
theory,providinggoodinterpretability. isthemostbasicpracticeunit,denotingthatthestudent’sresponse
• ExtensiveexperimentsdemonstratetheeffectivenessofPSKT. toproblem𝑝 𝑛attimestamp𝑡𝑠 𝑛is𝑟 𝑛.Where𝑟
𝑛
∈{0,1},0denotes
anincorrectanswerand1denotesacorrectanswer.
2 RelatedWork
ProblemDefinition.Givenastudent’shistoricallearningse-
2.1 ItemResponseTheory quence𝑋 𝑛,thetaskofKTistoevaluatethestudent’sknowledge
statesbasedon𝑋 𝑛 andpredicttheprobabilityofcorrectlyanswer-
ItemResponseTheory(IRT)isaclassicmeasurementtheoryrooted
ineducationandpsychology.Itcalculatestheprobabilityofacor-
ingthenextproblem,thatis,𝑝(𝑟 𝑛+1 =1|𝑝 𝑛+1 ,𝑋 𝑛).
rectresponsebasedonthestudent’slatenttraitsandtheproblem’s
4 ThePSKTModel
characteristics.AlthoughthetraditionalIRTmodelishighlyinter-
pretable,ittreatsstudents’latenttraitsasstaticparameters,making Studentsincreasetheirknowledgebypracticingproblems,sothe
itsuitableonlyforsingleassessments.RecognizingIRT’slimita- coreofPSKTisquantifyinglearners’knowledgegrowthbyde-
tions,manyresearchershaveincorporateditintoKTforprocess constructingtheirproblem-solvingprocess.AsshowninFigure2,
assessment.[18]integrateIRTandBKTmodelstomodelstudents’ tomodelthelearners’problem-solvingprocessandanalyzetheir
learningabilities.Deep-IRT[41]fitsstudentabilitythroughDKVMN knowledgetransformation,wedesignedasequenceneuralnetwork
[44]andusesIRTtocomputetheprobabilityofacorrectresponse. (SNN).ThePSKTmodelcomprisesfourmainmodules:problem
AKT[11]usesIRTtoenhancethepersonalizedembeddingofques- representation,knowledgeacquisition,application,andupdating.
tionsandresponses,whilePKT[33]appliesIRTtofitstudents’ First,wepresentaknowledge-centeredproblemrepresentation
knowledgemasterystates.PSKT,inspiredbyIRT,attributesan- thatenhancesitsexpressionbyadjustingproblemvariability.Then,
sweringperformancetoobjectiveproblemfactors(difficulty,dis- wemodellearners’personalizedproblemperceptionandknowl-
crimination)andsubjectivelearnerfactors(knowledgeapplication, edgeacquisitiondegreeintheknowledgeacquisitionmodule.Next,
guessing,andslipping).Thesericheducationalparametersmake PSKTmeasurestheknowledgeapplicationlevelbasedonknowl-
ourmodelinterpretablewhilemaintainingaccuracy. edgeacquisitionandcalculatesproblemresponsebyIRT.Finally,
theknowledgeupdatemodulequantifiesthedegreeofknowledge
2.2 KnowledgeTracing internalizationandforgetting.ThedesignoftheSNNisinspired
byproblem-solvingtheory[9]andconstructivistlearningtheory
Knowledgetracingtracksstudents’dynamicknowledgestatesby
[10],ensuringgoodinterpretability.
modelingtheirhistoricallearningsequences.Itissuitableformul-
tipleassessmentscenariosandperformsprocessmeasurementson
4.1 ProblemRepresentation
students.EarlyKTmethodswerebasedonhiddenMarkovmodels,
whichevaluatedstudentperformancebymodelingfourparame- Understandingthenature,scope,andrelevantfactorsofaproblem
ters:initialmastery,knowledgemasterytransformation,guessing isaprerequisiteforsolvingit.EarlyKTmethodsusedKCstoreplace
andslipping[6,28,43].Neuralnetworkshavegreatlyimproved problems,ordirectlyconcatenatedproblemsandKCs.However,
theperformanceofKTandhavebecomethecurrentmainstream thesemethodssimplyfusedinformationwithoutconsideringthe
method.DKT[30]introduceddeeplearningintoKTforthefirst primaryandsecondaryrelationshipsoftheproblems.Sincethe
timeandappliedRNN/LSTMtomodelstudents’knowledgechanges. goalofexercisesistolearnknowledge,theKCsexaminedbythe
Subsequentwork[20,24,42]improveduponthisbasis.[1,41,44] problemsareofutmostimportance.Moreover,problemsthattest
usememorynetworkstostorepotentialKCsandupdatestudents’ thesameKCscanhavedifferenteffectsonlearningandperformance
3153

OO O PP P
|     |     |     |     | SS S PP P |     | nn n |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
nn n
|     |     |     |     |     | EE E PP P |     | OO PP |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | nn n      |     | nn    |     |     |     |     |     |     |     |
EEPP
MM’24,October28-November1,2024,Melbourne,Australia SS PP nn TaoHuangetal.
nn
|     |     | Input     |             |                             |         |     |     | Sequential Neural Network (SNN) |                           |           | ˆr                    |         |        |     |
| --- | --- | --------- | ----------- | --------------------------- | ------- | --- | --- | ------------------------------- | ------------------------- | --------- | --------------------- | ------- | ------ | --- |
|     |     | P R K     | TS −TS      |                             | Before  |     |     |                                 | During                    |           | n                     | After   |        |     |
|     |     | n n       | n n+1       | n                           |         |     |     |                                 |                           |           |                       |         |        |     |
|     |     |           |             |                             |         |     |     |                            |                      |      |                  |         |        |     |
|     |     |           |             |                             | SPn SPn |     |     | G 1                             | − 1( +                    | (1 − Sn ) | 1(                    |         |        |     |
|     |     |           |             |                             |         |     |     | n                               | 1 + e − D  n KP n − dn ) | 1 +       | e − D  n KP n − dn ) |         |        |     |
|     |     |           | P           |                             |         |     |    |                                 |                           |           | K A n KP              | n RR nn |        |     |
|     |     |           | n           | EPn EPn                     |         |     |     |                                 |                           |           |                       |         | HH     |     |
|     |     |           |             |                             |         |     |     | EPn                             |                           |           |                       |         | nn     |     |
|     |     |           |             |                             | OPn OPn |     |     |                                 |                           |           | dd                  |         |        |     |
|     |     | K + (   | d +   )n |  P                         |         |     |     |                                 |                           |           | nn nn                 |         |        |     |
|     |     | n         | n           | n                           |         |     |     | KA                              |                           |           | SS                    |         |        |     |
|     |     |           |             | Problem Space Problem Space |         |     |     | n                               |                           | GG        | nn nI                 | HH      |        |     |
|     |     |           |             |                             |         |     |     |                                 |                           | nn        |                      |         | nn−−11 |     |
et
nr
zil a
|     |     | K   | d   |    |     |     | tanh |     | KK PP nn |        |           |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- | ------ | --------- | --- | --- | --- |
|     |     | n   | n   | n   |     |     |      |     |          | MMLLPP | MMLLPP ni |     |     |     |
g
tanh
(tanh+1)/2
|     |     |     | MMLLPP | MMLLPP |     |        |     |     |     |     |        |        |        |     |
| --- | --- | --- | ------ | ------ | --- | ------ | --- | --- | --- | --- | ------ | ------ | ------ | --- |
|     |     |     |        |        |     |        |     |     |     |     |        | SSPPnn | TS −TS |     |
|     |     |     |        | P      | HH  |        | SPn | OPn |     | PP  |        |        | n+1 n  |     |
|     |     |     | PP     |        | n   | nn−−11 |     |     |     | nn  | EEPPnn |        |        |     |
nn Perception Acquisition Application Answering OOPPnn  Forgetting
Problem Representation Knowledge Acquisition Knowledge Application Knowledge Updating
Figure2:ThearchitectureofthePSKTmodel.
duetodifferencesindifficultyanddiscrimination.InthePSKT,we derivedfromthelearner’spreviousknowledgestateH𝑛−1.Weuse
considerboththeprimary-secondaryrelationshipsandproblem thetanhtogeneratecandidatevalues.Thespecificformulais:
attributesto e n ha n ce p ro b l e m re p r e s e n ta ti on : (cid:16) (cid:17)
|     |     |     |          |          |             |        |     |     | KA𝑛 | =tanh | W 𝑇 (SP𝑛 | ⊕H𝑛−1 )+b𝐾𝐴 | ,   | (5) |
| --- | --- | --- | -------- | -------- | ----------- | ------ | --- | --- | --- | ----- | -------- | ----------- | --- | --- |
|     |     |     | (cid:16) | (cid:17) |             |        |     |     |     |       | 𝐾𝐴       |             |     |     |
|     |     | 𝑝 𝑎 | = 𝜎 W 𝑇  | P + b    | , 𝑝 𝑎 ∈ { 𝑑 | ,𝛼 𝑛}, | (1) |     |     |       |          |             |     |     |
|     |     | 𝑛   | 𝑝        | 𝑎 𝑛 𝑝 𝑎  | 𝑛 𝑛         |        |     |     |     |       |          |             |     |     |
sincelearnershavelimitedmemorycapacity,theywillselectively
P(cid:102)𝑛 =K𝑛+(𝜙×𝑑 𝑛+𝜑×𝛼 𝑛)×P𝑛 , (2) focusonthemostrelevantandcoreaspectsoftheproblemduring
∈R𝑑ℎ×1,𝑑 theknowledgeacquisitionprocessinordertoconductmoreeffec-
| whereW𝑝𝑎 |     |     | ℎ   | isembeddingdimension.𝑑 |     | 𝑛 isdifficulty, |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | ---------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tiveplanning[8].Therefore,wefurtherdesignagatetoselectand
𝛼 𝑛 isdiscrimination,andbotharescalars.Therepresentationis
inspiredby𝑚𝑒𝑎𝑛±𝜇·𝑠𝑡𝑑.K𝑛istheKCembedding,P𝑛istheoriginal retaintheessentialpartsthroughtheprobleminformation.
problemembedding.(𝜙×𝑑 𝑛+𝜑×𝛼 𝑛)iscoefficientofvariation, 𝐾𝐴 (cid:16) 𝑇 (cid:17)
|                         |     |     |     |     |     |     |     |     | Γ   | =𝜎 W | (SP𝑛 ⊕EP𝑛 | ⊕OP𝑛)+bΓ𝐾𝐴 | ,   | (6) |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---------- | --- | --- |
| 𝜙,𝜑aretrainableweights. |     |     |     |     |     |     |     |     | 𝑛   |      | Γ𝐾𝐴       |            |     |     |
𝐾𝐴
|     |     |     |     |     |     |     |     |     |     |     | K(cid:103)A𝑛 =Γ ×KA𝑛 | ,   |     | (7) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
𝑛
| 4.2 | KnowledgeAcquisition |     |     |     |     |     |     |     |     |     | ∈R2|𝐾|×|𝐾|,WΓ𝐾𝐴 |     | ∈R3|𝐾|×|𝐾|. |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- |
where𝜎issigmoid,W𝐾𝐴
Accordingtoproblem-solvingtheory,knowledgeacquisitionre-
quireslearnerstofirstclarifytheproblem,ensureanunderstanding 4.3 KnowledgeApplication
ofcriticalaspectsoftheproblem(problemperception),andthen
Acquiringknowledgeisonlythebeginningofproblem-solving.
acquireknowledgeabouttheproblem(knowledgeacquisition).
Whatismoreimportantishowtoapplyknowledgetoactualprob-
(1)ProblemPerception.Thelearner’ssolutiontoaproblem lemsorsituations.Duringpractice,learnerstransformacquired
beginswiththeconstructionofaninternalrepresentationofthe
theoreticalknowledgeintopracticalabilities,proposesolutions
externalproblemstatement,i.e.,the"problemspace"(including
(knowledgeapplication),andthenimplementactionstoachieve
theinitialstate,thegoalstate,andtheadaptedoperators)[14].To
theexpectedgoals(problemanswering).
simulatethelearner’spersonalizedperceptionoftheproblem,we
(1)KnowledgeApplication.Knowledgeapplicationinvolves
| integrate |     | the learner’s | prior | knowledge | H𝑛−1 | and problem | rep- |     |     |     |     |     |     |     |
| --------- | --- | ------------- | ----- | --------- | ---- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
transformingabstractknowledgeintoconcreteactionplansand
| resentationP(cid:102)𝑛 |     | torepresenttheinitialstateandgoalstateinthe |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
adaptingandrefiningtheseinpractice.Thesolutioniscontainedin
problemspace.WeusethedifferencebetweenthegoalstateEP𝑛
theadaptedoperatorsofproblemspace,andweusetanhtogenerate
andtheinitialstateSP𝑛torepresenttheapplicableoperationsOP𝑛:
possiblesolutions.Learnersneedtoflexiblyapplyknowledgeto
|     |     |     | (cid:16) | (cid:17) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑇 ,PP𝑛 ,EP𝑛}, makeaseriesofdynamicdecisionsandcontinuouslymonitorthe
|     | PP𝑛 | =W 𝑃𝑃 | P(cid:102)𝑛 ⊕H𝑛−1 | +b𝑃𝑃 | ∈{SP𝑛 |     | (3) |     |     |     |     |     |     |     |
| --- | --- | ----- | ----------------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consequencesofthesedecisionstoachievethegoalasmuchas
|     |     |     | OP𝑛 | =EP𝑛−SP𝑛 | ,   |     | (4) | possible.Therefore,wedesignedagateΓ𝐾𝑃 |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
ledbyproblemgoals
|     |     |     |     | ∈R(𝑑ℎ+|𝐾|)×|𝐾| |     | and|𝐾|isthetotal |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
where⊕isconcatenate,W𝑃𝑃 andknowledgeacquisitiontodeterminethelearner’sfinalsolution.
numberofKCs.
|     |     |     |     |     |     |     |     |     |     |     | (cid:16) (cid:16) | (cid:17) | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | -------- | --- |
(2)KnowledgeAcquisition.Knowledgeacquisitioninvolves Γ 𝐾𝑃 =𝜎 W 𝑇 EP𝑛 ⊕K(cid:103)A𝑛 +bΓ𝐾𝑃 , (8)
|     |     |     |     |     |     |     |     |     | 𝑛   |     | Γ𝐾𝑃 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesystematicgenerationandintegrationofinformation.Thisin-
𝐾𝑃
|     |     |     |     |     |     |     |     |     |     | K(cid:103)P𝑛 | =Γ 𝑛 ×tanh(OP𝑛). |     |     | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | --- | --- | --- |
cludesacquiringknowledgefromtheexternalenvironmentaswell
asconstructingnewknowledgethroughinternalthoughtprocesses. (2)ProblemAnswering.Applyingknowledgeistoachieve
IntheKTscenario,externalknowledgecomesfromtheinitialstate goals.IRTshowsthatwhetherstudentscananswerproblemscor-
oftheproblemSP𝑛(knownconditions),andinternalknowledgeis rectlydependsnotonlyontheirknowledgeapplicationbutalsoon
3154

RememberingisNotApplying:InterpretableKnowledgeTracingforProblem-solvingProcesses MM’24,October28-November1,2024,Melbourne,Australia
theproblemitself.InspiredbytheFour-parameterIRTandBKT,we Table1:Detailsofthealldatasets.
simulatestudents’responsesbyfullyconsideringproblemfactors
(difficulty,discrimination),learnerknowledgefactors(knowledge datasets Students Problems KCs Responses
application),andlearnerbehavioralfactors(guessingandslipping).
|     |     |     |     |     |     |     |     | ASSIST12 | 29,018 | 53,091 | 265 2,711,813 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | ------------- | --- |
Thecorefunctionsareasfollows:
|     |     |          |     |                   |     |                   |          | ASSIST17 | 1,709 | 3,162 | 102 942,816 |     |
| --- | --- | -------- | --- | ----------------- | --- | ----------------- | -------- | -------- | ----- | ----- | ----------- | --- |
|     |     | (cid:16) |     | (cid:16) (cid:16) |     | (cid:17) (cid:17) | (cid:17) |          |       |       |             |     |
|     |     | =𝜎       | 𝑇   | 𝑇                 |     |                   |          |          |       |       |             |     |
K(cid:100)P𝑛 W ·ReLU W K(cid:103)P𝑛 ⊕P(cid:102)𝑛 +b1 +b2 (10) EdNet-KT1 100,000 12,267 189 12,092,643
|        |      |         | 2               | 1        |           |     |                    |       |         |        |                  |     |
| ------ | ---- | ------- | --------------- | -------- | --------- | --- | ------------------ | ----- | ------- | ------ | ---------------- | --- |
|        |      |         |                 |          |           |     |                    | Junyi | 247,606 | 722    | 41 25,926,003    |     |
|        |      |         |                 |          |           |     |                    | Eedi  | 118,971 | 27,613 | 1,989 15,867,850 |     |
|        |  |         | 1               |      |       |     | 1 ,            |       |         |        |                  |     |
| 𝑟ˆ𝑛 =𝐺 |      |         |                 | +(1−𝑆    |           |     |                    |       |         |        |                  |     |
|        | 𝑛 1− |         | (cid:16)        | (cid:17) | 𝑛)        |     | (cid:16) (cid:17)  |       |         |        |                  |     |
|        |    | 1+𝑒−𝐷𝛼𝑛 | K(cid:100)P𝑛−𝑑𝑛 |        | 1+𝑒−𝐷𝛼𝑛 |     | K(cid:100)P𝑛−𝑑𝑛  |       |         |        |                  |     |
    continuousprocess[21].Therefore,currentknowledgemaybefor-
(11)
|     |     | ∈R(|𝐾|+𝑑ℎ)×𝑑ℎ,W2 |     | ∈R𝑑ℎ×|𝐾|.ThefirstterminEqua- |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whereW1 gottenovertimeintervals.Inordertomodelthecomplexforgetting
tion(11)representstheprobabilitythatthelearnerhasnotmastered effect,wedesignaforgettinggateasfollows:
|     |     |     |     |     |     |     |     |     | (cid:16) | (cid:16) | (cid:17) | (cid:17) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | -------- |
t h e k n o w le d g e b u t gu e s s ed co rr e c t l y , a nd t h e s e c o n d te r m in d ic a te s Γ 𝐾𝐹 =𝜎 W 𝑇 IT𝑛 ⊕P(cid:157)𝑛+1 ⊕H(cid:102)𝑛 +bΓ𝐾𝐹 , (16)
|        |            |            |           |                     |              |                 | 𝐷            |     | 𝑛 Γ𝐾𝐹 |     |     |     |
| ------ | ---------- | ---------- | --------- | ------------------- | ------------ | --------------- | ------------ | --- | ----- | --- | --- | --- |
| t h at | t h e le a | r n er c a | n a n s w | er co r r e c t l y | w it h o u t | s l ip p in g . | is a c o n - |     |       |     |     |     |
stantwithavalueof4×1.7[4].𝐺 𝑛isguessing,and𝑆 𝑛isslipping: H𝑛 =Γ 𝐾𝐹 ×H(cid:102)𝑛 , (17)
𝑛
(cid:16) 𝑇 (cid:16) (cid:17) (cid:17) w h e re t i m e in te r v a l i s 𝑖 𝑡 𝑛 = 𝑡 𝑠 𝑛 − 𝑡𝑠 𝑛 ,i n m in u te s. I T 𝑛 is em b e d d i ng
𝐺𝑆 𝑛 =𝜆×𝜎 W K(cid:100)P𝑛 ⊕P(cid:102)𝑛 +b𝐺𝑆 ,𝐺𝑆 𝑛 ∈{𝐺 𝑛 ,𝑆 𝑛}, (12) + 1
𝐺𝑆 of 𝑖 𝑡 , a n d w e s e t a l l i n ter v a l s g r ea te r t ha n 1 m o n t h to 1 m o n t h .
𝑛
where𝜆ishyperparameter,indicatingthethresholdofguessing
|     |     |     | ∈R(|𝐾|+𝑑ℎ)×1. |     |     |     |     | 4.5 ObjectiveFunction |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
andslipping,W𝐺𝑆
TotrainallparametersΘinPSKT,weusecross-entropylogloss
4.4 KnowledgeUpdating betweenthepredictedresponse𝑟ˆ𝑛 andtheactualresponse𝑟
𝑛 as
Afterpractice,thelearner’sknowledgestatechanges.Constructivist theobjectivefunction,minimizedwiththeAdamoptimizer:
| learningtheory[10]suggeststhatincreasingknowledgemastery |     |     |     |     |     |     |     |     | 𝑁   |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∑︁
reflectsknowledgeinternalizationwhileforgettingleadstoare- L𝑟(Θ)= −[𝑟 𝑛log𝑟ˆ𝑛+(1−𝑟 𝑛)log(1−𝑟ˆ𝑛)],
(18)
ductioninknowledge.Thus,learnerstateupdatingincludesboth
𝑛=1
knowledgeinternalizationandforgetting.
(1)Knowledgeinternalizing.Knowledgeinternalizingishow
5 Experiments
learnerstransformexternalknowledge,experienceorinformation
Weconductextensiveexperimentstoanswerthesequestions:
intothinkingstructuresandcognitivepatterns.Intheproblem-
• RQ1.WhatisthepredictiveperformanceofPSKT?
solvingprocess,thelearner’snewknowledgeoriginatesfromthe
• RQ2.CanPSKTreasonablyexplainthelearningprocess?
problems,sowefusealltheinformationoftheproblemstoobtain
•
thecandidatevalueofknowledgeincrement.Constructivistlearn- RQ3.HoweffectiveistheproblemrepresentationofPSKT?
• RQ4.WhatistheimpactofeachelementinPSKT?
ingtheoryshowsthatlearningisanactiveconstructionprocess,so
wetendtothinkthattheentirepracticeprocesspositivelyimpacts
5.1 ExperimentalSetting
learners,anduse(tanh((cid:133))+1)/2asanon-negativeconstraintop-
eratortoensurethattheincrementisnon-negative. 5.1.1 Dataset. Weselectedfivelargepublicdatasetstoevaluatethe
|     |       |                   |        |                |     |                   |          | e ff e c ti v e n | es s o f P S K T : A S | S I ST 1 2 1 ,A SS | I S T 1 7 2 , E d N e t -K | T 1 3, J u n y i 4, |
| --- | ----- | ----------------- | ------ | -------------- | --- | ----------------- | -------- | ----------------- | ---------------------- | ------------------ | -------------------------- | ------------------- |
|     |       | (cid:16) (cid:16) | 𝑇      |                |     | (cid:17) (cid:17) |          |                   |                        |                    |                            |                     |
|     | KI𝑛 = | tanh              | W (SP𝑛 | ⊕EP𝑛 ⊕OP𝑛)+b𝐾𝐼 |     | +1                | /2. (13) | i5                |                        |                    |                            |                     |
𝐾𝐼 E e d . T h e s ta t is t ic a l in f o r m a ti o n of d a t as e t s i s s h o w n i n T a b l e 1 .
Wefilteredlearningrecordsforalldatasetswithmissingrelevant
Throughinternalization,learnersdonotsimplyacceptinformation
KCsandremovedproblemswithfewerthan10occurrencesand
butintegrateitintotheircognitiveframework.Thus,evenifdiffer-
learnerswithfewerthan3responserecords.Duetothelargesize
entlearnersanswerthesameproblem,thelevelofknowledgethey
oftheEdnet-KT1,werandomlyselected100,000learners[33,40].
internalizewillbedifferentduetodifferencesintheknowledge
FordatasetswhereaproblemassessesmultipleKCs,weusethe
theyacquire,theknowledgetheyapply,andtheresultsoftheir
averageofallKCembeddingstorepresentthefinalKCembedding.
answers.Tothisend,weproposeagrowthindicatortodetermine
thelearner’spersonalizedknowledgeincrement. 5.1.2 TrainingDetails. Allinputsequenceswerefixedatalengthof
100.Longersequencesweresplitintoseveraluniquesubsequences.
|     |     | 𝐾𝐼  | (cid:16) 𝑇 | (cid:16)                   | (cid:17) | (cid:17) |        |     |     |     |     |     |
| --- | --- | --- | ---------- | -------------------------- | -------- | -------- | ------ | --- | --- | --- | --- | --- |
|     | Γ   | =𝜎  | W          | K(cid:103)A𝑛 ⊕K(cid:103)P𝑛 | ⊕R𝑛      | +bΓ𝐾𝐼    | , (14) |     |     |     |     |     |
𝑛 Γ𝐾𝐼 Weused5-foldcross-validation:80%ofthesequencesweresplit
intotrainingandvalidationsets(8:2),and20%servedasthetestset.
𝐾𝐼
H(cid:102)𝑛 =H𝑛−1 +Γ ×KI𝑛 , (15) Parameters𝑑 ℎ,learningrate,and𝜆weresetto256,0.001,and0.5,
𝑛
∈R(2|𝐾|+𝑑ℎ)×|𝐾|. 1https://sites.google.com/site/assistmentsdata/2012-13-school-data-withaffect
whereR𝑛isresponseembedding,WΓ𝐾𝐼
2https://sites.google.com/view/assistmentsdatamining/dataset
| (2) | Knowledge |     | Forgetting. | Limited | by the | human | memory |     |     |     |     |     |
| --- | --------- | --- | ----------- | ------- | ------ | ----- | ------ | --- | --- | --- | --- | --- |
3https://github.com/riiid/ednet
system,althoughlearnersmaydelaytheoccurrenceofforgetting 4https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=1198
throughreviewandreinforcementlearning,forgetting isstilla 5https://eedi.com/projects/neurips-education-challenge
3155

MM’24,October28-November1,2024,Melbourne,Australia TaoHuangetal.
Table2:Comparativeresultsofstudentresponseprediction.Thebestresultsareinbold,andthenextbestareunderlined.*
indicatesp-value<0.05inthet-testcomparedtothesecond-bestresult.
Datasets Metrics DKT DKVMN SAKT Deep-IRT DKT-F AKT SAINT LPKT ATDKT FKT PKT PSKT
AUC 0.7191 0.7261 0.7741 0.7660 0.7504 0.7938 0.7856 0.7974 0.7631 0.7931 0.7938 0.8252∗
ASSIST ACC 0.7313 0.7301 0.7553 0.7522 0.7451 0.7664 0.7640 0.7692 0.7519 0.7667 0.7647 0.7838∗
-12 RMSE 0.4272 0.4258 0.4090 0.4116 0.4169 0.4006 0.4037 0.3987 0.4120 0.4006 0.4011 0.3858∗
R2 0.1354 0.1410 0.2077 0.1992 0.1786 0.2415 0.2305 0.2468 0.1976 0.2400 0.2398 0.2966∗
AUC 0.7295 0.7511 0.7355 0.7500 0.7518 0.7781 0.7649 0.8058 0.7488 0.7888 0.7947 0.8182∗
ASSIST ACC 0.6940 0.7043 0.7053 0.7139 0.7054 0.7210 0.7113 0.7414 0.7026 0.7326 0.7327 0.7503∗
-17 RMSE 0.4454 0.4379 0.4419 0.4364 0.4376 0.4308 0.4323 0.4136 0.4389 0.4224 0.4194 0.4075∗
R2 0.1556 0.1839 0.1690 0.1896 0.1852 0.2101 0.2048 0.2719 0.1803 0.2408 0.2515 0.2933∗
AUC 0.7128 0.7401 0.7590 0.7600 0.7316 0.7623 0.7509 0.7645 0.7413 0.7639 0.7588 0.7749∗
EdNet ACC 0.6961 0.7138 0.7213 0.7229 0.7054 0.7247 0.7166 0.7262 0.7099 0.7247 0.7216 0.7318∗
-KT1 RMSE 0.4438 0.4346 0.4285 0.4280 0.4379 0.4271 0.4316 0.4251 0.4348 0.4267 0.4286 0.4220∗
R2 0.129 0.1646 0.1882 0.1900 0.1521 0.1933 0.1763 0.2009 0.1639 0.1946 0.1876 0.2125∗
AUC 0.7510 0.7964 0.7976 0.7971 0.7646 0.7995 0.7958 0.8004 0.7839 0.8035 0.7970 0.8057∗
ACC 0.8457 0.8523 0.8531 0.8525 0.8477 0.8537 0.8527 0.8530 0.8503 0.8550 0.8539 0.8558∗
Junyi RMSE 0.3445 0.3336 0.3329 0.3333 0.3414 0.3322 0.3337 0.3323 0.3370 0.3309 0.3326 0.3296∗
R2 0.1584 0.2108 0.2140 0.2121 0.1735 0.2173 0.2103 0.2168 0.1949 0.2233 0.2155 0.2298∗
AUC 0.7714 0.7691 0.7760 0.8068 0.7813 0.8082 0.8045 0.8053 0.7928 0.8065 0.8087 0.8201∗
ACC 0.7240 0.7224 0.7244 0.7470 0.7313 0.7480 0.7450 0.7461 0.7375 0.7476 0.7487 0.7571∗
Eedi RMSE 0.4273 0.4278 0.4253 0.4113 0.4228 0.4106 0.4126 0.4120 0.4179 0.4114 0.4104 0.4045∗
R2 0.2042 0.2023 0.2116 0.2628 0.2210 0.2651 0.2581 0.2602 0.2389 0.2625 0.2661 0.2867∗
respectively.Batchsizeswere64forASSIST12andASSIST17,and 5.2 StudentPerformancePrediction(Q1)
512forlargerdatasets.Weusedanearlystoppingmechanismwith Wemeasuremodelperformanceintermsofareaunderthecurve
5epochsofpatience.Forfairness,thebaselines’hyper-parameters (AUC),accuracy(ACC),rootmeansquareerror(RMSE),andPear-
aretunedtoachieveoptimalperformance.Allexperimentswere soncorrelationsquared(R2).Weusedtheaverageresultof5-fold
performedonaLinuxserverwithanNVIDIAGeForceRTX3090. cross-validationonthetestsetastheexperimentalresult.Since
theEedidoesnothaveresponsetimefeatures,theFKTandLPKT
5.1.3 Baselines. WecomparedPSKTwith11baselines.
resultsonEediareaftereliminatingresponsetime.
• DKTusesthehiddenstateofRNNtorepresentthelearner’s TheexperimentalresultsareshowninTable2,andPSKTconsis-
knowledgestate.[30] tentlyoutperformsallbaselinemethodsonalldatasetsandmetrics.
• DKVMNdefinesastaticKCmatrixandadynamicstate TheexcellentperformanceofPSKTshowsthatcomprehensively
matrix,usingreadandwriteoperationstoupdatestate.[44] modelingthelearner’sproblem-solvingprocesssignificantlyim-
• SAKTutilizestheself-attentionmechanismtocapturethe pacts understanding the entire learning process and predicting
relationshipsbetweenhistoricalrecords.[27] learningperformance.Comparedwiththemostadvanceddeep
• Deep-IRTutilizesDKVMNtoestimatethelearner’sability learningmodels,thesuperiorityofthePSKTframeworkalsoshows
andusesIRTtocomputethecorrectprobability.[41] thatthefactorthatrestrictstheperformanceofthecurrentKT
• DKT-FincorporatestemporalinformationintoDKTtomodel methodisnottheexpressiveabilityofthealgorithmbutthedesign
learnerforgettingbehavior.[24] ofascientificframeworkthatconformstostudents’cognitiverules.
• AKTenhancesproblems’personalizedembeddingbyIRT AmongthemodelscombinedwithIRT(AKT,Deep-IRT,PKT,PSKT),
andcapturesthelearner’sstatebyattentionmechanism.[11] PSKTperformsbest,furtherprovingtheefficacyofthePSKTal-
• SAINTdirectlyappliestransformertechnologyandsepa- gorithmmechanism.Thesuperiorityofittakesintoaccountboth
ratesproblemsandresponsesininteractions.[5] highaccuracyandinterpretability.
• LPKTusesresponsetimesandintervalstomodelthelearn-
ingprocess,calculatinglearninggainsandforgetting.[32]
5.3 Explainthelearningprocess(Q2)
• ATDKTimprovesperformancebyaddingKCpredictionand
learnerpriorknowledgepredictiontasks.[20] ToprovethatPSKTcancapturestudents’reasonableknowledge
• PKTusesIRTtocomputestudents’knowledgestatesand states, we conducted experiments on learning process analysis.
modelsansweringbehaviors(guessingandslipping).[33] InFigure3,werandomlyselectastudentfromeachdatasetand
• FKTfeedsresponseandintervaltimeintothetransformer visualizetheirlearningprocesswhentheypracticedthesameKC
toenrichthelearner’sobservableperformance.[15] consecutively.WeillustratethesuperiorityofPSKTintwoaspects.
3156

RememberingisNotApplying:InterpretableKnowledgeTracingforProblem-solvingProcesses MM’24,October28-November1,2024,Melbourne,Australia
KKnnoowwlleeddggee SSttaattee DDiiffffiiccuullttyy DDiissttiinngguuiisshh KKnnoowwlleeddggee AAccqquuiissiittiioonn Knowledge Application Guessing Slipping
PSKT
PKT
Deep-IRT
DKT
Response
ASSIST12 ASSIST17 Ednet-KT1 Junyi Eedi
Student_id:71 Student_id:21 Student_id:22 Student_id:0 Student_id:13
Concept_id:190 Concept_id:70 Concept_id:184 Concept_id:13 Concept_id:154
11 14 25 33 56 47 29 28 55 16 39 39 22 9 38 68 54 37 38 84 38 72 46 70 7 7 1 7 1 2 1 2 1 2 1 2 6 6 6 2 6 2 6 2 6 7 27 36 36 29 62 15 25
Figure3:ComparetheinterpretabilityofDKT,Deep-IRT,PKTandPSKTforthelearningprocess.
(1)Knowledgestaterationality.Therationalityoftheknowl- amorereasonableexplanation.Forexample,ontheEedidataset,
edgestateincludesboththestabilityoftheknowledgestatecurve thestudentincorrectlyansweredsixconsecutiveproblemsthat
andtherationalityoftheknowledgestatevalue.First,theknowl- examined154KC,whichDKTandPKTattributedtoadecreasein
edgestatecurvefittedbyPSKTismorestable.Wequantifyfluctua- students’knowledgemastery.Wethinkthatthepracticeprocess
tionsbasedondifferencesinknowledgestatesforallKCsbetween positivelyaffectslearnersandthatstudents’knowledgemastery
eachstudent’sadjacentresponses.AsshowninFigure4(a),PSKT doesnotdeclinesignificantlyduringcontinuousanswering.Specifi-
isthemoststableamongthethreemodels.Learners’knowledge cally,althoughstudentsansweredproblems1and2correctly,PSKT
masteryisdirectionalanddoesnotfluctuatedrasticallyinashort consideredthatlearners’masteryofthisknowledgewasstillonly
period[42].InFigure3,Deep-IRTandDKTknowledgestatecurves about0.5becauseofthelowdifficultyofthesetwoproblems.The
oftenfluctuatesharply.Incontrast,PKTalleviatestheirrationality studentansweredthelast6problemsincorrectly,though,which
throughapenaltymechanismbutdoesnotfullysolvetheproblem PSKTattributedtothehighdifficultyandthelowlevelofknowl-
andaffectsperformance.PSKT,basedonhumanproblem-solving edgeapplication.Atthesametime,studentscorrectlyanswered
theory,employsascientificframeworkforamoredirectionalcurve. thefirstproblem(moredifficult)butincorrectlyansweredthelast
Secondly,PSKTtrackedmorereasonableknowledgestatevalues. twoproblems,whichPSKTattributedtotheslipping.
DKT,Deep-IRT,andPKTobtainedhighknowledgevalues(>0.5)
whenlearnersrespondedcorrectlyanddecreasedwhenincorrect. 5.4 StudytheProblemRepresentation(Q3)
InASSIST12,whenthestudentansweredthe4th(indicesstartfrom
Inthissection,weconductsomeexperimentstodemonstratethe
0)problemincorrectly,thePKTknowledgevaluedroppedfrom0.56
reliabilityoftheproblemrepresentationlearnedinPSKT,including
to0.30andthenincreasedsignificantlyforthelastthreecorrect
theeffectivenessofproblemdifficultyassessmentandtheinter-
answers(0.31→0.71).PSKTmaintainsthatlearners’knowledge
pretabilityoftheproblemrepresentation.
statesremainstable(around0.55),attributingcorrectanswersto
(1)Validityofproblemdifficultyassessment.Sincethereis
improvedapplicationlevels.The4thproblemwasdifficult,sothe
noproblemdifficultyindicatorinalldatasets,toevaluatetheeffec-
incorrectanswerwasduetoamismatchbetweenknowledgestate
tivenessofthedifficultylearnedbyPSKT,werefertotheClassical
anddifficulty,notaknowledgedecline.Thecorrectanswersfor
TestTheory[36]andpreviousKTworkthatconsidersdifficulty
thelastthreeproblemsareduetoimprovedknowledgeapplication,
[23,31,45],anddefinesthestatisticaldifficultyoftheproblemasthe
notasignificantincreaseinknowledgestate.
errorrate.WeconductedaPearsoncorrelationtestbetweenthetwo
(2)Learningprocessinterpretability.Comparedwithother
difficulties.Theexperimentalobjectsaretheproblemsinvolved
methods,PSKTprovidesmoreeducationalparameterstoexplain
inthetestset.Theexperimentalresultsareshowninsubgraph
thelearningprocess.DKTattributesstudentperformanceentirely
(b1)inFigure4.PSKTlearneddifficultyisstronglycorrelatedwith
toknowledgemastery,Deep-IRTaddstheeffectofproblemdiffi-
statisticaldifficulty(>0.7)onalldatasets,whichdemonstratesthe
culty,andPKTconsidersstudentguessingandslippingbehavior.
reliabilityofitsproblemdifficulty.Inaddition,thescatterploton
However,thesemodelsrelyheavilyonasuddendropinknowledge
ASSIST17alsoshowsacertaindegreeofcorrelationandconsistency
masterytoexplainresponsesincorrectly,whereasPSKTprovides
betweenthetwodifficulties(Figure4(b2)).
3157

MM’24,October28-November1,2024,Melbourne,Australia TaoHuangetal.
(a) Comparison of the waviness of the knowledge state   Table3:Resultsofablationexperiments.
| ASSIST12 | ASSIST17 | Junyi |        |         |        |        |        |        |        |        |        |
| -------- | -------- | ----- | ------ | ------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|          |          |       | Data   | Metrics | PR     | EP     | KA     | KP     | KI     | KF     | PSKT   |
|          |          |       |        | AUC     | 0.8248 | 0.8158 | 0.8243 | 0.8232 | 0.8244 | 0.8132 | 0.8252 |
|          |          |       | ASSIST | ACC     | 0.7834 | 0.7784 | 0.7823 | 0.7817 | 0.7830 | 0.7764 | 0.7838 |
-12
|              |              |              |        | RMSE | 0.3861 | 0.3905 | 0.3866 | 0.3871 | 0.3864 | 0.3918 | 0.3858 |
| ------------ | ------------ | ------------ | ------ | ---- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|              |              |              |        | R2   | 0.2954 | 0.2793 | 0.2935 | 0.2918 | 0.2942 | 0.2744 | 0.2966 |
|              |              |              |        | AUC  | 0.8175 | 0.8146 | 0.8157 | 0.8166 | 0.8141 | 0.8078 | 0.8182 |
| DKT PKT PSKT | DKT PKT PSKT | DKT PKT PSKT |        |      |        |        |        |        |        |        |        |
|              |              |              | ASSIST | ACC  | 0.7496 | 0.7476 | 0.7485 | 0.7490 | 0.7473 | 0.7433 | 0.7503 |
(b) Correlation between two difficulties -17 RMSE 0.4080 0.4096 0.4088 0.4083 0.4097 0.4127 0.4075
(b2) Scatter Plot
(b1) Pearson Correlation R2 0.2917 0.2861 0.2889 0.2905 0.2856 0.2753 0.2933
|     |     |     |     | AUC | 0.7745 | 0.7729 | 0.7686 | 0.7724 | 0.7667 | 0.7640 | 0.7749 |
| --- | --- | --- | --- | --- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
ytluciffiD lacitsitatS ACC 0.7311 0.7329 0.7277 0.7304 0.7261 0.7247 0.7318
Ednet
|     |     |     | -KT1 | RMSE | 0.4222 | 0.4223 | 0.4247 | 0.4230 | 0.4256 | 0.4264 | 0.4220 |
| --- | --- | --- | ---- | ---- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
erocS
|     |     |     |     | R2  | 0.2119 | 0.2151 | 0.2025 | 0.2089 | 0.1991 | 0.1961 | 0.2125 |
| --- | --- | --- | --- | --- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|     |     |     |     | AUC | 0.8052 | 0.8042 | 0.8048 | 0.8049 | 0.8042 | 0.8040 | 0.8057 |
|     |     |     |     | ACC | 0.8555 | 0.8550 | 0.8553 | 0.8554 | 0.8552 | 0.8555 | 0.8558 |
Junyi
|         |     |                 |     | RMSE | 0.3298 | 0.3303 | 0.3300 | 0.3299 | 0.3302 | 0.3303 | 0.3296 |
| ------- | --- | --------------- | --- | ---- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Dataset |     | PSKT Difficulty |     |      |        |        |        |        |        |        |        |
|         |     |                 |     | R2   | 0.2286 | 0.2262 | 0.2280 | 0.2281 | 0.2267 | 0.2265 | 0.2298 |
|         |     |                 |     | AUC  | 0.8194 | 0.8193 | 0.8183 | 0.8180 | 0.8170 | 0.8090 | 0.8201 |
Figure4:Visualizationofknowledgestatefluctuationsand
|                                    |     |     |      | ACC  | 0.7569 | 0.757  | 0.7561 | 0.7555 | 0.7547 | 0.7482 | 0.7571 |
| ---------------------------------- | --- | --- | ---- | ---- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| correlationbetweentwodifficulties. |     |     | Eedi |      |        |        |        |        |        |        |        |
|                                    |     |     |      | RMSE | 0.4047 | 0.4049 | 0.4054 | 0.4057 | 0.4065 | 0.4103 | 0.4045 |
|                                    |     |     |      | R2   | 0.2861 | 0.2854 | 0.2839 | 0.2827 | 0.2799 | 0.2663 | 0.2867 |
perception,KAmeansremovingknowledgeapplication,andKP
denotesremovingknowledgeacquisition.KIisknowledgeinternal-
izationwithoutconsideringknowledgeacquisitionandKnowledge
application,KFrepresentsremovingknowledgeforgetting.
First,knowledgeforgettingisvitalinthelearningprocess,and
deletingthismodulecausesthemostsignificantperformancedrop.
AccordingtothedesignofPSKT,ifforgettingisnotconsidered,
thelearner’sknowledgemasterywillcontinuetoincrease(orre-
mainunchanged)asthenumberofexercisesincreases,making
itchallengingtoidentifyincorrectanswers.Secondly,theimpact
ofproblemperceptionisalsosignificant.Thisisbecauseproblem
perceptioninvolvesmodelingtheproblem’sinitialstate,thetarget
state,andtheadaptedoperator.Thesethreevariablesarethrough-
|     |     |     | out the | entire | problem-solving |     | process. |     | Third, | both knowledge |     |
| --- | --- | --- | ------- | ------ | --------------- | --- | -------- | --- | ------ | -------------- | --- |
acquisitionandknowledgeapplicationcontributetotheperfor-
manceofPSKT,provingthatknowledgeacquisitionandknowledge
Figure5:WeightsofproblemrepresentationsonASSIST17.
applicationarebothindispensableprocessesforproblem-solving.
Thelabel[𝑖,𝑗,𝑘]indicates[𝐾𝐶,𝑑𝑖𝑓𝑓𝑖𝑐𝑢𝑙𝑡𝑦,𝑑𝑖𝑠𝑐𝑟𝑖𝑚𝑖𝑛𝑎𝑡𝑖𝑜𝑛].
6 Conclusion
(2)Interpretabilityofproblemrepresentation.Wevisualize Inthispaper,weproposeaproblem-solvingprocess-orientedknowl-
thecorrelationweightsbetweenproblemsbycomputingthecosine
edgetracingmodeltoexplorehowstudentstransformtheoretical
similarityoftheproblemrepresentations,asshowninFigure5.We
knowledgeintopracticalskills.Beforeproblem-solving,weobtain
randomlyselectedeightquestionsonASSIST17.Theseproblems students’personalizedperceptionsoftheproblemandsimulate
testedtwoKCs(9,74).First,thecorrelationweightstendtobe theiracquisitionofproblem-relatedknowledge.Duringproblem-
higherbetweenproblemsthattestthesameKC,suchasproblems solving,wemodelthelearner’sknowledgeapplicationleveland
1,2,and3.Secondly,whendifferentproblemshavethesameKC,
useeducationallymeaningfulparameterstopredictresponses.Af-
thecloserthedifficultyanddiscriminationoftheproblemsare,the
|     |     |     | ter problem-solving, |     |     | we design | an  | update | indicator | to  | measure |
| --- | --- | --- | -------------------- | --- | --- | --------- | --- | ------ | --------- | --- | ------- |
higherthesimilarity,forexample,[9,0.60,0.81]and[9,0.58,0.85].
theirknowledgeinternalizationandtheforgettingeffectovertime.
Finally,extensiveexperimentsvalidatedthatPSKTexcelsinre-
5.5 Ablationexperiments(Q4)
sponsepredictionandeffectivelyevaluateslearners’knowledge
WeexploretheimpactofeachmoduleinPSKTthroughablation masterypatterns,providinginsightsintostudents’successorfail-
experiments.AsshowninTable3,weselected6variants,each ure.Lookingforward,PSKTcanbeimprovedbycollectingdetails
removinganelementfromthePSKT.PRisreplacingtheproblem ofstudents’answersandusinglargelanguagemodeltechnology
representationwithconcatenate,EPdenotesremovingproblem tocaptureknowledgetransformationmorefinelyfromtheirsteps.
3158

RememberingisNotApplying:InterpretableKnowledgeTracingforProblem-solvingProcesses MM’24,October28-November1,2024,Melbourne,Australia
Acknowledgments
InIEEE/WIC/ACMInternationalConferenceonWebIntelligence.156–163.
[26] AllenNewell,HerbertAlexanderSimon,etal.1972. Humanproblemsolving.
ThisresearchwassupportedbytheNationalKeyR&DProgramof
Vol.104.Prentice-hallEnglewoodCliffs,NJ.
China(GrantNo.2023YFC3305600),theNationalNaturalScience [27] ShaliniPandeyandGeorgeKarypis.2019.Aself-attentivemodelforknowledge
FoundationofChina(GrantNo.U20A20229,62307029). tracing.arXivpreprintarXiv:1907.06837(2019).
[28] ZacharyAPardosandNeilTHeffernan.2010. Modelingindividualizationin
abayesiannetworksimplementationofknowledgetracing.InUserModeling,
References Adaptation,andPersonalization:18thInternationalConference,UMAP2010,Big
Island,HI,USA,June20-24,2010.Proceedings18.Springer,255–266.
[1] GhodaiAbdelrahmanandQingWang.2019.Knowledgetracingwithsequential [29] PhilipIPavlikJr,HaoCen,andKennethRKoedinger.2009.PerformanceFactors
key-valuememorynetworks.InProceedingsofthe42ndinternationalACMSIGIR Analysis–ANewAlternativetoKnowledgeTracing.OnlineSubmission(2009).
conferenceonresearchanddevelopmentininformationretrieval.175–184. [30] ChrisPiech,JonathanBassen,JonathanHuang,SuryaGanguli,MehranSahami,
[2] GhodaiAbdelrahman,QingWang,andBernardoNunes.2023.Knowledgetracing: LeonidasJGuibas,andJaschaSohl-Dickstein.2015. Deepknowledgetracing.
Asurvey.Comput.Surveys55,11(2023),1–37. Advancesinneuralinformationprocessingsystems28(2015).
[3] JohnRAnderson.1993.Problemsolvingandlearning.Americanpsychologist48, [31] ShuanghongShen,ZhenyaHuang,QiLiu,YuSu,ShijinWang,andEnhongChen.
1(1993),35. 2022.Assessingstudent’sdynamicknowledgestatebyexploringthequestion
[4] FrankBBaker.2001.Thebasicsofitemresponsetheory.ERIC. difficultyeffect.InProceedingsofthe45thinternationalACMSIGIRconferenceon
[5] YoungduckChoi,YoungnamLee,JunghyunCho,JineonBaek,ByungsooKim, researchanddevelopmentininformationretrieval.427–437.
YeongminCha,DongminShin,ChanBae,andJaeweHeo.2020.Towardsanap- [32] ShuanghongShen,QiLiu,EnhongChen,ZhenyaHuang,WeiHuang,YuYin,Yu
propriatequery,key,andvaluecomputationforknowledgetracing.InProceedings Su,andShijinWang.2021.Learningprocess-consistentknowledgetracing.In
oftheseventhACMconferenceonlearning@scale.341–344. Proceedingsofthe27thACMSIGKDDconferenceonknowledgediscovery&data
[6] AlbertTCorbettandJohnRAnderson.1994.Knowledgetracing:Modelingthe mining.1452–1460.
acquisitionofproceduralknowledge.Usermodelinganduser-adaptedinteraction [33] JianwenSun,MengqiWei,JintianFeng,FenghuaYu,QingLi,andRuiZou.
4(1994),253–278. 2024.Progressiveknowledgetracing:Modelinglearningprocessfromabstract
[7] JiajunCui,MingheYu,BoJiang,AiminZhou,JianyongWang,andWeiZhang. toconcrete.ExpertSystemswithApplications238(2024),122280.
2023.InterpretableKnowledgeTracingviaResponseInfluence-basedCounter- [34] JianwenSun,FenghuaYu,SannyuyaLiu,YaweiLuo,RuxiaLiang,andXiaoxuan
factualReasoning.arXivpreprintarXiv:2312.10045(2023). Shen.2023. AdversarialBootstrappedQuestionRepresentationLearningfor
[8] AndreasFischer,SamuelGreiff,andJoachimFunke.2011.Theprocessofsolving KnowledgeTracing.InProceedingsofthe31stACMInternationalConferenceon
complexproblems.JournalofProblemSolving4,1(2011),19–42. Multimedia.8016–8025.
[9] AndreasFischer,SamuelGreiff,andJoachimFunke.2017.Thehistoryofcomplex [35] ShiweiTong,QiLiu,WeiHuang,ZhenyaHunag,EnhongChen,ChuanrenLiu,
problemsolving.(2017). HaipingMa,andShijinWang.2020. Structure-basedknowledgetracing:An
[10] CatherineTwomeyFosnot.2013.Constructivism:Theory,perspectives,andpractice. influencepropagationview.In2020IEEEinternationalconferenceondatamining
TeachersCollegePress. (ICDM).IEEE,541–550.
[11] AritraGhosh,NeilHeffernan,andAndrewSLan.2020. Context-awareatten- [36] RossETraub.1997.Classicaltesttheoryinhistoricalperspective.Educational
tiveknowledgetracing.InProceedingsofthe26thACMSIGKDDinternational Measurement16(1997),8–13.
conferenceonknowledgediscovery&datamining.2330–2339. [37] EmikoTsutsumi,RyoKinoshita,andMaomiUeno.2021.Deep-IRTwithIndepen-
[12] LisaHarrell.2013.Alearnercenteredapproachtoonlineeducation.IAP. dentStudentandItemNetworks.InternationalEducationalDataMiningSociety
[13] DerekHodson.1998. Teachingandlearningscience:Towardsapersonalized (2021).
approach.McGraw-HillEducation(UK). [38] BihanXu,ZhenyaHuang,JiayuLiu,ShuanghongShen,QiLiu,EnhongChen,
[14] KeithJHolyoakandRobertGMorrison.2005. TheCambridgehandbookof JinzeWu,andShijinWang.2023.Learningbehavior-orientedknowledgetracing.
thinkingandreasoning.CambridgeUniversityPress. InProceedingsofthe29thACMSIGKDDconferenceonknowledgediscoveryand
[15] TaoHuang,ShengzeHu,HualiYang,JingGeng,ZhifeiLi,ZhuoranXu,and datamining.2789–2800.
XinjiaOu.2024.Responsespeedenhancedfine-grainedknowledgetracing:A [39] HualiYang,ShengzeHu,JingGeng,TaoHuang,JunjieHu,HaoZhang,andQiang
multi-tasklearningperspective. ExpertSystemswithApplications238(2024), Zhu.2024.Heterogeneousgraph-basedknowledgetracingwithspatiotemporal
122107. evolution.ExpertSystemswithApplications238(2024),122249.
[16] TaoHuang,XinjiaOu,HualiYang,ShengzeHu,JingGeng,ZhuoranXu,and [40] YangYang,JianShen,YanruQu,YunfeiLiu,KerongWang,YaomingZhu,Weinan
ZongkaiYang.2024. Pulltogether:Option-weighting-enhancedmixture-of- Zhang,andYongYu.2021.GIKT:agraph-basedinteractionmodelforknowledge
expertsknowledgetracing.ExpertSystemswithApplications(2024),123419. tracing.InMachineLearningandKnowledgeDiscoveryinDatabases:European
[17] SlavaKalyuga.2007.Expertisereversaleffectanditsimplicationsforlearner- Conference,ECMLPKDD2020,Ghent,Belgium,September14–18,2020,Proceedings,
tailoredinstruction.Educationalpsychologyreview19(2007),509–539. PartI.Springer,299–315.
[18] MohammadMKhajah,YunHuang,JoséPGonzález-Brenes,MichaelCMozer, [41] Chun-KitYeung.2019.Deep-IRT:Makedeeplearningbasedknowledgetracing
andPeterBrusilovsky.2014.Integratingknowledgetracinganditemresponse explainableusingitemresponsetheory.arXivpreprintarXiv:1904.11738(2019).
theory:Ataleoftwoframeworks.InCEURWorkshopproceedings,Vol.1181. [42] Chun-KitYeungandDit-YanYeung.2018. Addressingtwoproblemsindeep
UniversityofPittsburgh,7–15. knowledgetracingviaprediction-consistentregularization.InProceedingsofthe
[19] QiLiu,ShuanghongShen,ZhenyaHuang,EnhongChen,andYongheZheng. fifthannualACMconferenceonlearningatscale.1–10.
2021.Asurveyofknowledgetracing.arXivpreprintarXiv:2105.15106(2021). [43] MichaelVYudelson,KennethRKoedinger,andGeoffreyJGordon.2013.Individ-
[20] ZitaoLiu,QiongqiongLiu,JiahaoChen,ShuyanHuang,BoyuGao,WeiqiLuo, ualizedbayesianknowledgetracingmodels.InArtificialIntelligenceinEducation:
andJianWeng.2023.Enhancingdeepknowledgetracingwithauxiliarytasks.In 16thInternationalConference,AIED2013,Memphis,TN,USA,July9-13,2013.
ProceedingsoftheACMWebConference2023.4178–4187. Proceedings16.Springer,171–180.
[21] ShaulMarkovitchandPaulDScott.1988.Theroleofforgettinginlearning.In [44] JianiZhang,XingjianShi,IrwinKing,andDit-YanYeung.2017.Dynamickey-
Machinelearningproceedings1988.Elsevier,459–465. valuememorynetworksforknowledgetracing.InProceedingsofthe26thinter-
[22] SeinMinn,Jill-JênnVie,KohTakeuchi,HisashiKashima,andFeidaZhu.2022. nationalconferenceonWorldWideWeb.765–774.
Interpretableknowledgetracing:Simpleandefficientstudentmodelingwith [45] MoyuZhang,XinningZhu,ChunhongZhang,YangJi,FengPan,andChangchuan
causalrelations.InProceedingsoftheAAAIconferenceonartificialintelligence, Yin.2021.Multi-factorsawaredual-attentionalknowledgetracing.InProceedings
Vol.36.12810–12818. ofthe30thACMInternationalConferenceonInformation&KnowledgeManage-
[23] SeinMinn,FeidaZhu,andMichelCDesmarais.2018.Improvingknowledgetrac- ment.2588–2597.
ingmodelbyintegratingproblemdifficulty.In2018IEEEInternationalconference [46] MoyuZhang,XinningZhu,ChunhongZhang,WenchenQian,FengPan,and
ondataminingworkshops(ICDMW).IEEE,1505–1506. HuiZhao.2023.CounterfactualMonotonicKnowledgeTracingforAssessing
[24] KokiNagatani,QianZhang,MasahiroSato,Yan-YingChen,FrancineChen, Students’DynamicMasteryofKnowledgeConcepts.InProceedingsofthe32nd
andTomokoOhkuma.2019. Augmentingknowledgetracingbyconsidering ACMInternationalConferenceonInformationandKnowledgeManagement.3236–
forgettingbehavior.InTheworldwidewebconference.3101–3107. 3246.
[25] HiromiNakagawa,YusukeIwasawa,andYutakaMatsuo.2019. Graph-based
knowledgetracing:modelingstudentproficiencyusinggraphneuralnetwork.
3159