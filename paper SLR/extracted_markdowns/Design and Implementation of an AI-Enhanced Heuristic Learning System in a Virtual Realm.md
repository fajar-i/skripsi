Design and Implementation of an AI-Enhanced Heuristic
Learning System in a Virtual Realm
XiaozhuWang ShengzhuoLiu PaulAdams
TheOpenUniversityofChina CollegeofComputerScienceand DepartmentofMedia,
China Mathematics,FujianUniversityof CommunicationandJournalism,
wangxzh@ouchn.edu.cn Technology CaliforniaStateUniversity,Fresno
China USA
liu-sz09@fjut.edu.cn drpaul16@gmail.com
Abstract 1 INTRODUCTION
Thispaperexploreshowartificialintelligence(AI)andVirtualRe- Heuristiclearning,derivedfromtheGreekwordheuriskein,mean-
ality (VR) technology can be integrated with heuristic learning ing”todiscover,”isaneducationalapproachthatencourageslearn-
methods in a virtual realm. Heuristic learning emphasizes the ersto activelyengage in problem-solvingand exploration. Un-
promotionofdeeperunderstandingandinternalizationofknowl- liketraditionalrotememorizationtechniques,heuristiclearning
edgethroughdiscovery,problem-solving,andpractice.Thispaper emphasizescriticalthinking, experimentation, andareal-world
outlinesAI-enhancedheuristiclearningstrategies, highlighting application of knowledge. By encouraging learners to actively
howAIintegrationenablescustomizedlearningpaths,immersive seeksolutionsratherthanpassivelyreceiveinformation,heuristic
simulationenvironments,intelligentfeedbackandevaluation,aux- learningfostersdeepercomprehensionandlong-termretentionof
iliaryfunctions, anddata-driveninsights. Thedesignedsystem concepts. Thebenefitsofheuristiclearningaremanifold. Firstly,
structureincludesmodulesfordatacollection,featureengineering, itpromotesadeeperunderstandingofsubjectmatterbyencour-
modeltraininganddeployment,knowledgebasecreation,anduser aginglearnerstoactivelyengagewiththematerialandapplyit
interface. Examples of intelligent learning companions demon- inpracticalcontexts. Secondly,itcultivatescriticalthinkingand
stratethepracticalapplicationofAI-assistedtoolsinproviding problem-solvingskills,essentialcompetenciesinanincreasingly
real-timeheuristicguidanceandpersonalizedsupportinanimation complexanddynamicworld.Finally,heuristiclearningencourages
designcourses. Throughexperimentalcomparativeanalysis,itis agrowthmindset,instillinginlearnerstheconfidencetotackle
concludedthatcombiningheuristicmethodswithAI-supported challengesandlearnfromfailures.
environmentscanenhancethelearningexperienceofstudents,pro- TheintegrationofAIandVRtechnologiesholdsimmensepo-
vidingvaluableinsightsforfuturecoursesintermsofparticipation, tentialforenhancingheuristiclearningexperiences.AIalgorithms
efficiency,customization,andknowledgeinternalization. cananalyzevastamountsoflearnerdatatopersonalizeinstruction,
providingtailoredguidanceandfeedbacktoindividualstudents
CCSConcepts basedontheiruniquelearningstylesandpreferences.VRtechnol-
ogy,ontheotherhand,createsimmersivelearningenvironments
•Appliedcomputing;•Education;•E-learning;
thatsimulatereal-worldscenarios,enablinglearnerstoapplytheo-
reticalknowledgeinpracticalcontexts.BycombiningAI’sadaptive
Keywords
capabilitieswithVR’simmersiveenvironments,educatorscancre-
Heuristiclearning,Artificialintelligence,Adaptivelearning,Con- atehighlypersonalizedandengaginglearningexperiencesthat
versationalagents,Knowledgetracing catertotheindividualneedsandpreferencesofeachlearner.More-
over,AI-poweredvirtualtutorscanprovidereal-timefeedbackand
ACMReferenceFormat: support,facilitatingself-directedlearningandexploration. This
XiaozhuWang,ShengzhuoLiu,andPaulAdams. 2024. DesignandIm- synergybetweenAIandVRtechnologieshasthepotentialtorev-
plementationofanAI-EnhancedHeuristicLearningSysteminaVirtual olutionizeeducation,makinglearningmoreaccessible,engaging,
Realm.In20248thInternationalConferenceonDigitalTechnologyinEduca- andeffectivethaneverbefore.
tion(ICDTE)(ICDTE2024),August07–09,2024,Berlin,Germany.ACM,New
York,NY,USA,9pages.https://doi.org/10.1145/3696230.3696231 2 LITERATUREREVIEW
Inrecentyears,therehasbeenasignificantsurgeofinterestin
leveraging artificial intelligence (AI) and heuristics to facilitate
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
adaptiveandpersonalizedlearningexperienceswithinvirtualenvi-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ronments.Thispaperpresentsacomprehensivesynthesisofkey
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe researchconductedoverthepastfiveyears,focusingonthemost
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
recentadvancementsrelatedtothedesignandimplementationof
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. AI-poweredheuristiclearningsystemsinvirtualrealms.
ICDTE2024,August07–09,2024,Berlin,Germany Thereviewcoversvariousdomainsofresearch,startingwithin-
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
telligenttutoringsystems(ITS),whichrelyonAItodelivertailored
ACMISBN979-8-4007-1757-4/24/08
https://doi.org/10.1145/3696230.3696231 instructionautonomously.Mousavinasabetal.(2021)highlighted
255

