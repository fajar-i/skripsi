TheThirty-SeventhAAAIConferenceonArtificialIntelligence(AAAI-23)
Learning Logical Reasoning Using an Intelligent Tutoring System: A Hybrid
|     |     |     |     |     | Approach | to Student | Modeling |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
RogerNkambou1,JanieBrisson1,AngeTato1,2,SergeRobert1
|     |     | 1Universite´ |     | duQue´beca` |     | Montre´al,CentredeRechercheenIntelligenceArtificielle |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ----------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
201President-KennedyAvenue,Montreal,Quebec,H2X3Y7,Canada
2E´coledeTechnologieSupe´rieure
1111Notre-DameW.st.,Montre´al,Quebec,H3C6M8,Canada
{nkambou.roger,brisson.janie,robert.serge}@uqam.ca,ange-adrienne.nyamen-tato@etsmtl.ca
|     |     |     | Abstract |     |     |     | beansweredwithaproperunderstandingofhumanreason- |     |     |        |               |     |             |     |
| --- | --- | --- | -------- | --- | --- | --- | ------------------------------------------------ | --- | --- | ------ | ------------- | --- | ----------- | --- |
|     |     |     |          |     |     |     | ing processes                                    | and | the | active | participation |     | of relevant | ex- |
Inourpreviousworks,wepresentedLogic-MuseasanIntelli-
|     |     |     |     |     |     |     | perts, including |     | logicians, | psychologists, |     | education |     | profes- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | -------------- | --- | --------- | --- | ------- |
gentTutoringSystemthathelpslearnersimprovelogicalrea-
|        |           |          |           |            |     |            | sionals,   | and IT    | specialists. | By  | bringing   | together | specialists |         |
| ------ | --------- | -------- | --------- | ---------- | --- | ---------- | ---------- | --------- | ------------ | --- | ---------- | -------- | ----------- | ------- |
| soning | skills in | multiple | contexts. | Logic-Muse |     | components |            |           |              |     |            |          |             |         |
|        |           |          |           |            |     |            | from these | different | fields,      | the | Logic-Muse |          | project     | aims to |
werevalidatedandarguedbyexpertsthroughoutthedesign-
ing process (ITS researchers, logicians, and reasoning psy- study the basics of logical reasoning skills acquisition, un-
chologists).Acatalogofreasoningerrors(syntacticandse- derstand the difficulties associated with this learning, and
mantic)hasbeenestablished,inadditiontoanexplicitrepre- createanITSthatcandetect,diagnose,andcorrectreason-
sentationofsemanticknowledgeandthestructuresandmeta- ing errors in various situations. Logic-Muse’s architecture
structuresunderlyingconditionalreasoning.ABayesiannet- lookslikeaclassicalITSwithitsthreestandardmodelcom-
workwithexpertvalidationhasbeendevelopedandusedina
ponents:theknowledgedomainexpert,thelearner,andthe
BayesianKnowledgeTracing(BKT)processthatallowsthe
|           |        |         |         |            |          |          | tutor. The | participatory |     | approach | adopted | led | to the | devel- |
| --------- | ------ | ------- | ------- | ---------- | -------- | -------- | ---------- | ------------- | --- | -------- | ------- | --- | ------ | ------ |
| inference | of the | learner | skills. | This paper | presents | an eval- |            |               |     |          |         |     |        |        |
opmentofessentialcomponentsforconstructingtheLogic-
| uation | of the learner-model |     | components |     | in Logic-Muse | (a  |     |     |     |     |     |     |     |     |
| ------ | -------------------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MuseITS.Thesecomponentsincludethecatalogoferrors,
bayesianlearnermodel).Weconductedastudyandcollected
|           |        |              |     |               |     |              | a bayesian | network | for | logical | reasoning | skills, | and | some |
| --------- | ------ | ------------ | --- | ------------- | --- | ------------ | ---------- | ------- | --- | ------- | --------- | ------- | --- | ---- |
| data from | nearly | 300 students |     | who processed |     | 48 reasoning |            |         |     |         |           |         |     |      |
activities. These data were used to develop a psychometric remedialstrategiesthatpromotelearning.Theexpertshave
modelforinitializingthelearner’smodelandvalidatingthe previouslyelicited,validated,andarguedthesecomponents.
structureoftheinitialBayesiannetwork.Wehavealsodevel- Logic-Muse, in its current version, implements these com-
opedaneuralarchitectureonwhichamodelwastrainedto ponents for propositional logic and offers a panoply of ac-
support a deep knowledge tracing (DKT) process. The pro- tivities allowing a learner to develop his logical reasoning
posedneuralarchitectureimprovestheinitialversionofDKT skillsinseveralsituationsestablishedbythedomainexperts.
| by allowing  | the    | integration | of  | expert   | knowledge | (through      |            |            |      |            |     |              |       |          |
| ------------ | ------ | ----------- | --- | -------- | --------- | ------------- | ---------- | ---------- | ---- | ---------- | --- | ------------ | ----- | -------- |
|              |        |             |     |          |           |               | This       | paper aims | to   | evaluate   | the | learner      | model | of the   |
| the Bayesian | Expert | Validation  |     | Network) | and       | allowing bet- |            |            |      |            |     |              |       |          |
|              |        |             |     |          |           |               | Logic-Muse | ITS.       | More | precisely, | it  | uses machine |       | learning |
tergeneralizationofknowledgewithfewsamples.Theresults
|     |     |     |     |     |     |     | techniques | on human |     | participants’ |     | problem-solving |     | data to |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------------- | --- | --------------- | --- | ------- |
showasignificantimprovementinthepredictivepowerofthe
initializeandvalidatetheITSlearnermodel.
learnermodel.Theanalysisoftheresultsofthepsychometric
modelalsoillustratesanexcellentpotentialforimprovingthe
Bayesiannetwork’sstructureandthelearnermodel’sinitial- TheLearnerModelinLogic-Muse
izationprocess.
|     |     |     |     |     |     |     | Logic-Muse’s | learner |     | model | has several | dimensions. |     | The |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ----- | ----------- | ----------- | --- | --- |
episodicmemorykeepstrackoftheexercisesperformedby
Introduction thelearneraswellasallrelatedperformanceelements.The
|         |             |     |           |         |      |            | cognitive | model | is a Bayesian |     | network | (BN) | whose | nodes |
| ------- | ----------- | --- | --------- | ------- | ---- | ---------- | --------- | ----- | ------------- | --- | ------- | ---- | ----- | ----- |
| Decades | of research | in  | cognitive | science | show | that human |           |       |               |     |         |      |       |       |
arethe96unitsofknowledgerelatedtoreasoning,asiden-
reasoningdoesnotfunctionaccordinglytotherulesoffor-
tifiedbytheknowledgedomainspecialists.Thepriorprob-
mallogic(e.g.,(Cumminsetal.1991;Gilovich,Griffin,and
abilitiesaswellasthecausalrelationshipsbetweenthedif-
| Kahneman | 2002; | Markovits | and | Vachon | 1989; | Thompson |     |     |     |     |     |     |     |     |
| -------- | ----- | --------- | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ferentunitsofknowledgewerealsoestablishedbeforehand
1994)).Whenlookingforsolutionstoimprovehumanskills
|     |     |     |     |     |     |     | by the experts. |     | It is worth | noting | that | causality | in  | this case |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------ | ---- | --------- | --- | --------- |
inthisarea,severalquestionsarise:whatisimportantinthe
|            |            |             |     |      |     |             | materializes | the | influence | of  | one unit | of knowledge |     | in the |
| ---------- | ---------- | ----------- | --- | ---- | --- | ----------- | ------------ | --- | --------- | --- | -------- | ------------ | --- | ------ |
| assessment | of logical | competence? |     | What | are | the phenom- |              |     |           |     |          |              |     |        |
learningoftheother.Thenodesaredirectlyconnectedtothe
| ena involved | in  | the acquisition |     | of logical | reasoning | skills? |           |            |        |               |     |     |          |      |
| ------------ | --- | --------------- | --- | ---------- | --------- | ------- | --------- | ---------- | ------ | ------------- | --- | --- | -------- | ---- |
|              |     |                 |     |            |           |         | reasoning | activities | (items | corresponding |     | to  | Bayesian | net- |
WhatshouldbethecharacteristicsofanIntelligentTutoring
|             |           |     |            |     |          |        | work leaves). | The | skills | involved | in  | the Bayesian |     | network |
| ----------- | --------- | --- | ---------- | --- | -------- | ------ | ------------- | --- | ------ | -------- | --- | ------------ | --- | ------- |
| System (ITS | (Nkambou, |     | Mizoguchi, | and | Bourdeau | 2010)) |               |     |        |          |     |              |     |         |
includetheinhibitionofexceptionstothepremises,thegen-
designedtosupportthislearning?Thesequestionscanonly
erationofcounterexamplestotheconclusion,andtheability
Copyright©2023,AssociationfortheAdvancementofArtificial to manage all the relevant models for familiar, counterfac-
Intelligence(www.aaai.org).Allrightsreserved. tual,andabstractsituations(Markovits2013).Thesystem’s
15930

Familiar CF Abstract firmation of the Consequent inference (“If P then Q, Q is
I G M I G M I G M true, therefore P is true”) is referred to as AC, and the De-
| MPP FFD |     | 1 0 | 0 0 | 0 0 | 0   | 0 0 |             |            |     |           |        |         |             |
| ------- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------- | ------ | ------- | ----------- |
|         |     |     |     |     |     |     | nial of the | Antecedent |     | inference | (“If P | then Q, | P is false, |
MPP FMD 1 0 0 0 0 0 0 0 0 therefore Q is false”) referred to as DA) are both invalids
MTT FFD 1 0 1 0 0 0 0 0 0 since their putative conclusion does not necessarily follow
MTT-FMD 1 0 1 0 0 0 0 0 0 from the premises. These four logical forms are declined
AC FMA 0 1 1 0 0 0 0 0 0 in 3 levels of content based on a developmental model of
AC FFA 0 1 1 0 0 0 0 0 0 conditional reasoning. Markovits (2013) suggests that the
DA FMA 0 1 1 0 0 0 0 0 0 more a premise has familiar content, the more rapid and
DA FFA 0 1 1 0 0 0 0 0 0 easy the retrieval of a counter-example to invalid conclu-
MPP CCF 1 0 0 1 0 0 0 0 0 sionswillbe.Consequently,themorefamiliarapremiseis,
themorereasonerswillavoidreasoningerrors.Inthissense,
| MTT CCF |     | 1 0 | 1 1 | 0 1 | 0   | 0 0 |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AC CCF 0 1 1 0 1 1 0 0 0 Markovitshasdevelopedagraduatedscaleofcontentlevels
DA CCF 0 1 1 0 1 1 0 0 0 for a premise that grows in difficulty and level of abstrac-
tion.Thetransitionbetweentwolevelsofcontentisgradual
| MPP A |     | 1 0 | 0 1 | 0 0 | 1   | 0 0 |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anddoneinstages:whenalevelismastered,theskillinthe
| MTT A |     | 1 0 | 1 1 | 0 1 | 1   | 0 1 |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nextlevelbegins.
| AC A |     | 0 1 | 1 0 | 1 1 | 0   | 1 1 |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DA A 0 1 1 0 1 1 0 1 1 The familiar level contains meaningful premises repre-
|     |     |     |     |     |     |     | senting | a plausible | rule | linking two | known | entities | or cat- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ---- | ----------- | ----- | -------- | ------- |
I=Inhibit,G=Generate,M=Manage,CF=Contrarytofact
egories.Contenteffectswiththesetypesofinferenceshave
|     |     |     |     |     |     |     | been heavily | documented. |     | Investigations |     | of content-related |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | -------------- | --- | ------------------ | --- |
Table1:Q-matrixforconditionalreasoning
|          |            |       |             |     |             |         | variability | can    | fall under | a general     | perspective |           | called the |
| -------- | ---------- | ----- | ----------- | --- | ----------- | ------- | ----------- | ------ | ---------- | ------------- | ----------- | --------- | ---------- |
|          |            |       |             |     |             |         | “semantic   | memory | framework” | (De           | Neys,       | Schaeken, | and        |
|          |            |       |             |     |             |         | D’ydewalle  | 2002), | where      | the retrieval | of          | stored    | knowledge  |
| estimate | of student | skill | acquisition | is  | continually | updated |             |        |            |               |             |           |            |
primarilyimpactsreasoningwithmeaningfulpremises.The
everytimeastudentrespondstoaproblem,andthatanswer
impactofinformationretrievalonconditionalreasoninghas
isusedasevidencebythesystemtore-computetheproba-
|     |     |     |     |     |     |     | been mostly | observed |     | through the | effect | of potential | coun- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ----------- | ------ | ------------ | ----- |
bilitythatthisstudentknewtheskillbeforetheanswer.The
terexamplesonaputativeconclusion.FortheACandDAin-
| tutor then | chooses | exercises | based | on  | these probabilities. |     |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | ----- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ferences,suchcounterexamplesarealternativeantecedents,
| The episodic | memory |     | keeps track | of all | the exercises | per- |     |     |     |     |     |     |     |
| ------------ | ------ | --- | ----------- | ------ | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
i.e.,antecedentsthatdifferfromPbutimplytheconsequent
| formed by | the | learner. | The Q-Matrix | (built | by  | the experts) |            |     |         |             |                 |     |     |
| --------- | --- | -------- | ------------ | ------ | --- | ------------ | ---------- | --- | ------- | ----------- | --------------- | --- | --- |
|           |     |          |              |        |     |              | Q. For the | MPP | and MTT | inferences, | counterexamples |     | are |
illustratingtherelationshipbetweenitemtypes(16)andrea-
|               |     |              |     |       |          |             | disabling | conditions, | i.e. | a condition | that | prevents | the an- |
| ------------- | --- | ------------ | --- | ----- | -------- | ----------- | --------- | ----------- | ---- | ----------- | ---- | -------- | ------- |
| soning skills | (9) | relationship | is  | shown | in Table | 1. Figure 1 |           |             |      |             |      |          |         |
showsan excerptof theBayesian networkstructure, which tecedent P from implying the consequent Q. Many stud-
|            |                  |     |         |     |       |             | ies have | shown | that the | number of | potential | counterexam- |     |
| ---------- | ---------------- | --- | ------- | --- | ----- | ----------- | -------- | ----- | -------- | --------- | --------- | ------------ | --- |
| highlights | the relationship |     | between | the | items | (48 grouped |          |       |          |           |           |              |     |
ples(Cumminsetal.1991;Thompson1994)orthestrength
intothe16item-types)andthenine(9)knowledgeunits(or
|     |     |     |     |     |     |     | of association |     | between | them and | the premise |     | (De Neys, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | -------- | ----------- | --- | --------- |
reasoningskills)thattheexpertshaveidentified.
|     |     |     |     |     |     |     | Schaeken, | and | D’Ydewalle | 2003) | determines | approval | rate |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ----- | ---------- | -------- | ---- |
ofthefourformsofconditionalinference.Forexample,with
ItemBankforConditionalReasoning
thepremise“Ifarockisthrownatawindow,thenthewin-
The items used for conditional reasoning in Logic-Muse dowwillbreak,”reasonerswilltendtoaccepttheACinfer-
are the four logical forms of conditional reasoning: the ence (a window is broken; therefore, a rock was thrown at
Modus Ponendo Ponens (MPP), the Modus Tollendo Tol- it)lessoftenthanwiththepremise“Ifafingeriscut,thenit
|             |     |             |     |                |     |           | will bleed” | (a  | finger bleeds, | therefore | it  | has been | cut). The |
| ----------- | --- | ----------- | --- | -------------- | --- | --------- | ----------- | --- | -------------- | --------- | --- | -------- | --------- |
| lens (MTT), | the | Affirmation | of  | the Consequent |     | (AC), and |             |     |                |           |     |          |           |
theDenialoftheAntecedent(DA). reasonisthattheformerpremisecontainsmanyalternative
Thereasonwhywestartedwithconditionalreasoningis antecedents,likethrowingachair,acaraccident,atropical
that many experimental studies in psychology have high- storm,etc.,thatarecounterexamplestotheputativeconclu-
|             |             |     |             |          |           |      | sion, while | the | latter contains | fewer | of such | antecedents | (a  |
| ----------- | ----------- | --- | ----------- | -------- | --------- | ---- | ----------- | --- | --------------- | ----- | ------- | ----------- | --- |
| lighted the | significant |     | variability | of human | reasoning | with |             |     |                 |       |         |             |     |
fingeriscrushed,etc.).
inferencesofthesamelogicalformbutdifferingincontent
(e.g., (Cummins et al. 1991; Markovits and Vachon 1989; The counterfactual level contains a reversed causal rule
Thompson1994),andalargepartoftheliteratureonhuman knowntobefalse.Itallowsthegenerationofanunrealistic
reasoning aims to explain such variability. Much focus has category of alternative antecedents. For example, with the
beenplacedontheeffectsofcontentonconditional(if-then) counterfactualpremise”Ifa featheristhrownata window,
reasoning. According to the logical definition of the con- thenthewindowwillbreak”,onecouldgenerateacounter-
ditional connective, two of these inferences are valid, and factualalternativeantecedentlike”throwingtissueonawin-
twoareinvalid.TheModusPonendoPonensinference(“If dow”oradisablingconditionlike”Thewindowwasstrong
PthenQ,Pistrue,thereforeQistrue”),referredtoasMPP, enoughtostayintact.”
andtheModusTollendoTollensinference(“IfPthenQ,Q Theabstractlevelcontainsif-thenruleslinkingmade-up
is false, therefore P is false”) referred to as MTT are both words, e.g., “If one blops, then one will become plede.”
validandleadtonecessaryconclusions.Bycontrast,theAf- Thislevelrequiresanabstractrepresentationofthepremises
15931

Figure1:ExcerptoftheBayesiannetworkstructureforconditionalreasoning
that can generate abstract alternative antecedents. Accord-
Instructions
ingto(Markovits2013),whenareasonerreachesthislevel,
hehasacompleteunderstandingoftheimplicativelink:he Inthefollowingpages,wewillpresentrulesthatyoumust
understandsthatforaconditionalpremise(unknownorab- assumetobetrue.Followingtherule,anobservationwill
stract),analternativeantecedentcanbegeneratedregardless bepresentedtoyou.Yourtaskistoselecttheconclusion
of background knowledge. We thus have a total of 16 item thatlogicallyfollowsfromtheinformationprovided.Here
classes(itemnodesintheBN). isanexampleofaquestionthatyouwillhavetoanswer:
Supposeitistruethat:Ifwetouchsomethingthatisvery
hot,thenweburnourselves.Observation:Marcotouched
TrainingaCDMModeltoValidatetheBNand somethingthatisveryhot.Onecanconcludethat:
toInitializetheLearnerModel
• Marcoburnedhimself.
• Marcodidnotburnhimself.
Logic-Muse’s learner model aims to represent user knowl-
edge as accurately as possible using the Bayesian network • One cannot conclude whether Marco burned himself
we created. It allows for diagnosis and modeling of the ornot.
learner’s current state of mastery for each identified skill. Pleaseindicatebelowthatyouhavereadtheinstructions.
Validity and reliability are thus very important features of Then press the ”Next” button at the bottom right to start
thismodel.Inthispaper,wewillprovidedatatoinitiateand thequestionnaire.
evaluate our model’s validity. To this end, we will use the
RlibraryCDM(Georgeetal.2016;RavandandRobitzsch
2015)torunaCognitiveDiagnosisModeloninputdatapre- Table2:Instructionstothelearners
viously collected. This CDM model is built using the item
bank, a Q-Matrix (items/skills), and data from all student
responses to items (De La Torre 2009). The Q-Matrix (Ta- DataPreparation
ble 1) connects item categories to the involved skills. The
Foreachofthe48items,participantshadtochoosebetween
resulting model is part of the learner model and allows for
3answers(thevalidone,theinvalidtypicalone,andthein-
initialpredictionsofthelearner’sstateofmastery,givenhis
validatypicalone).Answerswereencodedas“1”forvalid
responsevector.
and“0otherwise.Wethenhadtochoosebetweenthreepos-
sibleresponsematricesaccordingtothenumberofvalidre-
DataCollection sponses for the three repeated measures for each of the 16
categories. Each category is encoded as 1 if the participant
Participantsandprocedures.Atotalof294participantswere was successful for at least 2 out of 3 items. This particu-
recruitedonlineviatheProlificAcademicplatform. lar threshold was chosen out of consistency with previous
Materials. For each of the 16 items classes, three items modelingchoices:amajorityofasuccessfulresponseisthe
were constructed. This was done in order to obtain a more criteriatoactivateacompetencenodeinourBayesianNet-
reliable measure for each competence class. At the begin- work.Table3showssomeexamplesofitems.
ning of the questionnaire, participants were given some in-
structions,asshowninTable2. CDMModelTypeSelectionandTraining
Theseinstructionsarefollowedbythepresentationofthe WethentrainedaCDMmodelonthe294responsepatterns,
48items,similartotheexampleabove. which allowed us to estimate various parameters: posterior
15932

Familiarcontent(F) astheapriorilikelihood(priorprobability)ofmasteringthe
| Fewdisablers(FD),Manyalternatives(MA) |     |     |     |     |     | rootnode. |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Majorpremise:Ifonejumpsinapool,thenoneiswet.
|     |     |     |     |     |     | The first | matrix | indicated | that | the most | probable | vector |
| --- | --- | --- | --- | --- | --- | --------- | ------ | --------- | ---- | -------- | -------- | ------ |
MPP FFD Observation Bobjumpedinapool. was the “111 000 000”, which means a learner masters the
Conclusion Bobiswet. three competences for the familiar level of content, but no
MTT FFD Observation Paulitnotwet. competence for the counterfactual and the abstract levels.
|     |            |                        |     |     |     | This seems | to show | a separation |     | between | the familiar | con- |
| --- | ---------- | ---------------------- | --- | --- | --- | ---------- | ------- | ------------ | --- | ------- | ------------ | ---- |
|     | Conclusion | Pauldidn’tjumpinapool. |     |     |     |            |         |              |     |         |              |      |
AC FMA Observation Johniswet. tentandtheothertwolevels.However,giventheveryhigh
Conclusion Onecannotconclude number of possible combinations for these nine competen-
DA FMA Observation Markdidn’tjumpinapool. cies, the other vectors were numerous, showed very small
Conclusion Onecannotconclude. probabilities,andmanywereequiprobable.Wethusdecided
|     |     |     |     |     |     | to use vector | classes | based | on  | the types | of competencies |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | ----- | --- | --------- | --------------- | --- |
Manydisablers(Md),fewalternatives(Fa)
Major:Ifamatchisscraped,thenitwilllightup. identified in our model. The a posteriori matrix based on
ourclassificationisshowninFigure2.Theleftcolumnrep-
| MPP FMd | Observation | Amatchwasscraped. |     |     |     |     |     |     |     |     |     |     |
| ------- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resentsthesixvectorclasseswecreated.Eachcontentlevel
|         | Conclusion  | Thematchwilllightup.   |     |     |     |            |                          |      |          |              |            |      |
| ------- | ----------- | ---------------------- | --- | --- | --- | ---------- | ------------------------ | ---- | -------- | ------------ | ---------- | ---- |
|         |             |                        |     |     |     | (familiar  | (F), counterfactual(CF), |      |          | abstract(A)) | represents | a    |
| MTT FMd | Observation | Thematchisnotlit.      |     |     |     |            |                          |      |          |              |            |      |
|         |             |                        |     |     |     | triplet of | skills (inhibit          | (I), | generate | (G),         | and manage | (M)) |
|         | Conclusion  | Thematchwasnotscraped. |     |     |     |            |                          |      |          |              |            |      |
AC FFa Observation Thematchislit. for this level, while each skill (inhibit, generate, manage)
referstothesameskillinallthreelevels(familiar,counter-
|     | Conclusion | Onecannotconclude. |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factualandabstract).Inthefirstrow,“successful”meansall
| DA FFa             | Observation | Thematchwasnotscraped. |     |     |     |                                         |         |               |     |           |            |        |
| ------------------ | ----------- | ---------------------- | --- | --- | --- | --------------------------------------- | ------- | ------------- | --- | --------- | ---------- | ------ |
|                    |             |                        |     |     |     | three skills                            | for the | corresponding |     | level (or | all three  | levels |
|                    | Conclusion  | Onecannotconclude.     |     |     |     |                                         |         |               |     |           |            |        |
|                    |             |                        |     |     |     | for the corresponding                   |         | skill)        | are | mastered, | regardless | of the |
| Abstractcontent(A) |             |                        |     |     |     | performanceintheothertwolevelsorskills. |         |               |     |           |            |        |
Major:Ifoneblops,thenonewillbecomeplede.
|       |             |                 |     |     |     | For example, | being | successful |     | in the familiar |     | class may |
| ----- | ----------- | --------------- | --- | --- | --- | ------------ | ----- | ---------- | --- | --------------- | --- | --------- |
| MPP A | Observation | Mary-Annbloped. |     |     |     |              |       |            |     |                 |     |           |
refertovectorssuchas“111111111”,“111011111”,“111
Conclusion Mary-Annwillbecomeplede. 011011”oreven“111000000”.Inthesecondrow,“failed”
MTT A Observation Frankdidnotbecomeplede. means the opposite: all three skills for the corresponding
Conclusion Frankdidnotblop. level(orallthreelevelsforthecorrespondingskill)arenot
| AC A | Observation | Michellebecameplede. |     |     |     |     |     |     |     |     |     |     |
| ---- | ----------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mastered,irrespectiveofalearner’sperformanceintheother
|     | Conclusion | Onecannotconclude. |     |     |     |            |            |     |                   |     |           |       |
| --- | ---------- | ------------------ | --- | --- | --- | ---------- | ---------- | --- | ----------------- | --- | --------- | ----- |
|     |            |                    |     |     |     | two levels | or skills. | The | “only successful” |     | row means | that, |
DA A Observation Peterdidnotblop. ofallthreeskillsorlevels,onlythecorrespondingoneisen-
Conclusion Onecannotconclude. tirely(111)mastered.Forexample,beingonlysuccessfulin
thefamiliarclassmaycomefromthevector“111011011”
| Table 3: | Sample items in | the database. | Conclusion |     | means |     |     |     |     |     |     |     |
| -------- | --------------- | ------------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
oreven“111000000”,butnot“111111010”or“111000
validconclusion.
111”.The“Onlyfailed”rowreferstotheoppositesituation:
onlythecorrespondingskillorleveltripleisfailed(atleast
onezerointhetriplet),whilethetwoothertripletsarefully
| probabilities,thegoodnessoffitindicator,guess(theproba- |     |     |     |     |     | mastered(111). |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
bilitythatalearnercouldcorrectlyansweranexercisewith-
| out having     | the necessary | skills), slip | (the          | probability | of a     |     |     |     |     |     |     |     |
| -------------- | ------------- | ------------- | ------------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| wrong solution | while the     | learner had   | the necessary |             | skills), |     |     |     |     |     |     |     |
tetrachoriccorrelations,andmarginalskillprobabilities.We
| had to choose | between a           | Deterministic | Input,   | Noisy | ”Or”  |     |     |     |     |     |     |     |
| ------------- | ------------------- | ------------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| gate (DINO)   | and a Deterministic | Input,        | Noisy    | ”And” | gate  |     |     |     |     |     |     |     |
| (DINA) CDM    | model. We           | opted for     | the DINA | model | since |     |     |     |     |     |     |     |
itmakesthesameassumptionwemadeinourmodelingof
skills:thelearnermusthavemasteredalltherelatedskillsto
succeed in an item. The DINA model assumes that at least Figure2:SkillClassChunkProbabilities
oneoftherelatedskillsneedstobemasteredtosucceedin
anitem.Itwasthusdeemedinappropriateforourstudy.
|     |     |     |     |     |     | Results   | for the      | different | difficulty | levels       | point   | to a grad- |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --------- | ---------- | ------------ | ------- | ---------- |
|     |     |     |     |     |     | uation in | performance. |           | As can     | be expected, | results | show       |
BNInitializationthroughtheCDMModel that the “Familiar” level stands out in both “Successful”
TheCDMallowsustopredictauser’sprobabilityofmaster- and“OnlySuccessful”categories:thislevelisseldomfailed
ingtheoverallcompetence(rootnode)viaitspretestresults. and is usually the only one mastered by learners. On the
Forthis,weusetheaposterioriprobabilitiesobtained.Todo otheropposite,the‘CausalCounterfactual’levelisthelevel
so,fromalearner’svectorofcompetence,weseekthelineof most often failed and exclusively failed (‘Only failed’) by
theaposteriorimatrixcontainingthesameorsimilarvector. learners.Whilethedifferenceinmasterylevelisnotaspro-
Thejointprobabilitymatchingthispattern,calculatedbased nouncedasinthe‘Familiar’case,itisnonethelessnotewor-
on the probabilities associated with each skill, is then used thy, as both establish clear upper and lower boundaries for
15933

learningandperformance.Forinstance,whiletheprobabil- Tetrachoric Correlations. Tetrachoric correlations be-
itythatlearnersexclusivelyfailthe‘Familiar’caseisclose tween skills are shown in Figure 4. Based on our sample
tozero,thesamegoesfortheprobabilitythatlearnersexclu- size,correlationscoresover0.33areconsideredsignificant
sively master the ‘CausalCounterFactual’ level. As for the with α = 0.05 (Guilford and Lyons 1942). Using this cri-
in-between ‘Abstract’ level, results show that it is nonethe- terion for this analysis, one pattern that stands out is that
lessdifficulttomaster,closertothe‘CounterFactual’level. skillswithfamiliarcontentcorrelatehighlywithotherskills
Finally,resultsforthedifferentskills(‘Inhibit’,‘Generate’, of the same content level, but not with counterfactual and
‘Manage’)areinconclusive,asnoclearskillpatterncanbe abstractlevelskills.However,counterfactuallevelskillscor-
foundacrossthedifferentdifficultylevels. relatewellwiththemselvesandabstractlevelskills,andvice
versa.Overall,thesefindingssuggestaclearseparationbe-
ValidationfortheBNandUnderlying tweenthefamiliarlevelofcontentandtheothertwolevels.
PsychologicalModel
| GoodnessofFit. |     | Weoptedfortheitempairwiseχ2 |     |     |     | mea- |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
sure(Chen,delaTorre,andZhang2013)asanabsolutein-
dicatorofgoodnessoffitfortheCDMmodel.Thismeasure
| indicates | that the | model | is inadequate | if the | p-value | of the |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ------------- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
maximalitempairwiseχ2measureisabovethe0.01signifi-
cancelevel(Groß,Robitzsch,andGeorge2016).Theχ2test
resultswereχ2=33.95withp-value=6.79×10−7,whichis
| clearly below | any | significance | threshold | and | thus | indicates |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
thatthepresentmodelisadequate.
Figure4:Skillcorrelations
| Guess, | Slip and | Item | Discrimination | Index | (IDI). | Re- |     |     |     |     |     |     |     |     |
| ------ | -------- | ---- | -------------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sultsforguess,slip,anditemdiscriminationindexparame-
|     |     |     |     |     |     |     | MarginalSkillProbabilities. |     |     |     | Themeanmasterypercent- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
tersareshowninFigure3.First,wenotedahighguessand
ageforeachskillisshowninFigure5.Thehardestskillto
| low IDI | for both | MTT | with familiar | content. | This | can be |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ------------- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
explained by the fact that a biconditional interpretation of masterseemstobe”Inhibitcounterfactual(I-CF)”(44.3%),
the major premise leads to the correct answer to the MTT, which requires learners to inhibit disabling conditions to
|     |     |     |     |     |     |     | counterfactual |     | conditional | statements. |     | This | observation | is  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ----------- | --- | ---- | ----------- | --- |
regardlessofconditionalskills.Itisalsointerestingtonote
consistentwiththefactthattheMPPcounterfactualhasthe
| that all   | items involving |              | few alternatives | have   | a lower | IDI       |              |                |     |        |          |     |       |          |
| ---------- | --------------- | ------------ | ---------------- | ------ | ------- | --------- | ------------ | -------------- | --- | ------ | -------- | --- | ----- | -------- |
|            |                 |              |                  |        |         |           | highest item | discrimination |     | index. | However, |     | these | findings |
| than their | many            | alternatives | counterparts.    | Beyond |         | these re- |              |                |     |        |          |     |       |          |
marks,however,allitemshavegoodIDIvalues.Thisisespe- seem at odds with our initial psychological model. Indeed,
cially true for the MPP counterfactual, which suggests that thelatterconsidersabstractskillstobethehardestandleast
successfully completing this task is the best way to ensure masteredones;consequently,abstractskillsshouldbebetter
indicatorsofmasteryforconditionalreasoningthancounter-
| that conditional |     | reasoning | has been | fully mastered. |     | As dis- |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | -------- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
factualskills,nottheotherwayaround.Withhindsight,one
cussedbelow,thisfindingisconsistentwithresultsobtained
couldarguethatinhibitingexceptionstoaruleknowntobe
formarginalskillprobabilities.
|     |     |     |     |     |     |     | false, such | as ”If | I throw | ketchup | on  | a shirt, | then | the shirt |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | ------- | --- | -------- | ---- | --------- |
willbeclean,”mightproveharderthansimplyinhibitingan
|     |     |     |     |     |     |     | imaginary      | one. | This might | also        | be why | performances |     | with  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ---------- | ----------- | ------ | ------------ | --- | ----- |
|     |     |     |     |     |     |     | counterfactual |      | content    | are similar | to     | or sometimes |     | worse |
thanperformanceswithabstractcontent.Finally,hereasin
|     |     |     |     |     |     |     | the previous | analyses, |     | the much | higher | probability |     | of fa- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | -------- | ------ | ----------- | --- | ------ |
miliarlevelskillsclearlyseparatesthemfromtheothertwo
|     |     |     |     |     |     |     | levels’skills, | asthedifference |     |     | betweenabstractlevel |     |     | skills |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | --- | --- | -------------------- | --- | --- | ------ |
probabilitiesandtheirlower-scoringcounterfactualcounter-
partisnotnearlyaspronounced.
Figure5:Skilldistribution
|     |     |     |     |     |     |     | Summary      | of the     | Results.      |         | In summary, |             | the analysis | of       |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------------- | ------- | ----------- | ----------- | ------------ | -------- |
|     |     |     |     |     |     |     | CDM model    | data       | provided      | two     | significant |             | findings     | regard-  |
|     |     |     |     |     |     |     | ing the      | underlying | developmental |         | theory      | of          | our          | Bayesian |
|     |     |     |     |     |     |     | Network.     | First,     | there is      | a clear | separation  |             | between      | the fa-  |
|     |     |     |     |     |     |     | miliar level | of         | content       | and the | other       | two levels. | Moreover,    |          |
Figure3:Itemparametersestimation
|     |     |     |     |     |     |     | the hardest | skill | is not | an abstract | one, | like | our psycholog- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ----------- | ---- | ---- | -------------- | --- |
15934

ical model assumes, but a counterfactual one, i.e. the “in- model knowledge, observations and transitions impose a
hibitcounterfactual”skill.Thissurprisingresult,evidenced limit on the kinds of exercises that can be modeled. The
bothbyitemdiscriminationindicesandmarginalskillprob- DeepKnowldgeTracing(DKT)hasbeenproposedasanex-
abilities,canbeexplainedbythedifficultyofinhibitingex- cellentalternativetoovercomeBKTlimits.
| ceptions, | which | are in fact, | realistic situations, |     | to a false |     |     |     |     |     |     |     |     |
| --------- | ----- | ------------ | --------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
rule.Consequently,counterfactual-levelskillsmayverywell DeepKnowledgeTracing
provehardertomasterthantheAbstractlevelcounterparts.
Deeplearningisanapproachthathasbeensuccessfullyap-
|     |     |     |     |     |     | plied in | many | domains, | including | images | recognition |     | (He |
| --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | --------- | ------ | ----------- | --- | --- |
TheBayesianKnowledgeTracing et al. 2016), Natural Language Processing (Collobert and
|                    |              |             |              |           |          | Weston      | 2008)      | and more | recently | in education  |      | for model- |     |
| ------------------ | ------------ | ----------- | ------------ | --------- | -------- | ----------- | ---------- | -------- | -------- | ------------- | ---- | ---------- | --- |
| Now that           | the Bayesian | Network     | has been     | created   | and val- |             |            |          |          |               |      |            |     |
|                    |              |             |              |           |          | ing student | knowledge. | Among    |          | the different | deep | learning   |     |
| idated, Logic-Muse |              | can support | the Bayesian | Knowledge |          |             |            |          |          |               |      |            |     |
architecturesthatexist,theonethatfitswellforknowledge
Tracingprocess(BKT)(CorbettandAnderson1994).BKT
usestheBNtocapturestudents’knowledgewhichallowsin- tracingistherecurrentneuralnetwork,especiallytheLSTM
|     |     |     |     |     |     | (Long Short | Term | Memory), | as  | it is able | to capture | the | se- |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | -------- | --- | ---------- | ---------- | --- | --- |
ferringtheprobabilityofmasteringaskillfromaspecificre-
|     |     |     |     |     |     | quential | aspect | of the data, | which | is helpful | for | prediction. |     |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ------------ | ----- | ---------- | --- | ----------- | --- |
sponsepattern(Conati,Gertner,andVanlehn2002).Student
Inthatsense,DeepKnowledgeTracing(DKT)(Piechetal.
performanceistheobservedvariable(itemvariablenodes),
|     |     |     |     |     |     | 2015) uses | an LSTM | to  | predict | student | performance |     | based |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | ------- | ------- | ----------- | --- | ----- |
whichcorrespondstotheanswertoeachitemattachedtothe
item-typenodes(asinFigure1).ArandomvariableQwith on the pattern of their sequential responses. DKT observes
aBernoullidistributionrepresentstheseitemnodes.Q=1, knowledgeatboththeskilllevelandtheproblemlevel,ob-
|         |          |                  |          |            |     | serving | the correctness | of  | each | problem. | At any | time | step, |
| ------- | -------- | ---------------- | -------- | ---------- | --- | ------- | --------------- | --- | ---- | -------- | ------ | ---- | ----- |
| meaning | that the | student answered | the item | correctly, | and |         |                 |     |      |          |        |      |       |
theinputlayeroftheDKTisthestudent’sperformanceona
Q=0,thathis/heranswerisincorrect.
singleproblemoftheskillthatthestudentiscurrentlywork-
| The upper | level | of the bayesian | network | contains | latent |     |     |     |     |     |     |     |     |
| --------- | ----- | --------------- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
skillvariablenodesthatarenotdirectlyobserved.Someof ingon.Inotherwords,theskillandcorrectnessofeachitem
them,atthedeepestlevelinthenetwork,arerelatedtoitem are used to predict the correctness of the next item, given
|     |     |     |     |     |     | that problem | necessary |     | skills (Piech | et  | al. 2015). |     | Rather |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------------- | --- | ---------- | --- | ------ |
variablenodes.Thus,whenthelearnerrespondstoanitem,
|     |     |     |     |     |     | than constructing |     | a separate | model | for | each skill | as  | BKT |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ----- | --- | ---------- | --- | --- |
theprobabilitiesofmasteringthedifferentrelatedskillsare
|     |     |     |     |     |     | does, DKT | models | all skills | jointly | (Khajah, |     | Lindsey, | and |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | ------- | -------- | --- | -------- | --- |
updatedbyBayesianinference.Hence,forthechoiceofthe
next exercise to be presented to the learner, the tutor ques- Mozer 2016; Tato, Nkambou, and Dufresne 2019). It has
tions the network to extract a list of skill nodes still poorly been shown that DKT can robustly predict whether or not
astudentwillsolveaparticularproblemcorrectlygiventhe
mastered.Fromthatlist,thetutorselectsthefollowingrele-
accuracyofhistoricsolutions(Zhangetal.2017).
vantitemstobeproposedtothelearner.
| In fact, | the BKT | is a particular | case of | Hidden | Markov |     |     |     |     |     |     |     |     |
| -------- | ------- | --------------- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ConsideringExpertKnowledgeWhileTrainingthe
| Model where | student | knowledge | is represented | as  | a set of |     |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
DKTModel
| binary variables |     | (the skill is | either mastered | by the | student |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | --------------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Likeothermachinelearningtechniques,theDKTisbiased
ornot).Observationsarealsobinary:astudentgetsaprob-
towardsthedataseenduringthetrainingphase(itisadata-
lemeitherrightorwrong(Yudelson,Koedinger,andGordon
2013).However,thereisacertainprobability(G,theGuess drivenapproach).Therefore,thegeneralizationperformance
parameter)thatthestudentwithoutthenecessaryskillswill ofthemodeldependsonthetrainingdata.IntheEducation
give a correct response. Correspondingly, a student who domain,aprioriexpertknowledgecanbeavailablebutisnot
alwayssufficientlyaccurate(e.g.,TheinitialBayesianNet-
mastersthenecessaryskillsrelatedtoanitemwillgenerally
|                |           |          |          |           |        | work in | Logic-Muse | was | built | by the domain |     | experts | (lo- |
| -------------- | --------- | -------- | -------- | --------- | ------ | ------- | ---------- | --- | ----- | ------------- | --- | ------- | ---- |
| give a correct | response. | However, | there is | a certain | proba- |         |            |     |       |               |     |         |      |
bility (S, the Slip parameter) that the student will give an gicians, reasoning psychologists and computer scientists).
incorrectresponse.ThestandardBKTmodelisthusdefined Nevertheless,eveninaccuratemodelscanprovidehelpfulin-
byfourparameters(dBaker,Corbett,andAleven2008):ini- formation that should be considered (Zappone et al. 2018).
|     |     |     |     |     |     | In general, | employing | a   | fully data-driven |     | approach | to  | train |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----------------- | --- | -------- | --- | ----- |
tialknowledge,learningrate(learningparameters),slipand
|           |          |         |               |           |      | deep neural | networks | requires | the | acquisition |     | of a massive |     |
| --------- | -------- | ------- | ------------- | --------- | ---- | ----------- | -------- | -------- | --- | ----------- | --- | ------------ | --- |
| guess. In | general, | the BKT | applies prior | knowledge | (L0) |             |          |          |     |             |     |              |     |
andtheprobabilityoflearningtheappliedconcept(p(T))to amountofdata,whichmightnotalwaysbepracticalorreal-
measuretheprogressofstudentlearning.Theprocessworks isticduetoeconomicreasonsorthecomplexityofthepro-
wellinLogic-MuseIntelligentTutoringSystem.Ithasalso cess it entails. Thus combining a priori expert knowledge
|                   |     |                 |          |           |      | and data-driven |     | methods | using | the attentional |     | mechanism |     |
| ----------------- | --- | --------------- | -------- | --------- | ---- | --------------- | --- | ------- | ----- | --------------- | --- | --------- | --- |
| been successfully |     | used in various | systems, | including | com- |                 |     |         |       |                 |     |           |     |
constitutesasuitableapproachtothedesignofhybriddeep
| puter programming |     | (Kasurinen | and Nikula | 2009), | reading |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | ---------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
learningarchitecture.
skills(BeckandChang2007),etc.
|     |     |     |     |     |     | In Logic-Muse |     | Tutoring | System, | a priori | knowledge |     | is  |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------- | -------- | --------- | --- | --- |
CombiningtheBNwithaDeepLearning incorporated using attention mechanism in a deep learning
architecture(Tato,Nkambou,andDufresne2019;Tatoand
ModeltoSupportDeepKnowledgeTracing
|     |     |     |     |     |     | Nkambou | 2022). | The proposed |     | architecture | was | improved |     |
| --- | --- | --- | --- | --- | --- | ------- | ------ | ------------ | --- | ------------ | --- | -------- | --- |
Using a BN sometimes implies manually defining apriori to better manage skills that are difficult or easy to master.
probabilitiesandmanuallylabelingstudentinteractionswith ThisisbecausetheinitialDKTfailstogeneralizedwellon
relevant concepts. Also, the binary response data used to thosemarginalskills.
15935

F1score AC FMA DA FFA AC CCF DA CCF AC A DA A Accuracy
DKT 0.74 0.0 0.79 0.0 0.79 0.0 0.73 0.0 0.80 0.0 0.79 0.0 0.74
DKTm 0.70 0.36 0.80 0.47 0.83 0.54 0.76 0.51 0.85 0.48 0.86 0.46 0.80
DKTm+BN 0.70 0.74 0.80 0.47 0.87 0.80 0.82 0.72 0.83 0.58 0.88 0.80 0.82
Table4:TheDKT,theDKTm,andtheDKKm+BNonselectedskills
Skills N Average StandardDev tation1 done by Khajah et al. (Khajah, Lindsey, and Mozer
MPP FFD 294 0,9456 0,16078 2016).OurcodeisalsoavailableonGitHub2 forfurtherre-
MPP FMD 294 0,898 0,23726 search.
MPP CCF 294 0,907 0,2394 TheresultsareshowninTable4.Werepeatedtheexper-
MPP A 294 0,9615 0,16066 iments20times.Thelastcolumnistheoverallaccuracyof
MTT FFD 294 0,8435 0,26646 the model. For each skill, the first column corresponds to
MTT FMD 294 0,7925 0,29985 thevalueofthef1-scoreforpredictingthattheskillwasin-
MTT CCF 294 0,7494 0,33326 correctly answered and the second column to the value of
MTT A 294 0,8401 0,28974 the f1-score for predicting that the skill was correctly an-
AC FMA 294 0,424 0,38072 swered.Thebestratioforeachskillisinbold.Eachtimethe
AC FFA 294 0,3039 0,3652 student answers an exercise, we can predict whether or not
AC CCF 294 0,3345 0,40801 hewillansweranexerciseofeachtypecorrectlyonhisnext
AC A 294 0,2823 0,41038 interaction.Asexpected,theDKTm(originalDKT+gener-
DA FMA 294 0,407 0,37389 alizationonmarginalskills)enhancedwithBNoutperforms
DA FFA 294 0,3027 0,35081 allothermodelsonpredictingskillswithlittledata.
DA CCF 294 0,381 0,40662 Using the attention mechanism to incorporate expert
DA A 294 0,305 0,42077 knowledgeintoNNisnovel.Itcanbeusedinotherdomains,
suchastextclassificationormedicine,whereexpertknowl-
Table5:Distributionofresponsesoverskills:ceiling(Aver- edgeisavailable.Forexample,wecouldthinkofaclassifier
age<0.4)andfloor(Average>0.9)skillsareinbold. using a neural network combined with a rule-based system
playingtheroleofexpertknowledge.
The Dataset We used the same data collected from the
Conclusion
294 participants who participated in the previous study
(Bayesian Model). In our dataset, each line of data repre- Inthispaper,wepresentedthestudentmodelinLogic-Muse
sentseachparticipantwithitssequentialperformanceonthe Intelligent Tutoring System, which helps learners develop
48 reasoning problems. The amount of data is very few to logicalreasoningskills.Abayesianstudentmodelwasfirst
train a deep learning model. However, combined with ex- presented,includingitsvalidationusingacognitivediagno-
pert knowledge, we will see a substantial difference in the sismodeltrainedondatacollectedfrom294learners(each
results. The exercises were encoded using directly observ- studentsolved48reasoningproblems).TheresultingCDM
able skills, meaning that the questions related to the same model was also used for initializing the bayesian network
skillareencodedwiththesameId(1∼16).Theskillswith for a new learner who goes through a pretest (composed
few data are determined by comparing the average of cor- of those 48 items) during its first connection to the sys-
rectanswersobtainedforeachskill.InTable5,weaveraged tem. The bayesian network is the primary support of the
alltheanswersoneachskill.SincetheLSTMonlyaccepts bayesianknowledgetracing(BKT)inLogic-Muse.Wethen
a fixed length of vectors as the input, we used one-hot en- exploredanotherapproachbasedonDeepKnowledgeTrac-
codingtoconvertstudentperformanceintoafixedlengthof ing (DKT). Using the same dataset, we trained a particular
vectors whose all elements are 0 except for a single 1. The LSTM capable of considering domain expert prior knowl-
single1inthevectorindicatestwothings:whichskillisin- edge represented in the bayesian network. The result is a
volvedandiftheskillwasmasteredcorrectly. deep neural network model able to predict the student per-
formance on the next item accurately. We show how the
The Results To assess our proposed solutions, we ran new model (which integrates prior knowledge using an at-
threemodels:theDKT,theDKTwhereweappliedamask tentional mechanism) outperforms classic DKT. More in-
to the loss function (DKTm), and the DKTm with apriori vestigationwillbeconductedonlargedatasets.Inaddition,
knowledge (DKTm+BN). We used 20% of data for testing for the CDM method, we will investigate more data-driven
and 15% for validation. The BN alone gave 65% of global approaches (Xu and Desmarais C. 2018) that could signifi-
accuracy.TheresultisevaluatedusingtheF1-scoreoneach
cantlyimprovetheQ-Matrix.Thiscouldresultinre-training
skill(treatedastwoclasses-correctandincorrectanswers) themodelforbetteraccuracy.
being predicted and the overall accuracy. The models were
evaluatedin20experiments,andthefinalresultswereaver- 1https://github.com/mmkhajah/dkt
aged.OurimplementationoftheDKTm+BNmodelinTen- 2https://github.com/angetato/Deep-Knowledge-Tracing-On-
sorflowusingKerasbackendwasinspiredbytheimplemen- Skills-With-Limited-Data/blob/master/DKT BN.py
15936

References Khajah, M.; Lindsey, R. V.; and Mozer, M. C. 2016.
|     |     |     |     |     |     |     |     | How deep | is knowledge |     | tracing? |     | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | -------- | --- | ----- | -------- |
Beck,J.E.;andChang,K.-m.2007.Identifiability:Afunda-
mentalproblemofstudentmodeling. InInternationalCon- arXiv:1604.02416.
ferenceonUserModeling,137–146.Springer. Markovits, H. 2013. The development of abstract condi-
|           |       |        |         |        |     |                |     | tional reasoning. | In  | The development |     |     | of thinking | and rea- |
| --------- | ----- | ------ | ------- | ------ | --- | -------------- | --- | ----------------- | --- | --------------- | --- | --- | ----------- | -------- |
| Chen, J.; | de la | Torre, | J.; and | Zhang, | Z.  | 2013. Relative |     |                   |     |                 |     |     |             |          |
andabsolutefitevaluationincognitivediagnosismodeling. soning,83–104.PsychologyPress.
|     |     |     |     |     |     |     |     | Markovits, | H.; and | Vachon, | R.  | 1989. | Reasoning | with |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | --- | ----- | --------- | ---- |
JournalofEducationalMeasurement,50(2):123–140.
Collobert, R.; and Weston, J. 2008. A unified architecture contrary-to-factpropositions.JournalofExperimentalChild
Psychology,47(3):398–412.
fornaturallanguageprocessing:Deepneuralnetworkswith
|                    |     |                                     |     |     |     |     |     | Nkambou, | R.; Mizoguchi, |     | R.; and | Bourdeau, | J.  | 2010. Ad- |
| ------------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | --------- | --- | --------- |
| multitasklearning. |     | InProceedingsofthe25thinternational |     |     |     |     |     |          |                |     |         |           |     |           |
conferenceonMachinelearning,160–167.ACM. vancesinintelligenttutoringsystems,volume308. Springer
Science&BusinessMedia.
| Conati, | C.; Gertner, | A.; | and | Vanlehn, | K.  | 2002. | Using |     |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | -------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Bayesian networks to manage uncertainty in student mod- Piech, C.; Bassen, J.; Huang, J.; Ganguli, S.; Sahami, M.;
eling. User modeling and user-adapted interaction, 12(4): Guibas,L.J.;andSohl-Dickstein,J.2015. Deepknowledge
371–417. tracing. InAdvancesinNeuralInformationProcessingSys-
tems,505–513.
| Corbett, | A. T.; | and Anderson, |     | J. R. | 1994. | Knowledge |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------- | --- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tracing:Modelingtheacquisitionofproceduralknowledge. Ravand, H.; and Robitzsch, A. 2015. Cognitive diagnos-
Usermodelinganduser-adaptedinteraction,4(4):253–278. ticmodelingusingR. PracticalAssessment,Research,and
Evaluation,20(1):11.
Cummins,D.D.;Lubart,T.;Alksnis,O.;andRist,R.1991.
Conditionalreasoningandcausation. Memory&cognition, Tato, A.; and Nkambou, R. 2022. Infusing Expert Knowl-
|     |     |     |     |     |     |     |     | edge Into | a Deep Neural | Network |     | Using | Attention | Mecha- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------- | --- | ----- | --------- | ------ |
19(3):274–282.
|          |        |          |        |             |     |          |      | nismforPersonalizedLearningEnvironments. |     |     |     |     |     | Frontiersin |
| -------- | ------ | -------- | ------ | ----------- | --- | -------- | ---- | ---------------------------------------- | --- | --- | --- | --- | --- | ----------- |
| d Baker, | R. S.; | Corbett, | A. T.; | and Aleven, |     | V. 2008. | More |                                          |     |     |     |     |     |             |
ArtificialIntelligence,5(921476):1–19.
accuratestudentmodelingthroughcontextualestimationof
Tato,A.;Nkambou,R.;andDufresne,A.2019.HybridDeep
| slip and | guess probabilities |     | in  | bayesian | knowledge |     | tracing. |                 |     |         |             |     |           |         |
| -------- | ------------------- | --- | --- | -------- | --------- | --- | -------- | --------------- | --- | ------- | ----------- | --- | --------- | ------- |
|          |                     |     |     |          |           |     |          | Neural Networks | to  | Predict | Socio-Moral |     | Reasoning | skills. |
InIntelligentTutoringSystems,406–415.Springer.
InProceedingsofthe12thInternationalConferenceonEd-
DeLaTorre,J.2009.Acognitivediagnosismodelforcogni-
ucationalDataMining,623–626.
| tivelybasedmultiple-choiceoptions. |     |     |     |     | AppliedPsychological |     |     |           |             |     |                  |     |         |           |
| ---------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --------- | ----------- | --- | ---------------- | --- | ------- | --------- |
|                                    |     |     |     |     |                      |     |     | Thompson, | V. A. 1994. |     | Interpretational |     | factors | in condi- |
Measurement,33(3):163–183.
|                                            |             |           |     |     |             |        |       | tionalreasoning.                                | Memory&cognition,22(6):742–758. |     |     |                     |     |     |
| ------------------------------------------ | ----------- | --------- | --- | --- | ----------- | ------ | ----- | ----------------------------------------------- | ------------------------------- | --- | --- | ------------------- | --- | --- |
| De Neys,                                   | W.;         | Schaeken, | W.; | and | D’ydewalle, | G.     | 2002. |                                                 |                                 |     |     |                     |     |     |
|                                            |             |           |     |     |             |        |       | Xu,P.;andDesmaraisC.,M.2018.                    |                                 |     |     | AnEmpiricalResearch |     |     |
| Causal                                     | conditional | reasoning |     | and | semantic    | memory | re-   |                                                 |                                 |     |     |                     |     |     |
|                                            |             |           |     |     |             |        |       | onIdentifiabilityandQ-matrixDesignforDINAmodel. |                                 |     |     |                     |     | In  |
| trieval:Atestofthesemanticmemoryframework. |             |           |     |     |             | Memory |       |                                                 |                                 |     |     |                     |     |     |
&cognition,30(6):908–920. Proceedings of the 11th International Conference on Edu-
cationalDataMining,438–443.IEDMS.
| DeNeys,W.;Schaeken,W.;andD’Ydewalle,G.2003. |     |     |     |     |     |     | In- |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ference suppression and semantic memory retrieval: Every Yudelson,M.V.;Koedinger,K.R.;andGordon,G.J.2013.
Individualizedbayesianknowledgetracingmodels.InInter-
| counterexample |     | counts. | Memory | &   | cognition, | 31(4): | 581– |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ------ | --- | ---------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
nationalConferenceonArtificialIntelligenceinEducation,
595.
171–180.Springer.
George,A.C.;Robitzsch,A.;Kiefer,T.;Groß,J.;andU¨nlu¨,
|     |     |     |     |     |     |     |     | Zappone, | A.; Di Renzo, |     | M.; Debbah, |     | M.; | Lam, T. T.; |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ----------- | --- | --- | ----------- |
A.2016. TheRpackageCDMforcognitivediagnosismod-
|     |     |     |     |     |     |     |     | and Qian, | X. 2018. | Model-aided |     | wireless |     | artificial in- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | --- | -------- | --- | -------------- |
els. JournalofStatisticalSoftware,74(2):1–24.
|     |     |     |     |     |     |     |     | telligence: | Embedding | expert | knowledge |     | in  | deep neural |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | --------- | --- | --- | ----------- |
Gilovich, T.; Griffin, D.; and Kahneman,D. 2002. Heuris- networks towards wireless systems optimization. arXiv
| ticsandbiases:Thepsychologyofintuitivejudgment. |     |     |     |     |     |     | Cam- |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
preprintarXiv:1808.01672.
bridgeuniversitypress.
Zhang,L.;Xiong,X.;Zhao,S.;Botelho,A.;andHeffernan,
Groß,J.;Robitzsch,A.;andGeorge,A.2016. Cognitivedi- N.T.2017. Incorporatingrichfeaturesintodeepknowledge
agnosismodelsforbaselinetestingofeducationalstandards
|     |     |     |     |     |     |     |     | tracing. | InProceedingsoftheFourth(2017)ACMConfer- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------------------------------- | --- | --- | --- | --- | --- |
inmath. JournalofAppliedStatistics,43(1):229–243.
enceonLearning@Scale,169–172.ACM.
| Guilford, | J. P.; and | Lyons, | T.  | C. 1942. | On  | determining | the |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
reliabilityandsignificanceofatetrachoriccoefficientofcor-
relation. Psychometrika,7(4):243–249.
| He, K.;         | Zhang, | X.; Ren,    | S.; and      | Sun,   | J. 2016.       | Deep             | resid- |     |     |     |     |     |     |     |
| --------------- | ------ | ----------- | ------------ | ------ | -------------- | ---------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| ual learning    | for    | image       | recognition. |        | In Proceedings |                  | of the |     |     |     |     |     |     |     |
| IEEE conference |        | on computer |              | vision | and            | pattern recogni- |        |     |     |     |     |     |     |     |
tion,770–778.
| Kasurinen,                                 | J.; and | Nikula, | U.  | 2009. | Estimating | program- |       |     |     |     |     |     |     |     |
| ------------------------------------------ | ------- | ------- | --- | ----- | ---------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| mingknowledgewithBayesianknowledgetracing. |         |         |     |       |            |          | InACM |     |     |     |     |     |     |     |
SIGCSEBulletin,volume41,313–317.ACM.
15937