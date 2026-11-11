CLST: Cold-Start Mitigation in Knowledge
Tracing by Aligning a Generative Language
Model as a Students’ Knowledge Tracer
Heeseok Jung1, Jaesang Yoo1, Yohaan Yoon1, and Yeonju Jang2((cid:0))
1 Classting Edutech Research, Seoul, Republic of Korea
{poco2889,jsyoo,eddie}@classting.com
2 Korea University, Seoul, Republic of Korea
spring0425@korea.ac.kr
Abstract. Knowledgetracing(KT),whereinstudents’problem-solving
histories are used to estimate their current levels of knowledge, has at-
tractedsignificantinterestfromresearchers.However,mostexistingKT
modelsweredevelopedwithanID-basedparadigm,whichexhibitslimi-
tationsincold-startperformance.Theselimitationscanbemitigatedby
leveragingthevastquantitiesofexternalknowledgepossessedbygener-
ativelargelanguagemodels(LLMs).Inthisstudy,weproposecold-start
mitigationinknowledgetracingbyaligningagenerativelanguagemodel
as a students’ knowledge tracer (CLST) as a framework that utilizes a
generativeLLMasaknowledgetracer.Uponcollectingdatafrommath,
socialstudies,andsciencesubjects,weframedtheKTtaskasanatural
languageprocessingtask,whereinproblem-solvingdataareexpressedin
naturallanguage,andfine-tunedthegenerativeLLMusingtheformatted
KTdataset.Subsequently,weevaluatedtheperformanceoftheCLSTin
situationsofdatascarcityusingvariousbaselinemodelsforcomparison.
The results indicate that the CLST significantly enhanced performance
with a dataset of fewer than 100 students in terms of prediction, relia-
bility, and cross-domain generalization.
Keywords: intelligenttutoringsystem·knowledgetracing(KT)·per-
sonalized learning.
1 Introduction
Asweentertheeraofdigitaltransformation,onlinelearningisbecomingincreas-
ingly prevalent worldwide. In this context, intelligent tutoring systems (ITSs)
have become increasingly significant in the field of education [3]. These systems
can significantly enhance student learning by utilizing technologies that predict
academic achievement and dropout rates [12,49,8].
Among the various technologies used in ITSs, knowledge tracing (KT) has
emerged as a key component that enables personalized learning [40]. To pre-
dict students’ responses to new exercises, KT models their knowledge states by
analyzing their past performance [52]. Understanding the students’ knowledge
4202
nuJ
81
]LC.sc[
2v69201.6042:viXra

| 2   | Jung et | al. |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
states helps in recommending appropriate learning materials and offering rele-
| vant feedback, |     | thereby | enhancing | learning           | outcomes. |         |       |               |     |
| -------------- | --- | ------- | --------- | ------------------ | --------- | ------- | ----- | ------------- | --- |
| A variety      |     | of KT   | models    | have been proposed |           | to meet | these | expectations, | in- |
cludingbothtraditionalanddeeplearning(DL)-basedmodels[3].Inparticular,
theperformanceofDL-basedKTmodelsintermsofpredictingknowledgestates
| has notably | improved |     | with | successive developments. |     |     |     |     |     |
| ----------- | -------- | --- | ---- | ------------------------ | --- | --- | --- | --- | --- |
ThemajorityofexistingKTmodelsaredominatedbytheID-basedparadigm.
AlthoughsuchID-basedmodelsoftenperformwellinpredictingstudents’knowl-
edge states, they share one limitation: prediction performance is significantly
poorincold-startsituations[60].Asanissuestemmingfromscarcedataonusers
or items in recommendation systems [39], the cold-start problem is regarded as
an important issue in the KT field, occurring in the presence of insufficient
data pertaining to certain students or problem-solving interactions [53]. When
an educational institution or EdTech company that operates an online learn-
ing platform attempts to develop an ITS using a KT model for the first time,
it is likely to encounter cold-start problems in the early stages. Consequently,
educational institutions may encounter challenges in utilizing most existing KT
| models | during  | the development |      | of new ITSs.         |     |                |     |                |     |
| ------ | ------- | --------------- | ---- | -------------------- | --- | -------------- | --- | -------------- | --- |
| Many   | studies | have            | made | efforts to alleviate |     | the cold-start |     | issue inherent | to  |
KT,primarilybyutilizingvarioustypesofsideinformationsuchasthelanguage
proficiency of learners [19], difficulty level of questions [25,59], and students’
question-answeringpatterns[54].However,thesemethodsrequireefforttoobtain
additionalinformationbeyondeachlearner’sproblem-solvinghistory,whichmay
| be difficult | in        | the early | stages     | of a service. |          |        |        |             |     |
| ------------ | --------- | --------- | ---------- | ------------- | -------- | ------ | ------ | ----------- | --- |
| On           | the other | hand,     | generative | large         | language | models | (LLMs) | demonstrate |     |
outstanding performance in a wide range of fields and downstream applications
[63,18,22]. Generative LLMs, such as GPT, are auto-regressive language models
that can generate text similar to human writing. These models contain large
quantities of external knowledge and are able to extract high-quality textual
features.
| The | development |     | of KT | models using | external | knowledge |     | inherently | pos- |
| --- | ----------- | --- | ----- | ------------ | -------- | --------- | --- | ---------- | ---- |
sessed by generative LLMs opens the possibility of improving performance in
cold-start situations as well as enhancing the domain adaptability of KT mod-
els. In a cold-start scenario, the scarcity of information from the target domain
can be supplemented by using information from other domains as training data
[7].However,domainadaptationischallengingbecausemostID-basedKTmod-
els currently in use are domain-specific. If a generative LLM is used to train a
KT model with diverse domains, high performance can be achieved even in a
| small number |     | of target | domains | owned by       | educational |          | institutions. |                |     |
| ------------ | --- | --------- | ------- | -------------- | ----------- | -------- | ------------- | -------------- | --- |
| Despite      | the | potential | of      | this approach, | little      | research | has           | been conducted |     |
on the applicability of generative LLMs to KT tasks. One such study was con-
ducted [31]; however, this attempt failed to fully utilize the strengths of gener-
ative LLMs, only expressing exercise description information through IDs. Fur-
thermore, their model relied solely on the number of correct and incorrect an-
swers submitted by each learner, whereas it is also important to account for

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 3
the order in which each learner solves problems. As such, research on modeling
KT through language processing remains insufficient. Given their capabilities,
generative LLMs can be deployed to overcome the limitations of the ID-based
paradigm. As a result, more research is needed to determine the efficacy of ex-
| pressing | KT in | natural language | using | generative |     | LLMs. |     |     |
| -------- | ----- | ---------------- | ----- | ---------- | --- | ----- | --- | --- |
Inthisstudy,weproposeaframeworkcalled“cold-startmitigationinKTby
aligning a generative language model as a students’ knowledge tracer (CLST).”
WeconductedexperimentstodeterminewhetheragenerativeLLMalignedwith
KT could perform well in cold-start scenarios. Initially, we collected data for a
variety of subjects, including mathematics, social studies, and science. The KT
taskwasthenframedasanaturallanguageprocessing(NLP)taskbyexpressing
problem-solving data in natural language, and the formatted KT dataset was
used to fine-tune the generative LLM. Finally, multiple experiments were con-
ducted to investigate CLST’s performance in cold-start situations. This study
| was conducted |     | to address | the following | research | questions |     | (RQs): |     |
| ------------- | --- | ---------- | ------------- | -------- | --------- | --- | ------ | --- |
– RQ1: In cold-start scenarios, does the proposed method demonstrate suc-
| cessful | prediction | performance?  |                |             |     |            |           |     |
| ------- | ---------- | ------------- | -------------- | ----------- | --- | ---------- | --------- | --- |
| – RQ2:  | How        | can exercises | be effectively | represented |     | in natural | language? |     |
– RQ3: Does the proposed model provide a convincing prediction of learners’
| knowledge |     | states? |     |     |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
– RQ4: Is the proposed model effective at predicting student knowledge in
| cross-domain  |     | scenarios? |                    |     |             |     |            |           |
| ------------- | --- | ---------- | ------------------ | --- | ----------- | --- | ---------- | --------- |
| The remainder |     | of this    | paper is organized |     | as follows: | A   | literature | review on |
KT and generative LLMs in personalized learning are presented in Section 2.
Section 3 describes the methodology developed in this study. Section 4 presents
and discusses the experimental results. Finally, Section 5 concludes the study.
| 2 Literature  |     | Review  |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| 2.1 Knowledge |     | tracing |     |     |     |     |     |     |
KT utilizes students’ problem-solving histories to approximate their current
knowledge states and subsequently predict their future responses. A student’s
problem-solvinghistorycanberepresentedasX ={(e ,y ),(e ,y ),··· ,(e ,y )},
|     |     |     |     |     |     | 1 1 | 2 2 | t t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where e corresponds to an exercise that has been solved at a specific time t,
t
| and y represents |     | the correctness   | of the     | student’s | response    |     | to e .   |             |
| ---------------- | --- | ----------------- | ---------- | --------- | ----------- | --- | -------- | ----------- |
| t                |     |                   |            |           |             |     | t        |             |
| KT models        |     | can be distinctly | classified | as        | traditional | or  | DL-based | [3]. Tradi- |
tional approaches of KT include bayesian knowledge tracing (BKT) and factor
analysis models. BKT [9] is a Markov-process-based approach that represents
each student’s knowledge state as a collection of binary values, whereas factor
analysis approaches analyze the factors that affect students’ knowledge states,
suchasattemptcountsandexercisedifficulty.Performancefactoranalysis(PFA)
[36] and knowledge tracing machines (KTM) [47] are representative works on
factor analysis.

4 Jung et al.
The growth of online education has led to a substantial accumulation of
problem-solving data, allowing DL-based KT models to reach outstanding per-
formance. Such methods include recurrent neural network (RNN)-based [38,56],
memory-augmentedneuralnetwork(MANN)-based[58,2,20],transformer-based
[34,15,57], and graph neural network (GNN)-based [30,32,55] models. In this
study, the BKT [9] and factor analysis models [36,23] were chosen from the tra-
ditional KT models, and the RNN-based model [38], MANN-based model [58],
and transformer-based model [15] were chosen as baseline models and used in
the experiment.
2.2 Generative LLMs in personalized learning
Generative LLMs are pre-trained auto-regressive language models, such as
GPT-3, capable of generating human-like text [37]. These probabilistic mod-
els serve as the foundation for natural language processing (NLP) techniques,
which enable the processing of natural language using algorithms. The term
‘large’ denotes the extensive number of parameters each of these models con-
tains, while the term ‘generative’ refers to a subset of LLMs designed for text
generation.GenerativeLLMsarenowatthecoreofavarietyofapplications,in-
cludingsummarizationandtranslation,generallydeliveredthroughdialogue-like
communication with the user [62].
In light of their massive potential, attempts are being made to utilize gen-
erative LLMs in the field of education, with ongoing studies actively exploring
methods to facilitate personalized learning through the use of these models.
To date, LLMs have exhibited effective performance in generating various ed-
ucational materials, including multiple-choice questions [33], stories for reading
comprehensionassessments[5],andquizzes[11].Additionally,studieshavebeen
carried out on adaptive curriculum design [42], automatic grading [28], and au-
tomated feedback generation for assignments [1] utilizing generative LLMs.
AlthoughseveralstudieshavebeenconductedontheuseofgenerativeLLMs
in personalized learning, few attempts have been made to apply them to the
KTfield,whichisacoretechnologytosupportpersonalizedlearning.Theafore-
mentioned study conducted by [31] was limited in that it did not fully leverage
the capabilities of generative LLMs, as exercises were simply represented using
IDs. Moreover, the sequence of problem-solving by learners is crucial in the KT
task, whereas the study in question only considered the number of correct and
incorrect answers by each learner.
Studies on KT have been conducted in an NLP context, leveraging textual
data from questions. For instance, exercise-enhanced recurrent neural network
(EERNN) [44] leverages the text of each exercise to predict student responses
utilizing the Markov property or attention mechanism. Word2vec [29] is used to
transform the words of each exercise into word embeddings, and exercise em-
beddings are subsequently learned by a bidirectional long short-term memory
(LSTM) network. Exercise-aware knowledge tracing (EKT) [24] is an extended
version of EERNN, where a memory network is deployed to quantify the contri-
bution of each exercise to student mastery on multiple knowledge components

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 5
(KCs). Relation-aware self-attention model for knowledge tracing (RKT) [35]
leverages interaction data and the textual content of each exercise to compute
an exercise relation matrix for KT. Furthermore, [46] employed the BERT [10]
embeddingsimilaritiesbetweentextualdatafromexercisestoconstructagraph,
therebypredictingstudentresponsesusingahierarchicalGNNandtwoattention
mechanisms.
| However, | these | methods | did | not rely | on  | generative | language |     | models, | instead |
| -------- | ----- | ------- | --- | -------- | --- | ---------- | -------- | --- | ------- | ------- |
solely utilizing NLP to obtain exercise representations. In other words, there is
still plenty of potential for further research on the effectiveness of generative-
LLM-based KT models. In this study, we examined the efficacy of aligning gen-
| erative LLMs | to  | KT by | expressing | the | KT  | task in | natural | language. |     |     |
| ------------ | --- | ----- | ---------- | --- | --- | ------- | ------- | --------- | --- | --- |
3 Methodology
| 3.1 Problem | formulation |     |     |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Letting E be a set of exercises. A studnet’s responses to exercises in E,
and records of one’s problem-solving can be represented as the set X =
1:t
{x 1 ,x 2 ,··· ,x t }, comprising tuples x t =(e t ,y t ). Here, e t ∈E represents the ex-
ercise solved at a specific time step t, and y ∈{0,1} represents the correctness
t
oftheanswerrecordedbythestudentatt.Withthisnotation,wecanformulate
the KT task in the following way: Given a student’s historical information X 1:t ,
KT aims to predict the probability of correctly solving a new exercise at t+1.
| In the following |     | equation, | f denotes |      | the KT | model. |     |     |     |     |
| ---------------- | --- | --------- | --------- | ---- | ------ | ------ | --- | --- | --- | --- |
|                  |     |           | yˆ        | =f(X |        | ,e )   |     |     |     | (1) |
|                  |     |           |           | t+1  | 1:t    | t+1    |     |     |     |     |
3.2 CLST: Cold-start mitigation in KT by aligning a generative lan-
| guage model | as  | a students’ |     | knowledge |     | tracer |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | --- | ------ | --- | --- | --- | --- |
3.2.1 KTLP formatting: Utilizing natural language as KT information carrier
A student’s problem-solving history X must be transformed into textual se-
quences Xtext using prompt templates for generative LLMs. We start by orga-
nizing ‘Task Input’ to instruct the model to determine whether the student will
solve the target exercise based on their historical interactions, and then output
a binary response of “Yes” or “No”. Here, each exercise is represented by a tex-
tual description (e.g., name of KC), with interactions represented as tuples of
| (exercise description, |     | correctness), |       | connected |     | by the    | ‘->’ | symbol.  |     |        |
| ---------------------- | --- | ------------- | ----- | --------- | --- | --------- | ---- | -------- | --- | ------ |
| Additionally,          |     | the binary    | label | y ∈0,1    | is  | converted | into | a binary | key | answer |
word ytext ∈ {yes, no} to organize the ‘Task Output’. The aforementioned
processallowsustoframetheKTtaskasalanguageprocessingtask.Wecallthis
processKTaslanguageprocessing(KTLP)formatting,whichcanbeformulated
as follows:
|                |           | X text       | =g(X | ,e         | ) , | y text    | =g(y   | )         |     | (2)    |
| -------------- | --------- | ------------ | ---- | ---------- | --- | --------- | ------ | --------- | --- | ------ |
|                |           | 1:t          |      | 1:t        | t+1 | t+1       |        | t+1       |     |        |
| Here,          | g denotes | the          | KTLP | formatting |     | function. | Figure | 1 depicts | a   | sample |
| KTLP-formatted |           | interaction. |      |            |     |           |        |           |     |        |

| 6 Jung         | et al.     |        |           |                |     |              |     |     |     |     |
| -------------- | ---------- | ------ | --------- | -------------- | --- | ------------ | --- | --- | --- | --- |
|                |            | Fig.1. | Sample    | KTLP-formatted |     | interaction. |     |     |     |     |
| 3.2.2 Response | prediction |        | with CLST |                |     |              |     |     |     |     |
UpontakingthediscretetokensofX text asinput,anLLMisusedtogenerate
1:t
yˆtext
the next token as the output. This process can be formulated as follows:
t+1
|     |     |     | l =M(X |           | text)∈RV |      |     |     |     | (3) |
| --- | --- | --- | ------ | --------- | -------- | ---- | --- | --- | --- | --- |
|     |     |     | t+1    |           | 1:t      |      |     |     |     |     |
|     |     |     | p =    | Softmax(l |          | )∈RV |     |     |     | (4) |
|     |     |     | t+1    |           | t+1      |      |     |     |     |     |
yˆtext
|     |     |     |     |     | ∼p t+1 |     |     |     |     | (5) |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
t+1
| whereM | denotestheLLM,V |     |     | denotesthevocabularysize,andyˆtext |     |     |     |     | denotes |     |
| ------ | --------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ------- | --- |
t+1
| the next predicted |     | token | drawn from | the | probability |     | distribution | p   | .   |     |
| ------------------ | --- | ----- | ---------- | --- | ----------- | --- | ------------ | --- | --- | --- |
t+1
| However, | the KT | model’s | output | should | be  | a floating-point |     | number | yˆ  | ∈   |
| -------- | ------ | ------- | ------ | ------ | --- | ---------------- | --- | ------ | --- | --- |
t+1
[0,1] rather than a discrete token yˆtext. Therefore, following prior studies on
t+1
RV
| point-wise | scoring | tasks | (e.g., recommendation), |     |     | we  | take | the logits | l t+1 | ∈   |
| ---------- | ------- | ----- | ----------------------- | --- | --- | --- | ---- | ---------- | ----- | --- |
and apply a bi-dimensional softmax over the logits of binary answer words. The
| KT prediction | of LLM | can | thus be | written | as: |     |     |     |     |     |
| ------------- | ------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
|               |        |     |         | exp(l   |     | )   |     |     |     |     |
t+1, yes
|     |     | yˆ t+1 | =     |         |         |        |     |     |     | (6) |
| --- | --- | ------ | ----- | ------- | ------- | ------ | --- | --- | --- | --- |
|     |     |        | exp(l |         | )+exp(l |        | )   |     |     |     |
|     |     |        |       | t+1,yes |         | t+1,no |     |     |     |     |
3.2.3Instructionfine-tuningusingKTLP-formatteddatawithLoRAarchitecture
Sincewegeneratedboththetaskinputandthetaskoutputinnaturallanguage,
we can optimize the LLM by following the common instruction fine-tuning and
causal language modeling paradigm. This process can be formulated as follows:
|y|
|     |     |     | (cid:88) | (cid:88) |     |      |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | ---- | --- | --- | --- | --- |
|     |     | max |          | log(P    | (y  | |x,y | ))  |     |     | (7) |
|     |     |     |          |          | Φ   | k    | <k  |     |     |     |
Φ
(x,y)∈Zk=1
| Here,xandy | denotetheKTLP-formattedinputandoutput,respectively,Z |     |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
denotes the training dataset, y k represents the k-th token of y, y <k denotes the
| token preceding | y   | , and Φ | represents | the | parameters |     | of M. |     |     |     |
| --------------- | --- | ------- | ---------- | --- | ---------- | --- | ----- | --- | --- | --- |
k

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 7
| However, | it  | is highly | resource-intensive |     | to fine-tune | every parameter |     | of an |
| -------- | --- | --------- | ------------------ | --- | ------------ | --------------- | --- | ----- |
LLM.Toutilizetrainingresourcesefficiently,weinsteadadoptedlow-rankadap-
tation (LoRA) [16]. As a parameter-efficient fine-tuning method, LoRA incor-
porates smaller trainable matrices for each layer of the model through low-rank
decomposition and the freezing of pre-trained model parameters, thereby en-
abling lightweight tuning. As a result, the original parameters can be preserved
in a frozen state while additional information in the fine-tuning dataset is effi-
ciently incorporated by training smaller matrices. The final fine-tuning process
| can be formulated |     | as follows: |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|y|
|     |     |     | (cid:88) | (cid:88) |         |     |     |     |
| --- | --- | --- | -------- | -------- | ------- | --- | --- | --- |
|     |     | max |          | log(P    | (y |x,y | ))  |     | (8) |
|     |     |     |          |          | Φ+Θ k   | <k  |     |     |
Θ
(x,y)∈Zk=1
Here, Θ represents the LoRA matrices, which are only updated during the fine-
tuning process.
3.3 Dataset
ToinvestigatetheeffectivenessofCLST,wecollecteddatapertainingtomath-
ematics, social studies, and science subjects. Table 1 lists detailed statistics for
each dataset.
Formathematicsdata,weselectedtheopenbenchmarkdatasetsNIPS34,Al-
gebra05, and Assistments09 (Assist09), which are used as standard benchmarks
for KT methods [45,57]. The NIPS34 dataset was sourced from the third and
fourth tasks of the NeurIPS 2020 Education Challenge. Gathered from the Eedi
platform, the data encompass students’ problem-solving histories for multiple-
choice math exercises [50]. The Algebra05 dataset was sourced from the EDM
challenge of the 2010 KDD Cup, comprising the responses of 13- to 14-year-old
students to algebra exercises [43]. The Assistments09 dataset contains student
response data on math exercises collected from the ASSISTments platform in
| 2009–2010 | [13]. |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Forsocialstudiesandscience,wegathereddatafromClasstingAILearning,
anonlineeducationplatformthatofferslearningmaterialsinarangeofacademic
| subjects | for K–12 | students. |            |     |               |                |     |     |
| -------- | -------- | --------- | ---------- | --- | ------------- | -------------- | --- | --- |
|          |          | Detailed  | statistics | of  | datasets used | in this study. |     |     |
Table 1.
|                     |     |                | NIPS34           | Algebra05Assist09Social |         | studiesScience |           |     |
| ------------------- | --- | -------------- | ---------------- | ----------------------- | ------- | -------------- | --------- | --- |
| # interaction       |     |                | 1,382,727607,014 |                         | 282,071 | 4,215,373      | 5,484,647 |     |
| # learners          |     |                | 4,918            | 571                     | 3,644   | 40,217         | 45,211    |     |
| # exercises         |     |                | 948              | 173,113                 | 17,727  | 14,168         | 29,795    |     |
| # KCs               |     |                | 57               | 112                     | 123     | 40             | 76        |     |
| Median interactions |     | per learner239 |                  | 580                     | 25      | 40             | 35        |     |
| Median KCs          | per | learner        | 26               | 54                      | 5       | 3              | 3         |     |

| 8 Jung       | et al. |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.4 Baseline | models |     |     |     |     |     |     |     |     |
In our comparative experiments, traditional, DL-based, and NLP-enhanced
| DL-based | KT models | were | selected | as  | baselines. |     |     |     |     |
| -------- | --------- | ---- | -------- | --- | ---------- | --- | --- | --- | --- |
AstraditionalKTmodels,weselectedtheBKT,itemresponsetheory(IRT),
and PFA models. BKT is a hidden Markov model that encodes learners’ knowl-
edge states with binary variables [9]. IRT models KT via logistic regression,
accounting for each student’s ability as well as the difficulty of each exercise
[23]. PFA is another logistic regression model that incorporates exercise diffi-
| culty alongside | each | student’s  |     | prior successes |      | and failures | [36].   |        |     |
| --------------- | ---- | ---------- | --- | --------------- | ---- | ------------ | ------- | ------ | --- |
| As DL-based     |      | KT models, |     | we selected     | deep | knowledge    | tracing | (DKT), | dy- |
namickey-valuememorynetworksforknowledgetracing(DKVMN),andatten-
tive knowledge tracing (AKT). DKT [38] is a standard RNN-based KT model
thatpredictsstudents’knowledgestateswithasingleLSTMlayer[41].DKVMN
[58] is a KT model that uses static memory to encode latent KCs and dynamic
memory to track student proficiency for the latent KCs [41]. AKT [15] is an
attention-mechanism-based KT model that improves predictive performance by
| incorporating  | context-aware |              |     | attention | with Rasch | model-based |       | encoding. |      |
| -------------- | ------------- | ------------ | --- | --------- | ---------- | ----------- | ----- | --------- | ---- |
| We implemented |               | NLP-enhanced |     | DL-based  |            | KT models.  | These | models    | ini- |
tialize exercise embedding vectors in DL-based KT models with encoded text
features of the KC name that corresponds to each exercise. which covers each
exercise Specifically, we used OpenAI1’s text-embedding-3-large to encode text
features, with the resulting KT models denoted as DKT , DKVMN , and
|     |     |     |     |     |     |     | text | text |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
AKT .
text
| 3.5 Experimental |     | settings |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
To guarantee the quality of the data, only interactions from students who
| responded | to more       | than | five    | exercises | were used. |          |          |            |      |
| --------- | ------------- | ---- | ------- | --------- | ---------- | -------- | -------- | ---------- | ---- |
| Because   | the objective |      | of this | study     | was to     | mitigate | problems | that arise | from |
cold-startsituations,wealternatelylimitedthenumberoflearnersinthetraining
set to 64, 32, 16, and 8. We executed each method five times with different
random seeds and reported the average outcomes. For the mathematics data,
20% of the learners were held out for the test set. For the social studies and
science data, we selected 1000 random learners as the test set for each subject.
| The selectionofa |     | basemodel |     | requirescareful |     | consideration.Among |     |     | existing |
| ---------------- | --- | --------- | --- | --------------- | --- | ------------------- | --- | --- | -------- |
generative LLMs, many do not provide accessibility to their model weights or
APIs. Furthermore, data security is a critical concern in the field of education,
necessitatingadditionaldiscussionabouttheuseofthird-partyAPIs(e.g.,Ope-
nAI). After careful consideration, we selected the instruction-tuned Mistral-7B2
[17].
Becauseitwasessentialtoevaluatepredictiveperformancewithlimiteddata,
we only considered the first 50 interactions per student in the experiment [48].
For other baseline hyperparameters, we adhered to the settings described by
| [48,21], as | their evaluation |     | protocols | were | similar | to our | own. |     |     |
| ----------- | ---------------- | --- | --------- | ---- | ------- | ------ | ---- | --- | --- |
1 https://platform.openai.com/docs/guides/embeddings
2 https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 9
| 4 Results | and | discussion |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
To evaluate the effectiveness of CLST from multiple perspectives, as well as ad-
dressthefourRQs,weconductedfourexperimentswiththefollowingobjectives:
1) compare predictive performance between CLST and the baseline models in
cold-start scenarios; 2) investigate the effectiveness of each component of the
CLST through an ablation study; 3) analyze learning trajectories using CLST;
and 4) compare predictive performance between CLST and the baseline mod-
els in cross-domain tasks. The following subsections discuss our experimental
results.
| 4.1 Predictive | performance |     |     | under | cold-start | scenarios |     |     |     |
| -------------- | ----------- | --- | --- | ----- | ---------- | --------- | --- | --- | --- |
We evaluated the predictive performance of CLST in cold-start scenarios in-
volving a limited number of students, with the training set sequentially reduced
from 64 to 8 students. All baseline models listed in Section 3.4 were chosen for
comparison in this experiment. We measured the area under the receiving oper-
atorcharacteristic(AUC)asanevaluationmetric.AUCisthemostwidelyused
indicator for evaluating KT performance, with higher scores indicating better
| performance      | [26]. |         |     |           |     |        |          |              |     |
| ---------------- | ----- | ------- | --- | --------- | --- | ------ | -------- | ------------ | --- |
| The experimental |       | results | are | presented | in  | Figure | 2, where | traditional, | DL- |
based, and NLP-enhanced models are represented by yellow, red, and purple
| curves, respectively, |      | whereas | CLST    | is   | represented  | by  | a green curve. |        |       |
| --------------------- | ---- | ------- | ------- | ---- | ------------ | --- | -------------- | ------ | ----- |
| As observed           | from | the     | figure, | CLST | outperformed |     | every baseline | model, | irre- |
spectiveofthesizeofthetrainingset.Furthermore,modelsutilizingNLPdemon-
strated superior overall performance in comparison to traditional and DL-based
methods.
| Table 2 | presents | detailed | quantitative |     | results | of  | the cold-start | experiments, |     |
| ------- | -------- | -------- | ------------ | --- | ------- | --- | -------------- | ------------ | --- |
where the best AUC score for each trial is bolded and underlined, while the
second-highest AUC score is underlined. CLST outperformed the second-best
modelbyupto24.52%,14.66%,12.31%,and8.71%foratrainingsetcontaining
8, 16, 32, and 64 students, respectively. Furthermore, when comparing perfor-
mance between CLST and the baseline models across different datasets, CLST
exhibited improvements of up to 13.69% on the NIPS34 dataset, 5.62% on the
Algebra05dataset,24.52%ontheAssist09dataset,9.62%ontheClasstingSocial
| Studies dataset, | and | 11.82% | on  | the Classting |     | Science | dataset. |     |     |
| ---------------- | --- | ------ | --- | ------------- | --- | ------- | -------- | --- | --- |
WecanthereforeprovidethefollowingresponsetoRQ:Inalldatasetsandall
cold-startscenarios,theproposedmethodoutperformedthebaselineKTmodels;
therefore,wecanconcludethatthecold-startprobleminKThasbeenmitigated.
| The cold-start |     | problem | has | been a | major concern |     | in the field | of KT | [60,53]. |
| -------------- | --- | ------- | --- | ------ | ------------- | --- | ------------ | ----- | -------- |
Previousstudieshavesuggestedmethodsthatutilizeadditionalinformationfrom
the exercise side (e.g., relations among KCs) or the learner side (e.g., language
proficiency) to address this issue [19]. However, these methods require effort
to acquire additional information that extends beyond each student’s problem-
solving history, which may be difficult to collect during the initial stages of
service.Incontrast,wesuggestanovelapproachtomitigatingthecold-startissue

