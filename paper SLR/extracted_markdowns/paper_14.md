14384
Proceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages14384–14396
December6-10,2023©2023AssociationforComputationalLinguistics

mitigatetheseissues,anaturalsolutionisdistilling ally by exercises, thereby facilitating the genera-
theknowledgefromLLMs(i.e. teachermodels) tion of tailored educational experiences. Person-
into smaller, more efficient models (i.e. student alizedlearningisalsoofvitalimportance(Hattie
models). The majority of prior research has em- andTimperley,2007;GrantandBasye,2014). Be-
phasizedusingthe"explanation"componentofthe ingcognizantofthestudentmodel’slearningsta-
CoTapproachasthedistilledknowledge(Hoetal., tus ensures the optimally designed exercises are
2022;Lietal.,2022a;Shridharetal.,2022b;Magis- generated to address the model’s specific weak-
teretal.,2022). Nonetheless,thesemethodologies nesses. By monitoring the learning progress, our
exhibit certain limitations. Firstly, small student proposedmethodcandynamicallyadapttothestu-
modelsmaystruggletounderstandCoTexplana- dentmodel’sevolvingknowledgestate,fostering
tions,potentiallyimpedingtheirlearningefficacy. moreeffectivelearningoutcomes. Inourmethod,
Evidencefrom(Weietal.,2022b,a)indicatesthat weintegrateknowledgetracingandlearningstatus
onlyexceptionallylargelanguagemodelspossess into the distillation process to establish a robust
the capability to perform CoT during reasoning. connectionbetweentheLLMteacherandthestu-
Asaresult,manystudentmodels(Hoetal.,2022; dent model, yielding a more interactive and cus-
Li et al., 2022a; Magister et al., 2022) trained on tomizedlearningexperience. Consequently,thisap-
explanationsdonotattainsatisfactoryaccuracyin proachsubstantiallyenhancesthestudentmodel’s
MWP-solving tasks. Secondly, those distillation problem-solvingcapabilities. AsillustratedinFig-
processeslackfeedbackfromthestudentmodelto ure1,ourknowledgedistillationapproachachieves
theLLMteacher,andthus,neglecttoconsiderthe competitiveaccuracyontheSVAMPdataset,but
knowledgeacquisitionstateofthestudent. employssignificantlyfewerparameterscompared
tostate-of-the-artLLMs,suchasGPT-3+CoTand
In this paper, we also concentrate on harness-
PaLM+CoT with few-shot prompting (Wei et al.,
ingthestrengthsofLLMstocoachsmaller,more
2022b).
efficient MWP solvers, but introduce a novel
Ourcontributioncanbesummarizedasfollows:
method for addressing the limitations of previ-
ous approaches: Customized Exercise for MAth
• WeproposeanovelmethodnamedCEMAL
Learning(CEMAL).Wereframetheproblemby
thatutilizesLLMstogenerateadditionaldata
shiftingourfocusfromprovidingexplanationsfor
intheformoftargetedpracticeproblems,ad-
existingexercises(i.e.,trainingset)toidentifying
dressingthestudentmodel’sweakareas.
the student model’s learning needs and generat-
ing new exercises tailored to them. Our CEMAL • OurapproachisevaluatedonmultipleMWP
methodology offers a new perspective on knowl- datasets, including both in-distribution (ID)
edge distillation with LLMs by focusing on cus- andout-of-distribution(OOD)tests(Koncel-
tomizedexercisegeneration,basedonthestudent Kedziorskietal.,2016;Miaoetal.,2020;Pa-
models’currentlearningstate. Thisenablesmore tel et al., 2021). We show that our method
effectiveandadaptivelearning,addressinglimita- issignificantlyeffectiveinimprovingstudent
tionsinpriorapproachesthatrelyheavilyongen- modelsundertheOODsetting.
eratingmorehigh-qualityexplanationstoexisting
• Theexperimentalresultsdemonstratethatour
datasets. Thisapproachoffersseveraladvantages:
methodachievesstate-of-the-artaccuracy,sig-
(1)itdoesnotimposeCoTabilityrequirementson
nificantlyoutperformingfine-tunedbaselines.
smallmodels, allowingthemtolearnmoreeffec-
Notably, the student model trained with our
tively,(2)ittakesintoaccountthelearningstatus
methodevensurpassesLLMswithfew-shot
ofthestudentmodelduringtraining.
CoTprompting,despitehavingsignificantly
Infact,ourapproachCEMALseamlesslyaligns
fewerparameters.
with two fundamental tasks in educational sci-
ence: knowledge tracing and personalized learn- 2 RelatedWork
ing. Knowledgetracingpertainstomonitoringand
2.1 MathWordProblemSolving
modelingastudent’sevolvingknowledgestateover
time(CorbettandAnderson,1994;Abdelrahman After many years of research on rule-based algo-
et al., 2023). This process enables the identifica- rithms (Hosseini et al., 2014; Mitra and Baral,
tionofalearner’sstrengthsandweaknesses,usu- 2016) and semantic parsing methods (Shi et al.,
14385

2015; Huang et al., 2017), deep learning has AugESC(Zhengetal.,2022)leveragestheGPT-J
become the predominant technique for solving (WangandKomatsuzaki,2021)modelandutilizes
MWPs, thanks to its superior performance and publiclyavailabledialogpoststotriggerconversa-
better generalization ability. Deep neural solver tionsonvarioustopics. Then,Westetal.(2022)em-
(DNS)(Wangetal.,2017)wasamongthefirstto ploysageneralizedLLMtocreatecommonsense
applySeq2SeqmodelswithRNNencoderandde- knowledgegraphs,whileWANLI(Liuetal.,2022)
coderforMWPsolving,andsubsequentresearch combines LLM-generated examples with human
hasmainlyexploreddifferentstructuresofRNN- evaluationtoestablishdiversenaturallanguagein-
to-RNN solvers (Wang et al., 2018; Liu et al., ferencedatasets. Additionally,ZeroGen(Yeetal.,
2019a;XieandSun,2019;Lietal.,2019;Zhang 2022b)proposesazero-shotlearningapproachby
etal.,2020;Liuetal.,2021). Morerecently,pre- generating datasets using pre-trained LLMs, Pro-
trained language models such as BERT (Devlin Gen(Yeetal.,2022a)usesthequalityofgenerated
etal.,2019)andRoBERTa(Liuetal.,2019b)have samplesasfeedbacktoLLMstoimprovethedata
demonstratedremarkablelanguageunderstanding generation,andShaoetal.(2023)feedschain-of-
abilities,leadingresearcherstoreplaceMWPen- thoughtdemonstrationstoLLMsandtargetsgener-
coderswiththesemodels(Lietal.,2022b;Huang atingmoreexemplarsforin-contextlearning.
et al., 2021; Shen et al., 2021; Patel et al., 2021; In the domain of MWP solving, several stud-
Liangetal.,2022a), resultinginsignificantaccu- ies have also been conducted with the objective
racyimprovements. Recently,LLMshaveshown ofdistillingthereasoningcapabilityofLLMsinto
greatsuccessinMWPsolving,withmuchsuperior smallersolversbyemployingchain-of-thoughtex-
accuracycomparedtofine-tunedbaselines,simply planations. (Hoetal.,2022)introducesFine-tune-
by being provided with a few CoT examples of CoT,whichusesLLMstogeneratereasoningstep
the problem-solving processes. Interestingly, re- instances,subsequentlyfacilitatingthefine-tuning
searchers also found that LLMs can reason with ofsmallermodels. (Lietal.,2022a)exploresthree
zero-shotpromptssuchas"Let’sthinkstepbystep" explanationgenerationstrategiesandincorporates
(Kojimaetal.,2022). Currently,numerousstudies themintoamulti-tasklearningframeworktailored
havebeenconductedtoimprovetheperformance for compact models. (Magister et al., 2022) as-
ofLLMs,includingrecentworksby(Wangetal., sessestheefficacyofchain-of-thoughtexplanations
2023; Chen et al., 2022; Zhou et al., 2023; Diao in the training of a small model across three dis-
etal.,2023;Liangetal.,2023). parate tasks, namely arithmetic reasoning, com-
In this paper, we leverage the great success of monsensereasoning,andsymbolicreasoning. Fur-
LLMstofacilitatethetrainingofthestudentsolver. thermore,(Shridharetal.,2022b)presentsDecom-
Ourapproachutilizesanefficientfine-tunedsolver positionalDistillation,anapproachthatsegments
as its backbone and yields even superior perfor- theproblemintosubproblemstoenhancesmaller
mancetoLLMs,furtherpushingthelimitofdeep models’performance.
learningmethodsinMWPsolving. Incontrasttotheseexistingworks,ourproposed
knowledgedistillationapproachinMWPsolving
isuniqueinthatitdoesnotfocusonthechain-of-
2.2 LargeLanguageModelsforKnowledge
thought explanation and it takes into account the
DistillationandDataGeneration
learningstatusofthestudentmodelandgenerates
Inrecentyears,therehasbeenasurgeofinterestin exercisesthattailortothespecificweaknessesof
knowledgedistillationfromLLMstosmallermod- thestudent. Ourapproachbridgesthegapbetween
els. Duetotheunavailabilityofmodelstructurefor knowledge distillation and data augmentation in
LLMs,theirapplicationisoftenlimitedtoprompt thecontextofmathwordproblemsolvers,allowing
design and subsequent data generation. There- studentmodelstoimprovetheirproblem-solving
fore, datagenerationhasbecomeanintegralpart capabilitiesmoreeffectively.
ofknowledgedistillationinthecontextofLLMs.
Several studies have investigated the potential of 3 Approach
LLMs in knowledge distillation and data genera-
3.1 ProblemDefinition
tion. For instance, PromDA (Wang et al., 2022)
applies prompt-based data augmentation to low- OurobjectiveistotrainastudentMathWordProb-
resourcenaturallanguageunderstandingtasks,and lem(MWP)solverwiththeassistanceoflargelan-
14386