ICDTE2024,August07–09,2024,Berlin,Germany XiaozhuWangetal.
theincreasingintegrationofAItechniquesinintelligenttutoring Hantoobietal.(2021)presentedasystematicreviewfocusingon
systemsacrossdisciplinestoprovideadaptivelearning,butadvo- theintegrationofknowledgemanagementinVLEs,emphasizing
catedformoremobile-basedsystemstofurtherenablepersonalized theimportanceofefficientinformationmanagementinenhancing
education[1].IntelligenttutoringsystemsintegratingAI,asdemon- learningexperiences[14].SkalkaandDrlik(2022)proposedanAI-
stratedbyHazemA.Alrakhawietal.(2023),haveincreasinglybeen basededucationalmodelutilizingactivelearningstrategieswithin
utilizedineducation.Thesesystemsofferedadaptiveandperson- VLEs,aimingtoenhancestudentengagementandperformance
alizedlearningexperiencesacrossvariousdisciplines,ultimately [15].Together,thesestudiesunderscorethegrowingimportanceof
resulting in enhanced student outcomes [2]. Erümit and Çetin AIintransformingandoptimizingvirtuallearningenvironments
(2020)proposedadesignframeworkforadaptiveintelligenttutor- foreffectiveknowledgedisseminationandacquisition.
ingsystems,emphasizingtheimportanceoftailoredapproaches Afterconductingathoroughliteraturereview,severalkeyhy-
ineducationtechnology[3]. Additionally,D’MelloandGraesser pothesesandresearchquestionshavebeenidentifiedtoguidethe
(2023)exploredhowintelligenttutoringsystemsachievelearning experimentalstudy. Theseinquiriesaimtoshedlightontheef-
gainscomparabletohumantutors,highlightingtheirtransforma- fectivenessofAI-enhancedheuristiclearningenvironmentsand
tivepotentialinthefieldofeducation[4]. Adaptivee-learning theroleofsmartconversationalagentsinfacilitatingpersonalized
frameworksrepresentedanothersignificantareaofexploration, learningexperiences.Tosynthesizetheseelementsandoutlinethe
withresearchersproposingmodelsthatintegratelearninganalytics approach:
andAItomodifyvirtuallearningbasedonlearnerneeds.Smailiet Hypothesis1:AI-enhancedheuristiclearningenvironmentsim-
al. (2021)exploredtheconceptofsustainablee-learningsystems provestudentengagementandmotivationcomparedtotraditional
throughanadaptivelearningapproach,emphasizingtheimpor- learningmethods.
tanceofadaptabilityinpromotinglong-termviabilityinonline ResearchQuestion1:HowdoestheintegrationofAItechnolo-
education[5].Kaounietal.(2023)presentedadesignforanadap- giesinvirtuallearningenvironmentsaffectstudentengagement
tivee-learningmodeldrivenbyartificialintelligence,aimingto andmotivationlevels?
enhancetheefficacyofonlineteachingmethods[6].Kumaretal. Hypothesis2: Smartconversationalagentsprovidepersonal-
(2020)proposedaheuristicevaluationframeworkforassessingthe izedlearningexperiencesthatcatertoindividualstudentneedsand
qualityofmobilelearningapplications,providingvaluableinsights preferences.
forimprovinguserexperienceinmobilelearningenvironments ResearchQuestion2: Towhatextentdosmartconversational
[7]. Heuristics,commonlyreferredtoas”rulesofthumb,”have agentsadapttothelearningpaceandpreferencesofindividual
augmentedAIguidancequalityinvirtuallearningenvironments. students?
Alvarezetal. (2016)delvedintocybereducation,advocatingfor Hypothesis3:Thetimingandmannerofinterventionbysmart
ablendofpedagogicalandheuristiclearningapproaches. They conversationalagentsinfluencestudentlearningoutcomes.
emphasizedtheimportanceofincorporatingtechnologyintoeduca- ResearchQuestion3:Whatistheoptimaltimingandapproach
tiontoenhancelearningoutcomes[8]. Incontrast,Jinetal. (2021) forsmartconversationalagentstointerveneinthelearningprocess
focusedonprovidingdesignheuristicsspecificallytailoredforar- withoutbeingintrusive?
tificialintelligence(AI)applications.Theirworkaimedtoinspire Thestudyaimstoaddresskeyhypothesesandresearchques-
UXdesignersingeneratinginnovativeAI-poweredideas,thereby tionsregardingtheeffectivenessofAI-enhancedheuristiclearning
improvinguserexperienceinAI-drivensystems[9]. Meanwhile, environments. Specifically,theinvestigationwilldelveintohow
Mozeretal.(2019)exploredtheintegrationofartificialintelligence theseenvironmentsimpactstudentengagement,motivation,and
(AI)inhumaninstruction[10]. TheirresearchunderscoredAI’s personalizedlearningexperiences.Toanswerthesequestions,spe-
potentialtoaugmenttraditionalteachingmethodsandsuggestsits cializedsystemsandexperimentaldesignstailoredtoeachinquiry
roleinoptimizingeducationalprocessesforimprovedlearningeffi- willbeutilized,providingempiricalevidenceontheefficacyofAI
cacy.Conversationalagentsleveragingnaturallanguageprocessing technologiesineducation.
haveemergedasintuitiveAIguidancetoolsinvirtualenvironments.
ThesestudiescollectivelyexploredtheutilizationofArtificialIntelli-
gence(AI)inremotelearningandteaching.Atifetal.(2021)delved
intoAI-enabledremotelearningandteachingthroughPedagogi-
calConversationalAgentsandLearningAnalytics[11].Paschoal
etal. (2020)systematicallyidentifiedpedagogicalconversational
3 ANAI-ENHANCEDHEURISTICLEARNING
agents,layingthegroundworkfortheireffectiveintegrationinto
APPROACH
educationalsettings[12].Meanwhile,Mekni(2021)presentedan
AI-basedvirtualassistantutilizingconversationalagents,aimingto Heuristiclearningmethodologyrepresentsadynamicapproach
enhancelearningexperiencesandsupportremoteeducation[13]. toeducation, emphasizingproblem-solving, discovery, andself-
Together,theseworksunderscorethepotentialofAIinrevolutioniz- directedlearning.Byengaginglearnersinhands-onexperiences
ingonlineeducationthroughinnovativetechnologicalapplications. andencouragingexploration,heuristiclearningfostersdeeperun-
Furthermore,numerousstudieshaveexploredtheapplicationsof derstandingandretentionofknowledge. Inrecentyears,thein-
AIandvirtualenvironmentsinanimatededucationacrossvarious tegrationofartificialintelligence(AI)andvirtualreality(VR)en-
domains.Thesestudiescollectivelyexplorevariousaspectsofin- vironmentshasopenednewpossibilitiesforenhancingheuristic
tegratingtechnologyintovirtuallearningenvironments(VLEs). learningininnovativeways.
256

