JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 1
Data Augmentation for Sparse Multidimensional
Learning Performance Data Using Generative AI
Liang Zhang , Jionghao Lin , John Sabatini , Conrad Borchers , Daniel Weitekamp , Meng Cao , John
Hollander , Xiangen Hu , Arthur C. Graesser
Abstract—Learning performance data, such as correct or analytics.
incorrect answers and problem-solving attempts in Intelligent
Index Terms—Data Augmentation, Learning Performance
Tutoring Systems (ITSs), facilitate the assessment of knowledge
Data, Data Sparsity, Intelligent Tutoring System, Generative
masteryandthedeliveryofeffectiveinstructions.However,these
Artificial Intelligence
data tend to be highly sparse (80%∼90% missing observations)
in most real-world applications. This data sparsity presents
challengestousinglearnermodelstoeffectivelypredictlearners’ I. Introduction
future performance and explore new hypotheses about learning.
THEintegrationofAI-basededucationaltechnologiesinto This article proposes a systematic framework for augmenting
learningperformancedatatoaddressdatasparsity.First,learn- e-learningplatforms,combinedwithadvancedpedagogi-
ing performance data can be represented as a 3-Dimensional calstrategies,representsalandmarkadvanceinmoderneduca-
(3D) tensor with dimensions corresponding to learners, ques- tion [1]. This integration has profoundly transformed learning
tions, and attempts, effectively capturing longitudinal knowledge
and teaching strategies, making educational systems more
states during learning. Second, a tensor factorization method
adaptive for personalized learning, flexible for remote access,
is used to impute missing values in sparse tensors of collected
learner data, thereby grounding the imputation on knowledge scalable for resource distribution, and effective in improving
tracing tasks that predict missing performance values based educational outcomes [2]. An exemplary prototype of this
on real observations. Third, data augmentation using Genera- advancement is Intelligent Tutoring Systems (ITSs), which
tive Artificial Intelligence (GenAI) models, including Generative
provide personalized and adaptive instructions through hints,
Adversarial Network, specifically Vanilla Generative Adversarial
prompts, and other adaptive feedback to improve learner per-
Networks(GAN),andGenerativePretrainedTransformers(GPT,
specificallyGPT-4o),generatedatatailoredtoindividualclusters formance[3].TheeffectivenessofITSshasbeendemonstrated
of learning performance. We tested this systemic framework with considerable success in diverse areas such as science,
on adult literacy datasets from AutoTutor lessons developed technology, engineering, and mathematics, as well as in fields
for Adult Reading Comprehension (ARC). We found that: (1)
like reading and language learning [3]. Learning performance
tensor factorization outperformed baseline knowledge tracing
data, which include records of correct or incorrect answers
techniques in tracing and predicting learning performance,
demonstrating higher fidelity in data imputation, and 2) the and problem-solving attempts from learners using the ITS,
Vanilla GAN-based augmentation demonstrated greater overall are crucial for evaluating knowledge mastery, self-regulation,
stability across varying sample sizes, whereas GPT-4o based andothercharacteristicsthatsupportadaptiveinstructions[4],
augmentation exhibited higher variability, with occasional cases
[5].Forinstance,learners’correctandincorrectresponsescan
showing closer fidelity to the original data distribution. This
be leveraged within the learner model component of ITSs
framework facilitates the effective augmentation of learning
performance data, enabling controlled, cost-effective approach to facilitate learner modeling [6], [7]. This process involves
for the evaluation and optimization of ITS instructional designs trackinghistoricalperformanceandpredictingfutureoutcomes
in both online and offline environments prior to deployment, basedonknowledgecomponentsandconcepts,amethodology
and supporting advanced educational data mining and learning
referredtoasKnowledgeTracing(KT)[8].TheITScantailor
ManuscriptsubmittedonAugust4,2024.FirstrevisiononNov.23,2024; adaptive instructions, such as dialogue-based feedback, based
SecondrevisiononDec.31,2024.AcceptedonJan.2,2025. onpredictionsandassessments,offeringtargetedsupportwith
Liang Zhang, John Sabatini, and Arthur C. Graesser are with the
specific hints and prompts, especially when learners struggle
Institute for Intelligent Systems, University of Memphis, Memphis,
TN 38152, USA (e-mail: lzhang13@memphis.edu, jpsbtini@memphis.edu, or experience wheel-spinning [3].
art.graesser@gmail.com). In real-world educational practices, learning performance
John Hollander is with Arkansas State University, Jonesboro, AR, 72401,
data often suffers from data sparsity issues. Fig. 1 shows
USA(e-mail:jhollander@astate.edu).
Conrad Borchers, Daniel Weitekamp, and Meng Cao are with the how learners interact with an ITS, where their answers and
Human-Computer Interaction Institute, Carnegie Mellon University, Pitts- attempts at questions are recorded. The data matrix reveals
burgh,PA,15213,USA(e-mail:cborcher@cs.cmu.edu,weitekamp@cmu.edu,
many missing entries, indicated by the symbol “?”, high-
mengc2@andrew.cmu.edu).
Jionghao Lin is with the Faculty of Education, The University of Hong lighting the sparsity of the data. The real sparse scenarios
Kong, Hong Kong, PR China, also with the Human-Computer Interaction demonstrate inconsistent and incomplete data patterns, as
Institute,CarnegieMellonUniversity,Pittsburgh,PA,15213,USA,andalso
shown by the different colors within a single bar, representing
with the Centre for Learning Analytics, Faculty of Information Technology,
MonashUniversity,Clayton,VIC3800,Australia(e-mail:jionghao@hku.hk). various biased and unevenly distributed patterns. In contrast,
Xiangen Hu is with the Department of Applied Social Sciences, a well-structured and comprehensive dataset is expected to
Hong Kong Polytechnic University, Hong Kong, PR China (e-mail: xian-
encompass diverse scenarios, with each pattern maintaining
gen.hu@polyu.edu.hk).
5202
naJ
3
]GL.sc[
3v13651.9042:viXra

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 2
Fig. 1: Data sparsity issues in learning performance data in Intelligent Tutoring Systems.
relative quantities. This ensures a balanced and thorough instructional conditions have not been thoroughly explored
representation of the data, facilitating more robust analysis [19].Therefore,addressingdatasparsityiscrucialforavoiding
and modeling. Data sparsity is typically divided into two biased modeling, enabling more comprehensive evaluations
categories: (1) unobserved data resulting from unpresented of the learning process, and improving effective instructional
items (i.e., questions, problems) and limited learner responses support in ITSs.
orattempts[9],[10],and(2)insufficientlearningperformance Addressing data sparsity within ITSs represents a practical
patterns in the available empirical data [11], [12]. Insufficient yet challenging research area. Informed by advancements in
learning performance patterns specifically refer to the lack machine learning field [20], [21], tackling this issue typically
of quantity in the observed data required to model learning involves two interconnected and sequential strategies: data
processes effectively in this study. These patterns are often imputation and data augmentation. Data imputation focuses
defined by key learner-specific factors, such as initial learning on filling the gaps in missing data, thereby creating a more
ability (e.g., a learner’s baseline knowledge or proficiency complete dataset, which is crucial for accurate analysis and
before engaging with new content) and learning rate (e.g., the decision-making [22]. On the other hand, data augmentation
rate at which a learner improves accuracy or mastery through notonlyenrichesdatasetswherelearningperformancepatterns
repeated attempts) [12], [13]. These characteristics not only are rarely presented but also enhances the robustness of
help distinguish individual or group learning trajectories but analysis, modeling, and testing in ITSs, helping to mitigate
alsorevealunderlyingtrends,suchaswhetherhigh-performing the effects of sparsity on learner performance prediction [11].
learners exhibit slower incremental gains or if low-performing Despite the critical need, systematic efforts to address these
learners make rapid improvements due to starting from a datasparsityissuesintheITSsremainlimited,withfewstudies
lower baseline. By capturing and analyzing these patterns, focusingonthecomprehensivemanagementofsparsedata[9],
learner modeling can identify clusters of learners with similar [22].
performancecharacteristics,therebyenablingmorepreciseand Effective handling of missing data remains a challenge in
adaptive instructional strategies. Various reasons contribute educationaldataanalysis.Eventhoughgeneraldataimputation
to these data sparsity issues, including participant dropout methods (e.g., indicator or mean imputation [23], regression
from learning tasks [14], learner disengagement due to off- imputation [24], and multiple imputation [25]) have proven
task behavior [15] or gaming system [16], random data loss effective in the literature, they offer a cost-effective solution
from design and operation errors [17], and potential bias in thatavoidslabor-intensiveexperimentsbyleveragingobserved
the experimental groups [18]. These challenges are typical in datatoestimateunobserveddata.Thesemethodscapitalizeon
real-world settings. underlying patterns and characteristics [26], but they address
Data sparsity issues adversely affect the accurate modeling the missing data in a straightforward manner that fails to
of learning processes and assessment of learners’ knowledge capture the full complexity of the data structure. For example,
states, which in turn may compromise effective instructional indicator or mean imputation replaces missing values with a
support to learners, particularly those at risk [9], [11]. Specif- specified indicator or the mean of observed values. However,
ically, data sparsity could lead to biased or over-fitted KT this method may introduce bias by oversimplifying the com-
models, resulting in potentially misleading predictions of plexities of missing data [23]. Regression imputation predicts
learners’ future performance. Moreover, the insufficiency of missing values based on other observed data using regres-
learning performance data across a limited range of diverse sion models. Despite its utility, it often fails to capture the
patternsrestrictsthepotentialtocomprehensivelytestandfine- full spectrum of the underlying data structure [24]. Multiple
tune ITSs, particularly in cases where certain pre-designed imputation generates multiple datasets by imputing missing

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 3
valueswitha rangeofplausiblevaluesand thenaveragingthe effective tools for data augmentation, tailored to specific
results[25].Yet,itmaynotadequatelyaddresscomplex,high- learning needs.
dimensional correlations. Furthermore, data sparsity could in- The present study develops a systematic augmentation
fluence model prediction of learner performance. When using framework that integrates multidimensional modeling using
someKTmodelsinITSstopredictlearningoutcomes,suchas tensor factorization for data imputation and GenAI models
Performance Factor Analysis (PFA) and Bayesian Knowledge for data augmentation. This framework generates extensive
Tracing(BKT),uselogisticregressionandBayesiannetworks, learning performance data tailored to specific learning per-
respectively,topredictlearningoutcomes[27],[28].However, formance patterns, enhancing both data imputation and data
these models themselves are vulnerable to data sparsity and augmentation capabilities based on model-derived patterns
cannot account for the sequence effect of learning events, from real-world experimental datasets. The framework will be
though partially addressing data sparsity issues [9], [11]. tested with learning performance data from an example ITS
Therefore, to effectively address data sparsity and fully for adult literacy, using AutoTutor lessons for ARC [37]. Our
capture the data’s complexity, and improve the prediction of investigation is guided by the overarching Research Question:
learnerperformance,moreeffectivecomputationalapproaches “How can we develop a data augmentation framework to
that offer deeper insights are needed. In ITS research, tensor enhance sparse learning performance data and improve the
factorization, originating from recommendation techniques, scalability of learning performance data in the AutoTutor
has been used to recommend missing performance data based ARC?” This is explored through the following sub-questions:
on existing learner records [22]. This method leverages mul-
•
RQ1:Howdoestensorfactorizationperforminimputing
tidimensional relationships to enhance predictions and knowl- learnerperformancedatainARC,particularlyincompar-
edge representation by integrating three dimensions: learners, ison to baseline methods such as PFA, BKT, and Sparse
items (e.g., questions or learning materials), and temporal Factor Analysis Lite (SPARFA-Lite)?
factors (e.g., time or attempts) [22], [29]. Another source of
•
RQ2: How can GenAI models, including GAN specif-
inspiration stems from the advancements of GenAI models, ically Vanilla GAN) and GPT specifically GPT-4o), be
which are capable of generating new data based on patterns effectively and reliably utilized for data augmentation to
during training and have revolutionized data augmentation tailor individual performance patterns?
methodologies by being more flexible and powerful [30].
This study clarifies the selection of two fundamental types
One prototype is Generative Adversarial Networks (GANs),
ofGenAImodelsasthebasisforinitializingdataaugmentation
which can proficiently learn from existing data distributions
for sparse learning performance data. By employing both
and generate varied samples that extend beyond the original
GAN-based and GPT-based approaches, we aim to explore
dataset [31]. Since its development, the base architecture of
how these models can be utilized for data augmentation in
GAN, known as Vanilla GAN [32], has inspired numerous
learning engineering. Furthermore, we conduct a comparative
variants, such as Deep Convolutional GAN (DCGAN), Con-
analysis of these two types of GenAI models to address the
ditionalGAN(cGAN),andWassersteinGAN(WGAN).These
challenges posed by data sparsity.
variantshavebeenwidelyembracedfortheirabilitytoimprove
This proposed systematic augmentation framework has the
stability, handle specific types of data, and generate more
potential to emerge as a powerful tool for enhancing data
realistic samples, making them highly adaptable to various
richness and reliability. Firstly, it can perform data impu-
application domains. Another is the Generative Pre-trained
tation for sparse learning performance data, thereby enrich-
Transformer (GPT), which possesses reasoning abilities for
ing the data representation for more comprehensive learner
learning data distributions and can use both computational
modeling. Secondly, the generative models can increase the
and heuristic models to help sample larger datasets that align
diversity of individualized learner performance data, which
with the original data distribution [33]. The evolution of GPT
is essential for enriching learner modeling and ITS train-
models, from the initial versions such as GPT-2 and GPT-
ing. Practically, this study can lead to improved adaptation
3 to more advanced iterations like GPT-4o and GPT o-1,
and responsiveness within ITS environments by providing a
has brought increasingly sophisticated capabilities, including
broader dataset to fine-tune instructional feedback and in-
enhanced contextual understanding and greater fidelity in data
terventions. Enhanced data reliability and richness also en-
generation. These advancements highlight the potential of
able ITSs to make more accurate predictions of individual
GPT models to revolutionize data augmentation in domains
learnerneeds, ultimatelycontributingto personalizedlearning
requiring highly accurate and scalable solutions. Successful
paths, optimized feedback loops, and better overall learning
applications of GenAI models for data augmentation in ITSs
outcomes. By augmenting a wider range of learner behav-
include enriching mathematics student learning datasets with
iors, the framework supports the continuous improvement
multiple-choice questions [34], generating extensive student
of ITS instructional functions, ensuring these ITSs remain
behavioral data via GANs, from MOOC learning platforms
adaptable and effective across diverse learner profiles. Our
[35], and augmenting sparse learning performance data in
code and some results can be found at the following GitHub
readingcomprehension[12].Additionally,leveragingtheGPT
link:https://github.com/LiangZhang2017/3DGAI.
model has shown significant improvements in selecting ap-
propriate machine learning models and fine-tuning them for
predicting learning performance [36]. Building on the success
of GenAI models in ITSs, these models could become highly

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 4
II. RelatedWork tion with tensor factorization to incorporate temporal effects,
which significantly enhanced the accuracy of learner perfor-
A. IntelligentTutoringSystemsforAdultReadingComprehen-
mance predictions [22], [47]. Similarly, Sahebi et al. (2016)
sion
introduced Feedback-Driven Tensor Factorization (FDTF) to
Adult Reading Comprehension (ARC), essential for aca-
integrate sequences of students, quizzes, and attempts within
demic success and lifelong learning, can be enhanced through
a tensor framework, which again improved knowledge rep-
AI-based technologies that provide adaptive and personalized
resentation and performance predictions [29]. Doan and Sa-
solutions [37]. These AI-based technologies leverage educa-
hebi(2019)developedtheRanked-BasedTensorFactorization
tional data mining and learning analytics to assess student
(RBTF) model that uses tensor factorization to accommo-
performance (e.g., learner modeling), and to provide person-
date occasional forgetting of concepts and integrate biases
alized instruction tailored to individual learners (e.g., tutoring
related to students, problems, and time, thereby supporting
feedback, hints, nudges, and tailored recommendations for
a predominantly positive learning trajectory [48]. Over time,
readingmaterialsandcomprehensionexercises)[38],[39].For
various tensor factorization techniques have been developed
instance, the latest advances in natural language processing
to enhance the prediction accuracy and impute sparse data in
and machine learning have enabled digital textbooks to use
educationalsettings[49],[50].Thesedevelopmentsunderscore
their content and structure as a knowledge base for “smart”
the capability of tensor factorization to not only enhance
functionalitieslikeautomatedknowledgecompilation,adaptive
prediction accuracy but also perform tensor-based imputation,
navigation and presentation, and targeted content recommen-
effectively filling in missing values in sparse tensors. Tensor-
dations [40]. Another instance is the AutoTutor developed for
based of learning performance data preserves the “natural
ARC, which is investigated in the present study [37]. The
representation”ofsynchronousandsequentiallearningevents,
AutoTutor ARC employs the trialogue design, which includes
whichisessentialforaccuratelytracingandpredictinglearner
one human learner and two computer agents (virtual tutor
performance and for improving the imputation of missing
andvirtualcompanion)[37].Thissystemfacilitatesinteractive
values [51]. This process also allows for the efficient decom-
learningthroughathree-partyconversationthatassesseslearn-
position of interactions across different dimensions, enabling
ers’ responses, provides feedback, and corrects misconcep-
deeper analysis and further enriching the dataset’s utility
tions based on an Expectation-Misconception Tailored (EMT)
[48]. The method’s alignment with recommendation systems
mechanismthatattemptstocovergoodanswers(calledexpec-
highlightsitsutilityinidentifyingperformancesimilaritiesand
tations) and correct bad answers (called misconceptions) [41].
dependencies among learning events, making it a cornerstone
Thetutoringsessionconcludesoncealllessonexpectationsare
in educational data mining.
met. Other ITSs, such as DSCoVAR for vocabulary learning
[42], and ITSS for reading comprehension instruction through
C. Generative AI for Augmenting Sparse Educational Data
structurestrategytraining[43],arealsonoteworthybutarenot
The advent of GenAI technologies has revolutionized the
detailed here.
field of data augmentation, particularly in domains burdened
Recently, ITSs for ARC have increasingly incorporated ad-
by sparse and imbalanced datasets [52]. GenAI models have
vanced AI technologies, particularly GenAI. Large Language
providedgroundbreakingwaystosynthesizerealisticandexist-
Models (LLMs) have already been used to develop summary
ing data by capturing complex intrinsic patterns, distributions
gradingmodelsforintelligenttextbooksthatprovidereal-time
and characteristics, effectively enhancing dataset robustness
formative feedback and assess comprehension [44]. GenAI
for training machine learning models [32]. At this point,
models, including GAN and GPT, have been used to tackle
GenAIeffectivelyaddressesscalabilitychallengesinbothhigh
sparse data challenges in reading comprehension, thereby
and low-dimensional simulation data. It can simulate data
enhancing personalized educational technology in ITSs [12].
on a larger scale and generate tailored scenarios, facilitating
Furthermore, the use of LLMs to generate high-quality, per-
informeddecision-makingunderuncertaintyconditionsarising
sonalizedreadingmaterialsunderscoresthepotentialforfuture
from sparse datasets [53]. Many successful applications in
ITS designs to improve reading comprehension skills [45],
other fields have also exemplified the potential for educational
[46]. These AI advancements have revolutionized ITS devel-
data. Mariani et al. utilized GANs to balance imbalanced im-
opment from their design and creation to learning analytics
ageclassificationdatasets[54],whileFrid-Adaretal.increased
and modeling in ARC.
the size and diversity of medical imaging datasets through
synthetic data augmentation [55]. Huang et al. transformed
B. Tensor-based Imputation for Sparse Performance Data images for image-translation tasks, including day-to-night and
The increasing prevalence of sparse learning performance vice versa, using GANs [56]. In educational settings, GANs
datafromITSsnecessitatesrobustimputationmethodstohan- have synthesized additional data from sparse datasets in open
dle missing information effectively. Tensor-based imputation university learning analytics [57], illustrating their broad po-
has emerged as an important technique due to its ability to tential for improving learning performance data in ITSs.
maintain the multi-dimensional nature of learning data and TheGPTisastate-of-the-artGenAImodelknownforitsex-
to preserve intrinsic relationships across dimensions such as ceptionalabilityinhuman-liketextgenerationandperforming
learners, questions, time or attempts [13], [22], [29]. reasoning tasks with unprecedented accuracy [58]. ChatGPT
Pioneering implementations of tensor-based methods in- represents a significant advancement in AI, driving revolu-
cludeThai-Ngheetal.(2011),whoextendedmatrixfactoriza- tionary shifts in its application within education. It has been

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 5
TABLE I: Summary of the AutoTutor ARC Lessons Dataset.
Lesson Topic DifficultyLevel #Transactions #Learners #Questions #Max.Attempt
Medium 1160 107 10 9
Lesson1 PersuasiveText Easy — — — —
Hard 854 96 11 8
Medium 1527 118 9 9
Lesson2 CauseandEffect Easy 450 48 10 5
Hard 838 64 10 9
Medium 1444 140 11 5
Lesson3 ProblemsandSolutions Easy — — — —
Hard 891 124 8 5
Medium 442 46 10 7
Lesson4 InferencesfromTexts Easy 102 16 9 2
Hard 235 25 10 7
instrumental in enhancing instructional feedback [59], [60], Texts” (Lesson 4). Each lesson includes 8 to 11 multiple-
boosting student engagement [61], generating questions [62], choicequestionstotestlearners’readingcomprehensionskills.
simulatinglearningscenarios[63],andprovidingpersonalized Learnersstartwithmedium(M)difficultylevelmaterials,then,
learning experiences [45]. In parallel, recent work highlights depending on their performance, either progress to the hard
ChatGPT’s effectiveness in fostering self-regulated learning (H) level or move down to the easy (E) level. The “Max.
[64], GPT o-1’s potential for advancing higher-order thinking Attempt” column in Table I defines the baseline setting for
in education [65], and GPT-based methods that underpin the maximum number of attempts across all selected question
dialogue-drivenITSs[46].Notably,therehasbeentremendous records. For example, a sample learning record from the topic
progress in data augmentations in ITSs. For instance, Liu “Persuasive Texts” involve a anonymous learner identified as
et al. [66] employed ChatGPT to enrich open-ended student “CSU00032” (marked as Anon.Student.Id). When asked the
responses in computer science with knowledge-guided code question“Whatisthetopicofthearticle?”regardingthemain
for short programming tasks. Zhang et al. [12] demonstrated idea of a provided passage, the learner selected the option
ChatGPT’s capability in learning the distribution of learning “Minimum wage” by clicking the choice button and received
performance data tailored to individual patterns and selecting a“CORRECT”assessment(asevaluatedbyAutoTutor)onthe
appropriate machine learning models for data augmentation firstattempt.The“Transactions”columnineachlessondataset
in reading comprehension. Further studies have confirmed recordsthetotalnumberofobservations,servingasthesample
that ChatGPT can predict learning performance by encoding size for each lesson. Note that: 1) It is rare for learners to
datasets, selecting and fine-tuning models, and decoding out- engagewiththeeasylevelinLesson1and3,sincethemajority
putsasestimatedprobability-basedlearningperformance[36]. can advance to the hard level; and 2) There are instances of
All these related works demonstrate the potential of GenAI dropout among learners during transitions. For further details
modelsfordataaugmentationinITSs.Bygeneratingsynthetic on the experiments conducted, see the reference paper [67].
yet realistic examples, these models can significantly expand
thedepthandbreadthoflearningperformancedata,makingit IV. Methods
more comprehensive and representative. This enables a more
This section describes our data augmentation framework to
accurate assessment of learners’ progress and more robust
enhance the learning performance data for AutoTutor ARC as
training of AI systems that can adapt to various educational
well as the procedural methods used for its construction.
challenges and learner profiles.
A. The Systematic Augmentation Framework
III. Dataset
The systematic augmentation framework, shown in Fig. 2
Four lesson datasets1 were selected from a total of 29
integratestheconstructionofa3Dtensortorepresentlearning
AutoTutor ARC lessons used in an adult literacy intervention
performancedatawithsubsequenttensor-basedimputationand
program involving 252 participants. The intervention program
augmentation, effectively enriching these data. Initially, the
spanned from January 2015 to December 2016, with each in-
framework structures learning performance data from real-
terventionlastingapproximatelyfourmonths.Ethicalapproval
world learner-ITS interactions into a three dimensional tensor,
wasobtainedfromtheInstitutionalReviewBoard(IRB)under
encompassinglearners,questions,andattempts.Theentriesin
theapprovalnumberH15257.AsillustratedinTableI,thefour
this tensor represent learning performance values, quantified
lessons sourced from the “Stories and Texts” series within the
asbinaryvalues(1forcorrectand0forincorrect).Asdepicted
adult reading comprehension program cover topics including
in Fig. 2, the 3D tensor includes filled cubes that repre-
“PersuasiveTexts”(Lesson1),“CauseandEffect”(Lesson2),
sent recorded learning performance values and transparent
“Problems and Solutions” (Lesson 3), and “Inferences from
cubes that indicate sparse or missing values. Subsequently,
tensor-based imputation using Tensor Factorization converts
1AutoTutorMoodelWebsite:https://sites.autotutor.org/;AdultLiteracyand
AdultEducationWebsite: https://adulted.autotutor.org/ the sparse tensor into a densified form. The densified tensor
providesinvaluable insightsinto diverselearning performance

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 6
Fig. 2: The systematic augmentation framework for learning performance in Intelligent Tutoring System.
patterns, enabling the segmentation of the tensor into sub- Learners’ sequential interaction with questions affects their under-
tensorsbasedonthesedistinctpatterns(thiswillbedetailedin standing,comprehension,andperformance;forexample,onequestion
subsequent sections). GenAI models, such as GAN and GPT, might facilitate comprehension and performance of a subsequent
question [69], [70] and there may be recency effects where perfor-
are then used to simulate additional data samples, enriching
mance in recent items may be weighted higher on learner mastery
the original dataset based on specific learning performance [50], [71]. (d) Maximum Attempt Assumption: Assume a theoretical
patterns.Thisscalablesimulationprocessultimatelygenerates maximum number of attempts a learner might need, highlighting
a more comprehensive dataset that incorporates both imputed the importance of evaluating comprehensive learning states through
and augmented data. repeated attempts. (e) Similarity in Learning for Individual Learn-
The workflow framework can be formalized as follows: ers: Assuming a common relevance and utility in the mode of
knowledgeacquisitionamonglearners,itbecomespossibletopredict
logs →T →T →T (1) knowledge mastery based on similarities in their individual learning
learning sparse dense augmented
pathways [51]. (f) Probability-based Prediction: Predicted learning
where logs learning represents the logs of learning performance (in- performance is represented as a probability from 0 to 1, indicating
cludinglearner,questions,attempts,andactuallearningperformance the likelihood of knowledge mastery.
values). These logs are structured into sparse tensor T . This
sparse
sparse tensor is then processed through tensor-based imputation
techniquestoyieldT ,adensifiedtensorthathatfillsinmissing C. Tensor-based Imputation
dense
or sparse values to create a more complete dataset. The densified WemodelthesparsetensorT throughfactorizationintotwo
sparse
tensor is then used to further augment the tensor into T
augmented
, lowerdimensionalcomponents:(1)afactormatrixU ofsizeU×K,
scalingdatassamplebyindividualizedlearningperformancepatterns. whichcapturesthelatentlearning-relatedfeaturesofU learners,such
as initial learning abilities and learning rates, where K is the total
numberofthesefeatures;and2)alatenttensorV ofsizeK×M×N,
B. Constructionof3DTensorforLearningPerformanceData
representing learner knowledge in terms of K latent features across
Consider the data produced by a population of learners working M attempts on N questions. The approximated tensor T is is
in an ITS. The data consist of a set of U learners, represented by computed as follows: dense
{l ,l ,l ,··· ,l }, who engages with a sequence of N questions,
1 2 3 U
denoted by {q 1 ,q 2 ,q 3 ,··· ,q N }. Each question in this sequence T dense ≈U×V+b l +b a +b q +ε (2)
permits up to M attempts, represented by {t ,t ,t ,··· ,t },
allowing individual learners multiple opportunitie 1 s to 2 re 3 spond. M The where b l , b q , and b a represent the biases from learners, questions,
T ∈ RU×N×M captures these interactions, where the entry and attempts, respectively, and ε denotes a global bias. During
sparse tensorfactorization,thesigmoidfunctionisappliedtonormalizethe
τ inT recordstheperformanceoflearnerl onquestionq
uij sparse u i outputofestimatedperformancevalues,ensuringoutputsarebounded
at the attempt a , where the u ∈ (1,2,··· ,U), i ∈ (1,2,··· ,N),
j between0and1.Themodelalsoincorporatesarank-basedconstraint,
j ∈ (1,2,··· ,M). Within the AutoTutor ARC context, the entry
which promotes a trend of monotonic knowledge acquisition across
variableτ ={0,1,NaN},where1indicatesacorrectanswer,0
uij successive attempts by learners, while still allowing for potential
signifies an incorrect answer, and NaN donates unobserved values.
forgettingorslipping[48].Theobjectivefunctionincludestermsfor
The construction of the 3D tensor is guided theoretically by the
mean squared error to measure the discrepancy between observed
following assumptions: (a) Hierarchical Knowledge Representation:
values and predictions, and regularization terms for the decomposed
Each question involves distinct knowledge components or concepts,
including both procedural and declarative types; these knowledge components (the learner feature matrix U and the latent tensor V
and various biases) to mitigate overfitting, along with a rank-based
componentsmayalsobesharedacrossdifferentquestions[49],[68].
constraint. Optimization is carried out using stochastic gradient de-
(b) Latent Knowledge Relations: The specific knowledge embedded
scenttominimizetheobjectivefunction,iteratinguntilconvergence.
within each question is crucial for mastery, and the unique yet
interconnected knowledge across questions create a comprehensive Ultimately, the resulting T dense functions as a probability-based
filled tensor.
network of logic and procedures during the knowledge acquisition
TheTensorFactorizationmethodthusenablesustoconstructand
process [8], [50]. (c) Sequence Effects in Performance Interactions:
assess different multidimensional models for learning performance

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 7
that facilitate data imputation for comprehensive modeling of the a indicates the learner’s initial learning ability or prior knowledge,
learning process. We explored three different baseline models that and b quantifies the rate at which the learner acquires knowledge
will ultimately be compared with our proposed model. (a) Bayesian through practice. We then utilized K-means++ algorithm [76] to
Knowledge Tracing (BKT): BKT uses a Hidden Markov Model to clusterthedistributionoftheseparameters(aandb)amonglearners,
dynamically assess and predict a learner’s knowledge state (repre- which assists in identifying distinct individual learning performance
sentedasbinarystatesof“known”and“unknown”),withadjustments patterns.
basedontheirresponsestoquestionswhileconsideringprobabilities
oflearning,guessingandslipping[72];here,italsoinitiallyintegrates
VI. DataAugmentationbasedonGenerativeModels
both student-specific and skill-specific parameters to effectively ac-
We investigated two generative AI models, GAN and GPT, to
count for individual learner variability and the hierarchical nature
generate learner data that manifests particular performance patterns,
of skills [28], [72]. (b) Performance Factor Analysis (PFA): PFA
and thereby enable scalable sampling.
utilizeslogisticregressiontoestimatetheprobabilityofthelearner’s
performanceonthequestion,factoringinindividuallearningability, Generative Adversarial Networks. In this study, we employ
the Vanilla Generative Adversarial Network (GAN) [32], which
skill-related features (e.g., difficulty), and the learner’s previous
representsthefoundationalarchitectureintheGANfamily.Itconsists
success and failures [27]. (c) Sparse Factor Analysis Lite (SPARFA-
Lite):SPARFA-Lite,astreamlinedversionofSparseFactorAnalysis,
oftwocomplementarynetworks:agenerator(G)andadiscriminator
uses matrix completion techniques to efficiently analyze graded
(D), both implemented using fully connected (dense) layers [31],
[32]. The generator is designed to produce simulated data samples
learnerresponsesandpredictperformancebydeterminingtheoptimal
from initialized random noise, typically sourced from a Gaussian
number of knowledge components, offering enhanced computational
distribution.Itsoutputiscraftedtobecompatiblewiththeinputfrom
speed over the initial Sparse Factor Analysis [73]. The choice of
the individualized learning performance pattern as synthetic sample
these baseline models was guided by two primary criteria. First, we
data.Thediscriminator’sroleistodeterminewhethertheaugmented
prioritizedinterpretability.Complexdeepknowledgetracingmodels,
datasamplesarerealorsyntheticbycomparingthemwithactualdata
while potentially more accurate, were excluded due to their lack
samples (original learning performance distribution). Concurrently,
of transparency, which could hinder clear explanation and analysis
of results. Second, although prediction accuracy was an important the G(·) is trained to progressively reduce the difference between
the distributions of the real and augmented data through iterative
consideration, it was not our primary focus. This study emphasizes
addressingdatasparsityissues,aimingtoprovideactionableinsights
tuning.ThetrainingcostsforbothD(·)andG(·)aredictatedbythe
intoeffectivelyhandlingsparsedata.Whilealternativemethodsmay
objective function V(G,D), defined as follows [32]:
enhance prediction accuracy, many do so by relying on sparse data
maxminV(G,D)=E [logD(T ,T )]+
withoutdirectlyaddressingtheunderlyingsparsitychallenges,which D G simulate real simulate (4)
falls outside the scope of this investigation. Enoise[log(1−D(G(RandomNoise)))]
where the T represents the real performance sample input to
V. IdentificationofLearningPerformancePatternsby G(·),andT real denotestheoutputG(·),simulatingrealdatafor
simulate
Clustering assessmentbyD(·).ThetermE [·]calculatestheexpectation
simulate
Tomakedataaugmentationadaptivetoindividuallearningperfor-
oflog-probabilitythatD(·)correctlyidentifieswhetherdataisrealor
mancepatterns,wefirstidentifythesepatternsbyclusteringbasedon
simulated,whileE
noise
[·]measurestheexpectationoflog-probability
thesimilarityofeachlearner’sperformanceacrossdifferentattempts
thatD(·)correctlyrejectsgenerateddataasfake.Inpracticalimple-
mentations,thisVanillaGAN-basedaugmentationapproachtakesthe
at specific questions.
pro T b h a e bi m lit a y t - r b ix as s e l d ice kn Ω o q w n l , ed ex g t e ra s c t t a e t d es fr a o s m so t c h ia e te T d d w en i s th e , t e h n e ca p p e s r u fo la rm tes an th c e e m pe a r t f r o i r x m s a l n ic c e e Ω fo q r n l , ea w rn h e ic r h s a re c p ro re ss sen al t l s a th tt e em p p ro ts ba f b o i r lit t y h - e ba n se th d q le u a e r s n ti i o n n g
i o l n lus th tr e at n es th ou q r ue a s p t p io ro n ac q h n , to fo i r de a n ll ti U fyin le g ar l n ea e r r n s in ov g e p r e M rfor a m tt a e n m c p e ts p . a E tte q r . n 3 s b q n as , e a d s v t e h c e to r r e s al d T ata re f a r l o . m By Ω t q r n ai , n t i h n e g l t e h a e rn V e a r n d il i l m a e G ns A io N n o c n an th b e e le s a c r a n le e d r- ,
enabling synthetic augmentation of the existing data. The Vanilla
withinΩ .Thematrixcanberepresentedasasequenceofvectors
qn GANundergoestrainingovermultipleepochs(N=3,000),alternating
{L ,L ,L ,··· ,L },whereeachL aggregatestheuth learner’s
1 2 3 n u updates between the generator and discriminator. Each epoch begins
performance across all attempts for the specified question. The
withnoiseinputforthegenerator,whichproducessyntheticdataata
performance distribution for each learner vector is assumed to be
predefinedsamplesizeforlearners.Thediscriminatoristhentrained
modeled by function G(·), with the associated set of parameter
firstonrealdata,labeledas1,andthenonsyntheticdata,labeledas0,
vectorsdepictedas{ϑ ,ϑ ,ϑ ,··· ,ϑ }.Thefluctuationsinthese
1 2 3 M withanaveragelosscalculatedtoassessitsaccuracyindistinguishing
model parameters indeed reflect individual differences in learning
realfromsyntheticsamples.Subsequently,thegeneratoristrainedby
performance patterns by quantifying the uncertainties within the
propagatingthegradientfromthediscriminatorbacktothegenerator.
evolving knowledge states for each learner.
Specifically, the generator takes a random noise vector as input and
Ωqn =
 