14387

RoBERTa-base, and RoBERTa-large (Liu et al., TheexerciseproblemsgeneratedbyLLMsmay
2019b)todemonstratethebackbone-agnosticna- beoflowquality,inawrongformat,orrepetitive
tureofourapproach. (acasestudyincludingcorrectandincorrectexam-
|     |     |     |     |     |     | ples is presented |     | in Section |     | 4.7). To | alleviate | the |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | --- | -------- | --------- | --- |
3.4 ExerciseGeneration impactoftheselow-qualityexerciseproblems,we
|     |     |     |     |     |     | filter out | about | 30% of | problems | with | the | wrong |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ | -------- | ---- | --- | ----- |
Ourmethodgeneratestargetedexercisesandtheir
formatsduringthegenerationprocessbychecking
answersbasedonagivensourceproblem-answer
whetherthegeneratedproblemisrepetitiveandthe
pair(W andA),whichissimilartodataaugmen-
generatedanswerisavalidmathematicalequation.
| tation. Following |     | a previous | paper | on  | analogical |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
reasoning(Liangetal.,2022b),thegenerationof 3.5 Targetedvs. RandomGeneration
exercisetargetstoreachtwokindsofanalogiesto
|     |     |     |     |     |     | The generation |     | of targeted |     | exercises | to  | address |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | --------- | --- | ------- |
W andA-problemanalogyandsolutionanalogy-
MWPsthatthestudentmodelhaspreviouslyfailed
thathelpmodelsbetterunderstandMWPs.
tosolvesignificantlyimprovesthemodel’scapacity
Forproblemanalogy,wegenerateproblemswith
|     |     |     |     |     |     | toprocessproblemandansweranalogies. |     |     |     |     |     | Toeval- |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------- |
similarproblemdescriptionsbutdifferentsolutions.
|            |          |     |          |           |          | uate the | efficacy | of this | approach, |     | it is insightful |     |
| ---------- | -------- | --- | -------- | --------- | -------- | -------- | -------- | ------- | --------- | --- | ---------------- | --- |
| Our method | perturbs |     | not only | questions | but also |          |          |         |           |     |                  |     |
toconsiderabaselinegenerationstrategy,namely
considersthecontext,andwepromptLLMswith
|                                        |     |     |     |     |     | random   | generation   | (referenced |               | in  | lines 17-18 | of  |
| -------------------------------------- | --- | --- | --- | --- | --- | -------- | ------------ | ----------- | ------------- | --- | ----------- | --- |
| few-shotexamplestogenerateMWPvariants. |     |     |     |     | In  |          |              |             |               |     |             |     |
|                                        |     |     |     |     |     | Alg. 1). | We introduce |             | a probability |     | threshold   | λ   |
contrasttopreviousstudiesthatusedhumananno-
|                                 |     |            |      |         |             | to control      | the | employment | of       | generation | strategy |     |
| ------------------------------- | --- | ---------- | ---- | ------- | ----------- | --------------- | --- | ---------- | -------- | ---------- | -------- | --- |
| tators (Patel                   | et  | al., 2021; | Yang | et al., | 2022), our  |                 |     |            |          |            |          |     |
|                                 |     |            |      |         |             | when augmenting |     | the        | training | set (lines | 13-18    | in  |
| approachisautomatedandscalable. |     |            |      |         | Forsolution |                 |     |            |          |            |          |     |
Alg. 1). λ=0favorsrandomgeneration,whereasλ
analogy,wegenerateproblemswithdifferentkey-
=1mandatestheutilizationoftargetedgeneration.
wordsintheproblemdescriptionbutasimilarsolu-
Adetailedanalysisontheimpactofλcanbefound
tiontothesourceMWP.Interestingly,wefindthat
inSection4.4.
| LLMs can | achieve | this | generation | in  | a zero-shot |     |     |     |     |     |     |     |
| -------- | ------- | ---- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
mannerbysimplypromptingthemtogenerateprob-
4 Experiments
| lems similar | to  | the source | problem. |     | Our prompt |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
4.1 Datasets
designislocatedintheappendix.
Thisexercisegenerationisdeployedattwodif- MAWPS The MAWPS dataset (Koncel-
ferent steps in our proposed training framework. Kedziorski et al., 2016) is an aggregation of
First,wegenerateanexercisebookbyaugmenting 2,373 English Math Word Problems (MWPs)
theentiretrainingset(lines4-6inAlg. 1),which from various sources, including AddSub (Hos-
|     |     |     |     |     |     | seini et | al., 2014), | SingleOp |     | (Roy | et al., | 2015), |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | --- | ---- | ------- | ------ |
servesasavalidationsettoidentifytheweaknesses
of the student solver. We do not directly use the MultiArith (Roy and Roth, 2015), SingleEq
trainingsettovalidatethestudentsolverbecause (Koncel-Kedziorski et al., 2015), and SimulEq
we want a more diverse validation set to compre- (Kushman et al., 2014). We employ a 5-fold
hensivelyevaluatethestudentmodel. Additionally, cross-validationfortheevaluationonthisdataset.
thesolvermaymemorizetheMWPsinthetraining
|     |     |     |     |     |     | ASDiv-a | ASDiv(Miaoetal.,2020)isanEnglish |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------------- | --- | --- | --- | --- | --- |
setinsteadoffullyunderstandingthem,asprevious
|     |     |     |     |     |     | MWP dataset |     | designed | to exhibit | a   | more | diverse |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ---------- | --- | ---- | ------- |
researchhasfoundthatslightlyperturbedtraining
rangeoflanguagepatternsandproblemtypes,com-
MWPscancauseasolvertofail(LiangandZhang,
|     |     |     |     |     |     | prising 2,305 |     | MWPs. | In accordance |     | with | prior |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------------- | --- | ---- | ----- |
2021). Therefore,validationontheexercisebook,
studies(Pateletal.,2021;Lanetal.,2022),wese-
| which contains |     | many | variants | of the | training set, |     |     |     |     |     |     |     |
| -------------- | --- | ---- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
lectthearithmeticsubset,ASDiv-a,whichcontains
providesamorerobustevaluation.
1,218MWPsandutilizesa5-foldcross-validation
Secondly,afteridentifyingtheproblemsthatthe
methodforevaluation.
studentsolvercannotsolvefromtheexercisebook,
weusethemasthesourcetogeneratecustomized SVAMP The SVAMP dataset is a test-only
exercisesandaddthemtotheprevioustrainingset dataset(Pateletal.,2021),consistingof1,000En-
(lines12-16inAlg.1). Inthisway,thetrainingset glish MWPs generated by introducing challeng-
growsprogressivelyandcoversmoreknowledge, ingvariationstoexistingproblems. Weadoptthe
leadingtoastrongerstudentMWPsolver. two evaluation settings proposed in (Patel et al.,
14388

|     |     |     |     |     | MAWPS(ID) | ASDiv-a(ID) |     |     | SVAMP(ID) |     | SVAMP(OOD) |     |     |
| --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | --------- | --- | ---------- | --- | --- |
Priorbest(Fine-tuning) 92.0/121Ma 82.2/144Mb 65.0/144Mb 47.3/121Ma
| Priorbest(KnowledgeDistillation) |     |     |     |     | 94.5/11.3Bc |     |     |     |     |     | 20.7/6.7Bd |     |     |
| -------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ---------- | --- | --- |
|                                  |     |     |     |     |             |     | −   |     | −   |     |            |     |     |
Few-shotCoT(Weietal.,2022b) 93.3/540B 93.1/175B 79.0/540B 79.0/540B
∗
|     |     | LSTM(20M) |     |     | 82.6 |     | 71.4 |     | 45.0 |     |     | 30.8 |     |
| --- | --- | --------- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
Without
|     |     | Base(144M) |     |     | 88.5 |     | 81.2 |     | 69.2 |     |     | 41.0 |     |
| --- | --- | ---------- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
CEMAL
|     |     | Large(377M) |     |     | 90.4 |     | 87.6 |     | 78.5 |     |     | 49.5 |     |
| --- | --- | ----------- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
|     |     | LSTM(20M)   |     |     | 92.0 |     | 86.9 |     | 67.1 |     |     | 53.4 |     |
CEMAL
|     |     | Base(144M) |     |     | 93.9 |     | 90.9 |     | 81.5 |     |     | 68.6 |     |
| --- | --- | ---------- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
(OurSolvers)
|     |     | Large(377M) |     |     | 94.7 |     | 93.3 |     | 85.4 |     |     | 76.4 |     |
| --- | --- | ----------- | --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
Table1: Wecomparetheaccuracyandnumberofparameterson4benchmarksintheformatof(accuracy/number
ofparameters). Priorbestbaselinesarethefollowing. a: (Jieetal.,2022), b: (Pateletal.,2021), c: (Magister
et al., 2022), d: (Ho et al., 2022). On each dataset, the best performance is bolded and the second best is in
italics. : This accuracy is calculated on the ASDiv-a subset out of ASDiv based on the results in https://
∗
github.com/jasonwei20/chain-of-thought-prompting.
IDdenotesthein-distributiontestandOODdenotes
theout-of-distributiontest.
2021). The first setting employs a 5-fold cross- RTXA6000graphicscard,implementedinPython
validationapproachonthe1,000MWPs,incorpo- using the PyTorch framework. The training was
rating MAWPS (Koncel-Kedziorski et al., 2016) performedfor50epochswithabatchsizeof16,us-
and ASDiv-a (Miao et al., 2020) as additional ingtheAdamW(KingmaandBa,2015;Loshchilov
training data for each fold. In the second setting, and Hutter, 2018) optimizer with an initial learn-
MAWPS and ASDiv-a serve as the training set, ingrateof8e-6forthepre-trainedmodelpart(i.e.
whileSVAMPisusedasthetestingset. RoBERTa) and 5e-4 for the GTS decoder, which
|            |         |     |               |     |             | was | halved | every | 20  | epochs. | The | weight | decay |
| ---------- | ------- | --- | ------------- | --- | ----------- | --- | ------ | ----- | --- | ------- | --- | ------ | ----- |
| Evaluation | Setting |     | We categorize |     | the evalua- |     |        |       |     |         |     |        |       |
duringtrainingwassetto0.01,andadropoutrate
| tions on | MAWPS, | ASDiv-a, |     | and the | first setting |     |     |     |     |     |     |     |     |
| -------- | ------ | -------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
of0.25wasappliedtothedecodertopreventover-
onSVAMPasin-distribution(ID)tests,astheyall
fitting. Thetrainingsetwillbeaugmentedduring
involve5-foldcross-validationonaspecificdataset.
|     |     |     |     |     |     | epoch | 10  | and epoch | 20, | i.e., | lines | 8-18 | in Alg. 1 |
| --- | --- | --- | --- | --- | --- | ----- | --- | --------- | --- | ----- | ----- | ---- | --------- |
Conversely,thesecondsettingonSVAMPiscon-
|         |                        |     |     |       |             | willonlybeexecutedatepoch10and20. |     |     |     |     |     |     | mandn |
| ------- | ---------------------- | --- | --- | ----- | ----------- | --------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| sidered | an out-of-distribution |     |     | (OOD) | test, given |                                   |     |     |     |     |     |     |       |
inSection3.2aresetto20and4,respectively,with
thatthetrainingandtestingsetsoriginatefromdis-
|     |     |     |     |     |     | the | aim | of pushing | the | limit | of small | math | word |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | -------- | ---- | ---- |
tinctsources.
problemsolveraccuraciesandachievinghigherper-
|     |     |     |     |     |     | formance. |     | Thisisorthogonaltothecontributionof |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
4.2 Implementation
thispaperbecauseourproposedcustomizedgener-
The backbone of our pre-trained encoder is a ationstrategyandexercisebookaredemonstrated
| RoBERTa | model | (Liu | et al., | 2019b). | For LLM, |                                   |     |     |     |     |     |            |     |
| ------- | ----- | ---- | ------- | ------- | -------- | --------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
|         |       |      |         |         |          | tobeeffectiveinSections4.4and4.5. |     |     |     |     |     | Althoughwe |     |
weusetheChatGPTgpt-3.5-turboAPItoperform
understandthatfurtherincreasingtheoccurrences
| problemgeneration. |     | Toencourageamorediverse |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofvalidationandaugmentationwillfurtherboost
| generation,wesetthetemperatureto1.25. |     |     |     |     | Allthe |     |           |     |       |       |           |     |            |
| ------------------------------------- | --- | --- | --- | --- | ------ | --- | --------- | --- | ----- | ----- | --------- | --- | ---------- |
|                                       |     |     |     |     |        | our | accuracy, | we  | limit | their | magnitude |     | for better |
experimentsinthispapercanbeconductedwitha
|     |     |     |     |     |     | efficiencyandlowercostonAPIcalls. |     |     |     |     |     | Duringval- |     |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
costlowerthan100dollarsonOpenAIAPIcalls.
|     |     |     |     |     |     | idation, |     | we generate | 2   | zero-shot |     | and 2 | few-shot |
| --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | --------- | --- | ----- | -------- |
Forevaluation,weusetheaccuracyofanswervalue similar problems for each source problem in the
asourevaluationmetricfollowingallthebaselines.
|     |     |     |     |     |     | exercisebook,thereforek |     |     |     | =   | 4inAlg. | 1.  |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | ------- | --- | --- |
Sincetheanswervaluecanbecalculatedfromdif-
| ferent equations, |     | it is | more reasonable |     | to check |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
4.3 ComparisonwithBaselines
| if the value | is  | correct, | rather | than | checking the |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ------ | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
element-wiseequivalenceofageneratedequation In order to demonstrate the effectiveness of our
andthecorrespondinggroundtruthequation. knowledgedistillationapproach,wecompareour
WeconductedallexperimentsusinganNVIDIA methodwithseveralstrongbaselines,includingthe
14389

