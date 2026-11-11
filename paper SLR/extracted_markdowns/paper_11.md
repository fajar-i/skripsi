Knowledge Tracing for Complex Problem Solving: Granular
Rank-Based Tensor Factorization
ChunpaiWang ShaghayeghSahebi SiqianZhao
cwang25@albany.edu ssahebi@albany.edu szhao2@albany.edu
UniversityatAlbany-SUNY UniversityatAlbany-SUNY UniversityatAlbany-SUNY
Albany,NewYork,USA Albany,NewYork,USA Albany,NewYork,USA
PeterBrusilovsky LauraO.Moraes
peterb@pitt.edu laura.moraes@coppe.ufrj.br
UniversityofPittsburgh FederalUniversityofRiodeJaneiro
Pittsburgh,Pennsylvania,USA RiodeJaneiro-RJ,Brazil
ABSTRACT showsthatattemptaggregationeliminatestheunnecessaryfluc-
KnowledgeTracing(KT),whichaimstomodelstudentknowledge tuationsfromstudents’discoveredknowledgestatesandhelpsin
levelandpredicttheirperformance,isoneofthemostimportant discoveringcomplexlatentconceptsintheproblems.
applicationsofusermodeling.ModernKTapproachesmodeland
CCSCONCEPTS
maintainanup-to-datestateofstudentknowledgeoverasetof
courseconceptsaccordingtostudents’historicalperformancein •Socialandprofessionaltopics→Studentassessment;•Com-
attemptingtheproblems.However,KTapproachesweredesigned putingmethodologies→Tensorfactorization.
tomodelknowledgebyobservingrelativelysmallproblem-solving
stepsinIntelligentTutoringSystems.Whiletheseapproacheswere KEYWORDS
appliedsuccessfullytomodelstudentknowledgebyobservingstu- knowledgetracing,tensorfactorization,complexproblemsolving,
dentsolutionsforsimpleproblems,suchasmultiple-choiceques- aggregation
tions, they do not perform well for modeling complex problem
ACMReferenceFormat:
solvinginstudents.Mostimportantly,currentmodelsassumethat
ChunpaiWang,ShaghayeghSahebi,SiqianZhao,PeterBrusilovsky,andLaura
allproblemattemptsareequallyvaluableinquantifyingcurrent
O.Moraes.2021.KnowledgeTracingforComplexProblemSolving:Granular
studentknowledge.However,forcomplexproblemsthatinvolve
Rank-BasedTensorFactorization.InProceedingsofthe29thACMConfer-
manyconceptsatthesametime,thisassumptionisdeficient.It enceonUserModeling,AdaptationandPersonalization(UMAP’21),June
resultsininaccurateknowledgestatesandunnecessaryfluctua- 21–25,2021,Utrecht,Netherlands.ACM,NewYork,NY,USA,10pages.
tionsinestimatedstudentknowledge,especiallyifstudentsguess https://doi.org/10.1145/3450613.3456831
thecorrectanswertoaproblemthattheyhavenotmasteredall
ofitsconceptsorslipinansweringtheproblemthattheyhave 1 INTRODUCTION
alreadymasteredallofitsconcepts.Inthispaper,wearguethat Personalizedonlinelearningsystemshaverecentlydrawnalot
notallattemptsareequivalentlyimportantindiscoveringstudents’ ofattentionbecauseofthegrowingneedtoassistandimprove
knowledgestate,andsomeattemptscanbesummarizedtogether students’learning.Afundamentalpartoftheusermodelingtask
tobetterrepresentstudentperformance.Weproposeanovelstu- inthesesystemsisestimatingstudents’knowledgestatesasthey
dentknowledgetracingapproach,GranularRAnkbasedTEnsor workwithlearningmaterials[3].Thistask,knownasknowledge
factorization(GRATE),thatdynamicallyselectsstudentattempts tracing (KT), is necessary for predicting students’ performance
thatcanbeaggregatedwhilepredictingstudents’performancein infutureassessments,personalizingproblemsandexercisesfor
problemsanddiscoveringtheconceptspresentedinthem.Ourex- students,identifyingat-riskstudents,andprovidingteacherswith
perimentsonthreereal-worlddatasetsdemonstratetheimproved adetailedviewofoverallstudentprogress.Inparticular,KTmodels
performanceofGRATE,comparedtothestate-of-the-artbaselines, usestudentattemptsequences,includingstudentperformance(e.g.,
inthetaskofstudentperformanceprediction.Ourfurtheranalysis successorfailure)onpastproblems,toestimatestudentknowledge
attheendofasequenceandpredictstudentperformanceonthe
nextattempts.
Toquantifystudentknowledge,traditionalKTmodelsrelyon
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
apredefineddomainknowledgemodelthatrepresentstheassoci-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ationsbetweentheproblemsandcourseconcepts.Suchmodels
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM individuallytracestudentknowledgeineachoftheseconcepts,
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
neglectingthepotentialrelationshipsbetweendifferentconcepts.
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. Asthesemodelslearnthesamesetofparametersforallstudents,
UMAP’21,June21–25,2021,Utrecht,Netherlands theyarenotpersonalizedtothestudentspecifications.Forexample,
©2021AssociationforComputingMachinery.
Bayesianknowledgetracing(BKT)[3],whichisoneofthepioneer
ACMISBN978-1-4503-8366-0/21/06...$15.00
https://doi.org/10.1145/3450613.3456831 KTmodels,representsstudentknowledgestatesineachconcept
179

UMAP’21,June21–25,2021,Utrecht,Netherlands Wang,etal.
usingatwo-stateHMM,whichimposesaMarkovianassumption usingaconstraint,havingabinaryknowledgestateandfittingto
onknowledgestatesfromoneattempttothenext. everyattemptresultsinknowledgestateinaccuracies.
Inrecentyears,modernKTmodelshavebeendevelopedtoad- Inthispaper,wearguethat,duetothenoiseinsolvingcomplex
dresstheaboveproblems.Forexample,manyvariantsofBKThave problems,somestudentattemptobservationsaremoreinforma-
beenproposedtoimprovethemodelbyconsideringthepotential tiveandimportantthanothers.Forthat,weaddressthestudent
toforgetthelearnedconcepts[7],accountingforthedependencies knowledgetracingchallengeforcomplexproblemsbysummariz-
betweenconcepts[8],andpersonalizingthemodelparametersfor ingstudentattemptstobetterrepresentstudentperformance.We
differentstudents[27].InadditiontotheBayesianmodels,latent proposeapersonalizedknowledgetracingmodelthatautomati-
factorapproacheshavebeensuccessfulinconsideringtheconcept callydetects“lessimportant”studentattemptsandaggregatesthem
relationships[11,20,21,29].Forexample,Lanetal.[11]proposeda intootherattemptstobetterrepresentstudentknowledgeandpre-
sparsefactoranalysisframeworkforbothstudentknowledgetrac- dicttheirperformance.Additionally,ourproposedKTmodelis
inganddomainknowledgeestimation.Sahebietal.[20]proposed personalizedforstudentsandautomaticallydiscoversthedomain
atensorfactorizationmethodtoexplicitlymodelstudentlearning knowledgemodelwithoutrequiringextraprobleminformation,
processesbyassumingastrictlymonotonicincreasinglearning suchastext,topics,ortags.Inparticular,wemodelstudentse-
gain.Zhaoetal.[29]leveragethemultiviewtensorfactorization quencesinatensorandproposeanadaptiveGranularRAnkbased
methodformodelingstudentknowledgeusingmultiplelearningre- TEnsorfactorization(GRATE)toaddressthenoisinessandsparsity
sourcetypes.Similarly,deeplearningmodels,suchasDKT[17]and issuessoastoprovideaplausibleandpreciseknowledgemodeling.
DKVMN[28],haverecentlybeenintroducedintotheKTdomain. Weimposearank-basedconstraintonstudentknowledgeacross
However,themajorityofKTmodelshaveassumedthateach attemptstohelpreducetheunnecessaryfluctuationsinstudent
attemptinasequenceconsideredbytracingisrelativelysimple knowledgeandimprovetheinterpretabilityofthemodel.GRATE
andinvolvestheapplicationofoneorveryfewconcepts,suchas doesnotrelyonadomainknowledgemodel,asitautomatically
smallstepsinsolvingeitheracomplexproblemoranelementary discoverslatentconceptsfortheproblemspresentedtostudents.
problem.Withthisassumption,theobservedstudentperformance Itispersonalizedbyprofilingstudentsintostudentlatentfeatures
canbedirectlyassociatedwithafewinvolveddomainconcepts, andlearningaseparatesetofparametersfortheminacollaborative
andeachcorrectorincorrectattemptbythestudentcanprovide way.
arelativelyconfidentevaluationofstudentknowledgeinthose Ourcontributionsinthispaperare:(a),wearethefirsttoaddress
concepts.Asaresult,whenconsideringthesekindsofproblems, thenoisyobservationchallengeforstudentknowledgetracingin
currentKTmodelsassumethateveryattemptinstudenthistoryis complexproblemsolving;(b),forthis,weproposeanoveltensor
equallyimportantinquantifyingstudentknowledge.Thisassump- factorizationmethodthatadaptivelyaggregatesstudentattempts
tioncanbesufficientfordomainsinwhicheachproblemconsists whileimposingarank-basedconstrainttorepresentstudents’grad-
ofafewatomicconcepts.However,itisdeficientfordomainswith uallearning;(c),ourknowledgetracingmodelispersonalizedand
morecomplexproblems,suchaswritingaprogramorsolvingan doesnotrelyonadditionaldomainknowledgeinformation;(d),we
assignmentwithmultiplesteps. conductextensiveexperimentstoanalyzeandvalidatetheeffective-
Incomplexproblemsolving,eachproblemcanincludemultiple nessofourproposedmodel,comparedtoseveralstate-of-the-art
concepts,suchthatknowingallofthemtosomeextentisnecessary baselines,onthreereal-worlddatasets;and(e),wedemonstrate
forcorrectlyansweringtheproblem.Becauseofthiscomplexity, thatourproposedmethodiscapableofprovidingpreciseandplau-
studentattemptobservationswillbenoisier,asslippingineven siblestudentknowledgestateswhilelearningmeaningfulquestion-
oneoftherequiredconceptscansignificantlyharmstudentperfor- conceptassociations.
mance.Additionally,identifyingtheconceptsthatareresponsible
foranimperfectperformancewillbemorechallenginginsuchcom- 2 GRANULARRANKBASEDTENSOR
plexproblems.Similarly,solvingacomplexproblemcorrectlyby FACTORIZATION(GRATE)
guessingadifficultunknownconceptorbytrialanderroronthat
Ourgoalinthisworkistohandlethenoiseandfluctuationsin
importantconceptwillbewronglyattributedtoastudent’shigh
studentknowledgetracingofcomplexproblemswithoutrelying
knowledgeofalloftheinvolvedconcepts.Asaresult,suchnoisy
onadomainknowledgemodelorapredefinedmappingbetween
observationscouldeasilycausetraditionalKTmodelstoprovidean
problems and concepts. We aim to do this with a personalized
inaccurateestimationofoveralllevelsofstudentknowledge.Forex-
KTapproachthatisinterpretablewithoutharmingthemodelper-
ample,considerastudentwhohasalreadymasteredsomeconcepts.
formance;e.g.,inthestudentperformancepredictiontask.Inthe
Thisstudenttriesaproblemonthoseconceptsthreetimes,getting
following,weformulatethischallengeasatensorfactorization
theproblemrightthefirsttime(successfulattempt),slippingin
problem,presentourproposedmethodtoaddressthechallenge,
oneoftheconceptsthesecondtime(failedattempt),andgetting
explainourintuitionbehindchoosingtensorfactorizationasthe
itrightagaininthethirdtime(successfulattempt).IncurrentKT
basisofourmodel,andprovidethealgorithmforourmethod.
approaches,sincethemodeltriestofiteverystudentattempt,these
casesresultinfluctuationsinestimatedstudentknowledge.Evenin
2.1 ProblemFormulationandAssumptions
modelslikeBKT,whichtrytoconsidersmallguessandslipprobabil-
itiesbymodelingeachconceptindependently,orDKT+[26],which WeconsideranonlinelearningsysteminwhichMstudentsattempt
aimstosmoothoutstudentpredictedperformance(notknowledge) NproblemsinsequencesofmaximumlengthTovertime.Students
canattempttheproblemsinanyorderandasmanytimesasthey
180

