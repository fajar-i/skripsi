1390 IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024
Modeling Student Performance Using Feature
Crosses Information for Knowledge Tracing
LixiangXu ,Member,IEEE,ZhanlongWang ,SuojuanZhang ,XinYuan ,Member,IEEE,
MinjuanWang ,Member,IEEE,andEnhongChen ,Fellow,IEEE
Abstract—Knowledgetracing(KT)isanintelligenteducational NOMENCLATURE
technology used to model students’ learning progress and mas-
DescriptionofSomeImportantNotations
tery in adaptive learning environments for personalized educa-
tion. Despite utilizing deep learning models in KT, current ap- Notations Descriptions.
proachesoftenoversimplifystudents’exerciserecordsintoknowl- χ Student’shistoryresponsesequenceofquestion.
edgesequences,whichfailtoexploretherichinformationwithin qi,cj ithquestionandthejthlatentconcept.
i
n
n
e
d
g
i
l
v
e
i
c
d
t
u
t
a
h
l
e
q
c
u
o
e
m
st
p
io
l
n
ex
s.
, h
In
igh
a
e
d
r
di
o
ti
r
o
d
n
e
,
r
e
r
x
e
i
l
s
a
ti
t
n
io
g
ns
K
hi
T
ps
m
b
o
e
d
tw
el
e
s
en
ten
q
d
ue
t
s
o
-
ed
i
Questiondifficultycorrespondingtoqi.
Q,C Setofquestionsandthesetoflatentconcepts.
tionsandlatentconcepts.Therefore,weintroduceanovelmodel
called feature crosses information-based KT (FCIKT) to explore e q i ,ec j Embeddingoftheithquestionandjthlatentcon-
the intricate interplay between questions, latent concepts, and cept.
question difficulties. FCIKT utilizes a fusion module to perform yt Responseofthestudentcorrespondingtoqt.
feature crosses operations on questions, integrating information
from our constructed multirelational heterogeneous graph using
rt Probabilityofcorrectlyresponsethequestionattime
stept.
graphconvolutionalnetworks.Wedeployedamultiheadattention
mechanism,whichenrichesthestaticembeddingrepresentations MRHG Multirelationalheterogeneousgraph.
ofquestionsandconceptswithdynamicsemanticinformationto ht Knowledgestateofstudent.
simulate real-world scenarios of problem-solving. We also used
gatedrecurrentunitstodynamicallycaptureandupdatethestu-
dents’knowledgestateforfinalprediction.Extensiveexperiments I. INTRODUCTION
demonstrated the validity and interpretability of our proposed
EDUCATORSemployteachingtoeffectivelyintroduceand
model.
impart knowledge of novel concepts, theories, and prac-
Index Terms—Graph neural network (GNN), intelligent
ticestostudents,facilitatingcomprehensiveunderstandingand
education, knowledge tracing (KT), recurrent neural network
mastery. The central aspect of teaching activities is the ability
(RNN).
ofeducatorstomonitorandassessstudents’real-timeprogress.
This monitoring is crucial allowing for timely adjustments to
Manuscript received 25 December 2023; revised 8 March 2024; accepted teaching strategies, pacing, and materials, thereby optimizing
16March2024.Dateofpublication22March2024;dateofcurrentversion the growth of knowledge and the enhancement of competence
14 August 2024. This work was supported in part by the National Natural
in students [1]. Traditionally, educators primarily relied on di-
Science Foundation of China under Grant 62176085, Grant 62172458, and
Grant 62207031, and in part by the Intelligent Computing and Information rectclassroominteractionandconventional teachingmethods.
ProcessingKeyLaboratoryoftheMinistryofEducationunderGrant2021A001. However,advancementsinartificialintelligencetechnology,the
(Correspondingauthor:EnhongChen.)
proliferationofmassiveopenonlinecourses[2],andtherapid
Lixiang Xu is with the School of Artificial Intelligence and Big Data,
HefeiUniversity,Hefei230601,China,andalsowiththeSchoolofArtificial developmentofsmarteducationhavesignificantlytransformed
Intelligence,HefeiInstituteofTechnology,Hefei238076,China(e-mail:xlxi- traditionaleducationalapproaches[3].Forinstance,theCOVID-
ang@ustc.edu.cn).
19 pandemic shifted in this landscape, in which conventional
ZhanlongWangiswiththeSchoolofArtificialIntelligenceandBigData,
HefeiUniversity,Hefei230601,China(e-mail:wamreus@163.com). offlineeducationrapidlytransitionedtoonlineplatforms.This
Suojuan Zhang is with the School of Computer Science and Technology, shiftforcededucationalinstitutions,businesses,andindividuals
UniversityofScienceandTechnologyofChina,Hefei230026,China(e-mail:
to embrace online education and expedite the digital transfor-
sjzsj@ustc.edu.cn).
Xin Yuan is with the School of Electrical and Mechanical Engi- mationoftheeducationsector[4].Consequently,theutilization
neering, University of Adelaide, Adelaide, SA 5005, Australia (e-mail: ofeducationaldatamininghasbecomeincreasinglyprominent
xin.yuan@adelaide.edu.au).
inenhancingeducationsystems.Thesetechniquesmonitorstu-
MinjuanWangiswiththeEducationUniversityofHongKong,HongKong,
SAR999077,China,andalsowithSanDiegoStateUniversity,SanDiego,CA dents’knowledgemasterybyanalyzingdatafromtheirprevious
92182USA(e-mail:mwang@sdsu.edu). exerciserecords,enablingmoreeffectiveassessmentoflearning
Enhong Chen is with the Anhui Province Key Laboratory of Big Data
outcomesandpersonalizedlearningplans[5],[6].Thisprocess
Analysis and Application, School of Data Science and School of Computer
ScienceandTechnology,UniversityofScienceandTechnologyofChina,Hefei iscommonlyreferredtoasknowledgetracing(KT)[7].
230026,China,andalsowiththeStateKeyLaboratoryofCognitiveIntelligence, KT was first introduced in the domain of cognitive mod-
UniversityofScienceandTechnologyofChina,Hefei230026,China(e-mail:
eling and intelligent tutoring by Corbett and Anderson [8].
cheneh@ustc.edu.cn).
DigitalObjectIdentifier10.1109/TLT.2024.3381045 Subsequently,thisfieldhasevolved,producingadiverserange
1939-1382©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1391
Fig.1. Exampleillustratingthebenefitsofcross-featuresforKT.
of methods and models, and focused on assessing students’ theseKCshavecertaindependencies,callededges.Itiswidely
comprehension ofknowledge concepts (KCs)[9].Theearliest recognized that integrating a priori knowledge concerning the
model, Bayesian KT (BKT) [10], which often relied on sim- graph-based structureof data[16] into amodel enhances both
plifications of the model’s assumptions, such as assuming a itsperformanceandinterpretability.Therefore,theintegrationof
single concept for each question. Recently, the advent of deep graph-structured data that amalgamate questions and concepts
learninghassignificantlyenhancedinKTresearch,leveraging hasthepotentialtoenhancetheeffectivenessofKTmodels.
itsremarkablecapabilityinfeatureextraction,featurerepresen- Despite the success of previous work, there are still some
tation,andtheexplorationofintricatestructures.Piechetal.[11] importantlimitations.First,GKTdoesnotspecificallyanalyze
pioneeredthislineofresearchandrevealedthepowerofdeep whattypesofgraphsaremoresuitableasinputstothemodel.
learningtechniquesforKT.TheyintroducedthedeepKT(DKT) Thesimilaritycalculationemployedbytheretrievalmechanism
model,whichemploysrecurrentneuralnetworks(RNNs)[12] inCoKTisrelativelysimplistic,focusingsolelyonthestudents’
to capture temporal knowledge states within the sequence of historicalexercisesequences.Thisapproachmayoverlookes-
student–question–answer interactions. Long et al. [13] intro- sentialcontextualinformation,suchasquestiondifficultyandin-
ducedcollaborativeKT(CoKT),anovelmodelthatincorporates teractionsbetweendifferentconcepts.Inaddition,certainGKT
both intrastudent and interstudent information for KT tasks. methods in existence lack comprehensive consideration of the
Theinterstudentinformationisgatheredbyretrievingstudents relationshipsbetweenquestionsandKCs.Whenstudentsengage
who share similar question answering experiences using a se- inreal-worldproblemsolving,itbecomesevidentthatquestions
quence retrieval mechanism. Subsequently, various variants of andKCsexhibitastronger“and”relationshipratherthanan“or”
the KT model have emerged [14], considering diverse proper- relationship.Higherorderfeaturecrossescanpreciselyrealize
ties inherent in the learning sequences, leading to promising the extraction of “and” relationship information between con-
outcomes. cepts.AsillustratedinFig.1,weanalyzedtheexercisesequences
While the RNN-based model demonstrates proficiency in of three students. Bill successfully completed three questions
handlingsequentialdata,itpredominantlyemphasizesthestu- relatedtomultiplicationanddivisionbutencounteredanerroron
dents’latestexerciserecords,disregardingtheirperformanceon atrigonometryquestion.Itisreasonabletoconcludethatthelike-
earlierquestions.Inaccordancewithpedagogicalconventions, lihoodofBillcorrectlyansweringQ5 islow,giventheabsence
itisrecognizedthatstudentsmayinitiallyprovideanincorrect ofassuranceregardinghismasteryoftrigonometry.Incontrast,
responsetoaquestion.However,withsubsequentrepetitionsof Tom demonstrated the ability to answer questions pertaining
thesamequestion,theyacquiretheabilitytorespondcorrectly, to multiplication, division, and trigonometry correctly, despite
indicating an improved level of knowledge mastery compared initially getting Q9 (a division question) wrong. Thus, we can
with their initial correct response. As it is plausible to expect hypothesizethatTomismorelikelytoprovideacorrectresponse
thatstudentswillretaintheirpriorexperiencewhenattempting to Q17. Andy, on the other hand, made errors in questions
the question a second time. Graph-based KT (GKT) emerged. relatedtomultiplication,division,andtrigonometry,indicating
Nakagawa et al. [15] proposed GKT to potentially structure a potential challenges in mastering all the three concepts. This
question as a graph, where the requirements for mastering the observationsuggeststhatstudentswholackproficiencyinmul-
question are divided into KCs, called nodes of the graph, and tiplicationanddivisiontypicallystrugglewithtrigonometryas
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

