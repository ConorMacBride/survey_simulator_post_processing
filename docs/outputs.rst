Outputs
==================
  
Objects in Field (OIF) Output
------------------------------
The format of the OIF output looks something like::
   
   ObjID, FieldID, FieldMJD, AstRange(km), AstRangeRate(km/s), AstRA(deg), AstRARate(deg/day), AstDec(deg), AstDecRate(deg/day), Ast-Sun(J2000x)(km), Ast-Sun(J2000y)(km), Ast-Sun(J2000z)(km), Ast-Sun(J2000vx)(km/s), Ast-Sun(J2000vy)(km/s), Ast-Sun(J2000vz)(km/s), Obs-Sun(J2000x)(km), Obs-Sun(J2000y)(km), Obs-Sun(J2000z)(km), Obs-Sun(J2000vx)(km/s), Obs-Sun(J2000vy)(km/s), Obs-Sun(J2000vz)(km/s), Sun-Ast-Obs(deg), V, V(H=0)
   S100003Ua,992,59855.012720,232764749.248562,19.381,313.391309,0.093855,-14.189297,-0.001147,302701424.872,-141376977.611,-47258199.518,10.938,16.381,6.838,147675817.300,22607836.793,9798564.669,-5.071,27.085,11.641,22.025168,12.229,3.789
   S100005xa,40,59854.002209,311895722.264139,18.108,312.493375,0.024745,-10.868628,-0.020284,355032405.197,-205593003.122,-50029660.233,8.437,15.234,7.005,148124584.428,20259701.559,8780700.962,-4.542,27.134,11.674,17.656392,14.416,4.726


The output from OIF is directly input into surveySimPPr. The following table gives an overview of each of the output columns:

+------------------------+----------------------------------------------------------------------------------+
| Keyword                | Description                                                                      |
+========================+==================================================================================+
| ObjID                  | Object identifier                                                                |
+------------------------+----------------------------------------------------------------------------------+
| FieldID                | Pointing Identifer                                                               |
+------------------------+----------------------------------------------------------------------------------+
| FieldMJD               | MJD (Mean Julian Date) of the observation                                        | 
+------------------------+----------------------------------------------------------------------------------+
| AstRange(km)           | Topocentric distance to the small body (km)                                      |
+------------------------+----------------------------------------------------------------------------------+
| AstRangeRate(km/s)     | Radial component of the topocentric velocity vector (km/s)                       |
+------------------------+----------------------------------------------------------------------------------+
| AstRA(deg)             | Object Right Ascension (RA) (degrees)                                            |
+------------------------+----------------------------------------------------------------------------------+
| AstRARate(deg/day)     | Observed rate of on-sky motion in RA (degree/day)                                |
+------------------------+----------------------------------------------------------------------------------+
| AstDec (deg)           | Object Declination (Dec) (degrees)                                               |
+------------------------+----------------------------------------------------------------------------------+
| AstDecRate(deg/day)    | Observed rate of on-sky motion in Dec (degree/day)                               |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000x)(km)    | Object heliocentric distance (x-component) (km)                                  |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000y)(km)    | Object heliocentric distance (y-component) (km)                                  |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000z)(km)    | Object heliocentric distance (z-component) (km)                                  |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000vx)(km/s) | Object heliocentric velocity (x-component) (km/s)                                |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000vy)(km/s) | Object heliocentric velocity (y-component) (km/s)                                |
+------------------------+----------------------------------------------------------------------------------+
| Ast-Sun(J2000vz)(km/s) | Object heliocentric velocity (z-component) (km/s)                                |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000x)(km)    | Observer heliocentric distance (x-component) (km)                                |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000y)(km)    | Observer heliocentric distance (y-component) (km)                                |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000z)(km)    | Observer heliocentric distance (z-component) (km)                                |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000vx)(km/s) | Observer heliocentric velocity (x-component) (km/s)                              |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000vy)(km/s) | Observer heliocentric velocity (y-component) (km/s)                              |
+------------------------+----------------------------------------------------------------------------------+
| Obs-Sun(J2000vz)(km/s) | Observer heliocentric velocity (z-component) (km/s)                              |
+------------------------+----------------------------------------------------------------------------------+
| Sun-Ast-Obs(deg)       | Phase angle (hase angle between the Sun, object, & observer) (degrees)           |
+------------------------+----------------------------------------------------------------------------------+
| V                      | Object's apparent V magnitude, if H is provided                                  |
+------------------------+----------------------------------------------------------------------------------+
| V(H=0)                 | Object's apprent V amgnitude if H=0, if H is provided as input                   |
+------------------------+----------------------------------------------------------------------------------+

.. note::
   All positions, positions, and velocities are in respect to J2000. 

