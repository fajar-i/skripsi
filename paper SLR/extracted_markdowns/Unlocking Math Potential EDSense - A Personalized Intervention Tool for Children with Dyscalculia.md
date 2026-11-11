2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
Unlocking Math Potential: EDSense - A
Personalized Intervention Tool for Children with
Dyscalculia
*
1st Dipti Jadhav 2nd Sarat Kumar Chettri 3rd Amiya Kumar Tripathy
Department of Computer Engineering Department of Computer Applications Department of Computer Engineering
Don Bosco Institute of Technology School of Technology, A.D.B.U. Don Bosco Institute of Technology
Mumbai, India Guwahati, India Mumbai, India
dipti@dbit.in sarat.chettri@dbuniversity.ac.in amiya@dbit.in
4thOm Ghate 5th Raj Chaudhari 6th Sarvesh Avhad
Department of Computer Engineering Department of Computer Engineering Department of Computer Engineering
Don Bosco Institute of Technology Don Bosco Institute of Technology Don Bosco Institute of Technology
Mumbai, India Mumbai, India Mumbai, India
omghate9@gmail.com chaudhariraj152002@gmail.com sarveshavhad03@gmail.com
Abstract—Math difficulties, such as dyscalculia, can hinder and their relationships, can hinder children’s ability to grasp
children’sabilitytoacquirestrongmathematicalproblem-solving mathematicalconceptsandperformcalculationsaccurately[1]
capabilities, limiting their potential for success. Early identifica-
[2].Additionally,neurobiologicaldisorderssuchasdyscalculia
tionandinterventionareessentialinaddressingthesechallenges.
or dyslexia can also impact the development of math skills
This research paper introduces EDSense, a specialized Bayesian
KnowledgeTracing(BKT)modeldevelopedformathskillassess- [3]Furthermore,ineffectiveteachingmethodsthatdonotcater
mentinchildrenwhomayhavedyscalculia.Thesystememploys to diverse learning needs can further hinder the development
a Directed Acyclic Graph (DAG) to represent the dependencies of math problem-solving capabilities in children [4].
between probabilities and incorporates the prior probability of
Toaddressthesechallenges,the’EDSense’Researchinitia-
mastery, slip rate, and guessing rate to update the student’s
tivehasbeendevelopedasaninnovativeeducationalinterven-
knowledge state. The case study findings revealed challenges in
math comprehension, multiplication, and symbol identification tiontoimprovethemathematicalproblem-solvingcapabilities
among children who may have dyscalculia, highlighting the ofchildrenabovetheageof6-10years.Theinitiativeemploys
need for targeted interventions and instructional strategies. The a dynamic intervention approach using a Dynamic Bayesian
personalized and data-driven approach of EDSense contributes
Network where Directed Acyclic Graphs (DAGs) are used
tothefieldofdyscalculiaintervention,providingapromisingtool
for math skill topologies based on the difficulty level of the
for math skill assessment in children who may have dyscalculia.
The development of EDSense has the potential to enhance early skills. By providing personalized feedback and tailored learn-
identification and intervention for children with dyscalculia, ing experiences that cater to individual students’ needs, the
leading to improved math outcomes and better support for initiative aims to enhance their problem-solving capabilities
students with this specific learning disorder.
[5]. Moreover, the initiative adopts a collaborative approach
Index Terms—Bayesian Knowledge Tracing, dyscalculia, per-
involving educators, parents, and educational institutions to
sonalized learning
create a supportive learning environment [2].
I. INTRODUCTION This work aims to explore the effectiveness of the ’ED-
Sense’ initiative in improving the mathematical problem-
Intoday’ssociety,theimportanceofmathematicalproblem-
solving capabilities of children. Previous studies have shown
solving skills cannot be overstated. According to the Na-
that targeted interventions that cater to individual learning
tional Research Council (2001), these skills are crucial for
needscansignificantlyimprovemathskills[6].Therefore,this
success in academia and are vital in various fields, including
paper will evaluate the effectiveness of the ’EDSense’ initia-
science, engineering, and technology. However, some chil-
tive in addressing math difficulties such as insufficient num-
dren face challenges in developing strong math skills due
ber sense, neurobiological disorders, and ineffective teaching
to various factors. For example, insufficient number sense,
methods.Thepaperwillalsodiscussthepotentialimplications
which refers to the foundational understanding of numbers
of this research for educational institutions, educators, and
parents, and highlight the significance of early intervention
979-8-3503-4834-7/23/$31.00 ©2023 IEEE

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
in addressing math difficulties in children. interventions aimed at enhancing early mathematics develop-
In conclusion, the ’EDSense’ initiative provides a promis- ment. Zhang et al [15]. conducted a comprehensive review
ing avenue for enhancing the problem-solving capabilities of of the literature on number sense, while Patel and Groenke
children facing math difficulties. This research can contribute discussed interventions for improving mathematical cognition
to the development of effective educational interventions that and learning [16]. Parental involvement has been found to
cater to diverse learning needs and promote the acquisition play a significant role in children’s development of number
of strong mathematical problem-solving capabilities among sense. LeFevre and Berrigan [17] investigated the relationship
children. between parental involvement and children’s number sense
skills. The findings suggested that parental involvement, such
II. RELATEDWORK
as engaging in counting activities, playing number games,
Several studies have been conducted to investigate the and providing math-related materials at home, can positively
mathematical abilities and challenges faced by students with impact children’s development of number sense skills.
dyscalculia, as well as interventions aimed at improving early Severalstudieshavefocusedonwhole-schoolapproachesto
number sense skills in preschool and kindergarten children. developingearlynumbersenseinstudents.Torgesenetal.[18]
Jeya, S., Albina, A. (2019) conducted a study titled ”A Study described a whole-school approach that includes assessment,
of Students with Dyscalculia and their Mathematical Abilities targeted intervention, and professional development for teach-
atPrimarySchoolsinKaraikudi”inTamilNadu,India,which ers. The approach emphasized the importance of integrating
found that many students in the Karaikudi region struggled number sense development into the curriculum and providing
with mathematical concepts and a significant number of them ongoing support for teachers to effectively teach number
had dyscalculia [7]. The study utilized a survey, diagnostic sense skills to students. West et al. [19] explored the use of
testing, and comparison of the mathematical abilities of stu- visual representations, such as number lines, ten frames, and
dentswithandwithoutdyscalculiaasaresearchmethodology. manipulatives, to develop number sense in elementary school
Qi Liu et al. (2019) proposed in a research paper titled students. The results suggested that visual representations can
”ExploitingCognitiveStructureforAdaptiveLearning”which be an effective tool for promoting students’ understanding of
explored the use of the cognitive structure as a tool for numbers and their relationships.
creating adaptive learning systems. The authors argued that The relationship between number sense and mathematics
understanding a learner’s cognitive structure, knowledge, and achievement over time has also been investigated. Schneider
understanding of a given subject, can help tailor instruction et al. [20] [21] conducted longitudinal studies examining the
to suit individual needs. The paper presented a theoretical development of number sense and its relationship to math-
framework and a prototype system incorporating cognitive ematics achievement. The findings consistently showed that
structure for adaptive learning, suggesting potential for sig- strong number sense skills in early childhood are predictive
nificant improvement in adaptive learning systems [8] oflatermathematicsachievement.Thesefindingshighlightthe
Lijin Zhang et al. (2016) focused on early screening and importanceofearlynumbersensedevelopmentasafoundation
dynamic intervention for children with insufficient number for future mathematics learning.
sense,aimingtoimprovemath-solvingcapabilitiesinchildren Interventions aimed at improving number sense skills have
above10yearsofagewhofacedifficultieswithmath.There- been studied extensively. Mix et al. [22] discussed the im-
searchaimedtoenhancenumbersense,theabilitytoreadand portance of early mathematics education and the role of
understand numbers and perform mathematical calculations, developmental psychology in improving instruction. They
particularly in children with dyscalculia [9]. provided recommendations for developing number sense in
There have also been several studies examining effective young children, including the use of concrete manipulatives,
teachingstrategiesandinterventionsfordevelopingearlynum- real-world contexts, and engaging activities. Fuchs et al. [23]
ber sense skills in preschool and kindergarten children. For conducted a review of research on mathematics interventions
example,ClementsandSarama[10]providedacomprehensive for struggling students, including those with disabilities, and
review of the literature on early mathematics education and highlighted the significance of number sense development in
discussed the importance of developing early number sense these interventions.
and effective teaching strategies. Hoffer and Schmitt [11] Several studies have specifically investigated the effective-
presented a conceptual framework for a professional develop- ness of interventions aimed at developing early number sense
ment program targeting early number sense in preschoolers. in low-income or low-SES (socioeconomic status) students.
Vandermaas-Peeleretal.[12]conductedasystematicreviewof Jordan et al. [24] conducted a study on the effectiveness of a
intervention studies aimed at developing early number sense comprehensivenumeracyprogramforlow-SESkindergartners
in preschool children, providing insights into various inter- and found that the program led to significant improvements
vention strategies and recommendations for future research. in number sense skills. Jordan et al. [25] also conducted
Various studies have examined the importance of number a systematic review of interventions aimed at developing
sense in mathematics achievement, with Purpura et al. and early mathematics, including number sense, and discussed
Noe¨l et al [13] [14]. highlighting its significance in early the effectiveness of various intervention strategies. Abreu-
childhood. Jordan and Levine provided recommendations for Mendoza et al. [26] examined the early number sense skills

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
of preschoolers and provided guidance on effective teaching importance of early number sense development and providing
strategies, emphasizing the importance of early number sense practical guidance on effective teaching strategies. This work
development in this age group. canbeavaluableresourceforeducatorsandparentsinterested
Meta-analyses have been conducted to examine the overall inpromotingearlymathematicalskillsinyoungchildren.Kim
effectiveness of interventions aimed at developing number et al. [32] investigated the influence of instructional methods
sense skills. Kim et al. [27] conducted a meta-analysis ex- on young children’s early number sense development, pro-
amining the effectiveness of instructional strategies on the viding insights into effective instructional approaches. Their
development of early number sense and provided recommen- findings can inform educators and practitioners on evidence-
dations for effective teaching strategies. Schneider et al. [21] based instructional strategies for promoting early number
also conducted a meta-analysis examining the effectiveness of sense skills in young children.
numbersenseinterventionsandprovidedrecommendationsfor In summary, the related work reviewed in this paragraph
effective intervention strategies. encompasses a range of studies highlighting the importance
Other aspects related to number sense development have ofearlynumbersensedevelopmentinmathematicseducation.
also been studied. The role of executive functions, such as These studies provide insights into the effectiveness of vari-
working memory and cognitive flexibility, in early number ous intervention strategies, offer recommendations for future
sense development, has been investigated. St Clair-Thompson research, and provide evidence-based guidance on effective
and Gathercole [28] examines the role of executive functions teaching strategies. It is found that these studies significantly
in early number sense development and provide guidance contribute to our understanding of the development of early
on effective teaching strategies. Jordan et al. [25] conducted mathematical skills in young children and provide valuable
a systematic review of interventions aimed at developing insights into how educators and practitioners can support
early mathematics skills, providing valuable insights into the their growth, particularly in terms of fostering number sense
effectiveness of various intervention strategies. The authors abilities. Participants were given instructions on navigating
discussed the importance of early mathematics development Smartick and completing math exercises. The assessment
and provided recommendations for future research in this includedmathtaskstargetingprimarymathskills,andchildren
area. Abreu-Mendoza et al. [26] focused on preschoolers’ completed these tasks to the best of their abilities within a
early number sense skills and emphasized the significance of specified time period.
early number sense development. They provided guidance on
effective teaching strategies that can promote early number
III. PROPOSEDMETHODOLOGY
senseskillsinyoungchildren,contributingtotheliteratureon Atotalof137participantsaged6-10years,whohadaccess
early mathematics education. to a personal computer (PC) and an internet connection,
Vasilyeva et al. [29] investigated the relationship between were recruited from local schools in Mumbai to participate
number sense and mathematics achievement in early elemen- in this case study. The Smartick online math learning plat-
tary school children. Their findings highlighted the strong form [33] was utilized as the assessment tool in this study.
association between number sense skills and mathematics It offers personalized math lessons and exercises and em-
achievement, underscoring the importance of early number ploys adaptive technology to customize the math curriculum
sense development for later mathematics success. Symes et according to the individualized level and pace of learning
al. [30] conducted a systematic review of mathematics inter- of each child. The platform provides an engaging audio-
ventionsforchildrenwithspecialeducationalneeds,shedding visual interface for interactive assessments, covering primary
light on the effectiveness of different intervention strategies. math skills such as Dot Comparison, Subitizing, Number
Their recommendations for future research in this area can Comparison, Mental Number Line, Number Line, Counting,
inform practitioners and researchers working with children Addition,Subtraction,andMultiplication.Datacollectedfrom
with special educational needs. the Smartick assessments, including performance measures
Clements et al. [10] presented learning trajectories for such as accuracy, speed, and completion time, were recorded
young children in mathematics education, emphasizing the andanalyzedusingdescriptivestatistics.Thisanalysisallowed
significance of early number sense development. Their work for the identification of patterns or trends in the children’s
provided valuable guidance on effective teaching strategies math skills. The data were also used in selecting samples
that can foster early number sense skills in young children, for testing the proposed prototype. Following analysis of
servingasaresourceforeducatorsandpractitioners.Laskiand Smartick assessment results and observations, an EDSense
Yu[31]examinedthedevelopmentofearlymathematicalcog- prototype was designed for the proposed intervention. The
nition, including number sense and operations, and provided prototype was tested with dyscalculia specialists, including
evidence-based guidance on effective teaching strategies. This math educators, psychologists, and researchers. Expert feed-
contributestotheunderstandingofhowyoungchildrenacquire backwasincorporatedintorefiningtheprototypetoalignwith
early mathematical skills and how educators can support their bestpracticesandcurrentresearchindyscalculiaintervention.
development. EDSenseisaspecializedBayesianKnowledgeTracing(BKT)
Baratta-Lorton [9] provided a comprehensive approach to modeldesignedtoanalyzeassessmentdata,includingaccurate
developing number sense in early childhood, discussing the answers, incorrect answers, and specific types of incorrect

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
| answers          | commonly | made    | by           | students  | with            | dyscalculia. |           | The |     |     |     |     |     |     |
| ---------------- | -------- | ------- | ------------ | --------- | --------------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| model is         | tailored | to      | track        | and model | students’       |              | knowledge |     |     |     |     |     |     |     |
| and performance, |          | taking  | into         | account   | the             | specific     | mistakes  |     |     |     |     |     |     |     |
| they may         | make     | related | to addition, |           | multiplication, |              | carrying  |     |     |     |     |     |     |     |
digits,vanishingdigits,individualdigitaddition,andthe”zero
| makes zero” | concept. |         | This allows |     | for personalized |       | feedback    |     |     |     |     |     |     |     |
| ----------- | -------- | ------- | ----------- | --- | ---------------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| and support | to       | address | the unique  |     | learning         | needs | of students |     |     |     |     |     |     |     |
with dyscalculia.
| The Bayesian |               | Knowledge      |           | Tracing      | (BKT) | model               | used          | in      |     |     |     |     |     |     |
| ------------ | ------------- | -------------- | --------- | ------------ | ----- | ------------------- | ------------- | ------- | --- | --- | --- | --- | --- | --- |
| EDSense      | updates       | the            | student’s | knowledge    |       | state               | based         | on the  |     |     |     |     |     |     |
| probability  | of            | mastery,       | which     | is inferred  |       | from                | the student’s |         |     |     |     |     |     |     |
| responses    | to questions. |                | The       | model        | uses  | a directed          | acyclic       |         |     |     |     |     |     |     |
| graph (DAG)  | to            | represent      | the       | dependencies |       | between             | probabil-     |         |     |     |     |     |     |     |
| ities. For   | skills        | like Addition, |           | Subtraction, |       | and Multiplication, |               |         |     |     |     |     |     |     |
| separate     | DAGs          | are created.   | The       | DAG          | for   | Addition            | and           | Sub-    |     |     |     |     |     |     |
| traction     | includes      | 16 micro       | levels,   | ranging      |       | from simple         |               | 1-digit |     |     |     |     |     |     |
additiontocomplex3-digitadditionwithcarry.Theobservable
nodesintheDAGarethestudent’sresponses,whilethehidden
Fig.1. EDSenseSystemArchitecture
| nodes represent |      | the student’s |                   | inferred | knowledge |          | states. | The |     |     |     |     |     |     |
| --------------- | ---- | ------------- | ----------------- | -------- | --------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| DAG starts      | with | the           | prior probability |          | of        | mastery, | which   | is  |     |     |     |     |     |     |
updated using learning rate and guessing rate. The slip rate is generation module in Node.js is implemented for analyzing
alsoupdated,andfinally,theposteriorprobabilityiscomputed answersandgeneratingreports,andaPythonscriptisutilized
based on the updated prior probability and slip rate. Bayesian forretrievingquestionsfromSQLServerifneeded.Thisarchi-
Knowledge Tracing (BKT) is a statistical method used in tectureenablesseamlessinteractionbetweentheuserinterface,
|             |      |        |      |        |             |     |           | server-side | components, |     | and the database, | facilitating | efficient |     |
| ----------- | ---- | ------ | ---- | ------ | ----------- | --- | --------- | ----------- | ----------- | --- | ----------------- | ------------ | --------- | --- |
| educational | data | mining | that | models | a student’s |     | knowledge |             |             |     |                   |              |           |     |
or skill state while interacting with an educational system assessment and reporting of math skills for the participants.
usingBayesianprobabilities.TheBKTmodelconsistsofthree
IV. RESULTANDDISCUSSIONS
| probabilities: |     | The prior | probability |     | of mastery |     | (P(m)): | This |     |     |     |     |     |     |
| -------------- | --- | --------- | ----------- | --- | ---------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
representstheprobabilitythatthestudenthasalreadymastered When comparing the written and audio-visual assessments
the skill before interacting with the system. It is typically set for dyscalculia, several key factors come into play. The
to a low value, such as 0.1, to reflect that most students do written assessment predominantly relies on reading compre-
not start with full mastery [34]. hension and requires the child to translate problems into
Prior probability of mastery (P(m)) based on correct an- written formats, perform mental calculations, and provide
swers: written solutions. In contrast, the audio-visual assessment
P(m)=P(m)+(1−P(m))∗P(l) (1) combines auditory and visual modalities, presenting instruc-
|           |        |       |             |       |          |     |     | tions verbally |          | while displaying | relevant  | information |             | on the |
| --------- | ------ | ----- | ----------- | ----- | -------- | --- | --- | -------------- | -------- | ---------------- | --------- | ----------- | ----------- | ------ |
| Slip rate | (P(s)) | based | on specific | wrong | answers: |     |     |                |          |                  |           |             |             |        |
|           |        |       |             |       |          |     |     | screen. This   | approach | allows           | the child | to process  | information |        |
P(s)=P(s)+(1−P(s))∗P(g) (2) through both modalities simultaneously and refer back to
|           |             |     |            |        |       |     |         | visual cues   | during | calculations. | While      | the written | assessment |     |
| --------- | ----------- | --- | ---------- | ------ | ----- | --- | ------- | ------------- | ------ | ------------- | ---------- | ----------- | ---------- | --- |
| Posterior | probability |     | of mastery | (P(p)) | based | on  | correct | an-           |        |               |            |             |            |     |
|           |             |     |            |        |       |     |         | places higher |        | demands       | on reading | and written | skills,    | the |
swers:
|     |     |                       |     |     |     |     |     | audio-visual | assessment |         | offers a more | immediate | response     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --- | ------------ | ---------- | ------- | ------------- | --------- | ------------ | --- |
|     |     | P(p)=P(m)/(P(m)+P(s)) |     |     |     |     |     | (3)          |            |         |               |           |              |     |
|     |     |                       |     |     |     |     |     | and engages  | multiple   | senses, | potentially   | catering  | to different |     |
Where P(m) represents the prior probability of mastery, learning strengths and preferences. Considering the specific
P(l) represents the learning rate, P(s) represents the slip rate, needs and abilities of each child is crucial in selecting the
and P(g) represents the guessing rate. These equations can mostappropriateassessmentmethodorutilizingacombination
be used to update the probabilities in the BKT model for to provide a comprehensive evaluation of dyscalculia. The
analyzing student performance data in the context of math audio-visual Smartick tool, with its combination of auditory
skill assessment. instructions and visual cues, is an ideal choice for dyscalculia
The proposed system architecture shown in Fig.1 for the assessment due to its ability to engage multiple senses and
math skill assessment includes a front-end built with React.js provide immediate feedback. Therefore, Smartick is selected
for the user interface, a back-end powered by Node.js and as the preferred tool for assessing dyscalculia.
Express.js for handling requests and responses, and a MySQL The case study employed the Smartick online math learn-
database for storing assessment data. The system also incor- ing platform as the assessment tool for a sample of 137
porates a question generation module using Express.js and participants aged 6-10 years, who had access to a personal
MySQLfordynamicquestionselectionbasedontheposterior computer and internet connection. The findings indicated that
probability calculated as per the proposed method. A report students in standard 4 exhibited challenges in comprehending

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
Fig.4. MathSkillsPerformance:AccuracyResultsfromSmartickAssessment
Fig.2. Dyscalculiatestperformance
Fig.3. MathSkillsPerformance:SpeedResultsfromSmartickAssessment
Fig.5. EDsenseInterfaceforAdditionwithCarrySkillPractice
math terms and mastering multiplication, while students in
standard 3 relied on finger counting but demonstrated rel- port and intervention may be required. Fig 4. displays the
atively higher overall performance. Students in standard 2 accuracy rates of children across all 11 skills included in the
encountered difficulties in identifying mathematical symbols dyscalculia test. The figure highlights that children performed
and comprehending instructions. These findings emphasize relatively well in most of the skills, with high accuracy rates
the need for targeted interventions and instructional strategies observed in tasks such as counting, addition, and subtraction.
tailored to each standard’s specific math skill challenges. However, there is room for improvement in some areas such
Thecasestudyobservedthatchildrentakingthedyscalculia as number comparison, number sequence, and multiplication.
testhaddifficultyusingthemouseanddragginganddropping These findings provide valuable insights into the areas that
objects on the interface, which resulted in reduced speed. require more attention and support to enhance mathematical
Theseobservationshighlighttheimportanceofconsideringthe learning and performance in children.
usabilityandaccessibilityoftechnology-basedassessmentsfor Fig 5. depicts the proposed interface for practicing the skill
children, especially those with learning difficulties. of addition with carry in the EDsense platform. The interface
Fig 2. depicts the results of the dyscalculia test assessment, includes three columns representing the hundreds, tens, and
which included 11 tasks evaluating three key areas of math- one’s places. Each column contains different objects to rep-
ematical learning: comparison and recognition of quantities, resent the corresponding place value, such as watermelons,
Arabic numbers and numbering, and arithmetic, broken down grapes, and apples. The interface also includes a prompt for
by grade level. Fig 3. presents the distribution of speed for the Addition problem to be solved and a box for entering the
solving skills in the dyscalculia test, categorized into five lev- solution. Using different objects for each place value aims to
els: Very Slow, Slow, Average, Very Fast, and Not Attempted. avoid confusion and help children with insufficient number
The speed is measured in seconds, and the graph shows the sense better understand and visualize the concept of carrying
percentageofchildrenwhofellintoeachcategory.Theresults in Addition. Additionally, the interface allows children to
indicate that a majority of the children fell into the Very Slow manipulatetheobjectsbydragginganddroppingthemintothe
speed category, with a smaller percentage in the Very Fast corresponding columns, promoting a hands-on and interactive
and Average categories and a few children did not attempt learning experience. The use of bright and colorful graphics
the task. The distribution of speed across these categories is intended to engage children’s attention and facilitate their
provides valuable insights into the performance of children learning.Overall,theEDsenseinterfaceforadditionwithcarry
in the dyscalculia test, highlighting areas where further sup- skill practice offers a visually appealing and effective tool for

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
children to improve their understanding and mastery of this [8] Q. Liu, S. Tong, C. Liu, H. Zhao, E. Chen, H. Ma, and S. Wang,
essential mathematical skill. “Exploiting cognitive structure for adaptive learning,” in Proceedings
of the 25th ACM SIGKDD International Conference on Knowledge
V. CONCLUSION Discovery&DataMining,pp.627–635,2019.
[9] M. Baratta-Lorton, Teaching Early Math: A Comprehensive Approach
In conclusion, this research paper presents the develop- toDevelopingNumberSense. 2016.
ment of EDSense, a specialized Bayesian Knowledge Tracing [10] D.H.ClementsandJ.Sarama,EarlyChildhoodMathematicsEducation
Research:LearningTrajectoriesforYoungChildren. Routledge,2017.
(BKT) model for math skill assessment in children with
[11] A.HofferandS.A.Schmitt,“Buildingearlynumbersenseinpreschool-
dyscalculia. Through the assessment of 137 participants aged ers:Aconceptualframeworkforaprofessionaldevelopmentprogram,”
6-10 years using the Smartick online math learning platform, EarlyChildhoodEducationJournal,vol.44,no.6,pp.567–576,2016.
[12] M. Vandermaas-Peeler, K. E. Nelson, and M. W. Fuhs, “Developing
data on accuracy, speed, and completion time were collected
early number sense in preschool children: A systematic review of
andanalyzedusingdescriptivestatistics.Basedontheanalysis, intervention studies,” Review of Educational Research, vol. 88, no. 5,
an EDSense prototype was designed and tested with experts pp.783–827,2018.
[13] D. J. Purpura and J. A. Logan, “Number sense and mathematics
in dyscalculia.
achievement in kindergarten,” Journal of Experimental Child Psychol-
EDSense utilizes a directed acyclic graph (DAG) to repre- ogy,vol.153,pp.15–34,2017.
sent the dependencies between probabilities and incorporates [14] M.-P.Noe¨l,L.Rousselle,andC.Mussolin,“Exploringtherelationship
between working memory and early number sense development,” De-
prior probability of mastery, slip rate, and guessing rate to
velopmentalPsychology,vol.53,no.7,pp.1230–1243,2017.
updatethestudent’sknowledgestate.Thesystemalsoincludes [15] D. Zhang, Y. Ding, J. Li, and X. Wu, “The role of number sense in
a question selection module based on student performance, mathematicallearning,”EducationalPsychologyReview,vol.31,no.4,
pp.759–788,2019.
includingcorrectanswers,wronganswers,andspecificwrong
[16] S. S. Patel and S. L. Groenke, eds., Mathematical Cognition and
answersthatindicatecommonmistakesmadebystudentswith Learning:InfusingResearchintoPractice.InformationAgePublishing,
dyscalculia. 2018.
[17] J.-A. LeFevre and L. Berrigan, “The role of parental involvement
The findings from the case study highlight challenges in
in children’s development of number sense,” Early Education and
mathcomprehension,multiplication,andsymbolidentification Development,vol.26,no.3,pp.378–399,2015.
among children with dyscalculia, underscoring the need for [18] J. K. Torgesen, Y. Petscher, and E. A. Patall, “Developing early num-
ber sense: A whole-school approach,” Teaching Exceptional Children,
targeted interventions and instructional strategies. EDSense,
vol.47,no.5,pp.261–269,2015.
with its personalized and data-driven approach, presents a [19] R. West and J. Torgesen, “Developing number sense through the
promising tool for math skill assessment in children with useofvisualrepresentationsinelementarymathematics,”Mathematics
EducationResearchJournal,vol.30,no.3,pp.307–329,2018.
dyscalculia, contributing to the field of dyscalculia interven-
[20] M. Schneider, T. M. Beasley, A. L. Boudreaux, and M. B. Calhoon,
tion. “Thedevelopmentofnumbersenseanditsrelationshiptomathematics
Further research and development of EDSense could have achievement,” Journal of Experimental Child Psychology, vol. 149,
pp.50–65,2016.
significant implications for identifying and addressing math
[21] M. Schneider, K. Beeres, L. Coban, S. Merz, S. Susan Schmidt,
difficulties in children with dyscalculia, ultimately improving J. Stricker, and B. De Smedt, “A comprehensive meta-analysis of the
their math skills and academic outcomes. EDSense has the number sense intervention literature,” Educational Research Review,
vol.18,pp.40–58,2016.
potentialtobeintegratedintoeducationalsettingsasavaluable
[22] K. S. Mix and A. L. Bunter, Improving Elementary Mathematics
toolforeducatorsandpractitionersworkingwithchildrenwith Education:InsightsfromDevelopmentalPsychology. Routledge,2016.
dyscalculia, aiding in the development of effective interven- [23] L.S.Fuchs,D.Fuchs,S.R.Powell,andP.M.Seethaler,“Mathematics
interventions for struggling students with and without disabilities,”
tions and instructional strategies tailored to the unique needs
ExceptionalChildren,vol.82,no.4,pp.443–462,2015.
of these students. [24] N. C. Jordan, J. Huttenlocher, and S. C. Levine, “A comprehensive
numeracyprogramforlow-seskindergartners:Effectsonnumbersense,”
REFERENCES JournalofEducationalPsychology,vol.111,no.2,pp.224–241,2019.
[25] N. C. Jordan, J. Glutting, C. Ramineni, and M. W. Watkins, “Inter-
[1] B.Butterworth,“Thedevelopmentofarithmeticalabilities,”Journalof ventions to develop early mathematics: A systematic review of the
childpsychologyandpsychiatry,vol.46,no.1,pp.3–18,2005. literature,”EarlyChildhoodResearchQuarterly,vol.45,pp.1–16,2018.
[2] AMERICAN, “Dsm v: diagnostic and statistical manual of mental [26] R.A.Abreu-Mendoza,R.A.Arteaga-Va´zquez,andR.A.Arias-Garc´ıa,
disorders,”2013. “Investigating the early number sense skills of preschoolers: A cross-
[3] AMERICAN, “Dsm v: diagnostic and statistical manual of mental sectional study,” Early Childhood Education Journal, vol. 45, no. 3,
disorders,”2013. pp.327–335,2017.
[4] B.Walker,M.E.Shippen,P.Alberto,D.E.Houchins,andD.F.Cihak, [27] J. S. Kim, P. Griffin, S. R. Patton, J. Sarama, and D. H. Clements,
“Usingtheexpressivewritingprogramtoimprovethewritingskillsof “A meta-analysis of the effectiveness of instructional strategies on
high school students with learning disabilities,” Learning Disabilities the development of early number sense,” Early Childhood Research
Research&Practice,vol.20,no.3,pp.175–183,2005. Quarterly,vol.45,pp.1–17,2018.
[5] A.-O. deManizales, J. A. A.-G. COVID, S. Orozco-Arias, D. Arias- [28] H.L.StClair-ThompsonandS.E.Gathercole,“Theroleofexecutive
Garzo´n, L. H. Lo´pez-Murillo, M. de la Iglesia Vaya´, F. Buitrago- functionsinthedevelopmentofearlynumbersense,”CognitiveDevel-
Carmona, J. P. Villa-Pulgar´ın, R. Tabares-Soto, and E. Mercado-Ruiz, opment,vol.39,pp.29–40,2016.
“to deep learninguniversidad appliedsonia tecnolo´gicah. contreras-ortiz [29] M.Vasilyeva,E.V.Laski,andS.A.Petrill,“Therelationshipbetween
debol´ıvar,”AIApplicationsforDiseaseDiagnosisandTreatment,p.202, numbersenseandmathematicsachievementinearlyelementaryschool,”
2022. JournalofExperimentalChildPsychology,vol.166,pp.500–515,2018.
[6] D. C. Geary, “Early foundations for mathematics learning and their [30] W. Symes, T. P. Carpenter, and W. Tate, “Mathematics interventions
relations to learning disabilities,” Current directions in psychological for children with special educational needs: A systematic review,”
science,vol.22,no.1,pp.23–27,2013. EducationalPsychologyReview,vol.30,no.2,pp.477–509,2018.
[7] G. Rehill, “Building a strong foundation in mathematics,” Year 9 [31] E. V. Laski and Q. Yu, “The development of early mathematical
InteractiveMaths,2010. cognition: Number and operation,” Wiley Interdisciplinary Reviews:
CognitiveScience,vol.8,no.3,p.e1435,2017.

2023 International Conference on Advanced Computing Technologies and Applications (ICACTA)
[32] J.Y.Kim,D.H.Clements,andJ.Sarama,“Theinfluenceofinstructional [34] Z.A.PardosandN.T.Heffernan,“Kt-idem:Introducingitemdifficulty
method on young children’s early number sense development,” Early to the knowledge tracing model,” in User Modeling, Adaption and
ChildhoodResearchQuarterly,vol.39,pp.1–14,2017. Personalization: 19th International Conference, UMAP 2011, Girona,
[33] Smartick, “Smartick dyscalculia assessment tool.” Spain,July11-15,2011.Proceedings19,pp.243–254,Springer,2011.
https://www.smartick.com/dyscalculia-assessment/,2009.