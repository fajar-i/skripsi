Adapting DAS3H Model for a Personalized Distributed Practice
Schedule to Improve Long-Term Memorization in Designing an
Intelligent Programming Language Tutor
MaryJaneC.Samonte ReneeCharleneB.Evangelista DeniseNicoleB.Marcelo
SchoolofInformationTechnology, SchoolofInformationTechnology, SchoolofInformationTechnology,
MapúaUniversity,Philippines MapúaUniversity,Philippines MapúaUniversity,Philippines
mjcsamonte@yahoo.com rcbevangelista@mymail.mapua.edu.ph dnbmarcelo@mymail.mapua.edu.ph
ABSTRACT ConferenceonDistanceEducationandLearning(ICDEL2024),June14–17,
IntelligentTutoringSystems(ITS)aredigitallearningenvironments 2024,Guangzhou,China.ACM,NewYork,NY,USA,8pages. https://doi.
org/10.1145/3675812.3675854
employingArtificialIntelligence(AI)intheformofknowledgetrac-
ing(KT)tocraftpersonalizedlearningplansforstudents.Learning
thebasicsofprogramminglanguagedirectsthestudentstowrite 1 INTRODUCTION
instructions to perform tasks. With this, educational tools like
Theevolutionoftechnologyoverthedecadeshasledtoagrowing
IntelligentTutoringSystems(ITS)havebeendevelopedtoaidedu-
demandforindividualspossessingtechnicalskills. Educational
catorsandstudents.ThisstudyintroducestheDAS3Hmodeland
institutionsgloballyhaveadaptedtheircurriculatoimpartknowl-
Case-basedReasoningtoassiststudentsinmasteringprogramming
edgeandexpertiseinSTEMsubjects,withaparticularfocuson
languagebyaccuratelyidentifyinglearners’difficultiesandMod-
computerprogramming[1].Sincemasteringthefundamentalsof
elingStudentLearningandForgettingforOptimallyScheduling
programmingispivotal,theIntroductiontoComputerProgram-
DistributedPracticeSkills. Throughrigorousliteratureanalysis,
mingcourseplaysacriticalroleinshapingstudents’abilitiesand
thispaperaimstoproposeanIntelligentProgrammingTutor(IPT)
ensuringtheirsuccessinanever-evolvingtechnologicallandscape
toimprovetheefficiencyofstudyingintroductoryprogramming
[2].Tothisend,educationaltoolslikeIntelligentTutoringSystems
courses.Additionally,thepaperoutlinesseveralknowledge-tracing
(ITS)havebeendevelopedtoaidbotheducatorsandstudents.
algorithmsandmodels,alongwithfeedbacktools.Thecriticalanal-
IntelligentTutoringSystems(ITS)aredigitallearningenviron-
ysisofpreviousstudieshelpedtounderstandtheflexibleapproach
mentsemployingArtificialIntelligence(AI)intheformofknowl-
to learning materials, including spaced repetition, digital flash-
edgetracing(KT)tocraftpersonalizedlearningplansforstudents
cards,anddiversestudymodesthatcatertoindividuallearning
[3][4].Thesesystemsaimtomimichumantutoringindigitalset-
preferences. Additionally,includingCase-BasedReasoning(CBR)
tings,supportingstudentsastheyacquireknowledgeandskillsin
intheexpertmodelimprovesprogrammingskillsandenhances
variousfields,includingcomputerprogramming[5].Inthecontext
problem-solvingabilities.
ofthispaper,wewilluse”IntelligentProgrammingTutors(IPTs)”
CCSCONCEPTS insteadof”IntelligentTutoringSystems(ITSs)”sinceIPTsareITSs
thatarefocusedonprogramming,butessentiallyhasthesamestruc-
•:AppliedComputing→Education;Interactivelearningenvi-
ture[6][7].However,despitetheavailabilityofnumerousmethods
ronments.
andtoolsdesignedtoassistprogrammingstudents,thereremains
asubstantialdropoutrateinintroductoryprogrammingcourses
KEYWORDS
[8]. Consequently,furtherenhancementsinIPTsareessentialto
Intelligent Tutoring Systems, Intelligent Programming Tutor, bolsterthelearningexperience.
DAS3Hmodel,Case-BasedReasoning,ComputerProgramming, IntelligentProgrammingTutors(IPTs)typicallyconsistoffour
KnowledgeTracing primarycomponents:astudentmodel,aknowledgedomainmodel,
anexpertmodel,andauserinterfacemodel[9][10].Theknowledge
ACMReferenceFormat:
MaryJaneC.Samonte,ReneeCharleneB.Evangelista,andDeniseNicole domainmodelencompassesrelevantinformationaboutthesubject
B.Marcelo.2024.AdaptingDAS3HModelforaPersonalizedDistributed beingtaught,whiletheexpertmodelprovidesfeedbackbasedon
PracticeScheduletoImproveLong-TermMemorizationinDesigningan students’responses.Thestudentmodelrepresentsstudents’goals,
IntelligentProgrammingLanguageTutor. In2024the9thInternational needs,andknowledge,adaptinginresponsetothesystem’sintelli-
gence. Theuserinterfacemodelservesasthebridge,facilitating
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
seamlessinteractionbetweenthelearnerandthesystem. While
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation thestudentmodelisacrucialelement,preciselyassessingwhether
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe astudenthasgraspedaconceptremainschallenging,underscoring
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
theimportanceofcreatinganeffectivestudentmodelwithinthe
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. system [9][10][11][12]. Consequently, this paper would like to
ICDEL2024,June14–17,2024,Guangzhou,China proposeanIPTusinganeffectivestudentmodeltoimprovethe
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
efficiencyofthesesystemsinstudyingintroductoryprogramming
ACMISBN979-8-4007-1680-5/24/06
https://doi.org/10.1145/3675812.3675854 courses.
75

