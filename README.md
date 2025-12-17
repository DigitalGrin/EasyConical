# EasyConical
### Introduction
EasyConical is for generating 3D printing GCode without the need for support structures. It is intended to be used alongside regular 3D slicing softwares like [OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) or [Cura](https://github.com/Ultimaker/Cura). Our software is an easy to learn, plug-and-play soluion with virtually no setup time.

### User Guide

x

### Current Limitations

There is a feature/bug in slicers based on PrusaSlicer that sets part local part origins different from the bed origin, but this can be circumvented as described in the user guide.

EasyConical can only process gcode files with absolute extrusion (e) distances, files generated with relative e distances will not be processed correctly. We are currently working on another program that can convert gcode files between relative e to absolute e, but

### License

x

### Citations

The algorithns used in this software were modified from [these scripts](https://github.com/CNCKitchen/ConicalSlicer/tree/master/Scripts%20for%20Variable%20Angle), and were originally written for [this paper](https://www.researchgate.net/publication/354726760_A_Novel_Slicing_Strategy_to_Print_Overhangs_without_Support_Material):
```
@Article{app11188760,
AUTHOR = {Wüthrich, Michael and Gubser, Maurus and Elspass, Wilfried J. and Jaeger, Christian},
TITLE = {A Novel Slicing Strategy to Print Overhangs without Support Material},
JOURNAL = {Applied Sciences},
VOLUME = {11},
YEAR = {2021},
NUMBER = {18},
ARTICLE-NUMBER = {8760},
URL = {https://www.mdpi.com/2076-3417/11/18/8760},
ISSN = {2076-3417},
ABSTRACT = {Fused deposition modeling (FDM) 3D printers commonly need support material to print overhangs. A previously developed 4-axis printing process based on an orthogonal kinematic, an additional rotational axis around the z-axis and a 45° tilted nozzle can print overhangs up to 100° without support material. With this approach, the layers are in a conical shape and no longer parallel to the printing plane; therefore, a new slicer strategy is necessary to generate the paths. This paper describes a slicing algorithm compatible with this 4-axis printing kinematics. The presented slicing strategy is a combination of a geometrical transformation with a conventional slicing software and has three basic steps: Transformation of the geometry in the .STL file, path generation with a conventional slicer and back transformation of the G-code. A comparison of conventionally manufactured parts and parts produced with the new process shows the feasibility and initial results in terms of surface quality and dimensional accuracy.},
DOI = {10.3390/app11188760}
}
```