KnowledgeTracingforComplexProblemSolving:GranularRank-BasedTensorFactorization UMAP’21,June21–25,2021,Utrecht,Netherlands
like.Studentperformanceduringeachattemptisrecordedasa in which the set Ω consists of all non-missing values in X.
obs
score,gradevalue,orbinary(successorfailure)data.Werepresent Thelasttwotermsareregularizationconstraintswithimportant
thestudents’loggedperformancerecordsina3-modetensorX∈ weightsλs andλa to ensure the generalizability of the learned
[0,1]M×T×N.Everyentryxu,t,i ∈Xrepresentstheuth student’s values.
normalizedgradeonith problematattemptindext.Ourgoalis AdaptiveGranularity-BasedAggregation.Thestudentattempt
tofactorizethistensortobeabletoaccuratelyestimatestudent tensorXisverysparse,sincethestudentsonlyinteractwithone
knowledgeoftheproblems’latentconceptsandpredictstudent problemduringeachattempt.Additionally,becauseofproblem
performanceintheirfutureproblemattempts,accordingtotheir complexities,theobservedattemptsarenoisyandunreliable(as-
history. sumption (d) or attempt noisiness assumption). As a result, it is
ModelAssumptions.Webuildourmodelbasedonthefollow- difficulttoextractaccurateandinterpretableunderlyingstructures
ingassumptions:(a)Domainknowledgeassumption:Eachproblem fromthistensor.Moreover,equallyrelyingonallattempts,whether
coversanumberofconceptsthatarepresentedinthecoursewith theyarenoisyornot,resultsinimpreciseknowledgestatesand
differentproportions;thesetofallofthecourseconceptsareshared poorperformancepredictions.
acrossproblems;andthetrainingdatadoesnotincludetheprob- Toaddressthisissue,weproposetoautomaticallyaggregate
lems’contentsnortheirconcepts.(b)Studentperformanceassump- attemptslicesthataredeemedtobenotinformativeenoughwith
tion:Differentstudentshavedifferentlearningabilitiesandinitial theirneighborattempts.Thiswillsummarizetheinformativeand
knowledgeandtheirperformanceindifferentproblemsdepends non-informativeattemptstogether,keepingonlytheimportant
ontheirknowledgestate,especiallyintheconceptsrelatedtothose informationandleavingoutthenoisyones.Todothis,wefind
problems.(c)Studentlearningassumption:Asstudentsinteractwith asmalleraggregatedtensorthatsummarizesourinitialstudent
theproblems,theylearntheconceptsthatarepresentedinthem, attempttensor,alongwiththeattempts,withamaximalrecovery
meaningthattheirknowledgeintheseconceptsincreasesgradually; ofinformationoraminimallossofinformation.
butstudentsmayalsoforgetsomeconcepts.(d)Attemptnoisiness Inspiredby[18],weaimtofindanaggregated3-modetensorY
assumption:Studentdatacanbenoisy;e.g.,theymayslipinone ofdimensionsM×T˜ ×NwithT˜ ≤T,suchthatYcanaccurately
conceptoutofalltheproblemconceptsandreceivealowscore, representourinitialtensorX,measuredbyagoodnessoffitor
whiletheyhavealreadymasteredalloftheseconcepts.Similarly, utility function F. To achieve this goal, we find an aggregation
theymayguessthecorrectanswertoaproblemwithoutknowing matrixW thatindicateswhichattemptsshouldbeintegratedinto
alltheproblemconcepts.Asaresult,someattemptsmaynotbean theirneighboringattempts.Inotherwords,wefindW suchthat
accuraterepresentationofstudentknowledge. aggregatingtheX tensorusingitmaximizestheutilityfunctionF:
2.2 TheProposedModel
m
W
axF(X× 2W) (3)
TensorFactorization.Followingthe(a)domainknowledgeand where× 2denotestheaggregationoperationonthetensor’ssecond
(b)studentperformanceassumptionsabove,wefirstmodelstudent
mode(attemptmode),andW(i,j)=1ifsliceiintensorXisaggre-
interactiontensorXasafactorizationofthreelowerdimensional
gatedintoslicejintheresultingtensor,otherwiseW(i,j)=0.For
representations:1)anM×KstudentlatentfeaturematrixS,that theutilityfunctionF,weusemissingvaluepredictionaccuracy.As
representsparticularstudentfeatures(suchasabilitiesandper- aresult,wesummarizetheinputtensorXusingtheaggregation
sonalities)thatareconstantovertime;2)aK×T ×Ctemporal matrixW suchthatthenewtensorYprovidesuswiththehighest
dynamicknowledgetensorA,thatshowstheknowledgeofstudents studentperformancepredictionaccuracy.Forinstance,consider
withspecificabilitiesinthecourseconceptsastheyattemptthe thetensorXofdimension5×6×5withtheoptimalaggregate
problems;and3)aC×N matrixQservingasamappingbetween shapeofYis5×2×5.Inthiscase,W isofsize2×6suchas:
problemsandcourseconcepts.Theuppertensorfactorizationin (cid:20) (cid:21)
1 1 0 0 0 0
Figure1representsthismodel.Accordingtoourfactorization,the W = (4)
0 0 1 1 1 1
resultingtensorfromproductK=SArepresentsstudentknowl-
wherethefirsttwoslicesofXwillbeaggregatedasthefirstslice
edge in each concept at each attempt. In addition to the above
ofY,andthelastfourwillformthesecond.
factors,weaddastudent-specificbiasbu,problem-specificdiffi-
SincestudentknowledgestatestypicallyexhibitaMarkovian
cultybi,andaveragescoreoffsetµ.Consequently,wecanestimate
property[29],wefollowagreedyaggregationofslices,similarto
students’performanceatattemptt asinthefollowing,whereσ
theIceBreakeralgorithm[18],totrytoaggregatethesubsequent
representsastandardprobitorlogitlinkfunction:
attempts.Thisway,theaggregationmatrixW willhaveonesonly
xˆu,t,i =σ(su ·At ·qi +bu +bi +µ) (1)
closetothediagonalandzerosinallotherplaces.Thiskindof
Notethatusingσ makesthemodelinterpretationflexible:bothas aggregationalsoreducesthetimecomplexityofsolvingEquation3
anestimationofareal-valuedscorebetweenzeroandone,andas fromO(2T)tolineartimecomplexity.
theprobabilityvalueofthebinarysuccessorfailureinsolvinga Fortheaggregationoperation× 2,wefilltheunobservedvalues
problem(asinaclassifier).TolearntheparametersS,A,Q,andthe intheprevious(t−1)attemptslicewiththeobservedvaluesinthe
biases,wecanminimizethefollowingobjectivefunction: current(t)attemptslice.Also,wereplacetheobservedvaluesin
T thepreviousattemptwiththevaluesinthecurrentattemptifthey
L 0 = (cid:213) (cid:0) xu,t,i −xˆu,t,i (cid:1)2+λs ∥su ∥ 2 2+λa (cid:213) ∥At ∥ F 2 (2) areobserved.Thismeansthattheaggregatedattemptcontainspart
u,t,i∈Ωobs t=1 oftheobservationsfromboththepreviousandcurrentattempts.
181

