|     | International | Journal | of Information | and Communication |
| --- | ------------- | ------- | -------------- | ----------------- |
Technology

ISSN online: 1741-8070 - ISSN print: 1466-6642
https://www.inderscience.com/ijict

| Knowledge | tracing | in mathematical | problem-solving | processes: |
| --------- | ------- | --------------- | --------------- | ---------- |
a spatio-temporal graph neural network approach

Xia Li

DOI: 10.1504/IJICT.2026.10076456

Article History:
| Received:         |     | 11 August 2025   |     |     |
| ----------------- | --- | ---------------- | --- | --- |
| Last revised:     |     | 24 November 2025 |     |     |
| Accepted:         |     | 25 November 2025 |     |     |
| Published online: |     | 05 March 2026    |     |     |
Copyright © 2026 Inderscience Enterprises Ltd.
Powered by TCPDF (www.tcpdf.org)

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

      Int. J. Information and Communication Technology, Vol. 27, No. 14, 2026  23

Knowledge tracing in mathematical problem-solving
processes: a spatio-temporal graph neural network
approach
Xia Li
The Department of Public Courses,
City University of Wuhan,
Wuhan, 430083, China
Email: lixia888666@126.com
Abstract: A novel modelling method incorporating spatio-temporal graph
neural networks is proposed for the knowledge tracking problem in the process
|     |     | of  mathematical  | problem  | solving.  | In  the  spatial  | dimension,  | the  complex  |     |     |
| --- | --- | ----------------- | -------- | --------- | ----------------- | ----------- | ------------- | --- | --- |
relationships among three types of nodes, namely, students, exercises and
knowledge points, are integrated through a heterogeneous graph structure, and
|     |     | a  knowledge  | graph  is  | dynamically  | constructed  | to  capture  | the  implicit  |     |     |
| --- | --- | ------------- | ---------- | ------------ | ------------ | ------------ | -------------- | --- | --- |
associations among concepts; in the temporal dimension, a dual time encoder
and a memory gate mechanism are introduced to differentiate the semantic
differences between long and short time intervals, and a temporal sequential
convolution network is used to model the cumulative evolution characteristics
of the problem solving sequences. It is experimentally demonstrated that the
|     |     | prediction  | accuracy  of  | this  method  | is  improved  | by  5.3%–6.7%,  | which  |     |     |
| --- | --- | ----------- | ------------- | ------------- | ------------- | --------------- | ------ | --- | --- |
significantly optimises the ability to track the dynamic changes of students’
cognitive state and provides more robust decision support for personalised
learning path recommendation.
|     |     | Keywords:  | mathematical  | problem-solving  | process;  | knowledge  | tracing;   |     |     |
| --- | --- | ---------- | ------------- | ---------------- | --------- | ---------- | ---------- | --- | --- |
spatio-temporal graph neural network; STGNN.
Reference to this paper should be made as follows: Li, X. (2026) ‘Knowledge
tracing in mathematical problem-solving processes: a spatio-temporal graph
neural network approach’, Int. J. Information and Communication Technology,
Vol. 27, No. 14, pp.23–41.
|     |     | Biographical  | notes:  Xia  | Li  received  | her  Master’s  | degree  | from  Hubei  |     |     |
| --- | --- | ------------- | ------------ | ------------- | -------------- | ------- | ------------ | --- | --- |
University, China. Currently, she works in City University of Wuhan. Her
research interests include higher mathematics，linear algebra and probability
statistics.

|     | 1   | Introduction  |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
In the core area of intelligent education systems, knowledge tracking technology is
dedicated to diagnosing students’ dynamically changing knowledge mastery status in real
time and predicting their future problem solving performance by analysing their historical
learning behaviour sequences (Heng-yu et al., 2019). This ability is crucial for realising
personalised learning recommendation, precise intervention and adaptive teaching in the
      Copyright © The Author(s) 2026. Published by Inderscience Publishers Ltd. This is an Open Access Article