|         |          |     |     | In-Distribution |      |        |      | Trainingset    |      | Samesize      |      |      |
| ------- | -------- | --- | --- | --------------- | ---- | ------ | ---- | -------------- | ---- | ------------- | ---- | ---- |
| Dataset | Backbone |     |     |                 |      |        |      |                |      |               | n=2  | n=4  |
|         |          |     |     |                 |      |        |      | asexercisebook |      | astrainingset |      |      |
|         |          |     |     | Random          | Half | Target |      |                |      |               |      |      |
|         |          | GTS |     | 77.5            | 77.8 |        |      |                |      |               |      |      |
|         |          |     |     |                 |      | 79.0   | Base |                | 54.6 | 59.8          | 60.4 | 65.2 |
ASDiv-a RoBERTa-base 84.3 85.2 84.6 Large 64.7 69.8 70.2 72.7
|       | RoBERTa-large |     |     | 90.1 | 90.3 | 90.6 |               |                                         |          |               |                |     |
| ----- | ------------- | --- | --- | ---- | ---- | ---- | ------------- | --------------------------------------- | -------- | ------------- | -------------- | --- |
|       |               |     |     |      |      |      | Table3:       | Performancecomparisonofusingtrainingset |          |               |                |     |
|       |               | GTS |     | 89.2 | 88.9 | 89.3 |               |                                         |          |               |                |     |
|       |               |     |     |      |      |      | and different |                                         | sizes of | exercise book | for validation | on  |
| MAWPS | RoBERTa-base  |     |     | 90.3 | 90.3 | 91.0 | SVAMPdataset. |                                         |          |               |                |     |
|       | RoBERTa-large |     |     | 91.4 | 92.3 | 92.8 |               |                                         |          |               |                |     |
|       |               | GTS |     | 47.7 | 49.6 | 50.3 |               |                                         |          |               |                |     |
SVAMP RoBERTa-base 72.1 72.8 4.4 AnalysisonGenerationStrategy
73.3
RoBERTa-large 80.8 79.9 80.9 Theperformanceofstudentsolverscanbesignif-
Out-of-Distribution icantly impacted by the generation strategies em-
| Dataset | Backbone |     |     |     |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Random Half Target ployedtocreatetheexerciseproblems. Inthisanal-
ysis,weexploretheeffectivenessofthreedifferent
|       |               | GTS |     | 33.6 | 36.3 | 38.2 |                       |           |     |                           |     |          |
| ----- | ------------- | --- | --- | ---- | ---- | ---- | --------------------- | --------- | --- | ------------------------- | --- | -------- |
|       |               |     |     |      |      |      | generationstrategies: |           |     | random,half,andtarget(us- |     |          |
| SVAMP | RoBERTa-base  |     |     | 50.1 | 50.8 | 55.3 |                       |           |     |                           |     |          |
|       |               |     |     |      |      |      | ingthresholdvaluesofλ |           |     | = 0,0.5,1,respectively)   |     |          |
|       | RoBERTa-large |     |     | 62.9 | 63.1 | 65.0 |                       |           |     |                           |     |          |
|       |               |     |     |      |      |      | on three              | datasets, | in  | both in-distribution      |     | and out- |
Table2: Resultsofdifferentproblemgenerationstrate- of-distributionsettings. Ourgoalistoidentifythe
giesonthreedatasetsunderin-distributionandout-of- best strategy for maximizing the student model’s
| distribution(OOD)testing. |     |     | Boldfaceindicatesthebest |     |     |     |              |     |                                |     |     |     |
| ------------------------- | --- | --- | ------------------------ | --- | --- | --- | ------------ | --- | ------------------------------ | --- | --- | --- |
|                           |     |     |                          |     |     |     | performance. |     | Weremovetheinitialaugmentation |     |     |     |
resultamongthethreestrategies. (setting m = 0) and lower the number of genera-
|     |     |     |     |     |     |     | tions                                   | in this | analysis                        | to improve | the efficiency | of  |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------- | ------------------------------- | ---------- | -------------- | --- |
|     |     |     |     |     |     |     | theexperiments.                         |         | Therefore,theresultspresentedin |            |                |     |
|     |     |     |     |     |     |     | Table2differfromourbestresultsinTable1. |         |                                 |            |                | Our |
analysisrevealsthatthetargetedgenerationstrat-
|                 |     |           |     |                   |     |     | egy mostly |     | outperforms | the other | two strategies. |     |
| --------------- | --- | --------- | --- | ----------------- | --- | --- | ---------- | --- | ----------- | --------- | --------------- | --- |
| best fine-tuned |     | baseline, | the | best LLM-enhanced |     |     |            |     |             |           |                 |     |
Thissuggeststhatourproposedtargetedgeneration
knowledgedistillationbaseline,andfew-shotchain-
|            |       |           |     |      |         |         | is an | effective  | approach | for identifying |     | the weak  |
| ---------- | ----- | --------- | --- | ---- | ------- | ------- | ----- | ---------- | -------- | --------------- | --- | --------- |
| of-thought | (CoT) | prompting |     | (Wei | et al., | 2022b), |       |            |          |                 |     |           |
|            |       |           |     |      |         |         | areas | of student | solvers  | and improving   |     | them in a |
usingtheMAWPS,ASDiv-a,andSVAMPdatasets.
customizedway.
| The results | presented |     | in Table | 1   | show that | our |     |     |     |     |     |     |
| ----------- | --------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
approach outperforms all the baselines on the Moreover,wecanclearlyseethattheimprove-
|     |     |     |     |     |     |     | ment | is more | noticeable | in the OOD | scenario. | A   |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ---------- | ---------- | --------- | --- |
MAWPSandASDiv-adatasets,achieving94.7%
possiblereasonforthiscouldbethatintheIDsitu-
| and 93.3% | solving | accuracy, |     | respectively. |     | For |     |     |     |     |     |     |
| --------- | ------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ation,wherethetrainingandtestingsetshavesome
theSVAMPdataset,ourapproachoutperformsthe
sharedknowledgecomponents,usingrandomgen-
| best LLM-enhanced |     | knowledge |     | distillation |     | base- |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
erationforthesourceproblemsinthetrainingset
| line, achieving |     | 85.4% | accuracy | on  | the SVAMP |     |     |     |     |     |     |     |
| --------------- | --- | ----- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
alsohelpstoenhancetheperformanceonthetest-
| (ID) dataset, | which | is  | a significant |     | improvement |     |     |     |     |     |     |     |
| ------------- | ----- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
overthepriorbestaccuracyof65.0%achievedby ing set. On the other side, in the OOD scenario,
wherethere’salargegapbetweenthetrainingand
| fine-tuning. | On       | the SVAMP |     | (OOD)    | dataset, | our    |         |       |              |             |          |     |
| ------------ | -------- | --------- | --- | -------- | -------- | ------ | ------- | ----- | ------------ | ----------- | -------- | --- |
|              |          |           |     |          |          |        | testing | sets, | our approach | of creating | tailored | ex- |
| approach     | achieves | a solving |     | accuracy | of       | 76.4%, |         |       |              |             |          |     |
ercisesspecificallytargetstheweakpointsofthe
| which | is lower | than CoT-based |     | LLMs, | but | much |     |     |     |     |     |     |
| ----- | -------- | -------------- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- |
studentmodel,leadingtoamoreeffectiveboostin
| higherthanthefine-tunedbaselines. |     |     |     |     | Wealsoshow |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
itsaccuracy.
theoriginalperformanceofbackbonesolverswith-
| out any  | additional | exercises. |             | To obtain | best      | per- |     |                        |     |     |     |     |
| -------- | ---------- | ---------- | ----------- | --------- | --------- | ---- | --- | ---------------------- | --- | --- | --- | --- |
|          |            |            |             |           |           |      | 4.5 | AnalysisonExerciseBook |     |     |     |     |
| formance | in Table   | 1,         | our solvers |           | use about | 20x  |     |                        |     |     |     |     |
moreMWPsthantheoriginaltrainingsettotrain. We conducted an experiment to demonstrate the
Overall,ourresultsindicatethatourknowledgedis- effectivenessofourproposedexercisebookbyre-
tillation approach achieves superior performance placingtheoriginaltrainingsetwiththeexercise
withmuchfewerparametersthanthepriorstate-of- book and changing the size m. As illustrated in
the-artLLMs,andoutperformsthebestfine-tuning Table3,theperformanceofgeneratingasame-size
andknowledgedistillationbaselinesonalldatasets. exercisebookissignificantlybetterthanthatofus-
14390

