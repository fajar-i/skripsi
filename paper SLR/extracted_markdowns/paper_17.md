5202
nuJ
12
]YC.sc[
1v77571.6052:viXra
Optimizing Mastery Learning by Fast-Forwarding
Over-Practice Steps
Meng Xia1*[0000−0002−2676−9032], Robin Schmucker2*[0000−0002−5275−3608],
Conrad Borchers2*[0000−0003−3437−8979], and Vincent
Aleven2[0000−0002−1581−6657]
1 Texas A&M University
mengxia@tamu.edu
2 Carnegie Mellon University
{rschmuck,cborcher,aleven}@cs.cmu.edu
*Equal contribution.
Abstract. Masterylearningimproveslearningproficiencyandefficiency.
However,theoverpracticeofskills–studentsspendingtimeonskillsthey
havealreadymastered–remainsafundamentalchallengefortutoringsys-
tems. Previous research has reduced overpractice through the develop-
mentofbetterproblemselectionalgorithmsandtheauthoringoffocused
practicetasks.However,feweffortshaveconcentratedonreducingover-
practicethroughstep-leveladaptivity,whichcanavoidresource-intensive
curriculum redesign. We propose and evaluate Fast-Forwarding as a
technique that enhances existing problem selection algorithms. Based
on simulation studies informed by learner models and problem-solving
pathways derived from real student data, Fast-Forwarding can reduce
overpractice by up to one-third, as it does not require students to com-
pleteproblem-solvingstepsifallremainingpathwaysarefullymastered.
Fast-Forwarding is a flexible method that enhances any problem selec-
tion algorithm, though its effectiveness is highest for algorithms that
preferentially select difficult problems. Therefore, our findings suggest
thatwhileFast-Forwardingmayimprovestudentpracticeefficiency,the
size of its practical impact may also depend on students’ ability to stay
motivated and engaged at higher levels of difficulty.
Keywords: mastery learning, knowledge tracing, problem selection, intelligent
tutoring systems, data-driven optimization
1 Introduction
The field of technology-enhanced learning has successfully optimized problem
selection strategies and improved learning efficiency through methods such as
Bayesian Knowledge Tracing (BKT) [8]. BKT, one the most widely used knowl-
edge tracing algorithms, has proven effective in modeling student knowledge ac-
quisition, enabling tutoring systems to adaptively select practice problems with
relevant and adequately difficult skills. In addition, several extensions to BKT

2 M. Xia et al.
Fig.1: Fast-Forwarding reduces overpractice by avoiding problem-solving paths
students have fully mastered. Linear equation-solving steps in gray are known
tobemasteredbythestudentandcanbefast-forwardedtoreduceoverpractice.
have been proposed, including deep learning- (e.g., [26,33] and regression-based
approaches such as AFM, PFA and AugmentedLR (e.g., [25,29]).
Adaptiveproblemselectorsareinformedbyknowledgetracingandgrounded
in mastery learning [4]. Mastery learning assumes that learning and instruction
canbedividedintoatomicskillsthatstudentsacquirebyexercisingdistinctcog-
nitive operations and receiving feedback from which they learn. This idea aligns
with large-scale evidence from several datasets [15] and has improved student
performance at scale [27]. Mastery learning underlies the design of many con-
temporary tutoring systems and the idea that students require several practice
repetitions–learningopportunities–tomastereachskill.Onaverage,theyrequire
seven[15].However,whentasksor activitysequencesarepoorlydesigned,prac-
tice activities might lead to overpractice and underpractice of individual skills.
Overpractice occurs when students practice skills they have already mas-
tered, which is undesirable for learning efficiency if students have not yet mas-
teredotherskills[7].Overpracticetypicallyoccurswhenstudentspracticestatic
problem sets where problems include multiple skills, and there is little variabil-
ity in what skills the problems target. In contrast, underpractice can be due to
limited problem pools, meaning students do not master content upon complet-
ingaproblemsetorhaveinsufficienttimetopractice.Whilecurricularredesign
based on learning analytics has been suggested as one method to mitigate over-
and underpractice [7], avoiding both remains a fundamental challenge in adap-
tive learning, with learning analytics frameworks on the data-driven redesign
of adaptive learning systems considering problem selection a core dimension for
design improvement [12]. In particular, the consequences of reducing overprac-
tice on learning are known to be positive: empirical research has shown that
reducingoverpracticeinCognitiveTutorgeometrydecreasedpracticetimewith-
out impacting learning outcomes [7], and such reductions have thus far required
a careful and labor-intensive curricular redesign. In the present study, we study
whether overpractice can be reduced through more automated means, based on
optimization of step-level adaptivity (“inner loop” [3]) and having the system
takeoverthemasteredstepsundersomeconditions.Suchoptimizationbalances
the allocation of repetitions, giving students time to master challenging skills.

|            |     |              | Optimizing |     | Mastery | Learning | by Fast-Forwarding |         |          | 3   |
| ---------- | --- | ------------ | ---------- | --- | ------- | -------- | ------------------ | ------- | -------- | --- |
| One reason | why | overpractice |            | is  | an open | problem  | is that            | serving | practice |     |
problems with a single skill is not a viable solution, as multi-step problems give
learners important opportunities to learn, most notably when practicing two
skills together is more challenging than practicing them in isolation [10]. Hence,
itisimportanttodevelopnovelwaysforstudentstomastertheskillsrequiredto
learn while optimizing practice time and retaining multi-step problem solving.
| An emerging |     | approach | to  | improve | adaptive | problem | selection |     | efficiency | is  |
| ----------- | --- | -------- | --- | ------- | -------- | ------- | --------- | --- | ---------- | --- |
called focused practice. This approach involves isolating specific skills that the
learnercurrentlylacks.Recentproblemselectionalgorithmsconsidertheoverall
redundancy in mastery of knowledge and the degree of isolation of unmastered
skills in problem selection [11]. However, this approach still necessitates the
availability of a diverse pool of problems with sufficient breadth and variation
in skill density. Additionally, the requirement of designing focused tasks that
exercisealimitednumberofskillsnecessitatesadditionalcontentauthoringtime.
| Can a | general-purpose, |     | problem | pool | agnostic, | and | selector | agnostic | method |     |
| ----- | ---------------- | --- | ------- | ---- | --------- | --- | -------- | -------- | ------ | --- |
forfocusedpracticeincreasestudentlearningefficiencyasmeasuredinoverprac-
tice? We propose Fast-Forwarding (Fig. 1), which allows learners to complete
multi-step problems up to the point where all remaining problem-solving steps
are mastered, thereby contributing only to overpractice. Compared to prior ap-
proaches to focused practice [12,7], Fast-Forwarding neither requires a spe-
cific problem selection mechanism nor depends on curricular redesign
whileretainingmulti-stepproblemsolving.WequantifytheeffectivenessofFast-
Forwarding across various contemporary problem selection algorithms in intelli-
| gent tutoring   | systems  | through     |              | simulation | studies.    | We         | ask:         |          |          |       |
| --------------- | -------- | ----------- | ------------ | ---------- | ----------- | ---------- | ------------ | -------- | -------- | ----- |
| RQ1:            | How does | learning    | efficiency   |            | as measured | in         | overpractice |          | benefit  | from  |
| Fast-Forwarding |          | in          | a mastery    | problem    | selector    | given      | limited      | practice |          | time? |
| RQ2:            | How much |             | overpractice | does       | Fast        | Forwarding | reduce       | until    | content  |       |
| mastery         | across   | different   | problem      |            | selection   | regimes?   |              |          |          |       |
| We conducted    |          | experiments |              | through    | simulations | based      | on           | solution | pathways |       |
and parameters estimated from open-source data system. We chose equation
solving as a domain due to its recursive nature: foundational skills are often re-
peatedattheendofsolvingforX.However,wenotethatthemethods studied
here apply to numerous other domains of instruction with step-level
problem solving, for which tutoring systems are available [2]. In STEM
problem solving, science domain decisions tend to happen first (e.g., selecting
physics principles), while later steps involve algebra or arithmetic, which many
students may have mastered. In all of these domains, fast-forwarding could re-
move overpracticed steps by completingmastered steps onbehalf ofthe learner.
| 2 Related   | Work   |     |     |         |           |     |     |     |     |     |
| ----------- | ------ | --- | --- | ------- | --------- | --- | --- | --- | --- | --- |
| 2.1 Learner | Models |     | and | Problem | Selectors |     |     |     |     |     |
Various learner models have been developed to model students’ learning and
problem-solvingbehaviors.Bayesianknowledgetracing,arguablythemostwidely

4 M. Xia et al.
usedmodelinadaptivelearningsystemstoday,modelslearners’latentknowledge
of distinct skills as a probability of knowing each [8]. Other dynamic probabilis-
tic models have been proposed to model the dependency of different learning
concepts. For example, Learning Factor Analysis [6] models learner knowledge
states via logistic regression to deal with learning concepts at different levels,
and Performance Factor Analysis [25] fits distinct learning rates for correct and
incorrect responses. Other models, such as deep knowledge tracing, use neu-
ral network architectures to model and predict learner performance [26]. These
learnermodelsassesslearners’masteryofvariousskillsandhowtheyevolvewith
provided practice opportunities.
Many problem selection algorithms use estimated content mastery in adap-
tive learning in diverse ways. Contemporary mastery problem selection algo-
rithms used in Cognitive Tutor typically select the problem with the most un-
masteredskills(masteryhard)[2,14].ProblemselectionalgorithmsinTutorShop
[1] also offer a similar regime that selects problems with the least, but at least
one, mastered skills (mastery easy). However, all these selectors, while gener-
ally reducing student practice time [27], are limited in that they require a static
pool of content and skills. Few notable exceptions exist, where tutoring systems
have been designed to adaptively take over specific, commonly overpracticed
steps [28,16]. Other researchers proposed to supplement problem sets with fo-
cused tasks to reduce overpractice, which are problems that target a few skills
simultaneously. They particularly designed practice problems that involve only
a focused set of skills that students have not mastered and then selected these
focused tasks with higher probability [11,12]. However, designing focused tasks
istime-consumingandrequirescontentauthoring.Fast-Forwarding,themethod
proposed in this study, in contrast, can be applied to any existing question pool
and dynamically monitors whether certain steps can be skipped based on mas-
tery estimates to mitigate overpractice.
2.2 Learner Simulation
Simulating learner data to study learning processes and outcomes is a core
method in the field, particularly where obtaining real-world data is challeng-
ing,expensive,orimpractical[13].Thesesimulationsleveragecognitivelearning
theories to generate performance patterns that can be used to refine instruc-
tional methods. For instance, past research has employed simulated learners to
identify skill models based on performance patterns, which were subsequently
validated on real learner data, leading to improved instruction tailored to these
identified skills [19]. Similar refinements have been applied to analyzing error
types [31]. Recent research using Generative Adversarial Networks (GANs) has
alsobeenappliedtoenhancetheassessmentofstudentknowledgethroughsimu-
lation:Zhangetal.[33]augmentedlogdatafromtutoringsystemsusingGANs,
which improved the reliability of knowledge estimates.
However,despitetheseadvancesinsimulationsforrefiningknowledgetracing
andinstruction,thereisalackofsimulatedlearnerexperimentsthatquantifythe
impactofproblem selectionalgorithmsonpractice timeandefficiency.Previous

Optimizing Mastery Learning by Fast-Forwarding 5
workhasprimarilyfocusedonsimulatingtheeffectsofsettingmasterythresholds
for error types [9] or on performance prediction given different mastery levels
[24]. In addition, validating simulated learners on outcomes of interest remains
a key research challenge. According to a recent literature review by Käser and
Alexandron[13],amajorissueinpreviousresearchusingsimulatedlearnerdata
isthelackofsystematicstudiesonthevalidityofsyntheticdata.However,there
are exceptions, such as the work that used simulated student data in tutoring
systems to predict real student performance [22]. Similarly, recent studies have
increasingly used synthetic data to improve predictive models and predictive
validity [33]. Our research simulates the practice efficiency of different problem-
selection strategies in tutoring systems. We incorporate empirical estimates of
learning rates and solution pathways into our simulations to improve validity.
3 Methods
3.1 Study Context and Dataset
We utilize an open-source dataset from APTA, a collaborative tutoring sys-
tem for middle school equation-solving, available on PSLC DataShop (datasets
#5549 and #5604) [17]. The study sample consists of data from IRB-approved
classroom studies conducted in math classes at two public suburban middle
schools in a mid-sized city in the eastern U.S. Overall, 164 6th- to 8th-grade
students engaged with a series of multi-step linear equation-solving problems
[5].
We analyzed the data comprising 10,937 entries (N = 10,937) of completed
and timestamped problem-solving steps using the DataShop student step rollup
tool [17]. The log data provide a detailed description of the student solution
paths, meaning the order of operations used to solve individual problems. This
allows for a fine-grained analysis of skills (e.g., add constant) students employ
to derive solutions, offering deeper insights into their step-level problem-solving
processes and serving as reference pathways for our simulation studies.
We only considered students’ first attempts, as they reflect the students’
initial response to solving linear equation steps without tutor assistance. Steps
exhibiting hint usage were classified as incorrect attempts [17].
3.2 Computation of Overpractice
We define overpractice on a skill as the number of practice opportunities (e.g.,
problem-solving steps) on a skill given a predicted error rate on that skill below
0.05, in line with the mastery criteria in the Lynnette tutor [21]. Table 1 reveals
severalkeyfindingsregardingstudentperformanceandpracticebehavioracross
different skills. This analysis served as a baseline for how much over-
practice was present in our dataset from real students. Simulations, as
described below, were then used to determine how much students could poten-
tially save if they had unlimited practice time and under different, alternative
problem-solving regimes.

| 6 M. | Xia et al. |     |     |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- | --- | --- |
Table1:Studentmasteryrates,practiceandoverpracticeopportunitiesforeach
skillbasedonstudentdata.Thefirstrowshowsthe%ofstudentswhomastered
eachskill,thesecondrowtheaveragenumberofproblem-solvingstepsperskill,
| and the     | third row the | number  | of    | steps    | taken after         | mastery (overpractice). |            |
| ----------- | ------------- | ------- | ----- | -------- | ------------------- | ----------------------- | ---------- |
|             | cancel-       | cancel- | comb- | comb-    | division- division- | simplify- add/subtr-    | add/subtr- |
|             | const         | var     | const | var      | complex simple      | division const          | var        |
| Mastered(%) | 74.4          | 6.7     | 73.8  | 6.7      | 26.8 79.3           | 79.3 68.9               | 6.7        |
| AvgOpps.    | 15.9          | 1.1     | 16.2  | 0.9      | 4.1 15.4            | 18.3 16.3               | 1.2        |
| AvgOverpr.  | 6.4           | 0.5     | 6.7   | 0.5      | 1.5                 | 7.8 9.8 6.2             | 0.5        |
| Varied      | Skill Mastery |         | and   | Practice | Engagement          | The “Mastered”          | col-       |
umn indicates the proportion of students who achieved mastery for each skill,
whilethe“AvgOpps” columndenotestheaveragenumberofcompletedpractice
opportunities per skill. Average practice engagement varies significantly, with
some skills having a higher average number of completed practice opportunities
| than others, | such as      | division-simple. |     |        |               |            |             |
| ------------ | ------------ | ---------------- | --- | ------ | ------------- | ---------- | ----------- |
| Severe       | Overpractice |                  | The | column | “Avg Overpr.” | delineates | the average |
number of practice opportunities associated with overpractice for each skill. A
considerable number of students experience overpractice across all skills. While
more students overpractice the skills, some students achieve mastery of them.
3.3 Fast-Forwarding
Fast-Forwarding is a novel technique introduced in Fig. 1 that terminates
practice problems early and forwards students to the next problem during the
active problem-solving process (“inner loop” [30]). Fast-Forwarding is a flexible
technique that can augment existing problem selection algorithms. Its only re-
quirement is access to a pool of multi-step practice problems–a precondition for
| any step-level | adaptation. |     |     |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- | --- |
Fast-Forwardingoptimizespracticeefficiencybyfocusingonproblem-solving
stepsthatareunmastered,allowingstudentstoachieveproficiencymorequickly
without redundant practice of already mastered skills (i.e., overpractice). How-
ever, a key considerationwasto exclude skills from thesolution pathway if and
only if all remaining skills had already been mastered. This decision
is informed by the literature on the composition effect [10], which is explained
below.
| Specifically, | we  | did not | adopt | a model | that | would fast-forward | students |
| ------------- | --- | ------- | ----- | ------- | ---- | ------------------ | -------- |
through problem-solving steps for any skill they had already mastered in the
middle of the problem. Advancing students this way might limit the benefits
of practicing combinations of skills in multi-step problem solving; in that case,
unmastered in combination with mastered skills. This effect, known as the com-
position effect, suggests that a skill can be more challenging when practiced
alongside a second skill and may require integrated practice [10]. Thus, Fast-
Forwarding ensures students continue to practice skill combinations until all in-
volved skills are mastered, preventing premature advancement that could leave
| important | compositions | unpracticed |     | or  | systematically | underpracticed. |     |
| --------- | ------------ | ----------- | --- | --- | -------------- | --------------- | --- |

Optimizing Mastery Learning by Fast-Forwarding 7
3.4 Simulation Methodology
Wesimulatestudentperformance(AFM;[6])andtracestudentknowledge(BKT;
[8])throughtwodistinctmodels.AFMandBKTworktogethertosimulatestu-
dentresponsesanddifferentproblem-selectionregimes.Oursimulationsfocuson
problem-solvingprocessesatthestep-level,inlinewithAFM[6]andprioranal-
yses of our study data [5]. Besides the present description, we promote method
adoption and reproducibility by open-sourcing our code on GitHub3.
KnowledgeTracing:MimickingtheknowledgetracingwithintheLynnette
tutoring system, we employ BKT [8] to analyze student responses and consider
mastery to be achieved at a threshold of 95%, which is the threshold in our
study data’s Lynnette tutoring system [21]. BKT models student learning as a
hidden Markov process where each skill is represented by a binary latent state
(learned or unlearned). The model updates the probability of mastery based
on observed correct and incorrect responses, using four key parameters: prior
knowledge (p ), the initial probability that a student knows the skill before
init
any practice, learning rate (p ), the probability of transitioning from the
learn
unlearned to the learned state on each opportunity, guess rate (p ), the
guess
probability of answering correctly by guessing when the skill is unlearned, and
slip rate (p ), the probability of answering incorrectly due to a mistake when
slip
the skill is learned. Given an observed response, BKT applies Bayes’ rule to
update the posterior probability of mastery. If a student answers correctly, the
model increases the mastery probability, accounting for possible guessing. If
theyanswerincorrectly,itdecreasestheprobability,adjustingforslips.Mastery
is typically declared when the posterior probability of a student being in the
learned state exceeds a predefined threshold (here, 95%). For our simulations,
we used standard TutorShop BKT parameters for all skills (p = 0.25, p
init learn
=0.2,p =0.2,p =0.1),ensuringconsistencywithtypicalcognitivetutor
guess slip
implementations [1]. For this study, we simulate 10,000 simulated students that
exhibitanormaldistributionininitialAFMproficiencylevels.Thissamplesizeis
expectedtoyieldsufficientlyreliableresults.Wenotethatstatisticalsignificance
testing our context is not meaningful, as more simulation samples will always
tend to produce significant differences, no matter the minuteness of effect sizes.
Student Simulation: We simulate student learning data using AFM [6], a
logisticregressionmodelofknowledgeacquisition(representedastheprobability
of getting a specific problem-solving step requiring specific skills correct) as a
function of learners’ initial proficiency levels, skill-specific difficulty, and skill-
specific learning rates. To promote the validity of our methodology, we fit the
standard AFM model [6] to our open source dataset (see Section 3.1) to obtain
estimatesofstudentacquisitionratesacrossdifferentskills,whichthenservethe
simulation of performance in our experiments. Skill-level learning rates used for
simulation are encoded in interactions between the learning opportunity count
and the skill exercised at a given problem-solving step. This AFM learning rate
should not be confused with the BKT parameters for knowledge tracing serving
3https://github.com/rschmucker/fast-forwarding

| 8   | M. Xia | et al. |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
problem selection, where we use standard default settings from Lynnette, which
assumeconstantskilllearningratesacrossallskills(seeabove)tomimicstudent
| experiences | in     | the original | study.   |       |     |      |          |         |       |     |
| ----------- | ------ | ------------ | -------- | ----- | --- | ---- | -------- | ------- | ----- | --- |
| We          | define | prototypical | solution | paths | for | each | practice | problem | based | on  |
the most frequent skill-application path for each problem in our data. At each
step in the simulation, we sample a student response based on the correctness
probability estimated by the AFM model. We update the AFM simulation and
BKT models before moving to the next step or practice problem. In line with
Lynnette [21], BKT mastery estimates provide a basis for all problem-selection
algorithms–including the proposed Fast-Forwarding method. To address RQ2,
we implement a mechanism that replenishes the problem pool after it has been
exhausted,meaningthattheproblempoolisresettoitsinitialstate.Thismech-
anism ensures that the simulation only terminates once all skills are mastered.
| Problem-selection |     |     | Algorithms |     | Fast-Forwarding |     | offers | a flexible | method |     |
| ----------------- | --- | --- | ---------- | --- | --------------- | --- | ------ | ---------- | ------ | --- |
forenhancingtheefficiencyofexistingproblem-selectionalgorithms.Toverifyits
capabilities,thisstudyintegratesFast-Forwardingintodiverseproblemselectors:
| Random:        |          | Selects   | problems     | from     | the pool  | at random | without |                | replacement. |         |
| -------------- | -------- | --------- | ------------ | -------- | --------- | --------- | ------- | -------------- | ------------ | ------- |
| Deterministic: |          |           | Selects      | problems | following | a domain  |         | expert-defined |              | order   |
| taken          | directly | from      | the standard |          | Lynnette  | set suite | [21]    | designed       | to           | surface |
| increasingly   |          | difficult | and          | complex  | problems  | over      | time.   |                |              |         |
MasteryEasy[2]:Employsstudentmasteryestimatestoselectproblemsby
averagingthedifficultyofallavailableopportunitiesandservingtheproblem
| withthelowest |     | difficultybasedonmasteryestimateswhileensuringthatthe |              |            |         |           |     |           |          |     |
| ------------- | --- | ----------------------------------------------------- | ------------ | ---------- | ------- | --------- | --- | --------- | -------- | --- |
| problem       | has | at least                                              | one          | unmastered | skill.  |           |     |           |          |     |
| Mastery       |     | Hard                                                  | [2]: Employs | student    | mastery | estimates |     | to select | problems |     |
byaveragingthedifficultyofallavailableopportunitiesandservingtheprob-
lemwiththegreatestdifficulty,usuallyfeaturingthemostunmasteredskills.
| This | selector | is the | standard | problem | selector | in  | Lynnette | [21] | and is | evalu- |
| ---- | -------- | ------ | -------- | ------- | -------- | --- | -------- | ---- | ------ | ------ |
| ated | in RQ1.  |        |          |         |          |     |          |      |        |        |
FocusedPractice[11]:Morerecentselectionalgorithmthatconsidersprob-
lemdifficultywhilepreferentiallysamplingproblemswithfewskillsviamulti-
| nomial | sampling. |     |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4 Results
| 4.1 Learning |     | Efficiency |     | Benefits | (RQ1) |     |     |     |     |     |
| ------------ | --- | ---------- | --- | -------- | ----- | --- | --- | --- | --- | --- |
For the legacy mastery-based problem selector, Fast-Forwarding reduced over-
practiceby35.7%acrossthesimulatedstudents,asmeasuredinlearningoppor-
tunities to apply mastered skills. Assuming a median number of steps, under-
practicewasnotchangedbyFast-Forwarding(M=0.44forFast-Forwardingvs.
M=0.43without).Hence,Fast-Forwardingmitigatesoverpracticewhilenotin-
troducingmoreunderpractice,meaningthatoverallmasterylevelsdonotsuffer.

|     |     |     | Optimizing | Mastery | Learning | by Fast-Forwarding |     | 9   |
| --- | --- | --- | ---------- | ------- | -------- | ------------------ | --- | --- |
Fig.2: Stacked bar plot showing the reduction in overpractice across individual
| skills when | Fast-Forwarding |     | is     | applied.     |                |        |          |        |
| ----------- | --------------- | --- | ------ | ------------ | -------------- | ------ | -------- | ------ |
| Fig.        | 2 shows         | the | sum of | overpractice | across various | skills | averaged | across |
students.Overall,withoutFast-Forwarding,overpracticeissubstantiallyhigher,
whichcanbeattributedtocontinuingpracticewithoutearlyterminationoffully
masteredpathways.Notably,Fast-Forwardingremovesoverpracticeentirelyfrom
some skills. For example, in our sample, Fast-Forwarding removed overpractice
from the skills “subtract variable,”, “combining like variables,” and “cancel vari-
able.” Theseareskillsthattypicallyappearattheendofpracticeproblems.The
same is true for skills involving handling constants. However, these skills may
also be required to set up more advanced skills through transformation, such as
division. These “setup” skills may not always be eliminated by Fast-Forwarding.
For example, 3x - 2 = 4 requires first subtracting as division by 3 upfront is not
| permitted   | in Lynnette, |        | which   | only accepts | whole numbers | [21]). |     |     |
| ----------- | ------------ | ------ | ------- | ------------ | ------------- | ------ | --- | --- |
| 4.2 Effects |              | Across | Problem | Selectors    | (RQ2)         |        |     |     |
One strength of Fast-Forwarding is that it does not depend on the specific
problem-selection algorithm used. Fig. 3 shows the impact of applying Fast-
Forwarding on overpractice across various problem selection regimes. This sim-
ulation aimed to determine how much overpractice students would encounter to
reach mastery, assuming unlimited time. Notably, Fast-Forwarding consistently
reduced overpractice across all problem selectors, ranging from 0.1% to 35.7%.
The largest reduction for the legacy mastery hard problem selector aligns with
RQ1 findings, but with the difference that no learning opportunity limit was
| imposed  | here, | reducing | overpractice | somewhat        | more. |           |                 |     |
| -------- | ----- | -------- | ------------ | --------------- | ----- | --------- | --------------- | --- |
| As error | bars  | in Fig.  | 3 indicate,  | between-student |       | variation | in overpractice |     |
differed across problem selectors. As expected, random scheduling led to the
largest variation, and deterministic scheduling led to the second-lowest varia-
tion. Despite this variation, Fast-Forwarding still led to a notable reduction in
overpractice of 0.67 SD for this problem selector. Surprisingly, mastery easy

10 M. Xia et al.
led to the lowest variation in overpractice and only marginal overpractice re-
ductions from Fast-Forwarding. Notably, the modest reduction in the focused
practice problem selector was concurrent with the second-largest variation in
overpractice across students (7.9%, corresponding to a reduction of 0.41 SD).
Wesuspectthisvariationstemsfromincreasedrandomnessintheproblemselec-
tor,both choosingskillsand problems randomly. Accordingly, themastery hard
problem selector was more desirable based on the reported largest reduction in
overpractice (35.7%; RQ1) and lower between-student variation, corresponding
to a substantial effect size of 3.4 SD.
Finally, given the content unit being designed to include sufficient prob-
lems to allow all students to master content, the deterministic problem selector,
requiring all problems, was associated with substantial overpractice, over ten
times larger than mastery-based problem selectors. Overall, assuming students
exert continued practice effort, mastery is obtained with the least overpractice
for problem selectors with Fast-Forwarding, especially those who preferentially
serve difficult problems.
Fig.3: Overpractice difference across problem selectors for Fast-Forwarding, in-
cluding%decreaseswhenFast-Forwardingisapplied.Errorbarsare2SDacross
students.
5 Discussion
Masterylearningmakeslearnersimproveefficiently[27].Problemselectioniskey
inimprovinglearninganalyticsapplicationsthatsupportmasterylearning,most
notablytutoringsystems[12].Theobjectiveofthepresentstudywastoevaluate
a novel method that promises to improve the efficiency of mastery learning as
measuredinoverpractice[6]whilepreservingmulti-stepproblemsolvingandits
benefits to learning [10]. Through simulation based on parameters informed by

Optimizing Mastery Learning by Fast-Forwarding 11
realstudentdata,weappliedourmethod,Fast-Forwarding,tomitigateoverprac-
ticeacrosscontemporaryandlegacymethodsforproblemselectioninatutoring
system.
5.1 Fast-Forwarding Under Legacy Practice Conditions (RQ1)
RQ1 focused on learning efficiency gains in a legacy mastery problem selector,
prioritizing hard problems given limited practice time. Informing practice time
by average step completions of students in an open-source dataset and using
learningparametersfromthesamedata,ouranalysisaimedatcloselyestimating
how much practice students could save by our Fast-Forwarding method. Under
limitedpracticetime,ourfindingsindicatethatstudentscouldsaveuptoabout
athirdofoverpracticeinalinearequation-solvingtutor[21]byFast-Forwarding.
Inparticular,thisoverpracticebenefitwasnotaccompaniedbyanunderpractice
deficit, indicating that the overall efficiency of practice improved.
Ourfindingsposetwocentralquestionsforfutureresearch.First,whileFast-
Forwarding is generally applicable to any mastery-based problem selector and
contentunit,equationsolvingisataskdomainthatnaturallyaffordsahighlevel
of overpractice: More complex problems require more steps than simple prob-
lems, and intermediate problem states are similar to simpler problems, whose
problem steps are repeated. Some of these “foundational steps” at the end of
equations were eliminated from overpractice through Fast-Forwarding, for ex-
ample, combining variables. However, other task domains might not have such
hierarchical problem structures, such that Fast-Forwarding could potentially be
less effective for such domains, which merits future research. Specifically, our
methodcontributesanovelmethodofoverpracticereductioninadditiontocur-
ricular redesign [7] and problem selection optimization [12]. It is possible that
each of these methods may be most effective across different domains. However,
wearguethatourmethodcanbemostreadilyappliedtoanymulti-stepproblem-
solving domain with knowledge tracing [1], including any problem selector.
Notably, Fast-Forwarding could not eliminate all underpractice in equation
solving, potentially because some steps are required to set up more complex,
unmastered operations, such as division, where students first need to subtract
constants (a more foundational skill) to divide adequately (e.g., in 3x - 2 = 4,
where division by 3 upfront, leading to non-integers, is not permitted in Lyn-
nette [21]). While Lynnette could fast-forward students to the state 3x = 6 to
just practice division, dealing with constants, in this case, may pose an impor-
tant learning opportunity, assuming a compositioneffect whereby the same skill
is more or less difficult depending on co-occurring skills [10]. Although Fast-
Forwardingcurrentlypreservessuchlearningopportunities,futureresearchmay
investigate to what extent learners could benefit from intermediate forwarding.
5.2 Fast-Forwarding is Effective for High-Difficulty Selectors (RQ2)
Assuming unlimited practice time, RQ2 focused on the effectiveness of Fast-
Forwarding flexibly applied to different contemporary and legacy problem se-

12 M. Xia et al.
lection regimes. We find that, in a content pool with enough problems to allow
all students to master all skills, mastery learning as such already substantially
reduces overpractice compared to deterministic problem selectors that require
learners to fully complete a unit before moving on. However, for all mastery-
based algorithms, including recent ones that try to create more opportunities
for focused practice and less overpractice [11], Fast-Forwarding further reduced
overpractice. However, it was especially effective for selectors that prioritized
difficult problems while minimizing overpractice differences between students,
which may be desirable for creating practice regimes that are equally effective
forallstudents[15].Oneinterpretationofthisfindingisthatmasteryalgorithms
that prefer harder problems tend to serve problems with many skills (i.e., the
mastery hard algorithm used in this study tends to maximize the number of
unmastered skills in a problem). In contrast, the mastery easy algorithm tends
toserveproblemswithfewerskills(withatleastoneunmasteredskill)[14].Itis
hence expected that longer problems allow for more opportunities for the Fast-
Forwarding mechanism to fast-forward the student, reducing overpractice to a
larger extent. Second, selectors that preferred harder problems in our selection
also led to the least problem selection overall. This is perhaps because, unlike
Mastery Easy, such selectors more heavily punish problems that include mas-
tered knowledge, as Mastery Easy only requires at least one skill in a problem
to be unmastered.
5.3 Considerations Towards Applying Fast-Forwarding in Practice
While our findings suggest that Fast-Forwarding alongside selecting hard prob-
lemsreducesoverpracticemost(basedonsimulationassumptionsaboutlearning
based on real student data; a key issue identified in past research [13]), it is not
self-evident that such problem selection regimes will be most effective for learn-
ing in practice. Although mastery learning is effective [27], it can be difficult for
studentstomaintaintheeffortrequiredtoengageinpractice.Studiespublished
inthe1970sdocumentedthatstudentparticipationincomputer-assistedinstruc-
tiondecreasedwithdifficultiesbelow80%expectedaccuracyandwashighwhen
problems were easy [23]. While motivational theory suggests that a moderate
level of difficulty is the most desirable level for motivation, more recent research
also suggests that novelty and variation in learning tasks can compensate for
some of the adverse effects of high difficulty on motivation [20]. Engagement in
practice is crucial for the learning benefits of tutoring systems [15]. Therefore,
potentially more important than practice efficiency (i.e., much practice with a
little overpractice will usually result in more learning than little or no practice
with no overpractice), future research is required to determine to what extent
Fast-Forwardingcanbenefitstudentsandtheirlearningmost.Althoughourfind-
ingssuggestthatFast-Forwardingisespeciallyhelpfulinreducingoverpracticein
problemselectorsprioritizinghardproblems,increasingdifficulty(i.e.,removing
mastered skills) even further through Fast-Forwarding may not always be desir-
able for student motivation and engagement. Increasing the novelty of tasks to

|     |     |     | Optimizing |     | Mastery Learning |     | by Fast-Forwarding |     | 13  |
| --- | --- | --- | ---------- | --- | ---------------- | --- | ------------------ | --- | --- |
potentially and partially offset this effect [20] could be realized through author-
ing additional focused tasks [18] or potentially only executing Fast-Forwarding
sometimes and at random, which would also lower overall practice difficulty by
occasionally including mastered skills. Independently, current mastery thresh-
olds (i.e., 95%) might be better if they were higher to account for forgetting, an
interesting question outside the scope of our paper with some nascent evidence
[32]. These design considerations, including how to best introduce and realize
Fast-Forwarding in the tutoring system interface, are beyond the scope of the
| present         | study | and subject | to     | future | research. |     |     |     |     |
| --------------- | ----- | ----------- | ------ | ------ | --------- | --- | --- | --- | --- |
| 5.4 Limitations |       | and         | Future | work   |           |     |     |     |     |
First, our findings are limited to a single domain (i.e., equation solving). Given
the portability of Fast-Forwarding to any problem selector and problem domain
with empirically derived student solution pathways, our findings merit future
| research | into | more domains    | of  | tutoring,      | which | our open-source |         | code enables.    |     |
| -------- | ---- | --------------- | --- | -------------- | ----- | --------------- | ------- | ---------------- | --- |
| Second,  | our  | Fast-Forwarding |     | implementation |       | was             | limited | because Bayesian |     |
Knowledge Tracing (BKT) parameters were not fitted for individual students,
which may have impacted the precision of skill mastery predictions. Although
our BKT values used aligned with actual Lynnette settings [21], future research
shouldconsiderindividualfittingBKTparameterstolearnerdataformorepre-
| cise problem |     | selection | and simulation. |     |     |     |     |     |     |
| ------------ | --- | --------- | --------------- | --- | --- | --- | --- | --- | --- |
Third,ourfindingsarelimitedtoasingleskillmodel,whilepotentialdifficulty
factors in complex skill models may better describe the learner data [21]. A risk
of using Fast-Forwarding when applied to coarse-grained skill models is taking
away practice from difficult, hidden skills. Although skill model refinement is a
key challenge in data-driven tutoring system improvement [11], future research
maystudywhateffectsFast-Forwardinghasonmorecoarse-grainedskillmodels.
6 Conclusion
This study introduced the generalizable Fast-Forwarding method to enhance
mastery learning efficiency by reducing overpractice while preserving the ben-
efits of multi-step problem solving. Our simulation studies showed that Fast-
Forwardingreducesoverpracticebyuptoone-third,particularlyinselectorspri-
oritizing harder problems. This improvement makes it a promising tool for opti-
mizingtutoringsystems,akeyapplicationareaoftechnology-enhancedlearning.
These findings suggest that balancing efficiency with task difficulty, which may
reduce student engagement if too high, should be a key consideration in future
| research | to improve | learning |     | in practice. |     |     |     |     |     |
| -------- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
Acknowledgments
This research was funded by the Institute of Education Sciences (IES) of the
| U.S. Department |     | of Education |     | (Award | #R305A220386). |     |     |     |     |
| --------------- | --- | ------------ | --- | ------ | -------------- | --- | --- | --- | --- |

| 14 M. Xia | et al. |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
References
1. Aleven, V., Borchers, C., Huang, Y., Nagashima, T., McLaren, B., Carvalho,
| P., Popescu,     | O.,  | Sewall,     | J.,      | Koedinger, | K.:      | An integrated   | platform |       | for study- |
| ---------------- | ---- | ----------- | -------- | ---------- | -------- | --------------- | -------- | ----- | ---------- |
| ing learning     | with | intelligent | tutoring |            | systems: | CTAT+TutorShop. |          | arXiv | preprint   |
| arXiv:2502.10395 |      | (2025)      |          |            |          |                 |          |       |            |
2. Aleven,V.,Mclaren,B.M.,Sewall,J.,Koedinger,K.R.:Anewparadigmforintel-
ligenttutoringsystems:Example-tracingtutors.InternationalJournalofArtificial
| Intelligence | in  | Education | 19(2), | 105–154 | (2009) |     |     |     |     |
| ------------ | --- | --------- | ------ | ------- | ------ | --- | --- | --- | --- |
3. Aleven,V.,McLaughlin,E.A.,Glenn,R.A.,Koedinger,K.R.:Instructionbasedon
| adaptive   | learning | technologies. |     | Handbook | of  | research on | learning | and | instruction |
| ---------- | -------- | ------------- | --- | -------- | --- | ----------- | -------- | --- | ----------- |
| 2, 522–560 | (2016)   |               |     |          |     |             |          |     |             |
4. Bloom, B.S.: A response to slavin’s mastery learning reconsidered. Review of Ed-
| ucational | Research | 57(4), | 507–508 | (1987) |     |     |     |     |     |
| --------- | -------- | ------ | ------- | ------ | --- | --- | --- | --- | --- |
5. Borchers, C., Yang, K., Lin, J., Rummel, N., Koedinger, K.R., Aleven, V.: Com-
| bining dialog | acts | and | skill modeling: |     | What | chat interactions |     | enhance | learning |
| ------------- | ---- | --- | --------------- | --- | ---- | ----------------- | --- | ------- | -------- |
ratesduringai-supportedpeertutoring?In:Proceedingsofthe17thInternational
| Conference | on  | Educational | Data | Mining | (2024) |     |     |     |     |
| ---------- | --- | ----------- | ---- | ------ | ------ | --- | --- | --- | --- |
6. Cen, H., Koedinger, K., Junker, B.: Learning factors analysis–a general method
| for cognitive | model    | evaluation |     | and improvement. |          | In: International |     | conference | on  |
| ------------- | -------- | ---------- | --- | ---------------- | -------- | ----------------- | --- | ---------- | --- |
| intelligent   | tutoring | systems.   | pp. | 164–175.         | Springer | (2006)            |     |            |     |
7. Cen,H.,Koedinger,K.R.,Junker,B.:Isoverpracticenecessary?-improvinglearn-
| ing efficiency | with         | the | cognitive        | tutor | through | educational | data | mining. | Frontiers |
| -------------- | ------------ | --- | ---------------- | ----- | ------- | ----------- | ---- | ------- | --------- |
| in artificial  | intelligence |     | and applications |       | 158,    | 511 (2007)  |      |         |           |
8. Corbett,A.T.,Anderson,J.R.:Knowledgetracing:Modelingtheacquisitionofpro-
ceduralknowledge.Usermodelinganduser-adaptedinteraction4,253–278(1994)
9. Fancsali,S.,Nixon,T.,Ritter,S.:Optimalandworst-caseperformanceofmastery
learningassessmentwithbayesianknowledgetracing.In:EducationalDataMining
2013 (2013)
10. Heffernan, N.T., Koedinger, K.R.: A developmental model for algebra symboliza-
tion:Theresultsofadifficultyfactorsassessment.In:Proceedingsofthetwentieth
| annual conference |     | of the | cognitive | science | society. | pp. 484–489. |     | Routledge | (2022) |
| ----------------- | --- | ------ | --------- | ------- | -------- | ------------ | --- | --------- | ------ |
11. Huang, Y.: Learner modeling for integration skills in programming. Ph.D. thesis,
| University | of Pittsburgh |     | (2018) |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
12. Huang, Y., Lobczowski, N.G., Richey, J.E., McLaughlin, E.A., Asher, M.W.,
Harackiewicz,J.M.,Aleven,V.,Koedinger,K.R.:Ageneralmulti-methodapproach
todata-drivenredesignoftutoringsystems.In:LAK21:11thInternationalLearn-
| ing Analytics | and | Knowledge |     | Conference. | pp. | 161–172 (2021) |     |     |     |
| ------------- | --- | --------- | --- | ----------- | --- | -------------- | --- | --- | --- |
13. Käser, T., Alexandron, G.: Simulated learners in educational technology: A sys-
| tematic      | literature | review    | and    | a turing-like | test. | International | Journal | of  | Artificial |
| ------------ | ---------- | --------- | ------ | ------------- | ----- | ------------- | ------- | --- | ---------- |
| Intelligence | in         | Education | 34(2), | 545–585       | (Jun  | 2024)         |         |     |            |
14. Koedinger, K., Pavlik Jr, P.I., Stamper, J., Nixon, T., Ritter, S.: Avoiding prob-
| lem selection | thrashing |     | with conjunctive |     | knowledge | tracing. | In: | Educational | data |
| ------------- | --------- | --- | ---------------- | --- | --------- | -------- | --- | ----------- | ---- |
| mining 2011   | (2010)    |     |                  |     |           |          |     |             |      |
15. Koedinger, K.R., Carvalho, P.F., Liu, R., McLaughlin, E.A.: An astonishing reg-
| ularity in | student     | learning | rate. | Proceedings |     | of the National | Academy |     | of Sciences |
| ---------- | ----------- | -------- | ----- | ----------- | --- | --------------- | ------- | --- | ----------- |
| 120(13),   | e2221311120 | (2023)   |       |             |     |                 |         |     |             |
16. Koedinger, K.R., Corbett, A.: Cognitive tutors. Smart machines in education pp.
145–167 (2001)

Optimizing Mastery Learning by Fast-Forwarding 15
17. Koedinger, K.R., D’Mello, S., McLaughlin, E.A., Pardos, Z.A., Rosé, C.P.: Data
mining and education. Wiley Interdisciplinary Reviews: Cognitive Science 6(4),
333–353 (2015)
18. Koedinger, K.R., McLaughlin, E.A.: Closing the loop with quantitative cognitive
task analysis. International Educational Data Mining Society (2016)
19. Li, N., Stampfer, E., Cohen, W., Koedinger, K.: General and efficient cognitive
modeldiscoveryusingasimulatedstudent.In:ProceedingsoftheAnnualMeeting
of the Cognitive Science Society. vol. 35 (2013)
20. Lomas,J.D.:OptimizingMotivationandLearningwithLarge-ScaleGameDesign
Experiments. Phd thesis, Human-Computer Interaction Institute, School of Com-
puter Science, Carnegie Mellon University (2014)
21. Long, Y., Holstein, K., Aleven, V.: What exactly do students learn when they
practiceequationsolving?refiningknowledgecomponentswiththeadditivefactors
model.In:Proceedingsofthe8thInternationalConferenceonLearningAnalytics
and Knowledge. pp. 399–408 (2018)
22. Matsuda, N., Cohen, W.W., Sewall, J., Lacerda, G., Koedinger, K.R.: Predicting
students’performancewithsimstudent:Learningcognitiveskillsfromobservation.
Frontiers in Artificial Intelligence and Applications 158, 467 (2007)
23. Miller,R.,Hess,R.D.:Theeffectsuponstudents’motivationoffitbetweenstudent
abilityandlevelofdifficultyofcaiprograms.Tech.rep.,StanfordUniversity,School
of Education, Stanford, Calif. (1972)
24. Pardos, Z.A., Yudelson, M.V.: Towards moment of learning accuracy. In: AIED
2013 Workshops Proceedings Volume. vol. 4, p. 3. Citeseer (2013)
25. Pavlik Jr, P.I., Cen, H., Koedinger, K.R.: Performance factors analysis–a new al-
ternative to knowledge tracing. Online Submission (2009)
26. Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L.J., Sohl-
Dickstein, J.: Deep knowledge tracing. In: Advances in Neural Information Pro-
cessing Systems. pp. 505–513 (2015)
27. Ritter,S.,Yudelson,M.,Fancsali,S.E.,Berman,S.R.:Howmasterylearningworks
atscale.In:ProceedingsoftheThird(2016)ACMConferenceonLearning@Scale.
pp. 71–79 (2016)
28. Ritter,S.,Anderson,J.R.:Calculationandstrategyintheequationsolvingtutor.
In: Proceedings of the Annual Meeting of the Cognitive Science Society. vol. 17
(1995)
29. Schmucker, R., Wang, J., Hu, S., Mitchell, T.: Assessing the knowledge state of
online students - new data, new approaches, improved accuracy. Journal of Edu-
cational Data Mining 14(1), 1–45 (2022)
30. VanLehn, K.: The behavior of tutoring systems. International journal of artificial
intelligence in education 16(3), 227–265 (2006)
31. Weitekamp, D., Ye, Z., Rachatasumrit, N., Harpstead, E., Koedinger, K.: Investi-
gatingdifferentialerrortypesbetweenhumanandsimulatedlearners.In:Artificial
Intelligence in Education: 21st International Conference, AIED 2020, Ifrane, Mo-
rocco, July 6–10, 2020, Proceedings, Part I 21. pp. 586–597. Springer (2020)
32. Zhang, J., Vanacore, K., Baker, R.S., Ch, N., Mills, C., Henkel, O.: How much
mastery is enough mastery? the relationship between mastery in a lesson and
the performance on the subsequent lesson. In: Proceedings of the International
Conference on Educational Data Mining (2025)
33. Zhang, L., Lin, J., Borchers, C., Cao, M., Hu, X.: 3DG: A framework for using
generativeAIforhandlingsparselearnerperformancedatafromintelligenttutoring
systems. arXiv preprint arXiv:2402.01746 (2024)