ICDEL2024,June14–17,2024,Guangzhou,China MaryJaneSamonteetal.
Table1:SelectionProcess
| Database               | StudiesFound | StudiesFiltered | StudiesChosen |
| ---------------------- | ------------ | --------------- | ------------- |
| GoogleScholar          | 21           | 11              | 5             |
| IEEEXplore             | 12           | 9               | 2             |
| ResearchGate           | 3            | 2               | 1             |
| CornellUniversityarXiv | 5            | 5               | 2             |
| ACM                    | 4            | 4               | 2             |
| WileyOnlineLibrary     | 3            | 1               | 1             |
| ScienceDirect          | 7            | 4               | 1             |
| SpringerLink           | 6            | 4               | 2             |
| Total                  | 61           | 40              | 16            |
This study seeks to answer the questions, “What knowledge Atotalsixty-one(61)studiesweregatheredandfourty(40)studies
tracingmodelwillbestidentifyandpredicttheknowledgelevel fitthecriteriaaccordingtotheirabstractandtitleafterthefiltering
andacademicperformanceofthestudents?” and“Whatfeedback process. Amongthose,onlysixteen(16)waschosenastheywere
provisiontoolwillbestgivepersonalizedfeedbacktostudentsbased themostrelevanttothestudy.Keywordssuchas“IntelligentTutor-
ontheirinteractionswiththesystem?”.Themainaimofthestudyis ingSystem”,“IntelligentTutoringSystemforProgramming”,and
toproposeanIntelligentProgrammingTutor(IPT)forthelearning “Knowledgetracingmodels”weretypedonthesearchbar. Then,
enhancementofprogrammingstudents.Specifically,theobjectives thesearchresultswerefilteredtotheyears2018to2023,asindi-
ofthestudyare:Toreviewexistingliteraturerelatedtointelligent catedinTable2.Studiesthatwereselectedwereplacedinastudies
tutoringsystems(ITS);Toidentifyaknowledgetracingmodelthat listandfilteredaccordingtotheirtitleandabstract,asdisplayedin
handlesmultipleskillsgiveninaprogrammingquestion,and;To Table3.Lastly,thestudieswerechosenaccordingtohowwellthey
identify an effective feedback tool for personalized feedback to cananswertheresearchquestionofthecurrentstudy.
students
Thescopeofthisstudyencompassesanin-depthexaminationof
3 ANALYSIS,RESULTSANDUNDERSTANDING
IntelligentProgrammingTutors(IPTs)andtheirroleinenhancing
Thepurposeofthisliteraturereviewistocomprehendthedesignof
thelearningexperienceofstudents,particularlyinthedomainof
anintelligenttutoringsystem,recognizethealgorithmsemployed
| computerprogramming. ItdelvesintothearchitectureofIPTs, |     |     |     |
| ------------------------------------------------------- | --- | --- | --- |
forknowledgetracing,andthetoolsusedtocreatepersonalized
theuseofknowledgetracingmodelsforpredictingstudentperfor-
mance,andfeedbackprovisionmethods. Thisstudydrawsfroma feedbackforstudentsbasedontheirinputs,interactions,knowl-
selectionofresearchpapersobtainedfromreputableonlinesources edge level, and other attributes. While prior research presents
variousalgorithmsandmodelsforknowledgetracingandfeedback
toprovideacomprehensiveoverviewofthesubject.Thestudyalso
mechanisms,therearesomelimitations.First,thereisascarcityof
focusedonknowledgetracingalgorithmsandmodelsthatinvolve
studiesonstudentmodelscapableofhandlingthemultipleskills
multipleskillssinceprogrammingassessmentsorpracticeinvolve
|     |     | necessaryforprogrammingtasks. | Existingmodelsstrugglewhen |
| --- | --- | ----------------------------- | -------------------------- |
multipleskills.
Thestudydoesnotincludepracticalimplementationsorempiri- studentsneedtoapplyseveralconceptssimultaneously. Second,
caldatafromtheuseoftheproposedsystem.Additionally,whilea theaccuracyofthesemodelsheavilyreliesonstudentdata,which
canbechallenginginsmallersettings. Lastly,whilefuzzylogic
comprehensiveliteraturereviewwasconductedtoselectrelevant
andcase-basedreasoningareusedforfeedback,thereisaneedto
studies,theselectionprocessisbasedonabstractsandtitles,which
explorealternativemethodstoofferabroaderrangeofpersonalized
maynotcaptureallrelevantresearchinthefield. Moreover,the
| proposedsystem’seffectivenessanditsimpactonstudentlearning |                   | studentsupport. |     |
| ---------------------------------------------------------- | ----------------- | --------------- | --- |
| outcomeshavenotbeenempiricallytested.                      | Furtherresearchis |                 |     |
neededtovalidatethepracticalimplicationsoftheproposedsys- 3.1 INTELLIGENTTUTORINGSYSTEM
temanditsimpactonstudents’programmingskillsandknowledge ARCHITECTURE
acquisition. Lastly,thestudyislimitedtoafewresearchpapers
IntelligentTutoringSystems(ITS)arecomputer-basedlearning
duetotimeconstraints.
environmentsthatusesKnowledgeTracing(KT)-algorithmsthat
helpspredictstudentperformance,fordesigningandscheduling
2 METHODOLOGY
personalizedlearningplansforlearners[3].Throughthedifferent
The research papers used for this study were taken from vari- capabilitiesofArtificialIntelligence(AI),thesesystemshavecon-
ous online sources such as Google Scholar, IEEE Xplore (ieeex- tinuouslyevolvedthroughthecombinationofvariousknowledge
plore.ieee.org),ResearchGate,CornellUniversityarXiv(arXiv.org), gatheredfromobservingthetechniquesofhumantutors[13]. The
ACMDigitalLibrary(dl.acm.org),WileyOnlineLibrary,Science mainaimofthesesystemsistoimitatetheroleofhumantutorsin
DirectandSpringerLinkareshowninTable1.Aselectioncriterion thelifeofthestudentsandenhancethelearningjourneyofstudents
wasusedtoidentifyrelevantstudiesthatwillbeusedinthisstudy. byofferingcustomizedlearningexperiences.
76