DesignandImplementationofanAI-EnhancedHeuristicLearningSysteminaVirtualRealm ICDTE2024,August07–09,2024,Berlin,Germany
• EnhancedCollaborationandSocialLearning: AIand
VRenablecollaborativelearninginvirtualenvironments,
promotingteamworkandknowledgesharing.Thesespaces
developessentialcommunicationandcollaborationskillsfor
themodernworkforce.
• Data-Driven Decision-Making for Educators: AI an-
alyticsfromVRenvironmentsofferinsightsintostudent
behaviorsandperformance. Educatorscanpersonalizein-
structionandimplementinterventionsbasedonempirical
evidence,refiningeducationalapproachescontinuously.
• AccessibilityandInclusivity: AIandVRaccommodate
diverselearningneeds,withfeatureslikespeechrecognition
improvingaccessibilityforstudentswithdisabilities. VR
simulationscatertovariouslearningmodalities,ensuring
Figure1:TheIterativeProcessofHeuristicLearning equitableaccesstoeducationalopportunities.
4 ANAI-ENHANCEDHEURISTICLEARNING
3.1 Coreprinciplesofheuristiclearning
SYSTEM
Heuristiclearningoperatesonseveralfoundationalprinciplesand
techniquesdesignedtofosteractiveengagementandcriticalthink- AfterexploringtheAI-enhancedheuristiclearningapproach,it
ingamonglearners. Figure1illustratestheiterativeprocessof becomesevidentthatanAI-enhancedvirtuallearningsystemis
heuristiclearning,characterizedbycyclesofexploration,exper- crucialinmoderneducation. Itutilizesartificialintelligencetech-
imentation, reflection, andrefinement. Thisiterativemodelen- nologytopersonalizelearningexperiences,adaptstoindividual
courageslearnerstoactivelyexploreconceptsthroughhands-on studentneeds,providesreal-timefeedback,andenhancesoverall
activities,promotingdeeperunderstandingandretention. engagement.Thisinnovativeapproachrevolutionizestraditional
Inheuristiclearning,learnersembraceaproblem-solvingmind- learningmethods,makingeducationmoredynamic,efficient,and
set,seekingsolutionsthroughtrialanderrorratherthanpassive accessibletostudentsworldwide.
instruction. This approach cultivates deeper comprehension as
learnersconfrontreal-worldchallengesandapplycriticalthinking
4.1 AnAI-Enhancedheuristiclearningscenario
skillstodeviseinnovativesolutions.Furthermore,heuristiclearn-
ingemphasizesself-directedinquiry,empoweringlearnerstotake AIplaysapivotalroleinaugmentingheuristiclearningexperiences
ownershipoftheireducationaljourneyandpursueareasofinterest byprovidingpersonalizedguidance,facilitatingadaptivelearning
autonomously. pathways,andenhancinginstructionalsupport.Figure2illustrates
anAI-EnhancedHeuristicLearningScenarioandshowshowAI
3.2 SignificanceofintegratingAIandVRin algorithmsanalyzelearnerdatatodeliverpersonalizedrecommen-
dations,adaptivefeedback,andtailoredlearningexperiences.Ad-
educationaldesign
ditionally,AI-drivenconversationalagentsofferintuitiveguidance
TheintegrationofAIandVRtechnologiesholdsprofoundsignif-
andsupport,furnishinglearnerswithpersonalizedexplanations
icanceforeducationaldesign,particularlyinenrichingheuristic
andfeedback.
learningexperiences.AI-poweredadaptivelearningsystemscan
Inthisscenario,weenvisionanAI-enhancedvirtuallearningen-
analyzelearnerbehaviorandpreferencestocustomizeeducational
vironmentdesignedtofacilitatepersonalizedandadaptivelearning
contentandactivities,enhancingtheefficacyofheuristiclearning
experiencesforstudentsacrossdiverseeducationaldomains.The
experiences[16].VRtechnologyallowslearnerstoimmersethem-
scenarioillustrateshowadvancedAItechnologiescanbeintegrated
selvesintailoredenvironments,facilitatingexperientiallearning
intovirtuallearningplatformstooptimizelearningoutcomesand
and skill development. The profound implications and benefits
fosterstudentengagement.
ofcombiningAIandVRtechnologiesineducationalsettingsare
exploredinthepaper. 1. DataAnalyticsandInsights: TheAIsystemleverages
• PersonalizedLearningExperiences:AIandVRintegra- advanceddataanalyticscapabilitiestoderiveactionablein-
tionallowsfortailoredlearningexperiences,adjustingcon- sightsfromlearnerinteractionsandbehaviors. Thesein-
tent,pacing,andinstructionalstrategiesbasedonindividual sightsinforminstructionaldesign,curriculumdevelopment,
student data. This personalized approach fosters greater andpedagogicalstrategies,enablingeducatorstorefineand
engagementandacademicsuccess. optimizethelearningexperienceovertime.
• ImmersiveandInteractiveLearningEnvironments:VR 2. AI-EnhancedAdaptiveLearning:Atthecoreoftheinte-
technologyoffersimmersiveexperiences,simulatingreal- gration,AIalgorithmsanalyzelearnerdata,includingpref-
worldscenariosforactiveengagement. AIintegrationen- erences,behavior,andperformancemetrics.Theseanalyses
hancesinteraction,providingreal-timefeedbackandguid- enablethesystemtodynamicallyadaptthelearningexperi-
ancetoenhancecomprehensionandretention. encetosuitindividuallearnerneedsandpreferences.
257