10 Jung et al.
| Fig.2. Cold-start | performance | on each dataset. |
| ----------------- | ----------- | ---------------- |

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 11
|     | TSLC 536.0 736.0 | 156.0 166.0 556.0 166.0 207.0 | 227.0 986.0 286.0 486.0 117.0 | 475.0 755.0 175.0 695.0 | 975.0 085.0 785.0 406.0 |
| --- | ---------------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
txet
|              | 875.0 806.0 | 936.0 446.0 426.0 146.0 866.0 | 976.0 616.0 336.0 756.0 676.0 | 225.0 645.0 655.0 185.0 | 015.0 225.0 255.0 175.0 |
| ------------ | ----------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
| .stnemirepxe | TKA         |                               |                               |                         |                         |
decnahne-PLN
txet
NMVKD
| trats-dloc | 185.0 106.0 | 926.0 246.0 926.0 746.0 476.0 | 776.0 775.0 885.0 116.0 336.0 | 725.0 245.0 255.0 565.0 | 215.0 025.0 445.0 945.0 |
| ---------- | ----------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
CUA
txet
| fo  | egarevA 075.0 495.0 | 626.0 936.0 716.0 826.0 466.0 | 596.0 555.0 075.0 695.0 836.0 | 125.0 735.0 535.0 365.0 | 815.0 815.0 925.0 835.0 |
| --- | ------------------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
TKDTKANMVKDTKD
stluser
|     | 855.0 385.0 | 506.0 026.0 106.0 116.0 746.0 | 766.0 935.0 855.0 175.0 606.0 | 815.0 525.0 425.0 935.0 | 215.0 915.0 625.0 045.0 |
| --- | ----------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
deliateD
desab-LD
|     | 555.0 095.0 | 916.0 736.0 926.0 736.0 956.0 | 676.0 545.0 265.0 685.0 336.0 | 215.0 325.0 325.0 445.0 | 815.0 715.0 825.0 045.0 |
| --- | ----------- | ----------------------------- | ----------------------------- | ----------------------- | ----------------------- |
.2 elbaT
|     | 045.0024.0045.0445.0 065.0105.0565.0265.0 | 185.0985.0685.0475.0 595.0546.0706.0485.0 036.0574.0915.0026.0 146.0315.0935.0526.0 656.0555.0065.0076.0 | 486.0795.0685.0676.0 355.0974.0605.0055.0 385.0284.0905.0595.0 906.0794.0415.0606.0 456.0075.0525.0836.0 | 415.0674.0405.0425.0 235.0294.0805.0935.0 525.0005.0115.0945.0 945.0355.0915.0365.0 | 015.0294.0105.0515.0 915.0284.0405.0325.0 435.0494.0015.0935.0 445.0525.0025.0855.0 |
| --- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
AFP
lanoitidarT
TRI
TKB
stnedutS
|     | # 8 61 | 23 46 8 61 23 | 46 8 61 23 46 | 8 61 23 46 | 8 61 23 46 |
| --- | ------ | ------------- | ------------- | ---------- | ---------- |
50arbeglA
|     | tesataD | 43SPIN | 90tsissA | seidutS | ecneicS |
| --- | ------- | ------ | -------- | ------- | ------- |
laicoS