AdaptingDAS3HModelforaPersonalizedDistributedPracticeScheduletoImproveLong-TermMemorizationin
DesigninganIntelligentProgrammingLanguageTutor ICDEL2024,June14–17,2024,Guangzhou,China
Table2:YearofPublicationoftheChosenStudies
Year NumberofStudies References
2018 7 [5],[6],[7],[13],[14],[18],[19]
2019 3 [16],[17],[20]
2020 2 [9],[10]
2021 3 [3],[11],[15]
2022 1 [12]
Table3:RelatedStudiesonIntelligentTutoringSystemDevelopment
Reference Titleofthestudy FeedbackToolUsed Objective
EryılmazandAdabashi DevelopmentofanIntelligentTutoringSystem FuzzyLogic TodesignandproposeanITS
(2020) UsingBayesianNetworksandFuzzyLogicfora thatcombinesFuzzyLogic
HigherStudentAcademicPerformance andBayesianNetworkto
supportstudentlearning
Karaci(2018) Intelligenttutoringsystemmodelbasedonfuzzy FuzzyLogic ToproposeanITSmodelthat
logicandconstraint-basedstudentmodel. usesFuzzyLogicanda
constraint-basedstudent
modeltoteachTurkish
punctuationuse.
Duttetal.(2021) Anintelligenttutoringsystemarchitecturebasedon FuzzyLogic TodesignanITSusingfuzzy
FuzzyNeuralNetwork(FNN)forspecialeducation tohelpidentifythosewith
oflearningdisabledlearners. learningdisabilities
SharmaandHarikshan Designinganintelligenttutoringsystemfor CBR TodesignanITSforthe
(2022) computerprograminginthePacific enhancementofthelearning
andteachingprocessin
programmingtopicsfor
students.
Schwetaetal.(2018) Agent-baseddistributedintelligenttutoringsystem CBR Toproposeanagent-based
usingcase-basedreasoning. distributedITSusingCBRfor
anenhancedlearning
environment
Salem(2019) AProposedModelforSmartTutoringSystemfor CBR TodiscussanITSmodelthat
BiologicalSciences. usesCBRforbiological
sciences
ITSsplayapivotalroleinhelpingstudentsacquiremasteryin ThearchitectureofanIntelligentTutoringSystems(ITS)inFig-
specificsubjectareas,withapplicationsspanningdiversefields,in- ure 1 shows how each of these components interacts with one
cludinginformationtechnology[5].AstudybyMousavinasabetal. another. Theknowledgedomainordomainmodelcontainsrele-
[6]revealedthat37.73%ofITSimplementationsareconcentratedin vantknowledgeconcerningtheparticularareatheITSisdesigned
therealmofcomputerscience. Giventheconsiderableoverlapbe- toteach.Thismayalsoincludethelecturematerialspreparedfor
tweencomputerscienceandinformationtechnology,ITSsdesigned teachingthetopic,suchasnotes,questions,quizzes,andmore.This
forcomputersciencecanbeeffectivelyleveragedbyinformation modelpresentstheknowledgeofexpertsqualitativelyandmay
technologystudents. Computerprogrammingisacommonarea alsorepresentthemethodstheyusetosolveproblems.Thismodel
ofinterestbetweenthesetwodisciplines,andnumerousITSshave evaluateswhetherthestudents’answersarecorrect[9][12]. In
beendevelopedtofacilitatecomputerprogramminginstruction[7]. somestudies,theexpertorpedagogicalmodelpresentsthedomain
Throughthesesystems,studentscanengageinfocusedpractice model’scontentsinawaythatsatisfiesthestudent’spreference,
andskilldevelopment,ultimatelyequippingthemwithvaluable generating appropriate feedback to the users based on their re-
expertisethatbenefitstheirfuturecareers. sponses. Thisfeedbackmaydeterminewhetherthestudentsare
ThearchitectureofITSsiscomposedof4maincomponents:a correctorincorrect,providingtherightanswersorshowinghints
studentmodel,aknowledgedomainmodel,apedagogicalorexpert [9][11].
model,andauserinterfacemodel[9][10]. Thestudentmodelwithinthesystemservesasavitalcomponent,
encapsulatingeachstudent’sgoals,needs,andknowledge. This
77