ICDTE2024,August07–09,2024,Berlin,Germany XiaozhuWangetal.
Figure2:AnAI-EnhancedHeuristicLearningScenario
3. PersonalizedLearningPathways:Throughtheintegra- 4.2 AnAI-EnhancedHeuristicLearningSystem
tionofAI,thevirtuallearningplatformgeneratesperson- Structure
alizedlearningpathwaystailoredtoeachstudent’sgoals,
ThepromiseofAIandVRineducationstemsfromtheirpotential
interests,andacademicstrengths.Thesepathwaysleverage
tocreatehighlyadaptive,experientiallearningenvironments.To
machinelearningalgorithmstorecommendrelevantcourses,
realizethispotential,thesystemstructuremustenabledynamic
resources,andactivitiesalignedwithstudents’educational
personalizationandinteractivity. Atthecore,anAIenginelever-
objectives. Forinstance,astudentinterestedincomputer
ages data on learners’ knowledge, skills, interests and progress
sciencemayreceiverecommendationsforcodingtutorials,
tocontinuallytailorcontentandactivities. Thisenginerelieson
virtuallabs,andonlinecoursesinsoftwaredevelopment.
componentsforcollectinglearnerdata,extractinginsights,and
4. InteractiveConversationalAgents: Integratedconver-
trainingmodelstorefinerecommendationsovertime. Seamless
sationalagentspoweredbyAIengagelearnersininterac-
integrationofthisAI-poweredpersonalizationenginewithimmer-
tivedialogue,offeringpersonalizedexplanations,answering
siveVRenvironmentscanenablelearnerstoactivelyengagewith
queries,andprovidingcontextualizedassistance. Thesecon-
educationalcontentinnewways,supportingcriticalthinkingand
versationalagentsenhancelearnerengagement,promote
improvedoutcomes. Thesystemstructuremusttightlyconnect
deeperunderstanding, andfacilitateseamlessinteraction
theAImoduleswithVRfront-endstodeliverthisnext-generation
withinthelearningenvironment.
learningexperience,asshowninFigure3.
5. AdaptiveAssessmentandFeedback: AIalgorithmsen-
TheAI-enhancedvirtuallearningsystemcomprisesessential
ableadaptiveassessmenttoolsthatdynamicallyadjustthe
modules,eachfacilitatingefficientlearningexperiences. TheData
difficultyandformatofquizzes,tests,andassignmentsbased
AcquisitionModulegathersdatafromvarioussources,whilethe
onstudents’skilllevelsandperformance.Additionally,AI-
DataPreprocessingModuleensuresitscleanlinessandtransforma-
drivenfeedbackmechanismsprovidetimelyandpersonal-
tion. TheFeatureEngineeringModuleextractsrelevantfeatures
izedfeedbacktostudents,highlightingstrengths,addressing
andscalesthemappropriately. TheModelTrainingModuleopti-
misconceptions,andsuggestingstrategiesforimprovement.
mizesAImodels,andtheModelDeploymentModuleseamlessly
Thisfeedbacklooppromotesmetacognitiveawarenessand
deploysthemintotheproductionenvironment. TheKnowledge
self-regulatedlearningamongstudents.
Basestoresexpertinsightsandmodeltrainingrecordsforongo-
ingimprovement.TheUserInterfaceenablesintuitiveinteraction
andsmoothnavigation.Thesystemoperatesthroughwell-defined
steps:dataacquisitionfromdiversesources,meticulouspreprocess-
ing,featureengineeringformodelperformance,rigorousmodel
training,anddeploymentforpersonalizedlearningexperiences.
Overall,ThroughtheintegrationofAI,educatorscancreatedy-
Continuousupdatestotheknowledgebaseensureaccuracy,while
namicandresponsivelearningenvironmentsthatempowerlearn-
theuserinterfacefacilitatesseamlessinteractionandfeedbacksub-
erstoachievetheirfullpotentialandacquiredeep, meaningful
mission. Throughthesesteps,thesystemempowerseducatorsand
knowledgeandskills. Moreover,AI-poweredanalyticstoolstrack
learnersindynamicvirtuallearningexperiences.
learnerprogress,pinpointareasofstrengthandweakness,andoffer
targetedinterventionstobolsterlearningoutcomes.
258

