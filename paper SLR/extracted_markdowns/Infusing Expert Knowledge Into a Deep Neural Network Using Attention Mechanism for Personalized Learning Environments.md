ORIGINALRESEARCH
published:03June2022
doi:10.3389/frai.2022.921476
Infusing Expert Knowledge Into a
Deep Neural Network Using
Attention Mechanism for
Personalized Learning Environments
AngeTatoandRogerNkambou*
ArtificialIntelligenceResearchCenter,DepartmentofComputerScience,UniversitéduQuébecàMontréal,Montreal,QC,
Canada
Machine learning models are biased toward data seen during the training steps. The
modelswilltendtogivegoodresultsinclasseswheretherearemanyexamplesandpoor
results in those with few examples. This problem generally occurs when the classes to
predictareimbalancedandthisisfrequentineducationaldatawhereforexample,there
areskillsthatareverydifficultorveryeasytomaster.Therewillbelessdataonstudents
thatcorrectlyansweredquestionsrelatedtodifficultskillsandwhoincorrectlyanswered
thoserelatedtoskillseasytomaster.Inthispaper,wetackledthisproblembyproposing
a hybrid architecture combining Deep Neural Network architectures— especially Long
Editedby:
ChristosTroussas, Short-Term Memory (LSTM) and Convolutional Neural Networks (CNN)—with expert
UniversityofWestAttica,Greece knowledgeforusermodeling.Theproposedsolutionusesattentionmechanismtoinfuse
Reviewedby: expert knowledge into the Deep Neural Network. It has been tested in two contexts:
NasheenNur,
knowledgetracinginanintelligenttutoringsystem(ITS)calledLogic-Museandprediction
FloridaInstituteofTechnology,
UnitedStates of socio-moral reasoning in a serious game called MorALERT. The proposed solution
AniGrubišic´,
is compared to state-of-the-art machine learning solutions and experiments show that
UniversityofSplit,Croatia
the resulting model can accurately predict the current student’s knowledge state (in
*Correspondence:
RogerNkambou Logic-Muse)andthusenableanaccuratepersonalizationofthelearningprocess.Other
nkambou.roger@uqam.ca experiments show that the model can also be used to predict the level of socio-moral
reasoningskills(inMorALERT).Ourfindingssuggesttheneedforhybridneuralnetworks
Specialtysection:
that integrate prior expert knowledge (especially when it is necessary to compensate
Thisarticlewassubmittedto
AIforHumanLearningandBehavior for the strong dependency—of deep learning methods—on data size or the possible
Change,
unbalanced datasets). Many domains can benefit from such an approach to building
asectionofthejournal
FrontiersinArtificialIntelligence modelsthatallowgeneralizationevenwhentherearesmalltrainingdata.
Received:15April2022
Keywords:usermodeling,deeplearning,attention,socio-moralreasoningskill,logicalreasoningskill,expert
Accepted:13May2022
knowledge,hybridneuralnetworks
Published:03June2022
Citation:
TatoAandNkambouR(2022) 1. INTRODUCTION
InfusingExpertKnowledgeIntoa
DeepNeuralNetworkUsingAttention
Personalization(oradaptation)isafundamentalfunctionwhenbuildingadaptivelearningsystems.
MechanismforPersonalizedLearning
Oneofitsadvantagesistoaddressadiverseaudience(Birketal.,2015).Adaptationhasbeenwidely
Environments.
Front.Artif.Intell.5:921476. consideredinthefieldofAIED(ArtificialIntelligenceInEducation)whereoneofthegoalsisto
doi:10.3389/frai.2022.921476 makeintelligenttutoringsystems(ITS)moreeffective.Theadaptationofcontentandinteractions
FrontiersinArtificialIntelligence|www.frontiersin.org 1 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
based on a dynamic model of the learner remains one of the which means the rare occurrence of incorrect answers, the
main issues addressed in this field (Woolf, 2010). Learning modelwillalsofailtoaccuratelypredictthestudent’sknowledge.
performance can be enhanced immensely by identifying This problem is known in deep learning as the class imbalance
the characteristics of students and adapting contents and problem(Huangetal.,2016)wheretherearefeweroccurrences
presentation to better suit their needs (Tseng et al., 2008). ofdataforacertainclass(e.g.,correctanswersonskilldifficult
Many techniques have been proposed to identify learners’ tomaster),whichresultsinsub-optimalperformance.Awrong
characteristics during interactions with systems. Those usermodelingcansignificantlyaffectthepersonalizationprocess.
techniques include Bayesian Knowledge Tracing (BKT), Inthispaper,weproposetoleveragethisproblembyenhancing
Deep Knowledge Tracing (DKT), or simply the use of neural deep learning models with expert knowledge added using the
networksforusermodeling.Theuser(learner/student)modelis attentionmechanism(Xuetal.,2015).
an abstract description of the user in an environment (Bakkes The main contribution of this work is to show how an
etal.,2012).Usermodelingplaysanimportantroleinadaptive original hybrid deep neural architecture infused with a priori
systems such as ITSs, serious games, MOOCs (Massive Open expert knowledge through attention mechanism improves its
Online Courses), and even the applications and tools that generalization ability. The resulting architecture has proven its
surround us in our daily lives, such as social networks and cell effectiveness for learner modeling and personalization in two
phones.Itisimportanttodevelopasolutionthatisabletomodel educationalsoftware.
the user accurately from certain observations and thus be able
to predict her/his needs, her/his behavior, etc. User modeling
can include Knowledge Tracing which is considered the most 2. RELATED WORK
popular approach for modeling learners. It aims at modeling
2.1. Machine Learning and Deep
how students’ knowledge evolves during learning (Corbett and
Anderson, 1994). The student’s knowledge is modeled as a Learning/AI Approaches for User Modeling
latentvariableandisupdatedbasedonher/hisperformanceson The use of machine learning and deep learning algorithms for
given tasks. It can be formalized as follows: given interactions user modeling purposes has attracted much attention in the
x ,...,x of a learner on a particular learning task, how will past.Ingeneral,thegrowthinthevolumeofavailabledataand
1 t
she/hebehaveatt+1?Thegoalbeingtoestimatetheprobability the improvement of machine learning approaches are behind
p(x t+1 |x 1 ,...,x t ). the recent boom of research in this domain. In data-driven
Deep learning is an approach that has been successfully approaches,researchersusemachinelearninganddeeplearning
appliedinmanydomainsincludingimagesrecognition(Heetal., techniques to develop models to predict users’ intentions and
2016), Natural Language Processing (Collobert and Weston, behaviors and extract user classes or behavioral groups from
2008) and more recently in education for knowledge tracing. the interaction data collected in the system. Each user is thus
Among the different deep learning architectures that exist, the assigned one or more classes of reactions and behaviors based
onethatfitswellforknowledgetracingistheLSTM(LongShort on her/his actions. The most used algorithms in this context
Term Memory) as it can capture the sequential aspect of data aregenerallyK-means(Zakrzewska,2008;Drachenetal.,2016;
useful for prediction. Hence, DKT (Piech et al., 2015) uses a Troussasetal.,2020),deepneuralnetworks(Demuthetal.,2014;
LSTM to predict student performance based on the pattern of Piechetal.,2015;Zhangetal.,2017a;Domladovac,2021;Moon
their responses sequentially over time. DKT traces knowledge etal.,2021),naiveBayesiannetworks(Sternetal.,1999;Pardos
atboththeskillandtheproblem(item)levelsandobservesthe and Heffernan, 2010), and SVMs (Support Vector Machine)
correctness of each answer. At any time step, the input layer (Hearstetal.,1998;Muyuanetal.,2004).
of the DKT is the student’s performance on a single problem MissuraandGärtner(2009)developedamodeltodynamically
related to the skill that she or he is currently working on. In adapt the difficulty of a game based on the clusters extracted
otherwords,theskillassociatedwithandthecorrectnessofthe fromthegamedata.TheyusedtheK-meansalgorithmtocreate
learner’sperformanceoneachitemareusedtopredicthowwell clusters of users, each cluster representing a certain type of
she/hewillperformonthenextitem(Zhangetal.,2017b).Rather player. The adaptation model implemented here was implicit
than constructing a separate model for each skill as BKT does, and controlling: each cluster corresponds to a certain level of
DKT models all skills jointly (Piech et al., 2015; Khajah et al., difficulty.TheyusedtheSVMalgorithmandaregressionmodel
2016).IthasbeenshownthatDKTcanrobustlypredictwhether inapredictionmodeltopredictusers’behavior,includingactions
or not a student will solve a particular problem correctly given taken, decisions made, and the cluster they might belong to.
theaccuracyofhistoricsolutions(Wangetal.,2017;Zhangetal., Once this cluster was determined, the difficulty was modified
2017b). accordinglyduringthegame.Haetal.(2011)proposedamodel
However, they are biased toward the data they have oftheplayerrepresentingthegoalsheistryingtoreach.Todo
seen before (it is a data-driven approach). Therefore, the so,theydevelopedaframeworkbasedontheuseoftheLogical
generalization capability of a deep learning model depends on Markov Random Field (an undirected probabilistic graphical
the training data. For problems (or skills) that are difficult to modelwithstructuresdeterminedbyfirst-orderlogicformulas)
master which means the rare occurrence of correct answers, for goal recognition. Goal recognition is the task of inferring
the model will be unable to accurately predict the student’s users’ intended goals from observed sequences of actions. It
knowledge. In the same vein, for skills that are easy to master was used in Crystal island (Rowe et al., 2009), a game-based
FrontiersinArtificialIntelligence|www.frontiersin.org 2 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     |     |             |        |     |          | HybridNeuralNetworkforPersonalization |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | -------- | ------------------------------------- | --- | --- | --- |
|                |     |     |     |     |     |     |     | 2.2. Hybrid | Neural |     | Networks |                                       |     |     |     |
learningenvironmentwherelearners’goalsareinferredthrough
their responses to questions that the system asked narratively. Approaches using neural networks are called data-driven
YannakakisandHallam(2009)proposedareal-timeadaptation techniques since the training and the extracted model depend
model whose objective was to optimize user satisfaction. An onlyonthetrainingdata.Theirperformanceishighlydependent
artificial neural network and a parameter selection algorithm on the quantity and quality of the data. In general, the use of
wereappliedtodatafromasurvey(responsestoquestionnaires fully data-driven approaches requires the acquisition of a huge
administeredbeforeandduringtheuseofthesystem)andfrom amount of data, which is not always practical or realistic for
|              |             |         |     |          |       |           |          | economic | reasons | or because | of  | the complexity |     | of the | process |
| ------------ | ----------- | ------- | --- | -------- | ----- | --------- | -------- | -------- | ------- | ---------- | --- | -------------- | --- | ------ | ------- |
| the activity | log (score, | average |     | response | time, | etc.), to | generate |          |         |            |     |                |     |        |         |
a prediction model of user satisfaction. Drachen et al. (2012) involved.Thereareseveraldomainswherethereisfewtraining
proposed a grouping of different observable behaviors in the data but where a priori and/or a posteriori knowledge are
system.Thegoalwastoobtainclassesofbehaviorstomodelthe available. This is particularly the case in the fields of education
andthehumanities.Howcanapurelydata-drivenbutefficient
| users. They | use | data mining | algorithms |     | including | K-Averages |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ---------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and Simplex Volume Maximization (SIVM). Similarly, Gow architecture benefit from this knowledge often acquired over
etal.(2012)proposedausermodelbuiltfromasemi-automatic years of research? Such solutions combining data-driven and
|     |     |     |     |     |     |     |     | theory-driven | approaches |     | are | considered | hybrid. | Other | works |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | --- | ---------- | ------- | ----- | ----- |
andunsupervisedlearningapproachcombinedwithmulti-class
|     |     |     |     |     |     |     |     | have focused | on  | hybrid | neural | networks | but in | terms | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------ | -------- | ------ | ----- | ------ |
LinearDiscriminantAnalysis(LDA)(McLachlan,2004)applied
tothelogs.Dassetal.(2021)haveusedtherandomForestmodel combinationofmultipleneuralarchitectures(ChenandZhang,
topredictthedropoutofstudentsfromaMOOCcoursegivena 2021;Sharmaetal.,2021;Yanetal.,2021).
TowellandShavlik(1994)definedhybridlearningtechniques
setoffeaturesengineeredfromstudentdailylearningprogress.
as“methodsthatusetheoreticalknowledgeofadomainandaset
Theemergenceofbigdataandmachinelearningtechniques
haveopenedupseveralpossibilitiesformoreaccuratemodeling ofexamplestodevelopamethodforaccuratelyclassifyingunseen
|     |     |     |     |     |     |     |     | examples | during | training.” | A hybrid | learning | approach |     | should |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | -------- | -------- | -------- | --- | ------ |
ofusersespeciallyinEducationalDataMining(EDM)domain.
|          |          |          |     |            |     |             |     | learn more | efficiently | compared |     | to approaches |     | that use | only |
| -------- | -------- | -------- | --- | ---------- | --- | ----------- | --- | ---------- | ----------- | -------- | --- | ------------- | --- | -------- | ---- |
| Bayesian | and deep | learning |     | techniques | are | well-suited | to  |            |             |          |     |               |     |          |      |
the situation. They have allowed notable results in the field one of the two main sources of information (data and theory).
|               |           |     |              |     |              |     |          | There is | very little | research | on  | the combination |     | of a | priori/a |
| ------------- | --------- | --- | ------------ | --- | ------------ | --- | -------- | -------- | ----------- | -------- | --- | --------------- | --- | ---- | -------- |
| of behavioral | modeling, |     | particularly |     | in knowledge |     | tracing. |          |             |          |     |                 |     |      |          |
posterioriknowledgeanddeeplearningarchitectures.Towellet
| Some authors | have | used | Bayesian | networks |     | for modeling | the |     |     |     |     |     |     |     |     |
| ------------ | ---- | ---- | -------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
knowledge acquisition process (Tato et al., 2017a; Kantharaju al.(whichtoourknowledgeisoneofthefirstresearchworktobe
et al., 2018; Zhang and Yao, 2018). Several other authors have interestedinthisquestion)haveproposedahybridsystemcalled
|               |           |              |     |         |          |        |          | KBANN      | (Knowledge-Based |     | Artificial  | Neural           | Networks). |        | They |
| ------------- | --------- | ------------ | --- | ------- | -------- | ------ | -------- | ---------- | ---------------- | --- | ----------- | ---------------- | ---------- | ------ | ---- |
| recently      | focused   | on knowledge |     | tracing | using    | deep   | learning |            |                  |     |             |                  |            |        |      |
|               |           |              |     |         |          |        |          | map expert | knowledge,       |     | represented | in propositional |            | logic, | into |
| architectures | including | recurrent    |     | neural  | networks | (RNNs) | and      |            |                  |     |             |                  |            |        |      |
longandshort-termmemories(LSTMs)(Piechetal.,2015;Wang neural networks and then refine this reformulated knowledge
|     |     |     |     |     |     |     |     | using back-propagation. |     |     | Coro | et al. (2013) | combined |     | neural |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---- | ------------- | -------- | --- | ------ |
etal.,2017;Zhangetal.,2017b;Monteroetal.,2018;Songetal.,
networkswithsimulatedexpertknowledge.Thesimulatedexpert
2021;Xingetal.,2021)andotherhavefocusedonusermodeling
using the same techniques with some improvements (Yu et al., wasusedtogeneratesomeexamples,whichwerethenaddedto
2019;Nur,2021;Yuanetal.,2021).Itisworthnotingthattheuse the training set of their neural network model. Zappone et al.
|     |     |     |     |     |     |     |     | (2018) recently | did | the | same | by combining | expert | knowledge |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---- | ------------ | ------ | --------- | --- |
ofBayesiannetworkscanbeseenasahybridapproachsincethe
|     |     |     |     |     |     |     |     | and artificial | neural | networks |     | (ANNs) | to optimize |     | wireless |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | -------- | --- | ------ | ----------- | --- | -------- |
networkscanbedesignedmanuallybydomainexperts(Conati
et al., 1997; Horvitz et al., 1998; Rowe and Lester, 2010) or communication networks. They first obtained a training set
|     |     |     |     |     |     |     |     | from the | expert | knowledge | and | then | trained | the ANN | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | --- | ---- | ------- | ------- | --- |
designed(architectureandprobabilitytables)automaticallyfrom
|          |               |     |          |            |     |           |         | this generated | training | set. | Finally, | the pre-trained |     | architecture |     |
| -------- | ------------- | --- | -------- | ---------- | --- | --------- | ------- | -------------- | -------- | ---- | -------- | --------------- | --- | ------------ | --- |
| the data | using machine |     | learning | approaches |     | (Friedman | et al., |                |          |      |          |                 |     |              |     |
1999;Tsamardinosetal.,2006). was refined through a new training phase based on real
| Although      | data-driven |     | methods  | hold      | great       | promise  | for      | measureddata.  |           |         |          |               |            |           |     |
| ------------- | ----------- | --- | -------- | --------- | ----------- | -------- | -------- | -------------- | --------- | ------- | -------- | ------------- | ---------- | --------- | --- |
|               |             |     |          |           |             |          |          | In educational |           | domain, | a priori | and a         | posteriori | knowledge |     |
| automatically | extracting  |     | relevant | features, | they        | can also | extract  |                |           |         |          |               |            |           |     |
|               |             |     |          |           |             |          |          | are usually    | available | and     | are      | used to build | adaptive   | learning  |     |
| meaningless   | information |     | (Demuth  | et        | al., 2014). | For      | example, |                |           |         |          |               |            |           |     |
these methods can extract irrelevant relationships such as a systems such as ITS (Intelligent Tutoring Systems). In other
domains,knowledgemaybeavailablethroughbooksoralready-
| relationship | between        | age | and character |         | choice      | in a game, | since       |               |      |     |            |         |     |         |      |
| ------------ | -------------- | --- | ------------- | ------- | ----------- | ---------- | ----------- | ------------- | ---- | --- | ---------- | ------- | --- | ------- | ---- |
|              |                |     |               |         |             |            |             | built models, | such | as  | rule-based | models. | We  | believe | that |
| both pieces  | of information |     | will          | tend to | be repeated |            | if multiple |               |      |     |            |         |     |         |      |
players of the same age often choose the same character. this knowledge, sometimes acquired during decades of intense
|                 |             |              |                |              |                |     |         | research, | cannot    | simply | be ignored. | Thus,     | we  | propose | an    |
| --------------- | ----------- | ------------ | -------------- | ------------ | -------------- | --- | ------- | --------- | --------- | ------ | ----------- | --------- | --- | ------- | ----- |
| Classification, | prediction, |              | and clustering |              | of behaviorsin |     | today’s |           |           |        |             |           |     |         |       |
|                 |             |              |                |              |                |     |         | approach  | that uses | the    | attention   | mechanism | (Xu | et al., | 2015) |
| adaptive        | systems     | are becoming |                | increasingly | challenging    |     | due to  |           |           |        |             |           |     |         |       |
the volume, high dimensionality, and multi-modality of data and capitalizes on the availability of these a priori and a
(Drachen et al., 2016). Also, the fundamental techniques used posteriori data to reduce the amount of empirical data needed
|               |           |          |        |          |             |         |          | as well as | the complexity |            | of  | deep learning | architectures. |            | To  |
| ------------- | --------- | -------- | ------ | -------- | ----------- | ------- | -------- | ---------- | -------------- | ---------- | --- | ------------- | -------------- | ---------- | --- |
| for learning  | in neural | networks |        | are not  | necessarily | adapted | for      |            |                |            |     |               |                |            |     |
|               |           |          |        |          |             |         |          | the best   | of our         | knowledge, | no  | research      | proposes       | to combine |     |
| user modeling | in        | EDM      | and do | not take | into        | account | a priori |            |                |            |     |               |                |            |     |
andaposterioriknowledge.Therefore,itisnecessarytorelyon a priori and a posteriori knowledge with neural architectures
|     |     |     |     |     |     |     |     | using the | attention | mechanism. |     | Moreover, | no  | research | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | --------- | --- | -------- | ------ |
hybridtechniquesabletotakethebestofbothdata-drivenand
educationaldomain,especiallyinusermodeling,hasaddressed
theory-drivenapproaches.
FrontiersinArtificialIntelligence|www.frontiersin.org 3 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
this issue despite the availability of knowledge. We show that thatthedecoderwantstogenerate.Thismechanismissimilarto
the combination of knowledge-based and data-based methods humanattention,whosegoalistofocusonaportionofcurrent
using the attention mechanism is an appropriate solution information that is deemed important for future decision-
for the design of hybrid deep neural networks with better making.Thecontextvectorisconstructedasfollows:forafixed
generalizationcapability. targetelement(whichrepresentsawordintheFigure1),afirst
|     |     |     |     |     |     |     | loop is made | on  | all the | outputs | of the hidden | layers | (states) | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------- | ------------- | ------ | -------- | --- |
2.2.1.APrioriandaPosterioriKnowledge theencoderstocomparethetargetandsourcestatestogenerate
Sometimesaprioriandaposterioriknowledgemaybeavailable,
scoresforeachstateintheencoders.Then,thefunctionsoftmax
but it is not always sufficiently precise or is in a form that is isusedtonormalizeallthescores,whichgeneratestheprobability
notalwayseasytoexploit.Nevertheless,evenimprecisemodels distribution conditioned on the target states. Finally, weights
can provide useful information that should not be discarded are introduced to facilitate the learning of the context vector.
(Zapponeetal.,2018). Mathematically,hereishowtheattentionvectoriscomputed:
Inphilosophy,aprioriknowledgeisdefinedasknowledgenot
gainedthroughexperienceincontrasttoaposterioriknowledge exp(score(h,h))
|     |     |     |     |     |     |     |     |     | α   |     | t s |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
( G r e e n be r g , 2 0 1 0 ) . I n a p r io r i a n d a p o st e ri o ri k n o w l e d g e , w e t,s =
|               |                         |       |                |         |            |                    |     |     |     | S exp(score(h |     | ,h s′)) |     |     |
| ------------- | ----------------------- | ----- | -------------- | ------- | ---------- | ------------------ | --- | --- | --- | ------------- | --- | ------- | --- | --- |
|               |                         |       |                |         |            |                    |     |     | P   | s′=1          | t   |         |     |     |
| i n c l u d e | k n o w l e d g e fr om | e x p | e rt s . Ex pe | r t k n | o w le d g | e r e p r e s en t | s   |     |     |               |     |         |     |     |
|               |                         |       |                |         |            |                    |     |     |     | α             |     |         |     | (1) |
theskillsdemonstratedbyexpertsinaparticulardomain.Inthe c t =X t,s ·h s
educational domain, both a priori and a posteriori knowledge s
|     |     |     |     |     |     |     |     |     | =tanh(W |     | ;h  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
aregenerallyavailable.Forexample,inTatoetal.(2017a),expert a t c [c t t ])
| knowledge | was used via | a Bayesian | network, |     | designed | entirely |     |     |     |     |     |     |     |     |
| --------- | ------------ | ---------- | -------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
by domain experts to predict learners’ logical reasoning skills. The variable h represents the output of the decoder at time t,
t
|                                                       |     |     |     |     |     |     | c isthecontextvectoranda |     |     | istheattentionvector.Here,the |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ----------------------------- | --- | --- | --- | --- |
| Thisknowledgeisavailableinmostcasesintheformofwritten |     |     |     |     |     |     | t                        |     |     | t                             |     |     |     |     |
materialsuchasbooks,experimentalresults,etc. score is denoted as a content-based function. It evaluates how
Our goal is to combine a priori and a posteriori knowledge welleachencodedinput(overlineh )matchesthecurrentoutput
s
with data-only techniques. We assume that the quality of the h ofthedecoder.Thescoresarenormalizedusingthefunction
t
(α
expert knowledge must be good in order for the proposed softmax t,s ). This score can be computed in different ways,
⊺·h
solution to be effective. We will have to make this knowledge amongothersbyusingtheproduct:score(h,h)=h (Luong
|     |     |     |     |     |     |     |     |     |     |     |     | t s | t s |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
interpretableandusablebyamachine.Awell-knownapproach etal.,2015).Finally,thevariablec isthecontextvector.
t
| is to build | a rule-based | system | (Fisher | et  | al., 1990; | Cordón |     |     |     |     |     |     |     |     |
| ----------- | ------------ | ------ | ------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
et al., 2001). For example, Van Melle (1978) used knowledge 3. METHODOLOGY
| from experts | to develop    | the     | MYCIN             | expert | system.   | However, |              |              |     |           |          |       |     |           |
| ------------ | ------------- | ------- | ----------------- | ------ | --------- | -------- | ------------ | ------------ | --- | --------- | -------- | ----- | --- | --------- |
| it can be    | difficult and | tedious | to operationalize |        | expertise | into     |              |              |     |           |          |       |     |           |
|              |               |         |                   |        |           |          | The internal | architecture |     | of neural | networks | makes | it  | difficult |
rules. This is a task that typically requires the intervention of toincorporatedomainknowledgeintothelearningprocess(Lu
cognitiveengineers.Also,theseexpertisesaremostlyburiedina et al., 1996). Our solution consists in forcing the model to pay
writtenrepresentation.Whatweproposeistousepre-designed attention to what the a priori and a posteriori knowledge think
models (e.g., rule-based systems, Bayesian networks, etc.) as is of the current input x. It thus aims to infuse the expert’s final
when available, or to use standard natural language processing prediction into the system, rather than how this knowledge is
and information retrieval techniques for knowledge extraction processedbytheexpert.Sincetheattentionmechanism(Xuetal.,
fromtext.
|     |     |     |     |     |     |     | 2015) is  | a memory | access       | mechanism | as      | presented | above, | it is   |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------------ | --------- | ------- | --------- | ------ | ------- |
|     |     |     |     |     |     |     | a perfect | fit in   | this context | where     | we want | the       | model  | to have |
2.2.2.AttentionMechanism access to existing knowledge during learning. In other words,
The attention mechanism allows a neural network to focus theneuralnetworkwill“consult”thisknowledgebeforemaking
in part on a subset of information. Attention-based recurrent the final decision. The importance that the neural model will
networks have been successfully applied to a wide variety of give to what this knowledge predicts as output is computed
tasks:machinetranslation(Bahdanauetal.,2014;LiuandChen, using attention weights (W and W , see Figure2). As the
|     |     |     |     |     |     |     |     |     |     | a   | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2022),handwritingsynthesis(Graves,2013;Bhuniaetal.,2021),
|     |     |     |     |     |     |     | network | learns, | it will know | how | much importance |     | it will | give |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | --------------- | --- | ------- | ---- |
speechrecognition(Chorowskietal.,2015).Attentionisaweight toeachofthepredictionscomingfromtheknowledgebasedon
vector that allows neural networks to “intelligently” select the the trials/errors it will have committed. W corresponds to the
a
| information | contained | in the | input | that is | deemed | important |         |             |     |            |         |         |         |     |
| ----------- | --------- | ------ | ----- | ------- | ------ | --------- | ------- | ----------- | --- | ---------- | ------- | ------- | ------- | --- |
|             |           |        |       |         |        |           | weights | calculating | the | importance | of each | feature | learned | by  |
fordecisionmaking.Theattentionmechanismlookslikeabasic the neural architecture (y) t compared to each feature extracted
auto-encoder(seeFigure11).
|     |     |     |     |     |     |     | from the | knowledge. | W   | represents | the weights |     | measuring | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---------- | ----------- | --- | --------- | --- |
c
The principle is to connect a context vector between the importanceofthepredictionsmadefromtheknowledge(viathe
| encoder | (in blue) and | the decoder | (in | red). | The context | vector |                 |     |         |         |              |       |                |     |
| ------- | ------------- | ----------- | --- | ----- | ----------- | ------ | --------------- | --- | ------- | ------- | ------------ | ----- | -------------- | --- |
|         |               |             |     |       |             |        | context vector) |     | and the | learned | features (y) | t for | the estimation |     |
takes as input the outputs of all input cells to compute the of the final prediction vector (see Figure2). Thus, the model
probability distribution of the source elements for each output will focus on what the expert says, including a priori and a
posterioriknowledge,beforemakingadecision.Bymergingthe
1shorturl.at/gpxK6 expertknowledgewiththeneuralarchitectureusingtheattention
FrontiersinArtificialIntelligence|www.frontiersin.org 4 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |
| -------------- | --- | --- | --- | --- | --- | ------------------------------------- | --- |
FIGURE1|Attentionmechanism.ExampleoftranslationfromEnglish(Iamastudent)toFrench(jesuisunétudiant).
| mechanism, | the model iteratively | processes     | the knowledge by   | asfollows: |     |     |     |
| ---------- | --------------------- | ------------- | ------------------ | ---------- | --- | --- | --- |
| selecting  | the relevant content  | at each step. | In the attentional |            |     |     |     |
mechanism presented by Luong et al. (2015), specifically the score(e k ,y t )=e k ·y t ·W a +b
globalattentionalmodel,theattentionalvectoriscalculatedfrom
|     |     |     |     |     |     | exp(score(e k ,y)) | t   |
| --- | --- | --- | --- | --- | --- | ------------------ | --- |
α =
thetargethiddenstateh t andtheinputhiddenstate.Insteadof t,k s exp(score(e ,y )) (3)
|           |                |                     |                  |     |     | P j=1 | j t |
| --------- | -------------- | ------------------- | ---------------- | --- | --- | ----- | --- |
| the input | hidden state h | as presented above, | we will have the |     |     |       |     |
s
|                                                      |     |     |     |     | c e | =X α ·e |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- |
| datafromtheexpertknowledgethatwillbeusedtocomputethe |     |     |     |     | t   | t,k     |     |
contextvectorC t whichwewillcalltheexpert-sidecontextvector k
(seeFigure2inLuongetal.,2015).Thus,giventhehiddenstatey
t
whichisthefinalpredictionoftheneuralmodel,andtheexpert- Where 1 ≤ k ≤ s, e is the prediction made from the a priori
sidecontextvectorce,weuseaconcatenationlayertocombine andaposterioriknowledge,y isthecurrentpredictionmadeby
t
t the neural architecture and s is the size of the predicted vector
theinformationfromthetwovectorstoproducetheattentional
hiddenstatea asfollows: (the number of classes to predict). The variable e represents a
t
|     |     |     |     | vector of length | equal to | the size of the vector | to be predicted |
| --- | --- | --- | --- | ---------------- | -------- | ---------------------- | --------------- |
whereeachentryrepresentstheprobabilitythattheentrybelongs
=tanh(W [ce;y])
a t c t t (2) to each of the classes according to the expert’s knowledge. The
|     |     |     |     | variablee k representsofsize1andW |     | a ,W c ,W,W,y,e,a | s s t t areof |
| --- | --- | --- | --- | --------------------------------- | --- | ----------------- | ------------- |
Theattentionalvectora togetherwiththepredictionmadefrom size s. The score as mentioned above is a content-based vector
t
the knowledge e and the hidden state y (the prediction) of the that computes the correlation (alignment score) between the
t
neural model are then sent to a dense layer to produce the expert knowledge and the latent features learned by the neural
y′.
expected result The expert-side context vector is computed architecture.Thisparameterdefineshowexpertknowledgeand
t
FrontiersinArtificialIntelligence|www.frontiersin.org 5 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
FIGURE2|Globalattentionalhybridmodel.
latent features learned from the data are aligned. The model Figure2presentstheattentionmechanismappliedtoapriori
assigns a score α to the pair of features at position t and the knowledge.Theoperatingprincipleissimpleandintuitive:
t,k
expert knowledge (e k ,y t ), based on their correspondence. The • In the first step, the input data x is processed by the expert,
set of α t,k are weights defining how much each feature of the i.e.,themembershipofxtooneoftheclassestobepredicted
datafromtheexpertshouldbeconsideredforeachoutput(final is evaluated from the a priori and a posteriori knowledge.
prediction).Figure2showsindetailthisglobalprocess. The same data x is also processed by the neural architecture
FrontiersinArtificialIntelligence|www.frontiersin.org 6 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
inparallel.IntheFigure2,wehavetakentheexampleofan includes a learning environment which uses various meta-
LSTMbutitcanbereplacedbyaCNNorasimpleDNN. structures to provide reasoning activities on various contents
• What we call “A priori knowledge” in the Figure2 can be (Nkambou et al., 2015). The expert model implements logical
replacedbyanyprocesssimulatingtheexpert’sfunctioningor reasoning skills and knowledge as well as related reasoning
anyprocesssimulatingaprioriandaposterioriknowledge.It mechanisms (syntactic and semantic rules of the given logical
canbearule-basedengineoraBayesiannetworkforexample. system).Themodelofbothvalidandinvalidreasoningrulesis
Theoutputoftheaprioriknowledgeisavectorrepresenting encoded as a set of production rules. In addition, the semantic
a probability distribution where each of the inputs is the memory of the target logic (the logic behind the reasoning) is
probability that the data x belongs to each of the classes to implemented through a formal OWL ontology and connected
predict. For example, if we want to predict that an image is to the inference rules. The first version of Logic-Muse focuses
either a cat or a dog, then the knowledge output is a vector on propositional logic. Logic-Muse learner model goal is to
of size two whose first value represents the probability that represent, update and predict the learner state of knowledge
the image belongs to the cat class and the second is the based on her/his interaction with the system. It has multiple
probability that the image belongs to the dog class. In our aspectsincludingthecognitivepartthatessentiallyrepresentsthe
proposed architecture, we have assumed that the size of the stateofthelearner’sknowledge(masteryofthereasoningskills
expert’soutputvectorisequaltotheoutputvectorofthefinal ineachofthesixreasoningsituationsthathavebeenidentified
prediction.However,itcanbeofdifferentsizes. thankstotheexperts).Thecognitivestateisgeneratedfromthe
• We have considered only the output of the last cell (y) of learnerbehaviorduringhisinteractionswiththesystem,thatis,
t
the LSTM, but one could also concatenate all hidden states itisinferredbythesystemfromtheinformationavailable.Itis
(h ,...,h)forthecalculationofthecontextvector. supported by a bayesian network (Tato et al., 2017a) based on
| 0   | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Once the expert vector (e) and y are estimated, the domainknowledge,whereinfluencerelationshipsbetweennodes
t
ce).
architecture determines the expert context vector (called (reasoning skills) as well as prior probabilities are provided by
This vector represents the relevant information (features) theexperts.Somenodesaredirectlyconnectedtothereasoning
extractedfromthecombinationoftheexpertknowledgeand activities (items). The skills involved in the BN are those put
the information extracted by the neural architecture. It is forwardbythementalmodelstheorytoreasoninconformityto
computedaccordingtotheformulapresentedabove. thelogicalrules.Theseskillsincludetheinhibitionofexceptions
• Once the expert context vector is estimated, the attention to the premises, the generation of counterexamples to the
vector (a) is computed from the concatenation of the expert conclusionandtheabilitytomanagealltherelevantmodelsfor
contextvectorandy t (seecomputationformulaabove). familiar,contrarytofact(counterfactual)andabstractsituations
• Fortheestimationofthefinalpredictionvectory′,thereare (Markovits, 2013). There are 16 skills directly observable that
t
severalpossiblesolutions.Thefirstone(whichispresentedin are linked to the exercises (see Table1) and 12 latent skills. 48
theFigure2)wouldbetoconcatenatetheexpertvector(e),the exercisesonlogicalreasoningwereusedinthisstudy.
datalearnedbytheneuralarchitecture(y),andtheattention t For this first system, the goal is to train and test the DKT
vectora andthenpassthevectorobtainedintoanactivation model enhanced with our attentional expert knowledge for
t
function to compute the final vector. Other solutions would knowledge tracing. DKT is a LSTM which take sequences of
consist in, not including one or both vectors e and y t in the exercise-performance(e,p)pairspresentedonetrialatatime. t t
concatenation. Themodelthenpredicttheknowledgestate,basedonthecurrent
|     |     |     |     |     | hidden | state. | The hidden | layer | of  | the LSTM |     | represents the |
| --- | --- | --- | --- | --- | ------ | ------ | ---------- | ----- | --- | -------- | --- | -------------- |
WehavepresentedourapproachusinganLSTMasanexample,
|              |                |                          |           |          | latent encoding |           | of knowledge |          | state,       | based    | on the | current input |
| ------------ | -------------- | ------------------------ | --------- | -------- | --------------- | --------- | ------------ | -------- | ------------ | -------- | ------ | ------------- |
| but in the   | case of a CNN, | the y t would            | represent | the      | final           |           |              |          |              |          |        |               |
|              |                |                          |           |          | and previous    | latent    | encoding     |          | of knowledge |          | state. | It represents |
| output of    | the network    | that has been flattened. | The       | proposed |                 |           |              |          |              |          |        |               |
|              |                |                          |           |          | the latent      | knowledge |              | state of | student      | resulted |        | from his past |
| hybrid model | will allow     | taking into account      | the a     | priori   | and a           |           |              |          |              |          |        |               |
learningtrajectory.
posterioriknowledgeoftheexpertsforthemodelingoftheusers.
| One of the | uses of such | a model is knowledge | tracing |     | or skill |     |     |     |     |     |     |     |
| ---------- | ------------ | -------------------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
4.1.1.BayesianNetworkasAttentioninDKT
prediction,whichwewillpresentinthenextsectionsdedicated
|     |     |     |     |     | Bayesian | Network | (BN) | is a | graphical | model | used | to model |
| --- | --- | --- | --- | --- | -------- | ------- | ---- | ---- | --------- | ----- | ---- | -------- |
totheapplicationofoursolutioninrealcases.
|     |     |     |     |     | processes | under | uncertainty |     | by representing |     | the | relationship |
| --- | --- | --- | --- | --- | --------- | ----- | ----------- | --- | --------------- | --- | --- | ------------ |
betweenvariablesintermsofaprobabilitydistribution(Russell
|     |     |     |     |     | and Norvig, | 2016). |     | BN allows | inferring |     | the | probability of |
| --- | --- | --- | --- | --- | ----------- | ------ | --- | --------- | --------- | --- | --- | -------------- |
4. EXPERIMENTS
|     |     |     |     |     | mastering      | a skill | from      | a specific | response |           | pattern | (Nkambou       |
| --- | --- | --- | --- | --- | -------------- | ------- | --------- | ---------- | -------- | --------- | ------- | -------------- |
|     |     |     |     |     | et al., 2010). | The     | structure |            | and the  | parameter |         | or probability |
Ourgoalistocreateanaccurateusermodeloragoodmodelfor
distributionsareprovidedbyexpertsorlearnedusingalgorithms
| the prediction | of skills, | in order to improve | personalization |     | in  |     |     |     |     |     |     |     |
| -------------- | ---------- | ------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
suchasExpectation-Maximization.Ithasbeensuccessfullyused
adaptivelearningsystems.
|     |     |     |     |     | to model     | knowledge |         | state of | learners | (Martin    |     | and VanLehn,   |
| --- | --- | --- | --- | --- | ------------ | --------- | ------- | -------- | -------- | ---------- | --- | -------------- |
|     |     |     |     |     | 1995; Nguyen |           | and Do, | 2009;    | Tato et  | al., 2016) | or  | learner affect |
4.1. Logic-Muse (Sabourin et al., 2011). There are many contexts where a lot of
Logic-Muse is a web-based Intelligent Tutoring System (ITS) data or expert knowledge (e.g., medicine, Flores et al., 2011) is
thathelpslearnersimprovelogicalreasoningskills.Logic-Muse available to build BN. How the DKT can benefit from that? In
FrontiersinArtificialIntelligence|www.frontiersin.org 7 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
TABLE1|Distributionofresponsesoverskills.
| Skills | Skilldescription |     |     |     | N   |     | Average | Standarddev |     |
| ------ | ---------------- | --- | --- | --- | --- | --- | ------- | ----------- | --- |
MppFd Modusponendoponenswithfewdisablingconditions 294 0.9456 0.16078
MppMd Modusponendoponenswithmanydisablingconditions 294 0.898 0.23726
MppCcf Modusponendoponensatthecounterfactuallevel 294 0.907 0.2394
| MppA | Modusponendoponensattheabstractlevel |     |     |     | 294 |     | 0.9615 |     | 0.16066 |
| ---- | ------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | ------- |
MttFd Modustollendotollenswithfewdisablingconditions 294 0.8435 0.26646
MttMd Modustollendotollenswithmanydisablingconditions 294 0.7925 0.29985
MttCcf Modustollendotollensatthecounterfactuallevel 294 0.7494 0.33326
MttA Modustollendotollensattheabstractlevel 294 0.8401 0.28974
AcMa Affirmationoftheconsequentwithmanyalternatives 294 0.424 0.38072
AcFa Affirmationoftheconsequentwithfewalternatives 294 0.3039 0.3652
AcCcf Affirmationoftheconsequentatthecounterfactuallevel 294 0.3345 0.40801
AcA Affirmationoftheconsequentattheabstractlevel 294 0.2823 0.41038
DaMa Denialoftheantecedentwithmanyalternatives 294 0.407 0.37389
DaFa Denialoftheantecedentwithfewalternatives 294 0.3027 0.35081
DaCcf Denialoftheantecedentatthecounterfactuallevel 294 0.381 0.40662
DaA Denialoftheantecedentattheabstractlevel 294 0.305 0.42077
Skillsdifficulttomaster(Average<0.4)andskillseasytomaster(Average>0.9)areinbold.
| contextswhereexpertknowledgeisavailable,wewantedtotake |     |     |     | 4.1.3.Results |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
advantageofthat.Wealsoarticulatethat,asexpertknowledgeis Toassessourproposedsolution,weran2models:theDKTand
not biased toward rare data, the model could benefit from that theDKTwithaprioriknowledge(DKT+BN).Weused20%of
whenmakingpredictions. the data for testing and 15% for validation. The BN alone gave
In Logic-Muse BN, there are 16 nodes directly observable 69%ofglobalaccuracy.TheresultisevaluatedusingtheF1score
(representing skills linked to exercises) and 12 latent nodes oneachskill(treatedas2classes—correctandincorrectanswers)
representing knowledge that are a combination of observable being predicted and the overall accuracy. The models were
skills.Ateachtimet,theBNpredictstheprobabilityofmastering evaluatedin20differentexperiments(thesameexperimentwas
eachofthe16skillsforthecurrentstudentbasedonitsresponses repeated20times,thisistoensurethatthereisnorandomness
to past exercises. The output of the prediction represents a inthepresentedresults)andthefinalresultswereaveraged.Inall
|     |     |     |     | ourexperiments,wesetλ |     |     | andλ |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | ---- | --- | --- |
vector of 16 entries which is the vector e (expert knowledge in 1 2 =0.10.Ourimplementation
Figure2) in the attentional hybrid model. By integrating the oftheDKT+BNmodelinTensorflowusingKerasbackendwas
expert knowledge (here a BN) in the DKT using the attention, inspiredbytheimplementation2donebyKhajahetal.(2016)Our
codeisalsoavailableonGitHub3forfurtherresearch.
themodeliterativelyprocessestheaprioriknowledgebyselecting
relevantcontentateverystep. The results are shown in Tables2, 3 and in Figure3. As
expected,thenewDKTenhancedwithBNoutperformsthestate-
|     |     |     |     | of-the-art | model | for predicting | skills with | few data. For | skills |
| --- | --- | --- | --- | ---------- | ----- | -------------- | ----------- | ------------- | ------ |
4.1.2.Dataset that are easy to master (e.g., MPP type skills), all the models
Thereisatotalof294participantswhoparticipatedinthisfirst alwayspredictthatstudentswillgivecorrectanswers(theF1score
|             |               |                |                      | of incorrect | answers | is 0 | for DKT and almost | 0 for the | other |
| ----------- | ------------- | -------------- | -------------------- | ------------ | ------- | ---- | ------------------ | --------- | ----- |
| study. They | all completed | the 48 logical | reasoning exercises. | In           |         |      |                    |           |       |
ourdataset,eachlineofdatarepresentseachparticipant(atotal model). This is because, on the 294 data, we have for example
of 294 data and a sequence length of 48). The exercises were only 6 incorrect answers for the MPP_FFD skill. We tested the
|     |     |     |     | modelswithhighvaluesforλ |     |     | andwegetvaluesoff1scoreequal |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | ---------------------------- | --- | --- |
encoded using skills that are directly observable, which means 2
thatthequestionsrelatedtothesameskillareencodedwiththe to around 0.6 for correct answers and around 0.7 for incorrect
same Id (1–16). The skills with few data are determined by a answers. This result may be satisfactory in other contexts but
|     |     |     |     | in the | context of | logical reasoning | where | it is established | that |
| --- | --- | --- | --- | ------ | ---------- | ----------------- | ----- | ----------------- | ---- |
comparisonoftheaverageofcorrectanswersobtainedforeach
|                   |             |                 |                | the MPP | type skills | are always | well-mastered, | 0.6 as an | f1score |
| ----------------- | ----------- | --------------- | -------------- | ------- | ----------- | ---------- | -------------- | --------- | ------- |
| skill. In Table1, | we averaged | all the answers | on each skill. | The     |             |            |                |           |         |
skillsdifficultto masterarethosewith thelowestaveragevalue forcorrectlypredictingacorrectanswerisnotacceptable.That
andtheskillseasytomasterarethosewiththehighestaverage. is why we kept λ =0.10. However, the solution stays valid for
2
|     |     |     |     | datawheretheratior |     | =numberofcorrectanswers/numberof |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | -------------------------------- | --- | --- | --- |
SincetheLSTMonlyacceptsafixedlengthofvectorsastheinput,
weusedone-hotencodingtoconvertstudentperformanceintoa
fixedlengthofvectorswhoseallelementsare0exceptforasingle
2https://github.com/mmkhajah/dkt
1.Thesingle1inthevectorindicatestwothings:whichskillwas 3https://github.com/angetato/Deep-Knowledge-Tracing-On-Skills-With-
| answeredandiftheskillwasansweredcorrectly. |     |     |     | Limited-Data |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
FrontiersinArtificialIntelligence|www.frontiersin.org 8 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |               |     |     | HybridNeuralNetworkforPersonalization |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
|                |     |     |     |     |     | 4.2. MorALERT |     |     |                                       |     |     |     |     |
TABLE2|TheDKTandtheDKT+BNonskillsthataredifficulttomaster.
4.2.1.Context
| F1score | AcMa | DaMa | AcFa |     | DaFa |             |           |       |     |                   |     |           |     |
| ------- | ---- | ---- | ---- | --- | ---- | ----------- | --------- | ----- | --- | ----------------- | --- | --------- | --- |
|         |      |      |      |     |      | Socio-Moral | Reasoning | (SMR) | is  | a socio-cognitive |     | construct |     |
DKT 0.74 0.09 0.72 0.0 0.79 0.0 0.79 0.0 essential for decision-making, as well as social interaction
|        |           |           |      |           |      | adaptation. | It is commonly |     | defined     | as “how | individuals |        | think  |
| ------ | --------- | --------- | ---- | --------- | ---- | ----------- | -------------- | --- | ----------- | ------- | ----------- | ------ | ------ |
| DKT+BN | 0.70 0.64 | 0.78 0.43 | 0.86 | 0.74 0.80 | 0.47 |             |                |     |             |         |             |        |        |
|        |           |           |      |           |      | about moral | emotions       | and | conventions |         | that        | govern | social |
F1score AcCcf DaCcf AcA DaA Accuracy interactions in their everyday lives” (Beauchamp et al., 2013).
|        |                |           |           |      |      | Being able         | to predict   | and diagnose |          | one’s socio-moral |             | reasoning |          |
| ------ | -------------- | --------- | --------- | ---- | ---- | ------------------ | ------------ | ------------ | -------- | ----------------- | ----------- | --------- | -------- |
| DKT    | 0.79 0.0 0.73  | 0.0 0.80  | 0.0 0.79  | 0.0  | 0.74 |                    |              |              |          |                   |             |           |          |
|        |                |           |           |      |      | skill level        | (or ability) | is a         | key step | for               | quantifying |           | peoples’ |
| DKT+BN | 0.87 0.80 0.82 | 0.72 0.83 | 0.58 0.88 | 0.80 | 0.82 |                    |              |              |          |                   |             |           |          |
|        |                |           |           |      |      | social functioning | and          | can be       | used     | to identify       | those       | at        | risk for |
Werepeatedtheexperiments20times.Thelastcolumnistheoverallaccuracyofthe
|     |     |     |     |     |     | maladaptive | social | behavior. | This | diagnosis | could | help | orient |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | ---- | --------- | ----- | ---- | ------ |
model.Foreachskill,thefirstcolumncorrespondstothevalueofthef1scoreforpredicting
peopletowardappropriateservicesorprovideadequatesupport
thattheskillwasincorrectlyansweredandthesecondcolumntothevalueofthef1score
toimprovethisskill’sdevelopment.TheSocio-MoralReasoning
forpredictingthattheskillwascorrectlyanswered.Thebestratioforeachskillisinbold.
AptitudeLevel(SoMoral)(Dooleyetal.,2010)taskisacomputer-
|     |     |     |     |     |     | measured  | walkthrough | in which | children |      | and adolescents |       | are  |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | -------- | ---- | --------------- | ----- | ---- |
|     |     |     |     |     |     | presented | with visual | social   | dilemmas | from | everyday        | life. | They |
TABLE3|TheDKTandtheDKT+BNonSkillsthatareeasytomaster. arethenaskedtoverbalizehowtheywouldreactinthissituation,
F1score MppFd MppMd MttFd MttMd justifying their answer. The participants’ answers are recorded
|     |     |     |     |     |     | verbatim | in transcripts | that | are subsequently |     | scored | manually |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | ---- | ---------------- | --- | ------ | -------- | --- |
DKT 0.0 0.97 0.0 0.94 0.0 0.91 0.0 0.90 by experts using a moral-maturity coding scheme inspired by
DKT+BN 0.0 0.95 0.0 0.97 0.0 0.89 0.19 0.88 the Kohlberg’s theory of moral development (Kohlberg, 1984).
Verbatimsareshortorlongtextcontainingatleastonesentence.
F1score MppCcf MttCcf MppA MttA Each socio-moral reasoning rating was well-documented by
expertsusingannotateddata.Thegoalwastoputtogetherthese
| DKT | 0.0 0.96 | 0.0 0.87 | 0.0 | 0.96 0.0 | 0.90 |     |     |     |     |     |     |     |     |
| --- | -------- | -------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
twokindsofdatatobuildanaccuratemodelfortheautomatic
| DKT+BN | 0.0 0.97 | 0.12 0.85 | 0.0 | 0.99 0.1 | 0.89 |            |              |       |         |       |           |      |      |
| ------ | -------- | --------- | --- | -------- | ---- | ---------- | ------------ | ----- | ------- | ----- | --------- | ---- | ---- |
|        |          |           |     |          |      | prediction | of reasoning | skill | levels. | Using | annotated | data | only |
Werepeatedtheexperiments20times. would not give us good results in this context. Therefore we
|     |     |     |     |     |     | propose | a hybrid model | that | combines | expert | knowledge |     | with |
| --- | --- | --- | --- | --- | --- | ------- | -------------- | ---- | -------- | ------ | --------- | --- | ---- |
DNN(DeepNeuralNetworks)architectures(especiallyCNNand
|     |     |     |     |     |     | LSTM) | using the attentional |     | mechanism |     | (Xu et | al., 2015) | for |
| --- | --- | --- | --- | --- | --- | ----- | --------------------- | --- | --------- | --- | ------ | ---------- | --- |
questionsansweredorr=numberofincorrectanswers/number predicting the level of SMR skill of an individual based on his
ofquestionsansweredonaskillisnottoosmall(asinthiscase) justificationswhensolvingsocio-moraldilemmas.Thedeveloped
andislessthan0.5.Forskillsthataredifficulttomaster,thereisa solutionextendsthelearner/playermodelinaseriousgamecalled
hugedifferencebetweentheDKTandourproposedmodel.DKT LesDilemmes(Tatoetal.,2017b).
isunabletotrackcorrectanswersonskillsdifficulttomaster.This
4.2.2.MorALERT:ASeriousGameforImproving
behaviorcannotbeacceptedastheknowledgetracingofstudents
thatperformwellonthoseskillswillfail.Thusitisimportantto Socio-MoralReasoningSkills
make sure that the final model is accurate for all the skills. On The proposed hybrid model has been tested for the automated
skills with few samples, we can notice that the DKT + BN still scoring mechanism in a serious video game called MorALERT
behavesbetterthanDKT. (previouslycalledLesDilemmes)(Tatoetal.,2017b).MorALERT
During our experiments, we noticed that predictions are is a first-person serious game aiming to assess and train
not sometimes consistent with reality as other works have the player on social reasoning skills. MorALERT is a virtual
also highlighted (Yeung and Yeung, 2018). The model fails to learning environment offering an emotionally, socially, and
reconstructtheobservedinput.Asaresult,evenwhenastudent cognitivelyrichinteractivecontext.Playersfacedifferentsocio-
performswellonaskill,thepredictionofthatskill’smasterylevel moral dilemmas within a 3D environment (see Figure4) in
decreasesinstead,andviceversa.Also,thepredictedperformance whichtheyhavetomakedecisionsandareaskedtoprovideoral
across time steps is not consistent. As seen in Figure3—DKT, justifications for their choices. They can also ask the opinions
whenastudentgivescorrectanswerstoaskillk,theDKTdoes of virtual friends (Non-Player Characters) in the game. At the
not sometimes update the current state of knowledge on that beginning of the game, each Non-Player Character (NPC) is
skill(theskillstaysloworisupdatedveryslowly).Theproblem assigned an SMR maturity level. The NPCs’ opinions are then
can be addressed by adding regularization terms to the loss selected from previously recorded transcripts corresponding to
functionoftheoriginalDKTassuggestedbyYeungandYeung the different moral maturity levels according to the coding
(2018). It can also be partially solved when adding the apriori scheme(SoMoral,Beauchampetal.,2013).Thelearner(player)
knowledge as we noticed during our experiments (Figure3— modelimplementedinthelearningenvironmentincludesthree
DKT+BN). However, we stay confident in the fact that if the keydimensions:theaffectivestate,thecognitiveprofile,and,the
aprioriknowledgeismoreaccurate(whichisnotourcaseasthe socio-moralreasoningprofile.Therefore,socio-moralreasoning
accuracyoftheBNis0.65)wewillgetbetterresults. skill is part of the player model implemented in the game. As
FrontiersinArtificialIntelligence|www.frontiersin.org 9 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
FIGURE3|Heatmapsillustratingthepredictionwiththe2modelsonthesamestudent.DKTisunabletomakeaccuratepredictionsonskillswithlittledata,
especiallyskillsthataredifficulttomaster.Thelabelintheverticaldimensionreferstotheinputfedintothemodelsateachtimestep.Thecoloroftheheatmap
indicatesthepredictedprobabilitythatthestudentwillcorrectlyansweraquestionrelatedtoaskillinthenexttimestep.Thedarkerthecolor,thehigherthe
probability.Here,thestudentgave2outof3correctanswersonAC_FMAandweseethattheDKT+BNisabletotrackdownthatinformationcomparedtotheDKT.
FrontiersinArtificialIntelligence|www.frontiersin.org 10 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
FIGURE4|MorALERTseriousgame.
stated in Birk et al. (2015), a learner/player model that can modelwasnotabletopredictwhenapersonhasasocio-moral
accurately represent the learner longitudinally in a game leads reasoninglevelof2,3,or5.Allthepredictionswereeitherlevel
toefficientadaptation,whichinturnhelpsincreasetheplayer’s 1or3duetoanunbalanceddataset.Ournewmodeladdresses
satisfactionandmotivation.Tothisend,itisimportanttoensure thisissueinordertoensuretheaccuracyofthelearnermodelfor
the effectiveness of the learner/player model before deploying bettersupportofthelearningprocessintheseriousgame.
the system for real uses. One goal in MorALERT was to build
aneffectivemodelofthesocio-moralfacetofthelearner/player. 4.2.4.HybridArchitectureforSocio-MoralReasoning
Defininganindividual’ssocio-moralreasoninglevelnecessitates SkillPrediction
an examination of the verbal justifications he provided when 4.2.4.1.ExpertKnowledge
solving the dilemmas. This involves the implementation of a In our context, where we only have access to description (in
modelthatautomaticallymeasuresandpredictsthisdataduring textual form) of each of the levels (see Figure5, Chiasson
the game. We possessed a dataset of verbatim coming from etal.,2017),weemployedtwodifferenttechniquesrelatedtoIR
theSoMoral experimentationalreadyannotatedbyexpertsand (InformationRetrieval)andNLP(NaturalLanguageProcessing):
a description (a paragraph with key concepts) associated with the Word Movers’ Distance to compare the meaning of texts,
eachdifferentlevel(orclass)ofmaturity.Theexperimentinthis n-grams,andstemmingtotestwhetherverbatimcontainthose
second context aims to implement our solution so that we can specificelementsextractedforeachlevel.Weexplaineachofthe
accuratelyassessthesocio-moralreasoningskilllevelofaplayer techniquesinfurtherdetailsinthefollowingsection.
basedonhisverbatim.
4.2.4.2.WordMover’sDistance
4.2.3.Socio-MoralReasoningSkillLevels Word Mover’s Distance (WMD) (Kusner et al., 2015) is a
TheoriginalSoMoraltaskincludesfivedifferentlevelsofsocio- machinelearningtechniquethatallowssubmittingaqueryand
moralreasoningskill(Beauchampetal.,2013):(1)Authoritarian- returning the most relevant documents. It is used to assess
basedconsequences,(2)Egocentricexchanges,(3)Interpersonal the “distance” between two documents in a meaningful way,
Focus, (4) Societal Regulation, and (5) Societal Evaluation. even when they have no words in common. The assumption is
Transition levels (i.e., 1.5, 2.5, 3.5, 4.5) are used to account for that similar words should be linked to similar vectors. Instead
verbatimthatprovideselementsoftwodifferentreasoningstages of using Euclidean Distance and other bag-of-words based
and show a sequential progression from one stage to another. distance measurement, they proposed to use word2vec vector
Occasionally,averbatimisassignedtotwodifferentclosedlevels embeddingsofwordstocalculatesimilarities.Ithasbeenshown
(withamaximumdeviationof1)whentwoindependentexperts tooutperformmanyofthestate-of-the-artmethodsink-nearest
annotatethedataforinter-reliabilitypurposes. neighborsclassificationbynormalizingBag-of-WordsandWord
A first convolutional neural network has been proposed, to Embeddingstocalculatethedistancebetweendocuments.
automatically detect the player’s socio-moral reasoning level. WeusedtheWMDmethodtobuildthefirstpartoftheexpert
Despitethehighaccuracyreported(92%)(Tatoetal.,2017b),the knowledge content that will be combined with the DNN. Each
FrontiersinArtificialIntelligence|www.frontiersin.org 11 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
FIGURE5|BriefdescriptionofSoMoralcodingandexamples(Chiassonetal.,2017).
description of each socio-moral reasoning skill level as well as the text. The sum of the vectors generated by this process and
eachverbatimisconsideredasadocument.Wetransformedeach thepreviousone(n-grams)gaveus,foreachverbatim,avector
document to their word2vec representation using pre-trained ofsize5whereeachentryrepresentsthenumberofn-gramsand
word2vec models for French.4,5 The vectors have then been synonymsofeachlevelfoundintheverbatim.Wefinallyapplied
normalizedsothattheycouldallhaveequallength.Wecalculated thesoftmaxfunctiontotheresultingvectorwhichwasaddedto
the similarity between each verbatim and each description (5 theonegeneratedbytheWMDmethod.
| descriptions) | using gensim | Wmd-Similarity | tool.6 For each |     |     |     |     |     |     |     |
| ------------- | ------------ | -------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
4.2.5.Experiments
| verbatim | this calculation | provided us with | a vector of length |     |     |     |     |     |     |     |
| -------- | ---------------- | ---------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
5 where each entry is the similarity between the verbatim and In order to empirically evaluate the proposed solution in
thedescriptionofthecorrespondingsocio-moralreasoningskill this second context, we investigated six different models: a
level.Thevaluesrangebetween0and1. CNN (cnn-only), an LSTM (lstm-only), a CNN where expert
|     |     |     |     | knowledge | was | concatenated | to the | features | learned | (cnn- |
| --- | --- | --- | --- | --------- | --- | ------------ | ------ | -------- | ------- | ----- |
expert),anLSTMwhereexpertknowledgewasconcatenatedto
4.2.4.3.Bi-gramandStemming
|     |     |     |     | the features | learned | (lstm-expert) | and | finally | the cnn-expert- |     |
| --- | --- | --- | --- | ------------ | ------- | ------------- | --- | ------- | --------------- | --- |
N-gramisacontiguoussequenceofnitemsfromagivensample
|     |     |     |     | att (a CNN | where | expert | knowledge | was concatenated |     | to the |
| --- | --- | --- | --- | ---------- | ----- | ------ | --------- | ---------------- | --- | ------ |
oftextorspeech.Weextractedn-grams(uniandbigrams)from
featureslearned+knowledge-basedattention)andlstm-expert-
thetextualdescriptionoflevels,whichgaveusalistofn-gramfor
|     |     |     |     | att (a LSTM | where | expert | knowledge | was concatenated |     | to the |
| --- | --- | --- | --- | ----------- | ----- | ------ | --------- | ---------------- | --- | ------ |
eachreasoninglevel.Wealsogeneratedalistofsynonymsofall
featureslearned+knowledge-basedattention).Weusedthesame
keywords(extractedmanually)includedinthedescriptions.For
eachverbatim,wecountedthenumberoftimeseachn-gramof parameter initialization for all the models. Adam (Kingma and
|     |     |     |     | Ba, 2014) | was used | as the | optimizer | with a learning |     | rate set to |
| --- | --- | --- | --- | --------- | -------- | ------ | --------- | --------------- | --- | ----------- |
eachlevelappearedwithinthetext.
|     |     |     |     | 0.001. The | algorithms | were | implemented | using | Keras7 | and the |
| --- | --- | --- | --- | ---------- | ---------- | ---- | ----------- | ----- | ------ | ------- |
Stemmingistheprocessofreducinginflected(orsometimes
experimentsweredoneusingthebuilt-inKerasmodels,making
derived)wordstotheirwordstem,baseorrootform.Weapplied
onlysmalleditstothedefaultsettings.
thistechniquetoallthewordsinthesynonymslistgeneratedand
foreachwordinverbatim.Also,foreachverbatim,wecounted
4.2.5.1.DataPre-processing
thenumberoftimeseachsynonymofeachlevelappearedwithin
|     |     |     |     | The dataset | consists | of a benchmark |             | of 731 | verbatim  | (written |
| --- | --- | --- | --- | ----------- | -------- | -------------- | ----------- | ------ | --------- | -------- |
|     |     |     |     | in French)  | manually | annotated      | by experts. |        | Verbatims | are not  |
4http://fauconnier.github.io/
|     |     |     |     | equally distributed |     | between | classes (unbalancing |     | data). | Table4 |
| --- | --- | --- | --- | ------------------- | --- | ------- | -------------------- | --- | ------ | ------ |
5http://wacky.sslmit.unibo.it/doku.php?id=corpora
6https://tedboy.github.io/nlps/generated/generated/gensim.similarities.
| WmdSimilarity.html |     |     |     | 7https://keras.io/ |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
FrontiersinArtificialIntelligence|www.frontiersin.org 12 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
TABLE4|Distributionofverbatimsbetweenclasses.
| Class     | Frequency    |     |            | Class |         | Frequency   |     |     |     |     |     |
| --------- | ------------ | --- | ---------- | ----- | ------- | ----------- | --- | --- | --- | --- | --- |
| 1         |              | 232 |            | 1.5   |         | 11          |     |     |     |     |     |
| 2         |              | 76  |            | 2.5   |         | 29          |     |     |     |     |     |
| 3         |              | 207 |            | 3.5   |         | 31          |     |     |     |     |     |
| 4         |              | 40  |            | 4.5   |         | 3           |     |     |     |     |     |
| 5         |              | 49  |            |       |         |             |     |     |     |     |     |
| shows the | distribution | of  | data where | for   | example | the classes | 4   |     |     |     |     |
and5haveasmallnumberofverbatimsthanothers(1,2and3).
Infact,level5beingthehighestlevelofmaturity,itisraretocome
FIGURE6|Finalmodelforpredictingsocio-moralreasoningskilllevels.
acrosspeopleofthislevel.Thismeansthatsomeofthoseclasses
| have very  | few examples | to   | learn | from.      | On the 731 | verbatims,  |     |     |     |     |     |
| ---------- | ------------ | ---- | ----- | ---------- | ---------- | ----------- | --- | --- | --- | --- | --- |
| there were | 53 of them   | that | were  | classified | as 0,      | which means |     |     |     |     |     |
that the verbatim does not represent one of the socio-moral predictionoflevelsspecifiedbetweenparenthesis.Eachmodelis
reasoningskilllevels.Wedonotconsiderthesecasesinourstudy, eitherLSTMorCNNcombinedwithexpertknowledgeandthe
whichreducesourcorpusto678verbatims.Wealsolimitedour
attentionalvector.
predictionproblemto5levelsofsocio-moralreasoningskills:1,
2,3,4,and5.Theverbatimsbelongingtointermediarylevels1.5, 4.2.5.3.ProposedModels
2.5,3.5,and4.5wereaddedtoverbatimsbelongingtolevels2,3, Figure7 shows the proposed architectures. The models take as
4,and5,respectively. inputtheverbatimsthathavebeenpre-processed(tokenization,
texttosequence,etc.)andvectored.Thevectorsarethenpassed
4.2.5.2.DealWithUnbalancedData totheembeddinglayer.InFigure7(left),theembeddingvectors
AsshowninTable4,thedatasetisunbalanced.Thefirstmodels arepassedtotheLSTMlayer(notethatwehaveonlyconsidered
| we built | were biased | toward | classes | that | had more | samples. |            |                    |            |           |         |
| -------- | ----------- | ------ | ------- | ---- | -------- | -------- | ---------- | ------------------ | ---------- | --------- | ------- |
|          |             |        |         |      |          |          | the output | of the last cell). | The expert | knowledge | and the |
Therefore,weappliedsometechniquesthataimedtobalancethe output of the LSTM are then passed to the expert knowledge-
dataset. The first technique we had chosen is the penalization basedattention.Theattentionalvectorismergedwiththeexpert
| of models | (cost-sensitive |     | models, | Shi et | al., 2015). | It works as |           |                |              |                   |     |
| --------- | --------------- | --- | ------- | ------ | ----------- | ----------- | --------- | -------------- | ------------ | ----------------- | --- |
|           |                 |     |         |        |             |             | knowledge | and the output | of the LSTM. | The concatenation | is  |
follows:wepenalizetheclassificationbyimposinganadditional passedtothelastlayerfortheprediction.Thisprocessisthesame
cost on the models for making classification mistakes on the for the CNN (see Figure7, right), except that the knowledge-
minorityclassduringtraining.Thepenaltiescanbiasthemodel basedattentionlayertakesasinputtheexpertknowledgeandthe
| to pay more | attention | to  | the minority |     | classes. | However, this |     |     |     |     |     |
| ----------- | --------- | --- | ------------ | --- | -------- | ------------- | --- | --- | --- | --- | --- |
resultofthepoolingoperationappliedtotheoutputoftheCNN.
technique was unsuccessful because the results were no better To evaluate the added value of this knowledge-based attention,
than when using the original dataset. In fact, the generated wehaveconsideredtwosimilarmodels(cnn-expert,lstm-expert)
| solutions | were able | to classify |     | instances | from | the minority |     |     |     |     |     |
| --------- | --------- | ----------- | --- | --------- | ---- | ------------ | --- | --- | --- | --- | --- |
tothoseshowninfigures.However,thosemodelsdonothavethe
classes correctly, but less capable of classifying instance from knowledge-basedattentionlayer.Theyareusedasacomparison
themajorityclasses.Thesecondtechniqueweusedaimedatre- withtheproposedsolutions.
| sampling                                            | the dataset | (Ghosh | et al., | 2017). | With this | technique, |                 |     |     |     |     |
| --------------------------------------------------- | ----------- | ------ | ------- | ------ | --------- | ---------- | --------------- | --- | --- | --- | --- |
| themodelswereinsuredtonotbebiasedtowardoneclass.The |             |        |         |        |           |            | 4.2.5.4.Results |     |     |     |     |
dataset was re-sampled by using the oversampling technique, All the models have been trained on 80% (with 20% as
whichconsistsinrandomlyduplicatingsamplesfromclasseswith validationdata)ofthedataandtestedontheremaining20%.A
fewexamples,inordertomatchthenumberofsamplesofother standardmeasureforclassification/predictionperformanceisthe
classes. This second technique did not work as well. Instead of accuracy.However,fordatasetswithunbalanceddistributionlike
playing with the data, we found a solution based on training ours,thismeasurecanbeillusoryandnotveryinformativeonthe
multiplemodelsthatarespecializedinthepredictionofspecific errorsbeingcommittedbytheclassifier.Insteadofconsidering
socio-moral levels. We used ensemble methods to combine only the accuracy, we have considered the recall, the precision
results from those models and produce the final prediction. and the F1 score (or F-measure which takes in consideration
Ensemblemethods(Dietterich,2000)aretechniquesthatcreate both the precision and the recall) for all classes and for each
multiple models and then combine them to produce improved of the classes separately. Thus, we will be able to evaluate the
results. Voting and averaging are two of the easiest ensemble performance of the models on the prediction of classes with
| methods. | They are | both | easy to | understand | and | implement. | smallsamples. |     |     |     |     |
| -------- | -------- | ---- | ------- | ---------- | --- | ---------- | ------------- | --- | --- | --- | --- |
Votingstrategywasselected,asitiswell-suitedforclassification TheresultsareshowninTable5andinFigures8,9.Aswecan
problems. The architecture of the final model is presented in see,modelsthattakeintoaccountexpertknowledgeperformwell
Figure6. In Figure6, each sub model is specialized for the forthepredictionofclasseswithfewsamplescomparedtoothers
FrontiersinArtificialIntelligence|www.frontiersin.org 13 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- |
FIGURE7|TheproposedhybridarchitectureusingLSTM(left)orCNN(right)forthepredictionofsocio-moralreasoninglevel.
TABLE5|Overallprecision,recall,f1score,andaccuracyofallthemodels. 4.2.6.Discussions
|             |           |        |          |          | The computed     | a priori expert     | knowledge,          | alone, gave    | 40% of    |
| ----------- | --------- | ------ | -------- | -------- | ---------------- | ------------------- | ------------------- | -------------- | --------- |
| Models      | Precision | Recall | f1-score | Accuracy |                  |                     |                     |                |           |
|             |           |        |          |          | accuracy on      | all the dataset,    | which is not        | good. However, | when      |
|             |           |        |          |          | directly merged  | with the            | features learned    | by the DNNs,   | the       |
| Expert-only | 0.47      | 0.40   | 0.38     | 0.40     |                  |                     |                     |                |           |
|             |           |        |          |          | results are      | better than without | that concatenation. | Merging        | the       |
| cnn-only    | 0.58      | 0.53   | 0.49     | 0.53     |                  |                     |                     |                |           |
|             |           |        |          |          | expert knowledge | with the            | features learned    | by the         | models is |
| lstm-only   | 0.42      | 0.43   | 0.42     | 0.43     |                  |                     |                     |                |           |
|             |           |        |          |          | nonetheless      | not sufficient      | as it is comparable | to adding      | a bias.   |
| cnn-expert  | 0.62      | 0.62   | 0.62     | 0.62     |                  |                     |                     |                |           |
Expertknowledgeshouldbeconsideredasaninputthatcanmake
| lstm-expert | 0.54 | 0.53 | 0.51 | 0.53 |     |     |     |     |     |
| ----------- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
changetofeatureslearneddependingonwhetherthesefeatures
| cnn-expert-att | 0.67 | 0.65 | 0.63 | 0.65 |     |     |     |     |     |
| -------------- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
areimportantforthefinalprediction.Asseenintheresults,the
| lstm-expert-att | 0.59 | 0.60 | 0.58 | 0.60 |                 |           |                     |                 |     |
| --------------- | ---- | ---- | ---- | ---- | --------------- | --------- | ------------------- | --------------- | --- |
|                 |      |      |      |      | knowledge-based | attention | layer helps improve | the prediction, |     |
| Finalmodel      | 0.72 | 0.75 | 0.73 | 0.75 |                 |           |                     |                 |     |
whichsuggeststhatusingtheattentionalmechanismissuitable
|     |     |     |     |     | for the targeted | task. Here | are two advantages | of incorporating |     |
| --- | --- | --- | --- | --- | ---------------- | ---------- | ------------------ | ---------------- | --- |
expertknowledgetoDNN:(1)Modelsareabletogeneralizewell
evenwithalimitedamountofdata;(2)Modelsareabletomake
accuratepredictiononunbalanceddataset.
withnoexpertknowledge(f1scoreforclasses2,4,and5).Thisis
4.2.6.1.RealLifeSocio-MoralReasoningClassification
duetothefactthatexpertsdonotneeddatatomakedecisions
becausetheirdecisionsarebasedontheirownknowledge.This Different experts tend to associate to the same verbatim:
suggeststhat,incorporatingexpertknowledgetoneuralmodels different—butclose—classes.Takingintoconsiderationthateven
improvestheclassificationevenwhenthedatasetisunbalanced. expertscanmakeerrors,weretrainedourmodelbyconsidering
Also, even if there is not a huge amount of training data, the amarginerrorof1forthe5-classproblem.Forexample,ifthe
modelsarestillabletogeneralizewellonunseendata.Overall,the modelpredictsthattheclassoftheverbatimvis4andthatthe
CNN based models perform well than the LSTM based models realclassis5,thenitisconsideredasacorrectclassification.The
becauseithasbeenshownthatthelatterisasolutionthathasa results taking into account errors margins showed a noticeable
bettergeneralizationpowerwhenthereisalotofavailabledata. improvement.Wegainedmorethan5%ontheoverallf1score.
FrontiersinArtificialIntelligence|www.frontiersin.org 14 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
FIGURE8|Precisionofallthemodelsforeachlevel.
FIGURE9|F1-scoreofallthemodelsforeachlevel.
4.2.6.2.PersonalizationinMorALERT socio-moralreasoningskilllevelwasthereafterusedtoupdatethe
Thefinalmodel(usingCNNasitgavebestresults)wasintegrated currentplayermodelandtoadapttheseriousgameaccordingly.
inthegamethatiscurrentlyinexperimentation.Theprediction Tointroduceaformoffeedbackandscoringinsidethegame,
was done in real time. We recorded audio justification of the we added a simulated social feedback showing the number of
learner before transforming it to text using Google speech to “likes” and “friends” depending on the player responses. When
text API.8 The text was then fed into the model, outputting players’ socio-moral reasoning maturity level increased, players
the predicted socio-moral reasoning skill level. The predicted gained “likes”, and when they made positive evaluations of the
opinionsofNPCwithahigherlevelofmaturitythantheirown,
they gained “friends”. Their evaluation of the opinions of NPC
8https://cloud.google.com/speech-to-text/ withlowerlevelsofSMRmaturityhadnoeffectonthenumber
FrontiersinArtificialIntelligence|www.frontiersin.org 15 June2022|Volume5|Article921476

| TatoandNkambou |     |     |     |     |     |     |     |     |     | HybridNeuralNetworkforPersonalization |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
oflikesornumberoffriends.Forthe10playerswehavealready the dilemma sequencing in the game. The findings from a
experimented,themodelwasabletocorrectlypredictthesocio- recentexperimentofMorALERT(Zarglayounetal.,2022)show
moralreasoningskilllevelsbasedonthecomparisonwithhuman promise in terms of its potential for assessing and improving
experts’ prediction. Furthermore, the assessment of the game socio-moralreasoningmaturity.
suggests that the players appreciated it in terms of immersion, Thanks to its hybrid nature, the proposed model is also
playabilityandimpressionofhavinglearnedsomething.Results intended to help experts in the annotation of verbatims.
alsoshowthatthegameencouragesthedevelopment ofhigher Results are very promising for the field. Contrary to the
levelsofSMRskillfrompre-testcomparedtothegame,butalso state-of-the-art techniques in text classification, the solution
from pre-test compared to post test. In fact, results during the we proposed achieves the best results in our context. This is
post-testappeartobelowerthanduringthegame,whichmight mainlyduetothedeepstructuresthatcanlearnusefulfeatures
be related to the higher level of perceived immersion and also from data and also the a priori knowledge that can leverage
| because | of the | social simulation |     | associated | with | the NPC | and | unbalanceddata. |     |     |     |     |     |
| ------- | ------ | ----------------- | --- | ---------- | ---- | ------- | --- | --------------- | --- | --- | --- | --- | --- |
theiropinionsandalsothesocialfeedbackinterface. Theideaofusingattentiontoincorporateexpertknowledge
|     |     |     |     |     |     |     |     | to NN can | be used in | other domains such | as text | classification |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------------ | ------- | -------------- | --- |
5. CONCLUSION orinmedicinewherethereisalotofexpertknowledgeavailable.
Forexample,wecouldthinkofaclassifierusinganeuralnetwork
combinedwitharule-basedsystem,astheexpertknowledge.
| In this   | paper, | we proposed |      | a simple, | effective,   | and | intuitive |     |     |     |     |     |     |
| --------- | ------ | ----------- | ---- | --------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
| technique | to     | improve     | deep | learning  | architecture |     | on user   |     |     |     |     |     |     |
modeling for personalization purposes. It consists of DATA AVAILABILITY STATEMENT
| incorporating |            | expert knowledge |           | (when   | available)     | using | the |         |                 |                 |         |         |         |
| ------------- | ---------- | ---------------- | --------- | ------- | -------------- | ----- | --- | ------- | --------------- | --------------- | ------- | ------- | ------- |
|               |            |                  |           |         |                |       |     | The raw | data supporting | the conclusions | of this | article | will be |
| attention     | mechanism, |                  | to neural | network | architectures. |       | The |         |                 |                 |         |         |         |
solution was tested in two learning environments: Logic-Muse madeavailablebytheauthors,withoutunduereservation.
andMorALERT.
|                |     |          |             |            |        |            |          | AUTHOR | CONTRIBUTIONS |     |     |     |     |
| -------------- | --- | -------- | ----------- | ---------- | ------ | ---------- | -------- | ------ | ------------- | --- | --- | --- | --- |
| In Logic-Muse, |     | the      | experiments | consisted  |        | in tracing | the      |        |               |     |     |     |     |
| logical skills | of  | students | using       | the hybrid | model. | At         | the same |        |               |     |     |     |     |
time,weintroducedanewwayofusingtheattentionmechanism, AT and RN contributed to conception and design of the study
toallowneuralnetworkstotakeintoaccountexpertknowledge and wrote the sections of the manuscript. AT implemented
|     |     |     |     |     |     |     |     | the systems | (Logic-Muse | and MorALERT) | and | the | models, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- | --- | --- | ------- |
(whenavailable)intheirtraininganddecisionprocess.Wetested
thesolutiononadatasetthatisunbalanced.Theresultsshowed organized the datasets used for the experiments, performed
thattheDKTisunabletoaccuratelytrackskillswithlittledata, the analysis of the results, and wrote the first draft of the
manuscript.Allauthorscontributedtomanuscriptrevision,read,
comparetotheDKT+BN.
During the experiments, we noticed that, for skills that are andapprovedthesubmittedversion.
veryeasytomaster,allthe2modelswereunabletotrackincorrect
|     |     |     |     | =incorrectanswers/total |     |     |     | FUNDING |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
answers,duetothefactthattheratior
| of questions | answered |     | was very | low. Even | with | a penalty, | we  |     |     |     |     |     |     |
| ------------ | -------- | --- | -------- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
werenotabletosignificantlyimprovetheDKTmodel.However, ThisresearchwassupportedbygrantsfromNaturalSciencesand
in this paper, we have set the regularization parameters λ and Engineering Research Council of Canada (NSERC), Discovery
1
| λ      |         |       |         |              |     |         |        | GrantAwardedtoRN.Thisresearchwasalsosupportedbygrants |     |     |     |     |     |
| ------ | ------- | ----- | ------- | ------------ | --- | ------- | ------ | ----------------------------------------------------- | --- | --- | --- | --- | --- |
| 2 with | a fixed | value | but for | future work, | we  | will do | a grid |                                                       |     |     |     |     |     |
search to find the best values. We will do further experiments fromFondsdeRechercheduQuébecSociétéetCulture(FRQSC)
on the integration of expert knowledge into neural network awardedtoRNandhiscolleagues(ResearchTeam).
architectures.Wealsoplantotestourtechniquesonalargerand
| orpublicdataset. |     |       |     |           |        |              |     | ACKNOWLEDGMENTS |     |     |     |     |     |
| ---------------- | --- | ----- | --- | --------- | ------ | ------------ | --- | --------------- | --- | --- | --- | --- | --- |
| The proposed     |     | model | has | also been | tested | in MorALERT, |     |                 |     |     |     |     |     |
a serious game adaptive learning environment for assessing We would like to thank Miriam Beauchamp, Aude Dufresne,
andoptimizingSMRinadolescence.InMorALERT,ourmodel SergeRobert,JanieBrisson,andJulietteLaurendeaufortheirhelp
accurately predicts the socio-moral reasoning skill level based inthiswork.Thecontentofthismanuscripthasbeenpresented
on textual verbatimand a priori expertknowledge. Thismakes inpartattheTenthAAAISymposiumonEducationalAdvances
inArtificialIntelligence(Tatoetal.,2020).
| it possible | to  | propose | an adapted | (personalized) |     | order | for |     |     |     |     |     |     |
| ----------- | --- | ------- | ---------- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
|     |     |     |     |     |     |     |     | Beauchamp,    | M., Dooley,        | J. J., and Anderson, | V. (2013).      | A   | preliminary  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------ | -------------------- | --------------- | --- | ------------ |
|     |     |     |     |     |     |     |     | investigation | of moral reasoning | and empathy          | after traumatic |     | brain injury |
Bahdanau, D., Cho, K., and Bengio, Y. (2014). Neural machine translation in adolescents. Brain Injury 27, 896–902. doi: 10.3109/02699052.2013.
| by jointly | learning | to align | and | translate. arXiv | preprint | arXiv:1409.0473. |     | 775486 |     |     |     |     |     |
| ---------- | -------- | -------- | --- | ---------------- | -------- | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
doi:10.48550/arXiv.1409.0473 Bhunia, A. K., Khan, S., Cholakkal, H., Anwer, R. M., Khan, F. S.,
Bakkes, S. C., Spronck, P. H., and van Lankveld, G. (2012). Player and Shah, M. (2021). “Handwriting transformers,” in Proceedings of
behavioural modelling for video games. Entertain. Comput. 3, 71–79. the IEEE/CVF International Conference on Computer Vision, 1086–1094.
doi:10.1016/j.entcom.2011.12.001 doi:10.1109/ICCV48922.2021.00112
FrontiersinArtificialIntelligence|www.frontiersin.org 16 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
Birk, M. V., Toker, D., Mandryk, R. L., and Conati, C. (2015). “Modeling ProceedingsoftheFifteenthConferenceonUncertaintyinArtificialIntelligence
motivationinasocialnetworkgameusingplayer-centrictraitsandpersonality (SanFrancisco,CA:MorganKaufmannPublishersInc.),206–215.
traits,” in International Conference on User Modeling, Adaptation, and Ghosh, S., Baranowski, E. S., van Veen, R., de Vries, G.-J., Biehl, M., Arlt,
Personalization(Cham:Springer),18–30.doi:10.1007/978-3-319-20267-9_2 W., et al. (2017). “Comparison of strategies to learn from imbalanced
Chen, H., and Zhang, Z. (2021). Hybrid neural network based on classes for computer aided diagnosis of inborn steroidogenic disorders,” in
novel audio feature for vehicle type identification. Sci. Rep. 11, 1–10. Proc. of the European Symposium on Artificial Neural Networks (Bruges).
doi:10.1038/s41598-021-87399-1 doi:10.1530/endoabs.49.OC1.3
Chiasson, V., Vera-Estay, E., Lalonde, G., Dooley, J., and Beauchamp, Gow,J.,Baumgarten,R.,Cairns,P.,Colton,S.,andMiller,P.(2012).Unsupervised
M. (2017). Assessing social cognition: age-related changes in moral modelingofplayerstylewithLDA.IEEETrans.Comput.Intell.AIGames4,
reasoning in childhood and adolescence. Clin. Neuropsychol. 31, 515–530. 152–166.doi:10.1109/TCIAIG.2012.2213600
doi:10.1080/13854046.2016.1268650 Graves,A.(2013).Generatingsequenceswithrecurrentneuralnetworks.arXiv
Chorowski, J. K., Bahdanau, D., Serdyuk, D., Cho, K., and Bengio, Y. (2015). preprintarXiv:1308.0850.doi:10.48550/arXiv.1308.0850
“Attention-based models for speech recognition,” in Advances in Neural Greenberg,R.(2010).Kant’sTheoryofaPrioriKnowledge.UniversityPark,PA:
InformationProcessingSystemsedsCortes,C.,Lawrence,N.,Lee,D.,Sugiyama, PennStateUniversityPress.
M.,andGarnett,R(CurranAssociates,Inc.)28,577–585. Ha,E.Y.,Rowe,J.P.,Mott,B.W.,andLester,J.C.(2011).“Goalrecognition
Collobert,R.,andWeston,J.(2008).“Aunifiedarchitecturefornaturallanguage withMarkovlogicnetworksforplayer-adaptivegames,”inSeventhArtificial
processing:deepneuralnetworkswithmultitasklearning,”inProceedingsof IntelligenceandInteractiveDigitalEntertainmentConference(Stanford,CA:
the25thInternationalConferenceonMachineLearning(NewYork,NY:ACM), AAAI).
160–167.doi:10.1145/1390156.1390177 He,K.,Zhang,X.,Ren,S.,andSun,J.(2016).“Deepresiduallearningforimage
Conati, C., Gertner, A. S., VanLehn, K., and Druzdzel, M. J. (1997). “On-line recognition,”inProceedingsoftheIEEEConferenceonComputerVisionand
studentmodelingforcoachedproblemsolvingusingbayesiannetworks,”in PatternRecognition(LasVegas,NV:IEEE),770–778.doi:10.1109/CVPR.20
UserModelingedsJameson,H.,Paris,C.,andTasso,C.(Springer),231–242. 16.90
doi:10.1007/978-3-7091-2670-7_24 Hearst,M.A.,Dumais,S.T.,Osuna,E.,Platt,J.,andScholkopf,B.(1998).Support
Corbett, A. T., and Anderson, J. R. (1994). Knowledge tracing: modeling the vectormachines.IEEEIntell.Syst.Appl.13,18–28.doi:10.1109/5254.708428
acquisition of procedural knowledge. User Model User Adapt. Interact. 4, Horvitz,E.,Breese,J.,Heckerman,D.,Hovel,D.,andRommelse,K.(1998).“The
253–278.doi:10.1007/BF01099821 lumiereproject:Bayesianusermodelingforinferringthegoalsandneedsof
Cordón,O.,Herrera,F.,andVillar,P.(2001).Generatingtheknowledgebaseof softwareusers,”inProceedingsoftheFourteenthConferenceonUncertaintyin
afuzzyrule-basedsystembythegeneticlearningofthedatabase.IEEETrans. ArtificialIntelligence(SanFrancisco,CA:MorganKaufmannPublishersInc.),
FuzzySyst.9,667–674.doi:10.1109/91.940977 256–265.
Coro, G., Pagano, P., and Ellenbroek, A. (2013). Combining simulated Huang, C., Li, Y., Change Loy, C., and Tang, X. (2016).1 “Learning deep
expert knowledge with neural networks to produce ecological representation for imbalanced classification,” in Proceedings of the IEEE
niche models for latimeria chalumnae. Ecol. Modell. 268, 55–63. ConferenceonComputerVisionandPatternRecognition(LasVegas,NV:IEEE),
doi:10.1016/j.ecolmodel.2013.08.005 5375–5384.doi:10.1109/CVPR.2016.580
Dass, S., Gary, K., and Cunningham, J. (2021). Predicting student dropout in Kantharaju, P., Alderfer, K., Zhu, J., Char, B., Smith, B., and Ontanón, S.
self-paced mooc course using random forest model. Information 12, 476. (2018). “Tracing player knowledge in a parallel programming educational
doi:10.3390/info12110476 game,”inFourteenthArtificialIntelligenceandInteractiveDigitalEntertainment
Demuth,H.B.,Beale,M.H.,DeJess,O.,andHagan,M.T.1(2014).NeuralNetwork Conference(Publisher:AAAIPress).
Design.Stillwater,OK:MartinHagan. Khajah, M., Lindsey, R. V., and Mozer, M. C. (2016). How deep is
Dietterich,T.G.(2000).“Ensemblemethodsinmachinelearning,”inInternational knowledgetracing?arXivpreprintarXiv:1604.02416.doi:10.48550/arXiv.1604.
WorkshoponMultipleClassifierSystems(Berlin;Heidelberg:Springer),1–15. 02416
doi:10.1007/3-540-45014-9_1 Kingma,D.P.,andBa,J.(2014).Adam:amethodforstochasticoptimization.arXiv
Domladovac, M. (2021). “Comparison of neural network with gradient preprintarXiv:1412.6980.doi:10.48550/arXiv.1412.6980
boosted trees, random forest, logistic regression and SVM in predicting Kohlberg, L. (1984). Essays on Moral Development: The Psychology of Moral
studentachievement,”in202144thInternationalConventiononInformation, Development.Vol.2.Cambridge:Harper&Row.
CommunicationandElectronicTechnology(MIPRO)(Opatija:IEEE),211–216. Kusner, M., Sun, Y., Kolkin, N., and Weinberger, K. (2015). “From word
doi:10.23919/MIPRO52101.2021.9596684 embeddingstodocumentdistances,”inInternationalConferenceonMachine
Dooley, J. J., Beauchamp, M., and Anderson, V. A. (2010). The measurement LearningedsBach,F.,andBlei,D.(Lille:JMLR.org),957–966.
of sociomoral reasoning in adolescents with traumatic brain injury: a Liu, H.-I., and Chen, W.-L. (2022). X-transformer: a machine translation
pilot investigation. Brain Impairment 11, 152–161. doi: 10.1375/brim.11. model enhanced by the self-attention mechanism. Appl. Sci. 12, 4502.
2.152 doi:10.3390/app12094502
Drachen,A.,Green,J.,Gray,C.,Harik,E.,Lu,P.,Sifa,R.,etal.(2016).“Gunsand Lu, H., Setiono, R., and Liu, H. (1996). Effective data mining using neural
guardians:comparativeclusteranalysisandbehavioralprofilingindestiny,” networks. IEEE Trans. Knowledge Data Eng. 8, 957–961. doi: 10.1109/69.
in 2016 IEEE Conference on Computational Intelligence and Games (CIG) 553163
(Santorini:IEEE),1–8.doi:10.1109/CIG.2016.7860423 Luong, M.-T., Pham, H., and Manning, C. D. (2015). Effective approaches to
Drachen,A.,Sifa,R.,Bauckhage,C.,andThurau,C.(2012).“Guns,swordsand attention-basedneuralmachinetranslation.arXivpreprintarXiv:1508.04025.
data:clusteringofplayerbehaviorincomputergamesinthewild,”in2012IEEE doi:10.18653/v1/D15-1166
ConferenceonComputationalIntelligenceandGames(CIG)(Granada:IEEE), Markovits,H.(2013).“Howtodevelopalogicalreasoner:ahierarchicalmodel
163–170.doi:10.1109/CIG.2012.6374152 ofinformationuseinconditionalreasoning,”inTheDevelopmentalPsychology
Fisher,J.L.,Hinds,S.C.,andD’Amato,D.P.(1990).“Arule-basedsystemfor ofReasoningandDecision-MakingedMarkovits,H.(Hove:PsychologyPress),
documentimagesegmentation,”in10thInternationalConferenceonPattern 148–164.doi:10.4324/9781315856568
Recognition (Atlantic City, NJ: IEEE), 567–572. doi: 10.1109/ICPR.1990. Martin, J., and VanLehn, K. (1995). Student assessment using Bayesian
118166 NETs. Int. J. Hum. Comput. Stud. 42, 575–591. doi: 10.1006/ijhc.19
Flores, M. J., Nicholson, A. E., Brunskill, A., Korb, K. B., and Mascaro, 95.1025
S. (2011). Incorporating expert knowledge when learning Bayesian McLachlan,G.(2004).DiscriminantAnalysisandStatisticalPatternRecognition,
network structure: a medical case study. Artif. Intell. Med. 53, 181–204. Vol.544.NewYork,NY:JohnWiley&Sons.
doi:10.1016/j.artmed.2011.08.004 Missura, O., and Gärtner, T. (2009). “Player modeling for intelligent difficulty
Friedman, N., Nachman, I., and Peér, D. (1999). “Learning bayesian network adjustment,” in International Conference on Discovery Science (Berlin:
structure from massive datasets: the “sparse candidate” algorithm,” in Springer),197–211.doi:10.1007/978-3-642-04747-3_17
FrontiersinArtificialIntelligence|www.frontiersin.org 17 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
Montero,S.,Arora,A.,Kelly,S.,Milne,B.,andMozer,M.(2018).“Doesdeep Tato,A.,Nkambou,R.,Brisson,J.,andRobert,S.(2017a).“Predictinglearner’s
knowledge tracing model interactions among skills?” in 11th International deductive reasoning skills using a bayesian network,” in International
ConferenceonEducationalDataMining,EDM2018(Buffalo,NY). ConferenceonArtificialIntelligenceinEducation(Wuhan:Springer),381–392.
Moon, K., Kim, J., and Lee, J. (2021). Early prediction model of student doi:10.1007/978-3-319-61425-0_32
performancebasedondeepneuralnetworkusingmassiveLMSlogdata.J. Tato, A., Nkambou, R., and Dufresne, A. (2020). “Using ai techniques in
KoreaContentsAssoc.21,1–10.doi:10.1016/j.compedu.2020.104108 a serious game for socio-moral reasoning development,” in The Thirty-
Muyuan, W., Naiyao, Z., and Hancheng, Z. (2004). “User-adaptive music Fourth AAAI Conference on Artificial Intelligence, AAAI 2020, The Thirty-
emotionrecognition,”inProceedings7thInternationalConferenceonSignal Second Innovative Applications of Artificial Intelligence Conference, IAAI
Processing, 2004 (Beijing: IEEE), 1352–1355. doi: 10.1109/ICOSP.2004. 2020 (New York, NY: AAAI Press), 13477–13484. doi: 10.1609/aaai.v34i
1441576 09.7066
Nguyen,L.,andDo,P.(2009).“CombinationofBayesiannetworkandoverlay Tato, A. A. N., Nkambou, R., Dufresne, A., and Beauchamp, M. H. (2017b).
model in user modeling,” in International Conference on Computational “Convolutional neural network for automatic detection of sociomoral
Science (Baton Rouge, LA: Springer), 5–14. doi: 10.1007/978-3-642-019 reasoning level,” in EDM (Worcester, MA: International Educational Data
73-9_2 MiningSociety).
Nkambou,R.,Brisson,J.,Kenfack,C.,Robert,S.,Kissok,P.,andTato,A.(2015). Towell, G. G., and Shavlik, J. W. (1994). Knowledge-based artificial neural
“Towards an intelligent tutoring system for logical reasoning in multiple networks.Artif.Intell.70,119–165.doi:10.1016/0004-3702(94)90105-8
contexts,” in Design for Teaching and Learning in a Networked World eds Troussas, C., Krouska, A., and Virvou, M. (2020). “Using a multi module
Conole, G., Klobuar, T., Rensing, C., Konert, J., and Lavoue, E. (Berlin; modelforlearninganalyticstopredictlearners’cognitivestatesandprovide
Heidelberg:Springer-Verlag),460–466.doi:10.1007/978-3-319-24258-3_40 tailoredlearningpathwaysandassessment,”inMachineLearningParadigms
Nkambou, R., Mizoguchi, R., and Bourdeau, J. (2010). Advances in edsVirvou,M.,Alepis,E.,Tsihrintzis,G.,andJain,L.(Cham:Springer),9–22.
Intelligent Tutoring Systems, Vol. 308. Springer Science & Business Media. doi:10.1007/978-3-030-13743-4_2
doi:10.1007/978-3-642-14363-2 Tsamardinos, I., Brown, L. E., and Aliferis, C. F. (2006). The max-min hill-
Nur, N. (2021). Developing temporal machine learning approaches to support climbing bayesian network structure learning algorithm. Mach. Learn. 65,
modeling, explaining, and sensemaking of academic success and risk of 31–78.doi:10.1007/s10994-006-6889-7
undergraduate students (Ph.D. thesis). The University of North Carolina at Tseng,J.C.,Chu,H.-C.,Hwang,G.-J.,andTsai,C.-C.(2008).Developmentof
Charlotte,Charlotte,NC,UnitedStates. anadaptivelearningsystemwithtwosourcesofpersonalizationinformation.
Pardos, Z. A., and Heffernan, N. T. (2010). “Modeling individualization Comput.Educ.51,776–786.doi:10.1016/j.compedu.2007.08.002
in a Bayesian networks implementation of knowledge tracing,” in Van Melle, W. (1978). Mycin: a knowledge-based consultation program
InternationalConferenceonUserModeling,Adaptation,andPersonalization for infectious disease diagnosis. Int. J. Man Mach. Stud. 10, 313–322.
(Big Island, HI: Springer-Verlag, Berlin Heidelberg), 255–266. doi:10.1016/S0020-7373(78)80049-2
doi:10.1007/978-3-642-13470-8_24 Wang, L., Sy, A., Liu, L., and Piech, C. (2017). “Deep knowledge tracing
Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., et al. on programming exercises,” in Proceedings of the Fourth 2017 ACM
(2015).“Deepknowledgetracing,”inAdvancesinNeuralInformationProcessing Conference on Learning@ Scale (New York, NY: ACM), 201–204.
SystemsedsCortes,C.,Lawrence,N.,Lee,D.,Sugiyama,M.,andGarnett,R. doi:10.1145/3051457.3053985
(CurranAssociates,Inc.),505–513. Woolf, B. P. (2010). Building Intelligent Interactive Tutors: Student-Centered
Rowe, J., Mott, B., McQuiggan, S., Robison, J., Lee, S., and Lester, J. (2009). StrategiesforRevolutionizinge-Learning.Burlington,MA:MorganKaufmann.
“Crystal island: a narrative-centered learning environment for eighth grade Xing, W., Li, C., Chen, G., Huang, X., Chao, J., Massicotte, J., et al.
microbiology,” in Workshop on Intelligent Educational Games at the 14th (2021). Automatic assessment of students’ engineering design performance
International Conference on Artificial Intelligence in Education (Brighton), using a bayesian network model. J. Educ. Comput. Res. 59, 230–256.
11–20. doi:10.1177/0735633120960422
Rowe,J.P.,andLester,J.C.(2010).“Modeling userknowledgewithdynamic Xu, K., Ba, J., Kiros, R., Cho, K., Courville, A., Salakhudinov, R., et al.
Bayesiannetworksininteractivenarrativeenvironments,”inSixthArtificial (2015).“Show,attendandtell:neuralimagecaptiongenerationwithvisual
IntelligenceandInteractiveDigitalEntertainmentConference(PaloAlto,CA: attention,”inInternationalConferenceonMachineLearning(Lille:JMLR.org),
AAAI),57–62. 2048–2057.
Russell,S.J.,andNorvig,P.(2016).ArtificialIntelligence:AModernApproach. Yan,J.,Liu,J.,Yu,Y.,andXu,H.(2021).Waterqualitypredictionintheluanriver
Harlow:PearsonEducationLimited. basedon1-DRCNNandbigruhybridneuralnetworkmodel.Water13,1273.
Sabourin, J., Mott, B., and Lester, J. C. (2011). “Modeling learner affect doi:10.3390/w13091273
with theoretically grounded dynamic Bayesian networks,” in International Yannakakis, G. N., and Hallam, J. (2009). Real-time game adaptation for
ConferenceonAffectiveComputingandIntelligentInteraction(Memphis,TN: optimizing player satisfaction. IEEE Trans. Comput. Intell. AI Games 1,
Springer),286–295.doi:10.1007/978-3-642-24600-5_32 121–133.doi:10.1109/TCIAIG.2009.2024533
Sharma,G.,Parashar,A.,andJoshi,A.M.(2021).Dephnn:anovelhybridneural Yeung, C.-K., and Yeung, D.-Y. (2018). Addressing two problems in deep
network for electroencephalogram (EEG)-based screening of depression. knowledge tracing via prediction-consistent regularization. arXiv preprint
Biomed. Signal Process. Control 66, 102393. doi: 10.1016/j.bspc.2020. arXiv:1806.02180.doi:10.1145/3231644.3231647
102393 Yu,Z.,Lian,J.,Mahmoody,A.,Liu,G.,andXie,X.(2019).“Adaptiveusermodeling
Shi,D.,Guan,J.,andZurada,J.(2015).“Cost-sensitivelearningforimbalanced withlongandshort-termpreferencesforpersonalizedrecommendation,”in
baddebtdatasetsinhealthcareindustry,”in2015Asia-PacificConferenceon IJCAI(Macao:IJCAI),4213–4219.doi:10.24963/ijcai.2019/585
ComputerAidedSystemEngineering(Quito:IEEE),30–35. Yuan,F.,Zhang,G.,Karatzoglou,A.,Jose,J.,Kong,B.,andLi,Y.(2021).“One
Song,X.,Li,J.,Tang,Y.,Zhao,T.,Chen,Y.,andGuan,Z.(2021).JKT:ajoint person,onemodel,oneworld:learningcontinualuserrepresentationwithout
graphconvolutionalnetworkbaseddeepknowledgetracing.Inform.Sci.580, forgetting,”inProceedingsofthe44thInternationalACMSIGIRConferenceon
510–523.doi:10.1016/j.ins.2021.08.100 ResearchandDevelopmentinInformationRetrieval(NewYork,NY),696–705.
Stern, M., Beck, J., and Woolf, B. P. (1999). Naive Bayes Classifiers for doi:10.1145/3404835.3462884
User Modeling. Center for Knowledge Communication, Computer Science Zakrzewska, D. (2008). “Cluster analysis for users’ modeling in intelligent e-
Department,UniversityofMassachusetts. learningsystems,”inInternationalConferenceonIndustrial,Engineeringand
Tato,A.,Nkambou,R.,Brisson,J.,Kenfack,C.,Robert,S.,andKissok,P.(2016). OtherApplicationsofAppliedIntelligentSystems(Berlin:Springer),209–214.
“A Bayesian network for the cognitive diagnosis of deductive reasoning,” doi:10.1007/978-3-540-69052-8_22
inEuropeanConferenceonTechnologyEnhancedLearning (Lyon:Springer), Zappone, A., Di Renzo, M., Debbah, M., Lam, T. T., and Qian, X. (2018).
627–631.doi:10.1007/978-3-319-45153-4_78 Model-aided wireless artificial intelligence: embedding expert knowledge in
FrontiersinArtificialIntelligence|www.frontiersin.org 18 June2022|Volume5|Article921476

TatoandNkambou HybridNeuralNetworkforPersonalization
deepneuralnetworkstowardswirelesssystemsoptimization.arXivpreprint ConflictofInterest:Theauthorsdeclarethattheresearchwasconductedinthe
arXiv:1808.01672.doi:10.1109/MVT.2019.2921627 absenceofanycommercialorfinancialrelationshipsthatcouldbeconstruedasa
Zarglayoun, H., Laurendeau-Martin, J., Tato, A., Vera-Estay, E., Blondin, A., potentialconflictofinterest.
Lamy-Brunelle, A., et al. (2022). Assessing and optimising socio-moral
reasoningskills:findingsfromthemoralertseriousvideogame.Front.Psychol.
Publisher’sNote:Allclaimsexpressedinthisarticlearesolelythoseoftheauthors
12,767596.doi:10.3389/fpsyg.2021.767596
anddonotnecessarilyrepresentthoseoftheiraffiliatedorganizations,orthoseof
Zhang, J., Shi, X., King, I., and Yeung, D.-Y. (2017a). “Dynamic key-value
thepublisher,theeditorsandthereviewers.Anyproductthatmaybeevaluatedin
memory networks for knowledge tracing,” in Proceedings of the 26th
InternationalConferenceonWorldWideWeb(Geneva:InternationalWorld thisarticle,orclaimthatmaybemadebyitsmanufacturer,isnotguaranteedor
WideWebConferencesSteeringCommittee),765–774.doi:10.1145/3038912. endorsedbythepublisher.
3052580
Zhang, K., and Yao, Y. (2018). A three learning states bayesian knowledge Copyright©2022 TatoandNkambou.Thisisanopen-accessarticledistributed
tracingmodel.Knowl.BasedSyst.148,189–201.doi:10.1016/j.knosys.2018. under the terms of the Creative Commons Attribution License (CC BY). The
03.001 use, distribution or reproduction in other forums is permitted, provided the
Zhang, L., Xiong, X., Zhao, S., Botelho, A., and Heffernan, N. T. (2017b). original author(s) and the copyright owner(s) are credited and that the original
“Incorporatingrichfeaturesintodeepknowledgetracing,”inProceedingsof publicationinthisjournaliscited,inaccordancewithacceptedacademicpractice.
theFourth(2017)ACMConferenceonLearning@Scale(NewYork,NY:ACM), Nouse,distributionorreproductionispermittedwhichdoesnotcomplywiththese
169–172.doi:10.1145/3051457.3053976 terms.
FrontiersinArtificialIntelligence|www.frontiersin.org 19 June2022|Volume5|Article921476