| 12  | Jung et | al. |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
by conceptualizing KT as language processing and leveraging the capabilities of
| generative   | LLMs. |       |     |     |     |     |     |
| ------------ | ----- | ----- | --- | --- | --- | --- | --- |
| 4.2 Ablation |       | study |     |     |     |     |     |
To investigate the effectiveness of each component of CLST in addressing the
cold-start issue, we conducted two experiments with the following objectives:
(1) comparison of performance with respect to exercise representations (2) to
| evaluate | the effectiveness |                | of fine-tuning | on           | model’s reliability. |                 |     |
| -------- | ----------------- | -------------- | -------------- | ------------ | -------------------- | --------------- | --- |
| 4.2.1    | Comparison        | of performance |                | with respect | to exercise          | representations |     |
MostexistingKTmodelsrepresentexerciseswiththeirdistinctiveidentityval-
ues,orIDs.IntheexperimentsconductedinSection4.1,allmodelsrepresenting
exercises using textual descriptions outperformed those using ID-based repre-
sentations.Inparticular,theproposedCLST,whichexpressesallinformationin
natural language, exhibited the highest performance in each cold-start scenario.
(Description-based)
(ID-based)
|     | Fig.3.    | Examples  | of the     | two methods | for representing | exercises. |         |
| --- | --------- | --------- | ---------- | ----------- | ---------------- | ---------- | ------- |
| We  | therefore | conducted | additional | experiments | to compare       | two ways   | of rep- |
resentingexercisesinKTLPformat:adescription-basedmethodthatrepresents
each exercise with the corresponding KC name, which is used in CLST, and the
conventionalID-basedapproach,whereintheIDofthecorrespondingKCisused
to represent each exercise. In this method, the ID of each KC is defined using

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 13
brackets in the format ’<id>’ and added as extra vocabulary. Figure 3 presents
| sample | representations |     | of an         | exercise    | using | both  | approaches. |             |             |
| ------ | --------------- | --- | ------------- | ----------- | ----- | ----- | ----------- | ----------- | ----------- |
|        | Comparison      |     | of predictive | performance |       | (AUC) | based       | on exercise | representa- |
Table 3.
tion method.
# Students
|     |     | Dataset |          | Method |       |       |       |       |     |
| --- | --- | ------- | -------- | ------ | ----- | ----- | ----- | ----- | --- |
|     |     |         |          |        | 64    |       | 32 16 | 8     |     |
|     |     |         | ID-based |        | 0.658 | 0.646 | 0.638 | 0.629 |     |
NIPS34
|     |     |     | Description-based0.6610.651 |     |       |       | 0.637 | 0.635 |     |
| --- | --- | --- | --------------------------- | --- | ----- | ----- | ----- | ----- | --- |
|     |     |     | ID-based                    |     | 0.659 | 0.631 | 0.548 | 0.584 |     |
Algebra05
Description-based0.7220.7020.6610.655
|     |     |     | ID-based |     | 0.691 | 0.661 | 0.661 | 0.668 |     |
| --- | --- | --- | -------- | --- | ----- | ----- | ----- | ----- | --- |
Assist09
Description-based0.7110.6840.6820.689
|     |     | Social | ID-based |     |     | 0.541 | 0.537 | 0.567 |     |
| --- | --- | ------ | -------- | --- | --- | ----- | ----- | ----- | --- |
0.600
|     |     | Studies | Description-based |     | 0.596 |     |     |     |     |
| --- | --- | ------- | ----------------- | --- | ----- | --- | --- | --- | --- |
0.5710.5570.574
|     |     |     | ID-based |     | 0.599 | 0.584 | 0.577 | 0.570 |     |
| --- | --- | --- | -------- | --- | ----- | ----- | ----- | ----- | --- |
Science
Description-based0.6040.5870.5800.579
| Table | 3   | presents | a comparison | of  | predictive | performance |     | with respect | to ex- |
| ----- | --- | -------- | ------------ | --- | ---------- | ----------- | --- | ------------ | ------ |
erciserepresentation.Inmostcases,the description-basedmethodwasobserved
| to outperform |     | the ID-based | method. |     |     |     |     |     |     |
| ------------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
Basedonextensiveexternalknowledgeacquiredduringthepre-trainingpro-
cess, the generative LLM is enabled to perform the KT task by considering the
relationshipsbetweenKCs.Ingeneral,KTmodelsthataccountforrelationships
between KCs are more effective at predicting student performance [6,27]. As
a result, when an exercise is represented based on its description, the external
knowledge of generative LLMs can be fully utilized, resulting in improved pre-
diction performance. Thus, the results of this experiment can be used to answer
RQ2 as follows: When aligning generative LLM with KT, it is more effective to
representeachexerciseusingadescription-basedmethodincold-startsituations.
| 4.2.2 | Effectiveness |     | of fine-tuning | on model’s |     | reliability |     |     |     |
| ----- | ------------- | --- | -------------- | ---------- | --- | ----------- | --- | --- | --- |
To investigate the effects of fine-tuning with KTLP-formatted data, we com-
pared the calibration plot outputs from an untuned model (mistral-7b-instruct-
v02, the backbone model selected for this study) and its fine-tuned counterpart.
Figure4showsthechangesinoutputcalibrationasaneffectoffine-tuningfor
each dataset. Each calibration plot is an illustration that compares the average
predicted value of a model’s output for each bin (x-axis) with the fraction of
positiveclasses(y-axis).Adiagonaldottedlineinthefigurerepresentstheideal
calibration that a model can achieve by predicting events based on the base
rate of occurrences [14]. Therefore, the output values are more reliable when
the output calibration is closer to the diagonal line. Overall, the untuned model
exhibited poor output calibration; in contrast, output calibration significantly