ICDEL2024,June14–17,2024,Guangzhou,China MaryJaneSamonteetal.
Figure1:ArchitectureofanITSfromRekhawiandAwni[9]
modelmeticulouslyassessesthecurrentstateofstudents’knowl- FactorizationMachines(FM)-Factorizationmachines(FMs)
edgebyanalyzingtheirresponsesandbehavioralpatterns.Itthen areaversatileregressionorclassificationmodel,andtheycanbe
providesthisknowledgetoothersystemcomponents,influencing seenasaunifyingframeworkthatencompassesvariousestablished
thecustomizationoffeedbackforusers. Continualmonitoringof modelswithintheeducationalliterature.Theycanaccuratelyand
students’knowledgestatesisacorefeatureunderpinnedbythe efficientlyestimatestudents’knowledgeandexceleveninsituations
dynamicadaptationofthemodelthroughtheapplicationofArtifi- where student data is lacking. They are also adept at handling
cialIntelligence(AI).Nonetheless,thechallengeliesinaccurately additional contextual information, such as multiple knowledge
gaugingastudent’sgraspoftheconceptsimpartedbythesystem, componentsandthenumberofattemptsattheitemorskilllevel.
emphasizingthecriticalimportanceofdevelopinganeffectivestu- ThisisutilizedbyVieandKashima[16],andChoffinetal.[17].
dentmodeltoaddresstheinherentuncertaintiesassociatedwith
thestudentmodelingprocessinthesystem[9][10][11][12].
Lastly,theuserinterfacemodelallowsallofthesemodelsto 3.3 KNOWLEDGETRACINGMODELS
beaccessedbytheuser. Throughtheuserinterface,thestudent SinceKTisimplementedusingseveralalgorithmsasmentionedin
canfreelyinteractwiththedifferentfeaturesofthesystem,which theprevioussection,severalmodelshavebeencreatedtoenhance
thenaffectstheinformationstoredinthestudentmodel,affecting theeffectofthealgorithmandtofurtherincreasetheaccuracyof
thedomainmodel,andtheexpertmodel. Theseinterconnected studentperformanceprediction.Thesemodelsareusedinstudent
componentssynergizetoprovideasmoothandcohesivelearning models,andwerecreatedbasedonthesealgorithms,buttheones
experienceforthestudent. enumeratedbelowarethosewhofocusedonthestudents’inter-
actionswithquestionsinvolvingmultipleskillsorconceptssince
programmingquestionsinvolvesmultipleconcepts,especiallyif
3.2 KNOWLEDGETRACINGALGORITHMS
thequestionsinvolvewritingcode[14].DAS3Hmodelcombines
KnowledgeTracing(KT)isimplementedusingArtificialIntelli- thepredictionofstudentperformanceinpracticalquestionsofEKT
gence(AI)algorithmsinIntelligentTutoringSystemstopredictthe andtheuseoffactorizationmachinesusingKTMandwaschosen
performanceofthestudentsbyidentifyingtheircurrentknowledge asthemodelfortheproposedsytem.
states.Severalalgorithmswereusedintheselectedstudies. Exercise-aware Knowledge Tracing (EKT) - proposed by
Bayesian Network - Bayesian network serves as a model- Liu et al. [15] that uses a knowledge state matrix instead of a
ingtoolforrepresentinginterdependenciesamongdifferentcon- RecurrentNeuralNetworkfortrackingthestateofthelearner’s
ceptswithinaspecificdomain,utilizingaprobabilitydistribution. knowledgeinmultipleconceptsbyaddingtotheknowledgetopics
Bayesiannetworkshaveprovenvaluableasaprobabilisticframe- thatwerealreadypresentineachexercisegiventothestudents.
workinaddressingthedynamicmanagementandcontinuousup- Thisallowsthemeasurementofhowmucheachexercisecanaffect
dating of student models. It utilizes nodes to represent certain students’comprehensionofvariousknowledgeconceptswhilethey
topics,andismainlyusedduetoitsabilitytouseprobabilitiesto areexercising.
dealwithuncertainties. ThisalgorithmisusedbyEryılmazand KnowledgeTracingMachines(KTM)-Thiswasintroduced
Adabashi[10]. byVieandKashima[16]asafamilyofmodelsthatincludeses-
NeuralNetwork(NN)-Neuralnetworks,duetotheircapacity tablishedmodelsintheEDMliteratureasspecificinstancesfor
toeffectivelyanalyzeandidentifyrelationshipsamongmultiple addressingknowledgetracingclassificationproblems.Themodel
inputsthroughinterconnectednodes,serveasapowerfulalgorithm allowssideinformationlikemultipleskillstobeincludedinstudent
for addressing complex problems and generating a wide range models.Throughtheuseofvariousdatasets,theresearchreveals
ofoutcomes. Neuralnetworksleveragelearningtechniquesthat thatthesemachinescanaccuratelyestimateuseranditemparam-
reducethecomplexitiesassociatedwithhandlingmultipleinput eters,evenwhendataislimited. Furthermore,theyoutperform
layers, enabling effective decision-making. This algorithm was existingmodels,includingdeepneuralnetworks,inpredictiveac-
utilizedbyDuttetal.[11]inconjunctionwithFuzzylogic. curacy.KTMsserveasaversatileplatformforexperimentingwith
78

