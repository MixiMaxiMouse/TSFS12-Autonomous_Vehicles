# TSFS12: Autonomous Vehicles – Planning, Control, and Learning Systems

This repository includes lecture notes, material for hand-in exercises, links to reading material, and other course material. Information here will be added during the course, and you can always get the latest version of course material here. 

Note: 
* (2024) by the lecture indicates that the material is from the 2024 edition and may be updated during the course. Removal of (2024) indicates that the material is for the 2024 edition.
* The videos are from the 2020 edition of the course, produced during Corona, but will be available during the course. The content of the videos is for the most part the same as the live lectures, but there have been updates to the lectures. For some lectures, significant updates.

## Table of contents 
1. [Additional lectures and tutorials](#additional)
1. [Introduction videos for hand-ins](#handinintro)
1. Lectures
    1. [Lecture 1](#lecture01) - Introduction
    1. [Lecture 2](#lecture02) - Discrete motion planning
    1. [Lecture 3](#lecture03) - Modelling of ground vehicles
    1. [Lecture 4](#lecture04) - Motion planning with differential constraints
    1. [Lecture 5](#lecture05) - Dynamic optimization as a tool for motion planning and control
    1. [Lecture 6](#lecture06) - Control of autonomous vehicles: Ground vehicles
    1. [Lecture 7](#lecture07) - Model predictive control for autonomous vehicles
    1. [Lecture 8](#lecture08) - Collaborative control
    1. [Lecture 9](#lecture09) - Control of autonomous vehicles + introduction to learning
    1. [Lecture 10](#lecture10) - Learning for autonomous vehicles
    1. [Lecture 11](#lecture11) - Guest lecture
2. [Guest lectures](#industrial_guest_lecture)
3. [Research highlights](#research_guest_lecture)

# Additional lectures and tutorials
1. _Introduction to (some) computer tools for Python in TSFS12_ ([slides](Lecture_notes/computer_tools_introduction.pdf))
    * [Introduction & Working in Visual Studio Code - the basics](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/ComputerIntro/computer_intro_basics.mp4) [23:56]
    * [Working in VSCode - some next steps](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/ComputerIntro/computer_intro_next_steps.mp4) [17:17]
    * [Setting up Python on your computer](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/ComputerIntro/computer_intro_setting_up_python.mp4) [10:13]
    * [Setting up Visual Studio Code for Python](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/ComputerIntro/computer_intro_setting_up_vscode.mp4) [07:35]
    * [Install all packages needed for TSFS12](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/ComputerIntro/computer_intro_install_all_tsfs12.mp4) [04:21]
2. [_Introduction to the CARLA simulator_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/CARLA,%20introduction-20201003_070555.mp4) [40:44]

<a name="handinintro"></a>

# Hand-ins
<a name="additional"></a>

## Report Templates

It is encouraged, but not mandatory, to use the [report templates](https://gitlab.liu.se/vehsys/tsfs12/-/tree/master/Report_templates) that are provided for [LaTeX](https://tug.org) and [Typst](https://typst.app). 

## Instruction videos
Note that the hand-in instructions may have changed since recording. It is always the latest instructions that are valid.

* **Hand in 1**: [Discrete Planning in a Structured Road Network](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/HandIn/HI1-intro-20220828_124216.mp4) [18:09]
* **Hand in 2**: [Planning for Vehicles with Differential Motion Constraints](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/HandIn/HI2-intro-20220908_083838.mp4) [32:29]
* **Hand in 3**: [Vehicle Motion Control](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/HandIn/HI3-intro-20220915_053507.mp4) [26:30]
* **Hand in 4**: [Collaborative Control](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/HandIn/HI4-intro-20241001.mp4.mp4?csf=1&web=1&e=NpwiTx) [8:12]
* **Hand in 5**: [Learning](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/HandIn/HI5-intro.mp4?csf=1&web=1&e=2pPdfw) [40:37]

# Lectures
<a name="lecture01"></a>

## Lecture 1: Introduction [[slides](Lecture_notes/lecture_01_introduction.pdf)]

### Video (from corona editions)
1. [_Introduction to autonomous systems_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%201/Lecture%201a_%20Introduction-20200904_083247.mp4) [12:21]
2. [_Autonomous systems - a broader context_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%201/Lecture%201b_%20Autonomous%20systems%20-%20a%20broader%20context-20200904_083251.mp4) [16:03]
3. [_Enabling technologies_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%201/Lecture%201c_%20Enabling%20technologies-20200904_083248.mp4) [11:17]
4. [_Autonomous vehicles and summary_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%201/Lecture%201d_%20Autonomous%20vehicles%20and%20summary-20200904_083249.mp4) [18:34]

### Reading material
Recommended reading material for the introductory lecture are
* "[_National Highway and Traffic Safety Administration ODI on Tesla_](https://static.nhtsa.gov/odi/inv/2016/INCLA-PE16007-7876.PDF)". Interesting text but some parts have met critique, see, e.g., [_NHTSA's Flawed Autopilot Safety Study Unmasked_](https://www.thedrive.com/tech/26455/nhtsas-flawed-autopilot-safety-study-unmasked) (Note: Opinion piece written by automotive industry analyst).
* Recommends an interesting discussion on [_The Artificial Intelligence podcast_](https://lexfridman.com/ai/) with Sertac Karaman https://lexfridman.com/sertac-karaman/ on autonomous driving and flying. Sertac Karaman is also the author of course literature for lecture 4.
* G. Zardini, et al. "[_Analysis and control of autonomous mobility-on-demand systems_](https://doi.org/10.1146/annurev-control-042920-012811)". Annual Review of Control, Robotics, and Autonomous Systems, 5, 633-658, 2022.
* "[_Reflections on the Learning to Control Renaissance_](https://youtu.be/J_s-0kT0Cpg)", Plenary Lecture IFAC World Congress, 2020, Benjamin Recht, UC Berkeley. (YouTube)
* Gerdes, J. C., & Thornton, S. M. (2016). "[_Implementable ethics for autonomous vehicles_](https://link.springer.com/chapter/10.1007/978-3-662-45854-9_5)". In "[_Autonomous driving: Technical, legal and social aspects_](https://link.springer.com/book/10.1007/978-3-662-48847-8)" (pp. 87-102), Springer Berlin Heidelberg.

Some other related for the interested reader
* SAE, "[_Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles_](https://login.e.bibl.liu.se/login?url=https://saemobilus.sae.org/content/J3016_201806/)", Standard J3016.
* Michon, John A. "[_A critical view of driver behavior models: what do we know, what should we do?_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.473.3166&rep=rep1&type=pdf)." Human behavior and traffic safety. Springer, Boston, MA, 1985. 485-524.
* Introduction to SLAM, Part E Chapter 46.1 in Siciliano, B., and Oussama K., eds. “[_Springer handbook of robotics_](https://research.ebsco.com/linkprocessor/plink?id=c3f4173c-09f6-3d7b-b762-d16f6994ffad)”. 
* A short description of Lidar state-of-the-art (2023). 
M. R. Watts et al., "[_Lidar on a Chip Enters the Fast Lane: Sensors for Self-Driving Cars and Robots will be Tiny, Reliable, and Affordable_](https://doi.org/10.1109/MSPEC.2023.10234174)", IEEE Spectrum, vol. 60, no. 9, pp. 38-43, September 2023. (note: written by representatives of a Lidar development company)
* A. Pernestål et al. "[_Effects of driverless vehicles-Comparing simulations to get a broader picture_](https://d1rkab7tlqy5f1.cloudfront.net/TBM/Over%20faculteit/Afdelingen/Engineering%20Systems%20and%20Services/EJTIR/Back%20issues/19.1/362018%20Pernestal.pdf)" European Journal of Transport & Infrastructure Research 19.1 (2019).

<a name="lecture02"></a>

## Lecture 2: Discrete motion planning [[slides](Lecture_notes/lecture_02_discrete_motion_planning.pdf)]

### Video (from corona editions)

1. [_Introduction to graph search_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%202/Lecture%202a_%20Introduction%20to%20graph%20search-20200904_085642.mp4) [16:32]
2. [_Dijkstra's algorithm_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%202/Lecture%202b_%20Dijkstra%27s%20algorithm-20200904_085640.mp4) [14:04]
3. [_A* algorithm_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%202/Lecture%202c_%20A_%20algorithm-20200904_085638.mp4) [17:35]
4. [_Anytime planning and conclusions_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%202/Lecture%202d_%20Anytime%20planning%20and%20conclusions-20200904_085643.mp4) [08:59]

### Reading material
Main text is Chapter 2 (mainly sections 2.1-2.3) in "[_Planning Algorithms_](http://planning.cs.uiuc.edu)", S. Lavalle. 

For the interested reader, suggested material to dig deeper is
* Likhachev et al. "[_ARA*: Anytime A* with provable bounds on sub-optimality_](http://papers.nips.cc/paper/2382-ara-anytime-a-with-provable-bounds-on-sub-optimality.pdf)", Advances in neural information processing systems. 2004.
* Introductory section in Bertsekas, D.  "[_Reinforcement learning and optimal control_](https://web.mit.edu/dimitrib/www/RLbook.html)", 2019, Athena, is used in the exercise for higher grade in hand-in 1. A PDF with the introductory text can be found on the authors book-page at
https://www.mit.edu/~dimitrib/RLCOURSECOMPLETE.pdf
* Chen, Mo, et al. "[_Priority queues and Dijkstra's algorithm_](https://www.researchgate.net/profile/Vijaya_Ramachandran/publication/250152101_Priority_Queues_and_Dijkstra's_Algorithm/links/54170a0a0cf2218008bec462.pdf)". Computer Science Department, University of Texas at Austin, 2007. 

<a name="lecture03"></a>

## Lecture 3: Modelling of ground vehicles [[slides (2024)](Lecture_notes/lecture_03_ground_vehicles.pdf)]

### Video (from corona editions)
1. [_Mathematical modelling_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%203/Lecture%203a_%20Mathematical%20modelling-20200905_031151.mp4) [6:33]
2. [_Modelling of ground vehicles, part I_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%203/Lecture%203b_%20Vehicle%20models%20I-20200906_014155.mp4) [12:16]
3. [_Modelling of ground vehicles, part II_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%203/Lecture%203c_%20Vehicle%20Models%20II-20200907_065229.mp4) [14:08]

### Reading material
* Sections 13.1 and 15.3-15-4 in LaValle, S. M.: [_Planning Algorithms_](http://planning.cs.uiuc.edu). Cambridge University Press, 2006.
* Part B in “[_Springer handbook of robotics_](https://research.ebsco.com/linkprocessor/plink?id=c3f4173c-09f6-3d7b-b762-d16f6994ffad)”
* Dubins, L. E., "[_On curves of minimal length with a constraint on average curvature, and with prescribed initial and terminal positions and tangents_](https://doi.org/10.2307/2372560)", American Journal of Mathematics, 79(3), 497-516, 1957. 


<a name="lecture04"></a>

## Lecture 4: Motion planning with differential constraints [[slides (2024)](Lecture_notes/lecture_04_motion_planning_with_diff_constraints.pdf)] 

### Video (from corona editions)

1. [_Lecture 4a: Introduction to motion planning with differential constraints_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%204/Lecture%204a_%20%20Introduction%20to%20motion%20planning%20with%20differential%20constraints-20200907_124321.mp4) [19:18]
2. [_Lecture 4b: Motion planning using RRTs_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%204/Lecture%204b_%20Motion%20planning%20using%20RRTs-20200907_124752.mp4) [24:55]
3. [_Lecture 4c: Motion planning using motion primitives and state lattices_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%204/Lecture%204c_%20Motion%20planning%20using%20motion%20primitives%20and%20state%20lattices-20200907_125202.mp4) [20:50]
4. [_Lecture 4d: Path-constrained trajectory planning_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%204/Lecture%204d_%20Path-constrained%20trajectory%20planning-20200907_125610.mp4) [15:10]

### Reading material
* Sections 5.1-5.5 and 14.1-14.4 in LaValle, S. M: [_Planning Algorithms_](http://planning.cs.uiuc.edu). Cambridge University Press, 2006.
* Sections 3.3.3 and 5 in Karaman, S., & E. Frazzoli: ”[_Sampling-based algorithms for optimal motion planning_](https://login.e.bibl.liu.se/login?url=https://doi.org/10.1177%2F0278364911406761)". The International Journal of Robotics Research, 30(7), 846-894, 2011.
* Section 4.5 in Bergman, K: ”[_Exploiting Direct Optimal Control for Motion Planning in Unstructured Environments_](https://doi.org/10.3384/diss.diva-174175)”, Ph.D Thesis No. 2133, Div. Automatic Control, Linköping Univ., 2021.

Additional material for further reading:
* Likhachev, M., & D. Ferguson: ”[_Planning long dynamically feasible maneuvers for autonomous vehicles_](https://login.e.bibl.liu.se/login?url=https://doi.org/10.1177%2F0278364909340445)". The International Journal of Robotics Research, 28(8), 933-945, 2009.
* Dahl, O.: ”[_Path Constrained Robot Control_](https://lucris.lub.lu.se/ws/files/4364453/8566341.pdf)”, Ph.D. Thesis, Dept. Automatic Control, Lund Univ., 1992.
* Ljungqvist, O.: ”[_Motion planning and feedback control techniques with applications to long tractor-trailer vehicles_](https://doi.org/10.3384/diss.diva-165246)”, Ph.D. Thesis, Div. Automatic Control, Linköping Univ., 2020.
* Dubins, L. E., "[_On curves of minimal length with a constraint on average curvature, and with prescribed initial and terminal positions and tangents_](https://doi.org/10.2307/2372560)", American Journal of Mathematics, 79(3), 497-516, 1957. 

<a name="lecture05"></a>

## Lecture 5: Dynamic optimization as a tool for motion planning and control [[slides](Lecture_notes/lecture_05_dynamic_optimization_motion_planning_control.pdf)]

### Code for optimizing a trajectory
* During the lecture, [CasADi](https://web.casadi.org) was used for obtaining a trajectory, a motion primitive, using dynamic optimization. See here for code in [python](Lecture_notes/trajectory_casadi.py), [matlab](Lecture_notes/trajectory_casadi.m), and [C++](Lecture_notes/mprims_intro.zip).

### Video (from corona editions)

1. [_Lecture 5a: Introduction to dynamic optimization for motion planning and control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%205/Lecture%205a_%20Introduction%20to%20dynamic%20optimization%20for%20motion%20planning%20and%20control-20200910_073001.mp4) [23:44]
2. [_Lecture 5b: Challenges and solution strategies for dynamic optimization_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%205/Lecture%205b_%20Challenges%20and%20solution%20strategies%20for%20dynamic%20optimization-20200910_073651.mp4) [22:22]
3. [_Lecture 5c: Solution of the resulting non-linear program_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%205/Lecture%205c_%20Solution%20of%20the%20resulting%20non-linear%20program-20200910_074117.mp4) [22:23]
4. [_Lecture 5d: Case study on dynamic optimization for motion primitives_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%205/Lecture%205d_%20Case%20study%20on%20dynamic%20optimization%20for%20motion%20primitives-20200910_074507.mp4) [14:57]

### Reading material
* Limebeer, D. J., & A. V. Rao: ”[_Faster, higher, and greener: Vehicular optimal control_](https://login.e.bibl.liu.se/login?url=https://doi.org/10.1109/MCS.2014.2384951)”. IEEE Control Systems Magazine, 35(2), 36-56, 2015.

For a more mathematical treatment of the topic of numerical optimal control and further reading on the methods presented in this lecture:
* Chapter 8 in Rawlings, J. B., D. Q. Mayne, & M. Diehl: [_Model Predictive Control: Theory, Computation, and Design_](https://sites.engineering.ucsb.edu/~jbraw/mpc/). Nob Hill Publishing, 2017
* Diehl, M.: [_Numerical Optimal Control_](https://www.fs.isy.liu.se/Edu/Courses/NumericalOptimalControl/Diehl_NumOptiCon.pdf), Optec, K.U. Leuven, Belgium, 2011.

Additional material for further reading:
* Bergman, K: ”[_Exploiting Direct Optimal Control for Motion Planning in Unstructured Environments_](https://doi.org/10.3384/diss.diva-174175)”, Ph.D Thesis No. 2133, Div. Automatic Control, Linköping Univ., 2021.
* Berntorp, K., Olofsson, B., Lundahl, K., & Nielsen, L., "[_Models and methodology for optimal trajectory generation in safety-critical road-vehicle manoeuvres_](https://doi.org/10.1080/00423114.2014.939094)". Vehicle System Dynamics, 52(10), 1304-1332, 2014.
* Fors, V., "[_Autonomous Vehicle Maneuvering at the Limit of Friction_](https://doi.org/10.3384/diss.diva-170606)", Ph.D. Thesis No. 2102, Division of Vehicular Systems, Linköping University, 2020.
* Nocedal, J., & S. Wright: [_Numerical Optimization_](https://link.springer.com/book/10.1007%2F978-0-387-40065-5). Springer, 2006.

<a name="lecture06"></a>

## Lecture 6: Control of autonomous vehicles I: Ground vehicles [[slides (2024)](Lecture_notes/lecture_06_ground_vehicle_motion_control.pdf)]

### Video (from corona editions)

1. [_Introduction to paths and trajectories_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%206/Lecture%206a_%20Introduction%20to%20paths%20and%20trajectories-20200904_092303.mp4) [19:35]
2. [_Pure pursuit path controller_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%206/Lecture%206b%20(update)_%20Pure%20pursuit%20path%20controller-20210117_023635.mp4) [08:47]
3. [_State-feedback path controller_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%206/Lecture%206c_%20State-feedback%20path%20controller-20200904_092259.mp4) [16:32]
4. [_Tuning, non-linear control, and summary_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%206/Lecture%206d_%20Tuning,%20non-linear%20control,%20and%20summary-20200904_092257.mp4) [09:21]
5. [_Derivation of Frenet equations_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%206/Lecture%206e_%20Derivation%20of%20Frenet%20equations-20200904_092302.mp4) [13:23]

### Reading material
Main texts are
* Paden, Brian, et al. "[_A survey of motion planning and control techniques for self-driving urban vehicles_](https://doi.org/10.1109/TIV.2016.2578706)". IEEE Transactions on intelligent vehicles 1.1 (2016): 33-55.

    A good but slightly advanced text and therefore many details are included in the lecture notes.

* Coulter, R. Craig. "[_Implementation of the Pure Pursuit Path Tracking Algorithm_](https://apps.dtic.mil/dtic/tr/fulltext/u2/a255524.pdf)" (1992). 


    But don’t look at figure 1, it is badly scaled which makes it difficult to understand; use figures in the lecture slides instead

For the interested reader, suggested material to dig deeper is
* Siciliano, B., and Oussama K., eds. “[_Springer handbook of robotics_](https://research.ebsco.com/linkprocessor/plink?id=c3f4173c-09f6-3d7b-b762-d16f6994ffad)”. Springer, 2016. Part E, Chapters 49 (wheeled robots), 51 (underwater), and 52 (aerial) 

* Werling, M., Gröll, L., and Bretthauer, G.. "[_Invariant trajectory tracking with a full-size autonomous road vehicle_](https://doi.org/10.1109/TRO.2010.2052325)". IEEE Transactions on Robotics 26.4 (2010): 758-765. 
    An advanced text, nonlinear trajectory stabilizing controllers.

<a name="lecture07"></a>

## Lecture 7: Model predictive control for autonomous vehicles [[slides (2024)](Lecture_notes/lecture_07_model_predictive_control_for_autonomous_vehicles.pdf)]

### Video (from corona editions)

1. [_Lecture 7a: Introduction to model predictive control for autonomous vehicles_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%207/Lecture%207a_%20Introduction%20to%20model%20predictive%20control%20for%20autonomous%20vehicles-20200915_082357.mp4) [12:26]
2. [_Lecture 7b: Fundamentals of model predictive control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%207/Lecture%207b_%20Fundamentals%20of%20model%20predictive%20control-20200915_082540.mp4) [20:34]
3. [_Lecture 7c: Autonomous trajectory tracking and path following using MPC_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%207/Lecture%207c_%20Autonomous%20trajectory%20tracking%20and%20path%20following%20using%20MPC-20200915_082716.mp4) [26:24]
4. [_Lecture 7d: Summary, outlook, and tools for MPC in autonomous vehicles_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%207/Lecture%207d_%20Summary,%20outlook,%20and%20tools%20for%20MPC%20in%20autonomous%20vehicles-20200915_082920.mp4) [09:48]
5. [_Closed Loop RRT_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%209/Lecture%209a_%20Closed%20Loop%20RRT-20201006_025559.mp4) [15:14]

### Reading material
* Chapter 1 in Rawlings, J. B., D. Q. Mayne, & M. Diehl: [_Model Predictive Control: Theory, Computation, and Design_](https://sites.engineering.ucsb.edu/~jbraw/mpc/). Nob Hill Publishing, 2017
* Section V-C in Paden, B., et al.: "[_A survey of motion planning and control techniques for self-driving urban vehicles_](https://doi.org/10.1109/TIV.2016.2578706)". IEEE Transactions on Intelligent Vehicles, 1(1), 33-55, 2016.
* Kuwata, Y., Teo, J., Fiore, G., Karaman, S., Frazzoli, E., & How, J. P.: "[_Real-Time Motion Planning With Applications to Autonomous Urban Driving_](https://doi.org/10.1109/TCST.2008.2012116)". IEEE Transactions on Control Systems Technology, 17(5), 1105-1118, 2009.


Additional material for further reading:
* Berntorp, K., Quirynen, R., Uno, T., & Di Cairano, S: "[_Trajectory tracking for autonomous vehicles on varying road surfaces by friction-adaptive nonlinear model predictive control_](https://doi.org/10.1080/00423114.2019.1697456)". Vehicle System Dynamics, 58(5), 705-725, 2020.
* Diehl, M., Bock, H. G., & Schlöder, J. P: ”[_A real-time iteration scheme for nonlinear optimization in optimal feedback control_](https://doi.org/10.1137/S0363012902400713)”. SIAM Journal on Control and Optimization, 43(5), 1714-1736, 2005.
* Faulwasser, T., & Findeisen, R: ”[_Nonlinear model predictive control for constrained output path following_](https://doi.org/10.1109/TAC.2015.2466911)”. IEEE Transactions on Automatic Control, 61(4), 1026-1039, 2015.
* Gros, S., Zanon, M., Quirynen, R., Bemporad, A., & Diehl, M: ”[_From linear to nonlinear MPC: Bridging the gap via the real-time iteration_](https://doi.org/10.1080/00207179.2016.1222553)”. International Journal of Control, 93(1), 62-80, 2020.
* Hellström, Åslund, J., & Nielsen, L: ”[_Design of an efficient algorithm for fuel-optimal look-ahead control_](https://doi.org/10.1016/j.conengprac.2009.12.008)”. Control Engineering Practice, Vol. 18, nr 11, s. 1318-1327.


<a name="lecture08"></a>

## Lecture 8: Collaborative control [[slides (2024)](Lecture_notes/lecture_08_collaborative_control.pdf)]

### Video (from corona editions)

1. [_Introduction to Collaborative Control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%208/Lecture%208a_%20Introduction%20to%20Collaborative%20Control-20200921_042803.mp4) [10:45]
2. [_Position Based Collaborative Control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%208/Lecture%208b_%20Position-Based%20Formation%20Control-20200921_041348.mp4) [04:08]
3. [_Displacement Based Collaborative Control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%208/Lecture%208c_%20Displacement-Based%20Formation%20Control-20200921_042614.mp4) [07:26]
4. [_Distance Based Collaborative Control_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%208/Lecture%208d_%20Distance-Based%20Formation%20Control-20200925_033221.mp4) [13:14]

5. [_Artificial Potential Fields_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%209/Lecture%209b_%20Artificial%20Potential%20Fields-20210922_063731.mp4) [13:19]


### Reading material
Background and history can be found in “[_Springer handbook of robotics_](https://research.ebsco.com/linkprocessor/plink?id=c3f4173c-09f6-3d7b-b762-d16f6994ffad)”. Springer, 2016. Part E, Chapter 53 (Multiple Mobile Robot Systems).

The methods described in the lecture can be found in:
* Oh, K. K., Park, M. C., & Ahn, H. S.: "[_A survey of multi-agent formation control_](https://doi.org/10.1016/j.automatica.2014.10.022)". Automatica, 53, 424-440, 2015.

<a name="lecture09"></a>

## Lecture 9: Introduction to learning + research highlights [[learning-intro (2024)](Lecture_notes/lecture_10_learning_intro.pdf)]

### Video (from corona editions)


1. [_Introduction to learning for autonomous systems_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%2010_11/Lecture%2010-11a_%20Introduction-20200929_085149.mp4) [27:24]




<a name="lecture10"></a>

## Lecture 10: Learning for autonomous vehicles [[slides (2024)](Lecture_notes/lecture_10_11_learning_methods.pdf)]

### Video (from corona editions)
* [_2021 recorded live lecture_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%2010_11/Lecture%2010-11_live_2021-20210930_060258.mp4) [100:46]

2020 edition recorded lectures
2. [_Learning using neural networks_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%2010_11/Lecture%2010-11b_%20Learning%20using%20neural%20networks-20200930_111450.mp4) [30:39]
3. [_Introduction to reinforcement learning_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%2010_11/Lecture%2010-11d_%20Introduction%20to%20reinforcement%20learning-20200930_111812.mp4) [31:57]

### Extra video from 2020 (not part of later lecture series)
1. [_Learning using Gaussian processes_](https://liuonline.sharepoint.com/:v:/r/sites/VehicularSystemsEDU/Shared%20Documents/TSFS12/Lecture%2010_11/Lecture%2010-11c_%20Learning%20using%20Gaussian%20processes-20200930_111639.mp4) [17:01]


### Reading material

* "[_Reflections on the Learning-to-Control Renaissance_](https://youtu.be/IEZFwh8sw8s)", Plenary Talk from the June 2020 IFAC World Congress by [Benjamin Recht](https://www2.eecs.berkeley.edu/Faculty/Homepages/brecht.html), UC Berkley, USA. (https://youtu.be/IEZFwh8sw8s)
* Sections 11.2-11.8 in Hastie, T., R. Tibshirani, J. Friedman, & J. Franklin: [_The Elements of Statistical Learning: Data Mining, Inference and Prediction_](https://web.stanford.edu/~hastie/ElemStatLearn/). 2nd Edition, Springer, 2005.
* Sections 1, 4.1-4.4, and 6.1-6.5 in Sutton, R. S., & A. G. Barto: [_Reinforcement learning: An introduction_](http://incompleteideas.net/book/the-book-2nd.html). MIT Press, 2018.
* Mnih, V., Kavukcuoglu, K., Silver, D. et al: ”[_Human-level control through deep reinforcement learning_](https://doi.org/10.1038/nature14236)”, Nature 518, 529–533, 2015.

Further reading on deep neural networks and Markov decision processes under uncertain state information:
* Bishop, C. M., & Bishop, H. (2023) [_Deep Learning - Foundations and Concepts_](https://www.bishopbook.com) (available as a digital resource from the university library: [link](https://research.ebsco.com/linkprocessor/plink?id=25e800d4-ca0f-3b81-a4c2-64baa11b79ca))
* Goodfellow, I., Y. Bengio, & A. Courville: [_Deep Learning_](http://www.deeplearningbook.org). MIT Press, 2016.
* Westny, T., Frisk, E., Olofsson, B: ”[_Vehicle Behavior Prediction and Generalization Using Imbalanced Learning Techniques_](https://arxiv.org/abs/2109.10656)”, IEEE International Intelligent Transportation Systems Conference, 2021
* Åström, K. J.: ”[_Optimal control of Markov processes with incomplete state information_](https://doi.org/10.1016/0022-247X(65)90154-X)”, Journal of Mathematical Analysis and Applications, 10(1), 174-205, 1965.

<a name="lecture11"></a>

## Lecture 11: Industrial guest lecture

<a name="industrial_guest_lecture"></a>

# Guest lectures
## 2024 - Hannah Pelikan (LiU) and Andreas Allström (Einride)
### Hannah Pelikan, Postdoctoral researcher at the [Division of Language, Culture, and Interaction, LiU](https://liu.se/en/employee/hanpe82)

Title: "_Lessons from the road: Following delivery robots and self-driving vehicles on their rides through the city_"

* She wants to make robots behave better (https://liu.se/en/news-item/she-wants-to-make-robots-behave-better)
* Delivery robots on the road (https://doi.org/10.1145/3610977.3634936)
* When autonomous cars get honked at (https://doi.org/10.1145/3640792.3675732)
* Sound design for autonomous shuttle buses (https://doi.org/10.1145/3568162.3576979)

### Andreas Allström, [Einride](https://www.einride.tech)
Title: "_The future of freight transport - digital, electric and autonomous_"

## 2023 - Nils Hofemann and Jezdimir Milosevic, [Scania CV](https://www.scania.com)
Title: "_Motion planning and control for autonomous heavy-duty trucks: Mining and Hub to Hub use cases_"

## 2022 - Karl Granström, [Embark Trucks](https://embarktrucks.com)
Title: "_Perception, planning, and control at Embark_"

* MSc in Applied Physics and Electrical Engineering and PhD degree in Automatic Control
* Postdoctoral research fellow at the Department of Electrical and Computer Engineering at the University of Connecticut
* Since 2020 at Embark Trucks working on Ego Estimation and Odometry, Road Geometry Estimation for lane-lines and barriers, and Object Tracking.

## 2021 - Jesper Tordenlid, Combitech AB, 
Title: "_Research Arena for Public Safety Exploring autonomy in Reality_"
*  MSc Applied Physics and Electrical Engineering, Saab and Combitech AB, managing director of WASP ResearchArena Public Safety
* Information about WARA Public Safety on https://wasp-sweden.org/research/research-arenas/wara-ps-public-safety/

## 2020 - Karl Berntorp, MERL
Title: "_System Design, Motion-Planning, and Predictive Control for Autonomous Driving_"
*  Dr. Karl Berntorp, Principal Research Scientist, Mitsubishi Electric Research Labs, Boston, MA (https://www.merl.com/people/berntorp). 

* Reading material
    * Berntorp, K., T. Hoang, R. Quirynen, & S. Di Cairano: "[_Control Architecture Design for Autonomous Vehicles_](https://doi.org/10.1109/CCTA.2018.8511371)". IEEE Conference on Control Technology and Applications (CCTA), Copenhagen, 404-411, 2018.
    * Berntorp, K., T. Hoang, & S. Di Cairano: "[_Motion Planning of Autonomous Road Vehicles by Particle Filtering_](https://doi.org/10.1109/TIV.2019.2904394)". IEEE Transactions on Intelligent Vehicles, 4(2), 197-210, 2019.
    * Danielson, C., K. Berntorp, A. Weiss, & S. Di Cairano: "[_Robust Motion Planning for Uncertain Systems With Disturbances Using the Invariant-Set Motion Planner_](https://doi.org/10.1109/TAC.2020.3008126)". IEEE Transactions on Automatic Control, 65(10), 4456-4463, 2020.
    * Quirynen, R., K. Berntorp, K. Kambam, & S. Di Cairano: "[_Integrated Obstacle Detection and Avoidance in Motion Planning and Predictive Control of Autonomous Vehicles_](https://doi.org/10.23919/ACC45564.2020.9147820)". American Control Conference (ACC), Denver, CO, USA, 1203-1208, 2020.
    * Berntorp, K., R. Bai, K. F. Erliksson, C. Danielson, A. Weiss, & S. Di Cairano: "[_Positive Invariant Sets for Safe Integrated Vehicle Motion Planning and Control_](https://doi.org/10.1109/TIV.2019.2955371)". IEEE Transactions on Intelligent Vehicles, 5(1), 112-126, 2020.


## 2019 - Pär Degerman, [Einride](https://www.einride.tech)
* Pär Degerman, CTO at Einride, MSc Applied Physics and Electrical Engineering, Tech. Lic. Mechatronics


<a name="research_guest_lecture"></a>

# Research highlights
## 2024
### Jian Zhou -- "_Robust Motion-planning of autonomous vehicles under uncertainty_" 

### Theodor Westny -- "_Context aware vehicle trajectory prediction using Deep-Learning_"

## 2023
### Jian Zhou -- "_Motion-planning of autonomous vehicles using MPC_" 

### Theodor Westny -- "_Environment aware vehicle trajectory prediction_"

## 2022
### Jian Zhou -- "_Motion-planning of autonomous vehicles using MPC_" 
* Jian Zhou, PhD student, Dept. of Electrical Engineering, Linköping University.
* Reading material
    * Zhou, J., Olofsson, B., & Frisk, E. (2022, July). "[_Interaction-Aware Moving Target Model Predictive Control for Autonomous Vehicles Motion Planning_](https://doi.org/10.23919/ECC55457.2022.9838002)". In 2022 European Control Conference (ECC) (pp. 154-161). IEEE.

### Theodor Westny -- "_Neural ODEs and uncertainty estimation for vehicle trajectory prediction_"
* Theodor Westny, PhD student, Dept. of Electrical Engineering, Linköping University.
* Reading material
    * Westny, T., Frisk, E., & Olofsson, B. (2021, September). "[_Vehicle Behavior Prediction and Generalization Using Imbalanced Learning Techniques_](https://doi.org/10.1109/ITSC48978.2021.9564948)". In 2021 IEEE International Intelligent Transportation Systems Conference (ITSC) (pp. 2003-2010). IEEE.

## 2021
### Lars Svensson -- "_Motion Planning and Control of Automated Vehicles in Critical Situations_"
* Dr. Lars Svensson, Royal Institute of Technology (KTH), Stockholm
* Reading material
    * Svensson, L., Bujarbaruah, M., Kapania, N. R., & Törngren, M: "[_Adaptive trajectory planning and optimization at limits of handling_](https://doi.org/10.1109/IROS40897.2019.8967679)". In IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2019.
    * Svensson, L., Bujarbaruah, M., Karsolia, A., Berger, C., & Törngren, M: "[_Traction adaptive motion planning at the limits of handling_](https://arxiv.org/abs/2009.04180)". arXiv preprint arXiv:2009.04180, 2020.
    * Svensson, L: "[_Motion Planning and Control of Automated Vehicles in Critical Situations_](https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1554346), Ph.D. Thesis TRITA-ITM-AVL 2021:23, KTH Royal Institute of Technology, Stockholm, Sweden, 2021.


### Victor Fors -- "_Resilient Branching MPC for Multi-Vehicle Traffic Scenarios Using Open-Loop Adversarial Disturbance Sequences_"
* Dr. Victor Fors, Division of Vehicular Systems, Linköping University
* Reading material
    * Fors, V: ”[_Autonomous Vehicle Maneuvering at the Limit of Friction_](https://doi.org/10.3384/diss.diva-170606)”, Ph.D Thesis No. 2102, Div. Vehicular Systems, Linköping Univ., 2020.
    * Fors, V., Anistratov, P., Olofsson, B., & Nielsen, L: "[_Predictive force-centric emergency collision avoidance_](https://doi.org/10.1115/1.4050403)". Journal of Dynamic Systems, Measurement, and Control, 143(8), 081005, 2021.
    * Batkovic, I., Rosolia, U., Zanon, M., & Falcone, P: "[_A Robust Scenario MPC Approach for Uncertain Multi-modal Obstacles_](https://doi.org/10.1109/LCSYS.2020.3006819)". IEEE Control Systems Letters, 5(3), 947-952, 2020.
    * Cesari, G., Schildbach, G., Carvalho, A., & Borrelli, F: "[_Scenario Model Predictive Control for Lane Change Assistance and Autonomous Driving on Highways_](https://doi.org/10.1109/MITS.2017.2709782)". IEEE Intelligent Transportation Systems Magazine, 9(3), 23-35, 2017.
    * Alsterda, J. P., & Gerdes, J. C: "[_Contingency Model Predictive Control for Linear Time-Varying Systems_](https://arxiv.org/abs/2102.12045)". arXiv preprint arXiv:2102.12045, 2021.

<hr>

## 2020

### Kristoffer Bergman -- "_Tightly Combining Sampling-Based Motion Planning and Optimal Control_"
* PhD student, Dept. of Electrical Engineering, Automatic Control, Linköping University.
* Reading material
    * Bergman, K., Ljungqvist, O., & Axehill, D., "[_Improved path planning by tightly combining lattice-based path planning and optimal control_](https://doi.org/10.1109/TIV.2020.2991951)", IEEE Transactions on Intelligent Vehicles, 6(1), 57-66, 2021.
    * Bergman, K., Ljungqvist, O., Linder, J., & Axehill, D., "[_A COLREGs Compliant Motion Planner for Autonomous Maneuvering of Marine Vessels in Complex Environments_](https://arxiv.org/pdf/2012.12145.pdf)", arXiv preprint arXiv:2012.12145, 2021.
    * Bergman, K., "[_Exploiting Direct Optimal Control for Motion Planning in Unstructured Environments_](https://doi.org/10.3384/diss.diva-174175)", Ph.D. Thesis No. 2133, Division of Automatic Control, Linköping University, 2021.
    

### Marcus Greiff -- "_Motion planning and differential flatness_" [[slides](Lecture_notes/research_guest_lecture.pdf)]

* Department of Automatic Control, Lund University (http://www.control.lth.se/personnel/marcus-greiff/)
* Reading material
    * Greiff, M.: ”[_Modelling and control of the Crazyflie quadrotor for aggressive and autonomous flight by optical flow driven state estimation_](http://lup.lub.lu.se/student-papers/record/8905295)”, Master’s Thesis, Department of Automatic Control, Lund University, 2017.
    * Greiff, M.: ”[_A Time-Warping Transformation for Time-Optimal Movement in Differentially Flat Systems_](https://doi.org/10.23919/ACC.2018.8431230)”. Proc. American Control Conference (ACC), 6723-6730, 2018.
    * Fliess, M., Lévine, J., Martin, P., & Rouchon, P.: ”[_Flatness and defect of non-linear systems: Introductory theory and examples_](https://doi.org/10.1080/00207179508921959)”. International Journal of Control, 61(6), 1327-1361, 1995.
    * Richter, C., Bry, A., & Roy, N.: ”[_Polynomial trajectory planning for aggressive quadrotor flight in dense indoor environments_](https://doi.org/10.1007/978-3-319-28872-7_37)”. Proc. International Symposium of Robotics Research, 649-666, 2016.
    * Additional suggestions for further reading are available in the lecture slides.

<hr>

## 2019
### Oskar Ljungqvist - "_Motion planning and feedback control techniques with applications to long tractor-trailer vehicles_"
* PhD student, Dept. of Electrical Engineering, Automatic Control, Linköping University.
* Reading material
    * Andersson, Olov, Oskar Ljungqvist, Mattias Tiger, Daniel Axehill, and Fredrik Heintz. "[_Receding-horizon lattice-based motion planning with dynamic obstacle avoidance_](https://doi.org/10.1109/CDC.2018.8618964)". In 2018 IEEE Conference on Decision and Control (CDC), pp. 4467-4474. IEEE, 2018.
    * Ljungqvist, O., "[_Motion planning and feedback control techniques with applications to long tractor-trailer vehicles_](https://doi.org/10.3384/diss.diva-165246)", Ph.D. Thesis No. 2070, Division of Automatic Control, Linköping University, 2020.

### Zahra Gharee - "_A Bayesian Approach to Reinforcement Learning of Vision-Based Vehicular Control_"
* Dr. Zahra Gharee, post. doc, Dept. of Electrical Engineering, Computer Vision Laboratory, Linköping University.
* Reading material
    * Gharaee, Zahra, Karl Holmquist, Linbo He, and Michael Felsberg. "[_A Bayesian Approach to Reinforcement Learning of Vision-Based Vehicular Control_](https://doi.org/10.1109/ICPR48806.2021.9412200)". In 2020 25th International Conference on Pattern Recognition (ICPR), pp. 3947-3954. IEEE, 2021.

