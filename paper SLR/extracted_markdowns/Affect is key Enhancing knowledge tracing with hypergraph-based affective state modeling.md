Expert Systems With Applications 331 (2026) 133323
Contents lists available at ScienceDirect
Expert Systems With Applications
journal homepage: www.elsevier.com/locate/eswa
Affect is key: Enhancing knowledge tracing with hypergraph-based
affective state modeling
Changqin Huanga,b, Xi Chengb, Yi Wang c,∗, Huicheng Zengd, Xiaodi Huang e,
Qionghao Huangb
aCollege of Education, Zhejiang University, Hangzhou, 310058, Zhejiang, China
bZhejiang Key Laboratory of Intelligent Education Technology and Application, Zhejiang Normal University, Jinhua, 321004, Zhejiang, China
cDepartment of Mathematics, City University of Hong Kong, 999077, Hong Kong, China
dShanghai University of Finance and Economics Zhejiang College, Jinhua, 321000, Zhejiang, China
eSchool of Computing, Mathematics and Engineering, Charles Sturt University, Albury, 2640, New South Wales, Australia
a r t i c l e i n f o a b s t r a c t
Keywords: Contemporary knowledge tracing models have made substantial progress in modeling cognitive learning pat-
Knowledge tracing terns, yet their predominant focus on performance metrics overlooks the profound influence of affective states
Hypergraph neural network on educational processes. Affective factors critically shape students’ attentional engagement, concept assimila-
Affective state
tion, and problem-solving consistency – dynamics that existing cognitive-centric frameworks often fail to cap-
ture. We propose the Affective Hypergraph Knowledge Tracing (AHGKT) framework, which incorporates affective
intelligence into knowledge tracing through a dual-layer hypergraph architecture. The exercise layer establishes
high-order relationships among questions and knowledge concepts, while the affection layer tracks affective pat-
terns throughout learning sessions. A novel hypergraph convolution operator synergistically fuses these cognitive
and affective signals, enabling simultaneous modeling of concept mastery and affective impacts through hier-
archical graph propagation. Extensive experiments on three real-world datasets demonstrate the superiority of
AHGKT, achieving statistically significant accuracy improvements of up to 5% over state-of-the-art baselines. The
framework’s effectiveness is further validated through ablation studies quantifying the complementary benefits
of hypergraph modeling and affective feature integration. By modeling affection as a quantifiable predictor of
learning outcomes and introducing hypergraph neural networks into the educational domain, this work offers
a promising methodological contribution toward affect-aware intelligent tutoring systems. Our findings provide
practical insights and design principles for developing educational AI that better captures the interplay between
cognitive and affective dimensions in learning.
1. Introduction ing hidden variables and probabilistic updates. BKT relies on fixed prior
parameters, making it less adaptable to diverse and complex learning be-
With the development of educational data mining, Knowledge Trac- haviors. With the development of deep learning (Graves, 2013; Graves
ing has become a key direction in intelligent education research. It aims et al., 2013) , new breakthroughs have emerged in the KT domain. Deep
to assess students’ knowledge mastery and predict their learning per- Knowledge Tracing (DKT) (Piech et al., 2015) leverages Recurrent Neu-
formance (Abdelrahman et al., 2023; Tomasevic et al., 2020). Accurate ral Networks (RNNs) (Lipton et al., 2015) and Long Short Term Mem-
modeling of students’ knowledge states not only enhances learning effec- ory (LSTM) (Hochreiter & Schmidhuber, 1997) to model students’ learn-
tiveness but also supports intelligent services such as student profiling ing sequences, achieving improved performance by continuously updat-
(Zong et al., 2020)and personalized resource recommendation (Wang ing knowledge states. DKT primarily focuses on temporal relationships,
et al., 2021). lacking the capacity to fully explore complex connections between exer-
The evolution of KT methods has seen significant advancements. cises. The Self-Attentive Knowledge Tracing (SAKT) (Pandey & Karypis,
Early classical models, such as the Bayesian Knowledge Tracing (BKT) 2019) model assigns weights to exercises using scaled dot-product at-
(Corbett & Anderson, 1994), predict students’ knowledge mastery us- tention and multi-head attention mechanisms (Vaswani et al., 2017),
∗ Corresponding author.
E-mail addresses: cqhuang@zju.edu.cn (C. Huang), chengxi@zjnu.edu.cn (X. Cheng), ywan72@cityu.edu.hk (Y. Wang), Z2015003@shufe-zj.edu.cn (H. Zeng),
xhuang@csu.edu.au (X. Huang), qhhuang@zjnu.edu.cn (Q. Huang).
https://doi.org/10.1016/j.eswa.2026.133323
Received 31 March 2025; Received in revised form 9 June 2026; Accepted 13 June 2026
Available online 18 June 2026
0957-4174/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
To address these challenges, we construct an exercise-affection hier-
archical hypergraph and propose an affect-aware hypergraph convolu-
tion mechanism to explicitly capture high-order relationships among ex-
ercises involving the same concept (e.g., 𝑞 , 𝑞 , and 𝑞 for 𝑐 ). This novel
2 3 5 3
method, named Affective Hypergraph Knowledge Tracing (AHGKT), in-
tegrates affective states and exercise-concept interactions to enhance
the representation of student knowledge states. AHGKT also reveals the
influence of affective fluctuations on learning behaviors, supporting per-
sonalized learning and real-time intervention strategies. The key contri-
butions of this work are summarized as follows.
• We incorporate affective factors into the knowledge tracing frame-
work, enhancing the precision and adaptability of knowledge state
representation by integrating intrinsic factors such as individual stu-
dent differences and problem difficulty.
• We propose an affect-aware hypergraph convolution mechanism,
which integrates representations from the exercise and affection lay-
ers in a hierarchical hypergraph to capture complex high-order inter-
actions among exercises, knowledge concepts, and affective states.
• To handle both supervised and unsupervised scenarios, we introduce
specialized optimization strategies, enabling the model to learn the
influence of affective states on learning behaviors even in the ab-
sence of labeled affective data.
• Experimental results on multiple datasets demonstrate that our
model outperforms traditional methods in terms of both accuracy
and stability.
The remainder of this paper is organized as follows. Section 2 reviews
related work on knowledge tracking and affective analysis. Section 3
Fig. 1. (a) Correlation statistics between concentration and learning outcomes introduces the definitions and notations related to this paper. Section 4
on the ASSIST2017 dataset. (b) Students exhibit different affective states across
presents the proposed AHGKT framework. Section 5 provides the ex-
various exercises.
perimental results along with detailed analysis. Section 6 concludes the
paper.
capturing the varying impacts of exercises on knowledge state predic- 2. Related work
tion. It lacks sufficient exploration of the potential relationships between
questions. The Graph-based Knowledge Tracing (GKT) (Nakagawa et al., In this section, we review the work related to knowledge tracing.
2019) method represents students’ response records as nodes in a graph
and employs Graph Convolutional Networks (GCNs) (Kipf & Welling, 2.1. Knowledge tracing
2016) to propagate information among nodes, enabling precise model-
ing of complex relationships between knowledge points. Traditional knowledge tracing models, such as BKT (Corbett & An-
Although existing KT models perform well, they cannot model the derson, 1994), use Hidden Markov Models (Baker et al., 2008) to dynam-
mapping of learners’ complex inner states (such as unstable emotional ically track students’ knowledge states. Several important extensions of
factors) to the answer results (Mehta, 2022), thus limiting the ability BKT include personalized BKT, which introduces individual parameters
of models to achieve more accurate predictions. As shown in Fig. 1(a), to capture student-specific differences (Lee & Brunskill, 2012; Yudelson
statistical analysis on the ASSIST2017 dataset reveals that higher con- et al., 2013). For instance, Pardos and Heffernan (Pardos & Heffernan,
centration levels correlate with greater precision. However, most models 2010) focused on heuristically personalizing the prior knowledge proba-
focus primarily on exercises and response outcomes, failing to effectively bility 𝑝 for each student across different skills. Additionally, Käser et al.
capture the potential interactions between students’ affective states and (2017) proposed using a Dynamic Bayesian Network to jointly model
exercises. multiple skills and the dependencies between them, aiming to capture
Fig. 1(b) illustrates the variation in concepts and affective states hierarchical relationships among skills within a single model.
across exercises 𝑞 to 𝑞 . Although both 𝑞 and 𝑞 involve concepts 𝑐 A pioneering deep learning approach in knowledge tracing is the
1 5 2 3 2
and 𝑐 , they correspond to different affective states, which may result DKT model (Piech et al., 2015) , which leverages RNNs (Lipton et al.,
3
from differences in problem difficulty or format. In 𝑞 , students exhibit a 2015) to predict the probability of a student answering a question cor-
3
higher level of concentration, leading to a correct response, whereas in rectly at each time step. Some extended DKT models improve perfor-
𝑞 , a lower level of concentration results in an incorrect answer. More- mance by incorporating problem features like problem ID (Sonkar et al.,
2
over, both 𝑞 and 𝑞 involve concept 𝑐 and are associated with high 2020) and known difficulty (Shen et al., 2022), or student-related factors
4 5 4
levels of confusion, ultimately leading to incorrect responses. These ob- such as response rate and practice time (Xiong et al., 2016). DKT+ (Ye-
servations indicate that affective states are closely associated with the ung & Yeung, 2018) refines the loss function of the original DKT model
underlying knowledge concepts. The variations in affective states in- by incorporating two additional regularization terms. DKVMN (Zhang
duced by different exercises and concepts can significantly influence stu- et al., 2017) employed a combination of static key matrices and dy-
dent learning performance. Consequently, this presents two significant namic value matrices, further enhancing DKT’s ability to track the state
challenges for constructing affective knowledge tracing models, specif- of each concept over time. XKT (Huang et al., 2024b) model integrates
ically: (1) how to accurately represent affective states, and (2) how to multidimensional item response theory into knowledge tracing, simu-
characterize the complex interplay between affective states and under- lating students’ selective perception and knowledge memory processes
lying knowledge concepts. to enhance interpretability. THKT (Sun et al., 2024) dynamically tracks
2

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
students’ target hierarchies and assesses their problem-solving abilities confusion and fluency during the learning process are significantly pos-
within these hierarchies. Huang et al. (2024a) incorporates causal self- itively correlated with learning outcomes, whereas boredom exhibits
attention and gate mechanisms to improve the consistency of students’ a significant negative correlation. Pedro et al. (2013) employed a lo-
knowledge state representations. gistic regression model to analyze data from the ASSISTment system,
In the task of knowledge tracing, the introduction of attention mech- demonstrating that lower levels of boredom, higher levels of confusion,
anisms addresses the limitation of traditional models that treat all exer- and reduced instances of careless errors are significantly associated with
cises equally. Attention mechanisms can identify the importance of dif- an increased probability of college admission. Pardos et al. (2013) ex-
ferent exercises when predicting the target question and weight various amined the distribution of emotional states among students with differ-
interactions accordingly, thereby improving prediction accuracy. SAKT ent learning outcomes, finding that successful students typically demon-
(Pandey & Karypis, 2019) is the first model to introduce self-attention strate balanced focus and moderate frustration, while unsuccessful stu-
mechanisms into knowledge tracing. It uses the scaled dot-product at- dents are more prone to boredom or gaming behaviors. Liu et al. (2022)
tention mechanism and multiple attention heads to learn the importance developed a BERT-CNN-based model to automatically detect emotional
of different exercises during prediction. AKT (Ghosh et al., 2020) in- and cognitive engagement in MOOC discussions and demonstrated their
troduces a mechanism called "monotonic attention," which allows the joint effects on learning achievement. Furthermore, Wang et al. (2024)
attention weights to decay exponentially over time, reflecting the tem- integrated emotion-based estimates of guess and slip parameters with
poral relevance of student interactions. SAINT (Choi et al., 2020) further the fundamental neural cognitive diagnostic framework derived from
extends the Transformer architecture by separating question embed- the DINA model to diagnose the knowledge proficiency levels of stu-
dings and student response embeddings, and incorporates time-related dents.
features, such as response time, to refine the attention weights and cap- However, despite the revealed association between emotional states
ture the temporal impact on the learning process. and learning performance, how to incorporate emotional dynamics into
However, most of these methods consider different exercises, elapsed knowledge tracing models to enhance the precision of modeling stu-
time and other factors, while ignoring the importance of students’ emo- dents’ knowledge states remains a key challenge.
tional state to the prediction results. By introducing emotional factors
into the attention mechanism, the model can adjust the attention to dif- 3. Preliminaries
ferent exercises and thus improve the prediction accuracy.
Table 1
2.2. Graph-based knowledge tracing Main notations in this paper.
Symbol Definition
Compared to traditional knowledge tracing methods, graph-based
models excel at capturing the complex relationships between students, 𝑡 Time index.
problems, and skills, enabling more comprehensive learning state pre- 𝑛,𝑚 Number of exercises and concepts.
d
co
ic
m
ti
p
o
o
n
n
s.
e
T
nt
h
s
e
(
G
K
K
C
T
s)
(
a
N
n
a
d
k a
t
g
h
a
e
w
ir
a
d
e
e
t
p
a
e
l
n
.,
d
2
e
0
n
1
ci
9
e
)
s
m
a
o
s
d
a
e l
g
r
r
e
a
p
p
r
h
e s
s
e
tr
n
u
ts
c t
k
u
n
r
o
e,
w
t
l
r
e
a
d
n
g
s
e
-
𝑥