L
L
L
L
.
.
.
U
1
2
3
 

⇒
 

G
G
G
G
C
1
2
3
(
(
(
(
.
.
.
L
L
L
L
1
2
3
U
)
)
)
)
⇒
 

ϑ
ϑ
ϑ
ϑ
.
.
.
U
1
2
3 ⇒
 

C
C
C
C
l
l
l
l
u
u
u
u
s
s
s
s
.
.
.
t
t
t
t
e
e
e
e
r
r
r
r
C
1
2
3
(3)
g
d
s
i
c
t
s
h
c
l
e
i
a
s
e
o
n
c
s
c
r
o
e
s
r
e
d
r
m
i
i
a
f
m
i
i
s
y
t
p
n
e
c
i
i
u
d
n
n
s
r
t
i
i
a
g
e
c
m
s
t
d
a
y
o
t
i
t
h
n
r
n
i
b
n
e
t
a
a
e
h
g
t
s
v
s
e
o
e
y
a
t
w
r
d
i
n
l
’
c
u
s
h
t
o
h
a
e
d
n
t
o
e
t
a
e
h
t
u
h
t
s
i
e
a
t
c
o
r
p
,
t
w
h
d
u
t
w
h
i
a
t
s
e
e
t
h
a
ff
l
i
s
o
d
c
e
y
a
s
a
h
c
s
n
s
t
t
a
t
i
i
r
h
s
v
e
f
i
e
o
e
a
s
t
t
r
l
l
h
i
y
.
r
c
e
e
t
T
n
i
a
h
d
t
h
l
e
a
“
f
i
o
e
t
s
f
a
o
d
s
r
i
y
o
s
f
a
t
n
a
l
o
n
s
a
t
k
”
d
h
c
e
t
e
h
h
t
.
a
h
t
i
e
T
i
s
e
e
c
s
v
h
d
i
d
e
e
g
i
d
d
i
s
n
s
a
c
g
c
s
t
b
r
e
a
r
i
y
n
i
m
a
.
m
e
m
i
r
p
U
i
n
a
n
r
i
a
s
t
o
n
a
o
i
t
i
b
n
t
o
r
m
o
a
’
g
r
s
r
.
b
iz
i
l
i
T
t
l
o
n
i
h
i
n
h
t
t
s
i
g
y
o
e
s
s
In this study, we employed a power law function for G(·) to loss, the generator’s parameters are updated via backpropagation
model the relationship between learners’ performance values and using gradient descent. Over successive epochs, the generator learns
their number of attempts, drawing on the learning curve theory to produce increasingly realistic data that aligns closely with the
proposed by Newell and Rosenbloom [74]. This theory links error statistical patterns of the real learner performance data. Ultimately,
rates to practice amounts and supports the power law’s use [74]. thefinelytunedgeneratorproducesscalableaugmentedsampledata.
The power law learning curve is particularly valued for its robust Generative Pre-trained Transformer. This study highlights the
fit and interpretable parameters, which has been widely recognized use of GPT-4o for data augmentation, which involves capturing
in educational and training research [75]. In the power-law formula the actual data distribution and generating simulated data samples
Y = aXb, Y represents learning performance, quantified as the through a strategic, prompt-based process. This process, also de-
probability of producing correct answers, while X denotes the tailed in Zhang et al. [12], [36], involves three main procedures:
numberofattemptstorespondtothecurrentquestion.Theparameter encoding,whichconvertsnumericallearningperformancevaluesinto

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 8
TABLE II: Example prompt strategy for augmenting sparse learning performance using GPT-4o.
UserInput GPT-4oOutput
User:HelloChatGPT,yourexpertiseasanAIlanguagemodelmakesyouidealfor GPT-4o:Togeneratesyntheticlearningperformancedataforindividual
assistingmeingeneratingsyntheticlearningperformancedataforindividuallearners. learners,wewill:
Theprimarytaskinvolvesathoroughanalysisoftheexistinglearner-attemptsmatrix, • Analyzethecurrentdistributionofprobabilitiesinthe
whereeachvalueindicatestheprobabilityofalearnercorrectlyansweringaspecific learner-attemptsmatrix.
questiononaparticularattempt.Wewanttoscalethisdatatoaccommodatemore • Defineparameterstomimicreal-worldperformancepatterns(e.g.,
learners. power-lawdistributions).
(Providesrelevantreadingmaterial,questioninformation,andsampleJSON.) • Generatethenew,largersyntheticdatasetthatretainstheoriginal
data’sstatisticalproperties.
...
...
User:{YoucanasksomequestionstotestifGPT-4otrulyunderstandstheinformation GPT-4o:{Presenttheresultsbasedonyourtestingquery.}
provided.}
User:Thecurrentlearners-attemptsmatrix,partiallyshownas: GPT-4o:Theaugmentedlearners-attemptsmatrixforapopulationsizeof
1000learnershasbeengeneratedandsavedasaCSVfile....
0.99759290 0.99975013 0.99962294 ...
0.99932609 0.99996001 0.99990710 ...
 
 0.99705196 0.99976564 0.99956506 ... 
  . .