1392 IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024
well.Comparingstudentsproficientinbothmultiplicationand modules: the knowledge representation module, the modeling
division, as well as trigonometry with those proficient in only module,andtheinferencemodule.
one of these areas, the former combination more effectively Bayesiannetworkswereemployedformodelingandpredict-
underscorestheimportanceoffeaturecrosses[17].Tothebestof ing students’ cognitive states, termed as BKT. The model em-
theauthors’knowledge,trigonometryproblemsinvariablyentail ploysthehiddenMarkovmodel(HMM)[21]toassociatecon-
mathematical operations, such as multiplication and division. ceptswithbinaryknowledgestates(i.e.,learnedorunlearned).
The application of the feature crosses operation extracts more It assumes that each question corresponds to a single concept,
comprehensivefeaturesfrombothquestionsandKCs.Models renderingitincapableofaddressingquestionsinvolvingmultiple
lackinghigherorderfeaturecrossesstruggletouncovertheintri- concepts or representing dependencies among different con-
caterelationshipsbetweenquestionsandunderlyingeducational cepts.DKT,whichappliestemporally“deep”flexiblelongshort
concepts in data, thus hindering the ability to provide precise term memory networks (LSTM) [22] to KT tasks. This model
prediction. employs a multitude of artificial “neurons” to represent latent
In light of the preceding considerations, in this article, we knowledge states and their temporal dynamics, facilitating the
proposedamethodcalledfeaturecrossesinformation-basedKT learningofalatentvariablerepresentationofstudentknowledge
(FCIKT), which introduces higher order crosses information fromthedata.InresponsetoidentifiedlimitationsintheDKT
between the questions and the latent concepts to the previous model, Yeung and Yeung [23] highlighted two main issues: a
GKT.Tobespecific,weemploygraphconvolutionalnetworks reconstruction problem and the volatility of prediction results
(GCNs)[18],[19]toderiveembeddingrepresentationsofques- fortheinputsequence.Then,theyproposeanenhancedversion
tions and latent concepts from multirelational heterogeneous oftheDKTmodelcalledDKT+,achievedbyincreasingthecor-
graphs(MRHGs)thatencompassstudents,questions,andlatent respondingregularizationterm.Wangetal.[5]proposedanovel
concepts.Subsequently,wecombinethedifficultyinformation framework for dynamic cognitive diagnosis, which integrates
of questions with the previously extracted embeddings to per- educational priors from cognitive diagnosis (such as question
form feature crosses operation, yielding richer higher order attributesandinteractionfunctions)intodeeplearning-basedKT
information. In addition, we employ multiheads attention [20] models.Liuetal.[24]proposedexercise-awareKT,exploring
withaforgettingmechanismtoenhancethemodelingofques- bothstudent’sexerciserecordsandthecontentofexercisesfor
tionsandlatentconcepts.Weintegratethehigherordercrosses studentperformanceprediction.
informationwiththegatedrecurrentunits(GRUs)asaclueto The DKT-based study exhibits superior performance when
trace the students’ knowledge state and assess their likelihood comparedwithtraditionalprobabilisticmodels,yetitalsohigh-
of answering the new question correctly. We benchmark our lights significant shortcomings, particularly in terms of inter-
method against seven existing KT models on three publicly pretability. This led to the birth of the most iconic dynamic
available datasets. The experimental results demonstrate the key–valuememorynetworks(DKVMN)[25]forKT.DKVMN
efficacy and superiority of our proposed method in various introducesanexternalmemorymodule[26]tostoretheknowl-
aspects. edgeandupdatethestudent’sknowledgemasteryaccordingly.
In a nutshell, the main contributions of this article are sum- Italsoprovidesspecificinformationaboutstudents’knowledge
marizedasfollows. states across various KCs. Sun et al. [7] proposed DKVMN
1) Weintroduceaninnovativemethodtoenhancetheperfor- withrichfeaturesforKT.Thisapproachincorporatesstudents’
manceofmodelingstudents’knowledgestatesbyincor- behavioralfeaturesanddynamiclearningabilitiesintothedeep
poratinghigherorderfeaturecrossesinformationintoKT. memorynetworkframework,aimingtostrikeabalancebetween
Thisapproachalsofacilitatesamorerobustexplorationof personalizedlearningcapacitiesandbehavioralcharacteristics.
correlationsbetweenquestionsandlatentconcepts. Building upon the transformer architecture [27], numerous
2) WedesignedaneffectivemechanismthatutilizesMRHG studies have endeavored to integrate an attention mechanism
and multihead attention based on forgetting to simu- into the KT model. The central idea revolves around learning
late more realistic scenarios of students responding to theattentionweightsofquestionsduringaseriesofinteractions,
questions. This mechanism offers a more efficient GKT enablingthepredictionoftheprobabilityofcorrectlyanswering
approach. thesubsequentquestion,withdueconsiderationtothequestions’
3) Comprehensive experiments conducted on three real- relative importance. The pioneering work in this area is self-
world datasets show that FCIKT outperforms the state- attentive KT [28], which introduced an attention mechanism
of-the-art models. Additional investigations affirm the intotheKTmodels.Itemploysthescaleddot-productattention
efficiencyofourapproachinenhancingtheperformance mechanismoriginallyproposedbyVaswanietal.[27]toacquire
ofKTmodels. attentionmatricesthroughmultipleattentionheads.
Alltheaforementionedapproachessubstantiallyenhancethe
II. RELATEDWORK performanceoftheKTtask.Thesemethodsalltreatthestudents’
exerciserecordsassequentialdatatobefedintothemodel.To
A. KnowledgeTracing
thebestoftheauthors’knowledge,variousrelationalstructures
KT, a widely studied area in educational technology, fo- frequentlyemergeindailyexerciserecords,includingsimilari-
cusesonmodelingandunderstandingtheprocessofknowledge tiesbetweenKCs,similaritiesbetweenquestions,containment
acquisitionbylearners.KTmodelstypicallyconsistofthreekey relationshipsbetweenquestionsandKCs,andsoon.Fromadata
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1393
structure standpoint, a natural graph structure exists between estimatingreliableparametersforpredictionevenwhendealing
theseKCsandquestions. withhighlysparsedata.Factorisation-machinesupportedneural
|     |     |     |     |     |     |     |     | networks | (FNN) | [36] was | derived | on  | top of | FM, which | first |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ------- | --- | ------ | --------- | ----- |
B. Graph-BasedKT proposedanideatoenhanceFMbyinitializingMLP[37]with
thehiddenvectorslearnedfromtheFMmodel.
| Graph | neural | networks | (GNNs) | [29] | excel | in processing |     |            |      |           |          |     |                |     |           |
| ----- | ------ | -------- | ------ | ---- | ----- | ------------- | --- | ---------- | ---- | --------- | -------- | --- | -------------- | --- | --------- |
|       |        |          |        |      |       |               |     | To capture | both | low-order | features |     | and high-order |     | features, |
graph-structureddatabyeffectivelycapturingandleveragingthe
|            |              |     |         |       |         |             |     | Guo et al. | [38] | proposed | DeepFM. | The | model | comprises | two |
| ---------- | ------------ | --- | ------- | ----- | ------- | ----------- | --- | ---------- | ---- | -------- | ------- | --- | ----- | --------- | --- |
| relational | dependencies |     | between | nodes | to make | predictions | or  |            |      |          |         |     |       |           |     |
components:FM(responsibleforfusinglow-orderfeatures)and
performtasks.Thiscapabilityhasdiverseapplications,spanning
deepneuralnetworks(DNN)(responsibleforfusinghigh-order
socialnetworkanalysis,recommendationsystems,andknowl-
|     |     |     |     |     |     |     |     | features), | enhancing | the | accuracy | of click-through-rate |     |     | (CTR) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | --------------------- | --- | --- | ----- |
edgegraphs.
prediction.TheWide&Deep[39]model,thecoreimplemen-
Nakagawaetal.[15]proposedGKT.Thismarkedthepioneer-
|     |     |     |     |     |     |     |     | tation involves |     | combining | a linear | model | (Wide) | and | a deep |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | -------- | ----- | ------ | --- | ------ |
ingintegrationofGNNs,knownfortheirrobustgraph-structured
neuralnetwork(Deep)tocapturebothmemorizationandgen-
| data representation |     | capabilities, |       | into the  | KT task. | GKT    | con-  |              |           |             |     |             |     |                 |     |
| ------------------- | --- | ------------- | ----- | --------- | -------- | ------ | ----- | ------------ | --------- | ----------- | --- | ----------- | --- | --------------- | --- |
|                     |     |               |       |           |          |        |       | eralization, | resulting | in improved |     | performance |     | for large-scale |     |
| ceptualizes         | the | underlying    | graph | structure | of       | KCs as | graph |              |           |             |     |             |     |                 |     |
recommendersystems.
|     |     |     | ={V1,V2,...,Vn |     |     | }denotesthe |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
G=(V,E),wherethenodeV
| setofallKCs,andtheedgeE |     |     | ⊆V  | ×V denotestherelationship |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
III. PROBLEMFORMULATION
| of these | KCs. Rethinking |     | the KT | task, | they cast | it as a | time- |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ------ | ----- | --------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
series node-level classification task, leveraging conventional In this section, we briefly describe the relevant notations
graphlearningtechniques,suchasmessage-passingGNNsfor included in the KT task used in this article. We summarize
resolution. Recently, to further explore the information em- them in the Nomenclature. KT task is typically formalized as
bedded in knowledge structures, Tong et al. [30] proposed a supervised sequence prediction problem with two primary
structure-based KT, it aims to capture multiple relationships components: 1) modeling a student’s knowledge state through
amongknowledgestructures,suchassimilarityandprecedence hisorherexercisesequencerecordsand2)predictingwhether
relationships,andtomodelthepropagationofinfluenceamong thestudentwillanswerfuturequestioncorrectlyorincorrectly.
|          |        |               |     |       |              |       |     | LetQ={q1,...,qn |     | }representsthesetofalldistinctques- |     |     |     |     |     |
| -------- | ------ | ------------- | --- | ----- | ------------ | ----- | --- | --------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
| KCs. Xia | et al. | [31] proposed | a   | novel | multivariate | graph | KT  |                 |     |                                     |     |     |     |     |     |
∈Q
(MVGKT) framework based on GNNs. MVGKT incorporates tions in the dataset. Each qi may possess an unspecified
GCN and graph Fourier transform to capture both temporal level of difficulty. The embedding of qi is represented by
|            |     |              |             |     |                |         |     | q ∈Rd q.WhenastudentengageswiththequestionsinQ,we |     |     |     |     |     |     |     |
| ---------- | --- | ------------ | ----------- | --- | -------------- | ------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| dependence | and | interstudent | correlation |     | for predicting | student |     | e i                                               |     |     |     |     |     |     |     |
performance. canobserveasequenceofinteractionsχ={x1,x2,...,xt−1 },
|            |     |                |     |          |        |       |        | where xt | =(qt,yt) | consisting |     | of a question | qt  | and answer | yt. |
| ---------- | --- | -------------- | --- | -------- | ------ | ----- | ------ | -------- | -------- | ---------- | --- | ------------- | --- | ---------- | --- |
| To enhance |     | the extraction | of  | valuable | higher | order | infor- |          |          |            |     |               |     |            |     |
mation pertaining to questions and concepts, Yang et al. [32] Here, qt denotes the question answered by the student at time
proposedgraph-basedinteractionmodelforKT(GIKT),which stept.Thebinaryvariableyt representsthestudent’sresponse
constructsaquestion–conceptbipartitegraphandutilizesGCN correspondingtoquestionqt
(cid:2)
| to integrate | question–concept |     | correlations |     | through | embedding |     |     |     |     |     |     |     |     |     |
| ------------ | ---------------- | --- | ------------ | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1, ifthestudent’sanswerisright
propagation. To address the challenge of sparse student data, yt = (1)
Lu et al. [9] proposed concept map driven KT. This approach 0, otherwise.
| explicitly | incorporates | intrinsic |     | information | from | instructional |     |        |          |               |     |      |            |     |          |
| ---------- | ------------ | --------- | --- | ----------- | ---- | ------------- | --- | ------ | -------- | ------------- | --- | ---- | ---------- | --- | -------- |
|            |              |           |     |             |      |               |     | In the | KT task, | the questions |     | in Q | correspond | to  | multiple |
concept maps, including educational relations and topological C={c1,c2,...,cn },
|     |     |     |     |     |     |     |     | latent concepts |     |     |     |     | and the | corresponding |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | ------- | ------------- | --- |
information.
|     |     |     |     |     |     |     |     | embedding | of latent | concept | cj  | is represented |     | by ec | ∈Rd c. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | --- | -------------- | --- | ----- | ------ |
j
|     |     |     |     |     |     |     |     | Therefore, | a vital | aspect | of addressing |     | the KT | task | involves |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------ | ------------- | --- | ------ | ---- | -------- |
C. FeatureCrosses
|     |     |     |     |     |     |     |     | acquiring | effective | representations |     | (i.e., | embeddings), |     | as well |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------------- | --- | ------ | ------------ | --- | ------- |
The concept of feature crosses initially emerged in recom- astotracethestudents’knowledgestateaboutlatentconcepts
mendersystems[33].Itisemployedtointegrateusers’personal (i.e.,theirmasterylevels).
information,behavioraldata,andattributesofitemstoimprove For the purpose of obtaining the probability of student’s
recommendationaccuracyandpersonalization.Featurecrosses, correctresponsetoqt,wedefinethefollowingterminologies.
also known as feature combination, accomplishe a nonlinear Definition3.1(KT): Givenaninteractionsequenceχ,which
transformationofthesamplespacebymultiplyingtwoormore includes the student’s past question-answering history, the KT
features, enhancing the model’s nonlinear capabilities. Essen- problem involves predicting the probability rt of correctly an-
tially,featurecrossesinvolvemappingsamplesfromtheoriginal sweringanewquestionqtatthetimestept,i.e.,rt =(yt =1|
| space to | a high-dimensional |     | feature | space | through | a nonlinear |     | qt,χ). |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | ------- | ----- | ------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
mapping function, similar to the kernel trick [34] in machine Definition 3.2 (MRHG): Given that we are engaged in KT
learning. based on graph structures, heterogeneous graphs that include
Inthecontextoftemporaldynamics,anearlierclassicalmodel multiple relationships between students, questions, and latent
for learning feature combinations is factorization machines conceptsareembeddedintheexerciserecordsofstudents.An
|     |     |     |     |     |     |     |     |     |     | Gˆ  | ={Vˆ,Eˆ}, |     | Vˆ  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
(FM)[35].FMextractsfeaturecombinationsthroughtheinner MRHG is defined as where is the set of all
Eˆ
productofhiddenvectorsbetweenfeaturepairs.Itiscapableof entity types (students, questions, or latent concepts). is the
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