𝑞
𝑡 S
I
E
n
t
x
u
t
e
e
d
r
r
c
e
a
i
n
c
s
t
t
e
i
i
o
i
n
d
n
t
e
e
s
n
r
e
a
t
q
i
c
fi
u
ti
e
e
o
r
n
n
c
a
e
a
t
t
t
{
i
𝑥
t
m
i
1
m
,
e
…
e
𝑡 .
𝑡
,
.
𝑥 𝑡}.
𝑡
forming the knowledge tracing task into a time-series node-level classi- 𝑐 𝑗th knowledge concept.
𝑗
fication problem. The PEBG (Liu et al., 2020) model employs a bipartite 
𝑞
Exercise node set in hypergraph.
 Affective state node set.
graph to embed problems and skills, integrating exercise difficulty in- 𝑎
 Hyperedge set for knowledge concepts.
formation during training to enhance prediction accuracy. SGKT (Wu

𝑖𝑛
Inter-layer edges between exercise and affective layers.
et al., 2022) employs gated graph neural networks to capture students’  𝑜𝑢𝑡 Exercise-affect hierarchical hypergraph.
knowledge states from session graphs and utilizes GNN (Scarselli et al., 𝑨∈{0,1}𝑛×𝑚 Exercise-concept incidence matrix.
2008) to derive embeddings for exercises and skills in the relationship
graph.
We consider a student’s problem-solving process as an interaction
To further alleviate representation sparsity, Bi-CLKT (Song et al.,
between the student and the problem, which is influenced not only by
2022) introduced contrastive learning on question-KC and KC-KC graphs
the student’s knowledge mastery but also by factors such as emotional
to produce question embeddings enhanced with structural information
state and the number of practice attempts. Therefore, we represent the
from both questions and KCs. More recently, TCL4KT (Sun et al., 2023)
student’s exercise at time 𝑡 as 𝑥 =(𝑠,𝑞,𝑐,𝑎𝑡𝑡,𝑟,𝑎𝑓 ), where 𝑠 denotes
introduced a weighted heterogeneous graph-based contrastive learning 𝑡 𝑡 𝑡 𝑡 𝑡 𝑡 𝑡 𝑡
the student ID, 𝑞 represents the question ID, 𝑐 indicates the knowl-
framework to enhance question representation learning for knowledge 𝑡 𝑡
edge concept associated with the question, 𝑎𝑡𝑡 refers to the number of
tracing. Beyond pairwise graph modeling, the DGEKT (Cui et al., 2024) 𝑡
attempts made by the student, 𝑎𝑓 represents the student’s emotional
model leverages a conceptual association hypergraph (Chen et al., 2020; 𝑡
state, and 𝑟 denotes the response (correct or incorrect). Given the se-
Feng et al., 2019) to model related knowledge concepts within learning 𝑡
quence of exercises from time step 1 to 𝑡, ={𝑥 ,𝑥 ,…,𝑥}, and the
interactions, effectively capturing higher-order relationships among ex- 1 2 𝑡
question ID at the next time step 𝑞 , the goal of knowledge tracing
ercise concepts. 𝑡+1
is to predict the probability that the student will correctly answer the
However, most existing graph-based KT models primarily focus on
structural representation learning and neglect the dynamic role of learn-
question at time 𝑡+1, formulated as 𝑝(𝑟
𝑡+1
=1| ,𝑞
𝑡+1
). For clarity, the
main symbols used throughout this paper are summarized in Table 1.
ers’ emotional states during the learning process. By introducing an af-
fective attention mechanism into the hypergraph framework, emotional
4. The proposed method
states can be propagated among skill-related exercises through hyper-
graph convolution, enabling precise tracking of students’ personalized
In this section, we propose an Affective Hypergraph Knowledge
knowledge states.
Tracing (AHGKT) framework, designed to capture the affective inter-
actions of students during problem-solving, thereby enhancing the per-
2.3. Affective effects formance of knowledge tracing. As illustrated in Fig. 2, the framework
first constructs a layered hypergraph, comprising an exercise hyper-
Craig et al. (2004) investigated the emotional changes experienced graph layer and an affection layer. These layers respectively model the
by college students while learning the basics of computers. Utilizing ob- high-dimensional relationships between problems and knowledge con-
servational methods and a self-designed scale analysis, it was found that cepts, as well as the influence of students’ affective characteristics on
3

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
Fig. 2. The overall architecture of the AHGKT model. An exercise hypergraph layer and an affective layer are first constructed. Then, we design an affection-aware
hypergraph convolution network to integrate affective and knowledge representations. Finally, a GRU is employed to predict students’ knowledge states.
the problem-solving process. Subsequently, by integrating the two struc- represents the set of hyperedges corresponding to knowledge concepts.
tures, an affection-aware hypergraph convolution is constructed, effec- Each hyperedge 𝑐 ∈ connects all exercises associated with the con-
𝑗 𝑖𝑛
tively capturing the complex high-order relationships among affections, cept 𝑗th, thereby capturing high-order knowledge dependencies.
problems, and knowledge concepts. Finally, the model achieves collab- The connectivity between exercises and knowledge concepts is rep-
orative modeling of affective features and knowledge states through the resented by an incidence matrix 𝑨∈{0,1}𝑛×𝑚, where 𝑛 and 𝑚 denote
joint optimization of the affection layer modeling loss and prediction the numbers of exercises and concepts, respectively. The element 𝑨 is
𝑖𝑗
loss, providing more comprehensive and accurate representations for defined as:
knowledge tracing.
{
1, if 𝑞 ∈𝑐 ,
4.1. Exercise-affection hierarchical hypergraph 𝑨 = 𝑖 𝑗 (1)
𝑖𝑗 0, otherwise.
The hierarchical hypergraph consists of the exercise layer and the af- In addition, to incorporate affective information, we introduce inter-
fection layer. The exercise layer connects exercise nodes through hyper- layer hyperedges  to model the correspondence between the exercise
𝑜𝑢𝑡
edges based on knowledge concepts, capturing the high-dimensional re- layer and the affective layer. Specifically, each exercise node 𝑣 ∈ is
𝑞 𝑞
lationships between exercises and knowledge points. The affection layer connected to a corresponding affective state node 𝑣 ∈ via an inter-
𝑎 𝑎
models the interactions between students’ affection states and exercises, layer edge 𝑒 ∈ . This hierarchical hypergraph structure enables the
𝑜 𝑜𝑢𝑡
capturing the influence of affection on learning behaviors. model to simultaneously capture high-order relationships among exer-
cises and knowledge concepts, while integrating affective factors to en-
4.1.1. Exercise-layer hypergraph hance knowledge tracing performance.
To more comprehensively model the complex interactions among
exercises, knowledge concepts, and affective states, we first construct 4.1.2. Affection layer
an exercise-affection hierarchical hypergraph ={{ , }, , }, The affection state is influenced by multiple factors and relying on a
𝑞 𝑎 𝑖𝑛 𝑜𝑢𝑡
where  and  denote the sets of exercise nodes and affective state single dimension cannot fully capture the true emotional characteristics
𝑞 𝑎
nodes, respectively. The exercise-layer hypergraph is defined as a sub- of the students. Therefore, the affection layer integrates students’ per-
structure  =( , ), which captures the high-order relationships be- sonalized attributes, problem difficulty, and attempt count to construct
𝑖𝑛 𝑞 𝑖𝑛
tween exercises and knowledge concepts. Unlike conventional graphs associations between affection nodes and other elements. This integra-
that represent pairwise relations, hypergraphs allow each hyperedge to tion enables a more comprehensive and individualized representation
connect multiple nodes, making them suitable for modeling the many- of students’ emotional states.
to-many correspondence between exercises and concepts. Formally, Individual Student Characteristics: Different students may exhibit
 ={𝑞 ,𝑞 ,…,𝑞 } denotes the set of exercises, and  ={𝑐 ,𝑐 ,…,𝑐 } varying emotional experiences and interpretations when facing the same
𝑞 1 2 𝑛 𝑖𝑛 1 2 𝑚
4

C. Huang et al.
Expert Systems With Applications 331 (2026) 133323
problem, even if their knowledge levels are similar. To capture this indi-
vidual difference, student features are mapped into a personalized rep-
| resentation vector 𝒈 | :   |     |       | ⎛        | ⎞       |     |     |
| -------------------- | --- | --- | ----- | -------- | ------- | --- | --- |
|                      | 𝑠   |     |       | ⎜ 1 ∑    | 1 ⎟,    |     | (6) |
|                      |     |     | 𝐱̃=𝐪̂ | 𝑖⎜ 𝐚̂⊙ √ | √ 𝑾𝒉 𝑐⎟ |     |     |
𝑑
|              |      |     |     | ⎜ 𝑑 𝑞𝑖 𝑐∈ 𝑖𝑛(𝑞𝑖) | 𝑐 ⎟ |     |     |
| ------------ | ---- | --- | --- | ----------------- | --- | --- | --- |
|              |      |     |     | ⎝                 | ⎠   |     |     |
| 𝒈 =Sigmoid(𝒇 | ⋅𝑺), |     | (2) |                   |     |     |     |
𝑠 𝑠 where  (𝑞) denotes the set of hyperedges associated with exercise
𝑖𝑛 𝑖
|         |                                                              |     | node 𝑞 | , 𝒉  represents the feature vector of concept 𝑐, 𝐚̂ is the affec- |     |     |     |
| ------- | ------------------------------------------------------------ | --- | ------ | ----------------------------------------------------------------- | --- | --- | --- |
| where 𝒇 | ∈{0,1}1×𝑀 denotes the one-hot identity vector of student 𝑠,  |     |        | 𝑖 𝑐                                                               |     |     |     |
𝑠 tive vector, and 𝑑  and 𝑑  denote the degrees of the exercise node and
with 𝑀  representing the total number of unique students across both  𝑞𝑖 𝑐
concept hyperedge, respectively. Through this mechanism, the affec-
the training and testing sets. 𝑺∈ℝ𝑀×𝐾 is a global learnable student
tive vector 𝐚̂ effectively regulates the interaction between exercises and
embedding matrix that maps student features into a 𝐾-dimensional rep-
resentation space, where 𝐾 denotes the embedding dimension. Since 𝒇 knowledge concepts, enabling the hypergraph convolution to capture
𝑠
is a one-hot vector, the operation 𝒇 ⋅𝑺 is mathematically equivalent to   high-order relationships between problem-concept and problem-affect
𝑠
directly indexing and retrieving the  corresponding row of 𝑺 associated  interactions. The resulting representation 𝐱̃ is then used as the input to
with student 𝑠. The obtained representation is subsequently transformed  the subsequent prediction module.
by the Sigmoid activation function to produce the personalized student
4.3.  Prediction module
| representation 𝒈 | .   |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
𝑠
Problem Difficulty: Problem difficulty significantly influences emo-
Next, the affect-aware exercise representation 𝐱̃ is input into a GRU
tional states-more difficult problems may induce confusion or frustra-
module to dynamically model the evolution of the student’s knowledge
tion, whereas moderately difficult problems can enhance concentration.
state. The GRU performs dynamic information modeling using the fol-
The difficulty-related representation vector 𝒈  is obtained as:
𝑑 lowing state update equations:
| 𝒈 =Sigmoid(𝒇 | ⋅𝑫), |     | (3) |             |       |     |     |
| ------------ | ---- | --- | --- | ----------- | ----- | --- | --- |
| 𝑑            | 𝑑    |     | ⎧𝒖  | =𝜎(𝑾 𝐱̃+𝑼 𝒉 | +𝐛 ), |     |     |
|              |      |     |     | 𝑡 𝑢 𝑢 𝑡−1   | 𝑢     |     |     |
where 𝒇 ∈{0,1}1×𝑁 denotes the one-hot vector of the problem, with  ⎪ 𝐱̃+𝑼
|     |     |     | ⎪𝒛  | 𝑡 =𝜎(𝑾 𝑧 𝑧 𝒉 𝑡−1 | +𝐛 𝑧 ), |     | (7) |
| --- | --- | --- | --- | ---------------- | ------- | --- | --- |
𝑑
𝑁 being the total number of problems. 𝑫∈ℝ𝑁×𝐾 is a learnable weight  ⎨𝒉̃ =tanh(𝑾 𝐱̃+𝑼 (𝒖 ⊙𝒉 )+𝐛 ),
|     |     |     | ⎪   | 𝑡 ℎ ℎ | 𝑡 𝑡−1 ℎ |     |     |
| --- | --- | --- | --- | ----- | ------- | --- | --- |
matrix that maps problem features into the 𝐾-dimensional representa- ⎪𝒉 ⊙𝒉̃
|             |     |     |                        | 𝑡 =(1−𝒛)⊙𝒉 𝑡 𝑡−1 | +𝒛 𝑡 𝑡 ,                                        |     |     |
| ----------- | --- | --- | ---------------------- | ---------------- | ----------------------------------------------- | --- | --- |
| tion space. |     |     | ⎩                      |                  |                                                 |     |     |
|             |     |     | where the reset gate 𝒖 |                  |  controls the influence of the previous state 𝒉 |     |     |
Attempt Count: The number of attempts reflects a student’s behavioral  𝑡 𝑡−1
pattern in problem-solving; frequent attempts may indicate confusion  on the current candidate state, determining how much historical infor-
or difficulty, while successful consecutive attempts may be associated  mation should be forgotten. The update gate 𝒛  balances the contribu-
𝑡
with a sense of achievement. The attempt-related representation vector  tions of the previous hidden state 𝒉  and the candidate state 𝒉̃ , thereby
|     |     |     |     |     | 𝑡−1 | 𝑡   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
𝒈 is computed as: controlling the integration of historical and newly learned information.
𝑡
|     |     |     | The candidate state 𝒉̃ |     |  is generated from the current input 𝐱̃ and the  |     |     |
| --- | --- | --- | ---------------------- | --- | ------------------------------------------------ | --- | --- |
𝑡
𝒈 =Sigmoid(𝒇 ⋅𝑻), (4) previous hidden state 𝒉  under the modulation of the reset gate. The
| 𝑡   | 𝑡   |     |     |     | 𝑡−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
final hidden state 𝒉 is obtained by adaptively combining the previous
𝑡
where 𝒇 ∈{0,1}1×𝑃 is the one-hot vector representing the number of  hidden state and the  candidate state through the update gate.
𝑡
attempts, with 𝑃 being the maximum number of attempts. 𝑻 ∈ℝ𝑃×𝐾 The GRU output 𝒉 is then passed through a linear transformation fol-
𝑡
is a learnable weight matrix that maps attempt features into the 𝐾- lowed by a Sigmoid a ctivation function to produce the predicted prob-
dimensional representation space. ability 𝑟̂  of the student answering the next problem correctly:
𝑡+1
Based on the analysis above, the concatenation of the three feature
vectors produces an emotion vector, which is then processed through a  𝑟̂ =Sigmoid(𝑾 𝒉 +𝐛 ). (8)
|     |     |     |     | 𝑡+1 𝑐 𝑡 | 𝑐   |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
fully connected layer to generate the emotion prediction vector 𝐚̂:
By integrating affect-aware problem hypergraph representations with
students’ historical interaction records, this prediction module effec-
| 𝐚̂=Sigmoid(𝑾 | [𝒈 𝑠||𝒈 𝑑||𝒈 | ]+𝐛 ), | (5) |     |     |     |     |
| ------------ | ------------ | ------ | --- | --- | --- | --- | --- |
𝑎 𝑡 𝑎 tively captures the students’ knowledge states and affective features,
thereby enhancing the accuracy of next-response prediction.
| where 𝑾      |  and 𝐛  are the learnable parameters of the fully connected     |     |                                    |     |     |     |     |
| ------------ | --------------------------------------------------------------- | --- | ---------------------------------- | --- | --- | --- | --- |
| 𝑎            | 𝑎                                                               |     |                                    |     |     |     |     |
| layer, and   |  denotes the vector concatenation operation. The emotion        |     |                                    |     |     |     |     |
|              | | |                                                             |     | 4.4.  Loss and optimization module |     |     |     |     |
| prediction   | v ector 𝐚̂ serves as the feature representation of the emotion  |     |                                    |     |     |     |     |
| layer node 𝑣 | ∈𝑉 , characterizing the student’s emotional state during        |     |                                    |     |     |     |     |
𝑎 𝑎 The objective of this module is to optimize both the prediction of
the problem-solving process.
student knowledge states and the perception of emotional states. The
total loss function consists of two parts: the prediction loss and the affect
perception loss. The affect perception module uses either a supervised
4.2.  Affect-aware hypergraph convolution
learning or an unsupervised contrastive learning approach, depending
The integration of the exercise layer and the affective layer con- on whether labeled affect data is available in the dataset.
structs an affect-aware problem-concept hypergraph representation.  Prediction Loss. The prediction loss measures the discrepancy between
During the affect-aware hypergraph convolution process, node updates  the predicted correctness and the ground-truth responses. We adopt the
are influenced by both the associated hyperedge features and the af- cross-entropy loss function, defined as:
fective vector 𝐚̂. Specifically, the affective vector 𝐚̂ acts as a weighting
𝑁−1
|     |     |     |    | 1 ∑( |     | )   | (9) |
| --- | --- | --- | --- | ---- | --- | --- | --- |
factor, element-wise modulating the hyperedge features 𝒉  to amplify  𝑝 =− 𝑟 𝑡+1 log(𝑟̂ 𝑡+1 )+(1−𝑟 𝑡+1 )log(1−𝑟̂ 𝑡+1 ) ,
|                                                                 |     | 𝑐   |     | 𝑁   |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| the impact of affective information in the node update process. |     |     |     | 𝑡=1 |     |     |     |
Given the interaction-aware one-hot representation 𝐪̂ ∈{0,1}2|  𝑞|,  where 𝑁 denotes the total number of interaction records and i indexes
𝑖
constructed as onehot(𝑞 +𝑟 ⋅|  𝑞|), where   denotes the exercise set  a single interaction record, 𝑟 ∈{0,1} represents the ground-truth re-
|     | 𝑖   | 𝑖 𝑞 |     |     | 𝑡+1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
and    represents the total number of exercises, which encodes both  sponse at the next interaction step, and 𝑟̂  denotes the predicted prob-
| | 𝑞| |     |     |     |     | 𝑡+1 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
the target exercise index 𝑞 and the corresponding binary response cor- ability of answering correctly at the corresponding interaction step.
𝑖
rectness 𝑟 ∈{0,1}, the final affect-aware exercise representation is com- Affect Loss. The affect loss varies depending on whether labeled affect
𝑖
| puted as follows: |     |     | data is available. |     |     |     |     |
| ----------------- | --- | --- | ------------------ | --- | --- | --- | --- |
5

C. Huang et al.
Expert Systems With Applications 331 (2026) 133323
| 1) Supervised Learning: When true affect data is available, we use  |     |     |     | Table 2  |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- |
the Mean Squared Error (MSE) loss to measure the error between the  Statistics of dataset.
predicted and the true affect values. The supervised affect loss is given
|     |     |     |     |  Statistics  ASSIST2009 |  ASSIST2012 |  ASSIST2017 |     |
| --- | --- | --- | --- | ----------------------- | ----------- | ----------- | --- |
by:
|     |     |     |     |  #Students  3831   |  27,405 |  1709 |     |
| --- | --- | --- | --- | ------------------ | ------- | ----- | --- |
|     | 𝑁   |     |     |  #Problems  16,877 |  47,104 |  3162 |     |
1 ∑
| 𝑠 = | (𝑎 −𝑎̂)2, |     | (10) |  #Concepts  101    |  265       |  102     |     |
| ---- | --------- | --- | ---- | ------------------ | ---------- | -------- | --- |
| 𝑎 𝑁  | 𝑖 𝑖       |     |      |                    |            |          |     |
| 𝑖=1  |           |     |      |  #Records  274,092 |  2,621,374 |  942,816 |     |
where 𝑎 is the true affect value and 𝑎̂ is the predicted affect value for
| 𝑖   |     | 𝑖   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
the 𝑖th sample.
2) Unsupervised Contrastive Learning: In the absence of true af- • ASSISTments 2009 (ASSIST09)1 is one of the most widely used
fect data, we adopt a contrastive learning approach. We define positive  datasets in the realm of KT, which is provided by ASSISTments online
pairs as interactions sharing the same answer (both correct or both in- tutoring platform . In our experiments, we utilize the "skill-builder-
data-corrected-collapsed" version of this dataset. We also remove
correct) and negative pairs as interactions with different answers (one
users with less than three records to enhance data modeling.
correct, one incorrect). We assume that positive pairs tend to exhibit
ASSISTments 2012 (ASSIST12)2 is the dataset from the 2012-2013
| similar latent affective tendencies, whereas negative pairs tend to ex- |     |     | •   |     |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
school year, containing affective state predictions, and has been
hibit relatively different affective tendencies. From the perspective of
educational psychology (D’Mello & Graesser, 2012), learners’ affective  widely used in educational research related to emotion data. In our
states are dynamically coupled with performance outcomes: repeated in- data processing, we removed records that lacked skill tags and scaf-
correct responses are often accompanied by increased frustration or anx- folded problems, as well as users with fewer than three records.
iety, while sustained correct responses are associated with confidence  • ASSISTments 2017 (ASSIST17)3 ASSISTments 2017 was collected
and positive engagement. Therefore, response correctness can serve as  for the ASSISTments Longitudinal Data Mining Competition in 2017.
a coarse but informative proxy for underlying affective states. The co- As part of the data mining competition, this dataset contains the most
sine similarity between positive and negative pairs is then defined as: descriptive information from the ASSISTments data.
| 𝐚   | ⋅𝐚 𝐚 | ⋅𝐚  |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- |
𝑖 𝑗 𝑘𝑖 𝑘𝑗 (11) Both ASSISTments2017 and ASSISTments2012 provide four affective
| 𝑠 𝑖,𝑗 = | , 𝑠 𝑘𝑖,𝑘𝑗 = | .   |     |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- | --- | --- |
‖𝐚 𝑖‖‖𝐚 𝑗‖ ‖𝐚 𝑘𝑖 ‖‖𝐚 𝑘𝑗 ‖ states, namely bored, concentrating, confused, and frustrated, with each
The total contrastive loss is computed as: affective value ranging from 0 to 1. These affective labels are generated
by validated sensor-free affect detection models  (Botelho et al., 2017;
e x p(𝑠 ∕ 𝜏 )
𝑐 1 ∑ 𝑖 ,𝑗 (12) P a rd os   e t   a l. ,   2 0 1 3 ) .  T r a i n ed   o n   s y n c h r o n iz e d   c l as s r o o m   o b se r v a t io n s
| =−  | log∑ | ,   |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- |
𝑎 | |(𝑖,  e x p ( 𝑠 ∕𝜏) an d  fi n e - g r a i n e d in t e r a c ti o n  l o g s ,  t h e m o d e ls o u t p u t c o nfi d e n c e  s c o r e s
|     | 𝑗)∈ (𝑘𝑖,𝑘𝑗 )∈ | 𝑘𝑖,𝑘𝑗 |     |     |     |     |     |
| --- | -------------- | ----- | --- | --- | --- | --- | --- |
in [0,1] that represent the estimated intensity of each affective state.
where  is the set of positive pairs,  is the set of negative pairs, and
𝜏 is the temperature parameter. Following prior work, we directly use these scores as affective supervi-
The total loss is the weighted sum of the prediction loss and the affect  sion signals. In contrast, ASSISTments2009 does not contain affective
| loss, represented as: |     |     | information.                           |     |     |     |     |
| --------------------- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
| = +𝜆⋅              | ,   |     | (13)                                   |     |     |     |     |
| 𝑝                     | 𝑎   |     | 5.2.  Baselines and evaluation metrics |     |     |     |     |
where   denotes the affect loss, which takes different forms depending
𝑎
on the availability of labeled affect data: if affect labels are available,  To validate the performance of AHGKT, we compare our model with
|  =𝑠 ; otherwise,  | =𝑐 . 𝜆 is a hyperparameter that balances the  |     |                                 |     |     |     |     |
| -------------------- | ---------------------------------------------- | --- | ------------------------------- | --- | --- | --- | --- |
| 𝑎 𝑎                  | 𝑎 𝑎                                            |     | the following baseline methods. |     |     |     |     |
contribution of the prediction loss and the affect loss.
DKT (Piech et al., 2015): It is the pioneering model that employs
•
5.  Experiments deep learning techniques in knowledge tracing. In our implementa-
tion, we employed LSTM to predict students’ performance.
In this section, we conducted extensive experiments and provided
|     |     |     | • DKVMN (Zhang et al., 2017): It constructs a key-value memory net- |     |     |     |     |
| --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- |
detailed descriptions of the experimental setup. Experiments were con-
work to obtain student knowledge states, where the key matrix stores
ducted on a Linux server equipped with five NVIDIA RTX A6000  static potential knowledge concepts and the value matrix maintains
GPUs (48 GB memory each), using CUDA 12.1 and NVIDIA driver ver- dynamically updated student mastery information.
sion 530.30.02. By addressing the following four questions, we aim to  • SAKT (Pandey & Karypis, 2019): It relies on attention mechanism to
demonstrate the performance advantages of the AHGKT model: make predictions by capturing relevant interactions in the past.
SAINT (Choi et al., 2020):It is based on the Transformer architecture
| RQ1: Does AHGKT improve knowledge state prediction performance  |     |     | •   |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
• and leverages self-attention mechanisms to capture students’ interac-
compared to other models?
tion histories. Stacked self-attention layers and positional encoders
RQ2: How do different components of the AHGKT model impact the
| •   |     |     | are used for prediction. |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | --- | --- |
final prediction performance?
RQ3: Can unsupervised contrastive learning effectively train the  • AKT (Ghosh et al., 2020): It integrates the attention mechanism with
•
the IRT model, employing self-attention to acquire context-aware
affective-aware module?
representations of questions and responses. Additionally, it utilizes
• RQ4: Can AHGKT effectively capture the evolution of students’
a knowledge retriever module to access relevant knowledge for the
knowledge states?
current problem.
|     |     |     | • GKT (Nakagawa et al., 2019): It models knowledge components and  |     |     |     |     |
| --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- |
5.1.  Datasets
their dependencies as a graph structure and reformulates knowledge
We conducted experiments on three benchmark datasets in the field
of online education and compared the performance of our model with
|     |     |     | 1 https://sites.google.com/site/assistmentsdata/home/ |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
various types of knowledge tracing models. Table 2 presents the number
2009-2010-assistment-data
of students, questions, skills, and total exercise records for each of the
|                 |     |     | 2 https://sites.google.com/site/assistmentsdata/datasets/ |     |     |     |     |
| --------------- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
| three datasets. |     |     | 2012-13-school-data-with-affect                           |     |     |     |     |
The brief description of each dataset is as follows. 3 https://sites.google.com/view/assistmentsdatamining/
6