| 14  | Jung   | et al.  |     |                    |              |                 |     |     |
| --- | ------ | ------- | --- | ------------------ | ------------ | --------------- | --- | --- |
|     | Fig.4. | Changes | in  | output calibration | as an effect | of fine-tuning. |     |     |
improved as the number of learners in the KTLP dataset used for fine-tuning
| increased | to     | 16 and 64. |       |                    |              |           |     |          |
| --------- | ------ | ---------- | ----- | ------------------ | ------------ | --------- | --- | -------- |
| The       | output | of a KT    | model | is the probability | of correctly | answering |     | an exer- |
cise that covers a specific KC. This probability is often regarded as the mastery
level of that KC [38]. The output of a KT model can also be used for down-
stream tasks, such as personalized content recommendations [4], making output
reliability an essential priority [21]. The results of this experiment demonstrate
| enhanced     | reliability | when       | a model  | is fine-tuned | using KTLP-formatted |     |     | data. |
| ------------ | ----------- | ---------- | -------- | ------------- | -------------------- | --- | --- | ----- |
| 4.3 Learning |             | trajectory | analysis |               |                      |     |     |       |
To determine whether the method proposed in this study successfully predicts
students’ knowledge states, we visually analyzed the students’ understanding of
each KC in the process of solving exercises. Random selections of students from
thescience,socialstudies,andmathematicsdatasetsweremadeforthispurpose.
Among several datasets, students for the mathematics subject were selected at
| random  | from | Assistments09. |     |                       |        |          |          |     |
| ------- | ---- | -------------- | --- | --------------------- | ------ | -------- | -------- | --- |
| Figures | 5    | to 8 depict    | the | learning trajectories | of the | students | selected | for |
eachsubject.Heatmapsandlinegraphswereusedtovisualizehowthemastery
level for each KC changed as each student progressed through solving problems
for each subject.
| The | x-axis | of each | heat map | represents | the interaction | (KC | id, correctness) |     |
| --- | ------ | ------- | -------- | ---------- | --------------- | --- | ---------------- | --- |
at each time step, while the y-axis represents the KC of the questions that the

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 15
student primarily answered. In other words, the value of each cell indicates the
change in the mastery level for the corresponding KC after the interaction oc-
curred. The x-axis of the line plot (lower part of Figures) likewise represents
the interaction (KC id, correctness) at each time step, with the y-axis repre-
senting mastery level values; thus, each line represents the mastery level of the
corresponding KC.
Fig.5. Learning trajectories of student ’A’ in mathematics
The learning trajectory analysis revealed two observed facts. Initially, each
student’s knowledge state predicted by CLST was subject to change in accor-
dance with the correctness of the problem. In other words, when a student cor-
rectly or incorrectly answers a question about a specific KC, the mastery level
of the corresponding KC increases or decreases, respectively. For example, in
Figure 5, if the learner correctly answered the question about KC-92, the mas-
tery level for the corresponding KC increased, whereas if the learner answered
the question incorrectly, the mastery level decreased. Similarly, when questions
about KC-14 were correctly and incorrectly answered, the mastery level of the
corresponding KC (orange line in the figure) rose and fell accordingly.
Second,theCLSTpredictseachlearner’sknowledgestatebyconsideringrela-
tionshipsbetweenKCs.Forexample,Figure5depictsamathstudent’slearning
trajectory, showing changes in mastery levels for KC-13 (scatter plot), KC-14
(proportion),KC-20(percentof),KC-129(stemandleafplot),andKC-92(frac-

| 16 Jung | et al. |          |              |            |     |                |     |     |
| ------- | ------ | -------- | ------------ | ---------- | --- | -------------- | --- | --- |
|         | Fig.6. | Learning | trajectories | of student | ’B’ | in mathematics |     |     |
tion addition and subtraction). Among these, KC-13 and KC-129 are both con-
ceptsrelatedtoplots,andKC-14andKC-20aresimilarlyinterconnected.Upon
examining changes in the learners’ mastery levels, the trends within these pairs
of KCs exhibited mutually similar tendencies. In contrast, the mastery level for
| KC-92 exhibited |     | a different | pattern | compared            | to that | of the | other KCs.     |     |
| --------------- | --- | ----------- | ------- | ------------------- | ------- | ------ | -------------- | --- |
| Furthermore,    |     | when a      | learner | correctly responded |         | to an  | item regarding | KC- |
13, the corresponding mastery level increased along with that of the intuitively
related KC-129. Consequently, it is possible to infer that CLST estimates the
| learner’s | knowledge | state | by examining | relationships |     | between | KCs. |     |
| --------- | --------- | ----- | ------------ | ------------- | --- | ------- | ---- | --- |
Similarly,inthelearningtrajectoryofanothermathstudentshowninFigure
6, the mastery levels of related KCs, namely KC-25 (division of fractions) and
KC-92 (addition and subtraction of fractions), as well as KC-20 (percent of)
and KC-37 (conversion of fractions, decimals, and percents), displayed similar
trends.
| In the | social | studies | learning | trajectory shown | in  | Figure | 7, the mastery | level |
| ------ | ------ | ------- | -------- | ---------------- | --- | ------ | -------------- | ----- |
of related concepts KC-2 (national economy) and KC-39 (economic life and
choices) changed in a similar manner. For the science learner shown in Figure 8,
the mastery levels of related KCs—KC-59 (composition of earth materials) and
| KC-60 (history |     | of the earth)—changed |     | in similar | patterns. |     |     |     |
| -------------- | --- | --------------------- | --- | ---------- | --------- | --- | --- | --- |

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 17
| Fig.7. Learning | trajectories | of student ’C’ | in social studies |
| --------------- | ------------ | -------------- | ----------------- |
| Learning        | trajectories | of student     | ’D’ in science    |
Fig.8.