1394 IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024
Fig.2. OverallarchitectureoftheproposedFCIKTmethod.TheMRHGembeddingmoduleconstructsanMRHGutilizingstudentexerciserecordstoextract
embeddingsforbothquestionsandconcepts.Thefeaturecrossesfusionmoduleconductsfeaturecrossesforquestions,concepts,anddifficultyembeddings.The
knowledgestateevolutionmoduleisemployedtoacquireandupdatestudents’knowledgestate.Ultimately,allthegatheredinformationisfusedandemployed
forprediction.
set of multiple relationships that may exist between entities,
andEˆ ={(cid:3)a,(cid:3)c }.(cid:3)a denotestheansweredrelationshipand(cid:3)c A. MRHGEmbeddingModule
denotesthecontainedrelationship(i.e.,astudenthasanswered Similar to previous approaches, FCIKT predicts student re-
aquestion,andaquestioncontainssomelatentconcepts). sponsesbasedonknowledgestatesandquestionrepresentations.
Definition3.3(KnowledgeState): Asstudentsanswerques- Formally,therawdatafeaturesneedtobetransformedintode-
tions,theirknowledgestatesareevolving.Thestudents’knowl- siredembeddedinformationthroughtheembeddinglayer.Our
edgestaterepresentstheirmasterylevelofconcepts.Theknowl- FCIKTmodelutilizesembeddingstorepresentquestions,latent
edge state at step t is denoted by a dh dimensional vector concepts,andstudentresponsesforeachquestionintheexercise
ht ∈Rd h. records. These embeddings are denoted as: eq ∈R|Q|×d , ec ∈
Definition3.4(QuestionDifficulty): Thedifficultyed corre- R|C|×d ,andey ∈R2×d ,where|Q|and|C|representthenumber
i
spondingtoquestionqiisdefinedastheratioofcorrectresponse, ofquestionsandlatentconcepts,respectively,andddenotesthe
computed from the training set. All question difficulties are embeddingsize.Departingfromtraditionalsingle-relationship
formulatedasavectordˆ=[ed]∈R|Q|
. graphs, we incorporate multiple relationships among students
i
andquestions,questionsandconcepts,andconceptsthemselves,
IV. PROPOSEDMETHOD
forming an MRHG. Higher order interaction information be-
Previous GKT models have primarily focused on capturing tween question and concept nodes is extracted by aggregating
higherorderinteractionsbetweenquestionsandlatentconcepts, nodefeaturesusingGCN’smultilayermessagepassingmecha-
neglectingtoincorporatequestiondifficultyinformationwithin nism.
the exercise sequences. In addition, these models have not ef- We preprocess the original dataset accordingly to construct
fectively captured high-quality embeddings between question an MRHG, as shown in Definition 3.2. On top of that, we
features and latent concept features. To address this gap, this establishthreemetapathrelationshipsasfollows.Questionsare
sectionprovidesadetailedintroductiontoourproposedmodel, considered neighbors if they are either answered by the same
termed FCIKT. The FCIKT model incorporates the feature student (Q-S-Q) or cover the same latent concept (Q-C-Q).
crosses higher order information between questions and latent Likewise, latent concepts are neighbors if they are implied by
concepts into the KT task, augmenting the acquisition of stu- thequestionthatisthesourceofthatlatentconcept(C-Q-C).
dents’ knowledge states with question difficulty information. These three metapath relationships guide the utilization of the
An overview of the framework is presented in Fig. 2. The constructed MRHG data as input, enabling the GCN model to
main modules are MRHG embedding module, feature crosses generatenodeembeddingswithintheMRHG.Theembedding
fusionmodule,knowledgestateevolutionmodule,andpredic- layer in this module exclusively emphasizes the state infor-
tionmodule.Importantly,theprocessofacquiringthestudent’s mation of questions and latent concepts, treating students as
knowledge state is trained in conjunction with the prediction the bridge connecting questions. Thus, the question–question
module,wherequestionandconceptembeddings dynamically relationship matrix and question–concept relationship matrix
originate from the MRHG module. The details of FCIKT are play essential roles in the message passing process of GCN.
describedinthefollowingsections. Following the GCN aggregation, we obtain the embeddings
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1395
forquestionsandlatentconceptsthatincorporatehigherorder its expression formulated as the inner product of two vectors
informationfeatures:eq,ec. ui and uj in their eigenspaces z(ui) and z(uj), specifically
GCN is exquisitely designed to extract features from graph z(ui,uj)=<z(ui),z(uj)>.Then,wecanquantifytheinter-
data by combining and stacking multiple graph convolutional actionstrengthbetweenallpairsoffeaturesinaprincipledway
layerstoencodehigherorderneighborinformation.Equation(2) withinourframework.
depictstheprocessbywhichGCNlayersaggregaterepresenta- Wenowturntotheproductlayer,whichaggregatesthetwo
tionsfromneighboringnodesandupdatetherepresentationsof information matrices into single vectors lu and lm. The layer
targetnodes.Γl denotestherepresentationofnodeiinMRHG appliesthefollowingtransformations:
i
at the lth layer and N i denotes the set of neighbors of node i.
(cid:5)3 (cid:5)d
F
ot
o
h
r
e
e
r
x
q
a
u
m
es
p
t
l
i
e
o
,
n
w
sa
h
n
e
d
n
c
c
o
o
n
n
c
s
e
id
p
e
ts
ri
a
n
r
g
e
a
po
q
t
u
en
es
ti
t
a
io
l
n
so
a
u
s
rc
t
e
he
no
ta
d
r
e
g
s
e
.
t
Γ
n
l
o
c
d
a
e
n
,
l
u
(k)
=W
u
(k)(cid:4)U
= (ω
u
(k)
)ijuij (5)
q i i=1j=1
representeitherthequestionembeddinge orthelatentconcept
i
embeddingec (cid:5)3 (cid:5)3
j
⎛ ⎞ l m
(k)
=W m
(k)(cid:4)M
= (ω m
(k)
)ijmij (6)
(cid:5) i=1j=1
(l) ⎝ 1 (l) (l−1) (l)⎠
Γ =σ W Γ +b . (2)
i |N i | j where k ∈[1,...d˜]. (cid:4) denotes elementwise multiplication of
j∈N
i
twomatrices,thentheresultofthismultiplicationissummedup
W(l) and b(l) are the aggregation weights and biases that can toobtainascalar.d˜isthedimensionofthetransformationoflu
(k) (k)
belearnedatthelthGCNlayer,respectively.σisthenonlinear andlm.Wu andWm aretheweightsoftheproductlayer.
aggregationfunction.Therectifiedlinearunit(ReLU)[40]acti- Based on the definition of M and the commutative prop-
vationfunctionischosenduetoitsabilitytocomputeactivation erty in vector inner product, both M and Wm (k) are expected
values using only a threshold, thus enhancing computational to be symmetric. Therefore, employing matrix factorization
efficiency. Following the utilization of the MRHG embedding can mitigate the time complexity. We introduce assumptions
module, we are able to obtain embeddings for both questions Wm (k) =φ(k)φ(k)T andφ(k) ∈R3tofacilitatethesimplification
andlatentconcepts,separately. (k)
oftheformulalm asfollows:
(cid:5)3 (cid:5)3
B. FeatureCrossesFusionModule
W
m
(k)(cid:4)M
= φ
(
i
k)
φ
(
j
k)
<z(ui),z(uj)>. (7)
The MRHG lacks feature on question difficulty, which pre-
i=1j=1
vents the full extraction of higher order information from ex-
Wecan,then,computethequestionembeddingthatincorporates
ercise records. Vie and Kashima [41] employ FM to encode
thedifficultyinformation,whichcanbeexpressedas
side information and investigate feature crosses in the student
modeling task. To ensure the richness of questions and latent
δ =ReLU(lu+lm+ε) (8)
concepts features aggregated by GCN, we draw inspiration
from the CTR prediction task in recommendation scenarios where lu, lm, and bias vector b∈Rd˜ , and lu =(lu (1) ,lu (2) ,...,
andproposeusingthe“product”operationforexamininglocal (d˜) (1) (2) (d˜)
lu )andlm =(lm ,lm ,...,lm ).
dependenciesamongfeaturesfromvariousdomains,ratherthan
the“sum”operation.Weindividuallyadopttheproductlayerof
C. KnowledgeStateEvolutionModule
theproduct-basedneuralnetworks[42]toperformthe“product”
operation on the output of the MRHG module to obtain more Thismoduleseekstomodeltheentiretyofstudents’exercise
comprehensivecross-featureinformation. process,takingintoaccountthehistoricalprogressionofstudent
Specifically,weacquirethequestiondifficultyfeaturedˆfrom
performance.Itaimstouncovertheinvisiblerepresentationofa
theprimarydataset.Theembeddingdimensionmatchesthatof student’sknowledgestateatvariousstagesofquestionsolving.
eq and ec. The outputs of the MRHG module, encompassing FCIKTassumesthatstudent’sknowledgestateisinfluencedby
the question embedding eq, latent concept embedding ec, and boththequestionsandtheircorrespondinganswers.
the question difficulty features are aggregated to produce lin- Along this line, we utilize an RNN with the students’ exer-
ear information U and quadratic information M. The specific ciseprocessχ={(q1,y1),(q2,y2),...,(qt−1,yt−1)}asinput.
formulasarepresentedasfollows: Specifically,ateachtimestep,thenetworkreceivesacombinato-
rialencodingcontainingboththequestionanditscorresponding
U =(u1,u2,u3)= Δ (e q ,e c ,dˆ) (3) answer embedding. Correct (i.e., yt =1) or incorrect answers
M
=[mij]∈R3×3
(4)
(i.e.,yt =0)tothesamequestionactuallyreflectdifferentstates
ofknowledgeacquisition.Consequently,wemustidentifyanap-
wheremij =z(ui,uj)denotesthepairwisefeatureinteraction. propriatemethodtodifferentiatethesesituationsforindividual
Weapplythefundamentalideaofkernelfunction[16]tonon- students.
linearlymapthevectoruintoahigh-dimensionalfeaturespace, Methodologywise, we first concatenate and map the previ-
denotedastheHilbertspace,usingthemappingfunctionz.The ously learned question embedding δ and answer embedding
kernel function requires to satisfy positive definiteness, with ey into d-dimensional exercise representations via a nonlinear
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

