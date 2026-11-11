GuideAI: A Real-time Personalized Learning Solution with
Adaptive Interventions
Ananya Shukla∗ Satvik Bajpai∗
HTI Lab HTI Lab
Plaksha University Plaksha University
Mohali, Punjab, India Mohali, Punjab, India
ananya.shukla@plaksha.edu.in satvik.bajpai@plaksha.edu.in
Chaitanya Modi∗ Siddharth Siddharth
HTI Lab HTI Lab
Plaksha University Plaksha University
Mohali, India Mohali, Punjab, India
chaitanya.modi@plaksha.edu.in siddharth.s@plaksha.edu.in
Figure 1: GuideAI’s Comprehensive Adaptive Learning Interface. The image illustrates the multi-modal, biosensor-driven
approach of the personalized system across diferent learning modes—text-based, image-based, audio-based and video-based.
Each panel demonstrates real-time adaptation to the learner’s cognitive state, featuring dynamic interventions such as cognitive
load management, stress reduction techniques (box breathing), and posture correction.
Abstract progress markers), physiological interventions (breathing guidance
Large Language Models (LLMs) have emerged as powerful learning and posture correction), and attention-aware strategies (redirecting
tools, but they lack awareness of learners’ cognitive and physiolog- focus using gaze analysis). Additionally, GuideAI supports diverse
ical states, limiting their adaptability to the user’s learning style. learning modalities, including text-based, image-based, audio-based,
Contemporary learning techniques primarily focus on structured and video-based instruction, across varied knowledge domains. A
learning paths, knowledge tracing, and generic adaptive testing but preliminary study (N = 25) assessed GuideAI’s impact on knowledge
fail to address real-time learning challenges driven by cognitive load, retention and cognitive load through standardized assessments. The
attention fuctuations, and engagement levels. Building on fndings results show statistically signifcant improvements in both problem-
from a formative user study (  = 66), we introduce GuideAI, a multi- solving capability and recall-based knowledge assessments. Par-
modal framework that enhances LLM-driven learning by integrat- ticipants also experienced notable reductions in key NASA-TLX
ing real-time biosensory feedback including eye gaze tracking, heart measures including mental demand, frustration levels, and efort,
rate variability, posture detection, and digital note-taking behavior. while simultaneously reporting enhanced perceived performance.
GuideAI dynamically adapts learning content and pacing through These fndings demonstrate GuideAI’s potential to bridge the gap
cognitive optimizations (adjusting complexity based on learning between current LLM-based learning systems and individualized
learner needs, paving the way for adaptive, cognition-aware educa-
∗These authors contributed equally to the work. tion at scale.
CCS Concepts
This work is licensed under a Creative Commons Attribution 4.0 International License.
IUI ’26, Paphos, Cyprus • Applied computing → E-learning;• Human-centered com-
© 2026 Copyright held by the owner/author(s). puting → Interaction design theory, concepts and paradigms;
ACM ISBN 979-8-4007-1984-4/26/03
https://doi.org/10.1145/3742413.3789125 HCI theory, concepts and models.
1218

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
Keywords lack adaptive frameworks that decide when and how to inter-
large language models, adaptive learning, biosensory personaliza- vene. They rely on static prompts or fxed thresholds instead of
tion, multi-modal interaction, AI personalization, vision language context-aware, closed-loop strategies that preserve cognitive
models fow and support metacognitive control [9, 31].
ACM Reference Format: To address these limitations, we frst conducted a formative
Ananya Shukla, Satvik Bajpai, Chaitanya Modi, and Siddharth Siddharth. assessment (  = 66) to identify learner needs. Guided by these
2026. GuideAI: A Real-time Personalized Learning Solution with Adaptive results, this study addresses these gaps by introducing GuideAI,
Interventions. In 31st International Conference on Intelligent User Interfaces a novel biosensor-augmented personalized LLM system across di-
(IUI ’26), March 23–26, 2026, Paphos, Cyprus. ACM, New York, NY, USA, verse learning modalities. Our work makes the following contribu-
17 pages. https://doi.org/10.1145/3742413.3789125
tions:
1 Introduction (1) Integrated Biosensory Framework: We present a unifed
behavioral-physiological sensing framework that fuses real-
The rapid evolution of Large Language Models (LLMs) has trans-
time multi-modal signals such as gaze, HRV, posture, and in-
formed domains such as content generation, scientifc discovery,
teraction traces within an LLM-based learning environment.
and medicine. Their ability to process and generate natural lan-
This enables continuous inference of cognitive-afective states
guage has opened new frontiers in Human–Computer Interaction
including engagement, cognitive load, and fatigue, forming the
(HCI) [3]. In education, integrating LLMs with learning technologies
basis for context-aware and tone-sensitive feedback.
shows particular promise: they can provide instant feedback, scaf-
(2) Adaptive Intervention Strategies: We design a closed-loop
fold explanations, and adapt responses to learner inputs [20, 37, 41].
intervention model that dynamically determines when and how
Recent studies have demonstrated that LLMs have proven efec-
to respond based on inferred learner states. GuideAI delivers
tive as tutoring systems, capable of answering conceptual questions,
tiered interventions at the micro-level (content pacing and com-
explaining complex topics, supporting problem-solving, and pro-
plexity), meso-level (focus and afect regulation), and macro-
moting meta-cognitive refection on knowledge gaps [32]. However,
level (metacognitive guidance) to sustain fow and promote
most current systems remain text-centric and cognitively myopic,
self-regulation
ofering limited personalization and no awareness of learners’ real-
(3) Cross-modal Interface and Empirical Validation: We im-
time cognitive-afective states [2].
plement GuideAI in a multi-modal environment across text,
Learning science research emphasizes that efective learning
image, audio, and video formats, and evaluate it through a
depends on context and fuctuates with attention, cognitive load,
mixed-method study (N = 25) combining biosensor metrics
afect, and physiological well-being [35]. Ideally, intelligent tutors
with self-reported measures. Results demonstrate statistically
would infer these states from multi-modal signals such as gaze,
signifcant improvements in retention, understanding, and cog-
heart rate variability (HRV), posture, or interaction traces, and adapt
nitive load management compared to non-personalized LLM
their strategies accordingly. Yet current LLM tutors remain reactive,
baselines.
relying only on textual cues like correctness, verbosity, or sentiment.
This single-channel approach treats learning as static text-exchange, By creating systems that can sense and respond to learners’ cog-
overlooking the dynamic interplay of attention, uncertainty, and nitive and physiological states in real-time, GuideAI bridges the
afect that drives genuine learning. gap between current LLM-based learning systems and the individ-
This gap can be conceptualized along four critical dimensions ualized needs of learners, paving the way for adaptive, cognition-
that constrain current LLM-based learning systems: aware education at scale. GuideAI’s codebase will be released as
(1) Representation Gap — Textual Proxies for Cognition: Cur- open source.
rent systems assess learner’s understanding mainly through
surface-level text features such as accuracy, verbosity, or senti- 2 Related Work
ment. These overlook deeper indicators of learning—like atten-
2.1 Physiological and Cognitive States as
tion, uncertainty, and cognitive efort—that appear in physio-
Determinants of Learning Efciency
logical and behavioral signals rather than language [11, 12].
(2) Temporal Gap — Lack of Real-time Adaptivity: Most LLM Building upon the need for personalization, recent research em-
tutors follow a turn-based dialogue model, updating only af- phasizes that efective learning is not only a cognitive process but
ter learner’s input. This ignores the continuous dynamics of also deeply infuenced by physiological states. Commins et al. [7]
cognition and emotion, limiting timely interventions that could demonstrated that physical well-being directly modulates cogni-
sustain focus or prevent overload [9]. tive functions essential for efective information processing and
(3) Inference Gap — Absence of Multi-modal State Modeling: knowledge acquisition. Suboptimal physiological states, particu-
Existing systems seldom use multi-modal data such as gaze, larly poor posture, have been linked to increased cognitive load
HRV, or posture to infer learner’s real-time cognitive-afective and diminished learning efciency [48]. Research on cognitive load
states. Without these cues, personalization remains context- theory has established that when mental processing resources are
blind to engagement, fatigue, or frustration [58]. overwhelmed, learning efciency decreases substantially, highlight-
(4) Intervention Gap — Lack of Adaptive, Flow-preserving ing the necessity of monitoring and managing cognitive demands
Support: Even when learner’s states are inferred, most systems during educational activities [7, 43, 45].
1219

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
2.2 Biosensors as Biomarkers for Personalized 3.1 Pre-study Survey
and Adaptive Learning A total of 66 participants (mean age = 24.3, range = 19-42) completed
Advances in multi-modal biosensing now enable non-intrusive an online survey. The sample included undergraduate and graduate
monitoring of learners’ cognitive and emotional states in real time. students, educators, and professionals in learning-focused roles
Pupillometry, for instance, provides reliable indices of mental ef- (63.3% male, 36.7% female). The survey examined participants’ AI
fort and attentional load, with pupil dilation correlating strongly usage frequency, perceived utility, preferred learning modalities,
with task difculty and processing demand [10, 45]. Heart rate vari- and desired personalization features.
ability (HRV) serves as a biomarker of stress and engagement by
capturing autonomic regulation [1, 39], while posture dynamics
and micro-movements indicate fatigue or disengagement [25, 48].
These physiological and behavioral signals ofer complementary
perspectives on the learner’s internal state however, existing ap-
proaches typically use these signals in isolation for ofine analytics
or post-hoc feedback rather than integrating them into closed-loop
adaptive systems [12]
2.3 From Rule-based Systems to LLMs: Toward
Multi-modal Personalization in Education
The integration of LLMs into educational technologies has revolu-
tionized learning through advanced natural language understand-
ing and generation capabilities [6, 27, 40]. Contemporary imple-
mentations leverage LLMs’ sophisticated reasoning processes to
adapt instructional approaches based on inferred knowledge states
and learning preferences [5, 57], however fail to address the tem- Figure 2: Participant openness to working with a personal-
poral and inferential gaps of adaptive support: feedback timing, ized AI learning assistant on a scale from 1-10. The distribu-
intervention intensity, and context awareness. The combination of tion shows strong receptivity, with 50 out of 66 participants
LLMs with wearable biosensors represents a particularly promising (75.7%) rating their openness at 7 or higher, and a median
direction, with prior studies demonstrating content adaptation and rating of 8.
limited learner modeling through physiological data integration
[1, 14, 15]. These models’ multi-modal processing capabilities fa-
3.1.1 AI Usage and Perception. Most participants (55.0%) used AI
cilitate the integration of diverse data sources, including textual,
tools daily and 38.3% several times per week. Nearly all respondents
visual, physiological, and behavioral metrics, enabling a more com-
(96.6%) found AI systems at least somewhat useful for learning, with
prehensive understanding of learners’ states [53, 57].
40.7% rating them extremely useful. ChatGPT was the most used
Despite these advances, most current LLM tutoring systems re-
platform (96.7%), followed by Claude (61.7%) and Gemini (30.0%).
main reactive, inferring progress only from textual responses rather
Participants viewed AI primarily as an on-demand explainer for
than multi-modal learner-state cues. They fail to address the tem-
complex problems, rather than a continuous learning companion,
poral and inferential gaps of adaptive support: feedback timing,
indicating opportunities for more proactive, context-aware assis-
intervention intensity, and context awareness [39, 54]. While prior
tance.
frameworks have explored content adaptation and limited learner
modeling [1, 29, 56], none combine real-time multi-modal biosens- 3.1.2 Learning Modality Preferences. Text-based materials re-
ing, cognitive fow-aligned adaptation, and meta-cognitive scafold- mained the most preferred learning modality (98.3%), though many
ing within a unifed architecture. GuideAI contributes to this tra- participants expressed interest in video (53.3%), image-based (51.7%),
jectory by operationalizing a context-aware, biosensor-augmented and audio (44.6%) content. Text was valued for self-paced control,
LLM framework that performs continuous learner-state inference while visual and auditory formats aided understanding of spatial or
and adaptive intervention at multiple temporal and cognitive scales, procedural concepts. As one participant noted, “Text lets me learn
extending prior work in both educational AI and intelligent user at my own speed, but diagrams and videos help me grasp complex
interfaces. ideas much faster” (P7). This preference underscores the impor-
tance of multi-modal learning environments that fexibly align with
3 Formative Assessment learners’ cognitive and perceptual needs.
To ground our system design in authentic learner needs, we con- 3.1.3 AI Learning Tools: Usage Paterns and Limitations. Partici-
ducted a formative study to translate broad challenges, limited pants primarily used AI tools to explain difcult concepts (91.7%),
personalization and lack of real-time adaptation into actionable, interpret code or mathematical problems (78.3%), and summarize
user-centered design goals. The assessment captured learners’ AI readings (73.3%). These fndings indicate that learners rely on AI
usage patterns, limitations of current tools, and expectations for systems during moments of cognitive friction rather than routine
adaptive interventions. study.
1220

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
Figure 3: Desired interventions from personalized AI (N = 66). Top priorities: personalized learning paths (68.2%), tailored
practice questions (68.2%), and learning style adaptation (65.2%). Nearly half (47.0%) wanted break reminders and alternative
methods. Multiple selections allowed.
However, participants identifed several persistent limitations. (3) Physiological Awareness: Strong interest in systems that can
About one-third (31.7%) cited a lack of personalization or adapta- detect struggles and suggest interventions indicates the value
tion to their learning style as a major shortcoming. Others noted of incorporating biosensory data.
excessive textual explanations (33.3%) or missing step-by-step rea- (4) Personalized Learning Paths: Respondents prioritized indi-
soning (25.0%). As participants described, systems often “keep ex- vidualized content sequencing based on their unique strengths
plaining at the same level even when I’m lost” (P12) or “can’t tell and weaknesses, supporting our biosensory-informed personal-
when an explanation isn’t landing” (P15). Nearly half (42.3%) re- ization approach.
ported abandoning AI assistance when it failed to adjust to their
confusion. These limitations highlight the absence of real-time These fndings highlighted the gap between current AI learning
learner-state awareness—precisely the challenge GuideAI addresses systems and learner needs, directly informing our GuideAI system
through multi-modal biosensing and adaptive feedback. design that integrates biosensory data for responsive, personalized
learning across multiple modalities.
3.1.4 Desired Interventions. When asked about desired capabilities
in AI learning assistants, participants expressed strong interest in
4 GuideAI Solution
adaptive interventions (Figure 2). Top-ranked features included per-
sonalized learning paths (68.3%), targeted practice questions (66.7%), Following our formative studies, we developed GuideAI, a person-
and adaptive recognition of learning styles (65.0%) (Figure 3). Over alized system that identifes challenges and support opportunities
half (50.0%) wanted systems capable of detecting struggle and sug- based on multi-modal cognitive and behavioral cues.
gesting breaks or alternative strategies. These fndings directly
informed GuideAI’s design goals—developing a system that dynam-
4.1 Overview
ically infers cognitive-afective state, modulates support timing and
intensity, and maintains learner engagement across modalities. The GuideAI pipeline (Figure 4) comprises three core components:
(1) A sensor module, that includes an external posture camera, pupil-
3.2 Design Implications tracker, wrist-worn wearable, and note-taking device to monitor a
learner’s physiological and behavioral state during digital learning
The formative assessment yielded four key design implications that
sessions. (2) A processing module that analyzes the captured data
guided GuideAI’s development:
streams to infer the learner’s engagement, cognitive workload, and
(1) Multi-modal Learning Support: Signifcant interest in image- afective state. (3) A reasoning and inference module that integrates
based, audio-based and video-based learning suggests the need contextual understanding with pedagogical strategies to suggest
for systems that seamlessly integrate and adapt across modali- timely interventions.
ties. We implemented GuideAI as a web-based platform that supports
(2) Real-time Adaptation: Users desire systems that can detect real-time learning and assessment of study behavior. The plat-
learning states and dynamically adjust content and pace accord- form supports cross-device compatibility, enabling data input from
ingly. tablets, mobile devices, and desktop systems.
1221

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
Figure 4: GuideAI System Architecture with three modules: Sensor Module (left) collects eye tracking, heart activity, posture,
and notes data. Processing Module (center) transforms raw signals into physiological and behavioral metrics. Inference Module
(right) integrates these to assess six cognitive dimensions (cognitive load, attention, engagement, understanding, stress, fatigue)
and deliver personalized interventions across learning modalities (text, image, audio, video).
4.2 Data Capture information about visual attention, cognitive load, and information
processing patterns. The Max-Health-Band from Maxim Integrated
[16] captures heart rate (HR) and heart rate variability (HRV) at
200 Hz, enabling assessment of autonomic nervous system activity
and stress levels.
An external posture camera captures upper body positioning, while
iPad screen recordings provide observational data on note-taking
behaviors. To manage time-synchronized data fow across sensors,
we use the Lab Streaming Layer (LSL) framework [28]. LSL en-
sures consistent time-stamping and low-latency data integration,
enabling real-time fusion of biosignals, posture analysis, and task
interaction data for constructing a temporally coherent model of
learners’ attention, afect, and cognitive efort.
4.3 Processing Module
4.3.1 Biosensors-based Pipeline. To infer users’ cognitive and afec-
Figure 5: Multi-modal biosensory setup integrating eye track-
tive states in real-time, our system integrates physiological signals
ing, heart rate monitoring, note-taking analysis, and posture
from pupillometry and HRV, extracted via biosensor processing
detection.
pipelines. The eye-tracking module tracks and analyzes pupil dila-
tion, saccades, and fxations, all of which have been demonstrated
In our experimental setup (Figure 5), GuideAI uses a multi-modal to refect cognitive load, arousal, and visual attention dynamics.
sensor confguration to collect real-time data from the learner. We Fixation durations correlate with working memory load and atten-
use the Pupil Core eye tracker from Pupil Labs [26] to capture pupil- tional allocation during scene perception and memory integration
lometry data, fxations, and saccadic movements at 60 fps, providing tasks [4, 19, 33]. By employing robust fxation-detection algorithms
1222

| IUI ’26, March 23–26, 2026, Paphos, Cyprus  |     |     |     |     |     |     | Shukla et al.  |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- |
[38, 47], the system parses gaze data into real-time attentional  traditional learning systems that present standardized content re-
patterns. Saccadic movements are also analyzed, ofering rapid tem- gardless of the learner’s cognitive and afective state.
poral markers of stimulus-driven attentional shifts [17, 18]. These
Threshold Calibration and Rationale. All intervention thresholds
signals are instrumental in detecting user interest, task engagement,
are defned relative to participant-specifc baselines, obtained
and transitions between visual targets.
during a 5-minute calibration phase prior to each session (Section
To assess autonomic nervous system activity, we implement a HRV
5.1.1). For each physiological channel, we compute standardized
processor that analyzes data from a wearable physiological sensor.
deviations using a Z-score formulation:
The heart activity signal is sampled at 200 Hz and processed in
r ea l - ti m e .  T h e   sy st e m   e xtr a c ts   s t a n d a rd  t im e- d o m a i n  H R V   fe a t u r es ,       −
|     |     |     |     |     | =  baseline |     | (2) |
| --- | --- | --- | --- | --- | ----------- | --- | --- |
fo c u s i ng   o n   p N N 5 0 ,  R M S S D ,   a n d   S D N N  m e t r ics   [ 8 , 1 3 ,  5 0 ].   T h e
baseline
pNN50 value measures the percentage of successive RR intervals
|     |     |     | where  |  is the real-time signal value, and  |     | baseline | ,  baseline  are  |
| --- | --- | --- | ------ | ------------------------------------ | --- | -------- | ----------------- |
difering by more than 50 milliseconds, with thresholds indicating
participant-specifc baseline statistics.
stress levels: <20 (high), 20-50 (moderate), >50 (low stress) [46, 59].  We defne moderate deviation at |  | ≥ 1.0 and pronounced
These HRV metrics are contextualized against individual baseline  deviation at |  | ≥ 1.5, consistent with prior cognitive load and
recordings to account for inter-individual diferences in resting  stress detection literature using pupillometry and HRV-based mark-
autonomic tone.
ers. These values were further validated through pilot sessions to
balance sensitivity against false-positive intervention triggering.
Raw Signal Processing and Feature Extraction. Raw biosignals
are processed in real-time using modality-specifc pipelines prior  Why Semantic State Abstractions Instead of Raw Numeric Streams.
to state inference. For pupillometry, raw pupil diameter streams  While raw physiological values (e.g., pupil diameter in millimeters
sampled at 60 Hz are frst smoothed using a rolling median flter
or HRV metrics) are informative, directly injecting high-frequency
to remove blink artifacts, followed by baseline normalization. Fixa-
numeric streams into LLM prompts introduces substantial noise
tions are detected using a velocity-threshold identifcation (I-VT)
and token inefciency. Instead, we convert processed signals into

method, where gaze velocity    is computed as:  semantic state descriptors (e.g., High Stress, Moderate Cognitive
  Load) that preserve interpretability while remaining stable over
√
|     | (Δ     )2  + (Δ   |   )2  |          |     |     |     |     |
| --- | ----------------- | ----- | -------- | --- | --- | --- | --- |
|     | =                 | (1)   | tim e .  |     |     |     |     |
|     |   Δ               |       |          |     |     |     |     |
T h is abstraction enables the LLM to reason over learner state
using cognitively meaningful constructs, improving robustness and
| where     and     represent the horizontal and vertical gaze positions  |     |     |     |     |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
controllability of generated interventions without requiring the
| at time   , respectively. Δ | =   −    −1 and Δ | =   −    −1 are  |     |     |     |     |     |
| --------------------------- | ----------------- | ---------------- | --- | --- | --- | --- | --- |
              model to infer semantics from raw numerical values.
| the gaze displacements along each axis, and Δ |     |  is the sampling  |     |     |     |     |     |
| --------------------------------------------- | --- | ----------------- | --- | --- | --- | --- | --- |
 <
interval between successive measurements. Samples with        4.4.1  Physiological State Inference Model.
are classifed as fxations, enabling computation of fxation duration
Baseline Normalization and Signal Quantifcation. Each partici-
and dispersion metrics.
pant undergoes a 60-second calibration phase in a neutral resting
For cardiovascular signals, RR intervals extracted from the wearable
|     |     |     | s t a te   t o  c | o m p u t e  p e r - s e | n s o r  b a s e l in e  d | is t r i b u t i o n s   ( | ,    ).  |
| --- | --- | --- | ----------------- | ------------------------ | -------------------------- | -------------------------- | -------- |
s e n so r   a r e   p r o c e s s e d   o v e r  sl i di n g  w i n d o w s  t o  c o m p u te   s t a n d a r d   b a s e ,    base,
|     |     |     |                  |                         |                           |                      | ,   −  ,    |
| --- | --- | --- | ---------------- | ----------------------- | ------------------------- | -------------------- | ----------- |
|     |     |     | R e a l- t i m e |  r e ad i n g s    ,    | a r e  s t a n d a r d iz | ed   a s    ,    =   | b a s e   . |
H R V  f e a t u r e s   in c l u d i n g   R M S S D ,  S D N N ,  a n d  p N N 5 0 . T h e s e   fe a t u r e s  ba s e ,
are normalized against participant baselines to account for inter- Dimension Scoring. Each of the six psychophysiological dimen-
| individual physiological variability.  |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
sions   (e.g., cognitive load, attention) is computed as a weighted
4.3.2  Vision-based Pipeline. GuideAI tracks learner engagement  average of the absolute deviation scores of its constituent sensor
|     |     |     |                  | Í                    |                          |                     |                          |
| --- | --- | --- | ---------------- | -------------------- | ------------------------ | ------------------- | ------------------------ |
|     |     |     | f e a t u r e s: |    =    = 1    ,   · | ,   · |  ,    | ,  w h e | re    i s  t h e  f | e a t u r e  w e ig h t  |
t h ro u g h   p o s tu r e  a n al y s i s  a n d  n o t e -t a k i n g   b e h a v i o r .   F o r   p o s t u r e      Í     ·   ,
|     |     |     |     | = 1   | ,     ,    |     |     |
| --- | --- | --- | --- | ----- | ---------- | --- | --- |
m o n it o ri n g ,  w e  u s e  M e d i a P ip e  [ 34 ]   to   a n a ly z e   s h o u l d e r   p o s i ti o n i n g ,   a n d     ,  ∈ [ 0 ,  1 ]  is   t h e   r e a l - t i m e   s i g n al  q u a li ty   s c o r e  b a s e d   o n  se n s or

neck alignment, and back straightness, categorizing posture into  confdence. Weights were derived from meta-analytic efect sizes
four states: ideal (90-100%), average (75-89%), below average (60- in psychophysiology literature. For example, pupil dilation’s high
74%), and poor (<60%).
weight for cognitive load refects its documented large efect size
  = 0.8–1.2) in working memory paradigms [42].