| 18          | Jung et | al.          |             |              |     |            |           |        |
| ----------- | ------- | ------------ | ----------- | ------------ | --- | ---------- | --------- | ------ |
| Ultimately, |         | the analysis | of learning | trajectories |     | yields the | following | answer |
to RQ3: The CLST plausibly predicts each student’s mastery level and also
| understands    | the | relationships | between | KCs.               |     |           |     |     |
| -------------- | --- | ------------- | ------- | ------------------ | --- | --------- | --- | --- |
| 4.4 Predictive |     | performance   |         | under cross-domain |     | scenarios |     |     |
Finally, we examined the performance of CLST in a cross-domain scenario. In
this experiment, the terms ‘domain’ and ‘dataset’ are used interchangeably [61].
To evaluate cross-domain performance, we selected two or more datasets for the
same subject. Specifically, we conducted an experiment using the mathematics
| subject | datasets | NIPS34,   | Algebra05, | and      | Assistments09. |            |              |     |
| ------- | -------- | --------- | ---------- | -------- | -------------- | ---------- | ------------ | --- |
| We      | tuned    | CLST with | samples    | from one | source         | domain and | subsequently |     |
evaluateditspredictiveperformanceontestsamplesfromanothertargetdomain.
For example, we evaluated the performance of the CLST tuned with samples
from the NIPS34 dataset (referred to as CLST(nips) in the figure below) on the
Algebra05 dataset. In addition, we evaluated the performance of DL-based KT
| models | and the | CLST trained | with    | the target      | domain | samples.     |     |     |
| ------ | ------- | ------------ | ------- | --------------- | ------ | ------------ | --- | --- |
|        |         |              | Results | of cross-domain |        | experiments. |     |     |
Fig.9.
| Figure | 9 shows | the predictive |     | performance | in  | the cross-domain | scenario. | Ac- |
| ------ | ------- | -------------- | --- | ----------- | --- | ---------------- | --------- | --- |
cording to the overall experimental results, CLST tuned with the target do-
main data, depicted in green, showed the highest performance. Nonetheless, the
CLSTtrainedonadifferentsourcedomaindataset,denotedbypinkdottedlines,
outperformed the DL-based KT models trained on the target domain, denoted
by purple dotted lines. In particular, in experiments with the Assistments09

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 19
dataset, the CLST tuned with different domains (such as algebra and NIPS)
demonstrated performance comparable to that tuned with the target domain.
In fact, the majority of current research in the field of KT has primar-
ily concentrated on domain-specific cases. However, real-world scenarios may
present obstacles to this approach, such as the inability to obtain data on stu-
dent–exerciseinteractions.Insuchcases,domain-specificmodelsmightnotfunc-
tioneffectivelyasaresultofinsufficientdata[7],makingtheevaluationofcross-
domain generalization capacity critical when deploying KT models in practice.
Ultimately, this experiment reveals the following answer to RQ4: Models
trained with the CLST are more generalizable across domains; therefore, when
buildinganITSinsituationswheredataisscarceandsufficientstudent–exercise
interactions cannot be obtained, the CLST can be a promising choice.
5 Conclusion
In this study, we developed the CLST, which utilizes a generative LLM as a
knowledge tracer. Most existing KT models are designed based on an ID-based
approach, which exhibits poor predictive performance in cold-start cases with
insufficient data. In contrast, the CLST demonstrates high performance even in
cold-start scenarios and exhibits robust cross-domain generalizability. For the
experiments, we collected data on the subjects of mathematics, social studies,
and science. Subsequently, by expressing the problem-solving data in natural
language, we framed the KT task as an NLP task and fine-tuned a generative
LLM using the formatted KT dataset.
TheexperimentresultsshowedthatCLSToutperformedthebaselinemodels
by up to 24.52% (mathematics), 9.62% (social studies), and 11.82% (science) in
situations where the number of learners in the training data was insufficient.
Furthermore, the ablation study showed that the description-based method ap-
plied in CLST, which represents each exercise with its description, achieved
better performance than the conventional ID-based method. Additionally, the
reliabilityexperimentconfirmedthatfine-tuningwithKTLP-formatteddataen-
hancesmodelreliability.Moreover,thelearningtrajectoryanalysisrevealedthat
the CLST plausibly predicts students’ mastery levels and understands the rela-
tionships between KCs. Finally, the cross-domain KT experiments verified that
CLST is generalizable across multiple domains.
The results of this study have practical implications, serving as a guide for
educational institutions and EdTech companies interested in fostering personal-
ized learning through the development of ITS. Additionally, it offers theoretical
implications by shedding light on strategies for leveraging generative LLMs in
the KT domain.
Although the effectiveness of CLST has been demonstrated in numerous ex-
periments, it has the potential to yield even higher predictive performance. For
example,theinclusionofadditionaltasksmayincreaseperformanceonthetarget
task [51]. Therefore, it is worthwhile to contemplate future research endeavors
to align generative LLMs as superior knowledge tracers by integrating a vari-