distributed under the CC BY license. (http://creativecommons.org/licenses/by/4.0/)

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

24 X. Li
true sense. Mathematics, with its rigorous logical structure, progressive knowledge
system, and complex cognitive skills shown in the problem solving process, has become
one of the most challenging and valuable research objects for knowledge tracking
(Giroux and Taylor, 2002). Mathematical problem solving process is not a simple
application of isolated knowledge points, but a complex cognitive activity involving
conceptual understanding, skill transfer, strategy selection and time factor. The state of
students’ knowledge in this process is essentially a high-dimensional dynamic system
that evolves in the spatial dimension of knowledge structure and is jointly shaped by
dynamic processes in the temporal dimension.
Traditional knowledge tracking models, including classical sequence-based deep
learning approaches, although have made some progress in capturing temporal
dependencies, still face significant bottlenecks in accurately modelling the mathematical
problem solving process. On the one hand, these models tend to treat the knowledge
structure as a collection of discrete or implicit labels and lack explicit modelling of
complex correlations in the knowledge space. There are naturally strong logical
connections and hierarchical structures between mathematical knowledge points, and the
solution of a problem often requires the activation and coordination of multiple related
knowledge points. Neglecting this structured spatial correlation makes it difficult for the
model to accurately characterise the mechanism of synergistic activation and migration of
knowledge points in the problem solving process, limiting its ability to understand
students’ deep cognitive states (Broncano-Berrocal, 2018). On the other hand, the
fineness of time dynamic modelling is insufficient. Most of the existing models treat time
as a uniform sequence index, or adopt an oversimplified linear/exponential forgetting
function, which makes it difficult to effectively differentiate and characterise the time
interval effects that are prevalent in the mathematics learning environment and have
different semantics: a classic example in the psychology of learning is the contrast
between two study approaches. Intensive practice in a short timeframe capitalises on the
brain’s focused engagement, leading to a swift knowledge consolidation effect where
information is temporarily held in a readily accessible state. This is often mistaken for
mastery. In contrast, allowing long time intervals to pass between sessions initially
triggers a significant forgetting effect, as the memory trace weakens without
reinforcement. Paradoxically, this struggle is beneficial. The mental effort required to
retrieve seemingly ‘forgotten’ information strengthens the memory far more effectively
than repeated easy recall. Therefore, while cramming may aid short-term performance,
distributed practice that embraces some forgetting is vastly superior for genuine, long-
term learning, a critical insight for designing effective curricula. The formation and
decline of mathematical problem solving ability does not follow a single, static pattern,
but is influenced by the nonlinear interaction of multiple factors such as the frequency of
practice, the distribution of intervals, and the difficulty of problems. In addition, the
process of mathematical problem solving involves multiple heterogeneous entities such
as students, exercises, and knowledge points, as well as their complex interactions.
Traditional models usually focus only on the student-exercise interaction sequence,
failing to fully integrate and utilise the structured knowledge embedded in this rich
heterogeneous information, and limiting the model’s ability to generalise to sparse
interaction scenarios (Manierre, 2015).
To overcome the above challenges, a novel knowledge tracking framework that can
unify the modelling of spatial structural associations and temporal evolutionary dynamics
of knowledge is urgently needed. Graph neural networks provide a natural paradigm for

Knowledge tracing in mathematical problem-solving processes 25
explicitly portraying complex dependencies among knowledge points due to their
powerful ability to model graph-structured data. The development of spatio-temporal
graph neural networks (STGNNs) further provides a powerful technical tool for fusing
spatial structural information with temporal dynamic evolution, and has demonstrated
excellent performance in the fields of physics simulation and traffic prediction. However,
its direct application to the knowledge tracking of mathematical problem solving process
still requires in-depth adaptation and innovation for the unique needs of the field.
This paper proposes a spatiotemporal graph neural network for mathematical
knowledge tracing (STGNN-MKT). The core objective of this methodological approach
is to construct a unified and interpretable spatio-temporal coupling framework. This
initiative arises from the limitation of traditional analysis that often treats spatial
knowledge structure and its temporal evolution in isolation. The proposed framework
is specifically designed to accurately capture the dynamic interplay within the
problem-solving process: it simultaneously delineates the spatial structural
evolution – referring to how conceptual components and their interrelations are organised
and reconfigured – and the temporal cumulative evolution – denoting the progressive,
step-by-step building and refinement of knowledge states. Ultimately, this model aims to
provide a holistic and mechanistic understanding of learning trajectories in mathematics.
Specifically, in the spatial dimension, we break through the limitation of homogeneous
graphs and explicitly construct a heterogeneous graph structure containing three types of
nodes: students, exercises, and knowledge points. This graph structure not only encodes
the attribution relationship between exercises and knowledge points, but also dynamically
integrates the historical interaction records between students and exercises. By
introducing the heterogeneous graph attention mechanism, the model can adaptively learn
the complex association weights among different types of nodes and generate
semantically rich node embeddings, so as to more comprehensively characterise the state
of the knowledge network in which the student is located and its association with the
problem to be solved. In the temporal dimension, we design a dual temporal encoding
mechanism: on the one hand, we introduce fine-grained temporal gating units combined
with temporally gated convolutional networks, which focus on modelling short-term
dependencies and local patterns between neighbouring steps in a dense problem solving
sequence; on the other hand, we design explicit forgetting-memory gating modules,
which incorporate a variety of features affecting forgetting behaviour, and explicitly
differentiate and quantify them using nonlinear functions systematic forgetting due to
long-term intervals from the memory-reinforcing effects created by short-term repetitive
practice. Particularly critical is that the representation of spatial structure is not severed
from the modelling of temporal dynamics. Our model dynamically evolves the state of
knowledge nodes as the sequence of student interactions advances on the time axis
through an iterative message passing and state updating mechanism; at the same time, the
state of student nodes is updated by aggregating the spatio-temporal state information of
the exercises and their associated knowledge points from their historical interactions.
This close coupling and synergistic evolution of spatio-temporal states is at the core of
the model’s ability to deeply understand the dynamic changes in students’ cognitive
states.
Through systematic experimental validation on authoritative mathematics education
datasets such as ASSISTments and KDDCup, the results show that compared with the
graph knowledge tracking baseline model and other advanced temporal knowledge
tracking models, STGNN-MKT achieves a significant and consistent improvement in the

26 X. Li
key metrics of predicting students’ future performance in answering questions. More
importantly, the model demonstrated superior time-series dynamic modelling capabilities,
especially in capturing forgetting phenomena after long intervals and knowledge leaps
during periods of intensive practice; its heterogeneous graph structure also endowed the
model with a stronger basis for interpretability, which provides a potential basis for
understanding the correlation paths of students’ knowledge gaps. This study not only
provides a more powerful tool for the dynamic characterisation of knowledge states in the
mathematical problem solving process, but also lays a solid algorithmic foundation for
the construction of a smarter and more cognitively attuned personalised learning system.
2 Related work
The core task of knowledge tracking is to dynamically assess students’ knowledge status
through their historical question-answer sequences, providing a decision basis for
individualised learning. Early studies mainly relied on probabilistic graphical models
such as Bayesian knowledge tracking (BKT). Zhang and Yao (2018) proposed a BKT
model with three learning states. We utilise the evaluation function of three-way decision
making to divide the learning process into three parts. Comparative experiments
demonstrate the advantages of this three-part approach over the traditional two-part
approach. Based on the trichotomy of the learning process, a three-learning state model is
constructed. However, the BKT assumes that the knowledge points are independent of
each other, which makes it difficult to capture the logical connections in the mathematical
knowledge system. Subsequent extensions to the model attempt to introduce multiple
knowledge point interactions, but are still limited by artificial feature engineering and
static structure assumptions.
The rise of deep learning knowledge tracking (DLKT) has significantly improved
temporal modelling capabilities: recurrent neural network-based DKT models capture
long-term dependencies through implicit state transfer (Kim et al., 2021); and models
driven by attentional mechanisms dynamically weight historical interactions to enhance
the perception of critical steps (Wang et al., 2023). To visualise the knowledge structure,
memory-enhanced models store the state of knowledge points through key-value matrices
and support dynamic updating (Chen et al., 2023). However, DLKT still has significant
limitations: most models treat knowledge points as discrete labels, ignoring hierarchical
relationships and logical dependencies between concepts.
The time interval effect is mostly reduced to linear decay or static exponential
function, which is difficult to adapt to the nonlinear cognitive laws in math learning.
To model the spatial association of knowledge, graph-based knowledge tracking (KT)
has become an emerging direction. Wu et al. (2022) proposed a knowledge tracking
model based on practice learning graphs, known as learning graph-based knowledge
tracking (SGKT). This learning graph is used to model the student’s question answering
process, and the relationship graph is used to model the relationship between practice and
skills. Then, use a gated graph neural network to extract the student’s knowledge state
from the learning graph and a graph convolutional network to extract the embedded
representations of the exercises and skills in the relational graph. Next, multiple
interaction states consisting of knowledge states and embedded representations are
obtained through the interaction mechanism. The attention mechanism is used to find the
focus from these states and make predictions. Cui et al. (2024) proposed a novel

Knowledge tracing in mathematical problem-solving processes 27
dual-graph integrated learning knowledge tracking method (DGEKT), which captures
heterogeneous practice-concept associations and interaction transitions by building a
dual-graph structure of student learning interactions through hypergraph modelling and
directed graph modelling, respectively. In order to combine the dual-graph modelling,
they introduced an online knowledge distillation technique. This choice stems from the
observation that while the knowledge-tracking model aims at predicting students’
responses to different concept-related exercises, it optimises the prediction accuracy for
only a single exercise at each step. With online knowledge refinement, the dual-graph
model can be adaptively combined to form a more powerful integrated teacher model that
uses its predictions for all exercises as additional supervision to improve modelling
capabilities.
The success of STGNN in areas such as traffic prediction provides a new paradigm
for KT. Liu et al. (2025) proposed a knowledge tracking model that unifies
spatio-temporal information – spatio-temporal Fourier knowledge tracking. The model
solves the compatibility problem between the two by extracting information from
cognitive and behavioural perspectives, fusing information in the temporal and spatial
dimensions to construct a spatio-temporal map, and processing spatio-temporal
dependent features in the frequency domain through a Fourier map neural network to
capture complex spatio-temporal relationships and improve computational efficiency and
accurate modelling of spatio-temporal features.
However, the migration of existing methods to mathematical knowledge tracking still
faces challenges: traffic/video data nodes are homogeneous, whereas KT needs to model
three types of nodes: students, exercises, and knowledge points and their multi-order
relationships at the same time; and the cognitive evolution mechanism has not been
adapted: the update of students’ knowledge state needs to follow the cognitive law of
practice reinforcement-forgotten decay, whereas the general-purpose STGNN lacks the
dedicated spatiotemporal state-transfer equations.
Based on the above analysis, this paper proposes the spatio-temporal graph neural
network knowledge tracking model, and the core innovation is reflected in three aspects:
1 Constructing a three-body heterogeneous graph of student-exercise-knowledge point,
as shown in Figure 1, to dynamically integrate the knowledge ontology relationship
and learning behaviour relationship.
2 Capturing the coherence of thinking in intensive practice with a time-sequence gated
convolutional network, and designing a forgetting-memory gate module, which
integrates the Hawkes process with a nonlinear decay function to explicitly quantify
the reinforcing effects of interval forgetting and repetitive practice. The module
integrates seven forgetting characteristics to realise the mathematical expression of
cognitive laws.
3 Knowledge node states are dynamically updated with question-answering sequences,
and student node states evolve by aggregating the spatio-temporal features of their
historical interactive exercises. A primary aim of our proposed model is to decisively
overcome the prevalent defect of spatio-temporal module fragmentation, a critical
limitation observed in existing models like DGEKT and TSKT. In these
architectures, the spatial structure of knowledge concepts and their temporal
evolution are often processed by separate, loosely connected modules. This
disconnection creates an analytical gap, preventing a genuine understanding of how

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |   28  | X. Li  |     |     |     |     |     |     |
| --- | ----- | ------ | --- | --- | --- | --- | --- | --- |

knowledge dynamically transforms during problem-solving. Our framework directly
addresses this by designing an intrinsically coupled spatio-temporal mechanism,
ensuring that the spatial organisation of knowledge and its cumulative progression
over time are modelled as two inseparable facets of a unified process. This
integration is pivotal for constructing a more coherent and accurate representation of
the learning continuum.
Figure 1  Student-exercise-knowledge points of the three-body isomorphic map (see online
version for colours)
S1
|     |     | P1 P2 | P3  | P4 P5 |     |     |     |     |
| --- | --- | ----- | --- | ----- | --- | --- | --- | --- |
Student Node
Exercise Node
Knowledge Points Node
|     |     | K1  | K2  | K3  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Learning Behavioral Relationships
knowledge Ontology

|     | 3    | Theoretical analysis           |     |     |     |     |     |     |
| --- | ---- | ------------------------------ | --- | --- | --- | --- | --- | --- |
|     | 3.1  | Knowledge tracking foundation  |     |     |     |     |     |     |
The core task of Knowledge Tracing is to dynamically assess a student’s knowledge state
s ∈ ℝd and predict the probability of answering future questions correctly p(r + 1 = 1 |
|     | t   |     |     |     |     | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
q , ) based on his/her historical interaction sequence  = (q , r , t ),…, (q , r , t ) (Shen
|     | t+1 |     |     |     | 1 1 1 | T T T |     |     |
| --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
et al., 2024). Where q is the exercise identifier, r ∈ 0,1 denotes the answer result, and t
|     |     |     | t   | t   |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
is the timestamp. The problem can be formalised as a hidden state estimation problem:
|     |     | (       | ) (            | )    |     |     |      |     |
| --- | --- | ------- | -------------- | ---- | --- | --- | ---- | --- |
|     |     | s = f s | ,x , p =g s ,e |      |     |     | (1)  |     |
|     |     | t t−1   | t t+1 t        | qt+1 |     |     |      |     |
where t=[e
|     |     | ;r;Δt | ] is the input feature vector (containing exercise embedding, answer  |     |     |     |     |     |
| --- | --- | ----- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | qt t  | t                                                                     |     |     |     |     |     |
results, and time interval), and f and g are the state transfer function and prediction
function, respectively.
The classical probabilistic model is represented by BKT (Guzman-Jimenez et al.,
2025), which assumes that the knowledge state is a binary hidden variable z ∈ 0, 1 (0 not
t
mastered, 1 mastered), and its state transfer follows a Markov process:
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

        Knowledge tracing in mathematical problem-solving processes  29

|     |     | (       | )        |        |      |     |
| --- | --- | ------- | -------- | ------ | ---- | --- |
|     |     | P z =1z | =0 = p   |        | (2)  |     |
|     |     | t       | t−1      | learn  |      |     |
|     |     | (       | )        |        |      |     |
|     |     | P z =0  | z =1 = p |        | (3)  |     |
|     |     | t       | t−1      | forget |      |     |
|     |     | (       | )        |        |      |     |
|     |     | P r =1z | =1 = p   |        | (4)  |     |
|     |     | t       | t slip   |        |      |     |
|     |     | (       | )        |        |      |     |
|     |     | P r =0  | z =0 = p |        | (5)  |     |
|     |     | t       | t guess  |        |      |     |
where,  parameter  p ,  p ,  p ,  p   is  estimated  by  expectation  maximisation
|     |     |     | learn forget | slip guess |     |     |
| --- | --- | --- | ------------ | ---------- | --- | --- |
algorithm. The limitation of BKT is the assumption of knowledge point independence
and ignoring the logical connection between concepts (Holmqvist et al., 2023).
Deep  learning  models  break  through  probabilistic  model  limitations  through
end-to-end  learning.  Recurrent  neural  networks  model  knowledge  states  as  hidden
vectors h:
t
|     |     | =tanh  | ( +W    | )   |      |     |
| --- | --- | ------ | ------- | --- | ---- | --- |
|     |     | h      | W h t−1 | x   | (6)  |     |
|     |     | t      | h x     | t   |      |     |
|     |     | (      | )       |     |      |     |
|     |     | =σ wh | +b      |     |      |     |
|     |     | p      |         |     | (7)  |     |
|     |     | t      | t       |     |      |     |
Long short-term memory networks introduce gating mechanisms to mitigate gradient
vanishing and enhance long sequence modelling. Self-attentive models (e.g., SAKT), on
the other hand, dynamically compute historical interaction correlations via a weight
matrix Q, K, V:
QK
Attention(Q,K,V)=softmax
V   (8)
dk
 
Such models, while enhancing temporal dependency capture, do not explicitly encode the
knowledge structure and the time interval Δt is only used as a scalar input.
t
|     | 3.2  | Fundamentals of spatio-temporal graphical neural networks  |     |     |     |     |
| --- | ---- | ---------------------------------------------------------- | --- | --- | --- | --- |
The STGNN aims to deal with the problem of joint modelling of spatial associations and
temporal evolution in graph-structured data (Jin et al., 2023). Its input is defined as a
spatio-temporal graph ST = (, spa,  ): where  = v ,…,v  is the set of nodes and
tem 1 N
spa ⊆  ×  is the spatial edges; 
tem  = A(1),…,A(T) is a sequence of temporal edges.
The  graph  convolutional  network  updates  the  node  representation  through
neighbourhood aggregation (Skarding et al., 2021). For node v, its l+1 layer embedding
i
h(l+1) is computed as:
i
|     |     |           |  1           |          |      |     |
| --- | --- | --------- | ------------- | --------- | ---- | --- |
|     |     | h(l+1) =σ |              | W(l)h (l) |      |     |
|     |     |           |              |          | (9)  |     |
|     |     | i         | ˆ ˆ           | j         |      |     |
|     |     |           |  j∈(i) d d |          |      |     |
|     |     |           | i             | j        |      |     |
where dˆ
=d +1 is the normalisation degree and (i) is the set of neighbouring nodes.
i i
Adaptive weights are further introduced for graph attention networks (Jamshidiha et al.,
2025):
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     | 30  X. Li  |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |

|     |     |        |  1     |            |     |     |       |     |     |
| --- | --- | ------ | ------- | ----------- | --- | --- | ----- | --- | --- |
|     |     | h(l+1) | =σ     | W(l)h (l) , |     |     |       |     |     |
|     |     | i      |        | j          |     |     |       |     |     |
|     |     |        |  d ˆ   | d ˆ        |     |     |       |     |     |
|     |     |        | j∈(i) |            |     |     | (10)  |     |     |
i j
|     |     |            | (         | (     | ))   |     |     |     |     |
| --- | --- | ---------- | --------- | ----- | ---- | --- | --- | --- | --- |
|     |     | α =softmax |           | aWh |      |     |     |     |     |
|     |     |            | LeakyReLU |       | Wh  |     |     |     |     |
|     |     | ij         | j         |      | i j |     |     |     |     |
where α is the attention coefficient of node j to i and a is the learnable vector.
ij
4  Spatio-temporal graph neural network knowledge tracking model
(STGNN-MKT)
The spatio-temporal graph neural network knowledge tracking model proposed in this
paper aims to address the dynamic evolution of knowledge states during mathematical
problem solving. The input of the model is a sequence of student history interactions
), where q denotes the exercise identifier, r ∈ 0,1 is
|     |     |  = (q , r , t | ), (q , r , t ),…,(q | , r , t |     |     |     |     |     |
| --- | --- | -------------- | -------------------- | ------- | --- | --- | --- | --- | --- |
|     |     | 1 1            | 1 2 2 2              | T T T   | t   |     | t   |     |     |
the binary answer result (1 for correct and 0 for incorrect), and t is a time stamp accurate
t
to seconds. The output is the predicted probability of correctness of the target exercise
∈[0,1] the model realises high-precision dynamic tracking of knowledge state
|     |     | q T+1 .  pˆ T+1 |     |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
through  three  core  phases:  heterogeneous  spatio-temporal  graph  construction,  dual
temporal  encoding  mechanism,  and  spatio-temporally  coupled  state  evolution.  The
modelling framework of the method is shown in Figure 2.
|     |     | 4.1  Heterogeneous spatio-temporal graph construction  |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
In order to explicitly characterise the multiple entities and their complex relationships
involved  in  the  mathematical  problem  solving  process,  this  model  constructs  a
dynamically evolving spatio-temporal heterogeneous graph.  = (t, t) the set of nodes
t contains three types of heterogeneous entities:
•
Student node  = s: represents a single student instance that is currently being
s
tracked, whose initial embedding h(0)∈d is generated by the attributes of the
s
school register (e.g., grade level, historical average correctness) mapped through the
full connectivity layer.
|     |     | •  Exercise node q = q |     | ,q ,…,q : the embedding of each exercise q, eq ∈ ℝd  |     |     |     |     |     |
| --- | --- | ----------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |                         | 1   | 2 N                                                  |     | i i |     |     |     |
incorporating the question text semantic vectors and structured attribute features, i.e.,
|     |     | =MLP(BERT(text              |     | )⊕δ ⊕t                              |                                            |     |     |     |     |
| --- | --- | --------------------------- | --- | ----------------------------------- | ------------------------------------------ | --- | --- | --- | --- |
|     |     | eq                          |     | ) where 9 denotes vector splicing.  |                                            |     |     |     |     |
|     |     | i                           |     | qi i i                              |                                            |     |     |     |     |
|     |     | •                           |     |                                     | : The embedding ek ∈ ℝd of each knowledge  |     |     |     |     |
|     |     | Knowledge point node k = k |     | 1 , k 2 ,…,k                        | M                                          | j   |     |     |     |
point k is initialised from the pre-constructed course knowledge graph and a  j
hierarchical encoder is introduced to capture the hierarchical relationships of the
knowledge domains (e.g., algebra, geometry) to which it belongs (Wan et al., 2025).

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Knowledge tracing in mathematical problem-solving processes 31
Figure 2 Model framework diagram (see online version for colours)
Heterogeneous Space-Time Map Construction Layer
Input Layer
Output Layer
Core Processing Layer
Spatio-temporal graph convolutional networks
Edge set t contains two semantic types:
• Static knowledge edge qk = (q, k, w ): Describes the attribution relationship
i j ij
between exercises and knowledge points, with weights w ∈ [0, 1] labelled by
ij
educational experts or automatically extracted based on exercise parsing (Ma et al.,
2024).
• Dynamic interaction edge t =(s,q, f ): Record the interaction behaviour of
sq i i
student s on exercise q at time t, and feature vector f = [r; Δt; τ; c] ∈ ℝ8 contains
i i i i i i i
the answer result r, the time interval Δt = t – t (seconds) with the previous
i i i i–1
interaction, the time spent on answering τ (seconds), and the context features c.
i i
• The graph structure is dynamically updated along with the solving sequences: when
a new interaction (q , r , t ) is added, an edge (s, q , f ) is added to t , and the set
T T T T T sq
of knowledge points associated with this exercise is activated (q ) = k | (q , k) ∈
T j T j
qk. This design breaks through the limitation of traditional homogeneous graphs
and explicitly distinguishes entity types and relational semantics (Li et al., 2021).
4.2 Heteromorphic attentional coding
To aggregate heterogeneous neighbourhood information and preserve relational
semantics, metapath-aware graph attention networks are designed (Chang et al., 2024).
For any node i ∈ t and its neighbour nodes j ∈ (i), the computation of the attention
factor α depends on node type ϕ(i) and edge type ϕ(i, j):
ij

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |   32  | X. Li  |     |     |     |     |     |     |     |     |
| --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     | (         | (              |          | ))  |       |     |     |
| --- | --- | --- | --- | --------- | -------------- | -------- | --- | ----- | --- | --- |
|     |     |     |     |           | a W h(l)     | h(l)    |     |       |     |     |
|     |     |     | exp | LeakyReLU |                | W        |     |       |     |     |
|     |     |     |     |           | φ(i,k) φ(i) i | φ(j) j  |     |       |     |     |
|     |     | α = |     | (         | (              |          | ))  | (11)  |     |     |
ij
|     |     |     |       | exp LeakyReLU | a W        | h(l) W | h(l) |     |     |     |
| --- | --- | --- | ------ | ------------- | ------------ | ------ | ----- | --- | --- | --- |
|     |     |     | k∈N(i) |               | φ(i,j) φ(i) | i φ(k) | k    |     |     |     |
where ϕ(⋅) is a type mapping function, ϕ(i) ∈ student, question, knowledge, W  ∈ ℝd′×d
ϕ(⋅)
 ∈ ℝ2d′ is a learnable relational
are type-specific linear transformation matrices, a
ϕ(i, j)
attention vector, and || denotes a vector splicing operation (Song et al., 2024). The
embedding of node i at layer l+1 is updated by residual join:
|     |     | h(l+1) | =σ  | αW h(l)+h(l)  |     |     |     |     |     |     |
| --- | --- | ------ | ---- | ------------- | --- | --- | --- | --- | --- | --- |
(12)
|     |     | i   |     | ij φ(j) | j i |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
j∈N(i)
 layer graph attention propagation, student node h(Lg) incorporates semantic
|     | Through L |     | g   |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s
information from its historical interaction exercises and its associated knowledge points,
h(Lg) enhances context-aware representation, and knowledge point node
exercise node
q
|     | h   | (Lg)  dynamically reflects its current activation strength (Lin et al., 2025).  |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
k
|     | 4.3  | Dual time encoding mechanism  |     |     |     |     |     |     |     |     |
| --- | ---- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
For dense practice sequences, gated temporal convolutional networks are used to capture
local solution patterns (Dong et al., 2021). Given the practice node embedding sequence
|     | [hq(Lg),hq |     | (Lg),…,h | (Lg) ]∈T×d′ |     |     |     |     |     |     |
| --- | ---------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
 for student s, the lth layer timing convolution operation
|     |     | 1   | 2   | qT  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is defined as:
|     |     |      |          | (            | )   |     |     |       |     |     |
| --- | --- | ---- | -------- | ------------ | --- | --- | --- | ----- | --- | --- |
|     |     | H(l) | =ReLU    | Φ(l)∗ H(l−1) |     |     |     |       |     |     |
|     |     |      |          |              |     |     |     | (13)  |     |     |
|     |     |      |          | 1 d          |     |     |     |       |     |     |
|     |     |      | (        |              | )   |     |     |       |     |     |
|     |     | G(l) | =σ Φ(l)∗ | H(l−1)       |     |     |     |       |     |     |
|     |     |      |          |              |     |     |     | (14)  |     |     |
2 d
|     |     | H(l) | =H(l)G(l)  |     |     |     |     | (15)  |     |     |
| --- | --- | ---- | ----------- | --- | --- | --- | --- | ----- | --- | --- |
out
2l–1,
where  * d   denotes  the  null  convolution  with  expansion  factor  d  =
|     | Φ(l),Φ | (l) ∈k×din×dout is the learnable convolution kernel, and  |     |     |     |     |     |     |     |     |
| --- | ------ | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
 is the element-by-
1 2
|     | element multiplication. By stacking L layers, the TCN outputs the exercise temporal  |     |     |     | t                                 |     |     |     |     |     |
| --- | ------------------------------------------------------------------------------------ | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
|     | feature matrix Hout(Lt)∈T×d′′                                                       |     |     |     | , whose tth row vector hqtcn∈d′′ |     |     |     |     |     |
 encodes the evolution
t
of the solution pattern up to time t, effectively modelling the coherence of thinking and
immediate feedback effect (Yao et al., 2018).
To quantify the systematic forgetting effect caused by time intervals, the forgetting-
memory gate module is proposed (Zhu et al., 2022). This module is fundamentally based
on the Ebbinghaus forgetting curve theory from cognitive science, which quantifies the
decline  of  memory  retention  over  time.  By  leveraging  this  principle,  the  module
strategically schedules review and practice sessions to counteract natural forgetting,
thereby actively promoting long-term knowledge consolidation and strengthening the
durability of learned material, and maintains dynamic memory strength  mt ∈[0,1] for
j
each knowledge point k:
j
|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

        Knowledge tracing in mathematical problem-solving processes  33

( )
|     |     | mt =γt ⋅mt−1+ | 1−γt ⋅ct   |     | (16)  |     |
| --- | --- | ------------- | ---------- | --- | ----- | --- |
|     |     | j j           | j j j      |     |       |     |
where  γt ∈[0,1] is the forgetting gating, which controls the retention of historical
j
memories, and  ct ∈[0,1] is the reinforcement gating, which encodes the enhancement
j
effect of the current exercise on memory. Both are calculated as follows:
|     |     |            | Δt            |        |       |     |
| --- | --- | ----------- | -------------- | ------ | ----- | --- |
|     |     | γt =exp    | −η⋅ j          |        |       |     |
|     |     |             |               |        | (17)  |     |
|     |     | j          | 1+βn          |        |       |     |
|     |     |            | j             |        |       |     |
|     |     |             | (              | )      |       |     |
|     |     | ct =sigmoid | wh(Lg) h(Lg) | +b    |       |     |
|     |     |             |                | r g    | (18)  |     |
|     |     | j           | c  kj qt      | t t c |       |     |
where Δt =t−tj  denotes the time interval since knowledge point k was last practiced,
|     |     | j   | last | j   |     |     |
| --- | --- | --- | ---- | --- | --- | --- |
n is the cumulative number of times k has been practiced, η > 0 and β > 0 are the
|     | j   |     |     | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
learnable decay coefficients, and g = [Δt; τ; onehot(env)] is the temporal signature of
t i i t
the current interaction.
Memory strength  mt fuses the time interval effect with the practice history in a
j
nonlinear decay function, and its output is spliced with the knowledge point embedding
as an augmented representation hk′ =[hk (Lg) mt]∈d′+1. The core intelligence of this
j j j
mechanism lies in its explicit distinction of the profound cognitive differences between
short-term repeated practice and long-term interruptions. It recognises that short-term,
massed practice primarily enhances retrieval strength and procedural fluency, creating a
sense of immediate mastery which is, however, often transient. In stark contrast, long-
term interruptions, while inducing a state of retrieval difficulty and apparent forgetting,
engage  the  powerful  effects  of  spaced  repetition  and  desirable  difficulties,  which
fundamentally  strengthen  storage  strength  and  promote  durable  consolidation.  By
computationally modelling these divergent cognitive pathways, the mechanism can make
nuanced pedagogical decisions – such as capitalising on massed practice for initial skill
acquisition while strategically employing spaced intervals to transform fragile knowledge
into  robust,  long-term  understanding  –  therely  orchestrating  a  highly  adaptive  and
effective learning journey.
|     | 4.4  | State evolution of spatio-temporal coupling  |     |     |     |     |
| --- | ---- | -------------------------------------------- | --- | --- | --- | --- |
The updating of student knowledge state is realised by an iterative message passing-state
updating loop (Sun et al., 2019) with the following steps:
1  Time step t input: add new interaction (q, r, t), add edge t  to dynamic edge set
t t t sq
t
.
sq
2  Spatial graph convolution: perform L  layer heterogeneous graph attention coding
g
and update all node embeddings ht,ht,ht.
s q k
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     | 34  X. Li  |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- |

3  Temporal evolution: exercise node sequence [hqt,…,hqt] inputs L layers of Gated
1 t t
TCN, generates short-time features htcn, associates knowledge point sets (q)
t
qt
computes memory strength mt |k ∈(q ) via FMGM, and updates its embedding
|     |     |     |     |     | j j | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
h k′ .
j
4  Student state updating: fusion of spatio-temporal features based on gated recurrent
unit:
|     |     | (          |           | )             |                                                |     |       |     |
| --- | --- | ---------- | --------- | ------------- | ---------------------------------------------- | --- | ----- | --- |
|     |     | z =σ W     | ht−1 u   | +b           |                                                |     | (19)  |     |
|     |     | t          | z s      | t z          |                                                |     |       |     |
|     |     | (          |           | )             |                                                |     |       |     |
|     |     | =σ         | ht−1     | +b           |                                                |     |       |     |
|     |     | r W        |  u t    |               |                                                |     | (20)  |     |
|     |     | t          | r s       | r             |                                                |     |       |     |
|     |     |            | (         |               | )                                              |     |       |     |
|     |     | t         | ht−1     |               |                                                |     |       |     |
|     |     | h =tanh    | W r      | u +b         |                                                |     | (21)  |     |
|     |     | s          | h t      | s t          | h                                              |     |       |     |
|     |     | =(         | ) ht−1+z | t            |                                                |     |       |     |
|     |     | ht 1−z     |           | h            |                                                |     | (22)  |     |
|     |     | s          | t s       | t s           |                                                |     |       |     |
|     |     |            | =k       | ∈(q )Wspahk′ | +Wtemhqtcn is the spatio-temporal aggregation  |     |       |     |
|     |     |   where ut |           |               |                                                |     |       |     |
|     |     |            | j         | t             | j                                              | t   |       |     |
feature and Wspa, Wtem is the projection matrix.
5  Prediction layer: based on the student’s current state hst and the target exercise q
t+1
(Lg)
embedding hq , the probability of answering the question correctly is computed
t+1
by feature interaction:
|     |     |        | ( (          | )    | )   |     |       |     |
| --- | --- | ------ | ------------ | ---- | --- | --- | ----- | --- |
|     |     | =σ     | WT ht h(Lg) | +b   |     |     |       |     |
|     |     | pˆ t+1 |              |      |     |     | (23)  |     |
|     |     |        | p s          | qt+1 | p   |     |       |     |
  where  denotes the element-by-element multiplication (Hadamard product). We
are enriching the dynamic, interactive representation of the student’s knowledge state
by integrating it with the specific features of each exercise. This process involves
contextualising the learner’s profile with real-time data on problem difficulty,
required knowledge components, and the problem-solving context, enabling a more
nuanced and responsive model for personalised learning.
|     |     | 4.5  Model training and optimisation  |     |     |     |     |     |     |
| --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
The  loss  function  is  defined  as  the  sum  of  the  binary  cross  entropy  and  the  L2
regularisation term:
T
|     |     | 1   |         | +(  | ) (      | ) +λ 2 |       |     |
| --- | --- | --- | -------- | --- | -------- | -------- | ----- | --- |
|     |     | L=− | r logpˆ | 1−r | log 1−pˆ | θ        | (24)  |     |
|     |     |     |  t      | t   | t        | t  2    |       |     |
T
|     |     |     | t=1 |     |     | θ∈Θ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where Θ is the set of all learnable parameters of the model and λ is the regularisation
coefficient. The Adam optimiser is used to minimise L. The initial learning rate is
established at 3.0 to provide substantial gradient updates early in the training process.
This  rate  is  then  systematically  fine-tuned  throughout  the  training  using  a  cosine
annealing  scheduler,  which  smoothly  reduces  the  learning  rate  according  to  a
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Knowledge tracing in mathematical problem-solving processes 35
cosine-shaped curve over each training cycle. The selected batch size of 32 effectively
balances computational efficiency with stable gradient estimation, promoting consistent
model convergence and robust learning performance. The early stopping strategy is based
on monitoring the AUC index of the validation set, and the training is terminated if the
model fails to improve in 10 consecutive epochs.
5 Experimental results and analysis
5.1 Experimental setup
The experiment uses two authoritative public datasets in education data mining:
ASSISTments2009 and KDDCup2010. The ASSISTments2009 dataset contains math
problem solving logs from US middle school students, covering 1,000 students, 101
knowledge points (e.g., linear equations, geometric proofs), and a time span of 9 months,
including daily practice and vacation interruption scenarios. The KDDCup2010 dataset,
on the other hand, contains 98,200 algebra problem solving logs covering 1,000 students
and 211 knowledge points, and its time-series characteristics show a significant pattern of
stage-intensive exams (intervals of <1 hour) and long vacation interruptions (intervals of
>30 days). In the data preprocessing stage, we filtered the knowledge points that were
practiced less than 10 times to eliminate noise, merged the records of consecutive
answers with intervals of less than 5 minutes in the same exam, and converted all the
timestamps into seconds to ensure the accuracy of the time series modelling.
The evaluation indexes are selected to take into account the sorting ability,
classification accuracy and probability calibration: AUC (area under the curve): measures
the model’s ability to sort students’ probability of answering questions correctly, with a
value range of [0,1], the higher the value indicates that the model is more capable of
distinguishing between positive and negative samples, the higher the value indicates the
model’s ability to differentiate between positive and negative samples, the higher the
value indicates the model’s ability to differentiate between positive and negative samples,
and the higher the value indicates that the model can distinguish between positive and
negative samples, the lower the value indicates the model can distinguish between
positive and negative samples. Calibration.
In order to comprehensively verify the model validity, six types of frontier baseline
models are selected for comparison: traditional probabilistic models: BKT (Mao, 2018),
deep timing model (DKT) (Liu et al., 2020). Graph structure model: GKT (Yang et al.,
2024) and dynamically constructed student-problem interaction graph (DGKT) (Li et al.,
2018). Temporal fusion model: introducing linear forgetting gate (DGMN) in GKT
(Abdelrahman and Wang, 2022) with multi-relational GRU fusion time decay (MRTKT)
(Cui et al., 2023).
5.2 Comparative analysis of overall performance
Tables 1 and 2 show the performance comparison results on the ASSISTments2009 and
KDDCup2010 datasets, respectively. In the ASSISTments2009 datase, STGNN-MKT
fully leads the baseline model with AUC = 0.901, ACC=0.845, and RMSE = 0.218.
Compared to the optimal baseline DGKT (AUC = 0.832), the AUC of STGNN-MKT is
improved by 8.3% and the RMSE is reduced by 17.1%, indicating a better calibration of

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |   36  | X. Li  |     |     |     |     |     |     |
| --- | ----- | ------ | --- | --- | --- | --- | --- | --- |

its prediction probability. On the KDDCup2010 datase, which has a larger time span and
more frequent interruptions, STGNN-MKT’s lead is further extended: the AUC reaches
0.893,  a  7.9%  improvement  over  the  spatio-temporal  fusion  baseline  MRTKT
(AUC = 0.827), and the training time is only increased by 0.8 hours, which verifies the
efficient scalability of the model.
|     | Table 1  | ASSISTments2009 dataset performance comparison  |     |     |     |     |     |     |
| --- | -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
Number of participants
|     | Method  |     | AUC  | ACC  | RMSE  |     |     |     |
| --- | ------- | --- | ---- | ---- | ----- | --- | --- | --- |
(in thousands)
|     | BKT        |                                            | 0.712  | 0.698  | 0.312  | 0.5                    |     |     |
| --- | ---------- | ------------------------------------------ | ------ | ------ | ------ | ---------------------- | --- | --- |
|     | DKT        |                                            | 0.781  | 0.723  | 0.289  | 12.3                   |     |     |
|     | GKT        |                                            | 0.816  | 0.754  | 0.271  | 25.6                   |     |     |
|     | DGKT       |                                            | 0.832  | 0.769  | 0.263  | 31.2                   |     |     |
|     | DGMN       |                                            | 0.849  | 0.793  | 0.251  | 28.7                   |     |     |
|     | STGNN-MKT  |                                            | 0.901  | 0.845  | 0.218  | 34.5                   |     |     |
|     | Table 2    | KDDCup2010 dataset performance comparison  |        |        |        |                        |     |     |
|     | Method     |                                            | AUC    | ACC    | RMSE   | Training time (hours)  |     |     |
|     | SAKT       |                                            | 0.768  | 0.718  | 0.301  | 1.8                    |     |     |
|     | MRTKT      |                                            | 0.827  | 0.781  | 0.256  | 2.5                    |     |     |
|     | DGKT       |                                            | 0.841  | 0.792  | 0.247  | 3.1                    |     |     |
|     | DGMN       |                                            | 0.831  | 0.785  | 0.253  | 2.7                    |     |     |
|     | STGNN-MKT  |                                            | 0.893  | 0.839  | 0.224  | 3.9                    |     |     |
The AUC of STGNN-MKT reaches 0.872 in the long-term interval (>30 days) answer
samples, which is significantly higher than that of DGMN (0.801) and DGKT (0.819).
This  is  attributed  to  the  FMGM  module’s  accurate  modelling  of  the  Ebbinghaus
forgetting curve – integrating the time interval Δt with the number of practice sessions n  j
γt =exp(−ηΔt/(1+βn
through a nonlinear decay function  )), e.g., the forgetting gate
|     |     |     |     | j   | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
for a certain knowledge point is γt =0.65 at an interval of 60 days but with a number of
j
practice sessions n = 5, while it is γt =0.24 at n = 1 at the same interval, which is more
|     |     |     | j   | j   | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
in line with the laws of cognitive psychology.
|     | 5.3  | Fine-grained validation of time interval effects  |     |     |     |     |     |     |
| --- | ---- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
In order to verify the ability of gated TCNs to capture dense solving patterns and simulate
the exam, Figure 3 shows the trend of prediction accuracy for 10 consecutive questions in
the  ASSISTments  dataset. STGNN-MKT  predicts  the ACC  to be  0.82  in  the  first
question, and then gradually rises to 0.88 with the advancement of solving and stabilises
in the interval of 0.86 ± 0.02, which indicates that TCNs can effectively capture the
thinking and coherence and positive feedback effect of solving the problem chain through
the null convolution. coherence and positive feedback effect. Due to the lack of local
pattern modelling ability, the ACC of the comparison models DKT and SAKT dropped to
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

        Knowledge tracing in mathematical problem-solving processes  37

below 0.75 after the 5th question, and fluctuated significantly especially when the
questions involved cross-knowledge transfer.
Figure 3  Change curves of ACC for each model in short time intensive question answering
scenarios (see online version for colours)

Figure 4  Comparison of predicted AUC for the first question across models after a long interval
(see online version for colours)

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |   38  | X. Li  |     |     |     |     |
| --- | ----- | ------ | --- | --- | --- | --- |

Screening the answering records before and after the vacation in the KDDCup dataset,
Figure 4 compares the prediction AUC of each model for the first question after a long
interval. STGNN-MKT leads the way with an AUC=0.872, an improvement of 8.9%
compared to DGMN). Further analysis of the FMGM module behaviour: when the time
interval was Δt = 45 day and the number of practice sessions was n = 3, the memory
j
strength mt decayed to 0.61; whereas at the same interval if n = 7, mt it only dropped to
|     |     | j   | j j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0.78. This mechanism allowed the model to accurately reflect the inhibitory effect of the
frequency of historical practice on the rate of forgetting in predicting the performance of
the first question after a prolonged interruption.
|     | 5.4  | Ablation experiments and model robustness analysis  |     |     |     |     |
| --- | ---- | --------------------------------------------------- | --- | --- | --- | --- |
In Table 3 systematic assessment of the contributions of the STGNN-MKT modules. The
removal of the heterogram attention module (w/o heterogram attention) resulted in a
4.6% decrease in AUC, confirming that the student-exercise-knowledge point ternary
relationship is the core foundation of representational learning. The elimination of TCN
short-time encoding (w/o TCN) and FMGM long-time encoding (w/o FMGM) resulted in
a 2.5% and 3.4% AUC loss, respectively, demonstrating the complementary effects of the
dual  temporal  mechanisms  on  dense  and  sparse  scenarios.  The  ablation  of  the
spatio-temporal co-updating mechanism (w/o spatio-temporal co-updating) triggers the
maximum performance degradation (5.8% AUC drop), demonstrating that the coupling
of spatial structural evolution and temporal cumulative evolution is the key to the
dynamic tracking of cognitive states.
|     | Table 3                                | Comparison of ablation experiment results  |        |        |     |     |
| --- | -------------------------------------- | ------------------------------------------ | ------ | ------ | --- | --- |
|     | Model variant                          |                                            | AUC    | ΔAUC   |     |     |
|     | Full model                             |                                            | 0.893  | -      |     |     |
|     | W/o heterogram attention               |                                            | 0.852  | –4.6%  |     |     |
|     | W/o TCN                                |                                            | 0.871  | –2.5%  |     |     |
|     | W/o FMGM                               |                                            | 0.863  | –3.4%  |     |     |
|     | W/o space-time collaborative updating  |                                            | 0.841  | –5.8%  |     |     |
Figure 5  Effect of hidden layer dimension d and forgetting coefficient η on AUC (see online
version for colours)

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Knowledge tracing in mathematical problem-solving processes 39
Figure 5 explores the effect of hidden layer dimension d and forgetting factor η on model
performance. The AUC peaks at 0.893 when d = 64; the characterisation ability is
insufficient for d < 64, and the risk of overfitting rises for d > 64. Forgetting coefficient η
performs robustly in the [0.1, 0.2] interval (AUC>0.885); forgetting gate suppression is
insufficient at η < 0.1, and historical memories are excessively discarded at η > 0.2.
6 Conclusions
In this paper, we propose a spatio-temporal graph neural network knowledge tracking
method for mathematical problem solving process, which unifies the spatial correlation
and temporal evolution dynamics of the modelled knowledge structure by constructing a
student-exercise-knowledge point ternary heterogeneous graph. In the spatial dimension,
a meta-path-aware graph attention mechanism is designed to explicitly capture
inter-conceptual logical dependencies; in the temporal dimension, a gated temporal
sequential convolutional network and a forgetting-memory gate module are innovatively
integrated to portray the short-term thinking coherence of intensive problem solving and
the cognitive forgetting law of the long term intervals, respectively. Experiments show
that the method significantly outperforms the baseline model on the ASSISTments and
KDDCup datasets. This work provides a new paradigm for educational cognitive
modelling that balances predictive accuracy and educational interpretability, and will be
extended to cross-disciplinary knowledge transfer and privacy-preserving deployment
scenarios in the future.
Acknowledgements
This work is supported by the Innovation in OBE-Based Blended Teaching of Advanced
Mathematics, University-level (No. 2025CYYBJY007).
Declarations
Author declares no conflicts of interest.
References
Abdelrahman, G. and Wang, Q. (2022) ‘Deep graph memory networks for forgetting-robust
knowledge tracing’, IEEE Transactions on Knowledge and Data Engineering, Vol. 35, No. 8,
pp.7844–7855.
Broncano-Berrocal, F. (2018) ‘Knowledge and tracking revisited’, Analysis, Vol. 78, No. 3,
pp.396–405.
Chang, Z., Zhu, R., Liu, J., Shang, J. and Dai, L. (2024) ‘HGSMDA: miRNA – disease association
prediction based on HyperGCN and Sørensen-Dice Loss’, Non-coding RNA, Vol. 10, No. 1,
p.9.
Chen, M., Bian, K., He, Y., Li, Z. and Zheng, H. (2023) ‘Enhanced learning and forgetting
behavior for contextual knowledge tracing’, Information, Vol. 14, No. 3, p.168.