| UMAP’21,June21–25,2021,Utrecht,Netherlands |     |     |     |     |     |     |     |     |     |     | Wang,etal. |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
me Index
me Index
Raw Student Activity Data
|     |     |          |                     |                               |     | Ti       |     |                | Ti      |       |          |     |
| --- | --- | -------- | ------------------- | ----------------------------- | --- | -------- | --- | -------------- | ------- | ----- | -------- | --- |
|     |     | Stu dent | Q uesti o n         | T i m e Sco r e               |     |          |     | er             | ur e    | pt    |          |     |
|     |     |          |                     |                               |     | er       |     | s S            | ×       | e     |          |     |
|     |     |          |                     |                               |     |          | 𝑋   | U              | at A    | × n c | Q        |     |
|     |     |          |                     |                               |     | s        |     |                | e       | o     |          |     |
|     |     | 2        | 3 1 0 /21/2         | 0 : 14 :11:53 7 6             |     | U        |     |                | F       | C     |          |     |
|     |     | 1        | 1 10/21/20:14:14:01 | 90                            |     |          |     |                | Concept |       | Question |     |
|     |     | 3        | 2 10/23/20:15:29:51 | 34                            |     |          |     | Latent Feature |         |       |          |     |
|     |     | 10       | 9 10/23/20:11:50:15 | 95                            |     | Question |     |                |         |       |          |     |
|     |     | 5        | 3 10/23/20:13:05:28 | 76                            |     |          |     |                |         |       |          |     |
|     |     | 6        | 1 5 1 0 / 2         | 3 / 2 0 : 1 3 : 0 5 : 5 3 7 6 |     |          |     |                |         |       |          |     |
dex
|     |     | 5   | 3 1 0 / 2 | 3 / 2 0 : 1 3 : 0 5 : 5 3 6 7 |     | me Inde | x   |     | me In |     |     |     |
| --- | --- | --- | --------- | ----------------------------- | --- | ------- | --- | --- | ----- | --- | --- | --- |
GRATE
.
|     |     |     | ..  |     |        |     |     |     |  Ti |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Agg. T | i   |     |     | gg. |     |     |     |
pt
|     |     |     |           |                                 |     |     |     | er  | A ur e ~ | e   |          |     |
| --- | --- | --- | --------- | ------------------------------- | --- | --- | --- | --- | -------- | --- | -------- | --- |
|     |     | 1   | 1 1 0 / 2 | 8 / 2 0 : 2 1 : 1 6 : 0 1 1 0 0 |     | er  |     | s S | A        | c   | Q        |     |
|     |     | 1 0 | 2 1 0 / 2 | 9 / 2 2 : 0 9 : 11 : 3 8 8 6    |     |     | 𝑌   | U   | × at     | × n |          |     |
|     |     |     |           |                                 |     | U s |     |     | e        | C o |          |     |
|     |     | 5   | 1 1 0 / 2 | 9 / 2 3 : 0 2 : 4 7 : 2 9 8 0   |     |     |     |     | F        |     |          |     |
|     |     |     |           |                                 |     |     |     |     | Concept  |     | Question |     |
Latent Feature
Question
|     |     |     |     |     |     |     |     |                    | Student  |                    | Domain  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | -------- | ------------------ | ------- | --- |
|     |     |     |     |     |     |     |     | Knowledge Modeling |          | Knowledge Modeling |         |     |
Figure1:KnowledgeModelingviaGranularRank-BasedTensorFactorization.
Thisisbasedonanintuitiveassumptionthatthelaterattemptson notfollowsuchanassumption.Toaddressthis,weaddarank-
aquestionaremoreinformativethantheearlierones.Forinstance, basedconstrainttothetensorfactorizationmodel,inspiredby[4].
ifstudentsslippedonceonthesamequestion,theyarelesslikely Inparticular,wewouldliketomakesurethatstudentknowledge
toslipagain.Therefore,weusethecurrentattemptvaluesifthey increasesintheproblem-relatedconceptsafterthestudentinteracts
areavailable;otherwise,weusethelessinformativeobservations withaspecificproblem.Thatis𝑠 t ·At+1 ≥ 𝑠 t ·At or𝑘 u,t+1 ≥
fromthepreviousattempt.Themathematicalrepresentationofour 𝑘 u,t.Pleasenotethat,unlike[4]wherethisassumptionisimposed
aggregationoperationissummarizedbelow1. onpredictedperformancevalues,ourassumptionisimposedon
studentknowledge.Thisnewconstrainthelpsustonotonlyrelyon
(cid:40)
xu,t−1,i ifxu,t−1,i isobserved,butxu,t,i isnotobserved thesparseandnoisyperformanceobservationsinthedata,butalso
y =
u,t−˜1,i
xu,t,i ifxu,t,i isobserved toexploitthepredicted(andunobserved)studentperformances.
|     |     |     |     |     |     |     | (5) | Thismeansthatwecanusetheestimatedstudentscoresxˆu,t+1,ifor |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
Byhavingsuchanaggregation,weexpecttoruleoutthenoisy alleviatingthenoisinessandsparsityofthedatatensorandprevent
attemptsthatareobservedduetothecomplexityofproblemsbeing over-fittingtoit.Finally,toaddthisassumption,weminimizethe
rank-basedconstraintinEquation7.Thisconstraintwillleadtoa
solved.Tolearntheparametersofthisaggregatedmodel,weupdate
thelossinEquation2intwowaystoachievethelossfunctionin smoothandglobalknowledgeincreaseinstudents,whileallowing
Equation6.First,weusethenewaggregatedtensorYinsteadof forsmalldecreases,incasethestudentforgetssomeconcepts.
theinputtensorX2.Second,toreducethenoiseevenfurther,we
| usetheweightedleastsquareerrorwithconfidenceω |     |     |     |     |     | asour |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
u,t˜,i
o b je ct iv e fu n c t i o n. W es e t ω u ,t˜ ,i to b e t h e n u m b e ro f st u d e n t u ’ s (cid:16) (cid:16) (cid:17)(cid:17)
|     |     |     |     |     |     |     |     |     | L2 =log σ | 𝑠 ·A˜ | −𝑠 ·A˜ | (7) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | --- |
tr ia ls o n q u es t i o n i by a tt e m p t t˜, to r e p r es e n tt h e co n fi d e n c e i n u t˜+1 u t˜
thatattempt’sdata.Thismeansthatthemorethestudentattempts
| a question, |     | the more | confidence | we have in | our observation |     | of  |     |     |     |     |     |
| ----------- | --- | -------- | ---------- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
studentperformanceinit.
TheFullModel.Eventually,weputtogetherallpartsofthemodel
|     |           |     |          |           |     | T˜        |     | tofactorizetheaggregatedperformancetensorwitharank-based |     |     |     |     |
| --- | --------- | --- | -------- | --------- | --- | --------- | --- | -------------------------------------------------------- | --- | --- | --- | --- |
|     | (cid:213) |     | (cid:16) | (cid:17)2 |     | (cid:213) |     |                                                          |     |     |     |     |
L = ω · y −yˆ +λs ∥su ∥ 2+λa ∥A˜ ∥ 2 constraintandlearnthemodelparameters,includingthestudent
| 1   |     | u,t˜,i | u,t˜,i | u,t˜,i | 2   |     | t˜ F |     |     |     |     |     |
| --- | --- | ------ | ------ | ------ | --- | --- | ---- | --- | --- | --- | --- | --- |
latentfeaturematrix,theknowledgetensor,andtheproblemcon-
|     | u,t˜,i∈Ωobs |     |     |     |     | t˜=1 |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
cepts.Tothisend,weoptimizetheobjectivefunctioninEquation8,
(6)
whichisaweightedcombinationofpreviouslydefinedlossfunc-
Rank-BasedKnowledgeIncreaseConstraint.Finally,whilewe
tions.Thisway,theadaptivegranularityaggregationandtherank-
assumethatstudentknowledgeincreasesasaresultofsolvingmore
basedknowledgeincreaseconstraintcooperatetobothresolvethe
problems(studentlearningassumption(c)),themodelsofardoes sparsityproblemandremovethenoisyobservations,whichleads
|     |     |     |     |     |     |     |     | toamoreaccuratemodel.Here,η |     |     | ∈[0,1]isthetrade-offparame- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --------------------------- | --- |
1Pleasenotethatouraggregationoperationisdifferentfromin[18]inordertomatch terfortheknowledgeincreaseconstraintversustheperformance
ourKTapplication.
predictionfit.Theoutersummationcanbereplacedwithimplicit
2Pleasenotethattheaggregationandparameterestimationaredonesimultaneously
|     |     |     |     |     |     |     |     | feedbacksamplingforsomej |     | <   | t˜−1insteadofthesummation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------- | --- |
inthealgorithm,ratherthanbyfirstlearningafixedYandthenbylearningthe
| parameters(Section2.3). |     |     |     |     |     |     |     | fromj =1toj | =t˜−1. |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --- | --- |
182