20 Jung et al.
ety of educational tasks related to KT (e.g., difficulty estimation, KC relation
prediction, etc.) into the fine-tuning process.
References
1. Abdelghani, R., Wang, Y., Yuan, X., Wang, T., Sauzéon, H., Oudeyer, P.: Gpt-
3-driven pedagogical agents for training children’s curious question-asking skills.
arxiv. preprint arXiv 2211 (2022)
2. Abdelrahman,G.,Wang,Q.:Knowledgetracingwithsequentialkey-valuememory
networks. In: Proceedings of the 42nd international ACM SIGIR conference on
research and development in information retrieval. pp. 175–184 (2019)
3. Abdelrahman,G.,Wang,Q.,Nunes,B.:Knowledgetracing:Asurvey.ACMCom-
puting Surveys 55(11), 1–37 (2023)
4. Ai, F., Chen, Y., Guo, Y., Zhao, Y., Wang, Z., Fu, G., Wang, G.: Concept-aware
deepknowledgetracingandexerciserecommendationinanonlinelearningsystem.
International Educational Data Mining Society (2019)
5. Bulut,O.,Yildirim-Erbasli,S.N.:Automaticstoryanditemgenerationforreading
comprehensionassessmentswithtransformers.InternationalJournalofAssessment
Tools in Education 9(Special Issue), 72–87 (2022)
6. Chen,P.,Lu,Y.,Zheng,V.W.,Pian,Y.:Prerequisite-drivendeepknowledgetrac-
ing. In: 2018 IEEE international conference on data mining (ICDM). pp. 39–48.
IEEE (2018)
7. Cheng, S., Liu, Q., Chen, E., Zhang, K., Huang, Z., Yin, Y., Huang, X., Su, Y.:
Adaptkt: A domain adaptable method for knowledge tracing. In: Proceedings of
theFifteenthACMInternationalConferenceonWebSearchandDataMining.pp.
123–131 (2022)
8. Colpo, M.P., Primo, T.T., de Aguiar, M.S.: Lessons learned from the student
dropout patterns on covid-19 pandemic: An analysis supported by machine learn-
ing. British Journal of Educational Technology 55(2), 560–585 (2024)
9. Corbett,A.T.,Anderson,J.R.:Knowledgetracing:Modelingtheacquisitionofpro-
ceduralknowledge.Usermodelinganduser-adaptedinteraction4,253–278(1994)
10. Devlin,J.,Chang,M.W.,Lee,K.,Toutanova,K.:Bert:Pre-trainingofdeepbidirec-
tional transformers for language understanding. arXiv preprint arXiv:1810.04805
(2018)
11. Dijkstra, R., Genç, Z., Kayal, S., Kamps, J., et al.: Reading comprehension quiz
generation using generative pre-trained transformers. In: iTextbooks@ AIED. pp.
4–17 (2022)
12. Emerson,A.,Min,W.,Azevedo,R.,Lester,J.:Earlypredictionofstudentknowl-
edge in game-based learning with distributed representations of assessment ques-
tions. British Journal of Educational Technology 54(1), 40–57 (2023)
13. Feng,M.,Heffernan,N.,Koedinger,K.:Addressingtheassessmentchallengewith
anonlinesystemthattutorsasitassesses.Usermodelinganduser-adaptedinter-
action 19, 243–266 (2009)
14. Gervet, T., Koedinger, K., Schneider, J., Mitchell, T., et al.: When is deep learn-
ing the best approach to knowledge tracing? Journal of Educational Data Mining
12(3), 31–54 (2020)
15. Ghosh, A., Heffernan, N., Lan, A.S.: Context-aware attentive knowledge tracing.
In:Proceedingsofthe26thACMSIGKDDinternationalconferenceonknowledge
discovery & data mining. pp. 2330–2339 (2020)

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 21
16. Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L.,
Chen, W.: Lora: Low-rank adaptation of large language models. arXiv preprint
arXiv:2106.09685 (2021)
17. Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., Casas,
D.d.l.,Bressand,F.,Lengyel,G.,Lample,G.,Saulnier,L.,etal.:Mistral7b.arXiv
preprint arXiv:2310.06825 (2023)
18. Jin, M., Wen, Q., Liang, Y., Zhang, C., Xue, S., Wang, X., Zhang, J., Wang, Y.,
Chen, H., Li, X., et al.: Large models for time series and spatio-temporal data: A
survey and outlook. arXiv preprint arXiv:2310.10196 (2023)
19. Jung, H., Yoo, J., Yoon, Y., Jang, Y.: Language proficiency enhanced knowledge
tracing. In: International Conference on Intelligent Tutoring Systems. pp. 3–15.
Springer (2023)
20. Kim, S., Kim, W., Jung, H., Kim, H.: Dikt: Dichotomous knowledge tracing. In:
Intelligent Tutoring Systems: 17th International Conference, ITS 2021, Virtual
Event, June 7–11, 2021, Proceedings 17. pp. 41–51. Springer (2021)
21. Lee,W.,Chun,J.,Lee,Y.,Park,K.,Park,S.:Contrastivelearningforknowledge
tracing. In: Proceedings of the ACM Web Conference 2022. pp. 2330–2338 (2022)
22. Li, L., Zhang, Y., Liu, D., Chen, L.: Large language models for generative recom-
mendation: A survey and visionary discussions. arXiv preprint arXiv:2309.01157
(2023)
23. Van der Linden, W.J., Hambleton, R.: Handbook of item response theory. Taylor
& Francis Group. Citado na pág 1(7), 8 (1997)
24. Liu, Q., Huang, Z., Yin, Y., Chen, E., Xiong, H., Su, Y., Hu, G.: Ekt: Exercise-
aware knowledge tracing for student performance prediction. IEEE Transactions
on Knowledge and Data Engineering 33(1), 100–115 (2019)
25. Liu,Y.,Yang,Y.,Chen,X.,Shen,J.,Zhang,H.,Yu,Y.:Improvingknowledgetrac-
ing via pre-training question embeddings. arXiv preprint arXiv:2012.05031 (2020)
26. Liu, Z., Liu, Q., Chen, J., Huang, S., Tang, J., Luo, W.: pykt: a python library
to benchmark deep learning based knowledge tracing models. Advances in Neural
Information Processing Systems 35, 18542–18555 (2022)
27. Lu, Y., Chen, P., Pian, Y., Zheng, V.W.: Cmkt: Concept map driven knowledge
tracing. IEEE Transactions on Learning Technologies 15(4), 467–480 (2022)
28. Malik,A.,Wu, M.,Vasavada,V.,Song,J., Coots,M., Mitchell,J., Goodman,N.,
Piech,C.: Generative grading: near human-levelaccuracy for automated feedback
on richly structured problems. arXiv preprint arXiv:1905.09916 (2019)
29. Mikolov, T., Sutskever, I., Chen, K., Corrado, G.S., Dean, J.: Distributed repre-
sentations of words and phrases and their compositionality. Advances in neural
information processing systems 26 (2013)
30. Nakagawa, H., Iwasawa, Y., Matsuo, Y.: Graph-based knowledge tracing: model-
ingstudentproficiencyusinggraphneuralnetwork.In:IEEE/WIC/ACMInterna-
tional Conference on Web Intelligence. pp. 156–163 (2019)
31. Neshaei,S.P.,Davis,R.L.,Hazimeh,A.,Lazarevski,B.,Dillenbourg,P.,Käser,T.:
Towardsmodelinglearnerperformancewithlargelanguagemodels.arXivpreprint
arXiv:2403.14661 (2024)
32. Ni,Q.,Wei,T.,Zhao,J.,He,L.,Zheng,C.:Hhskt:Alearner–questioninteractions
based heterogeneous graph neural network model for knowledge tracing. Expert
Systems with Applications 215, 119334 (2023)
33. Olney, A.M.: Generating multiple choice questions from a textbook: Llms match
human performance on most metrics. In: AIED Workshops (2023)
34. Pandey, S., Karypis, G.: A self-attentive model for knowledge tracing. arXiv
preprint arXiv:1907.06837 (2019)