AdaptingDAS3HModelforaPersonalizedDistributedPracticeScheduletoImproveLong-TermMemorizationin
DesigninganIntelligentProgrammingLanguageTutor ICDEL2024,June14–17,2024,Guangzhou,China
newdatacombinations,suchasresponsetimesandthenumberof ThisstudyaimstodesignanIntelligentTutoringSystem(ITS)
attemptsattheitemlevel. basedontheDAS3HModelfortheLearningEnhancementofPro-
Difficulty,studentAbility,Skill,andStudentSkillpractice grammingStudents.Specifically,theobjectivesofthestudyareas
History(DAS3H)Model-Choffinetal.[17]introducedalearning follows:
andforgettingstudentmodelthatfactorsinmemorydecayand
• Todevelopauser-friendlyinterfaceforstudentstoaccess
recognizesthebenefitsofpracticewhenquestionsspanmultiple
thecoursematerials.
typesofknowledge.Thismodel,theDAS3H,buildsupontheDASH
• Todevelopquizzesthatwillassessthestudents’learning,
model,consideringmultipleskillsandincorporatingKnowledge
takingintoaccountthetimeittooktoaccomplish,thediffi-
TracingMachines(KTM).DAS3Hisanextensionofadditivefactor
cultyofthetask,andthecorrectnessoftheirresponses.
modelsthatintroducesarepresentationofthetemporalpatterns
• ToapplytheDAS3Hmodelforselectingtheappropriatetask
ofpastskillpractice. Notably,DAS3Henablesdistinctlearning
difficultyforeachstudent
andforgettingcurvesforindividualskills,offeringamorenuanced
• TouseCase-BasedReasoning(CBR)toprovidepersonalized
approach.
feedbackonthestudent’swork
• Toevaluatethesystembycomparingthepretestandposttest
scoresofstudentswhousedthesystemandthosewhoused
3.4 FEEDBACKPROVISIONTOOLS traditionallearning.
FeedbackisanessentialaspectinIntelligentProgrammingTutors Lastly,theDAS3Hmodel,amachinelearningalgorithmgaining
(IPTs)asitgivesinsighttostudentsonwhattopicstheyshould popularityineducationaltechnology,andCased-BasedReasoning
improveonbasedontheirresponsestoquestions.Immediatefeed- (CBR)willbeintegratedintotheapplication. Thismodelutilizes
backandprovidinghintsareprovidedbytheexpertmodeltohelp multiplefactorstopredictstudentperformanceandofferspersonal-
studentsprogressfurtherintheirlearningpath.Hence,thestudy izedrecommendationsbasedontheirlearninghistory. Inarecent
identifiedtwo(2)methodswhichhelpstheexpertmodelprovide studyconductedbyChoffinetal. [17],itwasdemonstratedthat
appropriatefeedback. the DAS3H model significantly amplifies the efficacy of spaced
FuzzyLogic-Fuzzylogicisusedinsolvingtheuncertaintythat repetitionasalearningstrategy,extendingitsutilitybeyondcon-
comeswithane-learningsystemthatadaptstothestudents’needs. ventionalmemorizationtaskstoabroaderrangeofeducational
Thismethodmirrorshumanthinkingbyallowingforgradations contexts,particularlythoseinvolvingtheapplicationofmultiple
betweentraditionalbinaryassessmentssuchasyesorno,bigor skills.SharmaandHarikshan[12]usedCBRasameanstoprovide
small,highorlow,trueorfalse,offeringamoreflexibleandhuman- feedbackandsolutionsinanITS.Usingthesetwotechniqueswill
like decision-making framework. This method is integrated by helpprovidestudentswithtailoredrecommendationsandtestsand
EryılmazandAdabashi[10],Karaci[18],andDuttetal. [11]in personalizedfeedback,optimizingtheirmasteryofprogramming
theirdevelopedITSs. concepts,skills,andterminology.
Case-BasedReasoning(CBR)-Case-BasedReasoning(CBR) The proposed process flow shown in Figure 2 of the current
followsafour-stepprocedure:initialretrievalofrelevantcases,sub- proposedsystembasedonanexistingprocessflowbySharmaand
sequentadaptationofpastcasestoaddressthecurrentsituation, Harkishan[12]. TheIPT’sprimaryfocusisonaidingstudentsin
potentialadjustmentofpriorsolutions, and, ifdeemedsuitable, craftingmoreefficientandeffectivecode,emphasizinghowthe
preservationofthenewcasewithinacasefoundation. Thisap- systemmanagesstudentresponses. Itinitiateswiththestudent
proachallowsthesystemtoutilizebothhistoricalcasesandthe inputtingtheircodesolutiontoagivenproblem,whichthesys-
currentexperiencesofstudentsinthecreationoftailoredsolutions. temsubsequentlyevaluates.Ifthestudent’scodefailstorun,the
Thismethodisusedbythesystemtosolveagivenproblem,and systemoffersfeedbackthroughsuggestionsorhints,allowingthe
canofferpersonalizedinsightsandfeedbackbasedontheretrieved studenttorevisetheiranswer.Uponsuccessfullyparsingthecode,
pastcases.ThismethodwasusedbySharmaandHarikshan[12], thesystemcompilesandexecutesit. Thesystemthencompares
Shwetaetal.[19],andSalem[20]indevelopinganITS. thestudent’ssolutionwithcasesstoredintheCase-BasedReason-
ing(CBR)Libraryandprovidesrelevantfeedback. Iftheproblem
issolved,itupdatesthedomainandstudentmodels,storingin-
puts, performance, andstudentbehavior. Additionally, itsaves
4 PROPOSEDSYSTEM
thenewcaseintheCBRlibraryforfutureuse. Thestudentand
Inthisstudy,theproposedsystemisaweb-basedapplicationde- domainmodelsareupdatedwithinformationcrucialforassessing
signedtoenhancestudents’masteryoffundamentalprogramming thestudent’sknowledgestate,includinginteractions,feedback,and
concepts, skills, and terminology. The application incorporates performance,andthesystemselectsanewproblemadjustedtothe
variousfeaturesandtechniquestooptimizethelearningprocess. student’sappropriatedifficultylevelbasedontheupdatedstudent
Oneofthecoreelementsofthewebapplicationistheintegration model.
ofdigitalflashcardsanddiversestudymodes. Thesystemincorpo- This new process flow underscores the integral role of Case-
ratesknowledgetracing,amethodfortrackingstudents’progress BasedReasoning(CBR)andDAS3Hinthesystem’sfunctioning,
overtime.Bymonitoringtheirperformanceandunderstandingof illustratingtheoverallsystemflowfollowingtheprovisionofsuit-
thesubjectmatter,theapplicationcantailorcontentandquestions able learning materials to the student. The system is expressly
toeachstudent’sindividuallearningpaceandneeds. designedtoenhancestudentlearningthroughiterativepractice,a
79