14391

| 4.7 CaseStudy |           |     |                |     |          |     | Ourcurrentfilteringprocessonlyeliminatesprob- |     |     |     |                   |     |     |
| ------------- | --------- | --- | -------------- | --- | -------- | --- | --------------------------------------------- | --- | --- | --- | ----------------- | --- | --- |
|               |           |     |                |     |          |     | lemswithincorrectformatting.                  |     |     |     | Thus,thereexistsa |     |     |
| InTable4,     | wepresent |     | severalexample |     | problems |     |                                               |     |     |     |                   |     |     |
significantopportunityforenhancingtheeffective-
| generated | by  | our method, |     | comprising | both | high- |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
nessofourapproachbyincorporatingmechanisms
| quality | and problematic |     |     | outputs. | The first | case |     |     |     |     |     |     |     |
| ------- | --------------- | --- | --- | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
forevaluatingandensuringthequalityandcorrect-
demonstratestheLLM’sabilitytoproduceamath-
nessofthegeneratedexercises.
ematicallyequivalentproblemusingdistinctkey-
words. Thesecondsuccessfulinstanceyieldsasub-
problemderivedfromthesourceproblem,which
References
| has been | proven | to  | facilitate | a better | understand- |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
GhodaiAbdelrahman,QingWang,andBernardoNunes.
| ing of | mathematical |     | word | problems | for models |     |       |                   |     |          |     |            |     |
| ------ | ------------ | --- | ---- | -------- | ---------- | --- | ----- | ----------------- | --- | -------- | --- | ---------- | --- |
|        |              |     |      |          |            |     | 2023. | Knowledgetracing: |     | Asurvey. |     | ACMComput- |     |
(Shridharetal.,2022a). However,notallgenerated ingSurveys,55(11):1±37.
| problemsareideal. |     |     | Asillustratedinthethirdexam- |     |     |     |            |          |     |       |             |     |         |
| ----------------- | --- | --- | ---------------------------- | --- | --- | --- | ---------- | -------- | --- | ----- | ----------- | --- | ------- |
|                   |     |     |                              |     |     |     | Tom Brown, | Benjamin |     | Mann, | Nick Ryder, |     | Melanie |
ple,ourmethodoccasionallygeneratesMWPswith
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
incorrectformatting,renderingthemunsuitablefor
Neelakantan,PranavShyam,GirishSastry,Amanda
trainingoursolver. Asaresult,wefilteroutsuch Askell,etal.2020. Languagemodelsarefew-shot
outputstomaintainthequalityandaccuracyofour learners. NeruIPS,33:1877±1901.
trainingdata,bycheckingifthegeneratedanswer
|     |     |     |     |     |     |     | Wenhu Chen, |     | Xueguang | Ma, | Xinyi | Wang, | and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | ----- | ----- | --- |
isavalidmathematicalequation. William W Cohen. 2022. Program of thoughts
|     |     |     |     |     |     |     | prompting: | Disentanglingcomputationfromreason- |           |     |        |       |          |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------------------------- | --------- | --- | ------ | ----- | -------- |
|     |     |     |     |     |     |     | ing for    | numerical                           | reasoning |     | tasks. | arXiv | preprint |
5 Conclusion
arXiv:2211.12588.
Inthiswork,wepresentanovelapproachCEMAL AakankshaChowdhery,SharanNarang,JacobDevlin,
to use large language models to facilitate knowl- Maarten Bosma, Gaurav Mishra, Adam Roberts,
|                   |     |     |      |              |          |     | Paul Barham, |           | Hyung | Won Chung, |       | Charles | Sutton, |
| ----------------- | --- | --- | ---- | ------------ | -------- | --- | ------------ | --------- | ----- | ---------- | ----- | ------- | ------- |
| edge distillation |     | in  | math | word problem | solving. |     |              |           |       |            |       |         |         |
|                   |     |     |      |              |          |     | Sebastian    | Gehrmann, |       | et al.     | 2022. | Palm:   | Scaling |
Ourmethodfirstgeneratesanexercisebooktoeval-
|     |     |     |     |     |     |     | language | modeling | with | pathways. |     | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | --------- | --- | ----- | -------- |
uatestudentmodelsandthenprovidesadditional
arXiv:2204.02311.
trainingexercisesthatarecustomizedtothelearn-
|     |     |     |     |     |     |     | AlbertTCorbettandJohnRAnderson.1994. |     |     |     |     |     | Knowl- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | ------ |
ingneedsofthestudentmodel,therebyimproving
|     |     |     |     |     |     |     | edgetracing: | Modelingtheacquisitionofprocedural |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------- | --- | --- | --- | --- | --- |
thestudentsolver’sabilitytosolveMWP.Ourex- knowledge. Usermodelinganduser-adaptedinter-
| tensiveexperimentalresultsdemonstratethatour |     |     |     |     |     |     | action,4:253±278. |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
proposedapproachoutperformsallfine-tunedand
|     |     |     |     |     |     |     | Jacob Devlin, | Ming-Wei |     | Chang, | Kenton | Lee, | and |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ------ | ------ | ---- | --- |
knowledge distillation baselines on all datasets, KristinaToutanova.2019. Bert: Pre-trainingofdeep
whileachievingcompetitiveperformanceagainst bidirectionaltransformersforlanguageunderstand-
LLMswithsignificantlyfewerparameters. Addi- ing. InNAACL,pages4171±4186.
tionally,weexploredifferentselectiongeneration Shizhe Diao, Pengcheng Wang, Yong Lin, and Tong
|     |     |     |     |     |     |     | Zhang. | 2023. | Active | prompting |     | with chain-of- |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------ | --------- | --- | -------------- | --- |
strategies,revealingthatourproposedcustomized
generation strategy is the most effective method, thoughtforlargelanguagemodels. arXivpreprint
arXiv:2302.12246.
| especiallyinthein-distributionsetting. |     |     |     |     | Inourfu- |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
turework,weaimtoextendthisapproachtoother CharlesRFletcher.1985. Understandingandsolving
NLPtaskstoevaluateitsgeneralizationcapability. arithmeticwordproblems: Acomputersimulation.
BehaviorResearchMethods,Instruments,&Comput-
ers,17(5):565±571.
Limitations
|     |     |     |     |     |     |     | PeggyGrantandDaleBasye.2014. |     |     |     | Personalizedlearn- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------ | --- | --- |
Firstly, our approach necessitates meticulous ing: Aguideforengagingstudentswithtechnology.
InternationalSocietyforTechnologyinEducation.
| prompt | design | to  | generate | exercises, | which | in- |     |     |     |     |     |     |     |
| ------ | ------ | --- | -------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
evitably entails human intervention. This aspect JohnHattieandHelenTimperley.2007. Thepowerof
could introduce potential bias or variability and feedback. Reviewofeducationalresearch,77(1):81±
112.
maynotscaleefficiently.
Secondly,wehavenotexplicitlyaddressedthe Mary Hegarty, Richard E Mayer, and Christopher A
|     |     |     |     |     |     |     | Monk. | 1995. | Comprehension |     | of arithmetic |     | word |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------------- | --- | ------------- | --- | ---- |
qualityandcorrectnessofthegeneratedproblems.
|     |     |     |     |     |     |     | problems: | A   | comparison | of  | successful | and | unsuc- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | ---------- | --- | ------ |
Codesanddataareavailableathttps://github.com/ cessfulproblemsolvers. Journalofeducationalpsy-
| Zhenwen-NLP/CEMAL. |     |     |     |     |     |     | chology,87(1):18. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
14392