| For note-taking analysis, an iPad M1 captures screenshots at  |     |     | (   |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
60-second intervals. These are processed using OpenAI’s gpt-4o
Intervention Triggering. An intervention is triggered when a di-
model to analyze handwritten notes, providing qualitative feed-
|                                                                     |     |     | mension score  |  surpasses a predefned threshold (e.g., > 1.5 for  |     |     |     |
| ------------------------------------------------------------------- | --- | --- | -------------- | -------------------------------------------------- | --- | --- | --- |
| back and a correctness score (0-1). This integration captures both  |     |     |                |                                                    |     |     |     |
physical engagement and cognitive processing refected in learning  "Moderate Deviation") for a sufcient duration (temporal persis-
artifacts.  tence > 10s), a policy designed to distinguish meaningful state
changes from transient noise.
4.4  Personalized Intervention Module
4.4.2  LLM Integration and Tone-adaptive Intervention Delivery. The
Our personalized learning system employs an intelligent interven- LLM serves as the primary intervention delivery mechanism, with
tion module that continuously analyzes the learner’s state and  responses enhanced by biosensory context. When biosensors de-
delivers adaptive support based on multi-modal biosensing data.  tect elevated stress, the system adopts a supportive tone with
This adaptive architecture represents a signifcant departure from  patience-signaling language. During high engagement, it increases
1223

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
(a) High Cognitive Load Detection (b) Low Understanding Intervention
(c) High Attention State Recognition (d) Stress Regulation
(e) Low Engagement Management (f) Fatigue Detection and Response
Figure 6: GuideAI’s biosensing-driven intervention framework linking physiological triggers to adaptive strategies. (a) High
cognitive load detected via pupil dilation, elevated heart rate, and fxation duration triggers content pausing and chunking; (b)
Understanding difculties from erroneous notes initiate conceptual correction; (c) High attention states enable complexity
increases; (d) Stress detection triggers graduated interventions from simplifcation to breathing exercises; (e) Low engagement
adapts content pacing; (f) Fatigue prompts strategic breaks. This represents a subset of GuideAI’s real-time pedagogical
adaptations.
Socratic questioning. For fatigue, it becomes more energetic and triggers directives to simplify explanations, reduce information
concise. Tone adaptation operates across multiple linguistic dimen- density, and incorporate learning aids.
sions—sentence complexity, encouragement frequency, explanation An intervention is triggered only when: (i) the deviation magni-
directness, and metaphor usage—calibrated to physiological indica- tude exceeds threshold, (ii) model confdence exceeds 0.6, and (iii)
tors. This ensures interventions address both content modifcations deviation persists across three consecutive windows to suppress
and optimal presentation for the learner’s current state. transient noise.
The system includes targeted directives based on detected states
that guide response generation. For instance, high cognitive load
4.4.3 Learning Mode–Specific Intervention Mechanisms. GuideAI
adapts interventions to the representational properties of each
1224

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
Figure 7: Comparison of standard LLM (left) vs. GuideAI (right) responses. GuideAI detects a misconception in the learner’s
notes (unlabeled vs. labeled data), identifes high stress levels, and delivers a tone-adaptive intervention with conceptual
correction and breathing guidance to address both cognitive and afective states.
medium, recognizing that cognitive load and comprehension chal- this concept might be challenging. I’ll break this down into smaller
lenges manifest diferently across text, image, audio, and video. components and explain each part more deliberately.”
This design choice follows evidence from multi-modal learning re- (4) Video-based learning: Playback is adaptively controlled, with
search that instructional efectiveness depends on aligning support pauses introduced at points of detected confusion, clarifying
strategies with modality-specifc afordances. The four modes were questions embedded, and captions or overlays added for empha-
selected based on learner preferences in our formative study, and sis. Example: [System automatically pauses video] “Let’s pause
the interventions were tailored accordingly. here to ensure this critical concept is clear. This segment explains
a fundamental principle we’ll build upon.”
(1) Text-based learning: Interventions reduce extraneous load These modality-specifc mechanisms illustrate how GuideAI
by dynamically restructuring content. For instance, dense text leverages the afordances of each medium to scafold comprehen-
is segmented into shorter paragraphs, converted into bullet sion, regulate pacing, and maintain learner engagement.
lists, or supplemented with refective prompts. Example: “Let
me organize this information diferently to make the relationships 4.4.4 Adaptive Interventions. GuideAI employs a tiered adaptive in-
clearer: First, the defnition of sampling distribution...” tervention framework across four categories: cognitive–attentional,
(2) Image-based learning: Complex visuals are progressively dis- physiological, comprehension-oriented, and challenge-enhancement.
closed, annotation density is adapted to cognitive capacity, and This structure draws on cognitive load theory, self-regulation re-
gaze-contingent highlighting draws attention to critical regions. search, and the principle of keeping learners within their zone of
Example: “Looking at this visualization of a sampling distribu- proximal development (ZPD).
tion, notice how the shape changes as sample size increases. I’ll (1) Cognitive and Attentional Interventions: For moderate cog-
present the sequence of images in a more structured order to help nitive load, GuideAI restructures content with clearer structure
clarify the relationship.” or contextual cues (“Let me highlight the key relationships.”). Un-
(3) Audio-based learning: Speech pacing and intonation are mod- der critical overload, it distills material to core ideas. GuideAI
ulated in response to overload signals. Strategic pauses and counters attention lapses with curiosity prompts (“What if we
summarizations aid temporal integration, while guided breath- doubled the sample size?”) or short physical resets (“Take a quick
ing cues are inserted during elevated stress. Example: “I notice stretch before we continue.”).
1225

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
(2) Physiological Interventions: GuideAI responds to stress with 5.1.2 Study Conditions. We developed a custom web-based in-
reassurance (“Many learners fnd this challenging at frst—let’s terface, ensuring a consistent user experience across condi-
break it down step by step.”) for moderate levels, and brief breath- tions. Based on our formative study, the system utilized Ope-
ing exercises (“Let’s pause briefy—inhale 4, hold 4, exhale 6.”) nAI’s models (gpt-4o-mini for dialogue, gpt-4o for vision, and
for high stress. Fatigue triggers shorter segments or breaks gpt-4o-mini-tts for audio) for their balance of quality and la-
depending on severity. tency. The interface design was identical in both conditions to
(3) Comprehension-oriented Interventions: When understand- isolate the efects of the adaptive interventions.
ing is low, GuideAI provides adaptive scafolding. Moderate gaps Participants each experienced two conditions in a counterbal-
trigger multiple explanation styles—formal, intuitive, or com- anced, within-subjects design. To control for content variability,
parative. Critical gaps prompt frst-principles reconstruction, topic difculty was matched, and sessions were spaced by at least
moving from concrete examples to abstract concepts (“Let’s re- 24 hours to mitigate fatigue. The two conditions were:
build this from a tangible example before the formal defnition.”). (1) Control (Non-adaptive Baseline): Participants used a non-
(4) Challenge-enhancement Interventions: Under-challenge personalized LLM-based learning system with an identical sen-
states (low load, high engagement) trigger increased task com- sor confguration to the experimental condition but without
plexity to sustain engagement within the ZPD. Moderate cases adaptive interventions or content personalization.
reduce scafolding or add advanced applications; substantial (2) Intervention (GuideAI): Participants used the fully-adaptive
ones extend to theoretical or synthesis prompts (“How might system, where content, pacing, and tone were dynamically per-
this apply to stratifed sampling in heterogeneous populations?”). sonalized in real-time based on the multi-modal analysis of their
(5) Implicit vs. Explicit Framing: GuideAI adjusts feedback style physiological and behavioral signals.
based on context. Implicit adaptations (e.g., simplifying expla-
This design allows us to test our primary hypothesis by measur-
nations) are used for moderate deviations, while explicit ac-
ing the holistic efect of our integrated, biosensor-aware support
knowledgments of stress or fatigue are reserved for persistent
system against a rigorously controlled and representative baseline.
or multimodally confrmed states. This ensures sensitivity to
learner diferences while supporting metacognitive awareness. 5.1.3 Learning Modes. Each condition consisted of four sequential
learning modes designed to engage diferent learning modalities,
which were selected based on the preferences identifed in our
5 Study Design and Evaluation formative study:
(1) Text-based Learning: Participants studied structured text con-
5.1 Procedure
tent on their assigned topic.
To evaluate GuideAI’s efectiveness, we conducted a controlled (2) Image-based Learning: Participants engaged with topic-
comparison study with 25 participants (13 male, 12 female; age appropriate visual content, where text explanations were sup-
range 18-42, mean 24.7 years). We employed a within-subjects plemented with illustrative images and diagrams. The content
design with counterbalanced order, wherein each participant was specifcally selected to beneft from visual reinforcement,
interacted with both the GuideAI system and a non-personalized for example, statistical distribution graphs for probability con-
control condition utilizing a standard LLM. cepts. Each visual element included detailed explanations of its
components.
This study is intended as a preliminary validation of GuideAI (3) Audio-based Learning: Participants engaged in audio-based
under controlled conditions, focusing on STEM-oriented learning dialogue with the LLM, asking questions and receiving spoken
tasks where outcomes can be assessed more objectively. General- responses about the topic, creating a more interactive learning
ization to more subjective domains is explored through hypotheses experience.
and discussion rather than empirical evaluation in this study. (4) Video-based Learning: Participants watched an educational
video on the topic, with the ability to ask the system clarifying
questions about the video content.
5.1.1 Participant Selection and Preparation. Participants were care-
fully screened to ensure they had no prior knowledge of the study 5.1.4 Assessment Methods. After each learning mode, participants
topics. The sample included diverse educational backgrounds across completed:
undergraduate, master’s, and doctoral programs. Each participant (1) Cognitive Load Assessment: NASA Task Load Index (NASA-
provided written informed consent for biosensing data collection TLX) [21] on a 7-point Likert scale measuring perceived mental
and analysis, with all data anonymized to protect privacy. Topics demand, efort, temporal demand, physical demand, perfor-
were selected from diverse domains including statistics (probabil- mance and frustration [30].
ity vs. sampling distributions), machine learning (supervised vs. (2) Knowledge Assessment: Multiple-choice questions test-
unsupervised learning), and biology (innate vs. adaptive immu- ing factual recall and conceptual understanding through
nity) [22, 51, 55]. Prior to each session, participants underwent application-based problems, with similar difculty across all
a calibration process establishing baseline physiological metrics, topics.
including eye-tracker calibration, ideal posture positioning, and (3) Subjective Evaluation: Participants rated their experience on
heart rate/HRV baseline measurements. These baselines served as 7-point Likert scales covering perceived focus, adaptation to
reference points for adaptive thresholds in the GuideAI condition. learning pace, quality of examples, and overall satisfaction.
1226

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
For the GuideAI condition, participants additionally evaluated the
quality and appropriateness of interventions received. All partici-
pants provided qualitative feedback on both systems at the conclu-
sion of each learning session.
5.2 Findings
Our evaluation demonstrates that GuideAI signifcantly improves
both learning outcomes and cognitive experience compared to the
non-adaptive control condition. Results are reported across three
dimensions: (1) cognitive load and user experience, (2) learning
performance, and (3) subjective evaluations.
5.2.1 Cognitive Load and User Experience. NASA-TLX analysis re-
vealed consistent reductions in cognitive load across all modalities
with GuideAI (Figure 8). Participants reported lower mental demand
(Δ = 0.49,  < 0.05), physical demand (Δ = 0.23,  < 0.05), efort
(Δ = 0.28,  < 0.05), and frustration (Δ = 0.54,  < 0.05), alongside
higher perceived performance (Δ = 0.34,  < 0.05). These results
indicate reduced cognitive burden and improved self-assessed learn-
ing efcacy.
7
6
5
4
3
2
1
Mental Demand Physical Demand Temporal Demand Performance Effort Frustration Level
erocS
• Video-based: Lower physical demand (Δ = 0.33,  < 0.05)
but higher temporal demand (Δ = 0.60,  < 0.05), likely
refecting real-time playback adjustments synchronized to
cognitive state (Figure 9d).
Participants’ qualitative feedback reinforced these fndings:
“The interventions were helpful as they were monitoring
stress, focus, etc. and trying to reduce the complexity
of concepts on the go, which helped in understanding
things in a simpler manner.” — P7
“I genuinely appreciated how it slowed down when I was
getting overwhelmed and ofered simpler explanations.
The personalized pacing made a noticeable diference
in how much information I was able to retain.” — P20
5.2.2 Learning Performance. GuideAI produced signifcant learn-
ing gains across modalities for both problem-solving and recall
tasks.
• Problem-solving: Text-based 75% vs 52%, Image-based 78%
vs 48%, Audio-based 70% vs 59% (  < 0.05); Video-based 72%
vs 68% (n.s.). The largest gain (Δ = 30 percentage points)
occurred in image-based learning (Figure 10b).
NASA-TLX Metrics (All Phases) • Recall: Image-based 82% vs 62%, Audio-based 70% vs 52%
C G o u n id t e ro A l I (  < 0.05); Text-based 65% vs 64% and Video-based 72% vs
Significant (p < 0.05)
70% (Figure 10a).
Performance improvements aligned with reduced cognitive load:
for instance, in image-based learning, higher recall corresponded
with lower mental (Δ = 0.51) and temporal demand (Δ = 0.59).
Audio-based gains in problem-solving paralleled reduced frustra-
tion (Δ = 1.14) and increased perceived performance (Δ = 0.77).
Across all modalities, GuideAI yielded a mean improvement of 16.5
percentage points in problem-solving and 10.3 percentage points in
recall, indicating stronger support for deep conceptual integration
Statistical test: Wilcoxon rank-sum test (p < 0.05) than rote memorization. These fndings validate that biosensor-
driven adaptive interventions enhance comprehension by reducing
Figure 8: Comparison of NASA-TLX metrics between control
cognitive burden and aligning feedback with learner state.
and GuideAI conditions across all learning modes. Lower
scores are better for all metrics except Performance, where 5.2.3 Subjective Evaluation. Participants’ subjective ratings (Ta-
higher scores indicate better perceived success. Gray high- ble 1) corroborated the quantitative results. Four dimensions
lighting indicates statistically signifcant diferences (p < 0.05) showed statistically signifcant improvements in the GuideAI con-
using Wilcoxon rank-sum tests [44], which were used due to dition:
the non-normal distribution and paired nature of the data. • Focus and Attention:  = 5.60,   = 1.25 vs Control
= 4.85,   = 1.34,  = 0.0418.
Learning mode-specifc analysis revealed how GuideAI infu- • Content Personalization:  = 5.55,   = 1.32 vs Control
enced cognitive load across diferent learning modalities (Figure  = 4.90,   = 1.26,  = 0.0362.
9): • Adaptive Pacing:  = 5.40,   = 1.28 vs Control  = 4.65,
= 1.22,  = 0.0322.
• Text-based: Largest reduction in cognitive load, particularly
• Perceived Learning:  = 5.50,   = 1.16 vs Control  =
in mental (Δ = 0.65,  < 0.05) and temporal demand (Δ =
4.75,   = 1.18,  = 0.0402.
0.96,  < 0.05), suggesting strong alignment between pacing
interventions and reading-intensive content (Figure 9a). Positive but non-signifcant trends were observed for task chal-
• Image-based: Signifcant decreases in mental (Δ = 0.51, lenge (  = 0.17) and frustration (  = 0.25). Overall enjoyment was
< 0.05) and temporal demand (Δ = 0.59,  < 0.05); perfor- comparable across conditions (GuideAI:  = 5.45,   = 1.38; Con-
mance gains were moderate (Figure 9b). trol:  = 5.20,   = 1.30). Qualitative feedback further illustrated
• Audio-based: Higher perceived performance (Δ = 0.77, increased engagement and perceived adaptivity:
< 0.05) and reduced frustration (Δ = 1.14,  < 0.05), “Before using this system, I’d often give up on difcult
indicating improved engagement through adaptive dialogue material. The way it broke concepts down when it de-
pacing (Figure 9c). tected my confusion gave me capabilities I didn’t have
1227

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions  IUI ’26, March 23–26, 2026, Paphos, Cyprus
|       | Text-based Learning |                        |       | Image-based Learning |                        |
| ----- | ------------------- | ---------------------- | ----- | -------------------- | ---------------------- |
| 7     |                     |                        | 7     |                      |                        |
|       |                     | Control                |       |                      | Control                |
|       |                     | GuideAI                |       |                      | GuideAI                |
| 6     |                     |                        | 6     |                      |                        |
|       |                     | Significant (p < 0.05) |       |                      | Significant (p < 0.05) |
| 5     |                     |                        | 5     |                      |                        |
| erocS |                     |                        | erocS |                      |                        |
| 4     |                     |                        | 4     |                      |                        |
| 3     |                     |                        | 3     |                      |                        |
| 2     |                     |                        | 2     |                      |                        |
| 1     |                     |                        | 1     |                      |                        |
Mental Demand Physical Demand Temporal Demand Performance Effort Frustration Level Mental Demand Physical Demand Temporal Demand Performance Effort Frustration Level
| Statistical test: Wilcoxon rank-sum test (p < 0.05) |                      |                        | Statistical test: Wilcoxon rank-sum test (p < 0.05) |                      |                        |
| --------------------------------------------------- | -------------------- | ---------------------- | --------------------------------------------------- | -------------------- | ---------------------- |
|                                                     | (a)                  |                        |                                                     | (b)                  |                        |
| 7                                                   | Audio-based Learning |                        | 7                                                   | Video-based Learning |                        |
|                                                     |                      | Control                |                                                     |                      | Control                |
|                                                     |                      | GuideAI                |                                                     |                      | GuideAI                |
| 6                                                   |                      | Significant (p < 0.05) | 6                                                   |                      | Significant (p < 0.05) |
| 5                                                   |                      |                        | 5                                                   |                      |                        |
| erocS                                               |                      |                        | erocS                                               |                      |                        |
| 4                                                   |                      |                        | 4                                                   |                      |                        |
| 3                                                   |                      |                        | 3                                                   |                      |                        |
| 2                                                   |                      |                        | 2                                                   |                      |                        |
Mental Demand 1 Physical Demand Temporal Demand Performance Effort Frustration Level Mental Demand 1 Physical Demand Temporal Demand Performance Effort Frustration Level
| Statistical test: Wilcoxon rank-sum test (p < 0.05) |      |     | Statistical test: Wilcoxon rank-sum test (p < 0.05) |      |     |
| --------------------------------------------------- | ---- | --- | --------------------------------------------------- | ---- | --- |
|                                                     | (c)  |     |                                                     | (d)  |     |
Figure 9: NASA-TLX metrics across learning modes comparing GuideAI vs. control. (a) Text-based learning showed signifcant
reductions in mental demand, temporal demand, and frustration; (b) Image-based learning reduced mental and temporal
demand via eye-tracking adaptations; (c) Audio-based learning showed the largest performance improvements with reduced
mental demand and frustration; (d) Video-based learning showed lower physical demand but higher temporal demand due to
adaptive pacing. Gray shading indicates signifcance (p < 0.05, Wilcoxon rank-sum). Lower is better except Performance (higher
is better).
100 Recall Performance Scores by Phase 100 Problem-solving Performance Scores by Phase
|              |     | Control                |              |     | Control                |
| ------------ | --- | ---------------------- | ------------ | --- | ---------------------- |
|              |     | GuideAI                |              |     | GuideAI                |
|              |     | Significant (p < 0.05) |              |     | Significant (p < 0.05) |
| 80           |     |                        | 80           |     |                        |
| )%( erocS 60 |     |                        | )%( erocS 60 |     |                        |
| 40           |     |                        | 40           |     |                        |
| 20           |     |                        | 20           |     |                        |
0 Text-based Learning Image-based Learning Audio-based Learning Video-based Learning 0 Text-based Learning Image-based Learning Audio-based Learning Video-based Learning
Statistical test: Wilcoxon rank-sum test (p < 0.05) Statistical test: Wilcoxon rank-sum test (p < 0.05)
| (a) Recall performance  |     |     | (b) Problem-solving performance  |     |     |
| ----------------------- | --- | --- | -------------------------------- | --- | --- |
Figure 10: Learning performance comparing Control vs. GuideAI. (a) Recall performance with signifcant improvements in
image-based and video-based learning. (b) Problem-solving performance with signifcant gains in image-based and audio-based
learning. GuideAI outperformed control across all modalities. Error bars: standard error. Gray shading: p < 0.05 (Wilcoxon
rank-sum).
1228

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
Table 1: Comparison of Control and GuideAI Groups on Likert Scale Responses ranging from 1 (Strongly Disagree) to 7 (Strongly
Agree)
Question Control GuideAI U- p- Efect
Mean/SD Mean/SD Statistic value Size
I found the learning task to be challenging using this 4.65 / 1.22 4.30 / 1.18 159.0 0.1672 0.29
learning system
I felt frustrated or overwhelmed while using the learning 4.10 / 1.32 3.75 / 1.28 165.5 0.2481 0.27
system
I was able to stay focused throughout the session with 4.85 / 1.34 5.60 / 1.25 127.5 0.0418 -0.48
the learning system
I enjoyed the learning task with the learning system 5.20 / 1.30 5.45 / 1.38 170.0 0.3621 -0.19
The examples provided by the learning system were 4.90 / 1.26 5.55 / 1.32 124.0 0.0362 -0.45
tailored to me and easy to follow
The learning system adapted well to my learning pace 4.65 / 1.22 5.40 / 1.28 123.0 0.0322 -0.47
I feel I understood the topic better after using this learn- 4.75 / 1.18 5.50 / 1.16 126.0 0.0402 -0.49
ing system
Note: Statistical analysis includes the U-statistic, p-value from the Wilcoxon rank-sum tests, and efect size (Cohen’s d). Negative efect sizes indicate that GuideAI
condition had a higher mean value than the Control condition.
Table 2: Additional Questionnaire Responses from the granularity of real-time difculty calibration. Qualitative feedback
GuideAI Group on Personalized Interventions substantiated these fndings. Participants emphasized the utility of
physiological regulation cues, such as breathing or posture prompts,
Question GuideAI Mean/SD in managing stress and sustaining focus:
Helped me understand the topic more 4.71 / 0.68
“I liked when it prompted me to take deep breaths to
clearly
control my heartbeat. It helped me relax and refocus on
Responded promptly to my needs 5.50 / 0.75
the task when I was feeling overwhelmed by the content.”
Provided examples that made concepts 4.75 / 1.28
— P8
easier to grasp
Positively impacted my task performance 5.25 / 0.58 “It was good and I liked this learning system because
Personalization 5.00 / 0.66 when I study normally, I don’t notice my posture. Hav-
Made learning experience more engaging 5.33 / 0.47 ing something remind me helped me stay comfortable
Adjusted based on my mistakes or strug- 4.43 / 0.55 and focused for longer periods.” — P15
gles
5.3 Ablation Study
Note: Values measured on a 7-point Likert scale where higher values indicate
To assess the individual efectiveness of GuideAI’s adaptive mech-
stronger agreement.
anisms, we performed an ablation study on the four intervention
types detailed in Section 4.4.5’s Adaptive Interventions framework.
before. I could actually stay with the material instead Specifcally, we isolated: cognitive optimization (the content restruc-
of getting lost.” — P4 turing and complexity adjustments described under "Cognitive and
Attentional Interventions"), physiological intervention (the breath-
5.2.4 Interventions Evaluation. Participants in the GuideAI condi- ing and posture guidance from "Physiological Interventions"), atten-
tion rated biosensor-driven interventions positively across all di- tion redirection (the focus management strategies from "Cognitive
mensions (Table 2). The highest ratings were observed for system and Attentional Interventions"), and tone-adaptive communication
responsiveness (  = 5.50,   = 0.75) and enhanced engage- (the afective language modulation described in Section 4.4.2).
ment (  = 5.33,   = 0.47), indicating strong appreciation for
GuideAI’s ability to detect and respond to cognitive-afective shifts 5.3.1 Methodology. For each intervention category, we calculated
in real time. Participants also rated performance impact highly improvement scores by comparing NASA-TLX metrics in trials
(  = 5.25,   = 0.58), suggesting that interventions efectively sup- where that intervention was active versus control trials (no inter-
ported comprehension and task progress rather than functioning vention) for the same participant.
as peripheral features. The improvement score is defned as the within-subject difer-
Personalization quality (  = 5.00,   = 0.66) and conceptual ence in NASA-TLX ratings (1-7 scale) between intervention and
clarity (  = 4.71,   = 0.68) were consistently endorsed, confrm- control trials, averaged across all six NASA-TLX dimensions. In in-
ing that biosensory adaptations successfully aligned with individual stances where multiple interventions were triggered simultaneously
learning needs. The comparatively lower score for error-based (approx. 12% of cases), the intervention associated with the highest
adjustments (  = 4.43,   = 0.55) indicates scope to refne the deviation score relative to baseline was prioritized for the analysis.
1229

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
Figure 11: NASA-TLX improvement scores by intervention category. Cognitive optimization shows strongest improvements;
attention redirection excels at performance enhancement. Error bars: SE.
This approach isolates the primary driver of the state change while 5.3.3 Key Findings. Cognitive optimization emerges as the primary
accounting for the system’s hierarchical decision-making process. driver of GuideAI’s efectiveness. This validates the importance
of real-time content adaptation based on cognitive load indica-
5.3.2 Results. Analysis of intervention logs revealed the distribu- tors. Attention redirection provides crucial performance benefts
tion of system actions per session: Cognitive Optimization was for maintaining engagement, while physiological interventions
the most frequently triggered mechanism (  = 5.2 times/session), serve as stress modulators. The synergistic efects demonstrate that
refecting the continuous need for micro-adjustments in content GuideAI’s multi-modal approach provides benefts beyond individ-
complexity to maintain the zone of proximal development. This was ual interventions in isolation, supporting the integrated system
followed by Attention Redirection (  = 3.8) and Tone-Adaptive design.
Communication (  = 3.1). Physiological Intervention was the least
frequent (  = 1.2), validating our hierarchical design which re- 6 Discussion
serves these explicit, fow-breaking interruptions (e.g., breathing
GuideAI demonstrates the potential of biosensor-augmented per-
exercises) only for sustained high-stress states to preserve learn-
sonalized learning to enhance educational outcomes and reduce
ing momentum. As shown in Figure 11, cognitive optimization
yielded the largest reductions in mental demand (0.49 ± 0.10), efort cognitive load. Integrating real-time physiological data with adap-
(0.31 ± 0.08), and frustration (0.52 ± 0.07). Attention redirection tive content delivery enables a responsive and efective learning
efectively reduced temporal demand (0.39±0.13) and improved per- environment. This section discusses broader implications, limita-
ceived performance (0.49 ± 0.13). Physiological regulation produced tions, and directions for future work.
moderate but consistent frustration reductions (0.58 ± 0.15), while
6.1 Multi-modal State-aware Learning
tone-adaptive communication most strongly reduced frustration
(0.72 ± 0.11) but showed smaller efects on other dimensions. Results show signifcant learning improvements across modalities,
The analysis revealed important synergistic efects between in- especially in audio-and image-based learning, suggesting modality-
tervention types. Combining cognitive optimization with attention specifc optimization. GuideAI’s adaptive mechanisms facilitate
redirection produced amplifed benefts beyond individual efects, higher-order cognition, with stronger efects on problem-solving
particularly for mental demand reduction (combined: 0.67 vs. sum than recall. These fndings extend cognitive load theory through
of individual: 0.58). real-time physiological monitoring, demonstrating the feasibility
1230

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
of state-aware systems that adapt to attention, stress, and cognitive observed occasional instances where the LLM generated plausible
fuctuations with minimal latency. but factually incorrect explanations, particularly when responding
While our evaluation focused on STEM-oriented tasks, the under- to edge case questions. This highlights the need for content verif-
lying state-aware adaptation framework is not inherently domain- cation mechanisms and domain-specifc knowledge guardrails in
specifc. Similar benefts may extend to non-technical subjects such educational applications of LLMs [24].
as the humanities, social sciences, language learning, and creative
6.2.4 Longitudinal Study Considerations. Our evaluation focused
disciplines, where learning often depends more on sustained at-
on immediate learning efects within controlled sessions rather than
tention, interpretation, and refection than on binary notions of
longitudinal outcomes. The lack of long-term assessment leaves
correctness. In these contexts, learning quality may be better cap-
open questions about knowledge retention over time and the po-
tured through engagement-oriented indicators, such as reading
tential development of dependency on adaptive interventions.
dwell time, interaction rhythm, or refective note-taking—rather
than accuracy-based metrics, suggesting that adaptive success may 6.2.5 Intervention-specific Efectiveness. While our system imple-
be operationalized diferently across domains. mented various intervention types, we did not systematically evalu-
ate their relative efectiveness. Participant feedback indicated vary-
6.2 Limitations and Challenges ing preferences for diferent intervention strategies, with physiolog-
Despite the promising results, several important limitations must ical regulation features (e.g., breathing guidance, posture correction)
be acknowledged: receiving particularly positive mentions, while explicit cognitive
state notifcations sometimes increased anxiety rather than alle-
6.2.1 Privacy and Data Security Concerns. The collection of viating it. More granular analysis of intervention-specifc efects
biosensing data raises signifcant privacy considerations. While would help optimize future implementations.
our study implemented data minimization principles and secure
encryption protocols, broader deployment would require robust 6.2.6 Sample Size and Scope of Validation. The present study
privacy frameworks to protect sensitive physiological information. should be interpreted as a preliminary validation of GuideAI rather
Future implementations must address questions around data own- than a conclusive assessment of its efectiveness across populations.
ership, storage limitations, and user control over their physiological While the sample size was sufcient to observe consistent within-
data. The trade-of between personalization benefts and privacy subject trends and statistically meaningful efects under controlled
risks necessitates careful ethical consideration in system design. conditions, it limits the generalizability of the fndings. Larger and
more diverse cohorts are required to evaluate robustness across
6.2.2 Technical Feasibility and Deployment Constraints. Our cur- demographic groups, learning styles, and prior knowledge levels.
rent implementation requires specialized hardware including eye- Future work should prioritize scaled evaluations to validate external
tracking devices, wearable sensors, and cameras, along with calibra- applicability and reduce sampling bias.
tion procedures and controlled environments that limit deployment
in typical educational settings. GuideAI’s efectiveness relies on ac- 6.3 Future Directions
curate physiological measurements, making it vulnerable to sensor
Building on our fndings and addressing the limitations identifed,
errors and calibration issues. During testing, we observed that pupil-
we propose several promising directions for future research:
lary measurements were occasionally afected by ambient lighting
(1) Accessible Sensing Technologies. Future work should focus
changes, while HRV readings showed sensitivity to minor physical
on developing cost-efective and unobtrusive sensing solutions
movements. The complexity of multi-modal sensor integration and
leveraging ubiquitous devices such as webcams for gaze track-
real-time processing demands substantial computational resources,
ing and smartwatches for HRV measurement. Such scalable
making the system less feasible for individual learners or resource-
alternatives could democratize biosensor-enhanced learning
constrained institutions. These technical and practical constraints
across diverse educational contexts.
highlight the gap between laboratory validation and real-world
(2) Longitudinal Learning Efects. Extending evaluation beyond
educational deployment.
short-term sessions to longitudinal studies can reveal sustained
In scenarios where dedicated physiological sensors are unavail-
efects on retention, metacognitive strategy development, and
able, future versions of GuideAI could leverage interaction-level
learner engagement. Examining how system familiarity and
behavioral signals as proxy indicators of learner state. Patterns such
trust evolve over time will clarify the durability of adaptive
as time-on-task (dwell time), mouse cursor movement dynamics,
intervention benefts.
response latency, and interaction rhythm have been shown to re-
(3) Learner-confgurable Interventions. Mixed qualitative feed-
late to user attention, cognitive efort, and stress. While noisier and
back underscores the need for user agency in adaptive systems.
less direct than physiological biosignals, these interaction-derived
Allowing learners to confgure intervention frequency, type
proxies enable sensor-light or sensor-free deployments and sup-
(implicit vs. explicit), and visibility could enhance comfort, miti-
port a graceful degradation of adaptivity in resource-constrained
gate over-reliance, and align adaptive strategies with individual
or privacy-sensitive environments [23, 36, 49, 52].
learning preferences.
6.2.3 LLM Hallucinations and Content Reliability. While we im- (4) Designing Transparent Adaptive Interventions. While
plemented guided prompts and structured reasoning frameworks GuideAI internally tracks the signals and conditions that trig-
to mitigate LLM hallucinations, the risk of generating inaccurate ger adaptive interventions, this information is not currently
or misleading content remains a concern. During our study, we exposed to learners in order to avoid inducing self-monitoring
1231

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
bias or anxiety. Future iterations should explore selective and the integration of additional biosignals or contextual factors could
user-controlled ways of communicating the rationale behind further refne the system’s understanding of learner states. Fu-
interventions (e.g., indicating that an adjustment was made due ture iterations could also investigate the system’s performance
to signs of increased cognitive load), balancing transparency across a wider variety of learning domains and task types beyond
with minimal disruption to the learning experience. those tested. Finally, addressing potential usability and privacy
concerns associated with continuous biosensing, perhaps through
7 Ethical Considerations on-device processing or alternative sensing methods, will be crucial
for broader adoption. This work represents a step toward truly
Our study’s use of biosensory data followed a robust ethical frame-
cognition-aware educational technology, adaptable to the dynamic
work with ethics committee approval, centered on data minimiza-
state of individual learners.
tion, user control, and secure processing.
The research adhered to principles of informed consent, privacy
(1) Anonymization and Minimization. All data was immedi-
protection, risk minimization, and data security. All physiological
ately anonymized with a participant ID. Raw sensor data was
and behavioral data were anonymized immediately upon collection,
stored locally only for the session and permanently deleted after
with personal identifers replaced by participant codes (P1-P25).
the extraction of anonymized features (e.g., mean HRV), which
Data were encrypted and stored on secure servers with restricted
were retained for analysis.
access, to be retained only for the period necessary for research
(2) Transparency and Consent. Participants were fully informed
validation.
about the data being collected and its purpose. A persistent
The research complied with the ACM Code of Ethics and Profes-
on-screen indicator showed when monitoring was active, and
sional Conduct, The Declaration of Helsinki, and applicable local
participants could withdraw consent at any time to have their
regulations governing human subjects research.
data immediately deleted.
(3) Privacy and Future Directions.To mitigate privacy risks from
9 GenAI Usage Disclosure
third-party LLM APIs, our system transmitted only anonymized,
feature-extracted data (such as summary statistics or note tran- The authors used generative AI language models (Claude by An-
scriptions) rather than raw sensor streams. For real-world de- thropic and ChatGPT by OpenAI) solely for better phrasing and
ployment, we strongly advocate for prioritizing on-device pro- language standardization for consistency with ACM publication
cessing to ensure sensitive biosensory data never leaves the standards. No generative AI was used for research design, data
user’s device, thus maximizing privacy and user trust. analysis, fgure generation, literature review, or writing of original
(4) Research Involving Human Participants and Subjects This content. All intellectual contributions, experimental work, and sub-
research involved human participants and was conducted in stantive writing were produced entirely by the authors, who take
accordance with ethical principles and applicable regulations. full responsibility for the accuracy and integrity of this work.
The study was approved by our institution’s ethics committee
prior to data collection. All 25 participants provided informed Acknowledgments
consent after being fully informed about the study’s purpose,
The authors are thankful to Harish and Bina Shah School AI &
procedures (including biosensory data collection via eye track-
CS and the Ofce of Research at Plaksha University for providing
ing, heart rate monitoring, posture analysis, and note-taking
seed fnancial support through the Startup Research Grant Ref. No.
screenshots), potential risks, and their right to withdraw at any
OOR/PU-SRG/2023-24/06 for this research work.
time without penalty.
References
8 Conclusion
[1] A. Ahmed, S. Aziz, A. Abd-alrazaq, et al. 2025. Leveraging LLMs and wearables
In this paper, we introduced GuideAI, a multi-modal framework to provide personalized recommendations for enhancing student well-being
that enhances LLM-driven learning by integrating real-time biosen- and academic performance through a proof of concept. Sci Rep 15 (2025), 4591.
doi:10.1038/s41598-025-89386-2
sory feedback, including eye gaze, heart rate variability, posture,
[2] Bashar Alhafni, Sowmya Vajjala, Stefano Bannò, Kaushal Kumar Maurya, and
and digital note-taking behavior. GuideAI dynamically adapts learn- Ekaterina Kochmar. 2024. LLMs in Education: Novel Perspectives, Challenges,
ing content, pacing, and interventions across diverse modalities and Opportunities. arXiv:2409.11917 [cs.CL] https://arxiv.org/abs/2409.11917
[3] Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, and et al. 2022. On the
(text-based, image-based, audio-based, and video-based) based on Opportunities and Risks of Foundation Models. arXiv:2108.07258 [cs.LG]
inferred cognitive and physiological states. Our preliminary study https://arxiv.org/abs/2108.07258
[4] James R. Brockmole and David E. Irwin. 2005. Eye movements and the integration
(N=25) demonstrated statistically signifcant improvements in infor-
of visual memory and visual perception. Perception & Psychophysics 67, 3 (2005),
mation recall and conceptual understanding compared to standard 495–512. doi:10.3758/BF03193327
LLM interactions, highlighting GuideAI’s potential to bridge the [5] Yulin Chen, Ning Ding, Hai-Tao Zheng, Zhiyuan Liu, Maosong Sun, and Bowen
Zhou. 2024. Empowering Private Tutoring by Chaining Large Language Models.
gap between current LLM systems and the personalized, adaptive
In Proceedings of the 33rd ACM International Conference on Information and
needs of learners. Knowledge Management (Boise, ID, USA) (CIKM ’24). Association for Computing
While GuideAI shows promise, several avenues exist for future Machinery, New York, NY, USA, 354–364. doi:10.1145/3627673.3679665
[6] Zhendong Chu, Shen Wang, Jian Xie, Tinghui Zhu, Yibo Yan, Jinheng Ye, Aoxiao
work. The current evaluation involved a limited number of par- Zhong, Xuming Hu, Jing Liang, Philip S. Yu, and Qingsong Wen. 2025. LLM
ticipants and learning duration; longitudinal studies with larger, Agents for Education: Advances and Applications. arXiv:2503.11733 [cs.CY]
https://arxiv.org/abs/2503.11733 arXiv preprint.
more diverse groups in real-world educational settings are needed
[7] Sean Commins. 2018. Efciency: an underlying principle of learning? Reviews in
to assess long-term efectiveness and generalizability. Exploring the Neurosciences 29, 2 (2018), 183–197. doi:10.1515/revneuro-2017-0050
1232

IUI ’26, March 23–26, 2026, Paphos, Cyprus Shukla et al.
[8] Christopher M. DeGiorgio, Patrick Miller, Sheba Meymandi, and et al. 2010. [29] Kristjan-Julius Laak and Jaan Aru. 2025. AI and personalized learning: bridging
RMSSD, a measure of vagus-mediated heart rate variability, is associated with the gap with modern educational goals. arXiv:2404.02798 [cs.CY] https://arxiv.
risk factors for SUDEP: the SUDEP-7 Inventory. Epilepsy & Behavior 19, 1 (Sep org/abs/2404.02798
2010), 78–81. doi:10.1016/j.yebeh.2010.06.011 Epub 2010 Jul 27. [30] Rensis Likert. 1932. A Technique for the Measurement of Attitudes. Archives of
[9] Dinithi Dissanayake and Suranga Nanayakkara. 2025. Navigating the State of Psychology 22, 140 (1932), 1–55.
Cognitive Flow: Context-Aware AI Interventions for Efective Reasoning Support. [31] Chaeyeon Lim et al. 2025. DeBiasMe: De-biasing Human–AI Interactions with
https://arxiv.org/pdf/2504.16021 Preprint available at arXiv:2504.16021. Metacognitive AIED Interventions. arXiv:2504.16770 [cs.HC] https://arxiv.org/
[10] Sidney D’Mello, Andrew Olney, Claire Williams, and Patrick Hays. 2012. Gaze abs/2504.16770 ACM AIREASONING 2025 workshop paper (preprint).
tutor: A gaze-reactive intelligent tutoring system. International Journal of Human- [32] Siyang Liu, Xiaorong Guo, Xiangen Hu, and Xin Zhao. 2024. Advancing Genera-
Computer Studies 70, 5 (May 2012), 377–398. doi:10.1016/j.ijhcs.2012.01.004 tive Intelligent Tutoring Systems with GPT-4: Design, Evaluation, and a Mod-
[11] Sidney K. D’Mello and Arthur Graesser. 2010. Multimodal semi-automated afect ular Framework for Future Learning Platforms. Electronics 13, 24 (2024), 4876.
detection from conversational cues, gross body language, and facial features. doi:10.3390/electronics13244876
User Modeling and User-Adapted Interaction 20, 2 (01 Jun 2010), 147–187. doi:10. [33] Zoe Loh, Elizabeth H. Hall, Deborah Cronin, and John M. Henderson. 2023. Work-
1007/s11257-010-9074-4 ing memory control predicts fxation duration in scene-viewing. Psychological
[12] Sidney K. D’mello and Jacqueline Kory. 2015. A Review and Meta-Analysis of Research 87, 4 (June 2023), 1143–1154. doi:10.1007/s00426-022-01694-8
Multimodal Afect Detection Systems. ACM Comput. Surv. 47, 3, Article 43 (Feb. [34] Camillo Lugaresi, Jiuqiang Tang, Hadon Nash, Chris McClanahan, Esha Uboweja,
2015), 36 pages. doi:10.1145/2682899 Michael Hays, Fan Zhang, Chuo-Ling Chang, Ming Yong, Juhyun Lee, Wan-Teh
[13] D J Ewing, J M Neilson, and P Travis. 1984. New method for as- Chang, Wei Hua, Manfred Georg, and Matthias Grundmann. 2019. MediaPipe:
sessing cardiac parasympathetic activity using 24 hour electrocar- A Framework for Perceiving and Processing Reality. arXiv:1906.08172 [cs.DC]
diograms. Heart 52, 4 (1984), 396–402. doi:10.1136/hrt.52.4.396 https://arxiv.org/abs/1906.08172 Presented at the CVPR 2019 Workshop on
arXiv:https://heart.bmj.com/content/52/4/396.full.pdf Computer Vision for AR/VR.
[14] Cathy Mengying Fang, Valdemar Danry, Nathan Whitmore, Andria Bao, An- [35] Jens Madsen, Sara U. Júlio, Pawel J. Gucik, Richard Steinberg, and Lu-
drew Hutchison, Cayden Pierce, and Pattie Maes. 2024. PhysioLLM: Support- cas C. Parra. 2021. Synchronized eye movements predict test scores
ing Personalized Health Insights with Wearables and Large Language Models. in online video education. Proceedings of the National Academy of
arXiv:2406.19283 [cs.HC] https://arxiv.org/abs/2406.19283 Sciences 118, 5 (2021), e2016980118. doi:10.1073/pnas.2016980118
[15] Emilio Ferrara. 2024. Large Language Models for Wearable Sensor-Based Human arXiv:https://www.pnas.org/doi/pdf/10.1073/pnas.2016980118
Activity Recognition, Health Monitoring, and Behavioral Modeling: A Survey of [36] Gonzalo Gabriel Méndez, Luis Galárraga, Rodne Quijije, and Miguel A Nacenta.
Early Trends, Datasets, and Challenges. Sensors 24, 15 (2024), 5045. doi:10.3390/ 2025. The Potential of Cognitive Circles to Measure Mental Load. In Proceedings
s24155045 of the 38th Annual ACM Symposium on User Interface Software and Technology
[16] Francesco Ferrati, Eduardo Gil, and Jesús Lázaro. 2023. Coverage of PPG-based (UIST ’25). Association for Computing Machinery, New York, NY, USA, Article
Wearable Devices in Ofce Tasks. In 2023 Computing in Cardiology (CinC), Vol. 50. 75, 10 pages. doi:10.1145/3746059.3747716
IEEE, Tampere, Finland, 1–4. [37] Ismael Villegas Molina, Audria Montalvo, Benjamin Ochoa, Paul Denny, and Leo
[17] B. Fischer and B. Breitmeyer. 1987. Mechanisms of visual attention revealed by Porter. 2024. Leveraging LLM Tutoring Systems for Non-Native English Speakers
saccadic eye movements. Neuropsychologia 25, 1, Part 1 (1987), 73–83. doi:10. in Introductory CS Courses. arXiv:2411.02725 [cs.HC] https://arxiv.org/abs/2411.
1016/0028-3932(87)90044-3 02725
[18] B. Fischer and H. Weber. 1993. Express saccades and visual attention. Behavioral [38] Susan M. Munn, Leanne Stefano, and Jef B. Pelz. 2008. Fixation-identifcation
and Brain Sciences 16, 3 (1993), 553–567. doi:10.1017/S0140525X00031575 in dynamic scenes: comparing an automated algorithm to manual coding. In
[19] Michael E. Goldberg, H. Eggers, and P. Gouras. 1991. The Oculomotor System. Proceedings of the 5th Symposium on Applied Perception in Graphics and Visualiza-
In Principles of Neural Science. Columbia University Press, New York, NY, USA, tion (Los Angeles, California) (APGV ’08). Association for Computing Machinery,
660–676. http://www.columbia.akadns.net/itc/hs/medical/neuralsci/2004/slides/ New York, NY, USA, 33–42. doi:10.1145/1394281.1394287
31_LectureSlides.pdf [39] Paola Nicolini, Gabriella Malfatto, and Tiziano Lucchi. 2024. Heart Rate Variability
[20] Adit Gupta, Jennifer Reddig, Tommaso Calo, Daniel Weitekamp, and Christopher J. and Cognition: A Narrative Systematic Review of Longitudinal Studies. Journal
MacLellan. 2025. Beyond Final Answers: Evaluating Large Language Models for of Clinical Medicine 13, 1 (2024), 280. doi:10.3390/jcm13010280
Math Tutoring. arXiv:2503.16460 [cs.HC] https://arxiv.org/abs/2503.16460 [40] OpenAI. 2024. Introducing ChatGPT Edu. https://openai.com/index/introducing-
[21] Sandra G. Hart and Lowell E. Staveland. 1988. Development of NASA-TLX chatgpt-edu/ Accessed: 2025-04-10.
(Task Load Index): Results of Empirical and Theoretical Research. In Human [41] Iris Cristina Peláez-Sánchez, Davis Velarde-Camaqui, and Leonardo David
Mental Workload, Peter A. Hancock and Najmedin Meshkati (Eds.). Advances Glasserman-Morales. 2024. The Impact of Large Language Models on Higher
in Psychology, Vol. 52. North-Holland, Amsterdam, The Netherlands, 139–183. Education: Exploring the Connection between AI and Education 4.0. Frontiers in
doi:10.1016/S0166-4115(08)62386-9 Education 9 (2024), 1392091. doi:10.3389/feduc.2024.1392091
[22] Bihao Hu, Jiayi Zhu, Yiying Pei, and Xiaoqing Gu. 2025. Exploring the potential [42] Tepring Piquado, Derek Isaacowitz, and Arthur Wingfeld. 2010. Pupillom-
of LLM to enhance teaching plans through teaching simulation. npj Science of etry as a measure of cognitive efort in younger and older adults. Psy-
Learning 10, 1 (06 Feb 2025), 7. doi:10.1038/s41539-025-00300-x chophysiology 47, 3 (2010), 560–569. doi:10.1111/j.1469-8986.2009.00947.x
[23] Jef Huang, Ryen White, and Georg Buscher. 2012. User see, user point: gaze arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-8986.2009.00947.x
and cursor alignment in web search. In Proceedings of the SIGCHI Conference on [43] Lauren B. Resnick. 2017. Toward a Cognitive Theory of Instruction. In Learning
Human Factors in Computing Systems (Austin, Texas, USA) (CHI ’12). Association and Motivation in the Classroom. Routledge, London, UK, 5–38. doi:10.4324/
for Computing Machinery, New York, NY, USA, 1341–1350. doi:10.1145/2207676. 9781315188522-2
2208591 [44] Denise Rey and Markus Neuhäuser. 2011. Wilcoxon-Signed-Rank Test. In
[24] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian International Encyclopedia of Statistical Science, Miodrag Lovric (Ed.). Springer
Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Berlin Heidelberg, Berlin, Heidelberg, 1658–1659. doi:10.1007/978-3-642-04898-
Liu. 2025. A Survey on Hallucination in Large Language Models: Principles, 2_616
Taxonomy, Challenges, and Open Questions. ACM Trans. Inf. Syst. 43, 2, Article [45] Marc Rodemer, Jessica Karch, and Sascha Bernholt. 2023. Pupil dilation as cogni-
42 (Jan. 2025), 55 pages. doi:10.1145/3703155 tive load measure in instructional videos on complex chemical representations.
[25] Udesh Jayasinghe, Benedikt Janko, Francis Hwang, Thomas Münzer, Christoph Frontiers in Education 8 (2023), 1062053. doi:10.3389/feduc.2023.1062053
Baer, and Gerhard Tröster. 2023. Classifcation of static postures with wearable [46] Lizawati Salahuddin, Jaegeol Cho, Myeong Gi Jeong, and Desok Kim. 2007. Ultra
sensors mounted on loose clothing. Scientifc Reports 13 (2023), 131. doi:10.1038/ short term analysis of heart rate variability for monitoring mental stress in
s41598-022-27306-4 mobile settings. In Proceedings of the Annual International Conference of the IEEE
[26] Moritz Kassner, William Patera, and Andreas Bulling. 2014. Pupil: An Open Engineering in Medicine and Biology Society. IEEE, United States, 4656–4659.
Source Platform for Pervasive Eye Tracking and Mobile Gaze-based Interaction. doi:10.1109/IEMBS.2007.4353378 Research Support, Non-U.S. Gov’t.
In Adjunct Proceedings of the 2014 ACM International Joint Conference on Pervasive [47] Dario D. Salvucci and Joseph H. Goldberg. 2000. Identifying fxations and
and Ubiquitous Computing (Seattle, Washington) (UbiComp ’14 Adjunct). ACM, saccades in eye-tracking protocols. In Proceedings of the 2000 Symposium on
New York, NY, USA, 1151–1160. doi:10.1145/2638728.2641695 Eye Tracking Research & Applications (Palm Beach Gardens, Florida, USA)
[27] Khan Academy. 2025. Meet Khanmigo: Khan Academy’s AI-powered teaching (ETRA ’00). Association for Computing Machinery, New York, NY, USA, 71–78.
assistant & tutor. https://www.khanmigo.ai/ Accessed: 2025-04-10. doi:10.1145/355017.355028
[28] Christian Kothe, Seyed Yahya Shirazi, Tristan Stenner, David Medine, Chadwick [48] Yixuan Shi. 2025. Biomechanics optimizes learning posture and learning efciency
Boulay, Matthew I. Grivich, Tim Mullen, Arnaud Delorme, and Scott Makeig. in higher education teaching and learning. Molecular &; Cellular Biomechanics
2024. The Lab Streaming Layer for Synchronized Multimodal Recording. doi:10. 22, 5 (Mar. 2025), 1620. doi:10.62617/mcb1620
1101/2024.02.13.580071 biorxiv:2024.02.13.580071 bioRxiv preprint. [49] David Sun, Pablo Paredes, and John Canny. 2014. MouStress: detecting stress
from mouse motion. In Proceedings of the SIGCHI Conference on Human Factors
1233

GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions IUI ’26, March 23–26, 2026, Paphos, Cyprus
in Computing Systems (Toronto, Ontario, Canada) (CHI ’14). Association for and Huajun Chen. 2024. Scientifc Large Language Models: A Survey on Biological
Computing Machinery, New York, NY, USA, 61–70. doi:10.1145/2556288.2557243 & Chemical Domains. arXiv:2401.14656 [cs.CL] https://arxiv.org/abs/2401.14656
[50] Hui-Min Wang and Sheng-Chieh Huang. 2012. SDNN/RMSSD as a [56] Zhaoli Zhang, Zhenhua Li, Hai Liu, Taihe Cao, and Sannyuya Liu. 2020.
Surrogate for LF/HF: A Revised Investigation. Modelling and Simu- Data-driven Online Learning Engagement Detection via Facial Expression
lation in Engineering 2012, 1 (2012), 931943. doi:10.1155/2012/931943 and Mouse Behavior Recognition Technology. Journal of Educational
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1155/2012/931943 Computing Research 58, 1 (2020), 63–86. doi:10.1177/0735633119825575
[51] Shen Wang, Tianlong Xu, Hang Li, Chaoli Zhang, Joleen Liang, Jiliang Tang, arXiv:https://doi.org/10.1177/0735633119825575
Philip S. Yu, and Qingsong Wen. 2024. Large Language Models for Education: A [57] Zhehao Zhang, Ryan A. Rossi, Branislav Kveton, Yijia Shao, Diyi Yang, Hamed
Survey and Outlook. arXiv:2403.18105 [cs.CL] https://arxiv.org/abs/2403.18105 Zamani, Franck Dernoncourt, Joe Barrow, Tong Yu, Sungchul Kim, Ruiyi Zhang,
[52] Pingmei Xu, Yusuke Sugano, and Andreas Bulling. 2016. Spatio-Temporal Model- Jiuxiang Gu, Tyler Derr, Hongjie Chen, Junda Wu, Xiang Chen, Zichao Wang,
ing and Prediction of Visual Attention in Graphical User Interfaces. In Proceedings Subrata Mitra, Nedim Lipka, Nesreen Ahmed, and Yu Wang. 2024. Personalization
of the 2016 CHI Conference on Human Factors in Computing Systems (San Jose, of Large Language Models: A Survey. arXiv:2411.00027 [cs.CL] https://arxiv.org/
California, USA) (CHI ’16). Association for Computing Machinery, New York, NY, abs/2411.00027
USA, 3299–3310. doi:10.1145/2858036.2858479 [58] Xiangrong (Daniel) Zhu, Yuan Xu, Tianjian Liu, Jingwei Sun, Yu Zhang, and
[53] Songlin Xu, Xinyu Zhang, and Lianhui Qin. 2024. EduAgent: Generative Student Xin Tong. 2025. Intelligent Interaction Strategies for Context-Aware Cognitive
Agents in Learning. arXiv:2404.07963 [cs.CY] https://arxiv.org/abs/2404.07963 Augmentation. arXiv:2504.13684 [cs.HC] https://arxiv.org/abs/2504.13684 ACM
[54] Ling Zhang, James D. Basham, and Sohyun Yang. 2020. Understanding the AIREASONING 2025 workshop paper (preprint).
implementation of personalized learning: A research synthesis. Educational [59] Michael G. Ziegler. 2004. 50 -Psychological Stress and the Autonomic Nervous
Research Review 31 (2020), 100339. doi:10.1016/j.edurev.2020.100339 System. In Primer on the Autonomic Nervous System (Second Edition) (second
[55] Qiang Zhang, Keyang Ding, Tianwen Lyv, Xinda Wang, Qingyu Yin, Yiwen Zhang, edition ed.), David Robertson, Italo Biaggioni, Geofrey Burnstock, and Phillip A.
Jing Yu, Yuhao Wang, Xiaotong Li, Zhuoyi Xiang, Kehua Feng, Xiang Zhuang, Low (Eds.). Academic Press, San Diego, 189–190. doi:10.1016/B978-012589762-
Zeyuan Wang, Ming Qin, Mengyao Zhang, Jinlu Zhang, Jiyu Cui, Tao Huang, 4/50051-7
Pengju Yan, Renjun Xu, Hongyang Chen, Xiaolin Li, Xiaohui Fan, Huabin Xing,
1234