ICDEL2024,June14–17,2024,Guangzhou,China MaryJaneSamonteetal.
Figure2:ProposedProcessFlow
Figure3:ProposedSystemArchitecture
facetstrengthenedbyDAS3H,whichconsidersmemorydecayand theknowledgelevelofthestudents,whichwillbethebasisofthe
themultipleskillsencompassedineachitem.Studentscanrefine contentthatwillbeshowntothem.
theirprogrammingskillsthroughconsistentpractice,tacklingprob- Theknowledgedomainmodelincludesthelearningmaterials
lemstailoredtotheirproficiencylevel,whichgraduallyescalates that will be shown to the students such as notes, videos, flash-
withtheircommitment.Thesystemmeticulouslytrackstheuser’s cards,andpracticequestionsthatwillbeprovidedbythesystem
progressandprovidesfeedbackontheirimprovement,solidifying accordingtotheComputerProgramming1(CS126-8)syllabusof
theproposedIPTasaninvaluabletoolforaspiringprogrammers MapuaUniveristy. Thiscoursefocusesonusingflowchartsand
atallskilllevels. pseudocodestoformulatelogictosolveproblems. Additionally,
Thesystemarchitecture,showninFigure3oftheproposedIPT, itprovidesanintroductoryoverviewofstructuredprogramming,
whichisbasedontheoriginalarchitectureofanITSexplainedby encompassingtopicssuchasproceduralsyntax,programflowde-
RekhawiandAwni[9]andtheproposedsystemarchitectureof piction,variablesanddatatypes,aswellasprogrammingconstructs
EryılmazandAdabashi[10].Thissystemwillbeabletopersonalize relatedtoselectionanditeration.Whenthesystemtriestoassess
thelearningpathofthestudentsbasedontheinformationgathered thestudent’slevelofknowledgeandidentifyhowwellthestudent
on their interactions, assessments, and more, which ultimately hadcomprehendedacertaintopic,assessmentsandquizzesare
identifiestheirknowledgelevel.Thesystemwillbeabletoupdate displayed.
80