NamgyuHo,LauraSchmid,andSe-YoungYun.2022. ShiyangLi,JianshuChen,YelongShen,ZhiyuChen,
Largelanguagemodelsarereasoningteachers. arXiv Xinlu Zhang, Zekun Li, Hong Wang, Jing Qian,
preprintarXiv:2212.10071. Baolin Peng, Yi Mao, et al. 2022a. Explanations
|     |     |     |     | from large | language | models |     | make small | reasoners |
| --- | --- | --- | --- | ---------- | -------- | ------ | --- | ---------- | --------- |
SeppHochreiterandJürgenSchmidhuber.1997. Long better. arXivpreprintarXiv:2210.06726.
| short-termmemory. | Neuralcomputation,9(8):1735± |     |     |                                            |     |     |     |     |       |
| ----------------- | ---------------------------- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ----- |
| 1780.             |                              |     |     | ZhongliLi,WenxuanZhang,ChaoYan,QingyuZhou, |     |     |     |     |       |
|                   |                              |     |     | ChaoLi,HongzhiLiu,andYunboCao.2022b.       |     |     |     |     | Seek- |
MohammadJavadHosseini,HannanehHajishirzi,Oren ingpatterns,notjustmemorizingprocedures: Con-
Etzioni,andNateKushman.2014. Learningtosolve trastive learning for solving math word problems.
| arithmeticwordproblemswithverbcategorization. |     |     |     | FindingsofACL. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
InEMNLP,pages523±533.
ZhenwenLiang,DianYu,XiaomanPan,WenlinYao,
|     |     |     |     | Qingkai | Zeng, Xiangliang |     | Zhang, | and | Dong Yu. |
| --- | --- | --- | --- | ------- | ---------------- | --- | ------ | --- | -------- |
DanqingHuang,ShumingShi,Chin-YewLin,andJian
2023. Mint:Boostinggeneralizationinmathematical
| Yin.2017. | Learningfine-grainedexpressionstosolve |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mathwordproblems. InEMNLP,pages805±814. reasoningviamulti-viewfine-tuning. arXivpreprint
arXiv:2307.07951.
| Shifeng | Huang, Jiawei Wang, | Jiao Xu,   | Da Cao, and |                |        |     |        |           |          |
| ------- | ------------------- | ---------- | ----------- | -------------- | ------ | --- | ------ | --------- | -------- |
|         |                     |            |             | Zhenwen Liang, | Jipeng |     | Zhang, | Lei Wang, | Wei Qin, |
| Ming    | Yang. 2021. Recall  | and learn: | A memory-   |                |        |     |        |           |          |
YunshiLan,JieShao,andXiangliangZhang.2022a.
| augmentedsolverformathwordproblems. |     |     | InFind- |           |                    |     |     |              |     |
| ----------------------------------- | --- | --- | ------- | --------- | ------------------ | --- | --- | ------------ | --- |
|                                     |     |     |         | Mwp-bert: | Numeracy-augmented |     |     | pre-training | for |
ingsofEMNLP,pages786±796.
|     |     |     |     | mathwordproblemsolving. |     |     |     | InNAACL,pages997± |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | ----------------- | --- |
1009.
| ZhanmingJie,JieruiLi,andWeiLu.2022. |     |                        | Learning |     |     |     |     |     |     |
| ----------------------------------- | --- | ---------------------- | -------- | --- | --- | --- | --- | --- | --- |
| toreasondeductively:                |     | Mathwordproblemsolving |          |     |     |     |     |     |     |
ZhenwenLiang,JipengZhang,andXiangliangZhang.
ascomplexrelationextraction. InACL,pages5944± 2022b. Analogicalmathwordproblemssolvingwith
5955.
|     |     |     |     | enhancedproblem-solutionassociation. |     |     |     |     | EMNLP. |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ------ |
Diederik P Kingma and Jimmy Ba. 2015. Adam: A ZhenwenLiangandXiangliangZhang.2021. Solving
| methodforstochasticoptimization. |     | ICLR. |     |           |          |      |         |              |     |
| -------------------------------- | --- | ----- | --- | --------- | -------- | ---- | ------- | ------------ | --- |
|                                  |     |       |     | math word | problems | with | teacher | supervision. | In  |
IJCAI,pages3522±3528.
| KennethRKoedingerandMitchellJNathan.2004. |     |     | The |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
realstorybehindstoryproblems: Effectsofrepresen- AlisaLiu,SwabhaSwayamdipta,NoahASmith,and
tationsonquantitativereasoning. Thejournalofthe YejinChoi.2022. Wanli: Workerandaicollabora-
learningsciences,13(2):129±164. tionfornaturallanguageinferencedatasetcreation.
FindingsofEMNLP.
TakeshiKojima,ShixiangShaneGu,MachelReid,Yu-
takaMatsuo,andYusukeIwasawa.2022. Largelan- Qianying Liu, Wenyu Guan, Sujian Li, Fei Cheng,
|                                   |     |     |          | Daisuke       | Kawahara, | and | Sadao | Kurohashi.        | 2021. |
| --------------------------------- | --- | --- | -------- | ------------- | --------- | --- | ----- | ----------------- | ----- |
| guagemodelsarezero-shotreasoners. |     |     | NeurIPS. |               |           |     |       |                   |       |
|                                   |     |     |          | Roda: reverse | operation |     | based | data augmentation |       |
Rik Koncel-Kedziorski, Hannaneh Hajishirzi, Ashish forsolvingmathwordproblems. IEEE/ACMTrans-
Sabharwal, Oren Etzioni, and Siena Dumas Ang. actionsonAudio,Speech,andLanguageProcessing,
| 2015. | Parsing algebraic | word problems | into equa- | 30:1±11. |     |     |     |     |     |
| ----- | ----------------- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- |
tions. TACL,3:585±597.
|     |     |     |     | Qianying Liu, | Wenyv | Guan, | Sujian | Li, | and Daisuke |
| --- | --- | --- | --- | ------------- | ----- | ----- | ------ | --- | ----------- |
RikKoncel-Kedziorski,SubhroRoy,AidaAmini,Nate Kawahara.2019a. Tree-structureddecodingforsolv-
|                                     |     |     |        | ingmathwordproblems. |     |     | InEMNLP,pages2370± |     |     |
| ----------------------------------- | --- | --- | ------ | -------------------- | --- | --- | ------------------ | --- | --- |
| Kushman,andHannanehHajishirzi.2016. |     |     | Mawps: |                      |     |     |                    |     |     |
2379.
| Amathwordproblemrepository. |     | InNAACL,pages |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
1152±1157.
YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
|               |             |                   |     | dar Joshi, | Danqi | Chen, | Omer | Levy, | Mike Lewis, |
| ------------- | ----------- | ----------------- | --- | ---------- | ----- | ----- | ---- | ----- | ----------- |
| Nate Kushman, | Yoav Artzi, | Luke Zettlemoyer, | and |            |       |       |      |       |             |
Regina Barzilay. 2014. Learning to automatically Luke Zettlemoyer, and Veselin Stoyanov. 2019b.
|       |                        |         |            | Roberta: | A robustly                     | optimized |     | bert pretraining | ap- |
| ----- | ---------------------- | ------- | ---------- | -------- | ------------------------------ | --------- | --- | ---------------- | --- |
| solve | algebra word problems. | In ACL, | pages 271± |          |                                |           |     |                  |     |
|       |                        |         |            | proach.  | arXivpreprintarXiv:1907.11692. |           |     |                  |     |
281.
|             |                  |        |             | Ilya Loshchilov            | and | Frank | Hutter. | 2018. | Decoupled |
| ----------- | ---------------- | ------ | ----------- | -------------------------- | --- | ----- | ------- | ----- | --------- |
| Yihuai Lan, | Lei Wang, Qiyuan | Zhang, | Yunshi Lan, |                            |     |       |         |       |           |
|             |                  |        |             | weightdecayregularization. |     |       | InICLR. |       |           |
BingTianDai,YanWang,DongxiangZhang,andEe-
| PengLim.2022. | Mwptoolkit:Anopen-sourceframe- |     |     |                 |           |     |          |            |       |
| ------------- | ------------------------------ | --- | --- | --------------- | --------- | --- | -------- | ---------- | ----- |
|               |                                |     |     | Lucie Charlotte | Magister, |     | Jonathan | Mallinson, | Jakub |
work for deep learning-based math word problem Adamek, Eric Malmi, and Aliaksei Severyn. 2022.
solvers. InAAAI,volume36,pages13188±13190. Teaching small language models to reason. arXiv
preprintarXiv:2212.08410.
JieruiLi,LeiWang,JipengZhang,YanWang,BingTian
Dai,andDongxiangZhang.2019. Modelingintra- Shen-Yun Miao, Chao-Chun Liang, and Keh-Yih Su.
relationinmathwordproblemswithdifferentfunc- 2020. Adiversecorpusforevaluatinganddeveloping
tional multi-head attentions. In ACL, pages 6162± englishmathwordproblemsolvers. InACL,pages
| 6167. |     |     |     | 975±984. |     |     |     |     |     |
| ----- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
14393