22 Jung et al.
35. Pandey, S., Srivastava, J.: Rkt: relation-aware self-attention for knowledge trac-
ing. In: Proceedings of the 29th ACM International Conference on Information &
Knowledge Management. pp. 1205–1214 (2020)
36. Pavlik Jr, P.I., Cen, H., Koedinger, K.R.: Performance factors analysis–a new al-
ternative to knowledge tracing. Online Submission (2009)
37. Peng,C.,Yang,X.,Chen,A.,Smith,K.E.,PourNejatian,N.,Costa,A.B.,Martin,
C.,Flores,M.G.,Zhang,Y.,Magoc,T.,etal.:Astudyofgenerativelargelanguage
modelformedicalresearchandhealthcare.NPJDigitalMedicine6(1), 210(2023)
38. Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L.J., Sohl-
Dickstein, J.: Deep knowledge tracing. Advances in neural information processing
systems 28 (2015)
39. Sahebi, S., Cohen, W.W.: Community-based recommendations: a solution to the
cold start problem. In: Workshop on recommender systems and the social web,
RSWEB. vol. 60 (2011)
40. Shen, S., Liu, Q., Chen, E., Huang, Z., Huang, W., Yin, Y., Su, Y., Wang, S.:
Learning process-consistent knowledge tracing. In: Proceedings of the 27th ACM
SIGKDDconferenceonknowledgediscovery&datamining.pp.1452–1460(2021)
41. Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M., Chen, E.: A survey
of knowledge tracing: Models, variants, and applications. IEEE Transactions on
Learning Technologies (2024)
42. Sridhar, P., Doyle, A., Agarwal, A., Bogart, C., Savelka, J., Sakr, M.: Harnessing
llms in curricular design: Using gpt-4 to support authoring of learning objectives.
arXiv preprint arXiv:2306.17459 (2023)
43. Stamper, J., Niculescu-Mizil, A., Ritter, S., Gordon, G.J., Koedinger, K.R.: Al-
gebra | 2005-2006. development data set from kdd cup 2010 educational data
mining challenge (2010), find it at http://pslcdatashop.web.cmu.edu/KDDCup/
downloads.jsp
44. Su, Y., Liu, Q., Liu, Q., Huang, Z., Yin, Y., Chen, E., Ding, C., Wei, S., Hu,
G.:Exercise-enhancedsequentialmodelingforstudentperformanceprediction.In:
Proceedings of the AAAI conference on artificial intelligence. vol. 32 (2018)
45. Sun, J., Wei, M., Feng, J., Yu, F., Li, Q., Zou, R.: Progressive knowledge trac-
ing: Modeling learning process from abstract to concrete. Expert Systems with
Applications 238, 122280 (2024)
46. Tong, H., Wang, Z., Zhou, Y., Tong, S., Han, W., Liu, Q.: Hgkt: Introducing
hierarchicalexercisegraphforknowledgetracing.arXivpreprintarXiv:2006.16915
(2020)
47. Vie, J.J., Kashima, H.: Knowledge tracing machines: Factorization machines for
knowledgetracing.In:ProceedingsoftheAAAIconferenceonartificialintelligence.
vol. 33, pp. 750–757 (2019)
48. Wang, C., Ma, W., Zhang, M., Lv, C., Wan, F., Lin, H., Tang, T., Liu, Y., Ma,
S.: Temporal cross-effects in knowledge tracing. In: Proceedings of the 14th ACM
International Conference on Web Search and Data Mining. pp. 517–525 (2021)
49. Wang,Q.,Mousavi,A.:Whichlogvariablessignificantlypredictacademicachieve-
ment?asystematicreviewandmeta-analysis.BritishJournalofEducationalTech-
nology 54(1), 142–191 (2023)
50. Wang, Z., Lamb, A., Saveliev, E., Cameron, P., Zaykov, Y., Hernández-Lobato,
J.M., Turner, R.E., Baraniuk, R.G., Barton, C., Jones, S.P., et al.: Instructions
and guide for diagnostic questions: The neurips 2020 education challenge. arXiv
preprint arXiv:2007.12061 (2020)