AdaptingDAS3HModelforaPersonalizedDistributedPracticeScheduletoImproveLong-TermMemorizationin
DesigninganIntelligentProgrammingLanguageTutor ICDEL2024,June14–17,2024,Guangzhou,China
Theexpertmodelinvolvesgatheringinformationtogeneratethe thisstudy,todeterminewhichmodelbestsuitstheneedsofpro-
appropriatefeedback,andassuch,Case-BasedReasoning(CBR)will grammingeducation. Giventheconstraintsoftime,therangeof
beutilizedsincethistechniquespecializesinprovidingfeedback researchpapersinvestigatedinthisstudyhasbeenlimited. To
based on previous cases. Meanwhile, the student model stores facilitatecomprehensiveinsights,futureresearchendeavorsshould
thegatheredinformationabouttheuserorlearner[9][12]. This expandtheirscopebyexploringawiderarrayofonlinedatabases
includestheinformationtheyhaveprovidedintheuserprofile,and andincorporatingadditionalstudies.Thisapproachwouldenable
alsotheirinteractionswiththesystemandtheirknowledgelevel. amorethoroughexaminationofdiversepossibilitiesandavenues
ThismodelwillbeutilizingthealgorithmoftheDAS3Hmodel forinvestigation. Lastly,furtherdevelopmentisneededforthis
totrackthechangesofthestudent’sknowledgelevelbasedon studysinceitonlyincludedmodels.
theirpastpractices,memorydecay,andthemultipleskillstagged
ontothetestquestions.Thiswillalsoallowthestudentmodelto
REFERENCES
providethematerialsortestsappropriatetotheidentifiedlevelof
thelearner’sknowledge. [1] RodrigoPessoaMedeiros,GeberLisboaRamalho,andTacianaPontualFalcao.
2019.Asystematicliteraturereviewonteachingandlearningintroductorypro-
gramminginHigherEducation.IEEETransactionsonEducation62,2(2019),
77–90.https://doi.org/10.1109/te.2018.2864133
5 IMPLICATIONANDCONCLUSION [2] JoséFigueiredoandFranciscoJoséGarcía-Peñalvo.2021.IntelligentTutoring
SystemsapproachtoIntroductoryProgrammingCourses.InEighthInterna-
Inconclusion,theproposedIntelligentProgrammingTutor(IPT) tionalConferenceonTechnologicalEcosystemsforEnhancingMulticulturality
representsasignificantadvancementinthefieldofprogramming (TEEM’20).AssociationforComputingMachinery,NewYork,NY,USA,34–39.
https://doi.org/10.1145/3434780.3436614
education. Basedonthechosenstudies,DAS3HandCase-Based
[3] ZefengLai,LeiWang,andQiangLing.2021.Recurrentknowledgetracingma-
Reasoning(CBR)willbeutilizedtoofferapersonalizedandeffective chinebasedontheknowledgestateofstudents.ExpertSystems38,8(2021).
learningexperiencetoprogrammingstudents.Theproposedsystem http://dx.doi.org/10.1111/exsy.12782
[4] TongxiLiu.2022.Knowledgetracing:Abibliometricanalysis.Computersand
addressesthechallengesassociatedwithprogrammingeducation, Education: ArtificialIntelligence3(2022),100090.http://dx.doi.org/10.1016/j.
includinghighdropoutrates,byprovidingtargetedfeedbackandre- caeai.2022.100090
[5] ArthurC.Graesser,XiangenHu,andRobertSottilare.2018.IntelligentTutoring
sourcestostudents.ThroughDAS3H,thesystemaddressesthecrit-
Systems.InFrankFischer,CindyE.Hmelo-Silver,SusanR.Goldman,andPeter
icalissueofmemorydecayandconsidersthenuancesofmultiple Reimann,InternationalHandbookoftheLearningSciences.NewYork,NY:
skills,effectivelypredictingstudentperformanceandknowledge Routledge,269–278.https://doi.org/10.4324/9781315617572
[6] ElhamMousavinasab,NahidZarifsanaiey,ShararehR.NiakanKalhori,Mahnaz
level,makingitavaluabletoolforlearnersatvariousproficiency
Rakhshan,LeilaKeikha,andMarjanGhaziSaeedi.2018.Intelligenttutoring
levels. Thesystem’sflexibleapproachtolearningmaterials,includ- systems: Asystematicreviewofcharacteristics,applications,andevaluation
ingspacedrepetition,digitalflashcards,anddiversestudymodes, methods.InteractiveLearningEnvironments29,1(2018),142–163.https://doi.
org/10.1080/10494820.2018.1558257
caterstoindividuallearningpreferences. [7] TyneCrow,AndrewLuxton-Reilly,andBurkhardWuensche.2018b.Intelligent
Additionally,theinclusionofCase-BasedReasoning(CBR)in tutoringsystemsforProgrammingEducation:ASystematicReview.Proceedings
ofthe20thAustralasianComputingEducationConference(2018),53–63.http:
theexpertmodeladdsanextralayerofsophisticationtothefeed-
//dx.doi.org/10.1145/3160489.3160492
backandguidanceprovidedtostudents,ensuringthattheyreceive [8] ErumMehmood,AdnanAbid,MuhammadShoaibFarooq,andNaeemA.Nawaz.
relevantandtailoredassistance.Thisapproachnotonlyimproves 2020.Curriculum,teachingandlearning,andassessmentsforintroductorypro-
grammingcourse.IEEEAccess8(2020),125961–125981.http://dx.doi.org/10.
programmingskillsbutalsoenhancesproblem-solvingabilities.
1109/access.2020.3008321
TheIPT’sflexiblelearningmaterials,adaptabilitytodifferentlearn- [9] AlRekhawiandHazemAwni.2020.AndroidApplicationsDevelopmentintelli-
ingstyles,andcomprehensiveknowledgedomainmodelalignwith genttutoringSystem.Retrievedfromhttps://www.researchgate.net/publication/
369019340_Android_Applications_Development_Intelligent_Tutoring_System.
theneedsofmodernprogrammingstudents. Thistoolhasthepo- [10] MeltemEryılmazandAfafAdabashi.2020.DevelopmentofanIntelligentTu-
tentialtoreducedropoutratesandequiplearnerswiththeskillsand toringSystemUsingBayesianNetworksandFuzzyLogicforaHigherStu-
dentAcademicPerformance.AppliedSciences10,19(September2020),6638.
knowledgeneededforsuccessinthecontinuouslyevolvingfieldof
https://doi.org/10.3390/app10196638
technology.TheintegrationofadvancedAItechniquesandeduca- [11] SarthikaDutt,NeeluJyothiAhuja,andManojKumar.2021.Anintelligenttutoring
tionalmodelspavesthewayformoreeffectiveandpersonalized systemarchitecturebasedonFuzzyNeuralNetwork(FNN)forspecialeducation
oflearningdisabledlearners.EducationandInformationTechnologies27,2
programmingeducation.
(2021),2613–2633.https://doi.org/10.1007/s10639-021-10713-x
[12] PriynkaSharmaandMayuriHarkishan.2022.Designinganintelligenttutoring
systemforcomputerprograminginthePacific.EducationandInformation
6 LIMITATIONANDFUTURERESEARCH Technologies27,5(2022),6197–6209.https://doi.org/10.1007/s10639-021-10882-9
[13] AliAlkhatlan,andJugalKalita.2018.IntelligentTutoringSystems:ACompre-
Thelimitationsofthisstudyshouldbeconsideredtoguidefuture hensiveHistoricalSurveywithRecentDevelopments.arXiv(CornellUniversity).
Retrievedfrom:https://doi.org/10.48550/arxiv.1812.09628.
researchinthefieldofIntelligentProgrammingTutors(IPTs)and
[14] AndrewLuxton-Reilly,Simon,IbrahimAlbluwi,BrettA.Becker,MichailGi-
educationaltechnology.Firstly,thisstudyprimarilyfocusesonthe annakos,AmruthN.Kumar,LindaOtt,JamesPaterson,MichaelJamesScott,
conceptualdesignofanIPTwithanemphasisonusingtheDAS3H JudySheard,ClaudiaSzabo.2018.Introductoryprogramming: Asystematic
literaturereview.ProceedingsCompanionofthe23rdAnnualACMConfer-
modelandCase-BasedReasoning(CBR)forfeedbackprovision.
enceonInnovationandTechnologyinComputerScienceEducation(2018).
Theeffectivenessandfeasibilityofthisproposedsystemneedtobe https://doi.org/10.1145/3293881.3295779
empiricallyevaluatedthroughextensivetestinganduserstudies [15] QiLiuetal.2021.Ekt:Exercise-awareknowledgetracingforstudentperformance
prediction.IEEETransactionsonKnowledgeandDataEngineering33,1(2021),
tovalidateitsimpactonstudents’learningoutcomes.Intermsof 100–115.https://doi.org/10.1109/TKDE.2019.2924374.
knowledgetracingmodels,whiletheDAS3Hmodelishighlighted, [16] Jill-JennVieandHisashiKashima.2019.KnowledgeTracingMachines:Factoriza-
tionmachinesforKnowledgeTracing.ProceedingsoftheAAAIConferenceon
futureresearchcouldexplorethecomparativeeffectivenessofdif-
ArtificialIntelligence33,01(2019),750–757.https://doi.org/10.1609/aaai.v33i01.
ferentknowledgetracingmodels,includingthosenotcoveredin 3301750
81

ICDEL2024,June14–17,2024,Guangzhou,China MaryJaneSamonteetal.
[17] BenoîtChoffin,FabricePopineau,YolaineBourda,andJill-JênnVie.2019.DAS3H: [19] Shweta,PraveenDhyani,andO.P.Rishi.2018.Agent-baseddistributedintelligent
Modelingstudentlearningandforgettingforoptimallyschedulingdistributed tutoringsystemusingcase-basedreasoning.IntelligentSystems(2018),901–928.
practiceofskills.arXiv.org.Retrievedfromhttps://arxiv.org/abs/1905.06873. https://doi.org/10.4018/978-1-5225-5643-5.ch037
[18] AbdulkadirKaraci.2018.Intelligenttutoringsystemmodelbasedonfuzzylogic [20] DaliaA.M.Salem.2019.AProposedModelforSmartTutoringSystemforBio-
andconstraint-basedstudentmodel.NeuralComputingandApplications31,8 logicalSciences.EgyptianComputerScienceJournal43,2(May2019).Retrieved
(2018),3619–3628.https://doi.org/10.1007/s00521-017-3311-2 Fromhttp://ecsjournal.org/archive/Volume43/Issue2/11.pdf.
82