C. Huang et al.
Expert Systems With Applications 331 (2026) 133323
Table 3
Comparison of AUC and ACC on ASSIST2012 and ASSIST2017 datasets.
|     |     |  ASSIST12 |  ASSIST17 |     |     |
| --- | --- | --------- | --------- | --- | --- |
Methods
|     |        | AUC ACC       | AUC ACC       |     |     |
| --- | ------ | ------------- | ------------- | --- | --- |
|     |  DKT   | 0.7271 0.7339 | 0.7167 0.6912 |     |     |
|     |  DKVMN | 0.7235 0.7244 | 0.7032 0.6775 |     |     |
|     |  SAKT  | 0.7156 0.7192 | 0.6728 0.6546 |     |     |
 SAINT
|     |        | 0.7421 0.7458 | 0.7405 0.7298 |     |     |
| --- | ------ | ------------- | ------------- | --- | --- |
|     |  AKT   | 0.7681 0.7628 | 0.7723 0.7235 |     |     |
|     |  DGEKT | OOM OOM       | 0.7776 0.7225 |     |     |
|     |  ASIKT | 0.7589 0.7438 | 0.7916 0.7328 |     |     |
 AHGKT
|                                                                         |              | 0.8103 0.7936 | 0.7986 0.7336 |     |     |
| ----------------------------------------------------------------------- | ------------ | ------------- | ------------- | --- | --- |
|                                                                         |  Improvement | 5.49% 4.05%   | 0.88% 0.11%   |     |     |
| tracing as a time-series node-level classification problem using graph  |              |               | Table 4       |     |     |
neural networks. Comparison of AUC and ACC on ASSIST2009 datasets.
PEBG (Liu et al., 2020): It formalizes question-concept relationships
| •   |     |     | Methods | AUC | ACC |
| --- | --- | --- | ------- | --- | --- |
as bipartite graphs and incorporates a product layer to acquire ques-
| tion embeddings for knowledge tracing. |     |     | DKT   | 0.7356 | 0.7081 |
| -------------------------------------- | --- | --- | ----- | ------ | ------ |
|                                        |     |     | DKVMN | 0.7394 | 0.6182 |
• DGEKT (Cui et al., 2024): It constructs a hypergraph and a directed  SAKT 0.7616 0.7578
transition graph from student learning interactions to learn node em- AKT 0.8011 0.7762
|     |     |     | PEGB | 0.8011 | 0.7766 |
| --- | --- | --- | ---- | ------ | ------ |
beddings. The model integrates both graphs into a teacher model and
|     |     |     | DGEKT | 0.7510 | 0.7223 |
| --- | --- | --- | ----- | ------ | ------ |
uses an online knowledge distillation to transfer the teacher model’s
|     |     |     | ASIKT | 0.7978 | 0.7519 |
| --- | --- | --- | ----- | ------ | ------ |
knowledge to the student model.
|     |     |     | AHGKT | 0.8289 | 0.7941 |
| --- | --- | --- | ----- | ------ | ------ |
• ASIKT (Qin et al., 2025): It combines difficulty-aware attention with
|     |     |     | Improvement | 3.47% | 2.25% |
| --- | --- | --- | ----------- | ----- | ----- |
a selective state space model to enhance interpretability while ef-
ficiently modeling the dynamic evolution of students’ knowledge
states. formance of ASSIST2009 data set without affective labels. The scores of
AUC and ACC are 0.8289 and 0.7941 respectively. AUC has increased by
This study frames knowledge tracing as a binary classification task,  3% compared with the best baseline model, indicating that our method
aiming to predict the correctness of a student’s next response (where 1  can improve greatly even without affective labels. It further proves that
indicates correct and 0 indicates incorrect). To evaluate model perfor-
students’ affective state can effectively affect students’ knowledge mas-
mance, Area Under the Curve (AUC) and Accuracy (ACC) metrics are
tery state.
used. In the experiments, a loss coefficient 𝜆 is introduced within the
affective module to balance its impact on the overall training objective.
5.4.  Ablation study (RQ2)
We randomly select 80% of students for training, and the remaining
20% of students for testing. In this section, we will address Q2 by conducting ablation experi-
ments on the model. First, we validate the effectiveness of the affective
5.3.  Results and discussions (RQ1) interaction and hypergraph structure on three datasets. Then, we ex-
plore the effectiveness of each factor in the affective interaction module.
Table 3 shows the AUC and ACC scores for the baseline method on
the two datasets. The AUC scores of the proposed AHGKT model on  5.4.1.  Component adjustment
the ASSIST2012 and ASSIST2017 datasets are 0.8103 and 0.7936, and  As shown in Table 5, it is evident that both the affective module and
the ACC scores are 0.7986 and 0.7336, respectively. As can be seen,  the hypergraph structure play critical roles in enhancing the predictive
AHGKT achieved the best results on all datasets, with AUC improving by
performance of the knowledge tracing model. Firstly, the model with-
up to 5% compared to the optimal baseline model. In addition, DGEKT
out the affective module (AHGKT-NF) shows a noticeable decrease in
encountered an out-of-memory (OOM) issue on the ASSIST2012 dataset  both AUC and ACC across all datasets, with significant drops observed
due to its relatively large parameter size and memory consumption, and  in ASSIST2009 and ASSIST2012, where the AUC scores fell to 0.7326
thus could not be successfully trained under our unified experimental  and 0.7281, respectively. This indicates that the affective module ef-
configuration. fectively captures changes in students’ affective states, contributing to
AHGKT demonstrated its ability to effectively diagnose students’  more accurate predictions of knowledge mastery. Secondly, replacing
mastery of knowledge by capturing the relationship between students’  the hypergraph with an ordinary graph (AHGKT-OG) results in a sub-
affective data and learning behaviors such as exercise difficulty and  stantial performance decline on the ASSIST2017 dataset, with the AUC
number of attempts. Unlike models such as DKT and DKVMN, which  dropping to 0.7324. Here, the ordinary graph refers to a conventional
primarily model learning sequences based on interaction information,  pairwise graph structure, where each edge connects only two nodes. The
AHGKT further incorporates an affect-aware hypergraph structure to
hypergraph structure excels at capturing the complex relationships be-
capture the high-order relationships between exercises and knowledge
tween questions and skills, enabling the model to better represent the
concepts, as well as their interactions with affective factors. Dataset per- dependencies among knowledge points. These results demonstrate that
formance differences mainly arise from the sparsity of emotional fea- the inclusion of both the affective module and the hypergraph structure
tures. In the small-scale ASSIST2017, limited affective signals constrain  significantly enhances AHGKT’s performance, making it well-suited for
the model’s learning, whereas the larger ASSIST2012 provides sufficient  knowledge tracing tasks.
non-zero observations for robust exploitation. The hypergraph structure
propagates sparse signals globally, and the adaptive attention mecha- 5.4.2.  Hyper-parameter analysis
nism filters noise, enabling AHGKT to achieve greater improvements  The parameter 𝜆 is a balancing factor between the prediction loss and
when emotional features are abundant (Fig. 3). Table 4 shows the per- the loss of the affect perception module. It is tuned within the range of
7

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
Fig. 3. AUC performance comparisons on the ASSIST2012 (a), ASSIST2017 (b), and ASSIST2009 (c) datasets.
Table 5 Table 6
Performance comparison across ASSIST datasets. Comparison of supervised and unsupervised training performance on af-
fective perception module.
Methods Metrics ASSIST17 ASSIST12 ASSIST09
ASSIST12 ASSIST17
AUC 0.7677 0.7281 0.7326 Methods
AHGKT-NF
ACC 0.7142 0.7294 0.7142 AUC ACC AUC ACC
AUC 0.7324 OOM 0.7719 Supervised 0.8103 0.7937 0.7986 0.7337
AHGKT-OG
ACC 0.6934 OOM 0.7545 Unsupervised 0.8097 0.7942 0.7962 0.7316
AHGKT AUC 0.7986 0.8103 0.8290 Difference 0.05% 0.06% 0.24% 0.20%
ACC 0.7337 0.7937 0.7941
the loss function, and the other using unsupervised contrastive learn-
ing loss without labels, training by constructing positive and negative
sample pairs.
As shown in Table 6, the model performance is nearly identical un-
der both training approaches, with similar performance outcomes. This
indicates that the unsupervised contrastive learning method may learn
representations that effectively encode behavioral patterns associated
with students’ affective states, thereby improving prediction accuracy
even without direct affective supervision. This result suggests that un-
supervised contrastive learning can serve as an effective training strat-
egy for the affective perception module, particularly in scenarios with
limited labeled data.
Fig. 4. Impact of 𝜆 on model performance (AUC and ACC). 5.6. Visualization (RQ4)
The radar chart in Fig. 5 shows the changes in student mastery across
five knowledge concepts (34, 39, 40, 41, 46). The red and blue lines rep-
resent the mastery levels before practice and after practice, respectively.
It is evident that the student shows significant improvement in knowl-
edge concepts 34 and 39, particularly in concept 34. This indicates that
the knowledge tracing model can effectively capture student progress
across different concept points.
Fig. 6 illustrates the evolution of a student’s knowledge state over
time using a sample from the ASSIST2017 dataset. The upper Q-row
corresponds to the problem sequence indices, while the R-row repre-
sents the student’s actual responses. By comparing the prediction results
of the AHGKT-Noaffect model (Fig. 6(a)), the DGEKT model (Fig. 6(b)),
Fig. 5. Radar chart of student knowledge concept mastery changes.
and the AHGKT model (Fig. 6(c)), we analyze the differences in how the
three models capture the student’s mastery of four knowledge concepts
0.001 to 10. As shown in the Fig. 4, the model achieves optimal perfor- (IDs 34, 39, 40, and 41, corresponding to multiplication, subtraction,
mance in both AUC and ACC when 𝜆 is set to 1. Overemphasizing either addition, and division, respectively). The horizontal axis denotes the
the affect module or the prediction loss leads to a decline in model per- problem (or response) sequence index, and the vertical axis represents
formance. the knowledge concept index. In the heatmap, the color intensity in-
dicates the predicted probability that the student will correctly master
5.5. Valid analysis (RQ3) the corresponding knowledge concept at the next time step; darker col-
ors indicate higher predicted mastery probability, while lighter colors
In this experiment, to verify the effectiveness of unsupervised con- indicate lower predicted mastery probability.
trastive loss in the affective perception module, we adopted two training Several key observations can be made from these visualizations.
approaches on a dataset with real affective labels: one based on affec- First, as practice on a specific knowledge concept increases, the model’s
tive labels using supervised learning with mean squared error (MSE) as predicted probability of mastering that concept rises significantly, align-
8

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
Fig. 6. Top: Exercise sequence and corresponding response outcomes. Bottom: Heat maps of different models. The x-axis denotes the sequence of exercises, and
the y-axis indicates knowledge concept IDs (34: multiplication, 39: subtraction, 40: addition, 41: division). The color intensity reflects the predicted probability of
mastering each concept.
ing with real-world learning patterns. For example, we further examine mastery probabilities of the other three related knowledge concepts, as
the model dynamics over a continuous sequence segment (questions 14- indicated by the yellow box in Fig. 6(c). This suggests that the AHGKT
20) for concept 39. As shown in the green boxes in Fig. 6, the AHGKT model is able to capture implicit relationships among addition, subtrac-
model demonstrates adaptive variations in its predicted mastery proba- tion, multiplication, and division. In contrast, the other two models do
bility that are more aligned with the student’s actual response patterns not fully exhibit this feature.
(consistent with the R-row response results shown in the upper part of
Fig. 6). In contrast, the DGEKT model shows relatively stable outputs
5.7. Model complexity analysis
with limited sensitivity to changes in student responses. Furthermore,
while the AHGKT-Noaffect model initially predicts a higher mastery To evaluate the computational efficiency of AHGKT, we analyzed
probability for knowledge concept 34, its probability decreases after re- both the theoretical complexity and actual runtime of its main compo-
peated practice, failing to accurately reflect knowledge acquisition, as nents on the ASSIST2017 dataset. For sequence modeling, DKT’s RNN
indicated by the red box in Fig. 6(a). has a computational complexity of 𝑂(𝑇 ⋅𝐻⋅(𝐻+𝐷)), where 𝑇 is the
Second, answering questions related to a specific knowledge concept sequence length, 𝐻 is the hidden dimension, and 𝐷 is the input dimen-
impacts not only the knowledge state of that concept, but also those sion. AHGKT introduces hypergraph convolution (HGNN) with com-
of related concepts. For example, in the AHGKT model, when problem plexity 𝑂(𝑁⋅𝐷2) and an affective modulation module with complexity
140 corresponds to knowledge concept 40 (addition), a correct response 𝑂(𝑁⋅𝑆), which adds limited overhead compared to the multi-step RNN
leads to a significant increase in its predicted probability, along with the computations. Table 7 presents a comparison of parameter count, train-
9

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
Table 7 Acknowledgements
Comparison of model complexity and performance on AS-
SIST2017. This work was supported by the National Natural Science Foundation
Model Params (M) Train (s) Inference (s) AUC of China (No. 62337001).
DKT 2.498 378 101 0.7271
DGEKT 10.596 390 75 0.7747
AHGKT 6.405 115 15 0.7947
References
Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. ACM Com-
puting Surveys, 55(11), 1–37.
ing and inference time per epoch, and predictive performance (AUC) on Baker, R. S. J. d., Corbett, A. T., & Aleven, V. (2008). More accurate student modeling
ASSIST2017. through contextual estimation of slip and guess probabilities in bayesian knowledge
tracing. In Intelligent tutoring systems: In proceedings of the 9th international conference,
The results show that, despite introducing hypergraph and affective
ITS 2008, montreal, canada, june 23–27, 2008 proceedings 9 (pp. 406–415). Springer.
modules, AHGKT maintains a moderate parameter size, achieves sig- Botelho, A. F., Baker, R. S., & Heffernan, N. T. (2017). Improving sensor-free affect detec-
nificantly faster training and inference, and improves predictive perfor- tion using deep learning. In International conference on artificial intelligence in education
(pp. 40–51). Springer.
mance on ASSIST2017, demonstrating a good balance between compu-
Chen, C., Cheng, Z., Li, Z., & Wang, M. (2020). Hypergraph attention networks. In In
tational complexity and effectiveness. proceedings of the 2020IEEE 19th international conference on trust, security and privacy
in computing and communications (trustcom) (pp. 1560–1565). IEEE.
Choi, Y., Lee, Y., Cho, J., Baek, J., Kim, B., Cha, Y., Shin, D., Bae, C., & Heo, J. (2020).
6. Conclusion Towards an appropriate query, key, and value computation for knowledge tracing. In
In proceedings of the seventh ACM conference on learning@ scale (pp. 341–344).
Corbett, A. T., & Anderson, J. R. (1994). Knowledge tracing: Modeling the acquisition of
We present an affective hypergraph knowledge tracing (AHGKT), a
procedural knowledge. User Modeling and User-Adapted Interaction, 4, 253–278.
knowledge tracing framework that innovatively integrates affective dy- Craig, S., Graesser, A., Sullins, J., & Gholson, B. (2004). Affect and learning: An exploratory
namics through a bilevel hypergraph architecture. The exercise layer look into the role of affect in learning with autotutor. Journal of Educational Media,
models high-order question-concept relationships, while the affective
Cui,
2 9
C
(
.,
3 )
Y
,
a
2
o
4
,
1
Y
–
.
2
,
5
Z
0
h
.
ang, C., Ma, H., Ma, Y., Ren, Z., Zhang, C., & Ko, J. (2024). DGEKT:
layer tracks emotion-driven behavioral patterns. Our affect-aware hy- A dual graph ensemble learning method for knowledge tracing. ACM Transactions on
pergraph convolution mechanism fuses these cognitive and emotional Information Systems, 42(3), 1–24.
D’Mello, S., & Graesser, A. (2012). Dynamics of affective states during complex learning.
signals via multilayer message passing, enabling precise knowledge state
Learning and Instruction, 22(2), 145–157.
modeling. Evaluations across three datasets demonstrate AHGKT’s supe- Feng, Y., You, H., Zhang, Z., Ji, R., & Gao, Y. (2019). Hypergraph neural networks. In In
riority and cross-domain robustness. By unifying hypergraph learning proceedings of the AAAI conference on artificial intelligence (pp. 3558–3565). (vol. 33).
with affective computing, this work advances educational AI through Ghosh, A., Heffernan, N., & Lan, A. S. (2020). Context-aware attentive knowledge tracing.
In In proceedings of the 26th ACM SIGKDD international conference on knowledge discovery
two critical insights: affective states are quantifiable predictors of learn- & data mining (pp. 2330–2339).
ing outcomes, and hypergraphs inherently capture the multidimensional Graves, A. (2013). Generating sequences with recurrent neural networks. arXiv preprint
interactions in learning systems. The framework provides a blueprint for arXiv:1308.0850, .
Graves, A., Mohamed, A.-r., & Hinton, G. (2013). Speech recognition with deep recurrent
emotionally intelligent tutoring tools that address both cognitive and af-
neural networks. In In proceedings of the 2013IEEE international conference on acoustics,
fective dimensions of education. speech and signal processing (pp. 6645–6649). Ieee.
In future work, we will explore rapid adaptation mechanisms (e.g., Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation,
meta-learning) to improve modeling for new users, and investigate
Hua
9
n
(
g
8
,
)
C
, 1
.,
7
W
35
ei
–
,
1
H
7
.
8
,
0
H
.
uang, Q., Jiang, F., Han, Z., & Huang, X. (2024a). Learning consistent
cross-domain representation learning to enhance transferability across representations with temporal and causal enhancement for knowledge tracing. Expert
courses and platforms. We also plan to incorporate richer behavioral sig- Systems with Applications, 245, 123128.
Huang, C.-Q., Huang, Q.-H., Huang, X., Wang, H., Li, M., Lin, K.-J., & Chang, Y. (2024b).
nals and adopt a causal perspective to better understand the dynamic
XKT: Toward explainable knowledge tracing model with cognitive learning theories
interplay between affect and knowledge acquisition, thereby improving for questions of multiple knowledge concepts. IEEE Transactions on Knowledge and Data
the robustness and interpretability of affect-aware knowledge tracing Engineering, 36(11), 7308–7325.
Käser, T., Klingler, S., Schwing, A. G., & Gross, M. (2017). Dynamic bayesian networks for
systems.
student modeling. IEEE Transactions on Learning Technologies, 10(4), 450–462.
Kipf, T. N., & Welling, M. (2016). Semi-supervised classification with graph convolutional
networks. arXiv preprint arXiv:1609.02907, .
CRediT authorship contribution statement Lee, J. I., & Brunskill, E. (2012). The impact on individualizing student models on neces-
sary practice opportunities. International Educational Data Mining Society, 118–125.
Changqin Huang: Conceptualization, Investigation, Resources, Lipton, Z. C., Berkowitz, J., & Elkan, C. (2015). A critical review of recurrent neural net-
works for sequence learning. arXiv preprint arXiv:1506.00019, .
Writing – original draft; Xi Cheng: Data curation, Methodology, Writing Liu, S., Liu, S., Liu, Z., Peng, X., & Yang, Z. (2022). Automated detection of emotional and
– original draft; Yi Wang: Conceptualization, Formal analysis, Supervi- cognitive engagement in MOOC discussions to predict learning achievement. Comput-
sion, Writing – review & editing; Huicheng Zeng: Visualization, Re- ers & Education, 181, 104461.
sources, Supervision, Writing – review & editing; Xiaodi Huang: Visu- Liu,
t r
Y
a
.
c
,
in
Y
g
a n
v
g
ia
, Y
p
.
r
,
e -
C
t
h
ra
e
i
n
n
,
i n
X
g
.,
q
S
u
h
e
e
s
n
ti
,
o
J
n
. ,
e m
Zh
b
a
e
n
d
g
d
,
i n
H
g
.
s
,
.
&
a r
Y
X
u
iv
, Y
pr
.
e
(
p
2
r
0
in
2
t
0 )
a
.
r X
Im
iv
p
:2
ro
0
v
1
i
2
n
.
g
0 5
k
0
n
3
o
1
w
,
l
.
edge
alization, Investigation, Validation, Writing – review & editing; Qiong- Mehta, K. J. (2022). Effect of sleep and mood on academic performance-at interface of
hao Huang: Visualization, Validation, Supervision, Writing – review & physiology, psychology, and education. Humanities and Social Sciences Communications,
editing. 9(1), 1–13.
Nakagawa, H., Iwasawa, Y., & Matsuo, Y. (2019). Graph-based knowledge tracing:
Modeling student proficiency using graph neural network. In In proceedings of the
Declaration of competing interest
Pan
I
d
E
e
E
y
E
,
/
S
W
.,
I C
&
/ A
K
C
a
M
ry p
in
is
t
,
e r
G
na
.
t
(
io
2
n
0
a
1
l
9
c
)
o
.
n
A
fe r
s
e
e
n
l
c
f-
e
a
o
tt
n
e n
w
t
e
iv
b
e
i n
m
te
o
ll
d
ig
e
e
l
n c
fo
e
r
( p
k
p
n
.
o
1
w
5
l
6
e
–
d
1
g
6
e
3
t
)
r
.
acing. arXiv
preprint arXiv:1907.06837, .
The authors declare that they have no known competing financial Pardos, Z. A., Baker, R. S., San Pedro, M. O., Gowda, S. M., & Gowda, S. M. (2013). Affec-
interests or personal relationships that could have appeared to influence tive states and state tests: Investigating how affect throughout the school year predicts
end of year learning outcomes. In In proceedings of the third international conference on
the work reported in this paper.
learning analytics and knowledge (pp. 117–124).
Pardos, Z. A., & Heffernan, N. T. (2010). Modeling individualization in a bayesian net-
works implementation of knowledge tracing. In User modeling, adaptation, and person-
Data availability alization:in proceedings of the 18th international conference, UMAP 2010, big island, HI,
USA, june 20–24, 2010. proceedings 18 (pp. 255–266). Springer.
The manuscript already contains the links to the publicly available Pedro, M. O., Baker, R., Bowers, A., & Heffernan, N. (2013). Predicting college enroll-
ment from student interaction with an intelligent tutoring system in middle school. In
datasets used in the paper.
Educational data mining 2013. Citeseer.
10

