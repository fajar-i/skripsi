| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |        |     |     |     |           |     |              |          |     |         |     |     |           |     | 1   |
| ----------------------------------------------- | ------ | --- | --- | --- | --------- | --- | ------------ | -------- | --- | ------- | --- | --- | --------- | --- | --- |
| A                                               | Survey |     |     | of  | Knowledge |     |              | Tracing: |     | Models, |     |     | Variants, |     |     |
|                                                 |        |     |     |     |           | and | Applications |          |     |         |     |     |           |     |     |
Shuanghong Shen, Qi Liu, Member, IEEE, Zhenya Huang, Member, IEEE, Yonghe Zheng,
|     |         |     |      | Member, | IEEE, |         |     | Member, | IEEE, |            |     |       | Fellow, | IEEE |     |
| --- | ------- | --- | ---- | ------- | ----- | ------- | --- | ------- | ----- | ---------- | --- | ----- | ------- | ---- | --- |
|     | Minghao |     | Yin, |         |       | Minjuan |     | Wang,   |       | and Enhong |     | Chen, |         |      |     |
Abstract—Modernonlineeducationhasthecapacitytoprovide videsadegreeofflexibilitythatconventionaleducationcannot
intelligent educational services by automatically analyzing sub- match, which enables teaching and learning to occur at any
4202 rpA 11  ]YC.sc[  4v60151.5012:viXra stantial amounts of student behavioral data. Knowledge Tracing time and any place. Meanwhile, online learning systems (e.g.,
| (KT) | is one | of the | fundamental |     | tasks | for student | behavioral |     |     |     |     |     |     |     |     |
| ---- | ------ | ------ | ----------- | --- | ----- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Coursera,ASSISTment)[4,5,6]haveproventobeevenmore
| data analysis, |        | aiming                | to monitor |     | students’ | evolving | knowledge |           |      |             |          |         |       |      |           |
| -------------- | ------ | --------------------- | ---------- | --- | --------- | -------- | --------- | --------- | ---- | ----------- | -------- | ------- | ----- | ---- | --------- |
|                |        |                       |            |     |           |          |           | effective | than | traditional | learning | styles, | since | they | can offer |
| state          | during | their problem-solving |            |     | process.  | In       | recent    | years, a  |      |             |          |         |       |      |           |
substantial number of studies have concentrated on this rapidly more intelligent educational services, such as recommending
growing field, significantly contributing to its advancements. In individualizedlearningresourcestostudents[7,8].Toprovide
this survey, we will conduct a thorough investigation of these theseintelligentservices,onlinelearningsystemscontinuously
| progressions. |          | Firstly, | we present      | three   | types         | of fundamental |      | KT       |              |        |            |           |                |       |           |
| ------------- | -------- | -------- | --------------- | ------- | ------------- | -------------- | ---- | -------- | ------------ | ------ | ---------- | --------- | -------------- | ----- | --------- |
|               |          |          |                 |         |               |                |      | record   | a massive    | amount | of         | available | data           | about | student-  |
| models        | with     | distinct | technical       | routes. | Subsequently, |                | we   | review   |              |        |            |           |                |       |           |
|               |          |          |                 |         |               |                |      | system   | interactions | (e.g., | responding |           | to exercises), |       | which can |
| extensive     | variants | of       | the fundamental |         | KT            | models         | that | consider |              |        |            |           |                |       |           |
morestringentlearningassumptions.Moreover,thedevelopment be further mined to assess their knowledge levels, learn-
of KT cannot be separated from its applications, thereby we ing preferences, and other attributes. Specifically, Knowledge
presenttypicalKTapplicationsinvariousscenarios.Tofacilitate Tracing (KT) [9] is one of the most fundamental and critical
| the work     | of        | researchers  |             | and practitioners |               | in         | this field,   | we        |           |              |           |                |          |              |       |
| ------------ | --------- | ------------ | ----------- | ----------------- | ------------- | ---------- | ------------- | --------- | --------- | ------------ | --------- | -------------- | -------- | ------------ | ----- |
|              |           |              |             |                   |               |            |               | tasks for | analyzing | students’    |           | learning       | behavior | data,        | which |
| have         | developed | two          | open-source |                   | algorithm     | libraries: | EduData       |           |           |              |           |                |          |              |       |
|              |           |              |             |                   |               |            |               | aims to   | explore   | the recorded |           | student-system |          | interactions | to    |
| that enables |           | the download |             | and               | preprocessing |            | of KT-related |           |           |              |           |                |          |              |       |
|              |           |              |             |                   |               |            |               | monitor   | their     | evolving     | knowledge | states         | [10,     | 11].         |       |
| datasets,    | and       | EduKTM       | that        | provides          | an            | extensible | and           | unified   |           |              |           |                |          |              |       |
implementation of existing mainstream KT models. Finally, we Fig. 1 presents a simple schematic diagram of knowledge
discuss potential directions for future research in this rapidly tracing. During the learning process, online learning systems
| growing | field. | We hope | that | the current |     | survey | will assist | both         |     |                  |     |          |            |     |           |
| ------- | ------ | ------- | ---- | ----------- | --- | ------ | ----------- | ------------ | --- | ---------------- | --- | -------- | ---------- | --- | --------- |
|         |        |         |      |             |     |        |             | continuously |     | record students’ |     | learning | behavioral |     | data, in- |
researchersandpractitionersinfosteringthedevelopmentofKT,
|         |              |     |            |       |              |     |          | cluding   | exercises   | and   | their related | knowledge    |     | concepts    | (e.g., |
| ------- | ------------ | --- | ---------- | ----- | ------------ | --- | -------- | --------- | ----------- | ----- | ------------- | ------------ | --- | ----------- | ------ |
| thereby | benefiting   | a   | broader    | range | of students. |     |          |           |             |       |               |              |     |             |        |
|         |              |     |            |       |              |     |          | equality, | inequality, | plane | vector,       | probability, |     | represented | in     |
| Index   | Terms—Online |     | Education, |       | Knowledge    |     | Tracing, | Educa-    |             |       |               |              |     |             |        |
variouscolors),andstudents’answers(i.e.,correctorincorrect
| tional | Data Mining, |     | Adaptive | Learning, | User | Modeling. |     |              |                |             |           |     |               |          |          |
| ------ | ------------ | --- | -------- | --------- | ---- | --------- | --- | ------------ | -------------- | ----------- | --------- | --- | ------------- | -------- | -------- |
|        |              |     |          |           |      |           |     | responses).  | A              | substantial | amount    | of  | supplementary |          | informa- |
|        |              |     |          |           |      |           |     | tion is also | simultaneously |             | recorded, |     | including     | response | time,    |
I. INTRODUCTION
|     |     |     |     |     |     |     |     | opportunity | count, | and | tutor | intervention, |     | which | provides a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | ----- | ------------- | --- | ----- | ---------- |
WITH the proliferation of the Internet and mobile com- more comprehensive reflection of students’ learning process.
munication technology, online education has become Based on the collected learning data, researchers are striving
increasingly popular and is now developing at an unprece- to maintain an estimate of students’ evolving knowledge
| dented        | scale      | [1, 2,  | 3]. This       | innovative |            | style of | learning   | pro-        |               |           |           |            |           |           |           |
| ------------- | ---------- | ------- | -------------- | ---------- | ---------- | -------- | ---------- | ----------- | ------------- | --------- | --------- | ---------- | --------- | --------- | --------- |
|               |            |         |                |            |            |          |            | states. For | illustration, |           | we give   | a case     | in        | Fig. 1,   | where the |
|               |            |         |                |            |            |          |            | student’s   | prior         | knowledge | is        | quantified | as        | 0.2, 0.4, | 0.4, and  |
| S. Shen,      | and        | E. Chen | (corresponding |            | author)    | are with | the School | of          |               |           |           |            |           |           |           |
|               |            |         |                |            |            |          |            | 0.5 across  | four          | distinct  | knowledge |            | concepts. | The       | radar map |
| Data Science, | University |         | of Science     | and        | Technology | of       | China &    | State Key   |               |           |           |            |           |           |           |
Laboratory of Cognitive Intelligence, Hefei, Anhui, 230026, China. Email: serves as a visual representation of the student’s knowledge
closer@mail.ustc.edu.cn,cheneh@ustc.edu.cn mastery,whichprogressivelyexpandsasthestudentcontinues
Q. Liu (corresponding author), and Z. Huang are with the School of to acquire new knowledge in learning. After a period of
Computer Science and Techonology, University of Science and Technology learning,thestudent’sknowledgestatesreach0.9,0.8,0.8,and
of China & State Key Laboratory of Cognitive Intelligence & Institute of 0.7 respectively, suggesting good knowledge growth. In the
ArtificialIntelligence,HefeiComprehensiveNationalScienceCenter,Hefei,
|     |     |     |     |     |     |     |     | aforementioned |     | learning | process, | KT  | models | aim | to monitor |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | -------- | --- | ------ | --- | ---------- |
Anhui,230026,China.Email:{qiliuql,huangzhy}@ustc.edu.cn
|     |     |     |     |     |     |     |     | changes | in students’ | knowledge |     | states. | Once | we  | understand |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --------- | --- | ------- | ---- | --- | ---------- |
Y. Zheng is with the Research Institute of Science Education, Faculty students’knowledgestates,thelearningsystemcancustomize
| of Education, | Beijing | Normal |     | University, | Haidian, | Beijing, | 100875, | China.        |     |          |         |     |           |           |         |
| ------------- | ------- | ------ | --- | ----------- | -------- | -------- | ------- | ------------- | --- | -------- | ------- | --- | --------- | --------- | ------- |
|               |         |        |     |             |          |          |         | more suitable |     | learning | schemes | for | different | students, | thereby |
Email:zhengyonghe@bnu.edu.cn
|           |        |             |        |                |        |         |                 | enabling     | the     | teaching      | of students |       | in accordance |            | with their   |
| --------- | ------ | ----------- | ------ | -------------- | ------ | ------- | --------------- | ------------ | ------- | ------------- | ----------- | ----- | ------------- | ---------- | ------------ |
| M.        | Yin is | with the    | School | of Information |        | Science | and Technology, |              |         |               |             |       |               |            |              |
|           |        |             |        |                |        |         |                 | proficiency. | It      | also allows   | students    | to    | better        | comprehend | their        |
| Northeast | Normal | University, |        | Changchun,     | Jilin, | 130117, | China.          | Email:       |         |               |             |       |               |            |              |
|           |        |             |        |                |        |         |                 | learning     | process | and gradually |             | focus | on improving  |            | their skills |
ymh@nenu.edu.cn
|     |     |     |     |     |     |     |     | with poorly | mastered |     | concepts | [12, | 13]. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | -------- | ---- | ---- | --- | --- |
M. Wang is with The Education University of Hong Kong, Hong Kong Knowledge tracing has been studied for decades, with the
SAR,999077,ChinaandSanDiegoStateUniversity,SanDiego,CA92182
|     |     |     |     |     |     |     |     | first studies | tracing | back | to  | the late | 1970s. | These | initial |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ---- | --- | -------- | ------ | ----- | ------- |
USA.Email:mwang@sdsu.edu
|     |     |     |     |     |     |     |     | works primarily |     | focused | on  | confirming | the | effectiveness | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | ---------- | --- | ------------- | --- |

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |             |     |     |     |     |     |     |     |     |     |     |     | 2   |
| ----------------------------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                 |     | K n | o w l ed ge |     | k   |     |     | k   | k   |     |     | k   |     |     |     |
C o m p o n en ts 1 ：equality 2 ：inequality 3 ：plane vector 4 ：probability
|     |     |     |     |     | e   | e e | e   | e   | e e | e   | e   | e   | e   | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 1   | 2 3 | 4   | 5   | 6 7 | 8   | 9   | 10  | 11  | 12  |     |
Exercises
|     |     | Answers |     |     | ×   | √ √ | ×   | ×   | √ √ | ×   | √   | ×   | √   | √   |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Side Information response time, opportunity count, tutor intervention, engagement …
Student
|     |     |           |     |     |     |         |     |     | 0.8 |     |     |     |     | 0.9 |     |
| --- | --- | --------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |           |     |     |     | 0.7 0.7 | 0.6 | 0.7 | 0.8 | 0.8 | 0.9 | 0.9 | 0.8 |     |     |
|     |     | Knowledge |     |     | 0.2 |         |     |     |     |     |     |     |     |     |     |
State 0.5 0.4 0.5 0.5 0.5 0.8 0.4 0.6 0.4 0.6 0.4 0.7 0.4 0.9 0.4 0.9 0.4 0.9 0.3 0.8 0.4 0.80.7 0.8
|     |     |     |     |     | 0.4 | 0.4 0.4 | 0.4 | 0.4 | 0.4 0.3 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |         |     |     |         | 0.5 | 0.5 | 0.5 | 0.7 | 0.8 |     |
Fig.1. Asimpleschematicdiagramofknowledgetracing.Differentknowledgeconceptsarerepresentedindifferentcolors,whileexercisesarealsodepicted
inthecolorrelevanttotheknowledgeconcepts.Duringthelearningprocess,differentkindsofsideinformationarealsorecorded.Theevolvingprocessof
theknowledgestateisassessedbyKTmodelsandillustratedbytheradarmaps.
mastery learning [14]. To the best of our knowledge, Corbett libraries, EduData1 and EduKTM2, include most existing KT-
and Anderson [9] were the first to introduce the concept of related datasets, extensible, and unified implementations of
knowledgetracing,employingBayesiannetworkstomodelthe existingKTmodels,andrelevantresources.Finally,wediscuss
student learning process, which they referred to as Bayesian potential future research directions. In summary, this paper
Knowledge Tracing. Since then, the significance of KT has presents an extensive survey of KT that can serve as a
been recognized by a broader spectrum of researchers, and comprehensive guide for both researchers and practitioners.
increasing attention has been directed towards KT-related The remainder of this survey is structured as follows.
research. Many logistic models have been applied to KT, SectionIIpresentsanoverviewoftheKTtaskandwediscuss
including Learning Factor Analysis [15] and Performance the differences between this and previous surveys. Section III
Factor Analysis [16]. In recent years, deep learning has provides a review of the three categories of fundamental KT
greatly enhanced research into the KT task, largely due to models. Section IV describes the variants of fundamental KT
its capacity to extract and represent features and discover models. Section V introduces the extensive applications of
intricate structure. For instance, Deep Knowledge Tracing KT in different scenarios. Section VI gives the summary of
introduced recurrent neural networks (RNNs) [17] into the existing datasets for evaluating KT models and details of the
KT task and was found to significantly outperform previous algorithm libraries we have released. Section VII discusses
methods [18]. Following this, various methods have been somepotentialfutureresearchdirections.Finally,sectionVIII
introduced that employ various types of neural networks to summarizes the paper.
theKTtask,consideringvariouscharacteristicsofthelearning
sequence [19, 20, 21]. Moreover, due to the requirements of II. OVERVIEW
| practical    | applications, | many | variants | of  | KT models | have         | been |            |            |     |     |     |     |     |     |
| ------------ | ------------- | ---- | -------- | --- | --------- | ------------ | ---- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
|              |               |      |          |     |           |              |      | A. Problem | Definition |     |     |     |     |     |     |
| continuously | developed,    |      | and KT   | has | already   | been broadly |      |            |            |     |     |     |     |     |     |
Inanonlinelearningsystem,supposingthereexistsasetof
| applied | in numerous | educational |          | scenarios. |         |               |     |                 |               |          |           |              |            |         |            |
| ------- | ----------- | ----------- | -------- | ---------- | ------- | ------------- | --- | --------------- | ------------- | -------- | --------- | ------------ | ---------- | ------- | ---------- |
|         |             |             |          |            |         |               |     |                 | S             |          |           | E.           |            |         |            |
|         |             |             |          |            |         |               |     | students        | and a set     | of       | exercises | Each         | exercise   |         | is related |
|         |             |             |          |            |         |               |     | to specific     | Knowledge     | Concepts |           | (KCs).       | Generally, |         | the name   |
|         |             |             |          |            |         |               |     | given to        | the knowledge |          | related   | to exercises |            | differs | across     |
|         |             |             |          |            |         |               |     | online learning | platforms.    |          | For       | instance,    | it is      | named   | skill in   |
| While   | novel KT    | models      | continue | to         | emerge, | there remains |     |                 |               |          |           |              |            |         |            |
ASSISTments[24].Topromotebetterunderstanding,werefer
alackofcomprehensivesurveysexploringthisyoungresearch
field, particularly regarding its numerous variants and appli- to these uniformly as knowledge concepts throughout this pa-
|          |              |             |     |        |         |                |     | per,anddenotethesetofallKCsasKC.Moreover,M |     |     |     |     |     |     | andK |
| -------- | ------------ | ----------- | --- | ------ | ------- | -------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- |
| cations. | To this end, | the current |     | survey | aims to | systematically |     |                                            |     |     |     |     |     |     |      |
arerespectivelyusedtorepresentthetotalnumberofexercises
| review       | the development |               | of KT. | As        | depicted | in Figure   | 2,  |                  |          |           |        |         |            |            |     |
| ------------ | --------------- | ------------- | ------ | --------- | -------- | ----------- | --- | ---------------- | -------- | --------- | ------ | ------- | ---------- | ---------- | --- |
|              |                 |               |        |           |          |             |     | and KCs.         | Students | are asked | to     | answer  | different  | exercises  | in  |
| we initially | categorize      | existing      |        | KT models | from     | a technical |     |                  |          |           |        |         |            |            |     |
|              |                 |               |        |           |          |             |     | order to achieve | mastery  |           | of the | related | knowledge. | Therefore, |     |
| perspective, | which           | is consistent |        | with the  | majority | of existing |     |                  |          |           |        |         |            |            |     |
|              |                 |               |        |           |          |             |     |                  |          |           |        |         |            |            | X = |
surveys[22,23].Thiscategorizationsplitsthemintothreecat- the learning sequence of a student can be formulated as
|     |     |     |     |     |     |     |     | {([e ,k | ],a ,r ),([e | ,k  | ],a | ,r ),...,([e | ,k  | ],a | ,r ),..., |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --- | ------------ | --- | --- | --------- |
egories:(1)Bayesianmodels,(2)logisticmodels,and(3)deep 1 e1 1 1 2 e2 2 2 t et t t
|     |     |     |     |     |     |     |     | ([e ,k | ],a ,r | )}, where | the | tuple | ([e ,k | ],a | ,r ) rep- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | --- | ----- | ------ | --- | --------- |
learningmodels.Ineachcategory,wefurtherorganizespecific N eN N N t et t t
KT methods according to their various techniques. Subse- resents the learning interaction at the t−th time step, e t
|     |     |     |     |     |     |     |     | represents | the exercise, |     | k represents |     | the exercise’s |     | related |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ------------ | --- | -------------- | --- | ------- |
quently, we introduce extensive variants of these fundamental et
|            |       |          |      |           |             |     |       | KCs,a representsthecorrectnesslabel(i.e.,with1forcorrect |     |     |     |                             |     |     |     |
| ---------- | ----- | -------- | ---- | --------- | ----------- | --- | ----- | -------------------------------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
| KT models, | which | consider | more | stringent | assumptions |     | about | t                                                        |     |     |     |                             |     |     |     |
|            |       |          |      |           |             |     |       | and0forincorrectanswers),r                               |     |     |     | standsforthesideinformation |     |     |     |
more complete learning process in different learning phases. t
|              |            |         |     |         |              |     |       | recordedinthislearninginteraction,andN |     |     |     |     | isthelengthofthe |     |     |
| ------------ | ---------- | ------- | --- | ------- | ------------ | --- | ----- | -------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
| In addition, | we present | several |     | typical | applications | of  | KT in |                                        |     |     |     |     |                  |     |     |
real learning scenarios. Due to the complexity of different KT learningsequence.Theresearchproblemofknowledgetracing
|     |     |     |     |     |     |     |     | can thus | be defined | as follows: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | --- | --- | --- | --- | --- |
models,wehaveopensourcedtwoalgorithmlibrariestobetter
| aid researchers | and | practitioners |     | in implementing |     | KT models |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1https://github.com/bigdata-ustc/EduData
and facilitate community development in this domain. These 2https://github.com/bigdata-ustc/EduKTM

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 3   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Knowledge Tracing
|     |     |     |     | Variants |     |     |     |     | Applications |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
Fundamental models
| Modeling individualization  |     |     |     |                 |     |                 |     |     |                      |     |     |     | Learning resources  |     |
| --------------------------- | --- | --- | --- | --------------- | --- | --------------- | --- | --- | -------------------- | --- | --- | --- | ------------------- | --- |
|                             |     |     |     | Bayesian models |     | Logistic models |     |     | Deep learning models |     |     |     |                     |     |
| before learning             |     |     |     |                 |     |                 |     |     |                      |     |     |     | recommendation      |     |
Incorporating engagement Bayesian knowledge tracing Learning factor analysis Deep knowledge tracing
Adapt pilavyere m oldeelinagrning
during learning
|     |     |     |     | D y n am i c  B a | y e s i a n  | Performance factor analysis |     | Memory-aware knowledge tracing |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------- | ------------ | --------------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
Considering forgetting  kn o w le d g e  tr a c i n g Broader Applications
after learning
Attentive knowledge tracing
Knowledge tracing machines
Utilizing side information
| across learning |     |     |     |     |     |     |     |     | Graph-based knowledge tracing |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
Fig.2. Anoverviewofknowledgetracingmodels.
Givensequencesoflearninginteractionsinonlinelearn- C. Differences between this and previous surveys
| ing systems,   | knowledge   |             | tracing | aims           | to monitor        | students’   |              |                |           |                   |              |         |              |          |
| -------------- | ----------- | ----------- | ------- | -------------- | ----------------- | ----------- | ------------ | -------------- | --------- | ----------------- | ------------ | ------- | ------------ | -------- |
|                |             |             |         |                |                   |             | Given        | the increasing |           | importance        |              | of      | KT, several  | recent   |
| evolving       | knowledge   |             | states  | during         | the learning      | process     |              |                |           |                   |              |         |              |          |
|                |             |             |         |                |                   |             | surveys      | have also      | examined  |                   | this area.   | These   | include      | works    |
| and predict    | their       | performance |         | on             | future exercises. | The         |              |                |           |                   |              |         |              |          |
|                |             |             |         |                |                   |             | by Schmucker |                | et al.    | [22], Abdelrahman |              |         | et al. [23], | Pela´nek |
| measured       | knowledge   |             | states  | can be further | applied           | to indi-    |              |                |           |                   |              |         |              |          |
|                |             |             |         |                |                   |             | [30], Song   | et al.         | [31],     | Liu [32],         | Zanellati    |         | et al. [33]. | Here, we |
| vidualize      | students’   | learning    |         | schemes        | in order          | to maximize |              |                |           |                   |              |         |              |          |
|                |             |             |         |                |                   |             | will briefly | discuss        | the       | key distinctions  |              | between | these        | studies  |
| their learning | efficiency. |             |         |                |                   |             |              |                |           |                   |              |         |              |          |
|                |             |             |         |                |                   |             | to highlight | the            | necessity | and               | significance |         | of this      | survey.  |
SomerecentworksdirectlyregardedtheKTtaskasstudent
|                  |             |          |               |             |            |                  | Existing      | surveys      | have               | either        | focused        | on           | specific       | categories  |
| ---------------- | ----------- | -------- | ------------- | ----------- | ---------- | ---------------- | ------------- | ------------ | ------------------ | ------------- | -------------- | ------------ | -------------- | ----------- |
| performance      | prediction, |          | without       | considering | students’  | knowl-           |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | of KT models  |              | or comprehensively |               |                | reviewed     | all available  | KT          |
| edge states      | [25,        | 26, 27]. | We            | agree that  | predicting | student          |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | models.       | For example, |                    | Pela´nek      | [30]           | provided     | an overview    | of          |
| performance      | is of       | great    | significance, | as          | it is now  | the best way     |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | KT in terms   | of           | Bayesian           | models        |                | and logistic | models,        | Song        |
| to evaluate      | the         | quality  | of the        | knowledge   | state      | traced by KT     |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | et al. [31]   | compared     |                    | and discussed |                | deep         | learning       | based KT    |
| models.          | However,    | we have  | to            | point out   | that KT    | focuses more     |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | models,       | while        | Zanellati          | et            | al. [33]       | presented    | to             | pay more    |
| on students’     | knowledge   |          | states,       | especially  | their      | interpretability |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | attention     | to hybird    |                    | models        | in KT.         | Liu          | [32] conducted | a           |
| and rationality, | which       | is       | related       | to the      | students’  | acceptance of    |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | bibliometric  | analysis     |                    | to examine    | the            | evolution    | of KT          | research    |
| the conclusions  |             | given    | based on      | the KT      | model      | [28, 29].        |               |              |                    |               |                |              |                |             |
|                  |             |          |               |             |            |                  | from 1992     | to 2021.     | Abdelrahman        |               | et             | al. [23]     | also           | presented a |
|                  |             |          |               |             |            |                  | comprehensive |              | survey             | for the       | KT literature, |              | including      | a broad     |
rangeofmethodsstartingfromtheearlyattemptstotherecent
B. Categorization
|     |     |     |     |     |     |     | state-of-the-art |     | techniques | utilizing |     | deep learning. |     | Schmucker |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --------- | --- | -------------- | --- | --------- |
As shown in Fig. 2, we categorize and summarize the et al. [22] summarized KT methods in the context of student
existing KT models according to their technical differences. performance modeling problems.
In more detail, the proposed taxonomy splits existing KT However, current surveys are somewhat limited in their
methodsintothreecategories:(1)Bayesianmodels,whichare scope,theyonlyprovideadetailedintroductiontovariousKT
implemented through probability model, (2) logistic models, methodsandcomparisonsbetweenthem.Giventhecomplexity
which are implemented through logistic functions, and (3) of online learning systems and the significant importance
deep learning models, which are implemented through neural of KT research in practical applications, this survey places
networks.Specifically,wedividethedeeplearningmodelsinto a greater emphasis on the variants and applications of KT
foursub-categoriesaccordingtofourvariousneuralnetworks, models, rather than solely introducing and comparing dif-
i.e., deep knowledge tracing based on recurrent neural net- ferent KT methods. Moreover, considering that datasets are
works, memory-aware knowledge tracing based on memory collectedfromdifferentsystemswithvarioussetting,subjects,
networks, attentive knowledge tracing based on self-attention learning stages, and scales, we do not report and compare
mechanism, and graph-based knowledge tracing based on the performance of KT models on the student performance
graph neural networks. In addition to these fundamental KT prediction task across various datasets in this survey. Pavlik
models, we also introduce a large number of their variants, et al. [34] have also empirically verified that no single KT
which respectively consider a more complete learning process model was always the best, a specific better model must
in distinct learning phases: (1) modeling individualization consider multiple student features and the learning context.
beforelearning,(2)incorporatingengagementduringlearning, Instead, we have open sourced two algorithm libraries which
(3) considering forgetting after learning, and (4) utilizing side include the majority of existing KT-related datasets and uni-
informationacrosslearning.Moreover,wealsosummarizethe fied implementations of existing KT models. Consequently,
extensiveapplicationsofKTindifferenteducationalscenarios, researchers and practitioners can freely select appropriate
including learning resources recommendation, adaptive learn- KT models based on their specific requirements in various
ing and broader applications beyond student learning. application scenarios.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 4
TABLEI
ASUMMARYOFDIFFERENTTYPESOFFUNDAMENTALKNOWLEDGETRACINGMODELS.
Category Typicalapproach Technique KCrelationship Knowledgestate
Bayesianknowledgetracing[9] Bayesiannetworks independent
unobservablenode
Bayesianmodels
dynamicBayesianknowledgetracing[35] dynamicBayesiannetworks pre-defined inHMM
learningfactoranalysis[15]
logisticregression theoutputof
performancefactoranalysis[16]
Logisticmodels independent logisticregressionfunction
knowledgetracingmachines[36] factorizationmachines
deepknowledgetracing[18] RNN/LSTM discoverautomatically thehiddenstate
Deeplearning memory-awareknowledgetracing[37] memorynetworks correlationweights valuematrix
models attentiveknowledgetracing[20,21] self-attentionmechanism attentionweights attentivehistoricalknowledgestate
graph-basedknowledgetracing[19] graphneuralnetworks edgesingraph aggregateinthegraph
III. FUNDAMENTALKNOWLEDGETRACINGMODELS
P(T) P(T) P(T)
P(L) K K K . . .
0
In this section, as shown in Table I, we will present the
P(G) P(G) P(G)
fundamental KT models, based on our taxonomic framework. P(S) P(S) P(S)
Specifically, we will introduce these models in accordance A A A . . .
with their development timeline. Subsequently, we will pro-
vide a summary of these fundamental KT models. Fig. 3. The topology of Bayesian Knowledge Tracing [9]. K are the un-
observedknowledgenodes,Aaretheobservedperformance(answer)nodes,
P(L0) represents the initial probability, P(T) is the transition probability,
P(G)istheguessingprobabilityandP(S)istheslippingprobability.
A. Bayesian Models
Bayesian models assume that the learning process adheres will convert to the mastered state. The posterior probability
to a Markov process. This process allows for the estimation P(L n |Answer) is estimated as follows:
o
p
f
er
s
fo
tu
r
d
m
e
a
n
n
ts
c
’
e.
la
I
t
n
en
t
t
he
kn
s
o
u
w
bs
l
e
e
q
d
u
g
e
e
n
s
t
ta
s
t
e
e
c
s
tio
b
n
as
,
e
w
d
e
on
wi
t
l
h
l
e
p
ir
re
o
se
b
n
se
t
r
t
v
w
e
o
d P(Ln|correct)=
P(Ln−1)(1
P
−
(
P
L
(
n
S
−
)
1
)
)
+
(1
(
−
1−
P(
P
S
(
)
L
)
n−1))P(G)
,
(2)
B
K
a
n
y
o
e
w
s
l
i
e
a
d
n
g
m
eT
od
ra
e
c
ls
in
i
g
n
(B
ou
K
r
T
t
)
ax
an
o
d
no
th
m
e
y
D
f
y
ra
n
m
am
ew
ic
o
B
rk
a
:
ye
th
s
e
ian
B
K
ay
n
e
o
s
w
ia
l
n
-
P(Ln|incorrect)=
P(Ln−1)P(S)
P
+
(
(
L
1
n
−
−1
P
)P
(L
(
n
S
−
)
1))(1−P(G))
.
edge Tracing (DBKT). 2) Dynamic Bayesian Knowledge Tracing: BKT indepen-
dently models the parameters of each KC, employing a spe-
1) Bayesian Knowledge Tracing: BKT’s structure is illus-
cific model for each KC. However, KCs are not completely
trated in Fig. 3; here, the unshaded nodes represent unobserv-
independent, but rather hierarchical and closely related [38].
ablelatentknowledgestates,whiletheshadednodesrepresent
Dynamic Bayesian networks are capable of jointly represent-
the observable answers of the student.
ingmultipleskillswithinasinglemodel,potentiallyenhancing
BKT is a unique instance of the Hidden Markov Model
therepresentationalpowerofBKT.Consequently,Ka¨seretal.
(HMM).TherearetwotypesofparametersinHMM:transition
[35]proposedynamicBayesianknowledgetracing(DBKT)to
probabilitiesandemissionprobabilities.InBKT,thetransition
represent the hierarchies and relationships within KCs using
probabilities are defined by two learning parameters: (1)
dynamicBayesiannetworks.Thisapproachconsidersdifferent
P(T), the probability of transition from the unlearned state
KCs jointly within a single model.
to the learned state; (2) P(F), the probability of forgetting
In DBKT, a student’s knowledge mastery is represented
previouslymasteredknowledge.Moreover,theemissionprob-
by binary latent variables, which are estimated based on
abilities are determined by two performance parameters: (1)
their learning interactions. Unlike BKT, DBKT takes into
P(G) - the probability that a student will guess correctly,
account the dependencies between various KCs. For exam-
despite non-mastery; (2) P(S) - the probability that a student
ple, if KC and KC are prerequisites for mastering KC ,
willmakeamistake,despitemastery.Additionally,P(L )rep- 1 2 3
0
students’ mastery of KC depends on their mastery of KC
resentstheinitialprobabilityofmastery.BKToperateswithin 3 1
and KC . Let H denote the unobserved variables, i.e., lack
a two-state student modeling framework: knowledge is either 2
of student answers and binary mastery variables. Assuming
learnedorunlearned,andthereisnoforgettingonceastudent
the student correctly answers an exercise associated with
has mastered the knowledge. Based on the observations of
KC at time step t , i.e., a = 1. The observed vari-
the student’s learning interactions, the following equation is 1 1 1,1
ables are then a = a and the unobserved variables are
utilized to estimate the knowledge state and the probability of m 1,1
h = {KC ,KC ,KC ,a ,a }. The objective of
correct answers: m 1,1 2,1 3,1 2,1 3,1
DBKT is to find the parameters θ that maximize the joint
P(L n )=P(L n |Answer)+(1−P(L n |Answer))P(T), (1) probability p(a m ,h m |θ). The log-likelihood can alternatively
P(C n+1 )=P(L n )(1−P(S))+(1−P(L n ))P(G), be formulated using a log-linear model, as follows:
(cid:88) (cid:88)
where P(L n ) is the probability that a KC is mastered at L(w)= ln( exp(wTΦ(a m ,h m )−ln(Z))), (3)
the n-th learning interaction, P(C n+1 ) is the probability of m hm
correct answers at the next learning interaction. P(L ) is the whereΦ:A×H →RF denotesamappingfromtheobserved
n
sum of two probabilities: (1) the probability that the KC is space A and the latent space H to an F-dimensional feature
already mastered; (2) the probability that the knowledge state vector. Z is a normalizing constant, w denotes the weights.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 5
of working with any real-valued feature vector, enabling the
V v v v
i j’ k’ model to represent all interactions between variables using
factorized parameters [41]. FMs provide a means of encoding
side information about exercises or students into the model.
w w w w
i j’ k’
Figure 4 illustrates the example of KTM, which models the
U i I j S k knowledge mastery of the student based on a sparse set of
l 1 1 1 weights for all features involved in the event. Let L be
the number of features; here, the features can be related to
Students Exercises KCs
students, exercises, KCs, or any other side information. The
Fig.4. Exampleofactivationofaknowledgetracingmachine[36].V refers
learning interaction is encoded by a sparse vector l of length
tothematrixofembeddings,wreferstothevectorofbiases,xistheencoding
vectorofthelearninginteraction. L. When feature i is involved in the interaction, l i > 0. The
probability p(θ) of the correct answer is determined by the
B. Logistic Models
following equations:
Logistic models represent the probability of students cor- L
(cid:88) (cid:88)
rectlyansweringexercisesasalogisticfunctionofthestudent p(θ)=σ(µ+ w i l i + l i l j ⟨v i ,v j ⟩), (6)
andKCparameters.Theyfirstusedifferentfactorsinstudents’ i=1 1≤i<j≤L
learning interactions to compute an estimation of the student whereµistheglobalbias,thefeatureiismodeledbythebias
andKCparameters,thenutilizealogisticfunctiontotransform w i ∈ R and the embedding v i ∈ Rd (d is the dimension).
this estimation into the prediction of the probability of mas- Note that only features with l i > 0 will have impacts on the
tery [30]. In the subsequent section, we will introduce three predictions.
types of logistic models: (1) Learning Factor Analysis (LFA),
(2) Performance Factor Analysis (PFA) and (3) Knowledge C. Deep Learning Models
Tracing Machines (KTM).
The cognitive process can be influenced by various factors
1) Learning Factor Analysis: The LFA model [15] consid-
at both the macro and micro levels. It is difficult for Bayesian
ers the following learning factors:
models or logistic models to adequately capture a cognitive
• Initial knowledge state: parameter α estimates the initial processofhighcomplexity[18].Deeplearning,withitspotent
knowledge state of each student; ability to achieve non-linearity and feature extraction, is well-
• Easiness of KCs: parameter β captures the easiness of suited for modeling complex learning processes, particularly
different KCs; whenasignificantamountoflearninginteractiondataisavail-
• Learning rate of KCs: parameter γ denotes the learning able[42].Inrecentyears,numerousresearchworkshavebeen
rate of KCs. proposedondeeplearningKTmodels,wewillintroducedeep
The standard LFA model takes the following form: learningmodelsfromfoursub-categories:(1)deepknowledge
p(θ)=σ( (cid:88) α S + (cid:88) (β +γ T )K ), (4) tracing, (2) memory-aware knowledge tracing, (3) attentive
i i j j j j
knowledge tracing, and (4) graph-based knowledge tracing.
i∈N j∈KCs
where σ is the sigmoid function, S is the covariate for 1) Deep Knowledge Tracing: Deep Knowledge Tracing
i
the student i, T represents the covariate for the number of (DKT) is the pioneering approach that introduces deep learn-
j
interactions on KC j, K is the covariate for KC j, p(θ) is ing to complete the KT task. DKT employs Recurrent Neural
j
the estimation of the probability of a correct answer. Networks (RNNs) [17] to process the input sequence of
2) Performance Factor Analysis: The PFA model [16] can learninginteractionsovertime,maintainingahiddenstatethat
be seen as an extension of the LFA model that is especially implicitly contains information about the history of all past
sensitive to the student performance. In contrast to the LFA elements of the sequence. This hidden state evolves based
model, PFA considers the following different factors: on both the previous knowledge state and the present input
learning interaction [18]. DKT provides a high-dimensional
• Previousfailures:parameterf isthepriorfailuresforthe
and continuous representation of the knowledge state, en-
KC of the student;
abling it to more effectively model the complex learning
• Previous successes: parameter s represents the prior suc-
process.Typically,RNNs’variant,theLongShort-TermMem-
cesses for the KC of the student;
ory (LSTM) networks [43], are more frequently used in the
• Easiness of KCs: parameter β means the easiness of
implementation of DKT, which is further strengthened by
different KCs, which is the same as in the LFA model.
considering forgetting.
The standard PFA model takes the following form:
Fig. 5 illustrates the process of deep knowledge tracing.
(cid:88)
p(θ)=σ( (β j +µ j s ij +ν j f ij )), (5) In DKT, exercises are represented by their contained KCs.
j∈KCs For datasets with different numbers of KCs, DKT applies
where µ and ν are the coefficients for s and f, which denote two different methods to convert students’ learning interac-
the learning rates for successes and failures. tions X ={(e ,a ),(e ,a ),...,(e ,a ),...,(e ,a )} into a
1 1 2 2 t t N N
3) Knowledge Tracing Machines: The KTM model, devel- sequence of fixed-length input vectors. More specifically, for
opedbyVieetal.[36],employsfactorizationmachines(FMs) datasetswithasmallnumberK ofuniqueKCs,x ∈{0,1}2K
t
[39, 40] to generalize logistic models to higher dimensions. is set as a one-hot embedding, where xk = 1 if the answer
t
FMs were initially introduced as a general predictor capable a of the exercise with KC k was correct or xk+K = 1
t t

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 6
y1 y2 y3 yN
predictions input exercise embeddings are then concatenated together and
passed to a fully connected layer to yield a summary vector
. . . f , which contains both the student’s knowledge mastery
t
hidden states h0 h1 h2 h3 hN
and the prior difficulty of the exercise. Furthermore, the
student’s performance can be predicted by applying another
learning interactions fully connected layer with a sigmoid activation function to
x 1 x 2 x 3 x N the summary vector:
N
Fig.5. ThearchitectureofDKT[18]. (cid:88)
r = w (i)Mv(i),
if the answer was incorrect. For datasets with a large num- t t t
ber of unique KCs, one-hot embeddings are considered too i=1 (9)
f =tanh(W [r ,k ]+b ),
sparse. Therefore, DKT assigns each input vector x to a t f t t f
t
corresponding random vector, and then uses the embedded p t =σ(W p f t +b p ),
learning sequence as the input of RNNs. A linear mapping whereW andW aretheweights,b andb arebiasterms.
f p f p
and activation function are then applied to the output hidden In the write operation, after an exercise has been answered,
states to obtain the knowledge state of students: DKVMNupdatesstudents’knowledgemastery(i.e.,thevalue
h =tanh(W x +W h +b ), matrix) based on their performance. Specifically, the learning
t hs t hh t−1 h
(7) interaction (e ,a ) is first embedded with an embedding ma-
y =σ(W h +b ), t t
t yh t y
trix B to obtain the student’s knowledge growth v . Then
where tanh is the activation function, W is the input t
hs DKVMN calculates an erase vector erase from v and
weights, W is the recurrent weights, W is the readout t t
hh yh decides to erase the previous memory with reference to both
weights, and b and b are the bias terms.
h y the erase vector and the correlation weight w . Following
Despite demonstrating superior performance compared to t
erasure, the new memory vectors are updated by the new
Bayesian and logistic models, DKT has several inherent
knowledge state and the add vector add , which forms an
shortcomings. For instance, the lack of interpretability is a t
erase-followed-by-add mechanism that allows forgetting and
significant drawback. It is challenging to understand how
strengthening knowledge mastery in the learning process:
the hidden states represent students’ knowledge states, and
erase =σ(W v +b ),
the model cannot explicitly determine a student’s knowledge t e t e
m
Ye
a
u
s
n
te
g
ry
[4
f
4
ro
]
m
ide
th
n
e
tifi
h
e
id
d
d
t
e
w
n
o
st
u
a
n
te
re
[
a
4
s
2
o
]
n
.
a
A
bl
d
e
di
p
t
h
io
e
n
n
a
o
l
m
ly
e
,
n
Y
a
eu
in
ng
D
a
K
n
T
d M(cid:102)
t
v(i)=M
t
v
−1
(i)[1−w
t
(i)erase
t
],
(10)
add =tanh(W v +b ),
t d t d
that contravene common sense. These are: (1) the inability
to reconstruct observed input, and (2) inconsistent predicted M t v(i)=M(cid:102) t v(i)+w t (i)add t ,
knowledge states across time-steps. However, despite these where W and W are the weights, b and b are bias terms.
e d e d
shortcomings, DKT remains a promising KT model [45]. Abdelrahman and Wang [47] point out that DKVMN failed
2) Memory-aware Knowledge Tracing: To enhance the in- to capture long-term dependencies in the learning process.
terpretabilityofDKT,memory-awareknowledgetracingintro- Therefore, they propose a Sequential Key-Value Memory
duces an external memory module, as proposed by [46]. This Network (SKVMN) to combine the strengths of DKT’s recur-
module is designed to store the and update the corresponding rent modelling capacity and DKVMN’s memory capacity. In
knowledge mastery of the student. The most representative SKVMN, a modified LSTM called Hop-LSTM is used to hop
exampleisDynamicKey-ValueMemoryNetworks(DKVMN) across LSTM cells according to the relevance of the latent
for knowledge tracing, as proposed by [37]. DKVMN high- KCs, which directly captures the long-term dependencies.
lights students’ specific knowledge states on various knowl- Duringthewritingprocess,SKVMNallowsforthecalculation
edge categories. It initializes a static matrix, referred to as a of the knowledge growth of a new exercise, taking into
key matrixtostorelatentKCsandadynamicmatrix,calleda consideration the current knowledge state, thereby yielding
valuematrixtostoreandupdatethemasteryofcorresponding more reasonable results.
KCs through read and write operations over time. 3) Attentive Knowledge Tracing: In the development of
As shown in Fig. 6, an embedding matrix is first defined to deep learning, the Transformer is initially proposed for neural
obtaintheembeddingvectork t oftheexercises.Acorrelation machine translation [25], which abandons recurrence and
weight w t is then obtained by taking the inner product solelyreliesontheself-attentionmechanismtocaptureglobal
between the exercise embedding k t and the key vectors Mk, dependencies within a sequence. The Transformer has been
followed by the softmax activation: demonstrated to excel in feature extraction and dependency
w =Softmax(k Mk), (8) capture, while maintaining high computational efficiency.
t t
where the correlation weight w represents the correlation Some representative pre-training models based on the Trans-
t
between the exercises and all latent KCs. former,suchasBERT[48]andGPT[49],haveobtainedstate-
In the read operation, DKVMN predicts student perfor- of-the-artresultsonvariousnaturallanguageprocessingtasks.
mancebasedonthestudent’sknowledgemastery.Specifically, Pandey and Karypis [20] propose a self-attentive model for
DKVMNreadsstudents’masteryoftheexerciser withrefer- knowledge tracing (SAKT), which directly apply the Trans-
t
ence to the weighted sum of all memory vectors in the value former to capture long-term dependencies between students’
matrix using the correlation weight. The read content and the learning interactions. Furthermore, Wang et al. [50] introduce

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |         |         |     |        |           |            |     |         | 7   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | ------ | --------- | ---------- | --- | ------- | --- |
|                                                 |     |     | pt  |     |     |     | where q |         | ∈RD | is the | KC-answer | embedding, |     | f       | ∈   |
|                                                 |     |     |     |     |     |     |         | (ct,at) |     |        |           |            |     | (ct,at) |     |
RD
|     |     | ft  |     |     |     |     | is        | the variation |     | vector.  | Through | the | above      | embedding, |       |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | -------- | ------- | --- | ---------- | ---------- | ----- |
|     |     |     |     |     |     |     | exercises | labeled       | as  | the same | KCs     | are | determined |            | to be |
∑
Write operation closely related while retaining important individual charac-
rt
|     |     |     |     |     |     |      | teristics. | Then, | in  | the exercise |     | encoder, | the | input | is the |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | ----- | --- | ------------ | --- | -------- | --- | ----- | ------ |
|     |     |     |     |     | M   | vt1 |            |       |     |              |     |          |     |       |        |
M vt-1 M vt exercise embeddings {e ,...,e } and the output is a sequence
|     |     |     |     |     |     |     |     |     |     | 1   | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 -
|     |     |     |     |     |     |     | of context-aware |     | exercise | embeddings |     | {e  | (cid:101)1 ,...,e | (cid:101)t }. AKT | de- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---------- | --- | --- | ----------------- | ----------------- | --- |
wt
|     |     |     |     |     |     |     | signs a | monotonic |     | attention | mechanism |     | to accomplish |     | the |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --------- | --------- | --- | ------------- | --- | --- |
softmax
|     |     |     |     |     |     |     | above process, |     | where | the context-aware |     |     | embedding |     | of each |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----------------- | --- | --- | --------- | --- | ------- |
Mk
|     |     |     |     |     |     |     | exercise | depends | on  | both | itself and | the | previous | exercises, |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | ---- | ---------- | --- | -------- | ---------- | --- |
eraset addt
|     |     |     |     |     |     |     | i.e., e    | = f | (e   | ,...,e | ). Similarly, |     | the knowledge |     | en- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------ | ------------- | --- | ------------- | --- | --- |
|     |     |     |     |     |     |     | (cid:101)t |     | enc1 | 1 t    |               |     |               |     |     |
kt
Sigmoid Tanh coder takes exercise-answer embeddings {y 1 ,...,y t } as input
|     |     | A   |     |     |     |     | and outputs | a   | sequence | of  | context-aware |     | embeddings |     | of the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | ------------- | --- | ---------- | --- | ------ |
vt
|     |     |     |     |     |     |     | knowledgeacquisitions{y |            |     |            | ,...,y }usingthesamemonotonic |            |     |              |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | ---------- | --- | ---------- | ----------------------------- | ---------- | --- | ------------ | --- |
|     |     |     | et  |     | B   |     |                         |            |     | (cid:101)1 | (cid:101)t                    |            |     |              |     |
|     |     |     |     |     |     |     | attention               | mechanism; |     | these      | are also                      | determined |     | by students’ |     |
Read operation
(et ,  at) answers to both the current exercise and prior exercises,
Fig.6. ThearchitectureofDKVMN[37].
|     |     |     |     |     |     |     | i.e., y (cid:101)t | = f enc1 | (y 1 ,...,y | t ). | Finally, | the | knowledge | retriever |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | -------- | ----------- | ---- | -------- | --- | --------- | --------- | --- |
an adaptive sparse self-attention network to generate missing takesthecontext-awareexerciseembeddinge andexercise-
(cid:101)1:t
features and simultaneously produce fine-grained predictions answer pair embeddings y as input and outputs a retrieved
(cid:101)1:t
of student performance. Zhu et al. [51] employ a multi- knowledgestateh t forthecurrentexercise.Sincethestudent’s
headProbSparseself-attentionmechanismtomitigatethetime current knowledge state depends on answering the related
complexityandeffectivelycapturethelong-termdependencies exercise, it is also context-aware in AKT. The novel mono-
in students’ learning interactions. tonic attention mechanism proposed in AKT is based on the
However, the complexity of the KT task often limits the assumptionthatthelearningprocessistemporalandstudents’
performance of the aforementioned simple Transformer appli- knowledge will decay over time. Therefore, the scaled inner-
cations. Choi et al. [26] introduce a novel approach named product attention mechanism utilized in the original Trans-
|           |                |     |        |           |         |         | former | is not suitable |     | for the | KT task. | AKT | uses | exponential |     |
| --------- | -------------- | --- | ------ | --------- | ------- | ------- | ------ | --------------- | --- | ------- | -------- | --- | ---- | ----------- | --- |
| Separated | Self-Attentive |     | Neural | Knowledge | Tracing | (SAINT) |        |                 |     |         |          |     |      |             |     |
to enhance self-attentive computation for KT adaptability. decay and a context-aware relative distance measure to com-
Specifically, SAINT employs an encoder-decoder structure, pute the attention weights. Finally, AKT achieves outstanding
withtheexerciseandanswerembeddingsbeingseparatelyen- performance in predicting students’ future answers, as well as
coded and decoded by self-attention layers. The separation of demonstrating interpretability due to the combination of the
the input allows SAINT to stack self-attention layers multiple psychometric model.
times,thuscapturingcomplexrelationsinstudentinteractions. ItisimportanttonotethatPuandBecker[53]haverecently
Subsequently, Shin et al. [27] introduce the SAINT+ model, proposedthatattentiveknowledgetracingmodelssignificantly
which integrates two temporal features into SAINT: namely, benefitfromstudents’continuous,repeatedinteractionsonthe
the time taken to answer each exercise and the interval time sameexercisesthroughoutthelearningprocess.Intheirexperi-
between consecutive learning interactions. Both SAINT and ments,theremovaloftheserepeatedinteractionsinthedataset
SAINT+ have outperformed the SAKT model on the student led to a decline in AKT’s performance, bringing it close to
performance prediction task. that of DKVMN. Moreover, according to the findings of Yin
Additionally, Ghosh et al. [21] observe that SAKT does et al. [54], existing attentive attentive KT models primarily
not surpass DKT and DKVMN in their experiments. Unlike trace patterns of a learner’s learning activities, rather than
SAINT and SAINT+, they present a context-aware attentive their evolving knowledge states. Consequently, they develop
knowledge tracing (AKT) model. This model integrates the the DTransformer model to facilitate stable knowledge state
self-attention mechanism with psychometric models, creating estimation and tracing, rather than solely focusing on next
a more effective system. AKT is composed of four modules: performance prediction.
Rasch model-based embeddings, exercise encoder, knowledge 4) Graph-based Knowledge Tracing: Graph neural net-
encoder, and knowledge retriever. Specifically, the embedding works (GNNs), which are designed to handle complex graph-
module employs the classic Rasch model in psychometrics related data, have developed rapidly in recent years [55]. The
[52] to construct embeddings for exercises and KCs: graph represents a kind of data structure that models a set
|     |     |     |       |          |      |      | of objects | (nodes) |     | and their | relationships |     | (edges). |     | From a |
| --- | --- | --- | ----- | -------- | ---- | ---- | ---------- | ------- | --- | --------- | ------------- | --- | -------- | --- | ------ |
|     |     | x t | =c ct | +µ et ·d | ct , | (11) |            |         |     |           |               |     |          |     |        |
where c ∈RD is the embedding of the KC of this exercise, data structure perspective, there is a naturally existing graph
ct
RD structure within the KCs. Therefore, incorporating the graph
| d ct ∈ | is  | a vector | that | summarizes | the variation |     | in  |     |     |     |     |     |     |     |     |
| ------ | --- | -------- | ---- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
exercises with the related KC, and µ ∈ RD is a scalar structure of the KCs as additional information should be ben-
et
difficulty parameter that controls the extent to which this eficial to the KT task. Nakagawa et al. [19] presented graph-
|          |          |      |             |     |                     |     | based knowledge |     | tracing | (GKT), |     | which | conceptualizes |     | the |
| -------- | -------- | ---- | ----------- | --- | ------------------- | --- | --------------- | --- | ------- | ------ | --- | ----- | -------------- | --- | --- |
| exercise | deviates | from | the related | KC. | The exercise-answer |     |                 |     |         |        |     |       |                |     |     |
tuple (e ,a ) is similarly extended using the scalar difficulty potential graph structure of the KCs as a graph G = (V,E),
| t         | t        |       |     |     |     |     |             |     |     |           |                          |     |     |     |     |
| --------- | -------- | ----- | --- | --- | --- | --- | ----------- | --- | --- | --------- | ------------------------ | --- | --- | --- | --- |
|           |          |       |     |     |     |     | wherenodesV |     | ={v | ,v ,...,v | }representthesetofKCsand |     |     |     |     |
| parameter | for each | pair: |     |     |     |     |             |     |     | 1 2       | N                        |     |     |     |     |
y =q +µ ·f , (12) the edges E ⊆ V ×V represent relationships of these KCs;
|     |     | t   | (ct,at) | et  | (ct,at) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |           |     |     |     |     |     |     |           |            |      |     |          |         |                 | 8   |
| ----------------------------------------------- | --------- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---- | --- | -------- | ------- | --------------- | --- |
|                                                 |           |     |     |     |     |     |     | knowledge | structure, | Tong | et  | al. [58] | propose | structure-based |     |
|                                                 | Aggregate | j   |     | i   |     | k   |     |           |            |      |     |          |         |                 |     |
neighbor neighbor knowledge tracing (SKT), which aims to capture the multi-
|     |     |     |     |     |     |     |     | ple relations | in  | knowledge | structure |     | to model | the | influence |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --------- | --- | -------- | --- | --------- |
Knowledge exercise Knowledgeexercise + answer Knowledge exercise propagation among concepts. SKT is mainly motivated by an
|     | state | embedding | state | embedding | state | embedding |     |     |     |     |     |     |     |     |     |
| --- | ----- | --------- | ----- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |       |           |       | ti        | tk    | E (k      | )   |     |     |     |     |     |     |     |     |
ht E c (j) h x Et x h c educationtheory,transferofknowledge[59],whichclaimsthat
j
|     |     |     |     |     |     |     |     | students’ | knowledge | states | on  | some | relevant | KCs | will also |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | --- | ---- | -------- | --- | --------- |
Update
|     |     |     |     |     |     |     |     | be changed | when | they | are practicing |     | on a | specific | KC due |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---- | -------------- | --- | ---- | -------- | ------ |
f f f to the potential knowledge structure among KCs. Therefore,
|     |     | outgo |     | self |     | income |     |             |           |     |       |               |     |        |          |
| --- | --- | ----- | --- | ---- | --- | ------ | --- | ----------- | --------- | --- | ----- | ------------- | --- | ------ | -------- |
|     |     |       |     |      |     |        |     | a student’s | knowledge |     | state | is determined |     | by not | only the |
temporaleffectfromtheexercisesequence,butalsothespatial
|     |     |     |     |     |     |     |     | effect from | the | knowledge | structure. |     | To concurrently |     | model |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | --------------- | --- | ----- |
thelatentspatialeffects,SKTpresentsthesynchronizationand
partialpropagationmethodstocharacterizetheundirectedand
directedrelationsbetweenKCs,respectively.Inthisway,SKT
Predict
|     |     |     |     |     |     |     |     | measures  | influence | propagation |         | in         | the knowledge |     | structure  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----------- | ------- | ---------- | ------------- | --- | ---------- |
|     |     |     |     |     |     |     |     | with both | temporal  | and         | spatial | relations. | To            | get | rid of de- |
y
t
pendenceonknowledgestructure,Longetal.[60]proposethe
AutomaticalGraph-basedKnowledgeTracing(AGKT),which
Fig.7. Thearchitectureofgraph-basedknowledgetracing[19].
utilizestheautomaticalgraphtomeasurestudents’knowledge
moreover, ht = {ht } represents the student’s temporal states automatically without annotation manual annotations.
i∈V
| knowledge    |     | state after     | answering | the exercise |         | at time | t. The    |                  |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --------- | ------------ | ------- | ------- | --------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|              |     |                 |           |              |         |         |           | D. Summarization |     |     |     |     |     |     |     |
| architecture |     | for graph-based |           | knowledge    | tracing | is      | presented |                  |     |     |     |     |     |     |     |
in Figure 7, which is composed of three parts: (1) aggregate, Itiscrucialtoemphasizethat,despitedeeplearningmodels
| (2) update |     | and (3) | predict. |     |     |     |     |            |          |             |     |          |     |             |      |
| ---------- | --- | ------- | -------- | --- | --- | --- | --- | ---------- | -------- | ----------- | --- | -------- | --- | ----------- | ---- |
|            |     |         |          |     |     |     |     | exhibiting | superior | performance |     | compared |     | to Bayesian | mod- |
In the aggregate module, GKT aggregates the temporal els and logistic models, there remains significant room for
knowledge state and the embedding for the answered KC i improvement in their interpretability and explainability. Due
and its neighboring KC j: to the end-to-end learning strategy, deep learning models are
(cid:40) [ht,atE notoriouslydifficulttointerpret.Themodelingprocessitselfis
|     |     |        |     | s ] (k | =i), |     |      |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ------ | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | h ′t = | k   |        |      |     | (13) |     |     |     |     |     |     |     |     |
k [ht,E alsochallengingtoexplain.Specifically,deeplearningmodels
|     |     |     |     | e (k)] (k | ̸=i), |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k are predominantly data-driven and benefit a lot from large-
where at represents the exercises answered correctly or in- scalestudentlearningdata.Itischallengingtounderstandhow
| correctly | at  | time step | t, E | is the embedding |     | matrix | for the |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ---- | ---------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
s they calculate a student’s knowledge state with no theoretical
learning interactions, E is the embedding matrix for the KC, guidance [33]. All we have are the results generated by these
e
and k represents the k-th row of E . models. Therefore, any errors made by these models will lead
e
In the update module, GKT updates the temporal knowl- students to doubt their reliability. The lack of explainability
edgestatebasedontheaggregatedfeaturesandtheknowledge andinterpretabilityhasthuslimitedtheirfurtherapplicability.
| graph | structure, | as follows: |     |     |     |     |     |         |     |         |     |        |                |     |            |
| ----- | ---------- | ----------- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | ------ | -------------- | --- | ---------- |
|       |            |             |     |     |     |     |     | To make | the | complex | KT  | models | interpretable, |     | especially |
(cid:40)
(h′t)(k those deep learning models, researchers have attempted vari-
|     |     |     | f self | =i), |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mt +1 = k ous methods. Lu et al. [61] presented a post-hoc approach to
|     |     | k   | f        | (h′t,h′t)(k |     | ̸=i), |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | neighbor | i           |     |       |     |     |     |     |     |     |     |     |     |
k (14) revealtheinterpretabilityofDKT.Specifically,theyemployed
|     |     | t +1 | (mt | +1), |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m =G the layer-wise relevance propagation (LRP) technique [62] to
|                       | (cid:102) | k      | ea             | k           |     |        |          |           |            |              |       |               |             |         |         |
| --------------------- | --------- | ------ | -------------- | ----------- | --- | ------ | -------- | --------- | ---------- | ------------ | ----- | ------------- | ----------- | ------- | ------- |
|                       | ht+1      |        | (mt+1,ht),     |             |     |        |          |           |            |              |       |               |             |         |         |
|                       |           | =G     |                |             |     |        |          | interpret | DKT        | by measuring |       | the relevance |             | between | DKT’s   |
|                       |           | k      | gru (cid:102)k | k           |     |        |          |           |            |              |       |               |             |         |         |
|                       |           |        |                |             |     |        |          | output    | and input. | Preliminary  |       | experimental  |             | results | suggest |
| where                 | f self    | is the | multilayer     | perceptron, | G   | ea is  | the same |           |            |              |       |               |             |         |         |
|                       |           |        |                |             |     |        |          | that this | post-hoc   | approach     | could | be            | a promising | method  | for     |
| erase-followed-by-add |           |        | mechanism      | used        | in  | DKVMN, | and      |           |            |              |       |               |             |         |         |
G explaining DKT. Besides, explainable AI (xAI) is proposed to
| gru | is the  | gated recurrent |             | unit (GRU)  | gate | [56]. Moreover, |     |          |           |      |          |        |     |                   |     |
| --- | ------- | --------------- | ----------- | ----------- | ---- | --------------- | --- | -------- | --------- | ---- | -------- | ------ | --- | ----------------- | --- |
|     |         |                 |             |             |      |                 |     | make the | black-box | deep | learning | models |     | more transparent, |     |
| f   | defines | the             | information | propagation |      | to neighboring  |     |          |           |      |          |        |     |                   |     |
neighbor
nodes based on the knowledge graph structure. therebypromotingitsapplications[63].Luetal.[64]proposed
|     |             |         |     |          |     |           |         | to use the | xAI  | technique | to interpret     |     | the complex | KT  | models   |
| --- | ----------- | ------- | --- | -------- | --- | --------- | ------- | ---------- | ---- | --------- | ---------------- | --- | ----------- | --- | -------- |
| In  | the predict | module, | GKT | predicts | the | student’s | perfor- |            |      |           |                  |     |             |     |          |
|     |             |         |     |          |     |           |         | based on   | deep | learning. | The interpreting |     | results     | of  | DKT have |
manceatthenexttimestepaccordingtotheupdatedtemporal
knowledge state: been demonstrated to aid in enhancing the trust of students
|     |     |     |     |        |     |     |     | and teachers. | Their | findings |     | suggested | that | it is | promising |
| --- | --- | --- | --- | ------ | --- | --- | --- | ------------- | ----- | -------- | --- | --------- | ---- | ----- | --------- |
|     |     | yt  |     | ht+1+b |     |     |     |               |       |          |     |           |      |       |           |
k =σ(W k k ), (15) to utilize xAI techniques to interpret the deep learning KT
k
where W k is the weight parameter and b k is the bias term. models, thereby assisting users in accepting and applying the
InadditiontomodelingthegraphstructureinKCsbygraph suggestions provided by these models.
| neural | networks, | Lu  | et al. | [57] propose | to model | the | educa- |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | ------ | ------------ | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
IV. VARIANTSOFKNOWLEDGETRACINGMODELS
tionalrelationandtopologyintheconceptmap,whichwillbe
intendedtoactasmathematicalconstraintsfortheconstruction The aforementioned fundamental KT models are typically
of the KT model. Recently, in the attempt to further explore based on simplistic assumptions regarding the learning pro-

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 9
cess. Specifically, these models predominantly employ learn- Another means of modeling individualization is clustering,
ing interactions such as exercises and responses to estimate which considers a wider range of students in different groups
students’ knowledge states. However, the learning process [69]. By clustering the students into various groups, we can
is not solely represented by exercises and responses, but is train different KT models and make predictions on the test
influenced by various factors. In summary, the aforemen- data. The number of clusters is then varied according to
tioned fundamental KT models, while straightforward, may the student groups and the predicting process is repeated
have reduced performance in real-world learning scenarios. iteratively. Finally, we can obtain a set of different predic-
Consequently, numerous variants have been proposed under tions. Furthermore, there are two common methods used to
more stringent assumptions, reflecting a more comprehensive combine these predictions [70]: (1) uniform averaging, which
learning process in real-world scenarios. Accordingly, we simplyaveragesthepredictions;(2)weightedaveraging,which
classifyandreviewcurrentvariantsoffundamentalKTmodels combines the models by means of a weighted average. To
into four categories: (1) Modeling individualization before realize clustering, K-means is a basic clustering algorithm
learning, (2) Incorporating engagement during learning, (3) that randomly initializes a set of cluster centroids, which are
Considering forgetting after learning, and (4) utilizing side identifiedusingEuclideandistance.Anotherpopularclustering
information across learning. algorithm is spectral clustering, which represents the data
as an undirected graph and analyzes the spectrum of the
graphLaplacianobtainedfromthepairwisesimilaritiesofdata
A. Modeling Individualization before Learning
points. Recently, some novel clustering algorithms have been
Everything and everyone possess unique characteristics. proposed, including discrete nonnegative spectral clustering
For instance, Liu et al. [65] explored several personalized [71] and clustering uncertain data [72].
factors of various tourists to recommend personalized travel Minn et al. [73] propose a model named deep knowledge
packages. Similarly, the concept of individualization in the tracingwithdynamicstudentclassification(DKT-DSC),which
KT task implies that different students often exhibit different introduces individualization to DKT by exploiting the idea
learning characteristics (such as varying learning rates or of clustering. According to students’ previous performance,
prior knowledge). Considering the student-specific variability DKT-DSCassignsstudentswithsimilarlearningabilitytothe
in learning could potentially enhance the KT process, as same group . The knowledge states of students in different
suggested by Yudelson et al. [66]. In the subsequent sections, groups are then traced by different DKT models. Moreover,
we will introduce various variant KT models that take into considering the dynamic property of the learning ability, each
account individualization before learning. student’s learning sequence is segmented into multiple time
The initial BKT paper has delved into the concept of intervals. At the start of each time interval, DKT-DSC will
individualization. Specifically, it uses all students’ learning reassess students’ learning ability and reassign their groups.
interactionsonaspecificKCtolearntheindividualparameter. In DKT-DSC, the K-means clustering algorithm is utilized
Similarly, for a specific student, all her learning interactions to split students with similar ability levels into the same
are utilized to fit her individual learning parameters [9]. group at each time interval. After learning the centroids of
Consequently, BKT is able to ascertain different learning all K clusters, each student is assigned to the nearest cluster.
and performance parameters for various students and KCs. Through dynamic student clustering, DKT-DSC offers an
However, this approach only offers a marginal improvement effective approach to realizing individualization in DKT.
compared to original BKT. Mao et al. [74] claim that it is significant to consider
Subsequently, Pardos and Heffernan [67] propose two sim- both individual exercise representation and individual prior
ple variants of BKT that respectively individualize students’ knowledge. They propose a fine-grained knowledge tracing
initial probability of mastery and the probability of transition model, named FGKT. FGKT obtains the individual exercise
from the unlearned state to the learned state. Specifically, a representation through the acquisition of knowledge cells
student node is added to individualize the initial probability (KCs) and exercise distinctions. Subsequently, it assesses the
of mastery for each student. The student node assigns each individual prior knowledge by evaluating the relevance be-
student with a personalized initial probability of mastery. A tween current and historical learning interactions. Finally, the
conditionalprobabilitytableisdesignedtodeterminethevalue above individual representations will be utilized as the input
of the student node. Similarly, if changing the connection of LSTM in FGKT to evaluate students’ evolving knowledge
of the student node to the subsequent knowledge nodes, the states. Zhao et al. [75] also notice that the individualization
transition probability parameter can also be individualized. of exercises is significant for measuring students’ knowledge
In this case, the student node gives individualized transition states. They propose to consider multiple exercise factors,
parameters to each student. Moreover, rather than individ- including the difficulty and the discrimination, to enhance the
ualizing only one kind of parameter in BKT, some other performance of DKT.
variants of BKT opt to individualize all four BKT parameters Shen et al. [76] propose a convolutional knowledge tracing
simultaneously[66].LeeandBrunskill[68]suggestthatwhen model (CKT) to implicitly measure student individualiza-
applied in an intelligent tutoring system, the individualized tion. Specifically, CKT considers two factors that influence
BKT model can yield good improvements to student learning students’ individualization: individualized learning rates and
efficacy, reducing by about half the amount of questions individualized prior knowledge. Individualized learning rates
required for 20% of students to achieve mastery. represent students’ differing capacities to absorb knowledge.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 10
The sequence of student learning interactions can reflect Schultz and Arroyo [83] further propose the knowledge trac-
different learning rates in the sense that students with high ing with behavior (KTB) model, which has only one latent
learning rates can rapidly master knowledge, while others knowledgenodethatactsasacombinationofbothknowledge
need to spend more time trying and failing. Therefore, it is and engagement. KTB assumes that both engagement and
reasonable to assess the differences in learning rate by simul- performance are expressions of knowledge. The Bayesian
taneously processing several continuous learning interactions estimationoftheknowledgestateneedstobeinferredbyboth
withinaslidingwindowofconvolutionalneuralnetworks[77]. student engagement and performance.
Besides, individualized prior knowledge refers to students’ Mongkhonvanit et al. [84] propose to add five features in
prior knowledge, which can be assessed via their historical the process of watching videos on MOOCs to the input of
learning interactions. DKT. These features reflect student engagement from various
aspects, including playback speed, whether or not the video
was paused, fast-forwarded or rewound, and whether or not
B. Incorporating Engagement during Learning
the video was completed. For example, if a student watches a
Student engagement is defined as ”the quality of effort video at a much faster playback speed, it is likely that he/she
students themselves devote to educationally purposeful ac- is impatient and absent-minded. This model incorporates two
tivities that contribute directly to desired outcomes” [78]. further features: whether or not the exercise was submitted
Thisdefinitionhighlightsastrongconnectionbetweenstudent with an answer selected and whether or not the exercise was
engagement and the learning process. Generally, higher en- a part of an end-of-unit quiz, both of which are considered
gagement leads to enhanced knowledge gains. Consequently, together. Experimental results indicate that DKT can achieve
considering student engagement in the learning process could better performance through incorporating the above binarized
potentially improve knowledge tracing results [79]. In this engagement covariates.
section, we will present some variants that integrate student
engagement into the KT models.
C. Considering Forgetting after Learning
Student engagement is difficult to be directly measured.
In practice, some online learning systems have made use of In real-world scenarios, while learning, forgetting is in-
sensor data to measure student engagement. For example, evitable [85]. The Ebbinghaus forgetting curve theory indi-
inexpensive portable electroencephalography (EEG) devices cates that students’ knowledge proficiency will decline due
canhelptodetectavarietyofstudentmentalstatesinlearning, to forgetting [86]. Recently, Huang et al. [87] proposed the
which can be seen as reflections of student engagement [80]. concept of ’Knowledge Proficiency Tracing’ (KPT), a model
Xu et al. [81] propose two methods that combine EEG- that can dynamically capture the changes in students’ profi-
measured mental states to improve the performance of BKT. ciency levels on knowledge concepts over time. This model
Concretely, the first one inserts a one-dimensional binary effectively tracks these changes in an interpretable manner.
EEG measure into BKT, forming the EEG-BKT structure that Therefore,theassumptionthatstudents’knowledgestateswill
extends BKT by adding a binary variable node E between remainconstantovertimeisuntenable.However,fundamental
the knowledge node and the answer node. The second one, KTmodels,suchastheBKT,oftenoverlookforgetting.Inthe
i.e., EEG-LRKT, utilizes logistic regression to combine an following, we will introduce some variants of fundamental
m-dimensional continuous variable E extracted from the raw KT models that have attempted to consider forgetting after
EEG signal in BKT. learning for more precise knowledge states.
However, in most cases, it is difficult to collect sensor Qiuetal.[88]discoverthatBKTconsistentlyoverestimates
data on every student. Therefore, Schultz and Arroyo [82] the accuracy of students’ answers when a day or more had
propose the knowledge and affect tracing (KAT) to model elapsed since their previous responses. The underlying reason
both knowledge and engagement in parallel. KAT is a sen- isthatBKTassumesthatstudentperformancewillremainthe
sorless model that does not rely on any sensor data. In this same regardless of how much time has passed. To consider
model, both knowledge and engagement are assumed to have how student performance declines with time, they propose
directinfluencesonstudentperformance.KATconsidersthree a BKT-Forget model, which hypothesizes that students may
kinds of disengagement behaviors: quick guess (the student forget information they have learned as days go by. In the
makes an attempt very quickly), bottom-out hint (all available BKT-Forget model, a time node is added to specify which
hints are used) and many attempts (making more than three parameters should be affected by a new day and the new day
attempts at an exercise). These three behaviors are grouped as nodeisfixedwithapriorprobabilityof0.2.Italsointroduced
“gaming” behaviors in order to predict students’ knowledge parameters to represent the forgetting rate on a new day and
and engagement at each learning interaction. Rather than denotetheforgettingrateonthesameday.However,although
assuming equal influence of knowledge and engagement on BKT-forget does consider the decline in student performance,
students’ knowledge state, one variation on the KAT model it can only model forgetting that occurs over the time scale
defines the connection between knowledge and engagement, ofdays.Tomodelthecontinuousdecayofknowledgeastime
andaccordinglyconsidersthatstudents’knowledgestateswill progresses, Nedungadi and Remya [89] incorporate forgetting
influence their engagement. For example, students are more into BKT based on the assumption that learned knowledge
likelytodisengagefromknowledgetheyarenotfamiliarwith. decays exponentially over time [90]. An exponential decay
Moreover,ratherthanexplicitlymodelingstudentengagement, function is thus utilized to update the knowledge mastery

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 11
level. They further assumed that the chance of forgetting will D. Utilizing Side Information across Learning
increaseifastudentdoesnotpracticetheknowledgeconcepts
Most KT models primarily rely on exercises and student
within 30 days. Moreover, Khajah et al. [42] introduce an
responses to evaluate students’ knowledge states. These mod-
approachthatcountsthenumberofinterveningtrialsandtreats
els have yielded impressive results and have been effectively
each as an independent opportunity for forgetting to occur.
implemented in online learning systems. Despite this, there
RecallthePFAmodelinEq.(5),inwhichtheprobabilityof
are various other types of side information collected across
students’masteryisestimatedusingalogisticfunction:p(θ)=
the learning process that could be utilized to enhance these
σ(β+µs+νf). The original PFA model ignores the order of
models. In this section, we will introduce several variants that
answers,inadditiontothetimebetweenlearninginteractions.
aim to leverage this diverse side information across learning.
Itisthereforedifficulttodirectlyincorporatetimeinformation
intotheoriginalPFAmodel.Pela´neketal.[91]proposePFAE In terms of a student’s first response time, a short ini-
tial response time could indicate either high proficiency or
(PFAElo/Extended),avariantofthePFAmodelthatcombines
’gaming’ behavior, while a long initial response time could
PFAwithsomeaspectsoftheEloratingsystem[92].TheElo
indicateeithercarefulthinkingorlackofconcentration.Since
ratingsystemisoriginallydevisedforchessrating(estimating
players’ skills based on match results). In PFAE, θ is updated the connection between initial response time and knowledge
state could be influenced by complex factors, Wang and Hef-
after each learning interaction:
(cid:40) fernan [96] propose to discretize the continuous first response
θ+µ·(1−p(θ)) if the answer was correct,
time into four categories (i.e., extremely short, short, long,
θ := (16)
θ+ν·p(θ) if the answer was wrong. extremely long) to eliminate unnecessary information and
simplify the latent complex possibilities. They then build a
As the forgetting behavior of students is closely related
one-by-four parameter table, in which each column represents
to time, in order to consider forgetting, Pela´nek [93] add a
the category of the initial response time of the previous
time effect function f to θ, i.e., using p(θ+f(t)) instead of
exercise, while the relevant values represent the probability
p(θ), where t is the time (in seconds) from the last learning
of correct answers.
interaction, and f is the time effect function.
Regarding tutor intervention, Beck et al. [97] propose the
To represent the complex forgetting behavior, the DKT-
Bayesian evaluation and assessment model, which simultane-
forget model [94] introduces forgetting into DKT, which
ously assesses students’ knowledge states and evaluates the
considers three types of side information related to forgetting:
lasting impact of tutor intervention. More specifically, it adds
(1) the repeated time gap that represents the interval time
one observable binary intervention node to BKT: True means
between the present interaction and the previous interaction
thatthetutorinterventionoccursincorrespondinginteractions
with the same KC, (2) the sequence time gap that represents
whileFalseindicatestheopposite.Theconnectionbetweenthe
the interval time between the present interaction and the
intervention node and knowledge node indicates the potential
previousinteraction,and(3)pasttrialcountsthatrepresentthe
impactofthetutorinterventiononstudents’knowledgestates.
number of times a student has attempted on the exercise with
The intervention node is linked to all four BKT parameters.
the same KC. All these three features are discretized at log
2
As a result, there are a total of eight parameters to learn in
scale. Those side information is concatenated as additional
order to incorporate tutor intervention. One possible way to
information and represented as a multi-hot vector c , which
t
reduce the number of parameters is choosing to link only the
is integrated with the embedding vector v of the learning
t
interventionnodetothelearningrateparameter[98].Similarly,
interaction, as follows:
Lin and Chi [99] develop the intervention-Bayesian knowl-
v t c =θin(v t ,c t ), (17) edge tracing (Intervention-BKT) model, which incorporates
where θin is the input integration function. The integrated two types of interventions into BKT and distinguishes their
input vc and the previous knowledge state h are passed different effects: elicit and tell. The relations between the
t t−1
through the RNNs to update h in the same way as in Eq.(7). intervention and performance nodes represent the impact of
t
The additional information at the next time step c is also teaching interventions on student performance, while the rela-
t+1
integrated with the updated h : tionsbetweentheinterventionandknowledgenodesrepresent
t
the impact of teaching interventions on students’ knowledge
hc =θout(h ,c ), (18)
t t t+1 states.Therefore,ateachlearninginteraction,whilethepresent
where θout is the output integration function. knowledgestateisconditionalonboththepreviousknowledge
Wang et al. [95] propose a novel HawkesKT model, which state and the current intervention, the student’s performance
introduces the Hawkes process to adaptively model temporal depends on both the present knowledge state and the current
cross-effects. The Hawkes process performs well at modeling intervention.
sequentialeventslocalizedintime,asitcontrolscorresponding Rather than considering only one kind of side informa-
temporal trends by the intensity function. The intensity func- tion, Gonza´lez-Brenes et al. [100] propose a feature-aware
tioninHawkesKTisdesignedtocharacterizetheaccumulative student knowledge tracing (FAST) model, which allows for
effects of previous learning interactions, along with their the utilization of all kinds of side information. Traditional
evolutionsovertime.InHawkesKT,thetemporalcross-effects BKT uses conditional probability tables for the guessing,
andthewaysinwhichtheyevolvebetweenhistoricallearning slipping,transitionandlearningprobabilities,meaningthatthe
interactions combine to form a dynamic learning process. number of features involved in inference grows exponentially.

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 12  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore, as the number of features increases, the time and backwarddirectionstolearnthesemanticwordrepresentation.
space complexity of the model also grow exponentially. To The element-wise max-pooling operation is utilized to merge
deal with this large number of features, FAST uses logistic words’ contextual representations into a global embedding.
regression parameters rather than conditional probability ta- Finally, EKT can update the student’s knowledge state with
bles. The number of features and complexity increase linearly the aid of the semantic representation of each exercise.
rather than exponentially. For parameter learning, FAST uses To achieve more feasible integration of side information,
the Expectation Maximization with Features algorithm [101] Loh [108] present a deep knowledge tracing method with
and focuses on only emission features. The E step uses the decision trees (DKT-DT), which takes advantage of Clas-
| current | parameter | estimates |     | λ to infer | the | probability |     | of the     |     |                |       |        |     |            |     |
| ------- | --------- | --------- | --- | ---------- | --- | ----------- | --- | ---------- | --- | -------------- | ----- | ------ | --- | ---------- | --- |
|         |           |           |     |            |     |             |     | sification |     | And Regression | Trees | (CART) | to  | preprocess | the |
student having mastered the KC at each learning interaction. heterogeneous input features [109]. Specifically, CART is
The parameters λ are now a function of the weight β and the utilizedtoautomaticallypartitionthefeaturespaceandoutputs
feature vector f(t). f is the feature extraction function, and whether or not a student can answer an exercise correctly.
f(t)isthefeaturevectorconstructedfromtheobservationsat Thepredictedresponseandthetrueresponseareencodedinto
therelevanttimestep.Theemissionprobabilityisrepresented a four-bit binary code; for example, the code is 1010 if the
with a logistic function: predictedresponseandthetrueresponsearebothcorrect.This
|     |     |     |     |     | 1   |     |     | binary | code | is then concatenated |     | with | the | original | one-hot |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------------------- | --- | ---- | --- | -------- | ------- |
λ(β)y ′ ,k ′
|     |     |     | =   |     |     | ,   |     | (19) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
1+exp(−βT ·f(t)) encoding of the exercise as the new input of DKT to train the
|       |              |     |             |            |     |             |          | corresponding |     | model. |     |     |     |     |     |
| ----- | ------------ | --- | ----------- | ---------- | --- | ----------- | -------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
| where | β is learned |     | by training | a weighted |     | regularized | logistic |               |     |        |     |     |     |     |     |
regression using a gradient-based search algorithm. Jung et al. [110] suggests that the student’s language pro-
|          |     |           |         |            |           |               |     | ficiency |     | can serve as | supplementary |     | information | to          | improve |
| -------- | --- | --------- | ------- | ---------- | --------- | ------------- | --- | -------- | --- | ------------ | ------------- | --- | ----------- | ----------- | ------- |
| Zhang    | et  | al. [102] | propose | an         | extension | to            | DKT | that     |     |              |               |     |             |             |         |
|          |     |           |         |            |           |               |     | existing |     | KT models.   | The student’s |     | language    | proficiency | is      |
| explored | the | inclusion | of      | additional | features. | Specifically, |     | it       |     |              |               |     |             |             |         |
incorporates an auto-encoder network layer to convert the extractedbyEloratingscoreandtimewindowfeatures.Then,
|                    |           |               |            |          |                 |                |             | the       | language | proficiency        | information   |            | is demonstrated |           | to be      |
| ------------------ | --------- | ------------- | ---------- | -------- | --------------- | -------------- | ----------- | --------- | -------- | ------------------ | ------------- | ---------- | --------------- | --------- | ---------- |
| higher-dimensional |           |               | input data | into     | smaller         | representative |             | fea-      |          |                    |               |            |                 |           |            |
|                    |           |               |            |          |                 |                |             | effective |          | in promoting       | several       | KT models, |                 | including | DKT,       |
| ture vectors,      |           | thereby       | reducing   | both     | the             | resource       | and         | time      |          |                    |               |            |                 |           |            |
|                    |           |               |            |          |                 |                |             | DKVMN,    |          | and SAKT.          | Additionally, | the        | problem         | of        | cold start |
| requirement        |           | for training. | Students’  |          | response        | time,          | opportunity |           |          |                    |               |            |                 |           |            |
|                    |           |               |            |          |                 |                |             | in        | the KT   | task is alleviated | with          | the        | assistance      | of        | language   |
| count,             | and first | action        | are        | selected | as incorporated |                | side        | in-       |          |                    |               |            |                 |           |            |
formation and all input features are converted into a fixed- proficiency information. Liu et al. [111] explore to add side
|        |       |         |            |       |          |               |     | information |     | to the original | KT  | model | by auxiliary |     | learning |
| ------ | ----- | ------- | ---------- | ----- | -------- | ------------- | --- | ----------- | --- | --------------- | --- | ----- | ------------ | --- | -------- |
| length | input | vector. | First, all | input | features | are converted |     | into        |     |                 |     |       |              |     |          |
tasks.Theyspecificallyintroducedtwotasks:(1)predictingthe
categoricaldataandrepresentedasasparsevectorbymeansof
KCsofthequestion,and(2)predictingtheindividualizedprior
| one-hot  | encodings.   |     | These                  | encoded | features | are concatenated |         |            |     |             |      |              |     |             |     |
| -------- | ------------ | --- | ---------------------- | ------- | -------- | ---------------- | ------- | ---------- | --- | ----------- | ---- | ------------ | --- | ----------- | --- |
|          |              |     |                        |         |          |                  |         | knowledge. |     | By training | with | these tasks, | KT  | can enhance | its |
| together | to construct |     | the higher-dimensional |         |          | input            | vector: |            |     |             |      |              |     |             |     |
C(e ,a )=e +(max(e)+1)a , understanding of the intrinsic relationships between questions
|     | t t | t      |     |          | t   |        |     |      |      |                  |           |               |     |              |     |
| --- | --- | ------ | --- | -------- | --- | ------ | --- | ---- | ---- | ---------------- | --------- | ------------- | --- | ------------ | --- |
|     |     |        |     |          |     |        |     | and  | KCs, | while explicitly | capturing | student-level |     | variability. |     |
|     | v   | =O(C(e | ,a  | ))⊕O(C(t | ,a  | ))⊕O(t | ),  | (20) |      |                  |           |               |     |              |     |
t t t t t t When solving programming problems, we can record stu-
′
v =tanh(W v v t +b v ), dents’ full code submissions, which can be employed to
t
where C is the cross feature, O is the one-hot encoder analyze their programming ability. Kasurinen and Nikula
| format,v | representstheresultinginputvectorofeachlearning |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t [112] collected student programming data and analyzed their
interaction, e is the exercise, a refers to the answer, t is the personalizedprogrammingpreferences.Thestudycommenced
|     |     | t   |     | t   |     |     | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
response time, W is the weight parameter and b is the bias with a statistical analysis of student errors, followed by an
|     |     | v   |     |     |     |     | v   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
term. Subsequently, an auto-encoder is introduced to reduce examinationofstudents’programmingstructuresderivedfrom
the dimensionality without incurring the loss of too much their code submissions, and finally used BKT to measure
| important | information. |     | Finally, | the | feature | vectors | extracted |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | -------- | --- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
students’programmingabilities.Wangetal.[113]transformed
by auto-encoder will be the new input of DKT. students’codesubmissionsintoembeddedvectors,andapplied
Liuetal.[103]presentedanotherextensiontoDKT,namely them in DKT to model students’ fine-graded programming
the Exercise-aware Knowledge Tracing (EKT), which utilized knowledge states. Zhu et al. [114] noticed that a single
the potential value of exercises’ text contents. Generally, the programming problem generally involves in multiple KCs,
| text content |     | is of great | significance |     | for students | to  | understand |         |     |               |          |        |             |     |           |
| ------------ | --- | ----------- | ------------ | --- | ------------ | --- | ---------- | ------- | --- | ------------- | -------- | ------ | ----------- | --- | --------- |
|              |     |             |              |     |              |     |            | thereby |     | they proposed | to learn | useful | information |     | about the |
the exercises. For example, Huang et al. [104] used text programming problem’s multiple requirements from students’
| materials | to       | automatically |         | predict | their difficulties, |            | Liu | et al. code | submissions. |     |     |     |     |     |     |
| --------- | -------- | ------------- | ------- | ------- | ------------------- | ---------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
| [105]     | utilized | the text      | content | to      | find similar        | exercises. |     | Yin         |              |     |     |     |     |     |     |
etal.[106]furtherproposedapre-trainingmodelcalledQues-
|         |          |     |         |                 |     |                  |     |     |     | V.  | APPLICATIONS |     |     |     |     |
| ------- | -------- | --- | ------- | --------------- | --- | ---------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| Net for | learning | the | unified | representations |     | of heterogeneous |     |     |     |     |              |     |     |     |     |
exercises. Therefore, instead of using one-hot encoding of Although knowledge tracing is an emerging research area,
exercises, EKT automatically learns the semantic representa- it has already been applied in a wide variety of scenarios.
tion of each exercise from its text contents. EKT first uses In the following, we will first survey the applications of KT
Word2vec [107] to pre-train the embedding vector for each modelsintwotypicaleducationalscenarios:learningresources
word in the exercise. It then constructs a bidirectional LSTM, recommendation and adaptive learning. Then, we will discuss
which captures the word sequence from both forward and broader applications of KT beyond student learning.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 13
A. Learning Resources Recommendation ingly considers the probability that a given video resource
will impart knowledge to a student. Moreover, the transition
Traditionally, learning resources for each student are se-
probability in BKT is conditional only on the presence of
lected in one of two ways. The first one requires teachers
eitheravideooranexercise.Thus,thequalityofthevideocan
to manually select suitable resources that match students’
bedeterminedbyitspromotionoflearning,andthismodelcan
knowledge levels. However, this approach requires substantial
be leveraged as a tool to aid in evaluating and recommending
time and effort, and different teachers may have different
video resources.
preferences. The second one allows students themselves to
Whenrecommendinglearningresources,theprimaryaimof
freely choose resources to learn. However, this may result
existing solutions is to choose a simple strategy for assigning
in students choosing too easy or too difficult materials that
non-mastered exercises to students. While reasonable, it is
will not benefit their learning [115], leading to low learning
also too broad to advance learning effectively. Huang et al.
efficiency.Inrecentyears,theprevalenceofintelligenttutoring
[118] accordingly propose three more beneficial and specific
systems and the development of KT methods have made it
objectives: review and explore, smoothness of difficulty level
possible to automatically recommend appropriate exercises to
and student engagement. In more detail, review and explore
each student based on artificially designed algorithms.
considers both enhancing students’ non-mastered concepts
Exercisesarethemostcommonlearningresourcesinlearn- with timely reviews and reserving certain opportunities to
ing.Giventheinferredknowledgestates,onecommonstrategy explore new knowledge; smoothness of difficulty level indi-
is selecting the next exercise that will best advance students’ cates that the difficulty levels of several continuous exercises
knowledge acquisition. Desmarais and Baker [115] propose should vary within a small range as students gradually learn
two extensions of the original BKT model, which respec- new knowledge; finally, student engagement considers that
tivelyconsideredexercises’difficultiesandstudents’multiple- to promote students’ enthusiasm during learning, the recom-
attempt behaviors. These two extensions are integrated into a mended exercises should be in line with their preferences.
BKT-sequence algorithm to recommend exercises to students In order to support online intelligent education with the
based on their knowledge states. Specifically, BKT-sequence abovethreedomain-specificobjectives,theydevelopedamore
firstdeterminesthepredictedrangeofscoresforeachexercise. reasonablemulti-objectivedeepreinforcementlearning(DRE)
It then computes an expected score for each exercise that the framework. DRE presented three corresponding novel reward
student should get to achieve mastery, which is dependent on functions to capture and quantify the effects of the above
theircurrentknowledgestate(forinstance,alowerknowledge three objectives. This DRE framework is a unified platform
state will result in higher expected scores). Finally, the algo- designedtooptimizemultiplelearningobjectives,wheremore
rithmreturnstheexercisewithapredictedscorethatisclosest reasonable objectives also can be incorporated if necessary.
to that of the expected score. Therefore, as the knowledge ExperimentalresultsshowthatDREcaneffectivelylearnfrom
stateofaparticularKCgrows,moredifficultexerciseswillbe the students’ learning records to optimize multiple objectives
recommended, as harder exercises are associated with a lower and adaptively recommend suitable exercises.
predictivescore.Experimentalresultshaveshownthatstudents
using the BKT-sequence algorithm were able to solve more
B. Adaptive Learning
difficult exercises, obtained higher performance and spent
moretimeinthesystemthanstudentswhousedthetraditional Adaptive learning, unlike learning resource recommenda-
approach. Moreover, students also expressed that the BKT- tions, goes beyond the mere provision of resources. It not
sequence algorithm was more efficient. Wan et al. [116] only concentrates on the selection of appropriate learning
expanded the DKVMN model [37] to include the exercise’s materials but also designs effective learning strategies and
typeanddifficulty.Thismodelisthenusedtoassessstudents’ dynamic learning pathways. These are structured based on
knowledge state and subsequently recommends personalized both the learning rules and students’ evolving knowledge
exercises for each student in Ssmall Private Online Courses states. Specifically, adaptive learning broadly refers to ”a
(SPOCs). They conducted a randomized controlled trial to learning process in which the content taught, or the way such
show the proposed personalized exercise recommendation content is presented, changes or ’adapts’ based on individual
could enhance students’ learning efficiency. student responses, and which dynamically adjusts the level or
In addition to exercises, there are also some other types of types of instruction based on individual student abilities or
multi-modal learning resources, such as videos and figures. preferences” [119].
Machardy [117] utilizes an adaptation of BKT to improve ThefirstfewattemptmadetoapplyKTtoadaptivelearning
student performance prediction by incorporating video ob- was the ACT Programming Tutor (APT) [9], where students
servation. Experimental verification demonstrates the impact were asked to write short programs and BKT was utilized
of both using and eschewing video data, as well as the to estimate their evolving knowledge state. This tutor can
learning rate associated with a particular video. In this way, presentanindividualizedsequenceofexercisestoeachstudent
they further developed a method to help people evaluate the basedontheirestimatedknowledgestatesuntilthestudenthas
quality of video resources. Concretely, they proposed the ”mastered” each rule.
Template 1 Video model to incorporate video observations In recent years, Massive Open Online Courses (MOOCs)
intoBKT,whichaddsvideoactivityasadditionalindependent have become an emerging modality of learning, particularly
observation nodes to the BKT model. This model accord- in higher education. Pardos et al. [11] adapt BKT on the edX

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 14  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
platform. The research object was a 14-week online course acommercialgameforequationsolving,i.e.,DragonBox,with
that included weekly video lectures and corresponding lecture aresearch-basedintelligenttutoringsystem,i.e.,Lynnette.The
problems. BKT was applied to enhance students’ learning results indicated that students who used DragonBox enjoyed
on this course. In order to better adapt BKT to the learning the experience more, while students who used Lynnette per-
platform, the original BKT was modified in several respects. formedsignificantlybetteronthetest.Therefore,itispossible
First, due to the lack of labeled KCs, the problems would toenablestudentstolearneffectivelyandhappilybydesigning
be directly seen as the KCs, while the questions would be suitable educational games on the online learning platform.
seenastheexercisesbelongingtotheKC.Second,inorderto In crowdsourcing, unlabeled data or specific tasks are as-
capturethevaryingdegreesofstudents’knowledgeacquisition signed to various crowd annotators. Understanding the dy-
at each attempt, the modified model assigned different guess namic capabilities of these annotators is crucial in ensuring
and slip parameters to different attempt counts. Third, to deal the reliability of their annotations and promoting the anno-
with the problem of multiple pathways in the system, which tation efficiency. Wang et al. [124] developed a framework
reflected that the impacts on learning may come from various called KT4Crowd, which utilized KT methods to predict the
resources, they framed the influence of resources on learning performance of annotators, which surpassed traditional rating
as a credit/blame inference problem. systems.Besides,Abdietal.[125]observedthatstudents’par-
Generally, students’ cognitive structures include both stu- ticipation in crowdsourcing tasks can enhance their learning.
dents’knowledgelevelandtheknowledgestructureoflearning KT methods can also better comprehend students’ knowledge
items (e.g., one-digit addition is the prerequisite knowledge states, aided by the students’ annotated items.
of two-digit addition). Therefore, adaptive learning should Crowston et al. [126] develop an online citizen science
maintain consistency with both students’ knowledge level and project that employs machine learning techniques to improve
thelatentknowledgestructure.Nevertheless,existingmethods the training of new volunteers using authentic tasks featuring
for adaptive learning often focus separately on either the uncertain outcomes, such as image classification. Specifically,
knowledgelevelsofstudents(i.e.,withthehelpofspecificKT they employ the BKT model to monitor the knowledge states
models)ortheknowledgestructureoflearningitems.Tofully of volunteers, enabling them to more efficiently complete
exploit the cognitive structure for adaptive learning, Liu et al. assigned tasks and contribute meaningfully to the project.
[13] propose a Cognitive Structure Enhanced framework for Zhao et al. [127] develop an automated exercise collection
adaptive Learning (CSEAL). CSEAL conceptualized adaptive approachforteachers,employingtheKTmodelandreinforce-
learning as a Markov Decision Process. It first utilized DKT ment learning. Specifically, the exercise collection need to be
to trace the evolving knowledge states of students at each well-designed to align with students’ abilities. This study first
learning step. Subsequently, the authors designed a navigation leverages the KT model to forecast students’ performance on
algorithm based on the knowledge structure to ensure that unseenexercisecandidates.Subsequently,theexerciseselector
|              |       |             |     |          |      |         |     | is designed | based | on  | the KT model’s | predictions, |     | ensuring |     |
| ------------ | ----- | ----------- | --- | -------- | ---- | ------- | --- | ----------- | ----- | --- | -------------- | ------------ | --- | -------- | --- |
| the learning | paths | in adaptive |     | learning | were | logical | and |             |       |     |                |              |     |          |     |
reasonable,whichalsoreducedthesearchspaceinthedecision thattheexercisecollectionisbothapproximateandoptimized.
process. Finally, CSEAL utilized the actor-critic algorithm Similarly, Shang et al. [128] design a reinforcement learning
to dynamically determine what should be learned next. In guided method for exam paper generation, where the DKT
this way, CSEAL can sequentially identify the most suitable model is utilized to measure examinees’ knowledge states.
| learning | resources | for different | students. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VI. DATASETSANDBASELINES
|                 |              |                      |                   |              |       |                  |         | After    | introducing     | above      | KT models         | and        | variants,   |               | to bet- |
| --------------- | ------------ | -------------------- | ----------------- | ------------ | ----- | ---------------- | ------- | -------- | --------------- | ---------- | ----------------- | ---------- | ----------- | ------------- | ------- |
| C. Broader      | Applications |                      |                   |              |       |                  |         |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | ter help | researchers     | and        | practitioners     | who        | want        | to            | further |
| The above       | two          | types of             | applications      |              | are   | most commonly    |         |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | conduct  | related         | work       | and promote       | the        | application | of            | KT,     |
| used for        | KT in        | student learning.    |                   | In addition, |       | the KT           | methods |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | we have  | open sourced    |            | two algorithm     | libraries, |             | i.e., EduData |         |
| can be expanded |              | to be utilized       | in                | any systems  |       | that necessitate |         |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | that for | downloading     |            | and preprocessing |            | most        | existing      | KT-     |
| continuous      | evaluation   | of                   | user capabilities |              | or    | states.          | We will |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | related  | datasets,       | and EduKTM | that              | includes   | extensible  |               | and     |
| introduce       | some         | broader applications |                   | of           | KT in | this section.    |         |          |                 |            |                   |            |             |               |         |
|                 |              |                      |                   |              |       |                  |         | unified  | implementations |            | of existing       | popular    | KT          | models.       | In      |
Ingamingsystems,theparadigmoftracingstudents’knowl-
|            |           |              |            |                  |           |              |        | the following, | we         | will give | detailed | introduction |     | of these | two |
| ---------- | --------- | ------------ | ---------- | ---------------- | --------- | ------------ | ------ | -------------- | ---------- | --------- | -------- | ------------ | --- | -------- | --- |
| edge state | can       | also work    | for player | modeling.        |           | Here,        | player |                |            |           |          |              |     |          |     |
|            |           |              |            |                  |           |              |        | algorithm      | libraries. |           |          |              |     |          |     |
| modeling,  | which     | is the study |            | of computational |           | models       | of     |                |            |           |          |              |     |          |     |
| players in | games,    | aims to      | capture    | human            | players’  | characteris- |        |                |            |           |          |              |     |          |     |
| tics and   | cognitive | features     | [120].     | For              | instance, | Fisch        | et al. | A. Datasets    |            |           |          |              |     |          |     |
[121] reveal that children engage in cycles of increasingly As we have mentioned, KT emerges from the development
sophisticatedmathematicalthinkingoverthecourseofplaying ofonlineeducation,wherealargenumberofstudents’learning
anonlinegame.Kantharajuetal.[122]presentanapproachto data is collected for analyzing their learning behaviors and
trace player knowledge in a parallel programming educational knowledgestates.Inthissection,wemainlyintroduceexisting
game,whichiscapableofmeasuringthecurrentplayers’real- public datasets available for evaluating KT models. Table
time state across the different skills required to play an edu- II lists all datasets, as well as their basic information and
cational game based only on in-game player activities. Long statistics. In our released EduData, we provide the service
and Aleven [123] conduct a classroom experiment comparing of downloading and preprocessing all these datasets, which

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 15  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEII
BASICINFORMATIONANDSTATISTICSOFEXISTINGDATASETSAVAILABLEFOREVALUATINGKTMODELS.
|          |     |          |     |                |     |             |           | Sources     |     |          |           | Statistics |     |                 |     |
| -------- | --- | -------- | --- | -------------- | --- | ----------- | --------- | ----------- | --- | -------- | --------- | ---------- | --- | --------------- | --- |
|          |     |          |     |                |     | Side        | Online    | Educational |     | #of      | #of       |            | #of | #of             |     |
| Datasets |     | Subjects |     | LearningStages |     | Information |           |             |     |          |           |            |     |                 |     |
|          |     |          |     |                |     |             | platforms | challenges  |     | Students | Exercises |            | KCs | Learningrecords |     |
ASSISTments2009[129] mathematics middleschool Yes (cid:33) 4,163 17,751 123 346,860
ASSISTments2012[130] mathematics middleschool Yes (cid:33) 46,674 179,999 265 6,123,270
ASSISTments2015 mathematics middleschool No (cid:33) 19,917 / 100 708,631
frommiddleschool
ASSISTments2017 mathematics Yes (cid:33) 1,709 3,162 102 942,816
tocollege
|     |     |     |     | fromprimary |     |     | (cid:33) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Junyi[131] mathematics tohighschool Yes 247,606 722 41 25,925,922
fromprimary
Eedi2020[132] mathematics Yes (cid:33) 118,971 27,613 388 15,867,850
tohighschool
(cid:33)
Statics2011[133] engineering university Yes 335 1,224 80 361,092
EdNet-KT1[134] english / Yes (cid:33) 784,309 13,169 188 95,293,926
EdNet-KT2[134] english / Yes (cid:33) 297,444 13,169 188 56,360,602
EdNet-KT3[134] english / Yes (cid:33) 297,915 13,169 293 89,270,654
EdNet-KT4[134] english / Yes (cid:33) 297,915 13,169 293 131,441,538
(cid:33)
CodeWorkout[135] programming university Yes 819 50 50 >130,000
is convenient to help beginners analyze and utilize them scaffoldingproblemsasthesameasmainproblems,and(3)
quickly. In summary, these datasets are collected in different repeated response sequences with different KCs. The latest
learning scenarios, so that they exhibit an extremely distinct version of ASSISTments2009 has fixed these problems.
differenceindatascale,subject,andsoon,indicatingcomplex • ASSISTments2012. ASSISTments2012 is collected from
applications in practical for KT models. the ASSISTments system, in the school year from 2012
1) ASSISTments Datasets: ASSISTments [129], created in to 2013 with affect predictions. Compared with ASSIST-
2004, is an online tutoring system in the United States, ments2009,ASSISTments2012hasmuchmorestudents,ex-
ercises,aswellaslearningrecords.However,manylearning
whichprovidesstudentswithbothassessmentinformationand
tutoringassistance.WhileworkingonASSISTments,students records have missed the related KCs in this dataset. After
will be provided with instructional assistance to help them filteringtheserecords,thereareonly29,018students,53,091
solve the problem in several substeps when they give wrong exercises, and 2,711,813 learning records. Besides, this
answers. After obtaining correct answers, they will be given a dataset contains more side information, such as start time,
newone.Meanwhile,thesystemwilllearnaboutthestudents’ end time, problem type, and average confidence. It worth
knowledge states and predict how they will do in future notingthatyoucanaccesstothetextoftheexercisesinAS-
tests. Up to now, the organizers have released four public SISTments2012formorefine-grainedresearch.Specifically,
youcanemailnth@wpi.eduandcctd@wpi.edu,explaining
| avaliable datasets | from | ASSISTments, |     | which | are | respectively |     |     |     |     |     |     |     |     |     |
| ------------------ | ---- | ------------ | --- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ASSISTments2009,ASSISTments20123,ASSISTments20154, yourpurposeandpromisingnottoshareitwithanyoneelse.
and ASSISTments20175. The ASSISTments datasets have ASSISTments2015. ASSISTments2015 covers the 2015
•
built profound impacts in the research community of KT, school years’ student response records on ASSISTments.
which can be seen in many related papers. Most of these This dataset only contains student learning records on 100
|               |           |      |             |     |           |         | KCs, | there | is no | information | about | the | exercise, | as  | well as |
| ------------- | --------- | ---- | ----------- | --- | --------- | ------- | ---- | ----- | ----- | ----------- | ----- | --- | --------- | --- | ------- |
| datasets were | collected | from | mathematics |     | in middle | school, |      |       |       |             |       |     |           |     |         |
the details of them are listed as follows. any other side information.
|                    |     |     |           |     |                 |     | ASSISTments2017. |     |     | ASSISTments2017 |     |     | is the | dataset | used |
| ------------------ | --- | --- | --------- | --- | --------------- | --- | ---------------- | --- | --- | --------------- | --- | --- | ------ | ------- | ---- |
| • ASSISTments2009. |     | The | full name | of  | ASSISTments2009 |     | •                |     |     |                 |     |     |        |         |      |
is the ASSISTments 2009-2010 skill builder data set [129], in the 2017 ASSISTments Longitudinal Data Mining Com-
|     |     |     |     |     |     |     | petition. | This | dataset | collected |     | data over | a   | decade, | which |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------- | --------- | --- | --------- | --- | ------- | ----- |
whichwascollectedformASSISTments’skillbuilderprob-
|     |     |     |     |     |     |     | tracked | students’ |     | intercations | at  | the ASSISTments |     |     | learning |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | --------------- | --- | --- | -------- |
lemsetsduringtheschoolyearfrom2009to2010.Students
|            |            |     |           |           |           |           | platform | from   | middle         | school | study | in   | 2004-2007 |      | to their |
| ---------- | ---------- | --- | --------- | --------- | --------- | --------- | -------- | ------ | -------------- | ------ | ----- | ---- | --------- | ---- | -------- |
| were asked | to work    | on  | exercises | with      | similar   | knowledge |          |        |                |        |       |      |           |      |          |
|            |            |     |           |           |           |           | high     | school | course-taking, |        | until | they | graduated | from | the      |
| concepts   | until they | can | answer    | correctly | for three | or more   |          |        |                |        |       |      |           |      |          |
times in a row. This dataset contains many valuable side college.Therefore,theaveragelearningrecordofstudentsin
ASSISTments2017ismuchlongerthanotherdataset,which
| information,    | such        | as          | attempt          | count that      | represents | the          |           |                   |            |           |         |                 |         |             |          |
| --------------- | ----------- | ----------- | ---------------- | --------------- | ---------- | ------------ | --------- | ----------------- | ---------- | --------- | ------- | --------------- | ------- | ----------- | -------- |
|                 |             |             |                  |                 |            |              | is beyond |                   | the length | of        | 1,000.  | ASSISTments2017 |         |             | also has |
| number          | of attempts | of          | the student,     | ms              | first      | reponse that |           |                   |            |           |         |                 |         |             |          |
|                 |             |             |                  |                 |            |              | rich      | side information, |            | including |         | but not         | limited | to AveKnow  |          |
| represents      | the time    | in          | the milliseconds |                 | for the    | student’s    |           |                   |            |           |         |                 |         |             |          |
|                 |             |             |                  |                 |            |              | that      | indicates         | students’  |           | average | knowledge       |         | level based | on       |
| first response, | and         | opportunity |                  | that represents |            | the number   |           |                   |            |           |         |                 |         |             |          |
BKT,timeTakenthatrepresentsthetimespentonthecurrent
| of opportunities |          | the student | has                | to practice. | It  | worth noting |           |     |                 |          |      |            |         |     |           |
| ---------------- | -------- | ----------- | ------------------ | ------------ | --- | ------------ | --------- | --- | --------------- | -------- | ---- | ---------- | ------- | --- | --------- |
|                  |          |             |                    |              |     |              | exercise, |     | frIsHelpRequest |          | that | represents | whether |     | the first |
| that the         | original | version     | of ASSISTments2009 |              |     | has three    |           |     |                 |          |      |            |         |     |           |
|                  |          |             |                    |              |     |              | response  | is  | a help          | request. |      |            |         |     |           |
seriousproblemsthatleadtounreliableexperimentalresults
[45]: (1) a large number of duplicated records, (2) treating 2) Junyi Dataset: The Junyi dataset [131] contains the
|     |     |     |     |     |     |     | problem | log | and | exercise-related |     | information |     | on the | Junyi |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---------------- | --- | ----------- | --- | ------ | ----- |
3https://sites.google.com/site/assistmentsdata/datasets/2012-13-school-data- Academy6, a Chinese e-learning website established in 2012
with-affect
|     |     |     |     |     |     |     | on the | basis | of  | the open-source |     | code | released | by  | Khan |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --------------- | --- | ---- | -------- | --- | ---- |
4https://sites.google.com/site/assistmentsdata/datasets/2015-assistments-
skill-builder-data
5https://sites.google.com/view/assistmentsdatamining/dataset 6http://www.junyiacademy.org/

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     | 16  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Academy. In contrast to the ASSISTments datasets, Junyi has pictureorlisteningmaterial.Therefore,exercisescomeupin
less exercsies and KCs, but includes an exercise hierarchy bundles and students have to answer all contained exercises
labeledbyexperts,theannotationsofexerciserelationshipare when a bundle is given.
alsoavailable.Therefore,manyresearchworksthatfocusedon EdNet-KT2. EdNet-KT2 recorded students’ action se-
•
the knowledge structure in KT had utilized this dataset [58]. quences, which indicated their full learning behaviors. For
Junyi provides the prerequisite exercise of a specific exercise example, a student who is not confident about the answer
in the knowledge map, the topic and area of each exercise, as may alternately select among several answer choices before
well as the coordiate position of the knowledge map. submitting. Such learning behaviors can reflect more fine-
|             |          |     |          |         |       |         | grained | knowledge | state | of students. |     | EdNet-KT2 | contains |
| ----------- | -------- | --- | -------- | ------- | ----- | ------- | ------- | --------- | ----- | ------------ | --- | --------- | -------- |
| 3) Eedi2020 | Dataset: | The | Eedi2020 | dataset | [132] | is also |         |           |       |              |     |           |          |
released in an achedemic challenge, i.e., NeurIPS 2020 Ed- three kinds of actions: enter when student first receives and
ucation Challenge7. This dataset contains students’ answers viewsabundle,respondwhenthestudentselectsananswer
to mathematics questions from Eedi, an online educational choicetotheexercise,andsubmit whenthestudentsubmits
platformwhichmillionsofstudentsinteractwithdailyaround his final answers to the the given bundle. It is worth noting
|           |             |      |         |       |               |     | that EdNet-KT2 |     | is a subset | of  | EdNet-KT1. |     |     |
| --------- | ----------- | ---- | ------- | ----- | ------------- | --- | -------------- | --- | ----------- | --- | ---------- | --- | --- |
| the globe | from school | year | 2018 to | 2020. | All exercises | are |                |     |             |     |            |     |     |
multiple-choice problems with 4 possible answer choices, ex- • EdNet-KT3. On the basis of EdNet-KT2, EdNet-KT3 col-
actlyoneofwhichiscorrect.InTableII,wegivethestatistics lected more students’ learning activities, such as reading
basedonthetrainingdatainthiscompetition,thetotalnumber explanations or watching lectures. These learning activities
of learning records in the full dataset exceeds 17 million. have potential impacts on students’ knowledge state so that
|          |             |          |       |           |       |        | they are | valuable | to be | analyzed. |     |     |     |
| -------- | ----------- | -------- | ----- | --------- | ----- | ------ | -------- | -------- | ----- | --------- | --- | --- | --- |
| It worth | noting that | Eedi2020 | gives | students’ | exact | answer |          |          |       |           |     |     |     |
choice so that we can also predict students options [136]. • EdNet-KT4. In EdNet-KT4, the very fine details of actions
Moreover, for the students, Eedi2020 records lots of valuable were provided. In particular, the following types of actions
context information, including the Gender, DateOfBirth, Pre- are added to EdNet-KT3: erase choice, undo erase choice,
miumPupil. For the learning records, Eedi2020 also presents play audio, pause audio, play video, pause video, pay,
their Confidence, GroupId, QuizId, and SchemeOfWorkId. refund, and enroll coupon.
4) Statics2011 Dataset: Different from the above datasets 6) CodeWorkout Dataset: The CodeWorkout dataset [135]
that focus on mathematics exercises, the Statics2011 dataset is utilized in the 2nd Computer Science Educational Data
[133] is obtained from a college-level engineering statics Mining Challenge (CSEDM)10. This dataset is collected from
course via online educational system developed by Carnegie aCS1courseintheSpringandFall2019semestersatapublic
University8.
Mellon The problems in college engineering university in United States. It contains the code submissions
course are quite complex, often comprising numerous inde- from students for 50 coding problems, each requiring 10-
pendent sub-steps. Consequently, we treat each sub-problem 26 lines of code. In this dataset, each exercise has a unique
as an exercise and calculate the number of exercises and KCs KC, thereby the number of KCs is equal to the number of
within this dataset. exercises.Intotal,thereare329and490studentsintheSpring
5) EdNet Dataset: The EdNet dataset [134] is related to and Fall semesters who completed the course. Each dataset
the english subject, which is consisted of students’ learning containsmorethan65,000codesubmissions,thescoresofthe
records in the multi-platform AI tutoring system Santa in submissions(%ofunittestspasses)arealsoavailable,aswell
South Korea9. EdNet collected learning data of students over as the compiler message if the compilation is not successful.
twoyearsfortheirpreparationoftheeTOEIC(TestofEnglish The final grades of students are also provided for this dataset.
forInternationalCommunication)ListeningandReadingTest.
| EdNetisnowthelargestpublicdatasetinKTfieldwithatotal |          |         |      |         |           |     | B. Baselines        |     |     |             |     |         |               |
| ---------------------------------------------------- | -------- | ------- | ---- | ------- | --------- | --- | ------------------- | --- | --- | ----------- | --- | ------- | ------------- |
| of 131,441,538                                       | learning | records | from | 784,309 | students. | Be- |                     |     |     |             |     |         |               |
|                                                      |          |         |      |         |           |     | The implementations |     |     | of existing | KT  | methods | are not stan- |
sides,itcontainsvariousfeaturesofstudents’learningactions, dardized, which may use different program languages (e.g.,
suchasthespecificlearningmaterialtheyhaveinteracted,how
|     |     |     |     |     |     |     | python, | lua) and | different | deep | learning | frameworks | (e.g., |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------- | ---- | -------- | ---------- | ------ |
much time they have spent for answering a given exercise. tensorflow, torch). Furthermore, some works did not well
TherearefourdiffernetversionsofEdNet,respectivelynamed
organizethecodessystematically(e.g.,themissingofrunning
| EdNet-KT1, | EdNet-KT2, | EdNet-KT3, |     | and | EdNet-KT4 | with |              |     |                |     |       |        |                 |
| ---------- | ---------- | ---------- | --- | --- | --------- | ---- | ------------ | --- | -------------- | --- | ----- | ------ | --------------- |
|            |            |            |     |     |           |      | environments | and | dependencies), |     | which | brings | difficulties in |
differentextents.Wenotethatthestudentsinthisdatasetmay reproducing the models. To this end, we put forward the
| be in different | learning | states. | Therefore | we  | do not | give the |           |         |        |            |       |         |       |
| --------------- | -------- | ------- | --------- | --- | ------ | -------- | --------- | ------- | ------ | ---------- | ----- | ------- | ----- |
|                 |          |         |           |     |        |          | algorithm | library | for KT | baselines, | named | EduKTM, | which |
learning state information in Table II. now has contained the concurrent popular works. EduKTM
• EdNet-KT1. EdNet-KT1 contains students’ basic exercise- will be always under development for including the latest KT
answering logs. This dataset has 784,309 students, 13,169 models, more algorithms and features are going to be added.
exercises, 188 KCs, and a total of 95,293,926 learning Besides, we provide detailed guidelines for everyone who is
records. Exercises in EdNet-KT1 are organized by bundles, interested in contributing to EduKTM.
i.e., a collection of exercises sharing a common passage, It worth nothing that we do not provide the performance
|     |     |     |     |     |     |     | evaluation | of these | baselines | using | the | aforementioned | bench- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | ----- | --- | -------------- | ------ |
7https://eedi.com/projects/neurips-education-challenge markdatasets.Thereasonsaretwo-folds:(1)Foreachbaseline
8https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=507
9https://github.com/riiid/ednet 10https://sites.google.com/ncsu.edu/csedm-dc-2021/home

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 17
method, their experimental settings are quite different as they employed contrastive learning to alleviate the data sparsity
were designed to handle with various learning scenarios. No problem in KT [141, 142]. For example, Lee et al. [143]
single KT model can always be the best one under various presented a contrastive learning framework to enhance KT,
learning contexts. It is not fair to compare all baselines under which measure the semantical similarity between various
a fixed setting. (2) Existing evaluation standards primarily learning interactions to effectively learn their representations.
concentrate on the performance of student performance pre- They further designed data augmentation methods to enhance
diction task, which cannot directly reflect the effectiveness of the semantics of students’ learning interactions. However,
various KT models in practical applications. Therefore, we while the aforementioned methods alleviate the data sparsity
decide to open source EduData and EduKTM. Researchers problem in various aspects, there remains a need for further
and practitioners can freely compare and select appropriate improvement in addressing this issue comprehensively.
KT models based on their specific requirements in various
application scenarios. C. Knowledge Tracing with Subjective Exercises
Most existing KT researches are capable of dealing with
VII. FUTURERESEARCHDIRECTIONS
objective exercises, assuming student responses are binary.
This survey has comprehensively reviewed the abundant However, they overlook students’ open-ended answers, often
current developments in the field of knowledge tracing, in- presented in natural language, on subjective exercises. As per
cluding fundamental KT models, their variations and typical the work by Liu et al. [144], an open-ended KT approach
applications. Despite this, as knowledge tracing is a relatively for computer science education was explored. This method
new but promising research area, there are still a substantial aimed to predict students’ precise solutions to programming
number of problems that require urgent resolution. In this questions,utilizinglanguagemodelsforassistance.Recentad-
section,wediscussseveralpotentialfutureresearchdirections. vancementsinlargelanguagemodelsofferpromisingpotential
toenhancetheabilityofKTmodelstocomprehendthecritical
information regarding students’ knowledge states embedded
A. Knowledge Tracing with Interpretability
withintheiropen-endedanswersonsubjectiveexercises[145].
The performance of KT models is now evaluated indirectly
through the student performance prediction task. The higher
D. Knowledge Tracing with Students’ Feedback
the precision of students’ responses on future exercises, the
Learning records are passive representations of students’
bettertheKTmodel’sperformance.Nonetheless,interpretabil-
knowledge states. In contrast, students’ feedback provides
ity plays a significant role in education, as students often
us with their proactive understanding of their knowledge
express more concern about the ’why’ than the ’what’ of
states, thereby offering direct and authentic indicators of their
a learning decision [137]. Enhancing the interpretability of
learningsituation.However,therearefewKTmodelsthattake
KT models is therefore crucial. Some educational theories,
advantage of training data related to students’ feedback, even
such as the Rasch model used in AKT [21] and the transfer
though it can play an important role in fixing the KT results
of knowledge used in SKT [58], could be considered for
[146]. Wang et al. [147] have noted that feedback plays a
this purpose. Minn et al. [138] noticed the significance of
positive role in learning, which may promote transfer and
interpretable KT, particularly for deep learning models, as
retention in learning from worked-out examples. Therefore,
theyhavenumerousparametersthatarechallengingtoexplain
incorporatingstudents’feedbackpresentsameaningfulavenue
meaningfully. Thus, they [138] introduced a straightforward
that could lead to significant improvements.
and interpretable KT approach, based on the causal rela-
tionships within the latent features extracted from students’
behavioral data. Zhu et al. [29] attempted to introduce causal E. Knowledge Tracing for General User Modeling
inference for explanatory analysis on KT, and they achieved Generally, user modeling refers to tools for characterizing
more stable and explainable knowledge tracing based on the users’ behaviors (e.g., frequent locations), personal informa-
analysis results. It is imperative to further refine existing KT tion (e.g., age, gender, and occupation) and latent features
models or to explore additional methods for interpretable KT (e.g., interests and abilities), which facilitate the provision of
researches. This will lead to the production of more accurate targeted services for different users [148]. As a type of latent
and interpretable evaluations of students’ knowledge states. featuremodeling,knowledgetracingdiagnosestheproficiency
of users (not only individuals, but also groups of individuals,
B. Knowledge Tracing with Sparse Learning Interactions like user teams and companies) on specific skills/concepts.
Thus, in addition to education, knowledge tracing can be
The acquisition of high-quality KT models necessarily re-
developed and applied across a wide range of domains for
quiresasubstantialamountofdatatoensuretrainingstability.
user modeling, including games, sports, and recruitment.
However, online learning systems often achieve less learning
interactionsinpracticaleducationalscenarios,therebyleading
F. Knowledge Tracing with Large Language Models
to the data sparsity problem. To address this issue, Yang
et al. [139] utilized graph convolutional network to include In recent years, the advancement of large language models
exercise-KCcorrelations.Huangetal.[140]turnedtoimprove (LLM), notably ChatGPT, has led to significant impacts and
the attention mechanism. More recently, researchers have garnered considerable research interest worldwide [149]. The

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 18
useofLLMineducationispromisingtorevolutionizethecur- distance to traverse before achieving a completely transparent
rent learning pattern [145]. The current study mainly focuses deep learning KT model.
on generating learning materials, improving student-system We posit that the application of KT methods in online edu-
interaction, and explaining educational contents. However, cationpresentsapromisingavenueforresearch.Itsignificantly
it remains unclear how LLM can assist in understanding enhancesthelearningexperienceforstudentswhilesimultane-
students’ knowledge states. Given the powerful capabilities ouslyalleviatingtheburdenonteachers.Despitethenumerous
ofLLM,ithasthepotentialtoenhancethegeneralizationand challenges and obstacles, researchers are be encouraged to
interpretabilityofexistingKTmethods.Specifically,LLMcan overcome them and ensure a reliable and equitable access to
analyze the content of students’ responses and evaluate their students’ evolving knowledge state in learning.
quality, which directly reflects students’ knowledge states.
Besides, LLM can play the role of the instructor, answering
ACKNOWLEDGMENT
questions for students and identifying their strengths and
weaknesses. Furthermore, LLM itself can serve as a KT This research was supported by grants from the National
model, which can output reasonable results about students’ Key Research and Development Program of China (Grant
knowledge states given their previous learning interactions. No. 2021YFF0901003), and the National Natural Science
Simultaneously, it is imperative to safeguard the privacy and Foundation of China (Grant No. 62337001, U20A20229).
security of student data when utilizing LLM [150].
REFERENCES
[1] G. Mckenna, “Theory and practice of online learning,” International
VIII. DISCUSSIONSANDCONCLUSIONS
JournalofInformationManagement,vol.29,no.6,pp.503–504,2009.
[2] A. Sun and X. Chen, “Online education and its effective practice:
In this survey, we conducted a thorough review of knowl-
A research review,” Journal of Information Technology Education
edgetracing.Specifically,weinitiallyconductedacomprehen- Research,vol.15,no.2016,pp.157–190,2015.
sive review of existing fundamental KT models. Considering [3] M. Wang, M. Wang, Y. Cui, and H. Zhang, “Art teachers’ attitudes
toward online learning: an empirical study using self determination
the complexity of online learning systems and the significant
theory,”FrontiersinPsychology,vol.12,p.627095,2021.
importance of KT research in practical scenarios, we inves- [4] K.VanLEHN,“Therelativeeffectivenessofhumantutoring,intelligent
tigated a broad range of variant KT research. Subsequently, tutoring systems, and other tutoring systems,” Educational Psycholo-
gist,vol.46,no.4,pp.197–221,2011.
we summarized some typical applications of KT in common
[5] A.CullyandY.Demiris,“Onlineknowledgeleveltrackingwithdata-
educationalscenarios.Furthermore,wereleasedtwoalgorithm driven student models and collaborative filtering,” IEEE Transactions
libraries for KT-related datasets and baselines, thereby facil- onKnowledgeandDataEngineering,vol.32,no.10,pp.2000–2013,
2020.
itating researchers and practitioners in selecting appropriate
[6] M.Guo,M.Wang,andB.Li,“Acasestudyofmobileblendedlearning
KT models based on their specific requirements. Finally, we inteachingenglishasaforeignlanguage.”inIntelligentEnvironments
outlined some potential future directions. (Workshops),2019,pp.269–279.
[7] L.Jiang,K.Liu,Y.Wang,D.Wang,P.Wang,Y.Fu,andM.Yin,“Re-
We hope that this comprehensive survey of knowledge
inforced explainable knowledge concept recommendation in moocs,”
tracing will assist readers in understanding the problem of ACM Transactions on Intelligent Systems and Technology, vol. 14,
modeling students’ dynamic knowledge states. It serves as a no.3,pp.1–20,2023.
[8] L. Jiang, Y. Wang, S. Xie, J. Wu, M. Yin, and J. Wang, “Which
fundamental framework for both researchers and practition-
courses to choose? recommending courses to groups of students in
ers in future studies, fostering the development of KT. The online tutoring platforms,” Applied Intelligence, vol. 53, no. 10, pp.
development of KT will directly benefit millions of students, 11727–11736,2023.
[9] A. T. Corbett and J. R. Anderson, “Knowledge tracing: Modeling
with its impact potentially extending to a broader audience
the acquisition of procedural knowledge,” User Modelling and User-
as online learning continues to evolve. In this context, KT AdaptedInteraction,vol.4,no.4,pp.253–278,1995.
willplayanincreasinglyimportantroleinenablingindividuals [10] C. E. Dowling and C. Hockemeyer, “Automata for the assessment of
knowledge,”IEEETransactionsonKnowledgeandDataEngineering,
to adapt to the ever-changing society [151]. Furthermore, the
vol.13,no.3,pp.451–461,2001.
development of more refined KT methods tailored to students [11] Z.A.Pardos,Y.Bergner,D.T.Seaton,andD.E.Pritchard,“Adapting
in various subjects and age groups will enhance their ability bayesian knowledgetracing toa massive openonline coursein edx.”
EducationalDataMining,vol.13,pp.137–144,2013.
to comprehend students’ individual knowledge states.
[12] J. Cowan, “A learner centered approach to online education,” British
However, we recognize some limitations of the current JournalofEducationalTechnology,vol.44,no.6,p.E221–E222,2013.
survey. Firstly, as new KT methods continue to emerge, [13] Q. Liu, S. Tong, C. Liu, H. Zhao, E. Chen, H. Ma, and S. Wang,
“Exploiting cognitive structure for adaptive learning,” in Proceedings
although we have conducted a thorough investigation, there
of the 25th ACM SIGKDD International Conference on Knowledge
maybesomerepresentativeworksthatwehaveoverlooked.If Discovery&DataMining,2019,pp.627–635.
necessary, we will incorporate these into our proposed frame- [14] J.H.BlockandR.B.Burns,“Masterylearning,”ReviewofResearch
inEducation,vol.4,no.1,pp.3–49,1976.
work in the future. Secondly, the complexity of KT methods
[15] H. Cen, K. Koedinger, and B. Junker, “Learning factors analysis–a
warrants attention, as it continues to grow, particularly in general method for cognitive model evaluation and improvement,” in
those based on deep learning. The complexity of the model International Conference on Intelligent Tutoring Systems. Springer,
2006,pp.164–175.
may enhance its accuracy, but it could also compromise its
[16] P. I. Pavlik Jr, H. Cen, and K. R. Koedinger, “Performance factors
applicability, as users will question the reliability of complex analysis–a new alternative to knowledge tracing.” Online Submission,
models. Despite the fact that some studies have attempted to 2009.
[17] R. J. Williams and D. Zipser, “A learning algorithm for continually
revealtheinterpretabilityofcomplexKTmodels,forinstance,
running fully recurrent neural networks,” Neural computation, vol. 1,
by utilizing the xAI technique, there remains a significant no.2,pp.270–280,1989.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 19
[18] C. Piech, J. Bassen, J. Huang, S. Ganguli, M. Sahami, L. J. Guibas, ConferenceonUserModeling,Adaptation,andPersonalization,2012.
andJ.Sohl-Dickstein,“Deepknowledgetracing,”inneuralinformation [41] S.Rendle,“Factorizationmachines,”in2010IEEEInternationalCon-
processingsystems,2015,pp.505–513. ferenceonDataMining,2010,pp.995–1000.
[19] H. Nakagawa, Y. Iwasawa, and Y. Matsuo, “Graph-based knowledge [42] M.Khajah,R.V.Lindsey,andM.C.Mozer,“Howdeepisknowledge
tracing:Modelingstudentproficiencyusinggraphneuralnetwork,”in tracing?”arXivpreprintarXiv:1604.02416,2016.
2019 IEEE/WIC/ACM International Conference on Web Intelligence [43] S.HochreiterandJ.Schmidhuber,“Longshort-termmemory,”Neural
(WI). IEEE,2019,pp.156–163. computation,vol.9,no.8,pp.1735–1780,1997.
[20] S. Pandey and G. Karypis, “A self-attentive model for knowledge [44] C.-K. Yeung and D.-Y. Yeung, “Addressing two problems in deep
tracing,”arXivpreprintarXiv:1907.06837,2019. knowledge tracing via prediction-consistent regularization,” arXiv
[21] A. Ghosh, N. Heffernan, and A. S. Lan, “Context-aware attentive preprintarXiv:1806.02180,2018.
knowledge tracing,” in Proceedings of the 26th ACM SIGKDD Inter- [45] X.Xiong,S.Zhao,E.G.VanInwegen,andJ.E.Beck,“Goingdeeper
national Conference on Knowledge Discovery & Data Mining, New withdeepknowledgetracing.”EducationalDataMining,2016.
York,NY,USA,2020,p.2330–2339. [46] A. Graves, G. Wayne, M. Reynolds, T. Harley, I. Danihelka,
[22] R. Schmucker, J. Wang, S. Hu, and T. M. Mitchell, “Assessing the A. Grabska-Barwin´ska, S. G. Colmenarejo, E. Grefenstette, T. Ra-
performance of online students–new data, new approaches, improved malho, J. Agapiou et al., “Hybrid computing using a neural network
accuracy.” Journal of Educational Data Mining, vol. 14, no. 1, pp. withdynamicexternalmemory,”Nature,vol.538,no.7626,pp.471–
1–45,2022. 476,2016.
[23] G. Abdelrahman, Q. Wang, and B. Nunes, “Knowledge tracing: A [47] G. Abdelrahman and Q. Wang, “Knowledge tracing with sequential
survey,”ACMComputingSurveys,vol.55,no.11,pp.1–37,2023. key-valuememorynetworks,”inProceedingsofthe42ndInternational
[24] L. Razzaq, J. Patvarczki, S. F. Almeida, M. Vartak, M. Feng, N. T. ACMSIGIRConferenceonResearchandDevelopmentinInformation
Heffernan,andK.R.Koedinger,“Theassistmentbuilder:Supporting Retrieval. ACM,jul2019.
thelifecycleoftutoringsystemcontentcreation,”IEEETransactions [48] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
onLearningTechnologies,vol.2,no.2,pp.157–166,2009. trainingofdeepbidirectionaltransformersforlanguageunderstanding,”
[25] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. inProceedingsofthe2019ConferenceoftheNorth. Associationfor
Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in ComputationalLinguistics,2019.
Advances in neural information processing systems, 2017, pp. 5998– [49] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,
6008. A.Neelakantan,P.Shyam,G.Sastry,A.Askelletal.,“Languagemod-
[26] Y.Choi,Y.Lee,J.Cho,J.Baek,B.Kim,Y.Cha,D.Shin,C.Bae,and elsarefew-shotlearners,”Advancesinneuralinformationprocessing
J.Heo,“Towardsanappropriatequery,key,andvaluecomputationfor systems,vol.33,pp.1877–1901,2020.
knowledgetracing,”ser.L@S’20,2020,p.341–344. [50] X. Wang, X. Mei, Q. Huang, Z. Han, and C. Huang, “Fine-grained
[27] D.Shin,Y.Shim,H.Yu,S.Lee,B.Kim,andY.Choi,“Saint+:Integrat- learningperformancepredictionviaadaptivesparseself-attentionnet-
ing temporal features for ednet correctness prediction,” in LAK2021: works,”InformationSciences,vol.545,pp.223–240,2021.
11thInternationalLearningAnalyticsandKnowledgeConference,apr [51] J.Zhu,W.Yu,Z.Zheng,C.Huang,andG.P.C.Fung,Learningfrom
2021. InterpretableAnalysis:Attention-BasedKnowledgeTracing,2020.
[28] S. Shen, E. Chen, Q. Liu, Z. Huang, W. Huang, Y. Yin, Y. Su, [52] F.M.Lord,ApplicationsofItemResponseTheorytoPracticalTesting
and S. Wang, “Monitoring student progress for learning process- Problems. LAWRENCEERLBAUMASSCCIAATES,1980.
consistent knowledgetracing,” IEEE Transactionson Knowledgeand [53] S. Pu and L. Becker, “Self-attention in knowledge tracing: Why
DataEngineering,2022. it works,” in International Conference on Artificial Intelligence in
[29] J.Zhu,X.Ma,andC.Huang,“Stableknowledgetracingusingcausal Education. Springer,2022,pp.731–736.
inference,” IEEE Transactions on Learning Technologies, pp. 1–11, [54] Y.Yin,L.Dai,Z.Huang,S.Shen,F.Wang,Q.Liu,E.Chen,andX.Li,
2023. “Tracingknowledgeinsteadofpatterns:Stableknowledgetracingwith
[30] R.Pela´nek,“Bayesianknowledgetracing,logisticmodels,andbeyond: diagnostic transformer,” in Proceedings of the ACM Web Conference
anoverviewoflearnermodelingtechniques,”UserModelingandUser- 2023,2023,pp.855–864.
AdaptedInteraction,vol.27,no.3-5,pp.313–350,2017. [55] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu, “A
[31] X. Song, J. Li, T. Cai, S. Yang, T. Yang, and C. Liu, “A survey on comprehensive survey on graph neural networks,” arXiv preprint
deep learning based knowledge tracing,” Knowledge-Based Systems, arXiv:1901.00596,2019.
vol.258,p.110036,2022. [56] K.Cho,B.VanMerrie¨nboer,C.Gulcehre,D.Bahdanau,F.Bougares,
[32] T.Liu,“Knowledgetracing:Abibliometricanalysis,”Computersand H.Schwenk,andY.Bengio,“Learningphraserepresentationsusingrnn
Education:ArtificialIntelligence,p.100090,2022. encoder-decoderforstatisticalmachinetranslation,”ArXiv:1406.1078,
[33] A. Zanellati, D. Di Mitri, M. Gabbrielli, and O. Levrini, “Hybrid 2014.
models for knowledge tracing: a systematic literature review,” IEEE [57] Y.Lu,P.Chen,Y.Pian,andV.W.Zheng,“Cmkt:Conceptmapdriven
TransactionsonLearningTechnologies,2024. knowledge tracing,” IEEE Transactions on Learning Technologies,
[34] P. I. Pavlik, L. G. Eglington, and L. M. Harrell-Williams, “Logistic vol.15,no.4,pp.467–480,2022.
knowledge tracing: A constrained framework for learner modeling,” [58] S. Tong, Q. Liu, W. Huang, Z. Huang, E. Chen, C. Liu, H. Ma,
IEEETransactionsonLearningTechnologies,vol.14,no.5,pp.624– andS.Wang,“Structure-basedknowledgetracing:Aninfluenceprop-
639,2021. agation view,” in Proceedings of the The 19th IEEE International
[35] T.Ka¨ser,S.Klingler,A.G.Schwing,andM.Gross,“Dynamicbayesian ConferenceonDataMining,2020.
networksforstudentmodeling,”IEEETransactionsonLearningTech- [59] RoyerandM.James,“Theoriesofthetransferoflearning,”Educational
nologies,vol.10,no.4,pp.450–462,2017. Psychologist,vol.14,no.1,pp.53–69,1979.
[36] J.-J.VieandH.Kashima,“Knowledgetracingmachines:Factorization [60] T. Long, Y. Liu, W. Zhang, W. Xia, Z. He, R. Tang, and Y. Yu,
machinesforknowledgetracing,”inProceedingsoftheAAAIConfer- “Automaticalgraph-basedknowledgetracing,”2022.
enceonArtificialIntelligence,vol.33,2019,pp.750–757. [61] Y. Lu, D. Wang, Q. Meng, and P. Chen, “Towards interpretable deep
[37] J. Zhang, X. Shi, I. King, and D.-Y. Yeung, “Dynamic key-value learningmodelsforknowledgetracing,”inArtificialIntelligenceinEd-
memorynetworksforknowledgetracing,”inProceedingsofthe26th ucation:21stInternationalConference,AIED2020,Ifrane,Morocco,
International Conference on World Wide Web. International World July6–10,2020,Proceedings,PartII21. Springer,2020,pp.185–190.
WideWebConferencesSteeringCommittee,2017. [62] G.Montavon,A.Binder,S.Lapuschkin,W.Samek,andK.-R.Mu¨ller,
[38] X. Huang, Q. Liu, C. Wang, H. Han, J. Ma, E. Chen, Y. Su, “Layer-wise relevance propagation: an overview,” Explainable AI:
and S. Wang, “Constructing educational concept maps with multiple interpreting, explaining and visualizing deep learning, pp. 193–209,
relationships from multi-source data,” in 2019 IEEE International 2019.
ConferenceonDataMining(ICDM),2019,pp.1108–1113. [63] W. Saeed and C. Omlin, “Explainable ai (xai): A systematic meta-
[39] N. Thai-Nghe, L. Drumond, T. Horva´th, A. Krohn-Grimberghe, survey of current challenges and future opportunities,” Knowledge-
A.Nanopoulos,andL.Schmidt-Thieme,“Factorizationtechniquesfor BasedSystems,vol.263,p.110273,2023.
predictingstudentperformance,”inEducationalrecommendersystems [64] Y. Lu, D. Wang, P. Chen, Q. Meng, and S. Yu, “Interpreting deep
and technologies: Practices and challenges. IGI Global, 2012, pp. learning models for knowledge tracing,” International Journal of
129–153. ArtificialIntelligenceinEducation,vol.33,no.3,pp.519–542,2023.
[40] N. Thai-Nghe, L. Drumond, T. Horva´th, and L. Schmidt-Thieme, [65] Q. Liu, Y. Ge, Z. Li, E. Chen, and H. Xiong, “Personalized travel
“Usingfactorizationmachinesforstudentmodeling.”inInternational packagerecommendation,”inIEEE11thInternationalConferenceon

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 20
DataMining. IEEE,2011,pp.407–416. matter?modelingtheeffectoftimewithbayesianknowledgetracing.”
[66] M. V. Yudelson, K. R. Koedinger, and G. J. Gordon, “Individualized inEducationalDataMining,2011,pp.139–148.
bayesian knowledge tracing models,” in Lecture Notes in Computer [89] P. Nedungadi and M. Remya, “Incorporating forgetting in the per-
Science. SpringerBerlinHeidelberg,2013,pp.171–180. sonalized, clustered, bayesian knowledge tracing (pc-bkt) model,” in
[67] Z. A. Pardos and N. T. Heffernan, “Modeling individualization in 2015InternationalConferenceoncognitivecomputingandinformation
a bayesian networks implementation of knowledge tracing,” in User processing(CCIP). IEEE,2015,pp.1–5.
Modeling, Adaptation, and Personalization. Springer Berlin Heidel- [90] G.R.Loftus,“Evaluatingforgettingcurves.”JournalofExperimental
berg,2010,pp.255–266. Psychology:Learning,Memory,andCognition,vol.11,no.2,p.397,
[68] J. I. Lee and E. Brunskill, “The impact on individualizing student 1985.
modelsonnecessarypracticeopportunities.”InternationalEducational [91] R.Pela´nek,J.Papousˇek,andV.Stanislav,“Adaptivepracticeoffacts
DataMiningSociety,2012. in domains with varied prior knowledge,” in Proceedings of the 7th
[69] Z.A.Pardos,S.Trivedi,N.T.Heffernan,andG.N.Sa´rko¨zy,“Clustered International Conference on Educational Data Mining. London,
knowledgetracing,”inInternationalConferenceonIntelligentTutoring UnitedKingdom:InternationalEducationalDataMiningSociety,2014,
Systems,2012,pp.405–410. pp.6–13.
[70] S. Trivedi, Z. A. Pardos, and N. T. Heffernan, “Clustering students [92] R. Pela´nek, “Application of time decay functions and elo system in
to generate an ensemble to improve standard test score predictions,” studentmodeling,”inEducationalDataMining,2014.
in International conference on artificial intelligence in education. [93] R. Pela´nek, “Modeling students’ memory for application in adaptive
Springer,2011,pp.377–384. educationalsystems.”InternationalEducationalDataMiningSociety,
[71] Y. Yang, F. Shen, Z. Huang, H. T. Shen, and X. Li, “Discrete 2015.
nonnegativespectralclustering,”IEEETransactionsonKnowledgeand [94] K.Nagatani,Q.Zhang,M.Sato,Y.-Y.Chen,F.Chen,andT.Ohkuma,
DataEngineering,vol.29,no.9,pp.1834–1845,2017. “Augmenting knowledge tracing by considering forgetting behavior,”
[72] B.Jiang,J.Pei,Y.Tao,andX.Lin,“Clusteringuncertaindatabasedon inTheWorldWideWebConference. ACM,may2019.
probability distribution similarity,” IEEE Transactions on Knowledge [95] C.Wang,W.Ma,M.Zhang,C.Lv,F.Wan,H.Lin,T.Tang,Y.Liu,
andDataEngineering,vol.25,no.4,pp.751–763,2013. and S. Ma, “Temporal cross-effects in knowledge tracing,” ser. The
[73] S. Minn, Y. Yu, M. C. Desmarais, F. Zhu, and J.-J. Vie, “Deep InternationalConferenceonWebSearchandDataMining. NewYork,
knowledge tracing and dynamic student classification for knowledge NY,USA:AssociationforComputingMachinery,2021,p.517–525.
tracing,” in 2018 IEEE International Conference on Data Mining [96] Y. Wang and N. T. Heffernan, “Leveraging first response time into
(ICDM). IEEE,nov2018. theknowledgetracingmodel.”InternationalEducationalDataMining
[74] S.Mao,J.Zhan,Y.Wang,andY.Jiang,“Improvingknowledgetracing Society,2012.
viaconsideringtwotypesofactualdifferencesfromexercisesandprior [97] J.E.Beck,K.-m.Chang,J.Mostow,andA.Corbett,“Doeshelphelp?
knowledge,” IEEE Transactions on Learning Technologies, vol. 16, introducing the bayesian evaluation and assessment methodology,” in
no.3,pp.324–338,2023. International Conference on Intelligent Tutoring Systems. Springer,
[75] Y.Zhao,H.Ma,W.Wang,W.Gao,F.Yang,andX.He,“Exploiting 2008,pp.383–394.
multiplequestionfactorsforknowledgetracing,”ExpertSystemswith [98] M.SaoPedro,R.Baker,andJ.Gobert,“Incorporatingscaffoldingand
Applications,vol.223,p.119786,2023. tutor context into bayesian knowledge tracing to predict inquiry skill
[76] S. Shen, Q. Liu, E. Chen, H. Wu, Z. Huang, W. Zhao, Y. Su, acquisition,”inEducationalDataMining,2013.
H. Ma, and S. Wang, “Convolutional knowledge tracing: Modeling [99] C.LinandM.Chi,“Intervention-bkt:incorporatinginstructionalinter-
individualization in student learning process,” SIGIR ’20: The 43rd ventionsintobayesianknowledgetracing,”inInternationalconference
InternationalACMSIGIRconferenceonresearchanddevelopmentin onintelligenttutoringsystems. Springer,2016,pp.208–218.
InformationRetrievalVirtualEventChinaJuly,2020,pp.1857–1860, [100] J.Gonza´lez-Brenes,Y.Huang,andP.Brusilovsky,“Generalfeaturesin
2020. knowledgetracingtomodelmultiplesubskills,temporalitemresponse
[77] Y.LeCun,Y.Bengio,andG.Hinton,“Deeplearning,”nature,vol.521, theory,andexpertknowledge,”inThe7thInternationalConferenceon
no.7553,p.436,2015. EducationalDataMining. UniversityofPittsburgh,2014,pp.84–91.
[78] V.Trowler,“Studentengagementliteraturereview,”Thehighereduca- [101] T. Berg-Kirkpatrick, A. Bouchard-Coˆte´, J. DeNero, and D. Klein,
tionacademy,vol.11,no.1,pp.1–15,2010. “Painless unsupervised learning with features,” in The 2010 Annual
[79] R. M. Carini, G. D. Kuh, and S. P. Klein, “Student engagement and Conference of the North American Chapter of the Association for
studentlearning:Testingthelinkages,”Researchinhighereducation, ComputationalLinguistics,2010,pp.582–590.
vol.47,no.1,pp.1–32,2006. [102] L. Zhang, X. Xiong, S. Zhao, A. Botelho, and N. T. Heffernan, “In-
[80] C.Berka,D.J.Levendowski,M.N.Lumicao,A.Yau,G.Davis,V.T. corporatingrichfeaturesintodeepknowledgetracing,”inProceedings
Zivkovic, R. E. Olmstead, P. D. Tremoulet, and P. L. Craven, “Eeg oftheFourth(2017)ACMConferenceonLearning@Scale,2017,pp.
correlatesoftaskengagementandmentalworkloadinvigilance,learn- 169–172.
ing,andmemorytasks,”Aviation,space,andenvironmentalmedicine, [103] Q.Liu,Z.Huang,Y.Yin,E.Chen,H.Xiong,Y.Su,andG.Hu,“EKT:
vol.78,no.5,pp.B231–B244,2007. Exercise-awareknowledgetracingforstudentperformanceprediction,”
[81] Y.Xu,K.-m.Chang,Y.Yuan,andJ.Mostow,“Eeghelpsknowledge IEEETransactionsonKnowledgeandDataEngineering,vol.33,no.1,
tracing!” in Workshop on Utilizing EEG Input in Intelligent Tutoring pp.100–115,2021.
Systems(ITS2014WSEEG),2014,p.43. [104] Z.Huang,Q.Liu,E.Chen,H.Zhao,M.Gao,S.Wei,Y.Su,andG.Hu,
[82] S. Schultz and I. Arroyo, “Tracing knowledge and engagement in “Questiondifficultypredictionforreadingproblemsinstandardtests,”
parallelinanintelligenttutoringsystem,”inEducationalDataMining, inProceedingsoftheAAAIConferenceonArtificialIntelligence,2017.
2014. [105] Q. Liu, Z. Huang, Z. Huang, C. Liu, E. Chen, Y. Su, and G. Hu,
[83] S.E.SchultzandI.Arroyo,“Modelingtheinterplaybetweenknowl- “Findingsimilarexercisesinonlineeducationsystems,”inProceedings
edge and affective engagement in students,” International Journal of of the 24th ACM SIGKDD International Conference on Knowledge
People-OrientedProgramming(IJPOP),vol.3,no.2,pp.56–74,2014. Discovery&DataMining,2018,pp.1821–1830.
[84] K. Mongkhonvanit, K. Kanopka, and D. Lang, “Deep knowledge [106] Y. Yin, Q. Liu, Z. Huang, E. Chen, W. Tong, S. Wang, and Y. Su,
tracing and engagement with moocs,” in Proceedings of the 9th “Quesnet: A unified representation for heterogeneous test questions,”
International Conference on Learning Analytics & Knowledge, 2019, inProceedingsofthe25thACMSIGKDDInternationalConferenceon
pp.340–342. KnowledgeDiscovery&DataMining,2019,pp.1328–1336.
[85] S.MarkovitchandP.D.Scott,“Theroleofforgettinginlearning,”in [107] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean,
MachineLearningProceedings1988. Elsevier,1988,pp.459–465. “Distributed representations of words and phrases and their composi-
[86] Y. Chen, Q. Liu, Z. Huang, L. Wu, E. Chen, R. Wu, Y. Su, and tionality,”inAdvancesinneuralinformationprocessingsystems,2013,
G.Hu,“Trackingknowledgeproficiencyofstudentswitheducational pp.3111–3119.
priors,” The 26th ACM International Conference on Information and [108] W.-Y.Loh,“Classificationandregressiontrees,”WileyInterdisciplinary
KnowledgeManagement(CIKM’2017),pp.989–998,2017. Reviews:DataMiningandKnowledgeDiscovery,vol.1,no.1,pp.14–
[87] Z. Huang, Q. Liu, Y. Chen, L. Wu, K. Xiao, E. Chen, H. Ma, and 23,2011.
G. Hu, “Learning or forgetting? a dynamic approach for tracking the [109] L.P.CheungandH.Yang,“Heterogeneousfeaturesintegrationindeep
knowledgeproficiencyofstudents,”ACMTransactionsonInformation knowledgetracing,”inInternationalConferenceonNeuralInformation
Systems(TOIS),vol.38,no.2,pp.1–33,2020. Processing. Springer,2017,pp.653–662.
[88] Y.Qiu,Y.Qi,H.Lu,Z.A.Pardos,andN.T.Heffernan,“Doestime [110] H.Jung,J.Yoo,Y.Yoon,andY.Jang,“Languageproficiencyenhanced

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 21
knowledgetracing,”inInternationalConferenceonIntelligentTutoring DataMiningSociety(IEDMS),2015,pp.532–535.
Systems. Springer,2023,pp.3–15. [132] Z. Wang, A. Lamb, E. Saveliev, P. Cameron, Y. Zaykov, J. M.
[111] Z.Liu,Q.Liu,J.Chen,S.Huang,B.Gao,W.Luo,andJ.Weng,“En- Herna´ndez-Lobato,R.E.Turner,R.G.Baraniuk,C.Barton,S.P.Jones,
hancingdeepknowledgetracingwithauxiliarytasks,”inProceedings S.Woodhead,andC.Zhang,“Diagnosticquestions:Theneurips2020
oftheACMWebConference2023,2023,pp.4178–4187. educationchallenge,”arXivpreprintarXiv:2007.12061,2020.
[112] J.KasurinenandU.Nikula,“Estimatingprogrammingknowledgewith [133] “AdatarepositoryfortheEDMcommunity:ThePSLCDataShop,”in
bayesianknowledgetracing,”ACMSIGCSEBulletin,vol.41,no.3,pp. HandbookofEducationalDataMining. CRCPress,2010,pp.65–78.
313–317,2009. [134] Y. Choi, Y. Lee, D. Shin, J. Cho, S. Park, S. Lee, J. Baek, C. Bae,
[113] L. Wang, A. Sy, L. Liu, and C. Piech, “Deep knowledge tracing on B. Kim, and J. Heo, “Ednet: A large-scale hierarchical dataset in
programming exercises,” in Proceedings of the fourth (2017) ACM education,”2019.
conferenceonlearning@scale,2017,pp.201–204. [135] S. H. Edwards and K. P. Murali, “Codeworkout: short programming
[114] M. Zhu, S. Han, P. Yuan, and X. Lu, “Enhancing programming exercises with built-in data collection,” in Proceedings of the 2017
knowledgetracingbyinteractingprogrammingskillsandstudentcode,” ACM conference on innovation and technology in computer science
in LAK22: 12th International Learning Analytics and Knowledge education,2017,pp.188–193.
Conference,2022,pp.438–443. [136] A. Ghosh, J. Raspat, and A. Lan, “Option tracing: Beyond correct-
[115] M. C. Desmarais and R. S. Baker, “A review of recent advances in ness analysis in knowledge tracing,” in International Conference on
learnerandskillmodelinginintelligentlearningenvironments,”User ArtificialIntelligenceinEducation. Springer,2021,pp.137–149.
ModelingandUser-adaptedInteraction,vol.22,no.1,pp.9–38,2012. [137] Q.Li,X.Yuan,S.Liu,L.Gao,T.Wei,X.Shen,andJ.Sun,“Agenetic
[116] H. Wan, Z. Zhong, L. Tang, and X. Gao, “Pedagogical interventions causal explainer for deep knowledge tracing,” IEEE Transactions on
inspocs:Learningbehaviordashboardsandknowledgetracingsupport EvolutionaryComputation,2023.
exerciserecommendation,”IEEETransactionsonLearningTechnolo- [138] S.Minn,J.-J.Vie,K.Takeuchi,H.Kashima,andF.Zhu,“Interpretable
gies,vol.16,no.3,pp.431–442,2023. knowledgetracing:Simpleandefficientstudentmodelingwithcausal
[117] Z. Machardy, “Applications of Bayesian Knowledge Tracing to the relations,”inProceedingsoftheAAAIConferenceonArtificialIntelli-
CurationofEducationalVideos,”ElectricalEngineeringandComputer gence,vol.36,no.11,2022,pp.12810–12818.
SciencesUniversityofCaliforniaatBerkeleyTechnical,2015. [139] Y.Yang,J.Shen,Y.Qu,Y.Liu,K.Wang,Y.Zhu,W.Zhang,andY.Yu,
[118] Z. Huang, Q. Liu, C. Zhai, Y. Yin, and G. Hu, “Exploring multi- “Gikt: a graph-based interaction model for knowledge tracing,” in
objective exercise recommendations in online education systems,” in MachineLearningandKnowledgeDiscoveryinDatabases:European
The 28th ACM International Conference on Information and Knowl- Conference, ECML PKDD 2020, Ghent, Belgium, September 14–18,
edgeManagement,2019. 2020,Proceedings,PartI. Springer,2021,pp.299–315.
[119] S.OxmanandW.Wong,“WhitePaper:AdaptiveLearningSystems,” [140] S. Huang, Z. Liu, X. Zhao, W. Luo, and J. Weng, “Towards robust
DV X Innovations DeVry Education Group, no. February, pp. 1–30, knowledge tracing models via k-sparse attention,” in Proceedings
2014. of the 46th International ACM SIGIR Conference on Research and
[120] G. N. Yannakakis, P. Spronck, D. Loiacono, and E. Andre´, “Player DevelopmentinInformationRetrieval,2023,pp.2441–2445.
modeling,”DagstuhlFollowUps,2013. [141] X.Song,J.Li,Q.Lei,W.Zhao,Y.Chen,andA.Mian,“Bi-clkt:Bi-
[121] S.M.Fisch,R.Lesh,E.Motoki,S.Crespo,andV.F.Melfi,“Children’s graphcontrastivelearningbasedknowledgetracing,”Knowledge-Based
mathematical reasoning in online games: Can data mining reveal Systems,vol.241,p.108274,2022.
strategicthinking?”ChildDevelopmentPerspectives,vol.5,no.2,pp. [142] H. Dai, Y. Yun, Y. Zhang, W. Zhang, and X. Shang, “Contrastive
88–92,2011. deep knowledge tracing,” in International conference on artificial
[122] P.Kantharaju,K.Alderfer,J.Zhu,B.Char,B.Smith,andS.Ontao´n, intelligenceineducation. Springer,2022,pp.289–292.
“Tracing player knowledge in a parallel programming educational [143] W. Lee, J. Chun, Y. Lee, K. Park, and S. Park, “Contrastive learning
game,”2019. for knowledge tracing,” in Proceedings of the ACM Web Conference
[123] Y. Long and V. Aleven, “Educational game and intelligent tutoring 2022,2022,pp.2330–2338.
system: A classroom study and comparative design analysis,” ACM [144] N. Liu, Z. Wang, R. Baraniuk, and A. Lan, “Open-ended knowledge
Transactions on Computer-Human Interaction, vol. 24, no. 3, pp. 1– tracing for computer science education,” in Proceedings of the 2022
27,2017. Conference on Empirical Methods in Natural Language Processing,
[124] Z. Wang, H. Sun, and T. Han, “Predicting crowdsourcing worker 2022,pp.3849–3862.
performance with knowledge tracing,” in Knowledge Science, En- [145] E. Kasneci, K. Seßler, S. Ku¨chemann, M. Bannert, D. Dementieva,
gineering and Management: 13th International Conference, KSEM F.Fischer,U.Gasser,G.Groh,S.Gu¨nnemann,E.Hu¨llermeieretal.,
2020,Hangzhou,China,August28–30,2020,Proceedings,PartII13. “Chatgptforgood?onopportunitiesandchallengesoflargelanguage
Springer,2020,pp.352–359. models for education,” Learning and individual differences, vol. 103,
[125] S. Abdi, H. Khosravi, and S. Sadiq, “Modelling learners in crowd- p.102274,2023.
sourcingeducationalsystems,”inArtificialIntelligenceinEducation: [146] E.Vasilyeva,S.Puuronen,M.Pechenizkiy,andP.Rasanen,“Feedback
21stInternationalConference,AIED2020,Ifrane,Morocco,July6–10, adaptation in web-based learning systems,” International Journal of
2020,Proceedings,PartII21. Springer,2020,pp.3–9. Continuing Engineering Education and Life Long Learning, vol. 17,
[126] K.Crowston,C.Østerlund,T.K.Lee,C.Jackson,M.Harandi,S.Allen, no.4/5,p.337,2007.
S.Bahaadini,S.Coughlin,A.K.Katsaggelos,S.L.Larson,N.Rohani, [147] M. Wang, Z. K. Yang, S. Y. Liu, H. N. H. Cheng, and Z. Liu,
J.R.Smith,L.Trouille,andM.Zevin,“Knowledgetracingtomodel “Usingfeedbacktoimprovelearning:Differentiatingbetweencorrect
learning in online citizen science projects,” IEEE Transactions on anderroneousexamples,”inInternationalSymposiumonEducational
LearningTechnologies,vol.13,no.1,pp.123–134,2020. Technology,2015.
[127] T.-Y. Zhao, M. Zeng, and J.-H. Feng, “An exercise collection auto- [148] G. Fischer, “User modeling in human–computer interaction,” User
assembling framework with knowledge tracing and reinforcement Modeling and User-Adapted Interaction, vol. 11, no. 1-2, pp. 65–86,
learning,”JournalofComputerScienceandTechnology,vol.37,no.5, 2001.
pp.1105–1117,2022. [149] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min,
[128] Y.Shang,X.Luo,L.Wang,H.Peng,X.Zhang,Y.Ren,andK.Liang, B. Zhang, J. Zhang, Z. Dong et al., “A survey of large language
“Reinforcement learning guided multi-objective exam paper genera- models,”arXivpreprintarXiv:2303.18223,2023.
tion,” in Proceedings of the 2023 SIAM International Conference on [150] X.Pan,M.Zhang,S.Ji,andM.Yang,“Privacyrisksofgeneral-purpose
DataMining(SDM). SIAM,2023,pp.829–837. languagemodels,”in2020IEEESymposiumonSecurityandPrivacy
[129] M.Feng,N.Heffernan,andK.Koedinger,“Addressingtheassessment (SP). IEEE,2020,pp.1314–1331.
challenge with an online system that tutors as it assesses,” USER- [151] M.Wotto,“Thefuturehigheducationdistancelearningincanada,the
ADAP,vol.19,no.3,pp.243–266,2009. unitedstates,andfrance:Insightsfrombeforecovid-19secondarydata
[130] Y. Wang, N. T. Heffernan, and C. Heffernan, “Towards better affect analysis,”JournalofEducationalTechnologySystems,2020.
detectors: Effect of missing skills, class features and common wrong
answers,” in Proceedings of the Fifth International Conference on
Learning Analytics And Knowledge, ser. LAK ’15. New York, NY,
USA:AssociationforComputingMachinery,2015,p.31–35.
[131] H. Chang, H. Hsu, and K. Chen, “Modeling exercise relationships in
e-learning: A unified approach,” in EDM. International Educational

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 22  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Shuanghong Shen recieved the B.E. degree from Minghao Yin (Member, IEEE) received the B.S.
Wuhan University, Wuhan, China, in 2018. He is and M.S. degrees from Northeast Normal Univer-
currently working toward the Ph.D. degree in the sity, Changchun, China, in 2001 and 2004, respec-
School of Computer Science and Technology, Uni- tively, and the Ph.D. degree from Jilin University,
versity of Science and Technology of China. His Changchun,China,in2008,allincomputerscience.
mainresearchinterestsincludedatamining,knowl- He is currently a professor, the dean of the School
edge discovery, natural language processing and ofInformationScienceandInformationTechnology
intelligenttutoringsystems.Hewonthefirstprizein at Northeast Normal University, and the director
task2oftheNeurIPS2020EducationChallenge.He of the Key Laboratory of Intelligent Information
haspublishedpapersinreferredconferenceproceed- Processing in Jilin Province Colleges and Univer-
ings,suchasKDD2023,AAAI2022,SIGIR2022. sities. He also contributes as the Associate Editor
fortheIEEETransactionsonLearningTechnologies(TLT).Hehaspublished
|     |     |     |     |     |     |     |     | multiple papers | in   | prestigious   | journals | and conferences, |     | including   | Artificial |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ------------- | -------- | ---------------- | --- | ----------- | ---------- |
|     |     |     |     |     |     |     |     | Intelligence,   | IEEE | Transactions, | ACM      | Transactions,    |     | JAIR, AAAI, | IJCAI,     |
andWWW.Hisresearchinterestsincludeheuristicsearch,datamining,and
combinatorialoptimization.
|     |     | Qi  | Liu (Member, |     | IEEE) received |     | the Ph.D. | degree |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | --- | -------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
fromUniversityofScienceandTechnologyofChina
|     |     | (USTC),    | Hefei,      | China,        | in          | 2013. He   | is currently | a        |     |     |     |     |     |     |     |
| --- | --- | ---------- | ----------- | ------------- | ----------- | ---------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Professor  |             | in the School | of          | Computer   | Science      | and      |     |     |     |     |     |     |     |
|     |     | Technology |             | at USTC.      | His         | general    | area of      | research |     |     |     |     |     |     |     |
|     |     | is         | data mining | and           | intelligent | education. |              | He has   |     |     |     |     |     |     |     |
|     |     | published  |             | prolifically  | in refereed | journals   |              | and con- |     |     |     |     |     |     |     |
ferenceproceedings(e.g.,TKDE,TOIS,KDD).He
is an Associate Editor of IEEE TBD and Neuro- MinjuanWang(Member,IEEE)obtainedherB.A.
|     |     |            |     |        |               |     |      |         |     | in Chinese | literature |     | from the | Beijing/Peking | Uni- |
| --- | --- | ---------- | --- | ------ | ------------- | --- | ---- | ------- | --- | ---------- | ---------- | --- | -------- | -------------- | ---- |
|     |     | computing. |     | He was | the recipient | of  | KDD’ | 18 Best |     |            |            |     |          |                |      |
versityin1995,M.A.incomparativeliteraturefrom
StudentPaperAwardandICDM’11BestResearch
|     |     |     |     |     |     |     |     |     |     | Penn | State | University | in 1997, | and | Ph.D. in in- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ---------- | -------- | --- | ------------ |
PaperAward.HeisamemberoftheAlibabaDAMOAcademyYoungFellow.
HewasalsotherecipientofChinaOutstandingYouthScienceFoundationin formation science and learning technologies from
| 2019. |     |     |     |     |     |     |     |     |     | University | of        | Missouri-Columbia |                 | in  | 2001. She is |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------------- | --------------- | --- | ------------ |
|       |     |     |     |     |     |     |     |     |     | a newly    | appointed |                   | Chair Professor |     | of Emerging  |
TechnologiesandFutureEducationatTheEducation
|     |     |     |     |     |     |     |     |     |     | University | of  | Hong | Kong. | She has | also been a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ----- | ------- | ----------- |
professorandprogramchairofLearningdesignand
technologyatSanDiegoStateUniversity,California,
USAsince2000.Inaddition,sheservesastheEditor-in-ChieffortheIEEE
|     |     | Zhenya | Huang | (Member,IEEE)receivedtheB.E. |             |     |         |              |             |              |     |        |              |             |     |
| --- | --- | ------ | ----- | ---------------------------- | ----------- | --- | ------- | ------------ | ----------- | ------------ | --- | ------ | ------------ | ----------- | --- |
|     |     |        |       |                              |             |     |         | Transactions | on Learning | Technologies |     | (TLT). | Her research | specialties | are |
|     |     | degree | from  | Shandong                     | University, |     | in 2014 | and the      |             |              |     |        |              |             |     |
multidisciplinary,focusingonSTEMeducation,newandemergingtechnolo-
|     |     | Ph.D. | degree    | from       | USTC, | in 2020.   | He is       | currently       |             |           |           |     |               |     |               |
| --- | --- | ----- | --------- | ---------- | ----- | ---------- | ----------- | --------------- | ----------- | --------- | --------- | --- | ------------- | --- | ------------- |
|     |     |       |           |            |       |            |             | gies in various | educational | settings, | Metaverse |     | and immersive |     | learning, and |
|     |     | an    | associate | researcher | of    | the School | of Computer |                 |             |           |           |     |               |     |               |
ScienceandTechnology,UniversityofScienceand the design and implementation of artificial intelligence including AIGC for
|     |     |            |     |          |         |     |      | education | and training. | She | is an internationally |     | recognized | scholar | and has |
| --- | --- | ---------- | --- | -------- | ------- | --- | ---- | --------- | ------------- | --- | --------------------- | --- | ---------- | ------- | ------- |
|     |     | Technology |     | of China | (USTC). | His | main | research  |               |     |                       |     |            |         |         |
keynotedabout45internationalconferences.Sheisrecognizedinternationally
|     |     | interests | include | data | mining, | knowledge | discovery |     |     |     |     |     |     |     |     |
| --- | --- | --------- | ------- | ---- | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
forherresearch,publishinganddedicatedservicetoIEEEandotherscholarly
|     |     | representation |     | learning | and | intelligent | tutoring | sys- |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | -------- | --- | ----------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
communities.Dr.WangisamemberofIEEEandtheIEEEEducationSociety.
tems.Hehaspublishedmorethan30papersinref-
ereedjournalsandconferenceproceedingsincluding Shealsoco-chairstheEducationSociety’stechnicalcommitteeforimmersive
learning(TC-ILE).
TKDE,TOIS,KDD,AAAI.Hehasservedregularly
intheprogramcommitteesofanumberofconferences,andisreviewersfor
theleadingacademicjournals.
|     |     | Yonghe | Zheng | is  | the funding | dean | of  | Research |     |     |     |     |     |     |     |
| --- | --- | ------ | ----- | --- | ----------- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Institute of Science Education in Beijing Normal EnhongChen(Fellow,IEEE)receivedtheB.S.de-
University,ProfessorinEducationFacultyofBNU, greefromAnhuiUniversity,Hefei,China,theM.S.
PhDSupervisor.Prof.ZhengistheVicepresidentof
|     |     |     |     |     |     |     |     |     |     | degree | from | the Hefei | University | of  | Technology, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --------- | ---------- | --- | ----------- |
the8thCouncilofChinaAssociationofChildren’s
Hefei,China,andthePh.D.degreeincomputersci-
Science Instructors and is the member of Teach- encefromtheUniversityofScienceandTechnology
ing Guidance Committee of the Basic Education, ofChina(USTC),Hefei,China,in1989,1992and
the member of comprehensive group of the com- 1996 respectively. He is currently a Professor and
|     |     | pulsory | education |     | curriculum | revision | committee, |     |     |              |     |        |          |              |     |
| --- | --- | ------- | --------- | --- | ---------- | -------- | ---------- | --- | --- | ------------ | --- | ------ | -------- | ------------ | --- |
|     |     |         |           |     |            |          |            |     |     | theExecutive |     | Deanof | Schoolof | DataScience, | the |
thesciencecurriculumstandardrevisiongroup;the
|     |     |     |     |     |     |     |     |     |     | Director | of Anhui | Province | Key | Laboratory | of Big |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | ---------- | ------ |
GeneralSecretaryoftheAwardingSchemeCouncil Data Analysis and Application. He has published
for outstanding computer teachers in Universities; the Vice director of the a number of papers on refereed journals and con-
academic committee of Chinese society of Natural Science Museum; and ferences, such as TKDE, TIST, TMC, KDD, ICDM, NIPS and CIKM. His
| former Director | General | of  | the Science | Policy | Bureau | of  | National | Natural          |           |         |      |        |             |           |        |
| --------------- | ------- | --- | ----------- | ------ | ------ | --- | -------- | ---------------- | --------- | ------- | ---- | ------ | ----------- | --------- | ------ |
|                 |         |     |             |        |        |     |          | current research | interests | include | data | mining | and machine | learning, | social |
ScienceFoundationofChina.Prof.Zhenghasengagedinprojectmanagement
networkanalysis,andrecommendersystem.Dr.Chenwasarecipientofthe
of basic research and S&T policy research for a long time. More than 60 NationalScienceFundforDistinguishedYoungScholarsofChina,theBest
articles have been published. And Zheng is the chief editor of Disciplinary Application Paper Award on KDD-2008, the Best Student Paper Award on
andInterdisciplinaryScienceEducationResearchJournal.Prof.Zhengjoined KDD-2018(Research),andtheBestResearchPaperAwardonICDM-2011.
| in Educational | Faculty | of  | Normal | University | in April, | 2018, | with | specific |     |     |     |     |     |     |     |
| -------------- | ------- | --- | ------ | ---------- | --------- | ----- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
HeisanIEEEFellowandanACMDistinguishedScientist.
| research interests | on  | science      | education | and | educational | technology. |     | Prof.   |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | --------- | --- | ----------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| Zheng established  |     | the Research | Institute |     | of Science  | Education   | of  | Beijing |     |     |     |     |     |     |     |
NormalUniversityinNovemberof2019.