SurveySimPP Output
----------------------
The format of the survey simulator output looks something like::
   
   ObjID	FieldID	FieldMJD	AstRange(km)	AstRangeRate(km/s)	AstRA(deg)	AstRARate(deg/day)	AstDec(deg)	AstDecRate(deg/day)	Ast-Sun(J2000x)(km)	Ast-Sun(J2000y)(km)	Ast-Sun(J2000z)(km)	Ast-Sun(J2000vx)(km/s)	Ast-Sun(J2000vy)(km/s)	Ast-Sun(J2000vz)(km/s)	Obs-Sun(J2000x)(km)	Obs-Sun(J2000y)(km)	Obs-Sun(J2000z)(km)	Obs-Sun(J2000vx)(km/s)	Obs-Sun(J2000vy)(km/s)	Obs-Sun(J2000vz)(km/s)	Sun-Ast-Obs(deg)	V(H=0	r	u-r	g-r	i-r	z-r	y-r	GS	FORMAT	q	e	incl	Omega	argperi	t_p	H	t_0	g	i	z	observationStartMJD	optFilter	seeingFwhmGeom	seeingFwhmEff	fiveSigmaDepth	fieldRA	fieldDec	rotSkyPos	MagnitudeInFilter	detection_probability	AstrometricSigma(mas)	PhotometricSigma(mag)	SNR	AstrometricSigma(deg)	dmagDetect	dmagVignet	AstRATrue(deg)	AstDecTrue(deg)	detectorID	counter
   St50000na	62219	60316.29343	681970963.2	-22.13	159.7465201	-0.044737	3.913379645	-0.005534	-679174915.5	365194946.6	102747132.1	-6.571	-9.857	-5.602	-40861819.07	129664764.6	56203804.57	-29.365	-8.001	-3.331	8.778568	7.471	16.07484516	0	0	0	0	0	0.15	COM	5.03716	0.02669	6.469	295.581	132.80719	46418.04982	8.59	54800	16.07484516	16.07484516	16.07484516	60316.29343	r	0.585678604	0.649244044	24.43052583	159.521035	3.397667557	92.68659281	16.07404683	1	10.00285687	0.000738342	1470.006032	2.78E-06	0	0	159.746518	3.91338	137	0
   St50000na	62265	60316.3154	681929000.3	-22.07	159.7455331	-0.044908	3.91325493	-0.005532	-679187393.4	365176229.6	102736495.2	-6.571	-9.857	-5.602	-40917530.36	129649531.7	56197475.35	-29.316	-8.043	-3.336	8.775898	7.471	16.07460555	0	0	0	0	0	0.15	COM	5.03716	0.02669	6.469	295.581	132.80719	46418.04982	8.59	54800	16.07460555	16.07460555	16.07460555	60316.3154	i	0.646608058	0.723367467	23.87237218	159.521035	3.397667557	103.1829538	16.07441405	1	10.00588854	0.000960114	1130.340983	2.78E-06	0	0	159.745533	3.913258	137	0
   
   
+------------------------------------+----------------------------------------------------------------------------------+
| Keyword                            | Description                                                                      |
+====================================+==================================================================================+
| ObjID                              | Object identifier                                                                |
+------------------------------------+----------------------------------------------------------------------------------+
| FieldMJD                           | MJD (Mean Julian Date) of the observation                                        |
+------------------------------------+----------------------------------------------------------------------------------+
| fieldRA                            | Right ascension (RA) of the center of the observation pointing (degrees)         | 
+------------------------------------+----------------------------------------------------------------------------------+
| fieldDec                           | Declination (Dec) of the center of the observation pointing (degrees)            |
+------------------------------------+----------------------------------------------------------------------------------+
| AstRa(deg)                         | Object Right Ascension (RA) (degrees)                                            |
+------------------------------------+----------------------------------------------------------------------------------+
| AstDec(deg)                        | Object Declination (Dec) (degrees)                                               |
+------------------------------------+----------------------------------------------------------------------------------+
| AstrometricSigma(deg)              | Astrometric uncertainty (degrees)                                                |
+------------------------------------+----------------------------------------------------------------------------------+
| optFilter                          | Filter Observation Taken in                                                      |
+------------------------------------+----------------------------------------------------------------------------------+
| observedPSFMag                     | Apparent magnitude in optFilter measured by the data management piplines         |
+------------------------------------+----------------------------------------------------------------------------------+
| observedTrailedSourceMag           | Apparent magnitude in optFilter adding up all of the counts in the trail         |
+------------------------------------+----------------------------------------------------------------------------------+
| PhotometricSigmaPSF(mag)           | observedPSFMag 1-sigma uncertainty                                               |
+------------------------------------+----------------------------------------------------------------------------------+
| PhotometricSigmaTrailedSource(mag) | observedTrailedSourceMag 1-sigma uncertainty                                     |
+------------------------------------+----------------------------------------------------------------------------------+
| fiveSigmaDepth                     |  5-sigma limiting magnitude at the center of the pointing                        |
+------------------------------------+----------------------------------------------------------------------------------+
| fiveSigmaDepthAtSource             |  5-sigma limiting magnitude at the object's location on the detector             |
+------------------------------------+----------------------------------------------------------------------------------+

.. note::
   All positions, positions, and velocities are in respect to J2000.