| 1396 |     |     |     |     |     |     |     |     | IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024 |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
transformationfunction
|             | ε          |           | (∗)            | (δ⊕e     | y         | (∗)      |            |     |     |     |     |     |     |
| ----------- | ---------- | --------- | -------------- | -------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
|             | e t        | =ReLU(W   |                |          | t)+b      | )        | (9)        |     |     |     |     |     |     |
| where ⊕     | is the     | operation | of aggregating |          | two       | vectors, | i.e., an   |     |     |     |     |     |     |
| elementwise | addition.  |           | It can reflect |          | accurate  | and      | inaccurate |     |     |     |     |     |     |
| responses   | pertaining | to        | a particular   | question |           | for an   | individual |     |     |     |     |     |     |
| student’s   | exercise   | sessions. | This           | process  | naturally |          | models the |     |     |     |     |     |     |
student’slearningbehaviortoobtainhisorherknowledgestate.
Withthestudent’sexerciserepresentation,thehiddenstudent
∈Rd
| state(i.e.,knowledgestate)ht |     |     |     | h   | attimesteptisupdated |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedonthecurrentinputeε
|     |     |     | andthepreviousstateht−1 |     |     |     | inthe |     |     |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
t
recursiveformula.Theprocessisformulatedas Fig.3. Exampleillustratingthebenefitsofmultiheadsattentionmechanism
withforgetting.
ε
|     |     | ht =RNN(e |     | ,ht−1;θh). |     |     | (10) |     |     |     |     |     |     |
| --- | --- | --------- | --- | ---------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
t
questionsandlatentconceptsbystackingmultipleself-attention
| Numerous | variants |     | of RNNs | exist | in the | academic | litera- |     |     |     |     |     |     |
| -------- | -------- | --- | ------- | ----- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- |
ture[24].Inthisarticle,consideringtherelativelymodestsizeof layerstolearndynamicsemanticinformationinstudents’exer-
theprocessedstudent’sexercisedatasetsandaimingtoimprove ciseandresponsebehaviors.Tohighlighttheimportanceofthe
|               |     |             |     |                  |     |     |            | multiheads | attention | forgetting | mechanism | in simulating | real- |
| ------------- | --- | ----------- | --- | ---------------- | --- | --- | ---------- | ---------- | --------- | ---------- | --------- | ------------- | ----- |
| computational |     | efficiency, | we  | have implemented |     |     | (10) above |            |           |            |           |               |       |
by the sophisticated GRU form, i.e., ht =GRU(eε ,ht−1;θh), worldstudentquestioning,weexaminethelearningscenario,as
t
illustratedinFig.3.
| which could | preserve |     | more | long-term | dependency |     | in the |     |     |     |     |     |     |
| ----------- | -------- | --- | ---- | --------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
sequence Thestudentreceived aseriesofquestionsselectedfromthe
|     |     |     |     |     |     |     |     | set {q1,q2,q3 | } and | was | tasked with providing | answers. | These |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | --------------------- | -------- | ----- |
ε
μt =σ(Wμ[e t ,ht−1]+bμ) (11) questions encompass various KCs {c1,c2,c3 }, with the stu-
λ =σ(Wλ[e ε ,ht−1]+bλ) (12) dent’smasterylevelofeachconceptcontinuallyevolving(i.e.,
|     | t   |     | t   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
knowledgestate).Itiswidelyrecognizedthatstudents’learning
ε ,λ (cid:4)ht−1]+bη)
|     | ηt  | = tanh(Wη[e |     | t t |     |     | (13) |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
behaviorsexhibitdynamicchanges,andthemultiheadsattention
ht =(1−μt)(cid:4)ht−1+μt (cid:4)ηt (14) mechanismfacilitatesaccesstodynamicsemanticinformation
inthehistoricalsequence.Atthesametime,students’forgetting
whereWμ,Wλ,andWηaretransformationmatrices,andbμ,bλ,
behaviormayresultinadeclineintheirmasterylevelofKCs.
andbη arebiasvectorstobelearned.(cid:4)denotestheHadamard
Therefore,ourapproachintegratesaforgettingfunctionintothe
product,σ(·)andtanh(·)[43]denotethesigmoidandhyperbolic
multiheadsattentionmechanismtosimulatearealisticscenario
| tangentactivationfunctions,respectively.ht−1 |     |     |     |     |     | summarizesthe |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
ofquestionanswering.
|     |     |     |     |     |     | eε  | ht−1 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
student’s past history of questions solving. t and are We designed the global answered questions of the student
concatenated and transformed into an update gate uk and a R={e q|i∈[1,2,...,t−1]}throughouttheexerciserecords.
i
| reset gate | λ k, respectively. |     | The | former | (11) | decides | the extent |          |              |       |             |                          |     |
| ---------- | ------------------ | --- | --- | ------ | ---- | ------- | ---------- | -------- | ------------ | ----- | ----------- | ------------------------ | --- |
|            |                    |     |     |        |      |         |            | The stud | ent’s answer | state | is obtained | through a self-attention |     |
to which past information is retained and combined with the mechanism.Thisprocessisformulatedas
currentinputataspecifictimestep.Whilethelatter(12)controls
|                                                     |     |     |     |     |     |     |     |     |     | (cid:8) |     | (cid:9) |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- |
| howmuchpastinformationneedstobeforgotten.Thecurrent |     |     |     |     |     |     |     |     |     |         |     | T       |     |
(RWQ)(RWK)
|        |         | ηt   |            |     |     |             |       |     | P =Softmax |     | √   | (RW V | ) (15) |
| ------ | ------- | ---- | ---------- | --- | --- | ----------- | ----- | --- | ---------- | --- | --- | ----- | ------ |
| memory | content | (13) | represents | the | new | information | to be |     |            |     |     |       |        |
dk
| added to | ht, and | is computed |     | based | on the | reset gate | and the |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ----- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- |
connectionbetweentheprevioushiddenstateafterthetransition whereWQ,WK, andWV ∈Rd×d
areprojectionmatrice√sfor
| and the | current | input. The | result | of the | computation |     | generates |                                                  |     |     |     |     |     |
| ------- | ------- | ---------- | ------ | ------ | ----------- | --- | --------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|         |         |            |        |        |             |     |           | query,key,andvaluespace,respectively.R∈R2d×d,and |     |     |     |     | dk  |
thecandidateactivationthroughthetanh(·)activationfunction.
dk
|     |     |     |     |     |     |     |     | is the | scaling factor. | Scaling | by serves | the purpose | of pre- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | ------- | --------- | ----------- | ------- |
Finally,htiscomputedbycombiningtheprevioushiddenstate
ventingexcessivelylargedotproducts.Anexcessivelylargedot
| ht−1 with | the candidate |     | activation | ηt  | (14). | μt is viewed | as  | a   |     |     |     |     |     |
| --------- | ------------- | --- | ---------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
productresultsinsmallgradientsthroughtheSoftmaxfunction.
balancingfactorinthisprocess.
Inpursuitofenhancedsupportforparallelcalculationwhile
learningvariousaspectsofattentionindifferentsubspaces,we
D. MultiheadsAttentionMechanismWithForgetting
calculatetheattentionweightsforH(setto5)headsasfollows:
Self-attentionmechanismisatechniqueemployedtomodel
|     |     |     |     |     |     |     |     |     | Multi−Head(W |     | Q K | V   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
relationships among elements within sequential data, enabling ,W ,W )
| theeffectivehandlingoflong-termdependenciesandtheacqui- |     |     |     |     |     |     |     |     |     |     |     | O   |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
=Concat(head1,...,headH)W
sitionofcomprehensiveglobalinformation.Althoughweexe-
cuted featurecrossesoperation onthequestion,latentconcept Q K V ),1≤i≤H
|     |     |     |     |     |     |     |     |     | headi | =P(W | i ,W i ,W i |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----------- | --- | ---- |
anddifficultyembeddingstoenhancetherichnessoffeaturesin
MRHG.However,thisfundamentallyrepresentsanembedding where the projection is a parameter matrix Wo ∈Rd k ×Hd.
ofthestaticrelationshipbetweenquestionsandlatentconcepts. Simultaneously,itisimperativetoconsiderthatstudents’actual
Inspired by transformer model, we are able to better model question solving process may lead to a deterioration of their
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1397
knowledge state over time. In this regard, we introduce a for- TABLEI
getting mechanism, such as [44], which can be formulated as
STATISTICSOFTHEEDUCATIONALDATASETS
follows:
(cid:10) (cid:11)
F = gi(ξ1 ×exp −ξ 2 Δτ i)|i∈[1,2,...,t−1] (17)
wheregi ∈P,andΔτidenotesthetime-stepintervalsbetween
theithtime-stepandtheinitialmoment.giisthevectorobtained
by(15)basedontheaggregationoftheelementsinsideRateach
time-step.
A. OverviewofDatasets
E. StudentPerformancePredictionModule
WeevaluateperformanceofFCIKTandseveralbaselineKT
For the KT task, the goal we are aiming for is response
models on predicting students’ response using three datasets.
prediction.Inthismodule,incontrasttopreviousKTmethods
DetailedstatisticsforthesedatasetsaregiveninTableI.
that primarily rely on interactions between student knowledge
ASSIST09wascollectedfromtheASSISTmentsonlineedu-
stateshtandexerciserepresentationsqˆ,weconsiderthefollow-
q cationplatform1 duringthe2009–2010academicyear.Recog-
ing interactions: 1) mastery of the target question <ht,e
t
>
and the related latent concept <ht,ec
j
> and 2) the impact of n
in
iz
[
in
2
g
5]
t
,
h
w
at
e
th
f
e
av
o
o
r
r
ig
t
i
h
n
e
al
u
d
p
a
d
ta
a
s
te
e
d
t’s
“
r
s
e
k
l
i
i
l
a
l
b
-b
il
u
it
i
y
ld
h
er
a
”
sb
v
e
e
e
rs
n
io
q
n
u
,
e
2
st
w
io
h
n
i
e
c
d
h
the student’s experience in answering the exercise record on
thetargetquestionisdefinedas<eε,e q >,andtheimpactofthe resolvesdatamodelingissuesandeliminatesduplicatedrecords.
i t
As a result, this dataset contains 3852 students, 123 latent
experienceoftheassociatedlatentconceptonthetargetquestion
isdefinedas<eε,ec >,whereansweredquestionembeddings concepts,and17737questions.
are e q
t
∈Ψt, late i nt j concepts embedding are ec
j
∈Φt, and Φt ASSIST 123 is the most expansive version of the ASSIST-
ments datasets consisting of data collected for one year (from
denotes neighbor latent concept embeddings that question qt
September2012toOctober2013).Inthisdataset,eachquestion
hasalreadyaggregated.Theseinteractionsundergoprocessing
is associated with a single latent concept, but a latent concept
withinanattentionnetworktodeterminetheirindividualweights
is still related to multiple questions. We performed the same
andthesumoftheseweightsiscomputedforprediction
dataprocessingasinATTIST09.Thedatasetcontains27485
students,53065questions,and265latentconcepts.
T
Θi,j =Softmaxi,j(W [∂i,∂j]+b) (18)
EdNet4 was compiled by Choi et al. [45], consisted of a
(cid:5) (cid:5)
substantial dataset. To make data manageable, we randomly
rt = Θi,jf(∂i,∂j) (19)
selected 5000 students that contain 189 latent concepts and
∂ ∈Ψ ∪{h }∂ ∈Φ ∪{ec}
i t t j t j
12161questions.
It is essential to highlight that, for each dataset, our exper-
wherertistheprobabilitythatthelearnerwillbeabletoanswer
iments focused on sequences with a maximum length of 3,
the next question correctly. The function f is deployed using
asshortersequenceslackmeaningfulinformation.Thestudent
the inner product. Similar to the selection of neighbors in the
exercisesequencesofeachdatasetweresplitintotrainingand
MRHG,wesetafixednumberofΨt andΦt bysamplingfrom
testsetsatan8:2ratio.Modelperformancewasevaluatedusing
bothsets.
theareaunderthecurve(AUC)-receiveroperatingcharacteristic
Thefinalobjectivefunctionistominimizethenegativelog-
(ROC)curve,astandardbinaryclassificationmetric.TheAUC
likelihood of predicted rt and true labels yt. Specifically, the
quantifies how accurately a KT model distinguishes correct
cross-entropy loss function is used to backpropagate for the
versusincorrectanswers[4].
gradient,whichcanbeformulatedas
B. Baselines
(cid:5)t
L=− (yilogri+(1−yi)log(1−ri)). (20) ToassesstheperformanceofFCIKT,weusedsevencurrent
i=1 representative KT models as benchmarks for comparison, as
detailedbelow.
V. EXPERIMENTS Traditional models: These methods predict students’ re-
sponsesconsideringthefactorsthatinfluencelearning.
Inthissection,wefirstintroducethedatasets.Then,perfor-
manceofFCIKTiscomparedwithseveralbaselines.Following
that,weconductthecorrespondingablationstudy.Atthesame 1[Online].Available:https://www.assistments.org/
time, we perform the sensitivity analysis on relevant hyperpa- 2[Online]. Available: https://sites.google.com/site/assistmentsdata/home/
rametersofthemodel.Finally,weshowtheinterpretabilityof assistment-2009-2010-data
3[Online]. Available: https://sites.google.com/site/assistmentsdata/home/
FCIKTbyacasestudyandthevisualizationsofquestionnodes
2012-13-school-data-with-affect
embeddingsonlatentconcepts. 4[Online].Available:https://github.com/riiid/ednet
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