DesignandImplementationofanAI-EnhancedHeuristicLearningSysteminaVirtualRealm ICDTE2024,August07–09,2024,Berlin,Germany
Figure3:AI-enhancedheuristiclearningsystemstructure
5 SMARTLEARNINGPARTNER ByleveragingadvancedAIalgorithms,theSmartLearningPart-
neranalyzesstudentinteractionsandperformance,offeringtailored
5.1 OverviewoftheSmartLearningPartner
guidanceandsupporttofacilitatethelearningprocess.Actingas
TheSmartLearningPartner[17]representsaninnovativeappli-
avirtualmentor,itaimstoenhancestudentcomprehensionand
cationofAI-enhancedheuristiclearningsystemsinvirtualenvi-
masteryofvariousconceptsthroughpersonalizedassistanceand
ronments,servingasanintelligentagentwithinvirtuallearning
feedback.
environments. TheSmartLearningPartnerfunctionsasanintel-
CorefunctionsoftheSmartLearningPartnerinclude:
ligentagentembeddedwithinvirtualenvironments,taskedwith
assistingstudentsinheuristiclearning. Hereisanexampleofhow
theSmartLearningPartnercouldfacilitateheuristiclearninginthe 1. Providereal-timeevaluationandheuristicsuggestions:
AnimationCharacterDesigncourse. Sarahislearningaboutwalk OneoftheprimaryfunctionsoftheSmartLearningPartner
cyclesinheranimationdesignclass. Assheattemptstoanimate istoofferreal-timeevaluationandheuristicsuggestionsto
abasicwalkcycle,shestruggleswithmakingthemovementlook students.Bycontinuouslymonitoringstudentprogressand
natural. TheSmartLearningPartnerdetectsSarah’sfrustration interactions,itidentifiesareasofimprovementandprovides
andsays:“Inoticeyouseemstuckonmakingthiswalkcyclelook timelyfeedbackbasedonheuristicprinciples.Thisfacilitates
natural.Thinkbacktothebounceandtimingprincipleswelearned adaptivelearningstrategiesandhelpsstudentsrefinetheir
earlier–howcouldapplyingthosehelpmakethemovementless problem-solvingskills.
rigid?”ThispromptsSarahtoreflectonherpriorlearning. She 2. Supportpersonalizedlearning:Oneoftheprimaryfunc-
realizessheneedstoaddmoreup-and-downmovementtomimic tionsoftheSmartLearningPartneristoofferreal-timeevalu-
thebounceofsteps. Shealsovariesthetimingofstepstolook ationandheuristicsuggestionstostudents.Bycontinuously
lessrobotic. TheSmartLearningPartnerprovidesanaffirming monitoringstudentprogressandinteractions,itidentifies
response: “Nicerefinementonthewalkcycle–thebounceand areasofimprovementandprovidestimelyfeedbackbased
timingadjustmentshelpedmakeitlookmuchmorenatural. Re- on heuristic principles. This facilitates adaptive learning
memberyoucanalwaysreferencethosecoreanimationprinciples strategiesandhelpsstudentsrefinetheirproblem-solving
ifyougetstuck.”BydirectingSarah’sattentionandpromptingher skills.
toapplypriorknowledge,theSmartLearningPartnerfacilitates 3. Stimulatelearninginterestandcreativity:Beyondaca-
heuristiclearningtohelpherovercomechallengesintheanimation demicassistance,theSmartLearningPartnerseekstostim-
process,asshowninFigure4. ulatestudentinterestandcreativity. Byincorporatinginter-
activelearningactivities,challengingtasks,andstimulating
259

ICDTE2024,August07–09,2024,Berlin,Germany XiaozhuWangetal.
Figure4:TheSmartLearningPartner
Table1:Keypointsofsupportindifferentsections
Section ProvidedbytheSmartLearning Points
Partner
AttheBeginningoftheCourse Guidance (cid:4)Structuralfeaturesofcharacters:proportionalrelationships
betweendifferentbodyparts
(cid:4)Commoncharacteractions:standing,walking,running,
jumping,etc.
(cid:4)Characteristicexpressionsofcharacters:happiness,anger,
sadness,joy,surprise,fear,etc.
WhenStudentsSubmitTheirWork EvaluationCriteria (cid:4)Overallstructureofthemodel:completenessandlogical
inProgress coherence
(cid:4)Gestures,expressions,andactions:alignmentwithintended
emotionalexpressionandnarrativecontext
PersonalizedLearningGuidance Guidance,Assessmentand (cid:4)Forstudentswithweakerfoundations:detailedexplanations
Encouragement andexamples
(cid:4)Forstudentswithstrongerproficiency:challengingtasksto
enhanceskillsandcreativity
content,itfostersadynamiclearningenvironmentthaten- integratedintothevirtualenvironment,studentsreceivepersonal-
couragescuriosity,exploration,andinnovation. Through izedassistancetailoredtothespecificrequirementsofthecourse.
engaginglearningexperiences,itaimstoinspirestudentsto Attheoutsetofthedesignprocess,theSmartLearningPartnerpro-
activelyparticipateintheireducationaljourneyanddevelop videsessentialguidelinesbasedonthecoursecurriculumandthe
apassionforlearning. giventask,ensuringthatstudentsgraspthefoundationalconcepts
andobjectives. Asstudents’progressthroughtheactivity,they
havetheopportunitytosubmittheirwork-in-progresstotheSmart
LearningPartnerforreal-timeevaluationandfeedback.Leveraging
5.2 ApplicationCase: AnimationCharacter
thefunctionalityofthesystem,theSmartLearningPartnerassesses
DesignCourse thesubmitteddesigns,offeringheuristicsuggestionsandinsights
5.2.1 LearningScenario. InthelearningscenariooftheAnimation aimedatguidingstudentstowardsfurtherrefinementandcreativ-
CharacterDesigncourse,tailoredforbeginners,studentsengage ityintheircreations. Throughthisiterativeprocessofcreation,
inthecreationofactionfigureswithinavirtualenvironment. The evaluation,andguidance,studentsareempoweredtoenhancetheir
primaryobjectivesofthiscoursearetwofold: toequipstudents skillsandproduceactionfiguredesignsthatexhibitbothtechnical
withacomprehensiveunderstandingofthefundamentalprinciples proficiencyandartisticexpression.
andtechniquesinvolvedinactionfiguredesignandtonurturetheir
abilitytoconceiveimaginativeandexpressivecharacterdesigns.
Throughoutthecourse,studentsimmersethemselvesintheintri- 5.2.2 SupportProvidedbytheSmartLearningPartner. Byoffering
caciesofactionfigurecreation,exploringvariousaspectssuchas structuredguidanceandpersonalizedsupportinthecourse,the
structuralcomposition,gestures,expressions,andmovements.Un- SmartLearningPartnerenhancesthelearningjourney,enabling
dertheguidanceoftheSmartLearningPartner,anintelligentagent studentstodeveloptheircreativityandproficiencyinanimation
260