KnowledgeTracingforComplexProblemSolving:GranularRank-BasedTensorFactorization UMAP’21,June21–25,2021,Utrecht,Netherlands
knowledgestateforstudents,ourmodelcanestimatehowmucha
studentknowsabouteachconcept.Finallyandmostimportantly,
t˜−1
(cid:213)(cid:213) (cid:16) (cid:16) (cid:17)(cid:17)
minimize L=L 1 +η log σ 𝑠 u ·A˜ j −𝑠 u ·A˜ j+1 byusingthetensorstructure,wecanmeasuretheimportanceof
su,A˜ t˜,qi,bu,bi j=1u,i eachattemptinstudentsequencesandeasilyaggregatetheless
informativeonesintopreviousattempts.
(8)
subjectto

q
su
c
,
,
i
i
≥
≥
0
0 ∀
∀u
c ∈
∈
{
{
1
1
,
,
·
·
·
·
·
·
,
,
C
M
},
}
∀
,∀
i
i
∈
∈
{1
{
,
1
·
,
·
·
·
··
,N
,K
}
}
T
2
h
.3 epse
A
ud
lg
o-
o
co
r
d
it
e
h
of
m
ou
a
r
n
GR
d
A
I
T
m
Em
pl
o
e
d
m
eli
e
s
n
de
t
s
a
c
t
ri
i
b
o
e
n
di
D
nA
e
l
t
g
a
o
i
r
l
it
s
hm13.
 (cid:205)
c
qc,i =1. ∀i ∈{1,···,N} Inlines1-2ofthealgorithm,wepredictstudents’performanceatat-

(9) tempt2.Lines3-20correspondstotheonlinetrainingoftherestof
theattempts.Forlines2and19,weleveragetheprojectedstochastic
cep
T
t
o
co
e
v
n
e
s
r
u
a
r
g
e
e
in
o
t
n
er
e
p
a
r
c
e
h
ta
p
b
r
l
o
e
b
s
le
tu
m
d
,
e
w
nt
e
m
en
o
f
d
o
e
r
l
c
i
e
ng
th
a
e
n
c
d
o
p
n
r
s
o
tr
p
a
o
in
rt
t
i
s
o
i
n
n
a
E
lc
q
o
u
n
a
-
-
gradientdescenttoalternatelyupdateparameters(su,A˜
t˜
,qi,bu,
andbi)tosolvetheminimizationproblem(8).Moreover,toensure
tion9.Specifically,thefirstconstraintonS ensuresthatstudent su,i ≥0∀u,iandqc,i ≥0∀c,i,theupdatedsu,i andqc,i arepro-
latentfeatureweightsorstudentsoftmembershipvaluesinthe
jectedtothefeasiblesetbyclippingthevaluesinto[0,1].Toensure
latentfeaturesarenon-negative.Thesecondandthirdconstraints (cid:205)
c
qc,i =1,∀i ∈{1,···,N},wenormalizethevectorqi.Westart
onQ makesurethattheconceptcontributionsineachproblem
withalargelearningrateforSGDandreduceitbyreceivingnew
arenon-negativeandsumtoone.Thisway,wecaninterpretthe
observationdata.Atline12,weusetheonlinetrainingmechanism
Q valuesashowmuchinformationoneachconceptisprovided
inwhichweonlytrainonnewdatapointswhennewobservation
ineachproblemandcandirectlycomparetheproblemswitheach
dataareadded.Thealgorithm’stimecomplexityislinearwithre-
other,accordingtotheirconcepts.Weuseaprojectedstochastic
specttothenumberofobservations.Sinceeachstudentcouldonly
gradientdescentonthefinallossLtolearntheparametersofthe
workonasinglequestionateachtimeindexandtheaggregation
model.
doesnotincreasethenumberofobservations,thetimecomplexity
OurIntuitiononChoiceoftheModel.Wehavesixmainrea-
isO(MT).
sonsformodelingthestudentknowledgetracingchallengeasa
tensorfactorizationproblem.First,unlikedeeplearningmodels,ten-
sorfactorizationmodelsdonotrequireanabundanceofdata.Our Algorithm1:GRATEKnowledgeModeling.
modelcanworkwellwithmedium-sizeddatasetsthathavemissing Input:Observedstudents’interactionrecords∆obs,includingtraining
andnoisyinformation.Second,ourtensorfactorizationdesignis students’historicalinteractionrecordsandtargetingstudents’first
interactionrecords;
perfectfordiscoveringtheunderlyingdomainknowledgeorcon- 1 Ωobs ={xu,1,i ∈∆obs,∀u,i}(cid:208){xu,2,i ∈∆obs,∀u,i}
ceptstructure.Theproblemlatentfactorsdiscoveredbyourmodel 2 Solvetheproblem(8)withconstraints(9)onΩobs.
canbeinterpretedasthediscoveredconceptsandtheproblemscan 3 Y prev ={xu,1,i ∈∆obs,∀u,i}
beexplainedasweightedcombinationsofthediscoveredconcepts. 4 Createatensor𝑌 withsizeM×1×NandfillY previntoit.
Inotherwords,problemsaresoftmembersoftheconcepts,and 5 foreachtimeindex2≤t <Tdo
6 Filltargetstudents’newrecordsxu,t,iinto∆obs
aconcept’simportancetoeachproblemcanbepresentedasthe 7 X t ={xu,t,i ∈∆obs,∀u,i}
membershipweight.ThisisunlikeKTmodels,suchasPFA[16], 8 Y curr =Y prev ⊔X t;▷ The ⊔ denotes aggregation operation.
thatrelyonapredefineddomainknowledgemodel,orthoselike 9 ifUtility(Y curr )>Utility(Y prev )then
BKT [3] and iBKT [27] that model each concept independently. 10 Y prev =Y curr.
11 FillY curr intolastsliceof𝑌.
Third,ourproposedfactorizationisdesignedforpersonalizedKT 12 else
instudents,followingacollaborative-filtering[10,13]typeofstruc- 13 Y prev =X t.
tureinrecommendersystems.Ourmodelautomaticallyattributes 14 Addanewsliceinto𝑌,andfillX tintothisnewslice.
studentstostudentlatentfeatures,whichcanbeinterpretedas 1 1 5 6 e X n t d +1 ={xu,t+1,i ∈∆obs,∀u,i}
studentabilitiesandlearningpace.Similartoproblems,students 17 Addanewsliceinto𝑌,andfillX t+1intothisnewslice.
havesoftmembershipsintheselatentfeaturesandaseparatesetof 18 Ωobs ={non-missingy u,t˜,i in𝑌}
personalizedknowledgeincreaseparametersarelearnedforeach 19 Solvetheproblem(8)withconstraint(9)onΩobs.
latentfeature.Thiscontrastswithmanyexistingdeeplearning 20 end
basedmodels[2,6,17,28]thatlearnthesamesetofparametersfor
allstudents.Fourth,ourchoiceoftensorfactorizationallowsus
tohavea“global”trendonstudentknowledgeincrease.Addinga
3 EXPERIMENTS
constraint,similartoourrank-basedconstraint,isintrinsictothe
tensorfactorizationmodels[4,23].Whiletherank-basedconstraint Weconductedexperimentsonthreedatasetstoevaluate:1)the
isappliedlocally,itwillresultinaglobalincreasingtrendinstu- model’sperformanceinthestudentperformancepredictiontask,
dentknowledgeintheconceptsthatthestudentisinteractingwith. ascomparedtothebaselines;2)theeffectofdifferentmodelparts
ThisissimilartoIRT[19]andFTDF[20]modelsandisdifferent onitsperformance;3)theaggregationeffectonstudentknowledge
frommodelssuchasDKT[17]andDKVMN[28]thatcannoteasily states;and4)thediscoveredlatentconcepts.
constraintstudentknowledgetrendsinaglobalway.Fifth,unlike
modelssuchasBKT[3]thathaveatwo-state(knownvs.unknown) 3Thesourcecodeisprovidedat:https://github.com/persai-lab/UMAP2021-GRATE
183