40 X. Li
Cui, C., Yao, Y., Zhang, C., Ma, H., Ma, Y., Ren, Z., Zhang, C. and Ko, J. (2024) ‘DGEKT: A dual
graph ensemble learning method for knowledge tracing’, ACM Transactions on Information
Systems, Vol. 42, No. 3, pp.1–24.
Cui, J., Chen, Z., Zhou, A., Wang, J. and Zhang, W. (2023) ‘Fine-grained interaction modeling
with multi-relational transformer for knowledge tracing’, ACM Transactions on Information
Systems, Vol. 41, No. 4, pp.1–26.
Dong, J., Li, X., Xu, C., Yang, X., Yang, G., Wang, X. and Wang, M. (2021) ‘Dual encoding for
video retrieval by text’, IEEE Transactions on Pattern Analysis and Machine Intelligence,
Vol. 44, No. 8, pp.4065–4080.
Giroux, H. and Taylor, J.R. (2002) ‘The justification of knowledge: tracking the translations of
quality’, Management Learning, Vol. 33, No. 4, pp.497–517.
Guzman-Jimenez, R., Prem, D., Saldívar, A. and Escotto-Córdova, E.A. (2025) ‘Yupana Inka Tawa
Pukllay arithmetic eye tracking analysis: novices’, Frontline Learning Research, Vol. 13,
No. 3, pp.29–52.
Heng-yu, L., Tian-cheng, Z., Pei-wen, W. and Ge, Y. (2019) ‘A review of knowledge tracking’,
Journal of East China Normal University (Natural Science), Vol. 2019, No. 5, p.1.
Holmqvist, K., Örbom, S.L., Hooge, I.T., Niehorster, D.C., Alexander, R.G., Andersson, R.,
Benjamins, J.S., Blignaut, P., Brouwer, A.-M. and Chuang, L.L. (2023) ‘RETRACTED
ARTICLE: Eye tracking: empirical foundations for a minimal reporting guideline’, Behavior
Research Methods, Vol. 55, No. 1, pp.364–416.
Jamshidiha, S., Pourahmadi, V., Mohammadi, A. and Bennis, M. (2025) ‘Power allocation using
spatio-temporal graph neural networks and reinforcement learning’, Wireless Networks,
Vol. 31, No. 2, pp.1163–1176.
Jin, G., Liang, Y., Fang, Y., Shao, Z., Huang, J., Zhang, J. and Zheng, Y. (2023) ‘Spatio-temporal
graph neural networks for predictive learning in urban computing: a survey’, IEEE
Transactions on Knowledge and Data Engineering, Vol. 36, No. 10, pp.5388–5408.
Kim, M., Shim, Y., Lee, S., Loh, H. and Park, J. (2021) ‘Behavioral Testing of Deep Neural
Network Knowledge Tracing Models’, International Educational Data Mining Society, Vol. 1,
No. 10, pp.1–13.
Li, C., Lin, L., Zuo, W., Tang, J. and Yang, M.-H. (2018) ‘Visual tracking via dynamic graph
learning’, IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 41, No. 11,
pp.2770–2782.
Li, M., Chen, S., Zhao, Y., Zhang, Y., Wang, Y. and Tian, Q. (2021) ‘Multiscale spatio-temporal
graph neural networks for 3d skeleton-based motion prediction’, IEEE Transactions on Image
Processing, Vol. 30, No. 1, pp.7760–7775.
Lin, Y., Wang, N., Liu, J., Zhang, F., Wei, Z. and Yi, M. (2025) ‘CHNSCDA: circRNA-disease
association prediction based on strongly correlated heterogeneous neighbor sampling’,
International Journal of Machine Learning and Cybernetics, Vol. 16, No. 3, pp.2023–2039.
Liu, D., Zhang, Y., Zhang, J., Li, Q., Zhang, C. and Yin, Y. (2020) ‘Multiple features fusion
attention mechanism enhanced deep knowledge tracing for student performance prediction’,
IEEE Access, Vol. 8, No. 1, pp.194894–194903.
Liu, Y., Ji, W. and Zhou, G. (2025) ‘Spatiotemporal fusion knowledge tracking model based on
spatiotemporal graph and fourier graph neural network’, Journal of King Saud University
Computer and Information Sciences, Vol. 37, No. 6, p.124.
Ma, W., Chu, Z., Chen, H. and Li, M. (2024) ‘Spatio-temporal envolutional graph neural network
for traffic flow prediction in UAV-based urban traffic monitoring system’, Scientific Reports,
Vol. 14, No. 1, p.26800.
Manierre, M.J. (2015) ‘Gaps in knowledge: tracking and explaining gender differences in health
information seeking’, Social Science & Medicine, Vol. 128, No. 1, pp.151–158.
Mao, Y. (2018) ‘Deep Learning vs. Bayesian knowledge tracing: student models for interventions’,
Journal of Educational Data Mining, Vol. 10, No. 2, pp.1–11.