DesignandImplementationofanAI-EnhancedHeuristicLearningSysteminaVirtualRealm ICDTE2024,August07–09,2024,Berlin,Germany
Table2:Comparativeresultanalysis
| EvaluationCriteria |     | ExperimentalGroup     |     | ControlGroup    |     |     |     |
| ------------------ | --- | --------------------- | --- | --------------- | --- | --- | --- |
| Structure          |     | Reasonableandcomplete |     | Average         |     |     |     |
| Gestures           |     | Logical               |     | Notsmoothenough |     |     |     |
| Expressions        |     | Vividandexpressive    |     | Lacksexpression |     |     |     |
| Actions            |     | Smoothandnatural      |     | Notlivelyenough |     |     |     |
| Creativity         |     | High                  |     | Average         |     |     |     |
| Completeness       |     | High                  |     | Average         |     |     |     |
| OverallPerformance |     | Outstanding           |     | Ordinary        |     |     |     |
characterdesign.Table1showsthekeypointsofsupportindiffer-
entsections.
1.AttheBeginningoftheCourse
AttheoutsetoftheAnimationCharacterDesigncourse,the
SmartLearningPartnerprovidesessentialguidancetostudents,
| covering various | aspects of | character design. | This guidance is |     |     |     |     |
| ---------------- | ---------- | ----------------- | ---------------- | --- | --- | --- | --- |
structuredandcomprehensive,addressingkeyelementssuchas
structuralfeatures,gestures,expressions,andactions.Forinstance,
inactivitieslike”DrawingaCow,”theSmartLearningPartneroffers
| specificguidancetailoredtomeetthetask’srequirements. |     |     | This |     |     |     |     |
| ---------------------------------------------------- | --- | --- | ---- | --- | --- | --- | --- |
guidanceincludesdetailsontheproportionalrelationshipbetween
differentbodyparts,commonactionsassociatedwithcharacters,
andcharacteristicexpressionstypicallyexhibitedbythem.
| 2.WhenStudentsSubmitTheirWorkinProgress |     |     |     |     | Figure5:Assignment |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- |
Asstudents’progressthroughthecourseandsubmittheirwork
forevaluation,theSmartLearningPartneroffersreal-timefeedback
|     |     |     |     | studentswhodidnotusetheSmartLearningPartner. |     |     | Theeval- |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | -------- |
andconstructivesuggestionsforimprovement.Theevaluationcri-
|                     |                                       |     |     | uationmainlyincludedtwoaspects:         |     | assessmentofthecreative |     |
| ------------------- | ------------------------------------- | --- | --- | --------------------------------------- | --- | ----------------------- | --- |
| teriaaremeticulous, | coveringmultipledimensionsofcharacter |     |     |                                         |     |                         |     |
|                     |                                       |     |     | processandassessmentoftheoveralleffect. |     | Intheassessment         |     |
design. Thisincludesassessingtheoverallstructureofthemodel
ofthecreativeprocess,theteacherfocusedontheperformance
| forcompletenessandlogicalcoherence. |     | Additionally,theSmart |     |     |     |     |     |
| ----------------------------------- | --- | --------------------- | --- | --- | --- | --- | --- |
instructure,gestures,expressions,andactions.Atthesametime,
LearningPartnerevaluatesthegestures,expressions,andactions
theteacheralsoconductedacomprehensiveevaluationofthecre-
depictedinthedesign,ensuringtheyalignwiththeintendedemo- ativity, completeness, and overall performance of the students’
tionalexpressionandnarrativecontext.
works. Uponevaluatingtheperformanceacrossvariouscriteria,it
3.PersonalizedLearningGuidance
becameapparentthattheexperimentalgroup,whichutilizedthe
| Recognizing | the varied | learning requirements | and skill sets |     |     |     |     |
| ----------- | ---------- | --------------------- | -------------- | --- | --- | --- | --- |
AI-enhancedlearningapproach,demonstratedsignificantlysupe-
amongstudents,theSmartLearningPartnerisadeptatdelivering
rioroutcomescomparedtothecontrolgroup,asshowninTable
customizedguidancethatalignswitheachlearner’suniqueprofile.
2.
| Byofferingdetailedexplanationsandexamples, |     |     | itassiststhose |     |     |     |     |
| ------------------------------------------ | --- | --- | -------------- | --- | --- | --- | --- |
WiththecomparisonresultssummarizedinTable2,theanalysis
withfoundationalgapsincharacterdesigntograspconceptseffec-
proceededtoamoredetailedinterpretationofthesefindings.
tively.Conversely,itchallengesstudentswithadvancedproficiency
|     |     |     |     | 1. Structure: | The experimental | group’s structures | were |
| --- | --- | --- | --- | ------------- | ---------------- | ------------------ | ---- |
throughengagingtasks,fosteringcontinuousskilldevelopmentand
nurturingcreativity.Throughsuchpersonalizedsupport,theSmart deemedreasonableandcomplete,suggestingaclearunder-
standingoffoundationalconceptsandeffectiveapplication
LearningPartneroptimizesthelearningjourneyforallstudents,
oflearnedprinciples.Incontrast,thecontrolgroup’sstruc-
ensuringcomprehensiveskillenhancementandgrowth.
tureswereratedasaverage,indicatingpotentialchallenges
intranslatingconceptualknowledgeintopracticalapplica-
| 5.2.3 ExperimentandAnalysis. |     | Intheexperiment,studentswere |     | tion. |     |     |     |
| ---------------------------- | --- | ---------------------------- | --- | ----- | --- | --- | --- |
givenanassignment:tocreateajoyfulrunningcowimagebasedon 2. Gestures:Membersoftheexperimentalgroupeffectively
theprovidedstaticimage(a),whileusingimage(b)asthestandard conveyedlogicalgestures,reflectinganuancedunderstand-
referenceanswer,asdepictedinFigure5. Inthistask,students ingofgesturedynamics. Incontrast,thecontrolgroup’s
receivedassistanceandguidancefromtheSmartLearningPartner. gestureswerecritiquedforlackingsmoothness,potentially
Theteacherevaluatedthecreativeprocessandoveralleffectofthe indicatingdifficultiesintranslatingconceptualideasinto
| twogroupsofstudents. |     |     |     | physicalrepresentation. |     |     |     |
| -------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
Theexperimentalgroupconsistedof52studentsusingtheSmart 3. Expressions:Theexperimentalgroupexhibitedvividand
LearningPartner,whilethecontrolgroupcomprisedanother110 expressivefacialexpressions,enhancingtheoverallnarrative
261