| 1398 |     |     |     |     |     | IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024 |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
TABLEII
CHARACTERISTICSOFTHECOMPARISONMETHODS
BKT: BKT is an HMM specifically designed to model a GAKT: Graph attention knowledge tracing (GAKT) is a
student’s latent knowledge state as a set of dichotomous vari- variant of exercise-enhanced RNN with attention mechanism
ablesinasequenceofexercises.TheBKTmodelassumesthat (EERNNA)model[24].GiventhatEERNNAreliesonquestion
onceknowledgeisacquired,itisretained,whileaccountingfor textual descriptions, which are often unavailable from public
factors,suchasguessingandslipping. datasets. Therefore, we utilize the input question embeddings
KTM:Knowledgetracingmachines(KTM)[41]isastate-of- obtainedthroughGCNaggregationasinputstoEERNNAand
the-artfactoranalysismodelthatleveragesFMtointeractwith comparethemaccordingtoitsframeworkdesign.
various features for prediction, making it capable of handling CoKT:CoKT[13]retrievessequencesofpeerstudentswith
awiderangeoffeaturetypes.Toensureexperimentalfairness, analogousquestion-answeringexperiences,extractinginterstu-
only questions, latent concepts, and answers are used as side dent information. This information is then amalgamated with
informationforcomparison. intrastudentdatatotrackstudents’knowledgestatesandpredict
Multistatemethods: These methods maintain one vector for theirquestion-answeringaccuracy.
eachconcepttorepresentstudents’knowledgestates. For better explanation, we summarize the characteristics of
DKVMN: DKVMN has the capacity to utilize relationships theadoptedbaselinemodelinTableII,whereBNisanabbre-
between latent concepts and directly output a learner’s pro- viation for Bayesian network, KVMN for key–value memory
ficiency level for each concept. DKVMN comprises a static network, and MSA for multihead self-attention mechanism or
| matrixreferredtoasthe“key”forstoringlatentconceptsanda |     |     |     |     | variants. |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
dynamicmatrixcalledthe“value”forstoringandupdatingthe
correspondingconceptmasterylevels.
Single-statemethods:Thesemethodsmaintainonevectorto C. ImplementationDetails
representsastudent’sknowledgestate. Comparative experiments involving different model ap-
DKT: DKT employs an RNN model to analyze exercise proacheswereconductedwithinthetensorflowframework.The
sequences and model students’ proficiency in latent concepts. embeddingsizeforquestions,latentconcepts,andanswerswere
Inaddition,DKTholdsthedistinctionofbeingthepioneering uniformlysetat100.Thestudent’sknowledgestate,represented
modeltoapplydeeplearningtoKT.
|     |     |     |     |     | as a vector, | was sized | at 100. | The initial | learning | rate is set |
| --- | --- | --- | --- | --- | ------------ | --------- | ------- | ----------- | -------- | ----------- |
DKT+:ProposedbyYeungandYeung[23],thisisanextended to 0.00025. In order to solve the problem that the loss of the
variant based on DKT. DKT+ redefines the loss function of training set cannot be reduced to a certain level, we set the
originalDKTmodelbyintroducingthreeregularizationterms, learning rate decay rate to 0.92, so that the learning rate will
improving the consistency of its prediction performance over graduallydecayasthetrainingprogress.Duringtheembedding
| time-steps. | The problem | that DKT cannot | reconstruct |     | the ob-     |          |           |          |             |        |
| ----------- | ----------- | --------------- | ----------- | --- | ----------- | -------- | --------- | -------- | ----------- | ------ |
|             |             |                 |             |     | propagation | process, | a maximum | of three | aggregation | layers |
servedinputsisadditionallyaddressed. were used, and a dropout rate of 0.8 was employed to prevent
GIKT: GIKT represents the relationship between questions overfitting.Extensiveexperimentsdemonstratedthattheoptimal
| and KCs | as a graph to learn | valuable | embeddings | for | answer      |              |      |         |         |               |
| ------- | ------------------- | -------- | ---------- | --- | ----------- | ------------ | ---- | ------- | ------- | ------------- |
|         |                     |          |            |     | performance | was achieved | with | a batch | size of | 6. All models |
prediction. GIKT assumes that a KC can be related to more are trained on a Linux server equipped with a 2.90 GHz Intel
thanonequestion,andaquestioncancorrespondtomorethan
|                                                  |     |     |     |     | Xeon Gold | 6226R CPU | and an | NVIDIA | GeForce | RTX 3090 |
| ------------------------------------------------ | --- | --- | --- | --- | --------- | --------- | ------ | ------ | ------- | -------- |
| oneKC.GNNsaggregateembeddingsfromquestionsandKCs |     |     |     |     | GPU.      |           |        |        |         |          |
basedontheirrelationshipsinthegraph.Theseembeddingsfor FCIKT also considers the higher order feature relationships
| each question | in the sequence | of interactions | are | then | fed into |     |     |     |     |     |
| ------------- | --------------- | --------------- | --- | ---- | -------- | --- | --- | --- | --- | --- |
betweenquestionsandlatentconcepts.Intheconstructionofthe
anRNNmodelforpredictingthestudent’sresponsetothenext attentionnetwork,ourexperimentsrevealedthatconsideringthe
question.
similaritybetweenquestionsismoreeffectivethanconsidering
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1399
Fig.4. Resultsofstudentperformancepredictiononthreepublicdatasetsandtheimprovementondifferenttypesofmodels.
thesimilaritybetweenlatentconcepts.Weestablishedthesimi- E. AblationStudy
larityconstraint(Sim_C)parameterat0.7tofilteroutirrelevant
Inthissection,weperformablationstudiestoinvestigatethe
embeddingsintheattentionnetwork.
|     |     |     |     |     |     |     |     | effectiveness | of        | two vital | components | in  | our proposed | model:       |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --------- | ---------- | --- | ------------ | ------------ |
|     |     |     |     |     |     |     |     | 1) multihead  | attention |           | mechanism  | and | 2) feature   | crosses that |
D. ExperimentResults integratequestiondifficulty.Wesetupthreecomparisonsettings
andthedetailsareshownbelow.
WemeasureAUCmetrictoevaluatetheperformanceofthe
|             |        |     |        |            |          |     |            | 1) Remove | multihead |     | attention | (RMHA) | does | not consider |
| ----------- | ------ | --- | ------ | ---------- | -------- | --- | ---------- | --------- | --------- | --- | --------- | ------ | ---- | ------------ |
| model, with | higher | AUC | values | signifying | superior |     | predictive |           |           |     |           |        |      |              |
dynamicsemanticinformationinstudents’questionsolv-
| capabilities | in predicting |     | student’s | responses. |     | Fig. 4 | illustrates |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --------- | ---------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
ingbehavior.
theperformanceofourmodelrelativetothebaselinemodelon
|     |     |     |     |     |     |     |     | 2) Remove | feature | crosses |     | (RFC) indicates |     | that there is no |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | --- | --------------- | --- | ---------------- |
threepublicdatasets.
featurecrossesoperationforquestion,latentconcept,and
AccordingtoFig.4,wecanobservethatourmethodoutper-
difficultyembeddings.
| forms all | seven | baselines | and | achieves | the best | performance. |     |           |      |           |     |           |     |                 |
| --------- | ----- | --------- | --- | -------- | -------- | ------------ | --- | --------- | ---- | --------- | --- | --------- | --- | --------------- |
|           |       |           |     |          |          |              |     | 3) Remove | both | multihead |     | attention | and | feature crosses |
OnASSIST09,ourmodelsurpassesthetopbaseline(GIKT)in
|        |        |           |     |             |     |           |         | (RBMF) | directly |     | concatenates | eq,ec | and | ey as the ex- |
| ------ | ------ | --------- | --- | ----------- | --- | --------- | ------- | ------ | -------- | --- | ------------ | ----- | --- | ------------- |
| AUC by | 0.31%. | On ASSIST | 12, | considering |     | that this | dataset |        |          |     |              |       |     |               |
erciserepresentationinsteadofusingfeaturecrossesand
| has the | most interaction |     | information |     | among | students, | ques- |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | ----------- | --- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
multiheadattention.
tions,andlatentconcepts,interactioninformation,thenonlinear
|                |     |            |       |             |     |                |     | Except      | for the | aforementioned |     | modifications, |     | the remain-     |
| -------------- | --- | ---------- | ----- | ----------- | --- | -------------- | --- | ----------- | ------- | -------------- | --- | -------------- | --- | --------------- |
| transformation | of  | the sample | space | is achieved |     | by introducing |     |             |         |                |     |                |     |                 |
|                |     |            |       |             |     |                |     | ing aspects | of the  | models         | and | experimental   |     | settings remain |
featurecrosses,whichimprovesthenonlinearcapabilityofthe
identical.
model.Thisleadstoaremarkable3.01%improvementinAUC
|     |     |     |     |     |     |     |     | We visualize |     | the performance |     | of these | settings | in Fig. 5. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | -------- | -------- | ---------- |
comparedwiththebestbaseline(GIKT).OnEdNet,ourmodel
|     |     |     |     |     |     |     |     | We can | observe | that the | performance | of  | FCIKT | consistently |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | -------- | ----------- | --- | ----- | ------------ |
surpassesthetopbaselineinAUCby0.59%(GIKT).Notably, deteriorates when any module of the model is removed. This
ourmodeloutperformsGIKT,eventhoughourapproachshares
|     |     |     |     |     |     |     |     | suggests | the importance |     | of all | these modules | to  | performance. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------ | ------------- | --- | ------------ |
abasicframeworkwithit.Thisimpliesthattheincorporationof
Notably,theremovaloffeaturecrossesfromFCIKThasamore
featurecrossesandmultiheadattentionmodulesinKTsignifi-
pronouncedimpactonperformancecomparedtotheremovalof
cantlycontributestoenhancedperformance.
multiheadattention.Thisobservationleadstothehypothesisthat
Itisevidentthatdeeplearning-basedmethodsgenerallysur-
featurecrosses,whichincorporatesinformationaboutquestion
passtraditionalmethodsinmostinstances.Nonetheless,tradi-
|     |     |     |     |     |     |     |     | difficulty, | contribute | more | to  | feature acquisition, |     | while multi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---- | --- | -------------------- | --- | ------------ |
tionalmethodsexhibitcomparableorevensuperiorperformance
headattentionprimarilyinfluencesthestudent’sknowledgestate
| in specific | cases. | For instance, |     | in the context |     | of EdNet, | KTM |     |     |     |     |     |     |     |
| ----------- | ------ | ------------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
inresponsetothequestion.Hence,theabsenceofthemultihead
| outperforms | DKT | and DKT+. |     | Overall, | there | is no substantial |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | -------- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
attentionmodulehasamildereffectonperformance.Itisalso
| disparity | in performance |     | between | multistate |     | and single-state |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
worthnotingthatremovingbothmultiheadattentionandfeature
methods.
crossesduringtrainingsignificantlyimpairstheperformanceof
| We also | compare | our | method’s | performance |     | with | leading |     |     |     |     |     |     |     |
| ------- | ------- | --- | -------- | ----------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
FCIKT,providingfurtherevidencethatbothofourproposedkey
methodsindifferentgroups,asillustratedinFig.4(d).Incontrast
modulesarecrucialforenhancingthemodel’sperformance.
tomultistatemethods,ourapproachutilizesasinglevectorfor
representingstudents’knowledgestatesacrossallconcepts,yet
| it surpasses | them | by outperforming |     | the  | DKVMN        | method | by       |                        |     |     |     |     |     |     |
| ------------ | ---- | ---------------- | --- | ---- | ------------ | ------ | -------- | ---------------------- | --- | --- | --- | --- | --- | --- |
|              |      |                  |     |      |              |        |          | F. SensitivityAnalysis |     |     |     |     |     |     |
| 3.62%–7.37%  | in   | AUC. Compared    |     | with | single-state |        | methods, |                        |     |     |     |     |     |     |
ourapproachconsistentlydeliverssuperiorperformance,witha 1) Parameter Sensitivity: As mentioned earlier, in the
notableimprovement,especiallyinthecaseofASSIST12,where FCIKT model, higher order information from questions and
itenhancesAUCby3.01%.However,theimprovementisless latent concepts is combined and the similarity constraint is
pronouncedforASSIST09andASSIST12,whereitoutperforms also employed to filter irrelevant embeddings in the attention
these methods by 0.31%–0.59% in AUC. This difference may network.Todeterminethemostsuitablesizeforthisparameter,
beattributedtothetask’srelativeeaseinASSIST09compared weconductedanevaluationofdifferentsizesofSim_Candas-
withotherdatasets. sessedtheirimpactonmodelperformance.Theexperimentwas
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