UMAP’21,June21–25,2021,Utrecht,Netherlands Wang,etal.
3.1 Datasets ofourmodelwiththesebaselinescanbefoundinthelastpartof
Threerepresentativereal-worlddatasetsareusedinourexperi- Section2.2(modelintuition).Hereisashortdescriptionofeachof
ments.Table1showsthedescriptivestatisticsofthesethreedatasets. thebaselinemethods.
MORF 4 is a framework for accessing and experimenting with • DKT:usesrecurrentneuralnetworkstomodelstudentlearn-
MOOCdataofover77uniquecourses[1].Weusethedatafrom ingononeconceptatatime[17].DKTdoesnothavethestu-
oneofthesecourses,“BigDatainEducation”,asourexperimen- dentknowledgemodelinganddomainknowledgemodeling
taldataset.Thiscourseincludes10complexassignments,eachof components.Theperformanceistypicallynotinterpretable.
whichcontainasetofquestionsthatarerelatedtoeachother.As • DKVMN: is a variant of memory-augmented neural net-
onlythestudents’gradesonthewholeassignmentsareavailable, worksthattracksstudentstatesonmultipleconcepts[28].
wevieweachassignmentasacomplex“problem”inourmodel OurmodelandDKVMNsharesomesimilarities:1)DKVMN
thatcoversmultiplelearningconcepts.Theseassignmentsarepub- alsousesadynamicmatrixtomodelstudent’sknowledge
lishedinsequentialorder,butstudentscanhavemultipleattempts state;2)astudent’sperformanceonaspecificquestionis
oneachassignmentatanytime.Students’scoresarenormalized determinedbytheconceptcoverageofthequestionandthe
into[0,1].CSIntro5 containsstudents’outcomesfrom10differ- student’smasterylevelofeachconcept;and3)theMarkov
entComputerScienceintroductorycoursescollectedduringtwo propertyoftheknowledgestateismodeled.
semesters,usingtheMachineTeachingITS[14].Foreachproblem, • iBKT7:isanextendedhiddenMarkovmodelvariantofthe
thestudentswriteaPythonprogramtosolvetheproposedproblem. standardBayesianknowledgetracing,providingindividu-
Theproblemsarecomplex,assolvingeachproblemrequiresanun- alization on student priors, learning rate, guess, and slip
derstandingofmultipleprogrammingconcepts,suchasvariables, parametersinstudents[15,25,27].
loops,andconditionalstatements.Studentcodesaretestedagainst • PMF:isaclassicprobabilisticmatrixfactorizationmethod
severaltestcases.Thegradegivenateachattemptisthepercentage forestimatingmissingvaluesinmatrices[13].Toapplyit
ofcorrecttestcases.MasteryGrids6 isadatasetcollectedfrom onsequentialstudentdata,weusethelastattemptofeach
students’interactionswiththeMasteryGridsinterface[12]tolearn questionbyeachtimeindextobuildthematrix,masktest
thePythonprogramminglanguage.Itcontainsstudents’binary students’nextquestionsforprediction,andestimatestudent
scores(successorfailure)ontheprogrammingproblemsinthe performanceonmaskedquestionsusingobservedentriesin
system.SimilartoCSIntrodataset,eachproblemsrequiresstudents thematrix.
tounderstandavarietyofconcepts.Figure6showssomeexamples • FDTF8:isaknowledgetracingmethodbasedontensorfac-
ofthequestions. torizationthatenforcesaconstrainttoguaranteeamono-
tonicincreaseinstudentknowledgeasperattempt[20].
3.2 ExperimentalSetupandBaselines • BPTF9:isaBayesiantensorfactorizationmethodforrec-
Weusea5-foldnestedstudent-stratifiedcrossvalidationforourex- ommender systems [23]. Unlike our model, BPTF uses a
periments.Weshuffledandsplitthestudentsrandomlyintofive Gaussiandistributiontosmooththeknowledgetransitions.
groupsandrantheexperimentsforfiverounds.Ateachround,
3.3 GRATEforStudentPerformancePrediction
weselectedoneofthefivestudentgroupsasthetestgroupand
the rest (four groups) as the training group. For test students, Inourfirstsetofexperiments,weevaluatedtheproposedmodel’s
we started by predicting their performance at second attempt, performanceinthetaskofstudentperformanceprediction,ascom-
giventheirfirstattempt.Then,wecontinuedbypredictingtheir paredtothebaselines.TheexperimentalresultsareshowninTa-
performance at the next attempts, one by one, using their pre- ble3.SinceintheMORFandCSIntrodatasets,thescoresarereal
viousattemptsandthetrainingstudents’data.Wereportedthe numbers,weusetherootmeansquarederror(RMSE)betweenthe
average performance over five folds of testing data, as well as predictedandtestscoresforevaluation(alowernumberisbetter).
its calculated 95% confidence interval. In order to see how the IntheMasteryGridsdataset,thestudentperformanceisrecorded
proposedmodelperformedovertime,weperformedonlinetrain- asabinarysuccessorfailure.Asaresult,weusedtheclassification
ingandtesting,inwhichwepredictthetestdataattemptbyat- modeofourproposedmodelandevaluatedtheresultsintermsof
tempt.Forhyper-parametertuningonourmethodandallbase- areaunderthecurve(AUC),inwhichthehighervaluesrepresent
lines,weperformgridsearchover25%ofthetrainingdatathat betterperformance.
is separated for validation. For GRATE, we grid searched over Aswecansee,ourproposedmethodsignificantlyoutperforms
K,C ∈ {3,5,···,17,19}, λs,λa ∈ {0.001,0.005,0.01,0.05,0.1}, mostofthebaselines.Theaggregationandrankedconstraintnot
andη ∈{0.001,0.01,0.1,0.2,0.3}.Thebesthyper-parametersare onlydonotharmtheresults,butcanimprovethemtoo.Based
listedinTable2. on our results, iBKT lags behind other baselines and FTDF has
Toevaluatetheproposedapproach’sperformance,wecompareit thesecond-bestperformanceinMORFandCSIntro,whileDKTis
withsixdifferentbaselinemodelsthatcoverarangeofapproaches betterthanFTDFinMasteryGrids.ThiscouldbebecauseDKTwas
tothetaskofknowledgetracing,fromhiddenMarkovmodelsto designedforpredictingtheprobabilityofsuccessindatasetswith
tensorfactorizationanddeeplearning.Amoredetailedcomparison binaryscores,whileFTDFwasoriginallydesignedforestimating
4https://educational-technology-collective.github.io/morf/ 7iBKTcodefromhttps://github.com/CAHLR/pyBKT
5http://www.machineteaching.tech/en/ 8FTDFcodefromhttps://github.com/persai-lab/Tensor-Factorization-EDM
6http://adapt2.sis.pitt.edu/wiki/Mastery_Grids_Interface 9BPTFcodefromhttps://www.cs.cmu.edu/~lxiong/bptf/bptf.html
184