ICDTE2024,August07–09,2024,Berlin,Germany XiaozhuWangetal.
andengagement. Conversely,thecontrolgroup’sexpres- 6.2 ContrastswithTraditionalMethods
sionswerenotedtobedeficientinexpression,potentially Comparedtotraditionalmethods,AI-enhancedlearningprovides
limitingtheimpactoftheirworkontheviewer. personalizedpathwaysanddynamiccontent,surpassingthelim-
4. Actions: Theexperimentalgroup’sactionsweredeemed itationsofstaticmaterialsanddelayedassessments. Traditional
smoothandnatural,indicatingahighlevelofproficiency methodsoftenfollowaone-size-fits-allapproachandrelyonstatic
inanimationtechniques. Incontrast,thecontrolgroup’s instructionalmaterials,lackingtheinteractiveandadaptivefea-
actionswereperceivedasnotlivelyenough,suggestingpos- turesofAI-enhancedlearning. Additionally,AI-poweredassess-
siblechallengesinanimatinglifelikemovements. menttoolsofferreal-timefeedback,addressingmisconceptionsor
5. Creativity: Membersoftheexperimentalgroupdemon- gapsinunderstandingimmediately.
stratedhigherlevelsofcreativity,incorporatinginnovative
elementsandoriginalideasintotheirwork.Thiswillingness 6.3 FutureEducationalPractices
toexploreunconventionalapproachessuggestsacapacity
TheintegrationofAIineducationwillcontinuetoevolve,offering
fordivergentthinkingandcreativeproblem-solving.
increasinglypersonalizedexperiencesandbreakingdownbarriers
6. Completeness: Theexperimentalgroup’screationswere
toaccess. Collaborationandknowledgesharingamongstudents
characterizedbythoroughnessandattentiontodetail,re-
willbeenhanced,promotingsocialinteractionandengagementin
sultingincomprehensiveandwell-developedfinalproducts.
virtualenvironments.AI-enabledplatformshavethepotentialto
Conversely,thecontrolgroup’screationsappearedlesspol-
democratizeeducationbyprovidingequalaccesstohigh-quality
ishedandrefined,potentiallyindicatinggapsinplanning
resourcesforlearnersworldwide. AsAItechnologiesadvance,ed-
andexecution.
ucatorsmustadapttheirpracticestoleveragethesetransformative
7. Overall Performance: Collectively, the experimental
technologieseffectivelyforthebenefitofalllearners.
group’sworksurpassedexpectations,showcasingablendof
technicalproficiency,creativeflair,andattentiontodetail.
7 CONCLUSIONS
Incontrast,thecontrolgroup’sperformancewasassessed
Thispaperexplorestheintegrationofartificialintelligence(AI)and
asordinary,highlightingthedisparitiesbetweenthetwo
VirtualReality(VR)technologywithheuristiclearningmethods
groups.
ineducation. Heuristiclearningfocusesondeepunderstanding
Thedisparitiesunderscoretheefficacyoftheexperimentalin- throughdiscovery,problem-solving,andpractice.AItechnology
tervention,indicatingthattheapplicationoftheSmartLearning enhancesthisprocessbyofferingcustomizedlearningpaths,im-
Partnerhasapositiveimpactonstudents’creativeprocessand mersivesimulations,intelligentfeedback,anddata-driveninsights.
overalleffect. ThisfurtherdemonstratesthattheSmartLearning Acomprehensivesystemisdesigned,includingmodulesfordata
Partner,asaneffectivelearningtool,canbepromotedforusein collection,modeltraining,anduserinterface,supportingeducators
othereducationalsettings. TheAI-enhancedlearningapproach inunderstandingstudents’needsandprogress.TheSmartLearning
not only facilitates skill development but also fosters creativity PartnerinAnimationCharacterDesigncoursedemonstratesthe
andexpression,offeringstudentsamoreenrichingandimmersive practicaleffectivenessofAI-enhancedtoolsinprovidingreal-time
learningexperience. guidanceandpersonalizedsupport. Experimentalresultsconfirm
thepositiveimpactofintelligentlearningcompanionsonstudent
outcomes,supportingthebroaderapplicationofAIineducation.In
6 PEDAGOGICALIMPLICATIONS conclusion,thisresearchprovidesvaluableinsightsforinnovation
Withthecontinuousdevelopmentandapplicationofartificialintel- ineducation. WiththeincreasingacceptanceofAItechnology,
ligence(AI)technology,thefieldofeducationhasundergonearev- theadoptionofAI-basededucationaltoolsisexpectedtosurge,
olutionarytransformation. AI-enhancedlearningscenariosalign enrichingstudentlearningexperiencesandadvancingeducation.
withthepedagogicalgoalsofonlineeducationanddemonstrate
Acknowledgments
numerousadvantagescomparedtotraditionallearningmethods.
ThisresearchwasfundedbytheBeijingMunicipalEducationCom-
mission(GrantNo:SM202110011005). WearegratefultotheKey
6.1 AlignmentofAI-EnhancedLearningwith
LaboratoryofDigitalMediaArtinBeijingforgenerouslyprovid-
OnlinePedagogy
inguswiththenecessaryexperimentalfacilities.Additionally,we
TheintegrationofAIintolearningscenariosofferspersonalized wouldliketoexpressoursincereappreciationtothe”Innovative
experiencestailoredtoindividualstudentneeds,aligningclosely TeamofAnimationArtDesign”foritsinvaluabletechnicalsupport.
withpedagogicalobjectivesinonlineeducation.Real-timeanaly-
sisofstudentdataallowsAIsystemstoadaptcontent,pace,and References
feedback, fostering greater engagement and motivation among [1] ElhamMousavinasab,NahidZarifsanaiey,ShararehR.NiakanKalhori,Mahnaz
learners. Additionally,AIpromotesactiveengagementanddeep Rakhshan,LeilaKeikha,andMarjanGhaziSaeedi.Intelligenttutoringsystems:
asystematicreviewofcharacteristics,applications,andevaluationmethods.
understandingthroughinteractiveandimmersivelearningenvi- InteractiveLearningEnvironments,29(1):142–163,2021.
ronments,enhancingcriticalthinkingandproblem-solvingskills. [2] HazemAAlrakhawi,NurullizamJamiat,andSamySAbu-Naser.Intelligent
tutoringsystemsineducation: Asystematicreviewofusage,tools,effects
Moreover,AIintegrationpromotesinclusivityandaccessibilityby
andevaluation.JournalofTheoreticalandAppliedInformationTechnology,
accommodatingdiverselearningstylesandabilities. 101(4):1205–1226,2023.
262