| 1400 |     |     |     |     |     |     |     | IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
Fig.5. Contributionofdifferentmodulesfordifferentdatasets.
Fig.6. InfluenceofSim_C.
| conducted | on  | the datasets | ASSIST09, |     | ASSIST12, | and | EdNet, |     |     |     |     |
| --------- | --- | ------------ | --------- | --- | --------- | --- | ------ | --- | --- | --- | --- |
respectively.
| We set | Sim_C | values | from | 0.1 to | 1 in | intervals | of 0.1, |     |     |     |     |
| ------ | ----- | ------ | ---- | ------ | ---- | --------- | ------- | --- | --- | --- | --- |
keepingotherhyperparametersconstant.Theperformanceeval-
uationmetricswereAUCandAccuracy(ACC).Asdepictedin
| Fig. 6, | for the | ASSIST09 | dataset | and | the ASSIST12 |     | dataset, |     |     |     |     |
| ------- | ------- | -------- | ------- | --- | ------------ | --- | -------- | --- | --- | --- | --- |
thecurvesforAUCandACCperformancemetricsexhibitsome
| differences, | but | both | reach | their peak | performance | at  | Sim_C |     |     |     |     |
| ------------ | --- | ---- | ----- | ---------- | ----------- | --- | ----- | --- | --- | --- | --- |
=0.7.However,fortheEdNetdataset,theperformancemetric
| curves follow |     | a similar | trend, | and the | optimal | performance |     | is  |     |     |     |
| ------------- | --- | --------- | ------ | ------- | ------- | ----------- | --- | --- | --- | --- | --- |
alsoachievedataSim_Cof0.7.Thesefindingsunderscorethe
importanceofappropriatelycontrollingthecoefficientsforirrel-
evantembeddingsintheattentionnetwork,whichsignificantly
enhancespredictionaccuracy.
| 2) Forgetting |     | Function: | The | multiheads |     | attention | mecha- |     |     |     |     |
| ------------- | --- | --------- | --- | ---------- | --- | --------- | ------ | --- | --- | --- | --- |
nism adeptly captures diverse aspects of questions by adjust- Fig.7. Benefitsofforgettingwithinthemultiattentionmechanism.
| ing attention | weights |     | across | different | subspaces. | Nonetheless, |     |     |     |     |     |
| ------------- | ------- | --- | ------ | --------- | ---------- | ------------ | --- | --- | --- | --- | --- |
accurately tracking students’ knowledge mastery solely based datasets, evaluated using the AUC metric. RFM signifies the
| on the latest | questions |     | while | disregarding | dynamic | changes |     | in  |     |     |     |
| ------------- | --------- | --- | ----- | ------------ | ------- | ------- | --- | --- | --- | --- | --- |
exclusionoftheforgettingfunctioninthemultiattentionmech-
thehistoricalexercisesequencepresentschallenges.Toaddress anism,whilemaintainingothersettingsunchanged.Itisevident
this,weincorporateaforgettingmechanismtomodelthephe-
thattheperformanceofRFMhassignificantlydeclined,substan-
| nomenon                                                   | of students |     | gradually | forgetting | old | knowledge | over |                        |                   |             |           |
| --------------------------------------------------------- | ----------- | --- | --------- | ---------- | --- | --------- | ---- | ---------------------- | ----------------- | ----------- | --------- |
|                                                           |             |     |           |            |     |           |      | tiating the importance | of the forgetting | function in | the FCIKT |
| time.Specifically,eachattentionheadlearnsadecayingforget- |             |     |           |            |     |           |      | model.                 |                   |             |           |
tingfunction,withearlyquestionsexertingthegreatestinfluence
ontheknowledgestate.Thisdifferentiationeffectivelydiscerns
|     |     |     |     |     |     |     |     | G. CaseStudy |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
thevaryingimportanceofquestionsovertimeandmitigatesthe
limitations of multiheads attention processing sequences. The To assess the interpretability of our proposed model, we
forgetting mechanism facilitates deep integration of historical conducted a case study. Fig. 8 illustrates the comprehensive
interactions,enablinglong-termdependentlearning. results. On the left-hand side of the figure, the first column
Fig.7illustratestheperformancecomparisonbetweenFCIKT
representsthestudent’sinitialknowledgemasterylevelwithout
and remove forgetting mechanism (RFM) on three public anypractice(i.e.,T=1),withvaryinglevelsofmasteryforeach
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1401
Fig.8. Visualizationofastudent’spredictionresultsonFCIKT.Anexampleoftheknowledgemasteryleveltrackingofacertainstudentonfiveconceptsduring
his30exercisingsteps,whichispaintedinthemiddlematrix.Left-handsideshowsallconcepts,whicharemarkedindifferentcolors.Toplinerecordshisorher
performanceonthe30questions.Rightradarfigureshowshisorherknowledgemasterylevels[intherange(0,1)]onfiveconceptsbefore(T=1)andafter(T=
30)exercising.
Fig.9. t-SNEvisualizationsofquestionnodesembeddingsonfourlatentconcepts.(a)ASSIST09.(b)ASSIST12.(c)EdNet.
of the five latent concepts. Then, he or she worked on each of accurately, especially when there are limited exercise records
the30questionsrelatedtotheseconcepts.Meanwhile,hisorher at the beginning. Improved performance could be achieved if
masterystate(outputbyFCIKT)oftheselatentconceptsevolved thestudentaccumulatesmoreexerciserecordsoversubsequent
graduallyduringthetrainingprocess.Dynamicallymonitoring steps.
students’masteryofconceptsisacrucialdeterminantforassess- Basedonthestudent’sresponsesto30questions,wecancon-
ingthemodel’sstrengthsandweaknesses,aswellasitscapacity cludethatheorshehasfinallyachievedastrongunderstanding
toeffectivelyextractandleverageintricateeducationaldata. oftheconceptof“multiplicationanddivisionoffractions”and
Specifically, when he or she answers a question correctly partially mastered “exponential function,” “general equation,”
(incorrectly), his or her knowledge state of the corresponding and “eccentricity,” but failed on “factors and highest common
latentconceptincreases(decreases).Forexample,heorsheac- factor,”asillustratedintherightradarfigure.
quiresknowledgeoftheconcept“multiplicationanddivisionof
fractions”aftersuccessfullycompletingthequestioninthethird
H. EmbeddingVisualizationAnalysis
exercisestep.Subsequentquestionsrevealagradualgraspofthis
concept, contrasting with a lack of understanding of “factors Inthissection,weaimtoverifythegraph-basedapproach’s
and highest common factor.” Because he or she completed all capabilitytouncoverhigh-ordersemanticassociationsbetween
thequestionson“multiplicationanddivisionoffractions”,but questionnodesandlatentconceptnodes.OurproposedFCIKT
skipped some related to “factors and highest common factor.” captures the relationships between questions and concepts by
However, an inconsistency arises: in the third exercise step, constructing a graph structure representation of the raw se-
despite answering the questions correctly, his or her mastery quential data. We analyze the feature representations learned
of“factorsandhighestcommonfactor”decreasedslightly.This by FCIKT from MRHG in the clustering analysis of node
discrepancy isduetothemodel’sinabilitytotracethestudent embeddings. Specifically, we use the t-distributed Stochastic
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.