KnowledgeTracingforComplexProblemSolving:GranularRank-BasedTensorFactorization UMAP’21,June21–25,2021,Utrecht,Netherlands
Table1:Statisticsof3Datasets.
|     |     |     |     |     |     |     |     | Median   | Median    | Median |     | Median    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --- | --------- | --- |
|     |     |     |     |     |     |     |     | #Problem | #Attempts | #Users |     | #Attempts |     |
Dataset #Users #Attempts #Problems #Records PerUser PerUser PerProblem PerProblem
|                                                |              | MORF    |     | 686 | 25  |     | 10 11700 | 8         | 17   | 643.5 |     | 1282 |     |
| ---------------------------------------------- | ------------ | ------- | --- | --- | --- | --- | -------- | --------- | ---- | ----- | --- | ---- | --- |
|                                                |              | CSIntro |     | 120 | 50  |     | 48 2231  | 6         | 16.5 | 17    |     | 37.5 |     |
|                                                | MasteryGrids |         |     | 382 | 70  |     | 30 10357 | 14        | 26   | 166.5 |     | 322  |     |
| Table2:Hyper-parametersofGRATEonthreedatasets. |              |         |     |     |     |     |          | 012345678 |      |       |     |      |     |
|                                                | Dataset      | M       | T   | N   | K C | λs  | λa η     |           |      |       |     |      |     |
tpecnoC
|     | MORF    | 686 | 25  | 10  | 3 9 | 0.001 | 0.001 0.1 |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
|     | CSIntro | 120 | 50  | 48  | 7 9 | 0     | 0.01 0.2  |     |     |     |     |     |     |
MasteryGrids 382 70 30 3 9 0 0 0.01 ]0[ ]1[ ]3 ,2[ ]5 ,4[ ]7 ,6[ ]11 ,01 ,9 ,8[ ]31 ,21[ ]61 ,51 ,41[ ]91 ,81 ,71[ ]02[ ]12[ ]22[ ]42 ,32[ ]52[ ]62[ ]72[ ]82[ ]92[ ]13 ,03[ ]23[ ]33[ ]43[ ]53[ ]73 ,63[ ]83[ ]93[ ]04[ ]14[ ]24[ ]34[ ]44[ ]54[ ]64[ ]74[ ]84[ ]94[
Table3:Studentperformancepredictionresultsineachof Aggregated Attempts
Figure2:GRATE:Averageknowledgetransitionoverallstu-
| the datasets. |     | Average | root | mean | square | error | (RMSE) and |     |     |     |     |     |     |
| ------------- | --- | ------- | ---- | ---- | ------ | ----- | ---------- | --- | --- | --- | --- | --- | --- |
dentsonCSIntrodataset.Thedarkerandbluercellsrepre-
| area | under | curve | (AUC) | over | five folds | are used | to evalu- |             |           |        |         |       |              |
| ---- | ----- | ----- | ----- | ---- | ---------- | -------- | --------- | ----------- | --------- | ------ | ------- | ----- | ------------ |
|      |       |       |       |      |            |          |           | sent higher | knowledge | values | and the | light | and yellower |
ateperformanceondatasetswithnumericalfeedbackand
|     |     |     |     |     |     |     |     | ones represent | lower | knowledge | values. | (Best | viewed in |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | --------- | ------- | ----- | --------- |
binaryfeedback,respectively.∗and∗∗denotesignificance
color).
| levelsofp-value< |     |     | 0.1and< | 0.05inGRATE’simprovement |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
overthebaselines.
|     |     | MORF |     |     | CSIntro | MasteryGrids |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Thisshowsthatneitherofthesetwocomponentswasdispensable
| Method |     | RMSE |     |     | RMSE |     | AUC |     |     |     |     |     |     |
| ------ | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
0.2170∗ 0.4132∗∗ forstudentknowledgemodelingandprovedouradaptivegranular-
|     | DKT |     |     |     |     |     | 0.6968 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
ityaggregationandrank-basedlearningassumptions.
| DKVMN |      | 0.2608∗∗ |     |     | 0.4202∗∗ |     | 0.6881   |     |     |     |     |     |     |
| ----- | ---- | -------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
|       | iBKT | 0.2470∗∗ |     |     | 0.6215∗∗ |     | 0.6048∗∗ |     |     |     |     |     |     |
PMF 0.2118 0.3982∗ 0.5647∗∗ 3.5 GRATEforStudentKnowledgeModeling
0.2235∗∗
BPTF 0.3796 0.6942 AsmentionedinSection2,GRATEcanrepresentstudentknowl-
edgeoverattemptsviatensorK=SA.Inthefollowing,wevisualize
| FDTF |     | 0.2088 |     |     | 0.3752 |     | 0.6877 |     |     |     |     |     |     |
| ---- | --- | ------ | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
GRATE 0.2033 0.3726 0.7035 studentknowledgetostudytheinterpretabilityofdiscoveredknowl-
edgevaluesinstudents.Foreasiervisualizationintwodimensions,
|     |     |     |     |     |     |     |     | we show | the average student | knowledge |     | values, | in each of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------- | --------- | --- | ------- | -------------- |
thescorevalues.Deeplearning-basedmethods(DKTandDKVMN)
discoveredlatentconcepts,overtime.TheresultsfortheCSIntro
| did not | have | the best | performance |     | among | the baseline | models. |     |     |     |     |     |     |
| ------- | ---- | -------- | ----------- | --- | ----- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
datasetareshowninFigure2.Thedarkerandbluercellsrepresent
For example, DKVMN performed poorly on the MORF dataset. higherknowledgevalues,andthelightandyelloweronesrepresent
Thiscouldbebecauseallthebaselineapproaches,especiallythe lowerknowledgevalues.TheX-axisshowstheattemptnumbers.
deeplearningandMarkovmodelones,weredesignedforsimple Aswecansee,studentsstartwithalowaverageknowledgeonall
typesofproblemsandarehighlysensitivetostudentperformance
conceptsintheirfirstattempt,andgraduallygainknowledgeas
fluctuations,whichresultinlessaccurateperformancepredictions.
theytrytheproblems.Thisincreaseisnotstrict,asinsomeattempts
Thiscouldalsobebecauseofthemediumsizeofourdatasetswith thestudentshavealowerlevelofknowledgeascomparedtotheir
afewernumberofbothproblemsandstudents.Theseresultsfrom previousattempt.Thisisexpected,asourrank-basedknowledge
deeplearningmodelsareinagreementwiththeconclusionsin increaseconstraintallowsforoccasionalforgetting.Thelearning
| previous | research |     | that show | that | deep learning | models | are not |     |     |     |     |     |     |
| -------- | -------- | --- | --------- | ---- | ------------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
ratesbetweendifferentconceptsaredifferentfromeachother.Most
| always | the | best choice | for | KT tasks | in terms | of data | efficiency, |     |     |     |     |     |     |
| ------ | --- | ----------- | --- | -------- | -------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
importantly,wecanseethatsomeattemptsareaggregatedtogether
interpretability,andpredictionaccuracy[5,9,22,24].
andsomeareleftasindividualattempts.Forexample,attempts4
and5aresummarizedtogether,andattempts17,18,and19are
| 3.4 | AblationStudy |     |     |     |     |     |     | joinedtogether. |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
Next,weexperimentedtoevaluatetheeffectofdifferentmodel Toevaluatetherank-basedconstrainteffectonstudentknowl-
componentsonitsperformance.Forthat,weconductedanabla- edge,welookedattheaveragestudentknowledgevaluescalcu-
tionstudy,removingonecomponentfromthemodeleachtime: latedusingtheGRATE-W/O-RankmodelshowninFigure3.Inthis
GRATE-W/O-AggforGRATEwithouttheadaptivegranularityag- model,theattemptsarestillaggregated.Wecanseethatremoving
gregationcomponentandGRATE-W/O-RankforGRATEwithout therank-basedconstraintresultsinhigherfluctuationsinstudent
therank-basedcomponent.Theresultsofcomparingthesetwo knowledgevalues.Forexample,studentsstartwithhigherknowl-
modelswith GRATEon thetask ofperformanceprediction are edgevaluesinthefirst(0)attemptinFigure3onlytoloseitinthe
showninTable4.Asindicated,thefullmodelperformedbetter nextattempt.ContrastingthiswithFigure2,weseetheeffectofthe
thanbothGRATE-W/O-AggandGRATE-W/O-Rankinalldatasets. knowledgeincreaseconstraintattheinitialattempts.Asanother
185

| UMAP’21,June21–25,2021,Utrecht,Netherlands |     |     |     |     |     |     |     |     | Wang,etal. |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Table4:Ablationstudyresults.Theaverageperformanceoverfivefoldsofdata±95%confidenceintervalsarereported.
|     |     |     |                | MORF          | CSIntro       |      | MasteryGrids  |     |     |
| --- | --- | --- | -------------- | ------------- | ------------- | ---- | ------------- | --- | --- |
|     |     |     | Methods        | RMSE          |               | RMSE | AUC           |     |     |
|     |     |     | GRATE-W/O-Agg. | 0.2100±0.0140 | 0.3809±0.0089 |      | 0.6849±0.0219 |     |     |
|     |     |     | GRATE-W/O-Rank | 0.2251±0.0109 | 0.3879±0.0244 |      | 0.6837±0.0297 |     |     |
|     |     |     | GRATE          | 0.2033±0.0081 | 0.3726±0.0116 |      | 0.7035±0.0240 |     |     |
mparison
012345678 Variables ments Operators Functions matting References Exception
|     |         |     |     |     |     |     | If Logical Loops Output | Strings Class Objects Value |     |
| --- | ------- | --- | --- | --- | --- | --- | ----------------------- | --------------------------- | --- |
|     | tpecnoC |     |     |     |     |     | State Co                | For Lists Dict              |     |
operation precedancevariable tracing
data type conversion
ambiguous value mapping
list indexingcomparison
value inplace increment
|     | ]0[ ]1[ ]3 ,2[ ]5 ,4[ | ]7 ,6[ ]11 ,01 ,9 ,8[ ]31 ,21[ ]61 ,51 ,41[ ]91 ,81 ,71[ ]02[ ]12[ ]22[ | ]42 ,32[ ]52[ ]62[ ]72[ ]82[ ]92[ ]13 ,03[ ]23[ ]33[ ]43[ ]53[ ]73 ,63[ ]83[ ]93[ | ]04[ ]14[ ]24[ ]34[ ]44[ ]54[ ]64[ ]74[ ]84[ ]94[ |     | placeholder |     |     |     |
| --- | --------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------- | --- | ----------- | --- | --- | --- |
define functionbuilt-in function call
|     |     |     |     |     |     | arithmetic len() |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
string/list manipulation
Aggregated Attempts
Figure3:GRATE-W/O-Rank:Students’AverageKnowledge Figure 5: Matrix Q discovered by GRATE for the Mastery
StateonCSIntroDataset. Gridsdataset.Eachcolumnrepresentsaproblem.Eachrow
representsalatentconcept.(Bestviewedincolor.)
012345678
tpecnoC
|     | 0 1 2 3 4 5 6 7 8 | 9 01 11 21 31 41 51 61 71 | 81 91 02 12 22 32 42 52 62 72 82 92 03 13 23 33 43 | 53 63 73 83 93 04 14 24 34 44 54 64 74 84 94 |     |     |     |     |     |
| --- | ----------------- | ------------------------- | -------------------------------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- |
Raw Attempt Index
| Figure | 4: GRATE-W/O-Agg.: |     | Students’ Average | Knowledge |     |     |     |     |     |
| ------ | ------------------ | --- | ----------------- | --------- | --- | --- | --- | --- | --- |
StateonCSIntroDataset.
|     |     |     |     |     | Figure | 6: Problems | 4 (left), 18 | (top right), and | 24 (bottom |
| --- | --- | --- | --- | --- | ------ | ----------- | ------------ | ---------------- | ---------- |
right)inMasteryGridsdataset.
example,studentknowledgevaluesonConcept2atAttempt29is
3.6 GRATEforDomainKnowledgeModeling
muchhigherthantheirknowledgevaluesatAttempts28and30.
Thisvalueismuchhigherthantheestimatedknowledgevaluesfor AsshowninGRATE’smodelinSection2.2,matrixQcanrepresent
Concept2atAttempt29inFigure2,whenwehavearank-based latentconceptsindifferentproblems.Inthisexperiment,welook
constraint. attheQ-matrixdiscoveredbyGRATEintheMasteryGridsdataset
Toassesswhysomeoftheattemptsareaggregatedtogetherin asacasestudy,tomakesenseofthediscoveredlatentconcepts.
GRATEandsomearenot,welookattheaveragestudentknowledge WechoseMasteryGridsforthisexperiment,sinceeachproblem
valuesintheGRATE-W/O-AggmodelinFigure4.Here,although is assigned to a “topic” in this dataset. We have not used these
therank-basedconstraintexistsinthemodel,weseemorefluc- topics,oranyformofcontentorannotatedconcepts,asaninput
tuationsinthestudentknowledgevalues,ascomparedtothefull toourmodel.Asaresult,weusethemasastandardtoanalyzethe
GRATEmodel.Inparticular,lookingattheattemptsthatareaggre- discoveredmatrixQ.
gatedtogetherinFigure2,weseethathighfluctuationattemptsin Figure5showsthematrixQdiscoveredbyGRATEfortheMas-
Figure4areaggregatedtogethertocreateasmootherknowledge teryGridsdataset.ThelowerX-axisshowsproblemIDs,theupper
increaseinFigure2.Forexample,lookingatConcept2atAttempts X-axisshowsproblemtopicsfromthedataset,andtheY-axisshows
17,18,and19inFigure4,wecanseethattheknowledgevalue thediscoveredlatentconcepts.Eachcelliscoloredaccordingtothe
|     |     |     | =0.30)to18(k | =0.15),just |     |     |     |     |     |
| --- | --- | --- | ------------ | ----------- | --- | --- | --- | --- | --- |
dropsfromAttempt17(withvaluek latentconceptweightintheproblem.Thedarkbluecellshavea
=
toincreaseagaininAttempt19(k 0.20).Similarly,lookingat higherweightandthelightyellowcellshavealowerweight.As
Concept3inthesameattempts,wecanseethattheknowledge thefigureshows,manyproblemswiththesametopichaveahigh
valuedecreasesfromAttempt17(k = 0.15)to18(k = 0.13),but weightinsimilarlatentconcepts.Forexample,Problems3and4
thenincreasesagaininAttempt19(k =0.22).However,inthefull thathavethe“ifstatement"topicbothhaveahighweightinlatent
GRATEresultsinFigure2,thesefluctuationsareconsideredtobe concept3andalowweightinlatentconcept0.Or,Problems16,
insignificant,andAttempts17,18,and19areaggregatedtogether. 17,18,and19thathavethe“listindexing"topicallhaveahigh
Anotherinterestingobservationisthattheinitialattemptsaremore weightinlatentconcept3andalowweightinlatentconcepts1
aggregatedtogether,ascomparedtothelastattempts.Thiscouldbe and2.However,wecanalsoseeproblemswithdifferenttopics
becauseofthemoreconfidentknowledgeestimationsasmoredata thathavesimilarweightsinlatentconceptsandproblemswith
isgatheredaboutstudentlearninginthefinalattempts.Another thesametopicthathavedifferentimportantlatentconcepts.For
potentialreasonisthelowvariabilityofknowledgeamongdifferent example,Problems4(withthe“ifstatement"topic)and5(withthe
studentsatthelargerattempts,sincealessernumberofstudents “comparison"topic)thatbothhaveahighweightinlatentconcepts
| havelongersequences. |     |     |     |     | 3and7. |     |     |     |     |
| -------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
186

KnowledgeTracingforComplexProblemSolving:GranularRank-BasedTensorFactorization UMAP’21,June21–25,2021,Utrecht,Netherlands
Tobetterunderstandandanalyzethisphenomenon,westudy ACKNOWLEDGMENTS
andannotateeachlatentconceptmanually.Tothisend,foreach ThispaperisbaseduponworksupportedbytheNationalScience
latentconceptq,wecomparetheproblemsinwhichqhasahigh FoundationunderGrantNo.1755910.
weightandcomeupwithalistofdetailedconceptsthatarepre-
sentedinthem.Then,weannotatethelatentconceptqwiththe
REFERENCES
intersectionoftheseconcepts.Theseannotationsarecolor-coded
andpresentedintheY-axisofFigure5,nexttothelatentconcept [1] JuanMiguelLAndres,RyanSBaker,GeorgeSiemens,DraganGašević,and
CatherineASpann.2016.Replicating21FindingsonStudentSuccessinOnline
numbers.Theproblemsthathaveahighweightofeachannotated
Learning.Technology,Instruction,Cognition,andLearning10,4(2016),313–333.
latentconceptaremarkedbycircleswiththesamecolorasthecon- [2] YoungduckChoi,YoungnamLee,JunghyunCho,JineonBaek,ByungsooKim,
cept.Forexample,latentconcept7hasahighweightinProblems YeongminCha,DongminShin,ChanBae,andJaeweHeo.2020. Towardsan
AppropriateQuery,Key,andValueComputationforKnowledgeTracing.In
{4,5,18,19,24}thatarefromdifferenttopics.Intheseproblems,be-
Proceedingsofthe7thACMConferenceonLearning@Scale(Virtual).ACM,341–
sidestheirmajortopicannotatedinthedataset,twomainconcepts 344.
repeatedlyappear:“arithmetics"operationsand“len()"function. [3] AlbertTCorbettandJohnRAnderson.1994.KnowledgeTracing:Modelingthe
AcquisitionofProceduralKnowledge.UserModelingandUser-AdaptedInteraction
Forinstance,weshowProblems4,18,and24inFigure6.Wecan 4,4(1994),253–278.
seethatinallofthesethreeproblemsanarithmeticoperationis [4] Thanh-NamDoanandShaghayeghSahebi.2019.Rank-BasedTensorFactoriza-
tionforStudentPerformancePrediction.InProceedingsofThe12thInternational
necessary:Problem4computestheremainderofadivision,Prob-
ConferenceonEducationalDataMining(Montreal,QC,Canada).International
lem18hastheadditionoperation,andProblem24hasadditionand EducationalDataMiningSociety,288–293.
subtractionoperations.Meanwhile,bothProblems18and24use [5] TheophileGervet,KenKoedinger,JeffSchneider,andTomMitchell.2020.Whenis
DeepLearningtheBestApproachtoKnowledgeTracing?JournalofEducational
the“len()”functiontocomputethelengthofalistandadictionary,
DataMining12,3(2020),31–54.
respectively.Wecanseesimilarpatternsinotherproblemswithla- [6] AritraGhosh,NeilHeffernan,andAndrewSLan.2020.Context-AwareAtten-
tentconcept7.Forthis,weannotatedConcept7with“arithmetics" tiveKnowledgeTracing.InProceedingsofthe26thACMSIGKDDInternational
ConferenceonKnowledgeDiscovery&DataMining(Virtual).ACM,2330–2339.
and“len()".Wefollowedthesameprocessforalllatentconcepts, [7] WilliamJHawkins,NeilTHeffernan,andRyanSJDBaker.2014. Learning
asshowninFigure6.ThisshowsthatourmatrixQ canunveil BayesianKnowledgeTracingParameterswithaKnowledgeHeuristicandEmpir-
icalProbabilities.InProceedingsofthe12ndInternationalConferenceonIntelligent
moredetailedandcomplexstructuresinproblemsthatgobeyond
TutoringSystems(Honolulu,HI,USA).Springer,150–155.
simplelabelingofthembasedontheir“topics”.Thediscovered [8] TanjaKäser,SeverinKlingler,AlexanderGSchwing,andMarkusGross.2017.
latentconceptsnotonlyrepresentconceptualsimilaritiesbetween DynamicBayesianNetworksforStudentModeling.IEEETransactionsonLearning
Technologies10,4(2017),450–462.
problems,butalsorelatetostudentskillsandperformanceina
[9] MohammadKhajah,RobertVLindsey,andMichaelCMozer.2016.HowDeep
detailedway. isKnowledgeTracing?.InProceedingsofThe9thInternationalConferenceon
EducationalDataMining(Raleigh,NC,USA).InternationalEducationalData
MiningSociety,94–101.
[10] YehudaKoren,RobertBell,andChrisVolinsky.2009.MatrixFactorizationTech-
niquesforRecommenderSystems.Computer42,8(2009),30–37.
4 CONCLUSIONS [11] AndrewSLan,AndrewEWaters,ChristophStuder,andRichardGBaraniuk.
2014.SparseFactorAnalysisforLearningandContentAnalytics.TheJournalof
Inthispaper,weproposeasolutiontotheknowledgetracingchal- MachineLearningResearch15,1(2014),1959–2008.
lengeforcomplexproblem-solving.Wearguethatnotallstudent [12] TomaszDLoboda,JulioGuerra,RoyaHosseini,andPeterBrusilovsky.2014.
MasteryGrids:AnOpenSourceSocialEducationalProgressVisualization.In
attemptsoncomplexproblemsareequallyinformativetoestimate
Proceedingsofthe9thEuropeanConferenceonTechnologyEnhancedLearning
studentknowledgeandproposeagranularrank-basedtensorfac- (Graz,Austria).Springer,235–248.
torization(GRATE)modelthatadaptivelyaggregatesconsecutive [13] AndriyMnihandRussRSalakhutdinov.2008.ProbabilisticMatrixFactorization.
InProceedingsofthe21stAnnualConferenceonNeuralInformationProcessing
studentattemptsforamoreaccurateestimateofstudentknowl- Systems(Vancouver,BC,Canada).JMLR.org,1257–1264.
edge. Withexperimentingonthreereal-worlddatasetswesup- [14] LauraO.MoraesandCarlosEduardoPedreira.2020.DesigninganIntelligent
TutoringSystemAcrossMultipleClasses.InProceedingsofthe4thEducational
portedourargumentbyshowingthat:(a)GRATEcouldperform
DataMininginComputerScienceEducationWorkshop(Virtual). http://ceur-
betterthanstate-of-the-artbaselinesinpredictingstudentperfor- ws.org/Vol-2734/short2.pdf
mance;(b)bothaggregationandrank-basedconstraintarenec- [15] ZacharyAPardosandNeilTHeffernan.2011. KT-IDEM:IntroducingItem
DifficultytotheKnowledgeTracingModel.InProceedingsofthe19thInternational
essaryforGRATE’ssuperiorperformance;(c)GRATEimproves
ConferenceonUserModeling,Adaptation,andPersonalization(Girona,Spain).
studentknowledgemodelingbydiscoveringandsmoothinghighly ACM,243–254.
fluctuatingandnoisyattemptsandimplicitlydetectingstudents’ [16] PhilipIPavlik,HaoCen,andKennethRKoedinger.2009.PerformanceFactors
Analysis-ANewAlternativetoKnowledgeTracing.InProceedingsofthe14th
slipandguess;and(d)thelatentconceptsdiscoveredbyGRATE InternationalConferenceonArtificialIntelligenceinEducation(Brighton,England).
aremeaningfulandgobeyondthelabeledtopicsinthedata.Al- Springer,531–538.
[17] ChrisPiech,JonathanBassen,JonathanHuang,SuryaGanguli,MehranSahami,
thoughGRATE’sdiscoveredconceptsarelatentandnotdirectly
LeonidasJGuibas,andJaschaSohl-Dickstein.2015.DeepKnowledgeTracing.
human-readable,GRATEcanguideteacherstodeterminewhich InProceedingsofthe28thAnnualConferenceonNeuralInformationProcessing
problemsastudentshouldpracticetogaintherequiredknowledge Systems.JMLP.org,505–513.
[18] EktaGujralRavdeepPasrichaandEvangelosPapalexakis.2020. Adaptive
intheseconcepts.Thelimitationsofourstudyincludetheplausible
GranularityinTimeEvolvingGraphsasTensors.InProceedingsofthe16th
butnotanalyzedassumptions,themediumsizeofourdatasets,and InternationalWorkshoponMiningandLearningwithGraphs(Virtual). http:
nothavingaccesstothedetailedexpertannotationsforlabeling //www.mlgworkshop.org/2020/papers/MLG2020_paper_35.pdf
[19] MarkDReckase.2009. MultidimensionalItemResponseTheoryModels. In
thelatentconcepts.Also,astheexactnessofthediscoveredlatent MultidimensionalItemResponseTheory.Springer,79–112.
conceptsdependsontheaccuracyofourmodelinpredictingstu- [20] ShaghayeghSahebi,Yu-RuLin,andPeterBrusilovsky.2016.TensorFactorization
forStudentModelingandPerformancePredictioninUnstructuredDomain..
dents’performance,theinterpretabilityofthediscoveredmatrixQ
InProceedingsofThe9thInternationalConferenceonEducationalDataMining
canvary. (Raleigh,NC,USA).InternationalEducationalDataMiningSociety.
187

UMAP’21,June21–25,2021,Utrecht,Netherlands Wang,etal.
[21] NguyenThai-Nghe,LucasDrumond,TomášHorváth,ArtusKrohn-Grimberghe, [25] YanboXu,MatthewJJohnson,andZacharyAPardos.2015.ScalingCognitive
AlexandrosNanopoulos,andLarsSchmidt-Thieme.2012. FactorizationTech- ModelingtoMassiveOpenEnvironments.InWorkshoponMachineLearning
niquesforPredictingStudentPerformance.InEducationalRecommenderSystems inEducationatthe32ndInternationalConferenceonMachineLearning. http:
andTechnologies:PracticesandChallenges.IGIGlobal,129–153. //ml4ed.cc/attachments/XuY.pdf
[22] KevinHWilson,YanKarklin,BojianHan,andChaitanyaEkanadham.2016. [26] Chun-KitYeungandDit-YanYeung.2018.AddressingTwoProblemsinDeep
BacktotheBasics:BayesianExtensionsofIRTOutperformNeuralNetworks KnowledgeTracingviaPrediction-ConsistentRegularization.InProceedingsof
forProficiencyEstimation.InProceedingsofThe9thInternationalConference theFifthAnnualACMConferenceonLearningatScale(London,UnitedKingdom).
onEducationalDataMining(Raleigh,NC,USA).InternationalEducationalData ACM,1–10.
MiningSociety,539–543. [27] MichaelVYudelson,KennethRKoedinger,andGeoffreyJGordon.2013.Indi-
[23] LiangXiong,XiChen,Tzu-KuoHuang,JeffSchneider,andJaimeGCarbonell. vidualizedBayesianKnowledgeTracingModels.InInternationalConferenceon
2010.TemporalCollaborativeFilteringwithBayesianProbabilisticTensorFactor- ArtificialIntelligenceinEducation(Berlin,Heidelberg).Springer,171–180.
ization.InProceedingsofthe2010SIAMInternationalConferenceonDataMining [28] JianiZhang,XingjianShi,IrwinKing,andDit-YanYeung.2017.DynamicKey-
(Columbus,OH,USA).SIAM,211–222. ValueMemoryNetworksforKnowledgeTracing.InProceedingsofthe26th
[24] XiaoluXiong,SiyuanZhao,EricGVanInwegen,andJosephEBeck.2016.Going InternationalConferenceonWorldWideWeb(Perth,Australia).ACM,765–774.
DeeperwithDeepKnowledgeTracing.InProceedingsofThe9thInternationalCon- [29] SiqianZhao,ChunpaiWang,andShaghayeghSahebi.2020.ModelingKnowledge
ferenceonEducationalDataMining(Raleigh,NC,USA).InternationalEducational AcquisitionfromMultipleLearningResourceTypes.InProceedingsofThe13th
DataMiningSociety,502–506. InternationalConferenceonEducationalDataMining(Virtual).International
EducationalDataMiningSociety,313–324.
188