Knowledge tracing in mathematical problem-solving processes 41
Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M. and Chen, E. (2024) ‘A survey of
knowledge tracing: Models, variants, and applications’, IEEE Transactions on Learning
Technologies, Vol. 17, No. 1, pp.1858–1879.
Skarding, J., Gabrys, B. and Musial, K. (2021) ‘Foundations and modeling of dynamic networks
using dynamic graph neural networks: A survey’, IEEE Access, Vol. 9, No. 1,
pp.79143–79168.
Song, X., Ling, G., Tu, W. and Chen, Y. (2024) ‘Knowledge-guided heterogeneous graph
convolutional network for aspect-based sentiment analysis’, Electronics, Vol. 13, No. 3,
p.517.
Sun, Y., Liu, S., Dong, Y., An, Y., Shi, F., Dong, S. and Liu, G. (2019) ‘Spatio-temporal evolution
scenarios and the coupling analysis of ecosystem services with land use change in China’,
Science of the Total Environment, Vol. 681, No. 1, pp.211–225.
Wan, H., Xiang, L., Cai, Y., Xie, Y. and Xu, R. (2025) ‘Temporal and spatial feature extraction
using graph neural networks for multi-point water quality prediction in river network areas’,
Water Research, Vol. 281, No. 1, p.123561.
Wang, X., Zheng, Z., Zhu, J. and Yu, W. (2023) ‘What is wrong with deep knowledge tracing?
Attention-based knowledge tracing’, Applied Intelligence, Vol. 53, No. 3, pp.2850–2861.
Wu, Z., Huang, L., Huang, Q., Huang, C. and Tang, Y. (2022) ‘SGKT: Session graph-based
knowledge tracing for student performance prediction’, Expert Systems with Applications,
Vol. 206, No. 1, p.117681.
Yang, Z., Hu, J., Zhong, S., Yang, L. and Min, G. (2024) ‘Graph-based effective knowledge tracing
via subject knowledge mapping’, Education and Information Technologies, Vol. 2, No. 1,
pp.1–28.
Yao, K., Zhang, L., Du, D., Luo, T., Tao, L. and Wu, Y. (2018) ‘Dual encoding for abstractive text
summarization’, IEEE Transactions on Cybernetics, Vol. 50, No. 3, pp.985–996.
Zhang, K. and Yao, Y. (2018) ‘A three learning states Bayesian knowledge tracing model’,
Knowledge-Based Systems, Vol. 148, No. 1, pp.189–201.
Zhu, K., Li, Y., Mao, W., Li, F. and Yan, J. (2022) ‘LSTM enhanced by dual-attention-based
encoder-decoder for daily peak load forecasting’, Electric Power Systems Research, Vol. 208,
No. 1, p.107860.