| 1402 |     |     |     |     |     |     |     |     | IEEETRANSACTIONSONLEARNINGTECHNOLOGIES,VOL.17,2024 |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
NeighborEmbedding(t-SNE)[46]toreducethedimensionof [4] G.Abdelrahman,Q.Wang,andB.Nunes,“Knowledgetracing:Asurvey,”
the node embeddings and visualize them in the 2-D space. To ACMComput.Surv.,vol.55,no.11,pp.1–37,2023.
|                 |     |          |     |         |         |                  |     |     | [5] F. Wang | et al., “Dynamic | cognitive | diagnosis: | An  | educational | priors- |
| --------------- | --- | -------- | --- | ------- | ------- | ---------------- | --- | --- | ----------- | ---------------- | --------- | ---------- | --- | ----------- | ------- |
| comprehensively |     | validate | the | learned | feature | representations, |     |     |             |                  |           |            |     |             |         |
enhanceddeepknowledgetracingperspective,”IEEETrans.Learn.Tech-
weintentionallyselectquestionscoveringeachofthefourlatent nol.,vol.16,no.3,pp.306–323,Jun.2023.
[6] S.Wang,H.Wu,J.H.Kim,andE.Andersen,“Adaptivelearningmaterial
concepts(“absolutevalue,”“inequality,”“operationofrational
recommendationinonlinelanguageeducation,”inProc.20thInt.Conf.
numbers,”and“Pythagoreantheorem”).Wethenassigndiffer-
Artif.Intell.Educ.,2019,pp.298–302.
| ent colors | to the | question | nodes | corresponding |     | to  | each | latent |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | ----- | ------------- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
[7] X.Sun,X.Zhao,B.Li,Y.Ma,R.Sutcliffe,andJ.Feng,“Dynamickey-
valuememorynetworkswithrichfeaturesforknowledgetracing,”IEEE
concept.
Trans.Cybern.,vol.52,no.8,pp.8239–8245,Aug.2022.
| Fig. 9 | shows | the compressed |     | 2-D | embeddings |     | of question |     |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | --- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
[8] A.T.CorbettandJ.R.Anderson,“Knowledgetracing:Modelingtheac-
nodes on the three datasets. Notably, question nodes related quisitionofproceduralknowledge,”UserModel.User-AdaptedInteract.,
to the same latent concept tend to cluster together in the 2-D vol.4,pp.253–278,1994.
|             |        |          |       |         |     |         |     |        | [9] Y. Lu, | P. Chen, Y. Pian, | and V. | W. Zheng, | “CMKT: | Concept | map |
| ----------- | ------ | -------- | ----- | ------- | --- | ------- | --- | ------ | ---------- | ----------------- | ------ | --------- | ------ | ------- | --- |
| space. This | result | suggests | that, | despite | the | absence | of  | direct |            |                   |        |           |        |         |     |
drivenknowledgetracing,”IEEETrans.Learn.Technol.,vol.15,no.4,
edges connecting question nodes in MRHG, the graph-based pp.467–480,Aug.2022.
approacheffectivelyextractshigherordersemanticinformation [10] M. V. Yudelson, K. R. Koedinger, and G. J. Gordon, “Individualized
between question and concept nodes fromthegraphstructure. Bayesianknowledgetracingmodels,”inProc.16thInt.Conf.Artif.Intell.
Educ.,2013,pp.171–180.
We speculate that GNNs, acting as feature extractors (e.g., [11] C.Piechetal.,“Deepknowledgetracing,”inProc.Int.Conf.Adv.Neural
GCNs), can capture intricate information from the network Inf.Process.Syst.,2015,pp.505–513.
[12] Y.Yu,X.Si,C.Hu,andJ.Zhang,“Areviewofrecurrentneuralnetworks:
| topology | between | the | question | and | concept | nodes. | This | infor- |     |     |     |     |     |     |     |
| -------- | ------- | --- | -------- | --- | ------- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
LSTMcellsandnetworkarchitectures,”NeuralComput.,vol.31,no.7,
mationisthenintegratedintothevectorrepresentationsofthe pp.1235–1270,2019.
nodesandvisualizedthroughdimensionreductiontoderivethe [13] T.Longetal.,“Improvingknowledgetracingwithcollaborativeinfor-
mation,”inProc.15thACMInt.Conf.WebSearchDataMining,2022,
associationsdistributionofquestionamongthelatentconcepts.
pp.599–607.
Real-worldeducationaldataencompassesintricaterelationships
[14] A.Zanellati,D.D.Mitri,M.Gabbrielli,andO.Levrini,“Hybridmodels
forknowledgetracing:Asystematicliteraturereview,”IEEETrans.Learn.
| among questions |     | and | diverse | concepts. | FCIKT | is  | strategically |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------- | --------- | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Technol.,vol.17,pp.1021–1036,Mar.2024.
poisedtograspthesehigh-orderinteractionsforachievingpre-
|           |          |           |     |           |        |     |             |     | [15] H. Nakagawa, | Y. Iwasawa,      | and         | Y. Matsuo, | “Graph-based | knowledge        |     |
| --------- | -------- | --------- | --- | --------- | ------ | --- | ----------- | --- | ----------------- | ---------------- | ----------- | ---------- | ------------ | ---------------- | --- |
| cision in | modeling | students’ |     | cognitive | states | and | performance |     |                   |                  |             |            |              |                  |     |
|           |          |           |     |           |        |     |             |     | tracing:          | Modeling student | proficiency | using      | graph        | neural network,” | in  |
Proc.IEEE/WIC/ACMInt.Conf.WebIntell.,2019,pp.156–163.
prediction.
[16] L.Xuetal.,“MultiplegraphkernellearningbasedonGMDH-typeneural
network,”Inf.Fusion,vol.66,pp.100–110,2021.
VI. CONCLUSION [17] F.Lietal.,“Explicitsemanticcrossfeaturelearningviapre-trainedgraph
neuralnetworksforCTRprediction,”inProc.44thInt.ACMSIGIRConf.
In this article, we introduce a novel model to address the Res.Develop.Inf.Retrieval,2021,pp.2161–2165.
KT problem. The model utilizes a feature crosses approach to [18] T.N.KipfandM.Welling,“Semi-supervisedclassificationwithgraph
convolutionalnetworks,”inProc.5thInt.Conf.Learn.Representations,
| integrate | questions, | latent | concepts, |     | and question |     | difficulty | in  |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | --------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
2017,arXiv:1609.02907.
| a sequence    | of student |                 | exercises. | This      | enhances | the  | richness | of  |               |                  |           |              |               |             |          |
| ------------- | ---------- | --------------- | ---------- | --------- | -------- | ---- | -------- | --- | ------------- | ---------------- | --------- | ------------ | ------------- | ----------- | -------- |
|               |            |                 |            |           |          |      |          |     | [19] Z. Chen, | J. Xu, T. Peng,  | and C.    | Yang, “Graph | convolutional |             | network- |
|               |            |                 |            |           |          |      |          |     | based         | method for fault | diagnosis | using a      | hybrid of     | measurement | and      |
| the embedding |            | representations |            | extracted | using    | GCN, | surpass- |     |               |                  |           |              |               |             |          |
priorknowledge,”IEEETrans.Cybern.,vol.52,no.9,pp.9157–9169,
| ing previous | GKT | methods. |     | At the | same | time, the | multihead |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | ------ | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sep.2022.
| attention | mechanism, |     | which | integrates | the | forgetting |     | behav- |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ----- | ---------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
[20] Z.Niu,G.Zhong,andH.Yu,“Areviewontheattentionmechanismof
ior, is also used to add dynamic semantic information to the deeplearning,”Neurocomputing,vol.452,pp.48–62,2021.
[21] B.Mor,S.Garhwal,andA.Kumar,“AsystematicreviewofhiddenMarkov
staticembeddingtosimulatemorerealisticquestionanswering
|            |            |     |        |        |         |           |          |     | models | and their applications,” | Arch. | Comput. | Methods | Eng., | vol. 28, |
| ---------- | ---------- | --- | ------ | ------ | ------- | --------- | -------- | --- | ------ | ------------------------ | ----- | ------- | ------- | ----- | -------- |
| scenarios. | Therefore, |     | it can | better | predict | students’ | learning |     |        |                          |       |         |         |       |          |
pp.1429–1448,2021.
performancebasedonbothrichembeddingrepresentationand [22] A.Sherstinsky,“Fundamentalsofrecurrentneuralnetwork(RNN)and
dynamic knowledge state. We compare the performance of longshort-termmemory(LSTM)network,”PhysicaD:NonlinearPhe-
nomena,vol.404,2020,Art.no.132306.
our proposed model with the state-of-the-art KT model on [23] C.-K.YeungandD.-Y.Yeung,“Addressingtwoproblemsindeepknowl-
three public datasets. The results demonstrate the superiority edgetracingviaprediction-consistentregularization,”inProc.5thAnnu.
andinterpretiveeffectivenessinmodelingstudentperformance, ACMConf.Learn.Scale,2018,pp.1–10.
[24] Q.Liuetal.,“EKT:Exercise-awareknowledgetracingforstudentper-
validating its potential to be applied in real-world educational formance prediction,” IEEE Trans. Knowl. Data Eng., vol. 33, no. 1,
settings.Inthefuturework,weplantoimproveandanalyzethe pp.100–115,Jan.2021.
[25] J.Zhang,X.Shi,I.King,andD.-Y.Yeung,“Dynamickey-valuememory
modelbyusingoptimizationideasonnodefeatureengineering.
networksforknowledgetracing,”inProc.26thInt.Conf.WorldWideWeb,
2017,pp.765–774.
REFERENCES [26] A.Gravesetal.,“Hybridcomputingusinganeuralnetworkwithdynamic
externalmemory,”Nature,vol.538,no.7626,pp.471–476,2016.
[1] H. Ma, Z. Huang, W. Tang, H. Zhu, H. Zhang, and J. Li, “Predicting [27] A.Vaswanietal.,“Attentionisallyouneed,”inProc.Int.Conf.Adv.
studentperformanceinfutureexamsvianeutrosophiccognitivediagnosis NeuralInf.Process.Syst.,2017,vol.30,pp.6000–6010.
inpersonalizedE-learningenvironment,”IEEETrans.Learn.Technol., [28] S.PandeyandG.Karypis,“Aself-attentivemodelforknowledgetracing,”
vol.16,no.5,pp.680–693,Oct.2023. inProc.12thInt.Conf.Educ.DataMiningSoc.,2019,pp.384–389.
[2] C.-A.Lee,N.-F.Huang,J.-W.Tzeng,andP.-H.Tsai,“AI-baseddiagnostic [29] Z.Wu,S.Pan,F.Chen,G.Long,C.Zhang,andP.S.Yu,“Acomprehensive
assessmentsystem:IntegratedwithknowledgemapinMOOCs,”IEEE surveyongraphneuralnetworks,”IEEETrans.NeuralNetw.Learn.Syst.,
Trans.Learn.Technol.,vol.16,no.5,pp.873–886,Oct.2023. vol.32,no.1,pp.4–24,Jan.2021.
[3] K.Ahmadetal.,“Data-drivenartificialintelligenceineducation:Acom- [30] S. Tong et al., “Structure-based knowledge tracing: An influence
prehensivereview,”IEEETrans.Learn.Technol.,vol.17,pp.12–31,Jan. propagation view,” in Proc. IEEE Int. Conf. Data Mining, 2020,
| 2024. |     |     |     |     |     |     |     |     | pp.541–550. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore.  Restrictions apply.