C. Huang et al. Expert Systems With Applications 331 (2026) 133323
Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., &
J. (2015). Deep knowledge tracing. Advances in Neural Information Processing Systems, Polosukhin, I. (2017). Attention is all you need. Advances in Neural Information Pro-
28 505–513. cessing Systems, 30, 5998–6008.
Qin, Y., Zhu, X., Tang, X., Zhang, C., Wu, K., Chang, F., Diao, J., & Hu, Z. (2025). Inter- Wang, C., Zhu, H., Wang, P., Zhu, C., Zhang, X., Chen, E., & Xiong, H. (2021). Personalized
pretable knowledge tracing with difficulty-aware attention and selective state space and explainable employee training course recommendations: A bayesian variational
model. In Proceedings of the 48th international ACM SIGIR conference on research and approach. ACM Transactions on Information Systems (TOIS), 40(4), 1–32.
development in information retrieval (pp. 316–325). Wang, S., Zeng, Z., Yang, X., Xu, K., & Zhang, X. (2024). Boosting neural cognitive diag-
Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., & Monfardini, G. (2008). The graph nosis with student’s affective state modeling. In In proceedings of the AAAI conference
neural network model. IEEE Transactions on Neural Networks, 20(1), 61–80. on artificial intelligence (pp. 620–627). (vol. 38).
Shen, S., Huang, Z., Liu, Q., Su, Y., Wang, S., & Chen, E. (2022). Assessing student’s dy- Wu, Z., Huang, L., Huang, Q., Huang, C., & Tang, Y. (2022). SGKT: Session graph-based
namic knowledge state by exploring the question difficulty effect. In In proceedings of knowledge tracing for student performance prediction. Expert Systems with Applications,
the 45th international ACM SIGIR conference on research and development in information 206, 117681.
retrieval (pp. 427–437). Xiong, X., Zhao, S., Van Inwegen, E. G., & Beck, J. E. (2016). Going deeper with deep
Song, X., Li, J., Lei, Q., Zhao, W., Chen, Y., & Mian, A. (2022). Bi-CLKT: Bi- knowledge tracing. International Educational Data Mining Society, 545–550.
graph contrastive learning based knowledge tracing. Knowledge-Based Systems, 241, Yeung, C.-K., & Yeung, D.-Y. (2018). Addressing two problems in deep knowledge trac-
108274. ing via prediction-consistent regularization. In In proceedings of the fifth annual ACM
Sonkar, S., Waters, A. E., Lan, A. S., Grimaldi, P. J., & Baraniuk, R. G. conference on learning at scale (pp. 1–10).
(2020). qDKT: Question-centric deep knowledge tracing. arXiv preprint Yudelson, M. V., Koedinger, K. R., & Gordon, G. J. (2013). Individualized bayesian knowl-
arXiv:2005.12442, . edge tracing models. In Artificial intelligence in education:in proceedings of the 16th in-
Sun, J., Du, S., Liu, Z., Yu, F., Liu, S., & Shen, X. (2023). Weighted heterogeneous graph- ternational conference, AIED 2013, memphis, TN, USA, july 9–13, 2013. proceedings 16
based three-view contrastive learning for knowledge tracing in personalized e-learning (pp. 171–180). Springer.
systems. IEEE Transactions on Consumer Electronics, 70(1), 2838–2847. Zhang, J., Shi, X., King, I., & Yeung, D.-Y. (2017). Dynamic key-value memory networks
Sun, X., Zhang, K., Shen, S., Wang, F., Guo, Y., & Liu, Q. (2024). Target hierarchy-guided for knowledge tracing. In In proceedings of the 26th international conference on world
knowledge tracing: Fine-grained knowledge state modeling. Expert Systems with Appli- wide web (pp. 765–774).
cations, 251, 123898. Zong, J., Cui, C., Ma, Y., Yao, L., Chen, M., & Yin, Y. (2020). Behavior-driven student
Tomasevic, N., Gvozdenovic, N., & Vranes, S. (2020). An overview and comparison of su- performance prediction with tri-branch convolutional neural network. In In proceedings
pervised data mining techniques for student exam performance prediction. Computers of the 29th ACM international conference on information & knowledge management (pp.
& Education, 143, 103676. 2353–2356).
11