.
. .
.
. .
.
...  
correspondstothequestion“Whatisthetopicofthearticle?”(choices:[“Sports”,
“Exercising”,“Skydiving”],correctanswer:“Exercising”).Eachmatrixcellindicatesthe
probability(rangingfrom0to1)ofalearnercorrectlyansweringoneachattempt.
Theseprobabilitiesfollowapower-lawfunctionwithincreasingattempts.Inaddition,the
matrixusesthek-means++algorithmtocategorizelearnersbytheirfittedpower-law
parameters,althoughalllearnersfellintooneclusterduetosimilarperformancepatterns.
Pleaselearnfromthismatrixandgenerateanew,augmentedsetof1000learners(i.e.,
1000rows)with9attempts(i.e.,9columns).Indoingso:1)Useyourcomputational
capabilitytosimulatetheaugmentedmatrix.2)Presentthefinalresultasacomplete
matrixinNumPyarrayformat.3)Avoidincludinginstructions,explanations,orextra
textintheoutput.4)ProvidetheentirematrixasadownloadableCSVfile....
User:Canyouprovidedetailsaboutthemodelandsetupyouusedforgeneratingthe GPT-4o:Forgeneratingthesyntheticlearners-attemptsmatrix,I
syntheticdata?... employedthefollowingmodelandsetup:
• Modeldetailsandparameters
• Softwarelibrariesandenvironment
• Keyassumptionsorconstraints
Uponexecutingthecode,thesyntheticlearners-attemptsmatrixwas
successfullygenerated....
User:HowcanIfine-tunethemodeltoachievemorerealisticaugmenteddata?... GPT-4o:Tofine-tunethesamplingmodelfordataaugmentationand
increasetherealismandvariabilityofthesyntheticdata,consider:
• Introducinglearner-levelparametervariations
• Adjustingsamplingdistributionstomatchobservedperformance
trends
• Incorporatingnoiseorslightrandomizationtoreplicatereal-world
fluctuations
Theseenhancementsensurethatthegenerateddatamorecloselyreflects
authenticlearnerbehavior....
User:... GPT-4o:...
contextual prompts; an LLM component that involves prompting Thesepromptsaredesignedtofacilitateamorestructuredsimulation
an augmentation method that capitalizes on GPT’s reasoning and process by encouraging GPT-4o to think through each step system-
understanding capabilities; and decoding, which entails generating atically. Table II shows a sample conversation that demonstrates the
the simulated data along with interpretations. In this study, we used step-by-stepaugmentationprocessforlearningperformancedata.By
GPT-4o, and all further references to GPT indicate this version. As embedding numerical data in carefully crafted prompts and drawing
for the aforementioned matrix slice Ω that represents the learners upon GPT-4o’s CoT, we iteratively generate an expanded learners-
qn
and questions for learning performance, it can be formalized as attemptsmatrixthatretainscriticalstatisticalfeatures.Thisapproach
GPT(Ω ), which scales the size of the learner’s data. Specifi- underscorestheflexibilityandadaptabilityofGPT-basedmethodsin
qn
cally, inputs such as individualized learning performance values are capturing subtle learning patterns. Furthermore, prompt refinements
contextualized with detailed information about questions, answers, anddomain-specificguidanceallowGPT-4otointroduceappropriate
and attempts, including descriptions of their format and content. variabilitywhilepreservingthecorebehaviorsoftheoriginaldataset.
Subsequently, a simulation request prompts GPT-4o to seamlessly Asaresult,themethodoffersarobustwaytoscaledataforbroader
integrate this numerical and textual data, driving the execution of a analyses without compromising fidelity.
simulation. During this process, sampling mathematical models can
besearched,selected,andfine-tunedbyGPT-4otoenhancethedata VII. ExperimentalSetupandEvaluation
augmentation process. The prompts are iteratively refined to yield The experimental setup is designed and optimized according to
results that align with our specifications. Additionally, the Chain-of- the framework’s workflow, allowing for thorough evaluation through
Thought(CoT)promptingtechnique[77]isincorporated,whichuses detailed procedures.
guiding sentences such as “Can you explain your understanding of • (a) Measurement of Sparsity Levels: The evaluation of sparsity
this data?”, “Can you suggest potential machine learning methods levels is conducted by calculating the missing rate, defined as
for augmenting the data, particularly concerning sample size of ... the percentage of missing values relative to the total entries in
?”, and“Could youprovide theresults andsettings ofthe model?”. the tensor of learning performance data [78].

| JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES |     |     |     |     |     |     |     |     |     |     |     |     | 9   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b) Latent Features from Tensor Factorization: The number of (h)EvaluationsofParametersDistributionsCharacteristics:To
| •   |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
latent features can range from 1 to 20, and the optimal setting comprehensivelyevaluatetheaugmenteddatasets,weemployed
isidentifiedthroughagridsearchmethodthatinvolvesiterative supplementarymeasures,includingvisualizationtechniques(vi-
optimization of Tensor Factorization in data modeling. olin plots) and quantitative metrics like the Interquartile Range
(c) Question-level Knowledge Component Configurations: The (IQR)[82]andBimodalityCoefficient(BC)[83],alongsidethe
•
BKT and PFA models utilize two distinct assumptions for EMD for divergence measurement. Violin plots were utilized
setting KCs: “Single KC”, where all questions are attributed to to illustrate the distribution shapes and spread of parameters
one common knowledge component, and “Unique KC”, which a and b, providing detailed insights into central tendencies
assumes a one-to-one correspondence between questions and and variability in both Vanilla GAN and GPT-4o augmented
knowledge components. data relative to the original dataset. The IQR, defined as the
(d)Cross-ValidationforRunningDataImputationModels:For range between the 25th percentile (first quartile) and the 75th
•
Tensor Factorization and other baseline models in the data percentile (third quartile) of a distribution, was calculated as a
imputation stage, training and testing consistently follow a 5- robust,nonparametricmeasureofspread.Unlikestandarddevi-
fold cross-validation strategy to ensure reliable results, with all ation,theIQReffectivelycapturesvariabilitywhilereducingthe
models evaluated by averaging these outcomes or through five influenceofoutliers,makingitparticularlysuitedforcomparing
independent runs for enhanced robustness. distributions with differing levels of skewness or kurtosis. The
(e) Evaluation of Predictive Accuracy for Data Imputation: As BC was calculated based on the skewness and kurtosis of the
•
referenced in other peer research [28], [48], [50], [79], both parameter distributions to quantitatively assess their modality.
Mean Absolute Error (MAE) and Root Mean Square Error Additionally, the BC was employed to quantitatively assess the
(RMSE) are employed to quantify the performance of the modality of the distributions, The formula for BC is:
models.
g2+1
| (f) Significance |     | of Model | Performance | by  | ANOVA | Analysis: |     |     |     |      |     |     | (7) |
| ---------------- | --- | -------- | ----------- | --- | ----- | --------- | --- | --- | --- | ---- | --- | --- | --- |
| •                |     |          |             |     |       |           |     |     |     | BC = |     |     |     |
ANOVA analysis is employed to assess the statistical signifi- k+ 3(n−1)2
(n−2)(n−3)
canceofmodelperformance,usingMAEandRMSEtocritically
evaluate and compare the effectiveness of tensor factorization where g represents the skewness, k is the kurtosis, and n
against other models. is the sample size. The threshold for bimodality was set at
(g)ScalingSampleSize:Varyingsamplesizesfordataaugmen- BC = 0.555, with values above this threshold generally
•
tationarecomparedbetweenVanillaGANandGPT-4omodels indicating bimodality, while values below suggest unimodality.
to examine their effects on variance and bias in parameter Thiscoefficientintegratesasymmetryandpeakednesstoprovide
estimates fitted to augmented learner performance datasets. a comprehensive measure of the distribution’s modality. By
|              |          |     |            |           |         |      |     | integrating |     | these supplementary | measures, | we performed | a   |
| ------------ | -------- | --- | ---------- | --------- | ------- | ---- | --- | ----------- | --- | ------------------- | --------- | ------------ | --- |
| Sample sizes | increase | in  | increments | of 1,000, | ranging | from |     |             |     |                     |           |              |     |
rigorousanalysisofthestructuralfidelityandvariabilityofthe
| 1,000 to 20,000. |       |              |             |             |            |          |     |              |       |                          |     |            |        |
| ---------------- | ----- | ------------ | ----------- | ----------- | ---------- | -------- | --- | ------------ | ----- | ------------------------ | --- | ---------- | ------ |
|                  |       |              |             |             |            |          |     | augmented    | data, | enabling a comprehensive |     | assessment | of the |
| (h) Divergence   |       | Measurement: | The         | Earth       | Mover’s    | Distance |     |              |       |                          |     |            |        |
| •                |       |              |             |             |            |          |     | augmentation |       | models’ performance.     |     |            |        |
| (EMD) metric     | [80], | [81]         | is employed | to quantify | divergence |          |     |              |       |                          |     |            |        |
by measuring the distance between parameters of the power- To achieve optimal models’ performance, it’s essential to fine-
lawfunctionsfittedtoaugmentedandoriginaldatadistributions tune the parameters of each model during the optimization process.
separately, and to assess the reliability of data augmentation For the BKT, the four key parameters (P(L ), P(S), P(G) and
0
across varying sample sizes. Before computing EMD, the pa- P(T)) start with initial values within a range of 0.05 to 0.95. The
rametersarenormalizedwithineachsamplesizegrouptoensure optimization process tailors these parameters to each specific KC,
comparability, as normalization scales the distributions to sum demonstratingtheiradaptabilitytotheuniquecharacteristicsofeach
to1,removingbiasesduetodifferencesinmagnitudeorsample KC. The PFA model using the generalized linear mixed model with
size. In this study, we use this normalization method to scale individual learners as random effects for each KC (under “Unique
values while preserving their relative proportions. Instead of KC” mode) emphasizes the consideration of individual differences
considering other methods like Min-Max normalization, which among different learners and their related skills for acquiring KCs
may distort the distribution’s shape, or Z-Score normalization, in the learning process. SPARFA-Lite derives its original matrix
whichisunsuitableforprobability-basedcomparisons,wechose by averaging performance across multiple attempts, a method that
this approach to ensure the data remains a valid probability simplifiesthedatapreparationstep.TheTensorFactorization,which
distribution. EMD measures the minimum cost of transforming isappliedtovariousAutoTutorARClessons,necessitatesadifferent
one distribution into another, reflecting the amount of work set of tuning parameters, including λ, λ , λ , η, K (as detailed in
1 2
needed.SmallerEMDvaluesindicateclosersimilaritybetween Table V), and learning rate lr. In our experiments, λ was adjusted
distributions, while larger values indicate greater divergence. from 10−1 to 10−6, λ and λ ranged from 10−4 to 10−9, and lr
|             |        |             |            |      |              |            |        |      |        | 1 2   |     |     |     |
| ----------- | ------ | ----------- | ---------- | ---- | ------------ | ---------- | ------ | ---- | ------ | ----- | --- | --- | --- |
| This EMD    | metric | effectively | captures   | how  | changes      | in simula- | varied | from | 0.5 to | 10−2. |     |     |     |
| tion sample | size   | influence   | divergence | from | the original | data.      |        |      |        |       |     |     |     |
This procedure is formalized as follows. Firstly, normalize the VIII. Results
| o ri g i n a l d | i s tr i b u ti | o n oˆ = | o i          | , ∀ i ∈ { | 1 , . . . , n | }, a n d t h | e   |     |     |     |     |     |     |
| ---------------- | --------------- | -------- | ------------ | --------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                  |                 | i        | (cid:80) n o |           |               |              |     |     |     |     |     |     |     |
a u g m e n t d i s tr ib u t io n j= s1 j . N e x t , A . S p ar s it y M e a s u r ement and Latent Features Obtained by
|               |           | s ˆ i       | = (cid:80) i | , ∀ i ∈       | { 1 , . . . ,m | }   |     |          |              |         |     |     |     |
| ------------- | --------- | ----------- | ------------ | ------------- | -------------- | --- | --- | -------- | ------------ | ------- | --- | --- | --- |
|               |           |             | m jo = 1l s  | j             |                |     | Te  | n so r F | a c to riz a | t i o n |     |     |     |
| c o m p u t e | t h e E M | D u s i n g | th e f l o   | w ing e q u a | t io n s :     |     |     |          |              |         |     |     |     |
Here,toanswertheRQ1,wepresenttheresultsaboutthesparsity
i i levels for the learning performance data and the latent feature
|     |     | (cid:88) |     | (cid:88) |     | (5) |     |     |     |     |     |     | K   |
| --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C Oˆ (i)= oˆ j , C Sˆ (i)= sˆ j obtainedfromtheTensorFactorizationcomputingprocessforvarious
j=1 j=1 lessonsandtheircorrespondingdifficultylevels.Thisanalysisaimsto
|     |     |     | n   |     |     |     | understandtheextentofmissingdataandtodeterminethenumberof |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
(cid:88)
W (O,S)= |C (i)−C (i)|·d (6) latentfeaturesrequiredtoaccuratelyrepresenttheunderlyingpatterns.
|     | 1   |     | Oˆ  | Sˆ  | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TableVpresentsthemeasuredsparsitylevelsandthenumberoflatent
i=1
where the represents the distance between successive points featuresK derivedviatensorfactorization.Thesparsitylevelsacross
d i
(often assumed to be 1 if indices correspond to bins or pa- the dataset predominately fall within the to range, except
80% 90%
rameters), and and are the cumulative sums of for Lesson 4 (E), which stands at 64.58%. Higher sparsity levels
|     | C   | Oˆ (i) | C Sˆ (i) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the normalized vectors up to index i, ensuring an accurate indicate a greater proportion of missing values in the dataset, and
calculation of the EMD. vice versa. The values of latent features exhibit variation across
K

| JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES |     |     |     |     |     |     |     |     |     |     |     | 10  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLE III: Comparative analysis of model prediction accuracy in AutoTutor ARC lesson dataset using RMSE. Bold values
| represent the lowest | values. |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataset BKT(SingleKC) BKT(UniqueKC) PFA(SingleKC) PFA(UniqueKC) SPARFA-Lite TensorFactorization
| Lesson1(M) | 0.4790 | 0.4331 |     | 0.4733 |     | 0.4550 |     |     | 0.6287 |     | 0.4328 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson1(H) | 0.4178 | 0.4011 |     | 0.4315 |     | 0.4152 |     |     | 0.4850 |     | 0.3973 |     |
| Lesson2(M) | 0.4575 | 0.3957 |     | 0.4557 |     | 0.4390 |     |     | 0.5691 |     |        |     |
0.3840
| Lesson2(E) | 0.4261 | 0.4118 |     | 0.4415 |     | 0.4389 |     |     | 0.4969 |     | 0.4085 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson2(H) | 0.4512 | 0.3861 |     | 0.4490 |     | 0.4358 |     |     | 0.5449 |     | 0.3715 |     |
| Lesson3(M) | 0.4077 | 0.3936 |     | 0.4227 |     | 0.4098 |     |     | 0.4644 |     | 0.3911 |     |
| Lesson3(H) | 0.4768 | 0.4004 |     | 0.4782 |     | 0.4704 |     |     | 0.5826 |     |        |     |
0.3948
| Lesson4(M) | 0.4766 | 0.4583 |     | 0.4775 |     | 0.4799 |     |     | 0.6008 |     |     |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | --- | --- |
0.4438
| Lesson4(E) | 0.4929 | 0.4750 |     | 0.4989 |     | 0.4939 |     |     | 0.5789 |     | 0.4457 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson4(H) | 0.4968 | 0.4605 |     | 0.5154 |     | 0.5027 |     |     | 0.6544 |     | 0.4545 |     |
TABLE IV: Comparative analysis of model prediction accuracy in AutoTutor ARC lesson dataset using MAE. Bold values
| represent the lowest | values. |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataset BKT(SingleKC) BKT(UniqueKC) PFA(SingleKC) PFA(UniqueKC) SPARFA-Lite TensorFactorization
| Lesson1(M) | 0.4623 | 0.3777 |     | 0.4500 |     | 0.4071 |     |     | 0.3954 |     | 0.3806 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson1(H) | 0.3535 | 0.3347 |     | 0.3340 |     | 0.3350 |     |     | 0.2387 |     | 0.3178 |     |
| Lesson2(M) | 0.4252 | 0.3257 |     | 0.4150 |     | 0.3806 |     |     | 0.3245 |     |        |     |
0.2740
| Lesson2(E) | 0.3731 | 0.3461 |     | 0.3666 |     | 0.3507 |     |     | 0.2503 |     | 0.3052 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson2(H) | 0.4184 | 0.3141 |     | 0.4003 |     | 0.3595 |     |     | 0.2979 |     | 0.2904 |     |
| Lesson3(M) | 0.3330 | 0.3175 |     | 0.3293 |     | 0.3256 |     |     | 0.2158 |     | 0.2805 |     |
| Lesson3(H) | 0.4588 | 0.3275 |     | 0.4446 |     | 0.4380 |     |     | 0.3400 |     | 0.3030 |     |
| Lesson4(M) | 0.4598 | 0.4106 |     | 0.4437 |     | 0.4487 |     |     | 0.3625 |     |        |     |
0.3494
| Lesson4(E) | 0.4819 | 0.4304 |     | 0.4789 |     | 0.4806 |     |     | 0.3583 |     | 0.3372 |     |
| ---------- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | ------ | --- | ------ | --- |
| Lesson4(H) | 0.4945 | 0.3998 |     | 0.4914 |     | 0.4815 |     |     | 0.4287 |     | 0.3832 |     |
different lessons and their corresponding difficulty levels, typically predictingmissingdatathroughitsmathematicalimputationmethods,
requiring between 4 to 7 latent features to accurately represent the addressingacriticalneedfordataimputationinadultliteracy.Among
underlying patterns in the learning performance data. the RMSE values of Tensor Factorization across all lessons and
|     |     |     |     |     | difficulty | levels, | the model | achieves | the | lowest | RMSE in | Lesson 2 |
| --- | --- | --- | --- | --- | ---------- | ------- | --------- | -------- | --- | ------ | ------- | -------- |
TABLE V: The sparsity levels and obtained latent features by (H)with0.3715andthehighestRMSEinLesson4(H)with0.4545,
tensor factorization. indicating that its prediction accuracy is best in Lesson 2 (H) and
|         |                |                    |     |     | less effective | in  | Lesson | 4 (H).   | Additionally, | the       | RMSE          | from the |
| ------- | -------------- | ------------------ | --- | --- | -------------- | --- | ------ | -------- | ------------- | --------- | ------------- | -------- |
|         |                |                    |     |     | BKT (unique    | KC) | model  | is quite | close         | to Tensor | Factorization | and      |
| Dataset | SparsityLevels | K (LatentFeatures) |     |     |                |     |        |          |               |           |               |          |
outperformsothermodelsinseveralinstances.Forexample,inLesson
| Lesson1(M) | 84.94% |     | 6   |     |           |                 |     |              |        |        |            |          |
| ---------- | ------ | --- | --- | --- | --------- | --------------- | --- | ------------ | ------ | ------ | ---------- | -------- |
|            |        |     |     |     | 1 (M),    | BKT (unique     |     | KC) achieves | an     | RMSE   | of 0.4331  | compared |
| Lesson1(H) | 89.89% |     | 7   |     |           |                 |     |              |        |        |            |          |
|            |        |     |     |     | to Tensor | Factorization’s |     | 0.4328,      | and in | Lesson | 3 (H), BKT | (unique  |
| Lesson2(M) | 84.02% |     | 6   |     |           |                 |     |              |        |        |            |          |
KC)achievesanRMSEof0.4004comparedtoTensorFactorization’s
| Lesson2(E) | 81.25% |     | 4   |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lesson2(H) 85.45% 6 0.3948.Thistrendisalsoobservedinotherlessons,includingLesson
Lesson3(M) 81.25% 5 1 (H), Lesson 2 (M), Lesson 2 (E), Lesson 2 (H), Lesson 3 (M),
Lesson3(H) 82.04% 6 Lesson 4 (M), Lesson 4 (E), and Lesson 4 (H). These trends reflect
Lesson4(M) 86.27% 6 therelativelyhigheraccuracyofBKTcomparedtotheothermodels,
| Lesson4(E) | 64.58% |     | 6   |     | except for | Tensor      | Factorization. |              |     |            |        |         |
| ---------- | ------ | --- | --- | --- | ---------- | ----------- | -------------- | ------------ | --- | ---------- | ------ | ------- |
| Lesson4(H) | 86.57% |     | 5   |     |            |             |                |              |     |            |        |         |
|            |        |     |     |     | Table      | IV presents |                | a comparison | of  | MAE values | across | various |
Notes: The table summarizes the sparsity levels and the number of latent models and lessons, with the lowest values highlighted in bold.
features (K) obtained from tensor factorization across various datasets. The Notably, Tensor Factorization frequently achieves the lowest MAE
datasetsaredividedbylessonandcategorizedasM(Medium),H(Hard),and values, signaling its robustness in closely estimating actual learning
E(Easy).Highersparsitylevelsindicateagreaterproportionofmissingvalues
performance.Nonetheless,somemodelssuchasSPARFA-Liteexhibit
| inthedataset.ThenumberoflatentfeaturesK |     | representsthedimensionality |     |     |             |             |     |             |         |           |        |       |
| --------------------------------------- | --- | --------------------------- | --- | --- | ----------- | ----------- | --- | ----------- | ------- | --------- | ------ | ----- |
|                                         |     |                             |     |     | exceptional | performance |     | in specific | lessons | including | Lesson | 1 (H) |
ofthelatentspaceresultingfromthefactorizationprocess.
|     |     |     |     |     | with an   | MAE of    | 0.2387, | Lesson   | 2 (E)   | with an    | MAE of 0.2503, | and      |
| --- | --- | --- | --- | --- | --------- | --------- | ------- | -------- | ------- | ---------- | -------------- | -------- |
|     |     |     |     |     | Lesson 3  | (M) with  | an      | MAE of   | 0.2158, | with BKT   | (Unique        | KC) also |
|     |     |     |     |     | excelling | in Lesson | 1       | (M) with | an MAE  | of 0.3777, | indicating     | their    |
B. Predictive Accuracy for Data Imputation potential effectiveness under specific conditions.
As demonstrated by the predictive accuracy results based on the To determine if the MAE values obtained by Tensor Factorization
two metrics, and MAE, which address RQ1, the following are significantly lower than those from other models, an ANOVA
RMSE
analysis provides insights into model performance. analysis was conducted using MAE as the dependent variable and
Table III demonstrates that Tensor Factorization consistently a binary factor indicating Tensor Factorization as the independent
achieves the lowest values across all lessons and difficulty variable. During the ANOVA analysis, the two degrees of freedom
RMSE
levels (medium, easy, and hard), highlighting its superior predic- areasfollows:df =5forbetweengroups,anddf =54
|     |     |     |     |     |     |     | between |     |     |     | within |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ------ | --- |
tion accuracy (with the lowest values bolded in the table). for within groups. The F-value is calculated to be 7.2003, with a
RMSE
This indicates that Tensor Factorization is particularly effective in correspondingp-valueof3.164×10−5,whichislessthan0.05.This
predicting performance compared to the other three KT models, indicates statistically significant differences in MAE between Tensor
includingBKT,PFA,andSPARFA-Lite.Thesuperiorperformanceof Factorization and the other models.
TensorFactorizationinlearnermodelingalsoreflectsitsaccuracyin In conclusion, Tensor Factorization allows for highly accurate

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 11
(a) Distribution of parameter a and b. (b) Curve fitting of learning performance along attempt
Fig. 3: Estimates of parameter estimates a and b and identification of learning performance patterns through clustering.
prediction of missing performance data based on the existing data and b across five clusters for the example 6th question of Lesson
distribution, enabling a comprehensive dataset for data imputation. 2(M). In both models (Vanilla GAN and GPT-4o), the parameters
a and b generally exhibit stable and relatively low EMD (mostly
below0.10)acrossincreasingsamplesizes(from1,000to20,000)for
C. IdentificationofIndividualizedLearningPerformancePat-
most clusters. However, exceptions are observed in GPT-4o Cluster
terns
5, where the EMD remains around 0.5 for both parameters a and b
To address RQ2, this section presents the results of identifying acrossallsamplesizes.ThisgenerallydemonstratesthatbothVanilla
individualizedlearningperformancepatternsthroughclusteringanal- GAN and GPT-4o models can generate stable augmented data by
ysis. By leveraging a dense 3-dimensional tensor representation of effectivelylearningtheoriginaldatadistributions,evenasthesample
dataimputedfromTensorFactorization,weanalyzedistinctlearning sizescales.Fig.5presentsthemeanEMDvaluesacrossallclusters.
performance clusters. The mean EMD values for Vanilla GAN and GPT-4o across both
Fig. 3 illustrates distinct learning performance patterns identified parameters are nearly identical, except for parameter b in Cluster 3,
throughclustering,basedonadense3Dtensorrepresentationofdata where Vanilla GAN has a slightly lower value (0.050 compared to
imputedfromTensorFactorization,usingthe6thquestionofLesson GPT’s 0.055). The overall mean EMD values across all six clusters
2 (M) as a case study. It identifies five distinct clusters based on are 0.137 for Vanilla GAN and 0.138 for GPT-4o, indicating closely
fluctuations in parameter a and b from power-law function fitting aligned performance between the two generative models. This simi-
on the learners-attempts matrix data (as mentioned before) for the laritysuggeststhatbothVanillaGANandGPT-4oexhibitcomparable
6th question, each depicted in different colors as shown in Fig. 3a. accuracy in capturing the data distributions across clusters, with
From Cluster 1 to Cluster 5, the a value decreases, starting largest minimaldivergencebetweenthem.IntheexceptionalcaseofGPT-4o
inCluster1andgraduallyreducingthroughtoCluster5.Conversely, Cluster5,however,wehypothesizethattheobserveddifferencesstem
the b value increases across the clusters from Cluster 1 to Cluster 5, from the model’s challenge in capturing this cluster’s specific data
indicating an inverse relationship between a and b among different distribution, likely due to its high sparsity with data from only two
clusters. users,asshowninFig.3).Inconclusion,whilebothVanillaGANand
Fig.3bdisplaystheclusteringresultsusingidenticalcolorcoding GPT-4omodelsgenerallyproduceaugmenteddatathatalignsclosely
for the five clusters and shows that predicted learning performance withtheoriginaldataacrossvaryingconditions,includingquantified
(probability-based) generally increases monotonically with the num- learning features, parameters a and b, and expanded sample sizes,
ber of attempts, approaching or reaching a performance level of Vanilla GAN demonstrates slightly better performance in certain
around 1 (y-axis value). This trend persists across all clusters, clusters,specificallytheCluster3forparameterb,whereitswhereits
although at varying rates. Specifically, most fitting curves approach EMDvaluesaremarginallylower.Overall,bothmodelsexhibitstable
around 1 within seven attempts, indicating that the majority of and reliable performance, with Vanilla GAN performing slightly
learners likely do not need more than seven attempts to achieve betterthanGPT-4oincertainscenarios,andminimaldivergencefrom
theoretical complete mastery, a pattern also observed in other cases the original data distributions in most cases.
notshown.Notethatthefittingcurvesexpresstheoveralltrend,while To further investigate these observations, we now examine the
scatter points represent the actual performance data. detaileddistributionpatternsofparametersaandbobtainedfromthe
augmented datasets, as illustrated in Fig. 6. This figure presents the
D. Results of Scalable Data Augmentation unnormalized distributions of parameters a and b obtained through
power-law fitting on the augmented learning performance dataset,
This subsection presents the data augmentation results based on
usingbothVanillaGANandGPT-4obasedaugmentation.Forclarity,
GenAImodelswithscalablesampling,addressingRQ2.Theanalysis
Cluster 3 of the 6th question from Lesson 2 (M) is used as an
highlights how these models effectively enhance data diversity and
example to highlight the differences in greater detail. By focusing
volume, thereby boosting the robustness of subsequent machine
on unnormalized data, we aim to preserve the original scale of the
learning applications. Furthermore, a detailed comparison between
parameters and directly compare their raw distributions. Note that
Vanilla GAN and GPT-4o based augmentation methods highlights
thegreycolorrepresentstheoriginaldatadistribution.Moreover,the
which approach offers greater stability across varying sample sizes.
IQR, depicted in Fig. 7, supplements this analysis by providing a
Fig. 4 illustrates the EMD measurement results for divergence in
refined measure of distribution spread. The combined insights from
power-law fitting parameters, comparing augmented learning perfor-
these two figures are summarized in the following paragraphs.
mance data to original data. It covers the full scope of parameter a

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 12
Fig. 4: EMD measurement for scalable sampling by data augmentation. The original sample size is 20, and the augmentations
| are shown | in increments | of 1,000, with total | sizes ranging | from 1,000 | to 20,000. |     |
| --------- | ------------- | -------------------- | ------------- | ---------- | ---------- | --- |
Fig. 5: Comparison of measurement for data augmentation between Vanilla GAN and GPT-4o.
EMD
(a) Distribution of parameter a (b) Distribution of parameter b
|     |     | Fig. 6: Distributions | of parameters | in augmented | learning performance | data. |
| --- | --- | --------------------- | ------------- | ------------ | -------------------- | ----- |

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 13
(a) Interquartile range of parameter a (b) Interquartile range of parameter b
Fig. 7: Variance comparison of parameters in augmented learning performance data.
(a) Bimodality coefficient of parameter a (b) Bimodality coefficient of parameter b
Fig. 8: Comparison of the bimodality coefficient of parameters in augmented learning performance data.
Fig.6aillustratesthedistributionofparameteraforVanillaGAN 14,000,and17,000to20,000,theGPT-4o-baseddistributionsexhibit
and GPT-4o models. The following observations can be made. First, relatively smaller ranges closer to the original data, which is also
the parameter distribution of a obtained from Vanilla GAN-based reflected in lower IQR values for these cases, though they still
augmentationgenerallyfallswithintherangeoftheoriginaldata,with extend beyond the original distribution. These observations show
a slightly extended tail beyond the original maximum value. Com- thatGPT-4o-basedaugmentationhashighvariabilityandinconsistent
paredtotheoriginaldistribution,theVanillaGAN-baseddistributions performance in approximating the original distribution, capturing its
maintain a similar shape with a concentrated and narrower central corecharacteristicsonlyoccasionally.Incontrast,VanillaGAN-based
region in the violin plots, indicating that the Vanilla GAN model augmentation exhibits consistently lower variability, with stable IQR
effectivelycapturesthecorecharacteristicsoftheoriginaldatawhile values, highlighting its reliability in preserving the original data’s
introducingminimalvariability.TheIQRvaluesforVanillaGAN,as structure and variability.
showninFig.7a,remainconsistentlystablewithminimalfluctuations Fig. 6b shows the distribution of parameter b for Vanilla GAN-
acrossallsamplesizes,reflectingreliablebehaviorandcloselyalign- based augmentation. First, the parameter distribution of obtained
ing with the original data’s variability. This consistent performance fromVanillaGAN-basedaugmentationalsogenerallyalignswiththe
in terms of parameter a highlights the stability and dependability originaldata,particularlyintermsofmaximumandminimumvalues.
of Vanilla GAN-based augmentation in preserving the structure and Thedistributionsexhibitasimilarshape,withslightlyextendedtails
corecharacteristicsoftheoriginaldistribution.Incontrast,theGPT- beyond the original range but no significant deviations. The IQR
4o-based augmentation exhibits considerably broader parameter a values for Vanilla GAN, as shown in Fig. 7b, remain consistently
distributionsformostsamplesizes,suggestinghighervariability.This stable across all sample sizes, reflecting Vanilla GAN’s stable and
variabilityisparticularlypronouncedforcertainsamplesizes,suchas reliable performance in data augmentation. This consistent behavior
1,000to9,000,and15,000to16,000,wheretheGPT-4odistributions in parameter b highlights the Vanilla GAN model’s effectiveness in
displayelongatedtailsandexhibitdistinctlydifferentcentralregions. preserving the structure and variability of the original distribution
Compared to the original distribution, these central regions are not withminimaldistortion.Incontrast,theGPT-4o-basedaugmentation
only wider but also shifted, indicating significant deviations in both exhibitssignificantlyhighervariabilityforparameterb,asevidenced
dispersionandcentralityfromtheoriginaldata’scorecharacteristics. by the broader distributions and elongated tails across most sample
This higher variability in parameter a is further evidenced by the sizes,asshowninFig.6b.TheGPT-4odistributionsdisplaymarked
fluctuating IQR values for GPT-4o-based augmentation in Fig. 7a. deviations from the original data, particularly for sample sizes be-
However,forspecificsamplesizes,including10,000,12,000,13,000, tween 1,000 and 9,000 and again at 15,000 to 16,000, where the

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 14
tails become elongated. The dispersion is further reflected in the asmodelingbias,reducedperformance,anddifficultiesinknowledge
fluctuatingIQRvaluesforGPT-4o,asseeninFig.7b.However,there tracing [10], [17]. Other research has also highlighted similar high
is occasional alignment with the original data for specific sample sparsitylevelsineducationaldatasets.Forexample,Saarela’sresearch
sizes,suchas10,000to14,000and17,000to20,000.Inthesecases, [17] on student performance data notes sparsity levels ranging from
the distributions are relatively closer to the original data compared 30% to 74% in the PISA 2012 dataset, and Thai-Nghe’s study [84]
to other sample sizes, as observed in both Fig. 6b and Fig. 7b. on the Algebra dataset reports extreme sparsity, with rates reaching
Theseobservationsindicatethat,forparameterb,VanillaGAN-based up to 99.81%. The latent features captured through tensor factor-
augmentation demonstrates consistent and reliable performance, ef- ization quantitatively reflect learner-specific characteristics, such as
fectivelycapturingtheoriginaldistribution’sstructureandvariability. learning abilities and personalities. These characteristics of learners
In contrast, GPT-4o-based augmentation exhibits greater variability remain stable over time in the reading comprehension context. The
and inconsistency, with fluctuations in alignment and dispersion number of features identified, averaging around six, closely aligns
that make it less reliable for preserving the original distribution’s with Graesser-McNamara’s multi-level theoretical framework [85]
characteristics. for reading comprehension, which includes six levels: word, explicit
Asindicatedbythedistributionshape,weanalyzetheparameters textbase, referential situation model, discourse genre and rhetorical
a and b through BC, which provides a quantitative measure of structure,andpragmaticcommunicationlevel[86].However,further
bimodality, as illustrated in Fig. 8. The threshold BC = 0.555, research is needed to verify this alignment and explore the potential
marked in the Fig. 8, indicates that values exceeding this threshold connections.
generallysignifybimodality,whilelowervaluessuggestunimodality. Constructing a 3D tensor of learning performance data provides
The original data distribution for Cluster 3 exhibits bimodality for a foundation for analyzing patterns across learners, questions, and
both parameter a and b, as evidenced by BC values greater than attempts. Tensor factorization captures complex interactions among
0.555, represented by the dark dot labeled “Original” in the figure. these dimensions and estimates missing values for unattempted
As shown in Fig. 8, the Vanilla GAN-generated data predominantly questions. This approach builds on successful applications of tensor
exhibitsunimodalityacrossallsamplesizesforbothparameters,with methods in learning performance analysis, as shown in prior studies
BC values remaining below the 0.555 threshold. On the other hand, [13],[48],[78].Byintegratingthismodelingtechnique,wecanmore
the GPT-4o-generated data generally exhibits unimodality, although accurately impute missing data, thereby enhancing the robustness of
it transitions to bimodality in specific cases. Notably, unimodality the analysis and providing deeper insights into learner behavior and
is observed at sample sizes of 12,000, 14,000, 17,000, 18,000, and performance trends in ITSs.
19,000 for both parameters a and b. The Vanilla GAN show stable Theidentificationofdifferentlearningperformancepatternsacross
though that distribution shape are different original data, the GPT- various clusters highlights the importance of variations in initial
4o is high variant but some cases distribution shape more closer learning performance and learning rate as key differentiators among
to original data distributions shape. These findings indicate that the learners. The observed inverse relationship between these two quan-
Vanilla GAN model consistently generates unimodal distributions, tified features (a and b) reveals a notable learning phenomenon:
which,whilestable,deviatefromtheoriginaldata’sbimodalcharac- learners with higher initial abilities are closer to complete mastery
teristics.Incontrast,theGPT-4omodelexhibitsgreatervariabilityin and exhibit slower knowledge acquisition, while those with lower
its distributions. In specific instances, the distributions generated by initial abilities achieve faster knowledge gains due to their lower
GPT-4oalignmorecloselywiththeoriginaldata’sbimodalstructure, starting points. While other past work has found such aptitude-
suggesting that GPT-4o has the potential to better capture certain treatmentinteractions,severalotherdatasets,broaderevidencefinds
features of the original data under specific conditions. thatlearningratesarelargelyindependentofability,withexceptions
oftenlyinginlanguagelearningdomains(suchasthedomainofthis
IX. Discussion study)whereindividuallearningdifferencescanbecompensatedfor
less by tailored instructions [87].
Thisstudyproposesasystematicaugmentationframeworkintegrat-
ing multidimensional learner modeling with generative AI models, In terms of EMD measurements, both Vanilla GAN and GPT-4o
models demonstrate stable performance in data augmentation across
specifically Vanilla GANs and GPT-4o, to address the critical issue
varying sample sizes, with Vanilla GAN showing slightly better
of data sparsity in ITSs. Our primary objective was to enhance the
resultsthanGPT-4oincertainscenariosandexhibitingminimaldiver-
quality and scalability of learning performance data in adult reading
gencefromtheoriginaldatadistributionsinmostcases.WhileVanilla
comprehension using tensor factorization for data imputation and
GANdemonstratesmoreconsistentandstableperformanceacrossall
generative models for data augmentation. Guided by the research
conditions,GPT-4ogenerateddataexhibitshighervariabilityandoc-
questions on the effectiveness of tensor factorization for imputing
casionalbimodality,allowingittoalignmorecloselywiththeoriginal
student performance data and the utilization of GenAI models for
data’s structure under specific sample sizes. These observations are
tailored data augmentation, our findings reveal that tensor factor-
furthervalidatedthroughevaluationsofthedistributioncharacteristics
ization outperforms traditional modeling methods, providing higher
predictive accuracy and more effective handling of missing values. of parameters a and b, using visualization techniques (violin plots)
and quantitative metrics such as IQR and BC metric. The Vanilla
Building on the densified 3D tensor-based learning performance
GAN model, with its advanced neural network architecture and
data,individuallearningperformancepatternswereidentifiedthrough
thousandsofparameters,outperformstraditionalstatisticalmethodsin
clustering,andbothVanillaGANandGPT-4omodelswereemployed
capturingtheoriginaldatadistribution,makingitadependablechoice
to augment learning performance data tailored to these patterns.
for scenarios requiring consistent augmentation across varied condi-
ResultsdemonstratethataugmenteddatasetsfrombothVanillaGAN
tions. On the other hand, GPT-4o based augmentation closely aligns
and GPT-4o align closely with the original data distribution, as
withtheoriginaldatadistribution,suggestinghighfidelity.GPT-4o’s
evidenced by divergence measurements using the EMD. However,
capability to understand context-based numerical values and execute
key differences between the models were observed: Vanilla GAN-
self-driventasksincludingself-analysis,self-programming,andself-
generated data consistently produces stable, unimodal distributions
computing during data augmentation [12] highlights its potential
withlowervariabilityanddivergence,whereasGPT-4ogenerateddata
for generating complex data patterns. These capabilities, especially
exhibits higher variability and occasional bimodality, aligning more
whencombinedwithadvancedcomputationaltechniques,underscore
closelywiththeoriginaldata’sstructureunderspecificsamplesizes.
GPT-4o’s promise for data augmentation tasks requiring nuanced
ThesecomplementarystrengthsunderscoreVanillaGAN’sreliability
contextual understanding and adaptability.
and GPT-4o’s potential to replicate complex patterns, highlighting
Whendecidingbetweenthetwotypeofmodels,thechoiceshould
their utilities for enhancing learning performance data.
bescenario-basedandgoal-driven,aligningwiththespecificcontext
Highsparsitylevelsinthedataset,ashighlightedinTableV,sig-
andobjectivesofthetask.Thisstudyprovidesafoundationalmethod-
nificantly impact modeling and analytics, leading to challenges such

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 15
ologyforemployingGenAImodels,includinggenerativecomputing GenAI models, particularly Vanilla GAN and GPT-4o. Our experi-
modelsexemplifiedbyGANandLLMsrepresentedbyGPT-4o,while mentswithGPT-4odemonstratedimprovedperformance,particularly
acknowledging that alternative GenAI models could also be applied, in terms of Earth Mover’s Distance (EMD) and visual analyses,
with performance varying based on testing and context. A scenario- comparedtoGPT-4.However,amoredetailedexplorationofvarious
based approach involves analyzing the context in which the model GPT versions, such as GPT o-1, is needed to fully understand the
willbeused,suchasfavoringVanillaGANforapplicationsrequiring specific improvements and differences they offer. Similarly, while
stabilityandconsistency,orGPT-4oforreplicatingcomplex,nuanced we employed the base GAN architecture, Vanilla GAN, for data
data patterns. A goal-driven perspective focuses on aligning the augmentation, advanced GAN variants like Deep Convolutional
model’s strengths with the intended outcomes, such as using Vanilla GAN (DCGAN), Conditional GAN (cGAN), and Wasserstein GAN
GAN to generate data with minimal variability and bias, or GPT-4o (WGAN)couldpotentiallyenhancetheaugmentationprocess.Future
to mimic intricate structures and support diversity. The performance work should investigate how these different versions of GAN and
in augmenting learning performance data may vary depending on GPT influence performance metrics and learning outcomes, thereby
thespecificmodelchosen,butthecomplementarystrengthsofGAN improving the framework’s robustness, scalability, and adaptability
(stability)andGPT-4o(complexity)highlighttheirutilityfordifferent across diverse ITS datasets. Additionally, we highlight that other
contexts and goals. open-source LLMs, such as Llama, Grok, and others, offer valuable
Further,VanillaGAN-derivedparameterestimatesexhibiteddesir- opportunitiesfortesting,whetherthroughinterface-basedimplemen-
ablepropertiesforbothparametersaandb:lowervariancecompared tations or API versions. Secondly, the tensor-based data imputation
to the original parameter distribution at the cost of small bias in and augmentation methods, although effective in this study, might
parameter estimates. Lower variance is desirable as it indicates a not capture all nuances of learner behavior and performance. Tensor
higher accuracy with which a can be estimated (in the absence factorizationmodelsassumethatlearnersatsimilarknowledgelevels
of statistical bias, which was minimal compared to the original exhibitcomparableperformancepatterns,whichmaynotalwayshold
parameterdistribution).Importantly,thisdesirablepropertyofVanilla true, especially in cases of highly individualized learning processes.
GAN augmentation is not dependent on the total augmented sample Given the remarkable success of generative deep learning models,
size, suggesting consistent performance irrespective of the degree of such as Generative Adversarial Imputation Networks (GAIN) [88],
data augmentation applied. In contrast, GPT-4o derived parameter [89] and Autoencoders (AE) [90] for data imputation through re-
estimates demonstrate greater variability compared to the original construction mechanism, future work should explore their potential
distribution,indicatinglessstabilityinreplicatingspecificparameter in handling data sparsity and capturing more complex patterns
characteristics. However, GPT-4o’s high fidelity in preserving the underlying learning performance data in ITSs. Thirdly, our study
original data’s structural features in certain occasional cases high- prioritizes the application of methodology over model optimization,
lightsitspotentialforgeneratingcomplexandnuanceddatapatterns. examining how GenAI can enhance data augmentation. Although
Future research exploring self-driven procedural prompts, such as emerging advanced models, such as the GPT o-1, present promising
self-searching, self-programming, and self-computing for numerical avenues for further testing [65], limitations in file processing and
value augmentation, may further enhance GPT-4o’s capabilities and project costs mean that a more extensive analysis is beyond the
improve upon the baseline performance reported in this study. current scope and deferred to future work. Additionally, the broad
The systematic augmentation framework that integrates multidi- scope of our systematic framework presents certain limitations, as
mensional learner modeling through tensor factorization and GenAI it extends beyond a focused investigation of specific aspects such
modelseffectivelyaddressesdatasparsityissuesinITSsandenables as multidimensional interactions, latent feature exploration in tensor
the augmentation of large-scale learning performance data. This factorization, and the verification of augmented data for real-world
approach captures the complexity of human learning performance learner modeling. These areas may not have been explored in suf-
with greater accuracy than traditional machine learning methods, ficient depth, limiting the granularity of insights. Lastly, while this
thereby enhancing predictive capabilities and providing deeper in- frameworkfocusesonaugmentinglearningperformancedata,itdoes
sightsintolearners’progress.Asaresult,ITSscanoffermoreprecise notdirectlyprovidestrategiesforintegratingtheproposedframework
recommendations and interventions, leading to personalized and withcomprehensivelearnermodelinginITSstogainamorenuanced
adaptivelearningexperiences.Bygeneratinghigh-qualityaugmented understanding of learner behavior and enhance adaptive instruction.
data, the framework supports more comprehensive and equitable Future research should aim to address these gaps, enabling more
analysis, reducing biases and enabling more inclusive educational effective personalization and support for learners within ITSs.
researchandpractice.This,inturn,helpseducatorsandpolicymakers
makemoreinformeddecisionsbasedonrobust,large-scaleevidence. XI. Conclusions
Additionally,theabilitytoconductextensiveanalyseswithaugmented
The present study presented a novel framework for augmenting
data mitigates biases such as group or data selection biases, leading
learning performance data in ITSs by integrating multidimensional
to fairer and more generalizable findings in educational research.
learnermodeling(specificallytensorfactorization)withGenAImod-
Ultimately,thisinnovativeframeworksignificantlycontributestothe
els. The presented empirical evaluation suggests that this framework
advancement of AI-driven educational tools, fostering better and
effectivelydensifiessparselearningperformancedata.Wespecifically
more effective instructions and recommendations, and improving
addressed the challenge of learning performance data sparsity issues
educational outcomes for all learners.
in ITSs using AutoTutor ARC as a case study, leveraging tensor
factorizationfordataimputationandGenAImodels,includingVanilla
X. LimitationsandFutureWorks GAN and GPT-4o, for data augmentation. Our findings highlighted
This study addresses the significant challenge of data sparsity in thesuperiorpredictiveaccuracyoftensorfactorizationoverbaseline
ITSs through a systematic augmentation framework that integrates methods, such as BKT, PFA and SPARFA-Lite, across four different
multidimensional learner modeling and GenAI models. However, AutoTutorARClessonsacrossdifferentdifficultylevels.Furthermore,
despite the promising results, there are several limitations that need VanillaGAN-basedaugmentationsdemonstrateddesirableproperties
to be addressed. Firstly, the datasets used in this study were limited such as lower variance in parameter estimates. These improvements
toadultreadingcomprehensioncasesfromtheAutoTutorARC.This werelargelyreliableacrossdifferentaugmentedsamplesizes.Vanilla
restrictsthegeneralizabilityofourfindingstootherdomainsofITSs, GAN-based augmentations exhibited desirable properties, including
where the characteristics and patterns of learner performance data lower variance in parameter estimates, ensuring stable and reliable
might differ. Future research should aim to apply this framework to performance regardless of the total augmented sample size. In con-
diverse ITSs and learning contexts to validate its applicability and trast, GPT-4o based augmentation demonstrated higher variability
effectiveness. Secondly, the study focused on specific versions of but occasionally showed closer alignment with the original data
distribution, particularly in cases where bimodality was observed.

| JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 16  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
These results underscore the complementary strengths of Vanilla [12] L.Zhang,J.Lin,C.Borchers,M.Cao,andX.Hu,“3DG:AFramework
GAN and GPT-4o: Vanilla GAN provides relatively reliable aug- forUsingGenerativeAIforHandlingSparseLearnerPerformanceData
mentation,whileGPT-4o,thoughhighlyvariable,offersthepotential From Intelligent Tutoring Systems,” arXiv preprint arXiv:2402.01746,
| for replicating | complex |              | data structures |     | and enhancing |           | data diversity. | 2024.          |     |           |        |           |           |          |             |
| --------------- | ------- | ------------ | --------------- | --- | ------------- | --------- | --------------- | -------------- | --- | --------- | ------ | --------- | --------- | -------- | ----------- |
|                 |         |              |                 |     |               |           |                 | [13] L. Zhang, | P.  | I. Pavlik | Jr, X. | Hu, J. L. | Cockroft, | L. Wang, | and G. Shi, |
| The systematic  |         | augmentation | framework       |     | effectively   | addresses | data            |                |     |           |        |           |           |          |             |
“ExploringtheIndividualDifferencesinMultidimensionalEvolutionof
| sparsity | issues in | ITSs, | enhancing | predictive |     | capabilities | and pro- |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | --------- | ---------- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
KnowledgeStatesofLearners,”inInternationalConferenceonHuman-
| viding deeper | insights |          | into learners’ | progress. |           | This framework | has        |                      |     |     |                           |     |     |     |     |
| ------------- | -------- | -------- | -------------- | --------- | --------- | -------------- | ---------- | -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
|               |          |          |                |           |           |                |            | ComputerInteraction. |     |     | Springer,2023,pp.265–284. |     |     |     |     |
| the potential | to       | mitigate | group          | and data  | selection | biases         | that often |                      |     |     |                           |     |     |     |     |
[14] G.Psathas,T.K.Chatzidaki,andS.N.Demetriadis,“PredictiveMod-
occur during the collection of learning performance data in real- eling of Student Dropout in MOOCs and Self-Regulated Learning,”
worldexperiments.TheframeworkshowspromiseforenhancingITSs Computers,vol.12,no.10,p.194,2023.
throughsafeandcost-effectiveaugmentation,enablingcomprehensive [15] R.S.Baker,“Modelingandunderstandingstudents’off-taskbehaviorin
data modeling by mitigating the impact of data sparsity, facilitating intelligenttutoringsystems,”inProceedingsoftheSIGCHIconference
virtual evaluations of instructional designs, and paving the way for onHumanfactorsincomputingsystems,2007,pp.1059–1068.
|          |            |              |     |            |     |           |          | [16] R. S. | Baker, | A. T. | Corbett, | and K. | R. Koedinger, | “Detecting | student |
| -------- | ---------- | ------------ | --- | ---------- | --- | --------- | -------- | ---------- | ------ | ----- | -------- | ------ | ------------- | ---------- | ------- |
| informed | real-world | applications |     | to improve |     | learners’ | outcomes | in         |        |       |          |        |               |            |         |
misuseofintelligenttutoringsystems,”inIntelligentTutoringSystems:
AI-driven education.
7thInternationalConference,ITS2004,Maceio´,Alagoas,Brazil,August
|     |     |     |     |     |     |     |     | 30-September3,2004.Proceedings7. |     |     |     |     | Springer,2004,pp.531–540. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
Acknowledgments [17] M. Saarela, “Automatic knowledge discovery from sparse and large-
|           |     |           |     |               |     |           |           | scale | educational | data: | case | finland,” | Ph.D. dissertation, |     | University of |
| --------- | --- | --------- | --- | ------------- | --- | --------- | --------- | ----- | ----------- | ----- | ---- | --------- | ------------------- | --- | ------------- |
| Our study | was | supported | by  | the Institute | of  | Education | Sciences, |       |             |       |      |           |                     |     |               |
Jyva¨skyla¨,2017.
| U.S. Department |     | of Education, |     | through | Grant | R305A200413 | and |               |     |          |             |     |         |                 |          |
| --------------- | --- | ------------- | --- | ------- | ----- | ----------- | --- | ------------- | --- | -------- | ----------- | --- | ------- | --------------- | -------- |
|                 |     |               |     |         |       |             |     | [18] J. Greer | and | M. Mark, | “Evaluation |     | methods | for intelligent | tutoring |
R305A190522toTheUniversityofMemphis.Theopinionsexpressed
|           |        |         |        |               |     |          |               | systems | revisited,” |     | International | Journal | of  | Artificial | Intelligence in |
| --------- | ------ | ------- | ------ | ------------- | --- | -------- | ------------- | ------- | ----------- | --- | ------------- | ------- | --- | ---------- | --------------- |
| are those | of the | authors | and do | not represent |     | views of | the Institute |         |             |     |               |         |     |            |                 |
Education,vol.26,no.1,pp.387–392,2016.
or the U.S. Department of Education. We also extend our sincere [19] M. Baudin, A. Dutfoy, B. Iooss, and A.-L. Popelin, “Openturns: An
gratitudetoProf.PhilipI.PavlikJr.fromtheUniversityofMemphis industrial software for uncertainty quantification in simulation,” in
andProf.ShaghayeghSahebifromtheUniversityatAlbany-SUNY Handbook of uncertainty quantification. Springer, 2017, pp. 2001–
| for their | expert | guidance | on the | tensor | factorization |     | method. We | 2038. |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ------ | ------ | ------------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
alsothankProf.MohammedYeasinfromtheUniversityofMemphis [20] C.ShortenandT.M.Khoshgoftaar,“Asurveyonimagedataaugmen-
|     |     |     |     |     |     |     |     | tation | for deep | learning,” |     |     | data, | vol. 6, no. | 1, pp. 1–48, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | --- | ----- | ----------- | ------------ |
for his critical suggestions on the divergence measurement method Journal of big
2019.
| used in | this study. | Additionally, |     | we  | express | our heartfelt | thanks |     |     |     |     |     |     |     |     |
| ------- | ----------- | ------------- | --- | --- | ------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
[21] T.Emmanuel,T.Maupong,D.Mpoeleng,T.Semong,B.Mphago,and
| to Prof. | Kenneth | R. Koedinger |     | of Carnegie | Mellon |     | University for |     |     |     |     |     |     |     |     |
| -------- | ------- | ------------ | --- | ----------- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
O.Tabona,“Asurveyonmissingdatainmachinelearning,”Journalof
his invaluable insights on knowledge tracing and simulations, which BigData,vol.8,no.1,pp.1–37,2021.
significantly enriched this study. [22] N. Thai-Nghe, L. Drumond, T. Horva´th, A. Krohn-Grimberghe,
|     |     |     |     |     |     |     |     | A. Nanopoulos, |         | and           | L. Schmidt-Thieme, |     | “Factorization |             | techniques for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------- | ------------------ | --- | -------------- | ----------- | -------------- |
|     |     |     |     |     |     |     |     | predicting     | student | performance,” |                    | in  | Educational    | recommender | systems        |
References
|     |     |     |     |     |     |     |     | and | technologies: | Practices |     | and challenges. |     | IGI Global, | 2012, pp. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | --------------- | --- | ----------- | --------- |
129–153.
[1] T.Dom´ınguez-Bolan˜o,V.Barral,C.J.Escudero,andJ.A.Garc´ıa-Naya,
[23] A.R.T.Donders,G.J.VanDerHeijden,T.Stijnen,andK.G.Moons,“A
“AnIoTsystemforasmartcampus:Challengesandsolutionsillustrated
gentleintroductiontoimputationofmissingvalues,”Journalofclinical
overseveralreal-worldusecases,”InternetofThings,vol.25,p.101099,
epidemiology,vol.59,no.10,pp.1087–1091,2006.
2024.
[2] B.Tabuenca,M.Uche-Soria,W.Greller,D.Herna´ndez-Leo,P.Balcells- [24] Z. Zhang, “Missing data imputation: focusing on single imputation,”
Annalsoftranslationalmedicine,vol.4,no.1,2016.
Falgueras,P.Gloor,andJ.Garbajosa,“Greeningsmartlearningenviron-
[25] D.B.Rubin,“Multipleimputationsinsamplesurveys-aphenomenolog-
mentswithArtificialIntelligenceofThings,”InternetofThings,vol.25,
|     |     |     |     |     |     |     |     | ical | Bayesian | approach | to nonresponse,” |     | in Proceedings |     | of the survey |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | -------- | ---------------- | --- | -------------- | --- | ------------- |
p.101051,2024.
researchmethodssectionoftheAmericanStatisticalAssociation,vol.1.
[3] A.C.Graesser,X.Hu,andR.Sottilare,“Intelligenttutoringsystems,”
inInternationalhandbookofthelearningsciences. Routledge,2018, AmericanStatisticalAssociationAlexandria,VA,USA,1978,pp.20–34.
|     |     |     |     |     |     |     |     | [26] ——, | “Assignment |     | to treatment | group | on the | basis of | a covariate,” |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------------ | ----- | ------ | -------- | ------------- |
pp.246–255.
JournalofeducationalStatistics,vol.2,no.1,pp.1–26,1977.
| [4] A. C. | Graesser, | S. Lu, | G. T. | Jackson, | H. H. | Mitchell, | M. Ventura, |            |        |        |          |       |            |              |         |
| --------- | --------- | ------ | ----- | -------- | ----- | --------- | ----------- | ---------- | ------ | ------ | -------- | ----- | ---------- | ------------ | ------- |
|           |           |        |       |          |       |           |             | [27] P. I. | Pavlik | Jr, H. | Cen, and | K. R. | Koedinger, | “Performance | Factors |
A.Olney,andM.M.Louwerse,“Autotutor:Atutorwithdialogueinnat-
urallanguage,”BehaviorResearchMethods,Instruments,&Computers, Analysis–ANewAlternativetoKnowledgeTracing,”OnlineSubmission,
| vol.36,pp.180–192,2004. |     |     |     |     |     |     |     | 2009.   |              |     |               |     |       |         |                 |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------------- | --- | ----- | ------- | --------------- |
|                         |     |     |     |     |     |     |     | [28] M. | V. Yudelson, | K.  | R. Koedinger, | and | G. J. | Gordon, | “Individualized |
[5] K.R.Koedinger,A.Corbettetal.,Cognitivetutors:Technologybringing
|                                 |     |     |     |     |          |     |     | bayesian | knowledge |     | tracing | models,” | in Artificial | Intelligence | in Edu- |
| ------------------------------- | --- | --- | --- | --- | -------- | --- | --- | -------- | --------- | --- | ------- | -------- | ------------- | ------------ | ------- |
| learningsciencestotheclassroom. |     |     |     |     | na,2006. |     |     |          |           |     |         |          |               |              |         |
cation:16thInternationalConference,AIED2013,Memphis,TN,USA,
[6] P.I.PavlikJrandL.Zhang,“UsingautoKCandInteractionsinLogistic
KnowledgeTracing,”GranteeSubmission,2022. July9-13,2013.Proceedings16. Springer,2013,pp.171–180.
[7] L.G.EglingtonandP.I.PavlikJr,“Howtooptimizestudentlearning [29] S. Sahebi, Y.-R. Lin, and P. Brusilovsky, “Tensor Factorization for
StudentModelingandPerformancePredictioninUnstructuredDomain,”
| using | student | models | that adapt | rapidly | to  | individual | differences,” |     |     |     |     |     |     |     |     |
| ----- | ------- | ------ | ---------- | ------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
InternationalEducationalDataMiningSociety,2016.
| International |     | Journal | of Artificial | Intelligence |     | in Education, | vol. 33, |         |           |     |              |             |     |            |               |
| ------------- | --- | ------- | ------------- | ------------ | --- | ------------- | -------- | ------- | --------- | --- | ------------ | ----------- | --- | ---------- | ------------- |
|               |     |         |               |              |     |               |          | [30] M. | Jovanovic | and | M. Campbell, | “Generative |     | Artificial | Intelligence: |
no.3,pp.497–518,2023.
[8] K. R. Koedinger, A. T. Corbett, and C. Perfetti, “The Knowledge- TrendsandProspects,”Computer,vol.55,no.10,pp.107–112,2022.
|     |     |     |     |     |     |     |     | [31] I. Goodfellow, |     | J. Pouget-Abadie, |     | M.  | Mirza, B. | Xu, D. | Warde-Farley, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------------- | --- | --- | --------- | ------ | ------------- |
Learning-Instructionframework:Bridgingthescience-practicechasmto
|     |     |     |     |     |     |     |     | S. Ozair, | A.  | Courville, | and | Y. Bengio, | “Generative | Adversarial | Net- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | ---------- | ----------- | ----------- | ---- |
enhancerobuststudentlearning,”Cognitivescience,vol.36,no.5,pp.
|     |     |     |     |     |     |     |     | works,” | Communications |     | of  | the ACM, | vol. 63, | no. 11, | pp. 139–144, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | --- | -------- | -------- | ------- | ------------ |
757–798,2012.
2020.
| [9] S. Pandey | and | G.  | Karypis, | “A self-attentive |     | model | for knowledge |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | -------- | ----------------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tracing,”arXivpreprintarXiv:1907.06837,2019. [32] ——, “Generative Adversarial Nets,” Advances in neural information
processingsystems,vol.27,2014.
[10] W.Lee,J.Chun,Y.Lee,K.Park,andS.Park,“Contrastivelearningfor
[33] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez,
knowledgetracing,”inProceedingsoftheACMWebConference2022,
|     |     |     |     |     |     |     |     |  L. Kaiser, | and | I. Polosukhin, |     | “Attention | is all | you need,” | Advances in |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | ---------- | ------ | ---------- | ----------- |
2022,pp.2330–2338.
neuralinformationprocessingsystems,vol.30,2017.
[11] X.Wang,S.Zhao,L.Guo,L.Zhu,C.Cui,andL.Xu,“GraphCA:Learn-
ingfromGraphCounterfactualAugmentationforKnowledgeTracing,” [34] P.Morales-Alvarez,W.Gong,A.Lamb,S.Woodhead,S.PeytonJones,
|     |     |     |     |     |     |     |     | N. Pawlowski, |     | M.  | Allamanis, | and C. | Zhang, | “Simultaneous | missing |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ---------- | ------ | ------ | ------------- | ------- |
IEEE/CAAJournalofAutomaticaSinica,vol.10,no.11,pp.2108–2123,
|       |     |     |     |     |     |     |     | value  | imputation  | and | structure  | learning | with | groups,” |              |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---------- | -------- | ---- | -------- | ------------ |
| 2023. |     |     |     |     |     |     |     |        |             |     |            |          |      |          | Advances in  |
|       |     |     |     |     |     |     |     | Neural | Information |     | Processing | Systems, | vol. | 35, pp.  | 20011–20024, |
2022.

JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES 17
[35] Z. Li, L. Shi, J. Wang, A. I. Cristea, and Y. Zhou, “Sim-GAIL: A [57] K.Hemachandran,P.Verma,P.Pareek,N.Arora,K.V.R.Kumar,T.A.
generativeadversarialimitationlearningapproachofstudentmodelling Ahanger,A.A.Pise,andR.Ratna,“ArtificialIntelligence:AUniversal
for intelligent tutoring systems,” Neural Computing and Applications, VirtualTooltoAugmentTutoringinHigherEducation,”Computational
vol.35,no.34,pp.24369–24388,2023. IntelligenceandNeuroscience,vol.2022,2022.
[36] L. Zhang, J. Lin, C. Borchers, J. Sabatini, J. Hollander, M. Cao, and [58] J. Achiam, S.Adler, S. Agarwal, L.Ahmad, I. Akkaya, F.L. Aleman,
X.Hu,“PredictingLearningPerformancewithLargeLanguageModels: D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “GPT-4
AStudyinAdultLiteracy,”arXivpreprintarXiv:2403.14668,2024. TechnicalReport,”arXivpreprintarXiv:2303.08774,2023.
[37] A. C. Graesser, Z. Cai, W. O. Baer, A. M. Olney, X. Hu, M. Reed, [59] W.Dai,J.Lin,H.Jin,T.Li,Y.-S.Tsai,D.Gasˇevic´,andG.Chen,“Can
and D. Greenberg, “Reading comprehension lessons in AutoTutor for Large Language Models Provide Feedback to Students? A Case Study
the Center for the Study of Adult Literacy,” in Adaptive educational on ChatGPT,” in 2023 IEEE International Conference on Advanced
technologiesforliteracyinstruction. Routledge,2016,pp.288–293. LearningTechnologies(ICALT). IEEE,2023,pp.323–325.
[38] A. C. Graesser, Z. Cai, B. Morgan, and L. Wang, “Assessment with [60] S. C. E. Fung, M. F. Wong, and C. W. Tan, “Automatic Feedback
computeragentsthatengageinconversationaldialoguesandtrialogues Generation on K-12 Students’ Data Science Education by Prompting
with learners,” Computers in Human Behavior, vol. 76, pp. 607–616, Cloud-based Large Language Models,” in Proceedings of the Eleventh
2017. ACMConferenceonLearning@Scale,2024,pp.255–258.
[39] J.Sabatini,A.C.Graesser,J.Hollander,andT.O’Reilly,“Aframework [61] C. W. Tan, “Large Language Model-Driven Classroom Flipping: Em-
ofliteracydevelopmentandhowAIcantransformtheoryandpractice,” powering Student-Centric Peer Questioning with Flipped Interaction,”
British Journal of Educational Technology, vol. 54, no. 5, pp. 1174– arXivpreprintarXiv:2311.14708,2023.
1203,2023. [62] C. N. Hang, C. W. Tan, and P.-D. Yu, “MCQGen: A Large Language
[40] P.Brusilovsky,S.Sosnovsky,andK.Thaker,“Thereturnofintelligent Model-DrivenMCQGeneratorforPersonalizedLearning,”IEEEAccess,
textbooks,”AIMagazine,vol.43,no.3,pp.337–340,2022. 2024.
[41] A. C. Graesser, X. Hu, and D. S. McNamara, “Computerized Learn- [63] J.M.Markel,S.G.Opferman,J.A.Landay,andC.Piech,“GPTeach:
ing Environments That Incorporate Research in Discourse Psychology, Interactive TA Training with GPT-based Students,” in Proceedings of
CognitiveScience,andComputationalLinguistics,”2005. thetenthacmconferenceonlearning@scale,2023,pp.226–236.
[42] G. A. Frishkoff, K. Collins-Thompson, S. Nam, L. Hodges, and S. A. [64] D. T. K. Ng, C. W. Tan, and J. K. L. Leung, “Empowering student
Crossley, “Dynamic Support of Contextual Vocabulary Acquisition for self-regulated learning and science education through ChatGPT: A
Reading(DSCoVAR):Anintelligenttutorforcontextualwordlearning,” pioneering pilot study,” British Journal of Educational Technology,
inAdaptiveeducationaltechnologiesforliteracyinstruction. Routledge, 2024.
2016,pp.69–81. [65] E.Latif,Y.Zhou,S.Guo,Y.Gao,L.Shi,M.Nayaaba,G.Lee,L.Zhang,
[43] B.J.MeyerandK.K.Wijekumar,“Intelligenttutoringofthestructure A. Bewersdorff, L. Fang et al., “A Systematic Assessment of OpenAI
strategy:Areadingstrategytutor,”inAdaptiveeducationaltechnologies o1-Preview for Higher Order Thinking in Education,” arXiv preprint
forliteracyinstruction. Routledge,2016,pp.82–103. arXiv:2410.21287,2024.
[44] W.Morris,S.Crossley,L.Holmes,C.Ou,M.Dascalu,andD.McNa- [66] N. Liu, Z. Wang, R. Baraniuk, and A. Lan, “Open-ended Knowledge
mara,“FormativeFeedbackonStudent-AuthoredSummariesinIntelli- Tracing for Computer Science Education,” in Proceedings of the 2022
gent Textbooks Using Large Language Models,” International Journal Conference on Empirical Methods in Natural Language Processing,
ofArtificialIntelligenceinEducation,pp.1–22,2024. 2022.
[45] C.Xiao,S.X.Xu,K.Zhang,Y.Wang,andL.Xia,“Evaluatingreading [67] J. Hollander, J. Sabatini, A. Graesser, D. Greenberg, T. O’Reilly, and
comprehensionexercisesgeneratedbyLLMs:AshowcaseofChatGPT J. Frijters, “Importance of learner characteristics in intelligent tutoring
in education applications,” in Proceedings of the 18th Workshop on foradultliteracy,”DiscourseProcesses,vol.60,no.4-5,pp.397–409,
Innovative Use of NLP for Building Educational Applications (BEA 2023.
2023),2023,pp.610–625. [68] A. T. Corbett and J. R. Anderson, “Knowledge tracing: Modeling the
[46] L. Zhang, J. Lin, Z. Kuang, S. Xu, and X. Hu, “SPL: A Socratic acquisitionofproceduralknowledge,”Usermodelinganduser-adapted
Playground for Learning Powered by Large Language Mode,” arXiv interaction,vol.4,pp.253–278,1994.
preprintarXiv:2406.13919,2024. [69] C. M. Conway and M. H. Christiansen, “Sequential learning in non-
[47] N.T.NgheandL.Schmidt-Thieme,“Factorizationforecastingapproach humanprimates,”Trendsincognitivesciences,vol.5,no.12,pp.539–
for user modeling,” Journal of Computer Science and Cybernetics, 546,2001.
vol.31,no.2,pp.133–148,2015. [70] M.Ramscar,“Learningandthereplicabilityofprimingeffects,”Current
[48] T.-N.DoanandS.Sahebi,“Rank-basedtensorfactorizationforstudent OpinioninPsychology,vol.12,pp.80–84,2016.
performance prediction,” in 12th International Conference on Educa- [71] P. I. Pavlik, L. G. Eglington, and L. M. Harrell-Williams, “Logistic
tionalDataMining(EDM),2019. knowledge tracing: A constrained framework for learner modeling,”
[49] S.Zhao,C.Wang,andS.Sahebi,“Modelingknowledgeacquisitionfrom IEEE Transactions on Learning Technologies, vol. 14, no. 5, pp. 624–
multiple learning resource types,” arXiv preprint arXiv:2006.13390, 639,2021.
2020. [72] Z. A. Pardos and N. T. Heffernan, “Modeling Individualization in a
[50] C. Wang, S. Sahebi, S. Zhao, P. Brusilovsky, and L. O. Moraes, BayesianNetworksImplementationofKnowledgeTracing,”inInterna-
“Knowledgetracingforcomplexproblemsolving:Granularrank-based tional conference on user modeling, adaptation, and personalization.
tensor factorization,” in Proceedings of the 29th ACM conference on Springer,2010,pp.255–266.
usermodeling,adaptationandpersonalization,2021,pp.179–188. [73] A.S.Lan,C.Studer,andR.G.Baraniuk,“Quantizedmatrixcompletion
[51] N. Thai-Nghe, T. Horva´th, L. Schmidt-Thieme et al., “Factorization forpersonalizedlearning,”arXivpreprintarXiv:1412.5968,2014.
Models for Forecasting Student Performance,” in EDM. Eindhoven, [74] A.NewellandP.S.Rosenbloom,“Mechanismsofskillacquisitionand
2011,pp.11–20. thelawofpractice.”CARNEGIE-MELLONUNIVPITTSBURGHPA
[52] A.Antoniou,A.Storkey,andH.Edwards,“Dataaugmentationgenera- DEPTOFCOMPUTERSCIENCE,Tech.Rep.,1980.
tiveadversarialnetworks,”arXivpreprintarXiv:1711.04340,2017. [75] R.DeKeyser,“Skillacquisitiontheory,”inTheoriesinsecondlanguage
[53] A. Aggarwal, M. Mittal, and G. Battineni, “Generative adversarial acquisition. Routledge,2020,pp.83–104.
network:Anoverviewoftheoryandapplications,”InternationalJournal [76] D. Arthur and S. Vassilvitskii, “K-means++ the advantages of careful
ofInformationManagementDataInsights,vol.1,no.1,p.100004,2021. seeding,” in Proceedings of the eighteenth annual ACM-SIAM sympo-
[54] G. Mariani, F. Scheidegger, R. Istrate, C. Bekas, and C. Malossi, siumonDiscretealgorithms,2007,pp.1027–1035.
“BAGAN: Data Augmentation with Balancing GAN,” arXiv preprint [77] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V.
arXiv:1803.09655,2018. Le, D. Zhou et al., “Chain-of-Thought Prompting Elicits Reasoning in
[55] M. Frid-Adar, E. Klang, M. Amitai, J. Goldberger, and H. Greenspan, Large Language Models,” Advances in Neural Information Processing
“SyntheticdataaugmentationusingGANforimprovedliverlesionclas- Systems,vol.35,pp.24824–24837,2022.
sification,” in 2018 IEEE 15th international symposium on biomedical [78] N. Thai-Nghe, N. Thai-Nghe et al., “Predicting Student Performance
imaging(ISBI2018). IEEE,2018,pp.289–293. in an Intelligent Tutoring System,” Ph.D. dissertation, University of
[56] S.-W.Huang,C.-T.Lin,S.-P.Chen,Y.-Y.Wu,P.-H.Hsu,andS.-H.Lai, Hildesheim,2012.
“AugGAN: Cross Domain Adaptation with GAN-based Data Augmen- [79] L. Xiong, X. Chen, T.-K. Huang, J. Schneider, and J. G. Carbonell,
tation,”inProceedingsoftheEuropeanConferenceonComputerVision “Temporalcollaborativefilteringwithbayesianprobabilistictensorfac-
(ECCV),2018,pp.718–731. torization,” in Proceedings of the 2010 SIAM international conference
ondatamining. SIAM,2010,pp.211–222.