Arindam Mitra and Chitta Baral. 2016. Learning to Yufei Wang, Can Xu, Qingfeng Sun, Huang Hu,
useformulastosolvesimplearithmeticproblems. In ChongyangTao,XiuboGeng,andDaxinJiang.2022.
ACL,pages2144±2153. Promda: Prompt-baseddataaugmentationforlow-
InACL,pages4242±4255.
resourcenlutasks.
| AnirbanMukherjeeandUtpalGarain.2008. |     |           |               |     | Areview |         |            |         |       |            |       |         |
| ------------------------------------ | --- | --------- | ------------- | --- | ------- | ------- | ---------- | ------- | ----- | ---------- | ----- | ------- |
|                                      |     |           |               |     |         |         | Jason Wei, | Yi Tay, | Rishi | Bommasani, | Colin | Raffel, |
| of methods                           | for | automatic | understanding |     | of      | natural |            |         |       |            |       |         |
languagemathematicalproblems. ArtificialIntelli- Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
genceReview,29:93±122. MaartenBosma,DennyZhou,DonaldMetzler,etal.
|     |     |     |     |     |     |     | 2022a. Emergentabilitiesoflargelanguagemodels. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
Arkil Patel, Satwik Bhattamishra, and Navin Goyal. TransactionsonMachineLearningResearch.
| 2021. | Are nlp | models | really | able to | solve | simple |     |     |     |     |     |     |
| ----- | ------- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
| mathwordproblems? |     |     | InNAACL,pages2080±2094. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Bosma,EdChi,QuocLe,andDennyZhou.2022b.
SubhroRoyandDanRoth.2015. Solvinggeneralarith- Chainofthoughtpromptingelicitsreasoninginlarge
meticwordproblems. InEMNLP,pages1743±1752. languagemodels. NeurIPS.
Subhro Roy, Tim Vieira, and Dan Roth. 2015. Rea- Peter West, Chandra Bhagavatula, Jack Hessel, Jena
soningaboutquantitiesinnaturallanguage. TACL, Hwang, Liwei Jiang, Ronan Le Bras, Ximing Lu,
|     |     |     |     |     |     |     | Sean Welleck, |     | and Yejin | Choi. | 2022. Symbolic |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ----- | -------------- | --- |
3:1±13.
|     |     |     |     |     |     |     | knowledgedistillation: |     | fromgenerallanguagemod- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ----------------------- | --- | --- | --- |
Zhihong Shao, Yeyun Gong, Yelong Shen, Min- elstocommonsensemodels. InNAACL,pages4602±
| lie Huang, | Nan        | Duan, | and        | Weizhu           | Chen. | 2023. | 4625. |     |     |     |     |     |
| ---------- | ---------- | ----- | ---------- | ---------------- | ----- | ----- | ----- | --- | --- | --- | --- | --- |
| Synthetic  | prompting: |       | Generating | chain-of-thought |       |       |       |     |     |     |     |     |
demonstrations for large language models. arXiv Zhipeng Xie and Shichao Sun. 2019. A goal-driven
tree-structuredneuralmodelformathwordproblems.
preprintarXiv:2302.00618.
InIJCAI,pages5299±5305.
JianhaoShen,YichunYin,LinLi,LifengShang,Xin
|                                 |     |     |     |     |           |     | Zhicheng Yang, |       | Jinghui Qin, | Jiaqi | Chen, and     | Xiao- |
| ------------------------------- | --- | --- | --- | --- | --------- | --- | -------------- | ----- | ------------ | ----- | ------------- | ----- |
| Jiang,MingZhang,andQunLiu.2021. |     |     |     |     | Generate& |     |                |       |              |       |               |       |
|                                 |     |     |     |     |           |     | dan Liang.     | 2022. | Unbiased     | math  | word problems |       |
rank: Amulti-taskframeworkformathwordprob-
Findingsof
lems. InFindingsofEMNLP,pages2269±2279. benchmarkformitigatingsolvingbias.
NAACL.
ShumingShi,YuehuiWang,Chin-YewLin,Xiaojiang
JiachengYe,JiahuiGao,JiangtaoFeng,ZhiyongWu,
| Liu, | and Yong | Rui. 2015. | Automatically |     |     | solving |         |              |       |        |         |      |
| ---- | -------- | ---------- | ------------- | --- | --- | ------- | ------- | ------------ | ----- | ------ | ------- | ---- |
|      |          |            |               |     |     |         | Tao Yu, | and Lingpeng | Kong. | 2022a. | Progen: | Pro- |
numberwordproblemsbysemanticparsingandrea-
gressivezero-shotdatasetgenerationviain-context
| soning. | InEMNLP,pages1132±1142. |     |     |     |     |     |           |                  |     |     |     |     |
| ------- | ----------------------- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | --- | --- | --- |
|         |                         |     |     |     |     |     | feedback. | FindingsofEMNLP. |     |     |     |     |
KumarShridhar,JakubMacina,MennatallahEl-Assady,
JiachengYe,JiahuiGao,QintongLi,HangXu,Jiangtao
TanmaySinha,ManuKapur,andMrinmayaSachan. Feng, Zhiyong Wu, Tao Yu, and Lingpeng Kong.
| 2022a.                            | Automatic | generation |         | of socratic | subques-     |     |                    |          |           |           |          |     |
| --------------------------------- | --------- | ---------- | ------- | ----------- | ------------ | --- | ------------------ | -------- | --------- | --------- | -------- | --- |
|                                   |           |            |         |             |              |     | 2022b.             | Zerogen: | Efficient | zero-shot | learning | via |
| tionsforteachingmathwordproblems. |           |            |         |             | InEMNLP.     |     |                    |          |           |           |          |     |
|                                   |           |            |         |             |              |     | datasetgeneration. |          | EMNLP.    |           |          |     |
| Kumar                             | Shridhar, | Alessandro | Stolfo, |             | and Mrinmaya |     |                    |          |           |           |          |     |
JipengZhang,LeiWang,RoyKa-WeiLee,YiBin,Yan
| Sachan.2022b. |     | Distillingmulti-stepreasoningcapa- |     |     |     |     |                                  |     |     |     |           |     |
| ------------- | --- | ---------------------------------- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --------- | --- |
|               |     |                                    |     |     |     |     | Wang,JieShao,andEe-PengLim.2020. |     |     |     | Graph-to- |     |
bilitiesoflargelanguagemodelsintosmallermod-
|     |     |     |     |     |     |     | tree learning | for | solving | math | word problems. | In  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ---- | -------------- | --- |
els via semantic decompositions. arXiv preprint ACL,pages3928±3937.
arXiv:2212.00193.
|             |                                |           |              |                |       |      | Chujie Zheng,    |     | Sahand Sabour, |         | Jiaxin Wen,  | and      |
| ----------- | ------------------------------ | --------- | ------------ | -------------- | ----- | ---- | ---------------- | --- | -------------- | ------- | ------------ | -------- |
| Ben Wang    | and                            | Aran      | Komatsuzaki. |                | 2021. | Gpt- |                  |     |                |         |              |          |
|             |                                |           |              |                |       |      | Minlie Huang.    |     | 2022.          | Augesc: | Large-scale  | data     |
| j-6b:       | A 6 billion                    | parameter |              | autoregressive |       | lan- |                  |     |                |         |              |          |
|             |                                |           |              |                |       |      | augmentation     |     | for emotional  | support | conversation |          |
| guagemodel. | https://github.com/kingoflolz/ |           |              |                |       |      |                  |     |                |         |              |          |
|             |                                |           |              |                |       |      | with pre-trained |     | language       | models. | arXiv        | preprint |
mesh-transformer-jax.
arXiv:2202.13047.
Lei Wang, Yan Wang, Deng Cai, Dongxiang Zhang, Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
andXiaojiangLiu.2018. Translatingamathword Nathan Scales, Xuezhi Wang, Dale Schuurmans,
problemtoaexpressiontree. InEMNLP,pages1064± OlivierBousquet,QuocLe,andEdChi.2023. Least-
1069.
|     |     |     |     |     |     |     | to-most              | prompting | enables | complex | reasoning | in  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --------- | ------- | ------- | --------- | --- |
|     |     |     |     |     |     |     | largelanguagemodels. |           | ICLR.   |         |           |     |
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,
| EdChi,andDennyZhou.2023. |     |     |     | Self-consistencyim- |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
proveschainofthoughtreasoninginlanguagemod-
els. ICLR.
| Yan Wang, | Xiaojiang     | Liu, | and  | Shuming | Shi.      | 2017. |     |     |     |     |     |     |
| --------- | ------------- | ---- | ---- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
| Deep      | neural solver | for  | math | word    | problems. | In    |     |     |     |     |     |     |
EMNLP,pages845±854.
14394

14395

14396