Cold-start Mitigation in Knowledge Tracing by Aligning a Language Model 23
51. Wei, J., Bosma, M., Zhao, V.Y., Guu, K., Yu, A.W., Lester, B., Du, N., Dai,
A.M., Le, Q.V.: Finetuned language models are zero-shot learners. arXiv preprint
arXiv:2109.01652 (2021)
52. Wu,T.,Ling,Q.:Fusinghybridattentivenetworkwithself-superviseddual-channel
heterogeneousgraphforknowledgetracing.ExpertSystemswithApplications225,
120212 (2023)
53. Wu, Z., Huang, L., Huang, Q., Huang, C., Tang, Y.: Sgkt: Session graph-based
knowledge tracing for student performance prediction. Expert Systems with Ap-
plications 206, 117681 (2022)
54. Xu, J., Huang, X., Xiao, T., Lv, P.: Improving knowledge tracing via a heteroge-
neousinformationnetworkenhancedbystudentinteractions.ExpertSystemswith
Applications 232, 120853 (2023)
55. Yang, H., Hu, S., Geng, J., Huang, T., Hu, J., Zhang, H., Zhu, Q.: Heteroge-
neous graph-based knowledge tracing with spatiotemporal evolution. Expert Sys-
tems with Applications 238, 122249 (2024)
56. Yeung, C.K., Yeung, D.Y.: Addressing two problems in deep knowledge tracing
via prediction-consistent regularization. In: Proceedings of the fifth annual ACM
conference on learning at scale. pp. 1–10 (2018)
57. Yin,Y.,Dai,L.,Huang,Z.,Shen,S.,Wang,F.,Liu,Q.,Chen,E.,Li,X.:Tracing
knowledge instead of patterns: Stable knowledge tracing with diagnostic trans-
former. In: Proceedings of the ACM Web Conference 2023. pp. 855–864 (2023)
58. Zhang,J.,Shi,X.,King,I.,Yeung,D.Y.:Dynamickey-valuememorynetworksfor
knowledge tracing. In: Proceedings of the 26th international conference on World
Wide Web. pp. 765–774 (2017)
59. Zhang, M., Zhu, X., Zhang, C., Ji, Y., Pan, F., Yin, C.: Multi-factors aware dual-
attentionalknowledgetracing.In:Proceedingsofthe30thACMInternationalCon-
ference on Information & Knowledge Management. pp. 2588–2597 (2021)
60. Zhao, J., Bhatt, S., Thille, C., Gattani, N., Zimmaro, D.: Cold start knowledge
tracingwithattentiveneuralturingmachine.In:ProceedingsoftheSeventhACM
Conference on Learning@ Scale. pp. 333–336 (2020)
61. Zhao,S.,Fu,H.,Gong,M.,Tao,D.:Geometry-awaresymmetricdomainadaptation
formonoculardepthestimation.In:ProceedingsoftheIEEE/CVFConferenceon
Computer Vision and Pattern Recognition. pp. 9788–9798 (2019)
62. Zhao, W.X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y., Min, Y., Zhang, B.,
Zhang, J., Dong, Z., et al.: A survey of large language models. arXiv preprint
arXiv:2303.18223 (2023)
63. Zhou,H.,Gu,B.,Zou,X.,Li,Y.,Chen,S.S.,Zhou,P.,Liu,J.,Hua,Y.,Mao,C.,
Wu,X.,etal.:Asurveyoflargelanguagemodelsinmedicine:Progress,application,
and challenge. arXiv preprint arXiv:2311.05112 (2023)