| JOURNALOFIEEETRANSACTIONSONLEARNINGTECHNOLOGIES |     |     |     |     |     |     |     |     |     |     |     |     |     | 18  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[80] Y.Rubner,C.Tomasi,andL.J.Guibas,“Theearthmover’sdistanceas is a PhD student at the Human-
|     |     |     |     |     |     |     |     |     |     | Conrad | Borchers |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- |
ametricforimageretrieval,”Internationaljournalofcomputervision, Computer Interaction Institute (HCII) at Carnegie
vol.40,pp.99–121,2000. Mellon University’s School of Computer Science.
[81] O.PeleandM.Werman,“Fastandrobustearthmover’sdistances,”in Heisbroadlyinterestedinstudyingtheeffectiveness
|                  |           |               |          |            |              |         | vision. IEEE, |     |     | of educational      |     | technologies | and pathways | through |
| ---------------- | --------- | ------------- | -------- | ---------- | ------------ | ------- | ------------- | --- | --- | ------------------- | --- | ------------ | ------------ | ------- |
| 2009             | IEEE 12th | international |          | conference | on computer  |         |               |     |     |                     |     |              |              |         |
| 2009,pp.460–467. |           |               |          |            |              |         |               |     |     | datasciencemethods. |     |              |              |         |
| [82] X. Wan,     | W. Wang,  | J.            | Liu, and | T. Tong,   | “Estimating  | the     | sample mean   |     |     |                     |     |              |              |         |
| and standard     |           | deviation     | from     | the sample | size,        | median, | range and/or  |     |     |                     |     |              |              |         |
| interquartile    | range,”   | BMC           | medical  | research   | methodology, |         | vol. 14, pp.  |     |     |                     |     |              |              |         |
1–13,2014.
| [83] R. Pfister, | K.  | A. Schwarz, | M.  | Janczyk, | R. Dale, | and | J. B. Freeman, |     |     |     |     |             |              |      |
| ---------------- | --- | ----------- | --- | -------- | -------- | --- | -------------- | --- | --- | --- | --- | ----------- | ------------ | ---- |
|                  |     |             |     |          |          |     |                |     |     |     |     | is a recent | PhD graduate | from |
“Good things peak in pairs: a note on the bimodality coefficient,” Daniel Weitekamp
CarnegieMellon’sHuman-ComputerInteractionIn-
Frontiersinpsychology,vol.4,p.700,2013.
stitute.Danielstudiessimulationsofhumanlearning
[84] T.-N.Nguyen,“Predictingstudentperformanceinanintelligenttutoring
system,”Ph.D.dissertation,StiftungUniversita¨tHildesheim,2011. that can learn directly from educational technology
[85] A. C. Graesser and D. S. McNamara, “Computational analyses of or interactively from a human instructor. His re-
|     |     |     |     |     |     |     |     |     |     | search | has been | applied to | building computational |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | ---------------------- | --- |
multileveldiscoursecomprehension,”Topicsincognitivescience,vol.3,
modelsoflearning,andforinteractivetasklearning
no.2,pp.371–398,2011.
|     |     |     |     |     |     |     |     |     |     | applications |     | where non-programmers | build | whole |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------------- | ----- | ----- |
[86] G.Shi,P.PavlikJr,andA.Graesser,“UsinganAdditiveFactorModel
andPerformanceFactorAnalysistoAssessLearningGainsinaTutoring programs by interactively teaching an AI. Daniel’s
SystemtoHelpAdultswithReadingDifficulties,”GranteeSubmission, recent dissertation work shows that untrained users
canbuild100%accurateintelligenttutoringsystems
2017.
inabout20minutesbyinteractivelyteachinghisAI,calledAI2T.
[87] R.LiuandK.R.Koedinger,“TowardsReliableandValidMeasurement
of Individualized Student Parameters,” International Educational Data Meng Cao is a postdoctoral researcher in the
MiningSociety,2017.
|     |     |     |     |     |     |     |     |     |     | Human-Computer |     | Interaction | Institute | at Carnegie |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --------- | ----------- |
[88] J.Yoon,J.Jordon,andM.Schaar,“GAIN:Missingdataimputationus-
|     |     |     |     |     |     |     |     |     |     | Mellon | University, | Pittsburgh, | PA, USA. | She re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----------- | -------- | ------- |
inggenerativeadversarialnets,”inInternationalconferenceonmachine
|     |     |     |     |     |     |     |     |     |     | ceived | her Ph.D. | in Experimental | Psychology | from |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --------------- | ---------- | ---- |
learning. PMLR,2018,pp.5689–5698. the Department of Psychology at the University of
[89] L. Zhang, M. Yeasin, J. Lin, F. Havugimana, and X. Hu, “Generative Memphis. Her research interests include computa-
AdversarialNetworksforImputingSparseLearningPerformance,”arXiv
tionalmodeling,optimallearning,adaptivelearning,
preprintarXiv:2407.18875,2024.
andcategorylearning.
[90] D.Bank,N.Koenigstein,andR.Giryes,“Autoencoders,”Machinelearn-
| ing for | data science | handbook: |     | data | mining and | knowledge | discovery |     |     |     |     |     |     |     |
| ------- | ------------ | --------- | --- | ---- | ---------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
handbook,pp.353–374,2023.
JohnHollanderisanAssistantProfessorintheDe-
partmentofPsychologyandCounselingatArkansas
BiographySection
StateUniversity.Hisresearchinterestsincludepsy-
cholinguistics,computationalsemantics,andthesci-
|     |     | Liang       | Zhang | is     | a PhD candidate |     | in Computer    |     |     | enceofreading. |     |     |     |     |
| --- | --- | ----------- | ----- | ------ | --------------- | --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- |
|     |     | Engineering |       | at the | Department      | of  | Electrical and |     |     |                |     |     |     |     |
ComputerEngineering,UniversityofMemphis.He
currentlyservesasaresearchassistantattheInstitute
|     |     | for     | Intelligent | Systems  | (IIS)   | at University     | of Mem- |     |     |     |     |     |     |     |
| --- | --- | ------- | ----------- | -------- | ------- | ----------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | phis    | and a       | visiting | scholar | at Educational    | Testing |     |     |     |     |     |     |     |
|     |     | Service | (ETS).      | He       | was an  | intern researcher | at the  |     |     |     |     |     |     |     |
Human-Computer Interaction Institute at Carnegie is Chair Professor of Learning Sci-
|     |     |     |     |     |     |     |     |     |     | Xiangen | Hu  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
Mellon University from May to August 2023, and ences and Technologies at Hong Kong Polytechnic
atthemachinelearninggroupatNECLaboratories University. He received his Doctor of Philosophy
America from May to August 2024. His research degreeinCognitivePsychologyfromtheUniversity
focuses on human-computer interaction, including learning analytics, educa- ofCalifornia,Irvinein1991and1993respectively.
tionaldatamining,andGenAIfordataimputationandaugmentationinAI- He took up an Assistant Professorship at The Uni-
education.HereceivedtheBestFullPaperAwardatHCII’24. versity of Memphis in 1993 and was promoted to
|     |     |          |     |                                     |     |     |     |     |     | Associate  | Professor | in 2000    | and Professor       | in the |
| --- | --- | -------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ---------- | --------- | ---------- | ------------------- | ------ |
|     |     |          |     |                                     |     |     |     |     |     | Department | of        | Psychology | in 2009. Meanwhile, | he     |
|     |     | Jionghao |     | Lin isanAssistantProfessorintheFac- |     |     |     |     |     |            |           |            |                     |        |
hasbeenappointedProfandDeanoftheSchoolof
ulty of Education at the University of Hong Kong. PsychologyintheCentralChinaNormalUniversity
Previously,hewasaPostdoctoralResearcheratthe since 2016 on a visiting basis where he has established good connections
Human-Computer Interaction Institute at Carnegie with the Chinese mainland. He joined PolyU in Dec 2023 as Director of
MellonUniversity,Pittsburgh,PA,USA,from2023
|     |     |     |     |     |     |     |     | the Institute | for Higher | Education | Research | and Development. | His | research |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --------- | -------- | ---------------- | --- | -------- |
to2025.HereceivedhisPh.D.inComputerScience
|     |     |                                               |     |     |     |     |     | areas include        | Mathematical | Psychology, |     | Research Design | and Statistics, | and |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | -------------------- | ------------ | ----------- | --- | --------------- | --------------- | --- |
|     |     | fromMonashUniversity,Clayton,VIC,Australia,in |     |     |     |     |     | CognitivePsychology. |              |             |     |                 |                 |     |
2023.Hisresearchinterestsincludelearningscience,
naturallanguageprocessing,datamining,andappli- is a Distinguished University
|     |     |     |     |     |     |     |     |     |     | Arthur | C. Graesser |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --- | --- |
cations of generative artificial intelligence in edu- ProfessorintheDepartmentofPsychologyandthe
cation.Hisworkhasbeenpublishedininternational Institute of Intelligent Systems at the University of
journalsandconferencesandrecognizedwithawards,includingtheBestPaper MemphisandisanHonoraryResearchFellowinthe
|                   |     |         |     |          |         |           |       |     |     | Department                                 | of  | Education at | the University | of Ox- |
| ----------------- | --- | ------- | --- | -------- | ------- | --------- | ----- | --- | --- | ------------------------------------------ | --- | ------------ | -------------- | ------ |
| Award at HCII’24, |     | EDM’24, | and | ICMI’19, | and the | Best Demo | Award | at  |     |                                            |     |              |                |        |
| AIED’23.          |     |         |     |          |         |           |       |     |     | ford.HereceivedhisPh.D.inpsychologyfromthe |     |              |                |        |
UniversityofCaliforniaatSanDiego.Art’sprimary
researchinterestsareincognitivescience,discourse
JohnSabatiniisaDistinguishedResearchProfessor
processing,andthelearningsciences.Morespecific
intheDepartmentofPsychologyandtheInstitutefor interestsincludeknowledgerepresentation,question
Intelligent Systems at the University of Memphis. asking and answering, tutoring, text comprehen-
He was formerly a Principal Research Scientist at sion, inference generation, conversation, reading, problem solving, memory,
Educational Testing Service, specializing in read- emotions, computational linguistics, artificial intelligence, human-computer
|     |     | ing | literacy, | assessment, | cognitive | psychology, | and |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | ----------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
interaction,andlearningtechnologieswithanimatedconversationalagents.
|     |     | educational |     | technology, | with | a focus | on adults and |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | ----------- | ---- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
adolescents.