DesignandImplementationofanAI-EnhancedHeuristicLearningSysteminaVirtualRealm ICDTE2024,August07–09,2024,Berlin,Germany
[3] AliKürşatErümitandİsmailÇetin.Designframeworkofadaptiveintelligent [11] AmaraAtif,MeenaJha,DeborahRichards,andAyseABilgin.Artificialintelli-
tutoringsystems.EducationandInformationTechnologies,25(5):4477–4500, gence(ai)-enabledremotelearningandteachingusingpedagogicalconversational
2020. agentsandlearninganalytics.InIntelligentsystemsandlearningdataanalytics
[4] SidneyKD’MelloandArtGraesser.Intelligenttutoringsystems:Howcomputers inonlineeducation,pages3–29.Elsevier,2021.
achievelearninggainsthatrivalhumantutors.InHandbookofEducational [12] LeoNatanPaschoal,AlianeLoureiroKrassmann,FelipeBeckerNunes,Myke
Psychology,pages603–629.Routledge,2023. MoraisdeOliveira,MagdaBercht,EllenFrancineBarbosa,andSimonedoRocio
[5] ElMiloudSmaili,SoukainaSraidi,SalmaAzzouzi,andMyElHassanCharaf. SengerdeSouza.Asystematicidentificationofpedagogicalconversationalagents.
Towardssustainablee-learningsystemsusinganadaptivelearningapproach. In2020IEEEFrontiersinEducationConference(FIE),pages1–9.IEEE,2020.
InEmergingTrendsinICTforSustainableDevelopment:TheProceedingsof [13] MehdiMekni.Anartificialintelligencebasedvirtualassistantusingconversa-
NICE2020InternationalConference,pages365–372.Springer,2021. tionalagents.JournalofSoftwareEngineeringandApplications,14(9):455–473,
[6] MounaKaouni,FatimaLakrami,andOuidadLabouidya.Thedesignofanadaptive 2021.
e-learningmodelbasedonartificialintelligenceforenhancingonlineteaching. [14] SendeyahHantoobi,AhlamWahdan,SaidASalloum,andKhaledShaalan.Integra-
InternationalJournalofEmergingTechnologiesinLearning(Online),18(6):202, tionofknowledgemanagementinavirtuallearningenvironment:Asystematic
2023. review.Recentadvancesintechnologyacceptancemodelsandtheories,pages
[7] BimalAkleshKumar,MunilShivaGoundar,andSaileshSarasChand.Aframe- 247–272,2021.
workforheuristicevaluationofmobilelearningapplications.Educationand [15] JanSkalkaandMartinDrlik.Proposalofartificialintelligenceeducationalmodel
InformationTechnologies,25:3189–3204,2020. usingactivelearninginavirtuallearningenvironment.E-learningintheTrans-
[8] IsabelBorgesAlvarez,NunoSAlvesSilva,andLuisaSampaioCorreia.Cyber formationofEducationinDigitalSociety,14:15–25,2022.
education:towardsapedagogicalandheuristiclearning.AcmSigcasComputers [16] MarianusDabingaya.AnalyzingtheeffectivenessofAI-poweredadaptivelearn-
andSociety,45(3):185–192,2016. ingplatformsinmathematicseducation.InterdisciplinaryJournalPapierHuman
[9] XiaonengJin,MarkEvans,HuaDong,andAnqiYao.Designheuristicsfor Review,3(1):1–7,2022.
artificialintelligence:inspirationaldesignstimuliforsupportinguxdesignersin [17] HaiderThSalimAlrikabi,NabaaAliJasim,BanHassanMajeed,AhmedZkear
generatingai-poweredideas.InExtendedAbstractsofthe2021CHIConference Abass,andIbtihalRazaqNiamaALRubee.Smartlearningbasedonmoodlee-
onHumanFactorsinComputingSystems,pages1–8,2021. learningplatformanddigitalskillsforuniversitystudents.InternationalJournal
[10] MichaelCMozer,MelodyWiseheart,andTimothyPNovikoff.Artificialintelli- ofRecentContributionsfromEngineering,Science&IT(iJES),10(01):109–120,
gencetosupporthumaninstruction.ProceedingsoftheNationalAcademyof 2022.
Sciences,116(10):3953–3955,2019.
263