XUetal.:MODELINGSTUDENTPERFORMANCEUSINGFEATURECROSSESINFORMATIONFORKNOWLEDGETRACING 1403
[31] Z.Xia,N.Dong,J.Wu,andC.Ma,“Multi-variateknowledgetracking SuojuanZhangreceivedthePh.D.degreeinsoft-
basedongraphneuralnetworkinassistments,”IEEETrans.Learn.Tech- wareengineeringfromtheArmyEngineeringUni-
nol.,vol.17,pp.32–43,Aug.2023. versityofPLA,Nanjing,China,in2022.
[32] Y.Yangetal.,“GIKT:Agraph-basedinteractionmodelforknowledge She is currently a Postdoctoral Fellow with the
tracing,”inProc.Mach.Learn.Knowl.Discov.Databases:Eur.Conf., SchoolofComputerScience,UniversityofScience
2021,pp.299–315. andTechnologyofChina,Hefei,China.Herresearch
[33] S.Wu,F.Sun,W.Zhang,X.Xie,andB.Cui,“Graphneuralnetworks interestsincludemachinelearning,datamining,and
inrecommendersystems:Asurvey,”ACMComput.Surv.,vol.55,no.5, intelligenteducation.
pp.1–37,2022.
[34] L.Xu,L.Bai,X.Jiang,M.Tan,D.Zhang,andB.Luo,“DeepRényi
entropygraphkernel,”PatternRecognit.,vol.111,2021,Art.no.107668.
[35] S.Rendle,“Factorizationmachines,”inProc.IEEEInt.Conf.DataMining,
2010,pp.995–1000.
[36] W.Zhang,T.Du,andJ.Wang,“Deeplearningovermulti-fieldcategorical
data:–Acasestudyonuserresponseprediction,”inProc.38thEur.Conf.
IRRes.Adv.Inf.Retrieval,2016,pp.45–57. Xin Yuan (Member, IEEE) received the B.E. and
[37] Z.Wang,W.Jiang,Y.M.Zhu,L.Yuan,Y.Song,andW.Liu,“DynaMixer: Ph.D.degreesinelectronicengineeringfromtheUni-
AvisionMLParchitecturewithdynamicmixing,”inProc.Int.Conf.Mach. versityofAdelaide,Adelaide,SA,Australia,in2016
Learn.,2022,pp.22691–22701. and2021,respectively.
[38] H.Guo,R.Tang,Y.Ye,Z.Li,andX.He,“DeepFM:Afactorization- HeiscurrentlyundertakingresearchwiththeUni-
machine based neural network for CTR prediction,” in Proc. 26th Int. versityofAdelaide,wherehisresearchinterestsin-
JointConf.Artif.Intell.,2017,pp.1725–1731. cludediscoveringnewapproachesforthecognitive
[39] H.-T.Chengetal.,“Wide&deeplearningforrecommendersystems,”in agent-based systems with artificial general intelli-
Proc.1stWorkshopDeepLearn.RecommenderSyst.,2016,pp.7–10. genceandtheirapplicationsinautonomousandcon-
[40] H.C.Jung,J.Maly,L.Palzer,andA.Stollenwerk,“Quantizedcompressed trolsystems.
sensingbyrectifiedlinearunits,”IEEETrans.Inf.Theory,vol.67,no.6,
pp.4125–4149,Jun.2021.
[41] J.-J.VieandH.Kashima,“Knowledgetracingmachines:Factorization
machinesforknowledgetracing,”inProc.AAAIConf.Artif.Intell.,2019,
vol.33,pp.750–757.
MinjuanWang(Member,IEEE)receivedtheB.A.
[42] Y.Quetal.,“Product-basedneuralnetworksforuserresponseprediction,”
degreeinChineseliteraturefromtheBeijing/Peking
inProc.IEEE16thInt.Conf.DataMining,2016,pp.1149–1154.
University,Beijing,China,in1995,theM.A.degree
[43] S.R.Dubey,S.K.Singh,andB.B.Chaudhuri,“Activationfunctionsin
incomparativeliteraturefromPennStateUniversity,
deeplearning:Acomprehensivesurveyandbenchmark,”Neurocomput-
State College, PA, USA, in 1997, and the Ph.D.
ing,vol.503,pp.92–108,2022.
degree in information science and learning tech-
[44] L.LiandZ.Wang,“Knowledgerelationrankenhancedheterogeneous
nologiesfromtheUniversityofMissouri-Columbia,
learninginteractionmodelingforneuralgraphforgettingknowledgetrac-
Columbia,MO,USA,in2001.
ing,”2023,arXiv:2304.03945.
Since2000,shehasbeenaProfessorandaProgram
[45] Y.Choietal.,“EdNet:Alarge-scalehierarchicaldatasetineducation,”in
Chair of learning design and technology with San
Proc.21stInt.Conf.Artif.Intell.Educ.,2020,pp.69–73.
Diego State University, San Diego, CA, USA. She
[46] L.VanderMaatenandG.Hinton,“Visualizingdatausingt-SNE,”J.Mach.
is a newly appointed Chair Professor of emerging technologies and future
Learn.Res.,vol.9,no.11,pp.2579–2605,2008.
educationwiththeEducationUniversityofHongKong,HongKong.Sheis
aninternationallyrecognizedScholarandhaskeynotedabout45international
conferences.HerresearchinterestsincludeSTEMeducation,newandemerging
LixiangXu(Member,IEEE)receivedtheB.Sc.de- technologiesinvariouseducationalsettings,metaverseandimmersivelearning,
gree in applied mathematics from Fuyang Normal andthedesignandimplementationofartificialintelligence,includingAIGCfor
University,Fuyang,China,in2005,theM.Sc.degree educationandtraining.
inappliedmathematicsfromtheHarbinUniversityof Dr.WangisaMemberofIEEEEducationSociety.Shealsoco-chairstheEd-
ScienceandTechnology,Harbin,China,in2008,and ucationSociety’sTechnicalCommitteeforImmersiveLearning.Inaddition,she
thePh.D.degreeincomputerscienceandtechnology istheEditor-in-ChiefforIEEETRANSACTIONSONLEARNINGTECHNOLOGIES.
fromAnhuiUniversity,Hefei,China,in2017. Sheisrecognizedinternationallyforherresearch,publishing,anddedicated
In2008,heworkedatHuaweiTechnologiesCom- servicetoIEEEandotherscholarlycommunities.
panyLtd.,beforejoiningHefeiUniversity,Hefei,in
thefollowingyear.HeiscurrentlyaProfessorwith
theHefeiUniversity.From2019to2022,hedidPost-
doctoralResearchattheUniversityofScienceandTechnologyofChina,Hefei.
Hiscurrentresearchinterestsincludestructuralpatternrecognition,datamining
andmachinelearning,socialnetworkanalysis,andrecommendersystems. Enhong Chen (Fellow, IEEE) received the Ph.D.
Dr.XuwastherecipientofascholarshiptopursuehisstudyinGermanyas degree in computer science from the University of
ajointPh.D.studentfrom2015to2017. Science and Technology of China (USTC), Hefei,
China,in1996.
HeiscurrentlyaProfessorandtheViceDeanwith
theSchoolofComputerScience,USTC.Hehasau-
thoredorcoauthoredmorethan200papersinrefereed
conferences and journals, including IEEE TRANS-
Zhanlong Wang is currently working toward the ACTIONSONKNOWLEDGEANDDATAENGINEERING,
master’s degree in electronic information with the IEEETRANSACTIONSONMOBILECOMPUTING,ACM
SchoolofArtificialIntelligenceandBigData,Hefei SIGKDDConferenceonKnowledgeDiscoveryand
University,Hefei,China. DataMining(KDD),andConferenceonNeuralInformationProcessingSys-
His research interests include graph neural net- tems.Hiscurrentresearchinterestsincludedataminingandmachinelearning,
works, data mining and knowledge discovery, and socialnetworkanalysis,andrecommendersystems.
intelligenteducationsystems. Dr.ChenwastherecipientoftheBestApplicationPaperAwardonKDD-2008,
BestResearchPaperAwardonICDM-2011,andBestofSIAMInternational
ConferenceonDataMining(SDM)-2015.HeisanAssociateEditorforIEEE
TRANSACTIONSONKNOWLEDGEANDDATAENGINEERING.
Authorized licensed use limited to: Universitaet Muenster. Downloaded on December 09,2024 at 08:24:34 UTC from IEEE Xplore. Restrictions apply.