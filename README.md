# EasyConical
### Introduction
EasyConical is for generating 3D printing GCode without the need for support structures. It is intended to be used alongside regular 3D slicing softwares like [OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) or [SuperSlicer](https://github.com/supermerill/SuperSlicer). Our software is an easy to learn, plug-and-play solution with virtually no setup time.

### User Guide

Please refer to the [User Guide](./User%20Guide.md). Remember to use EasyConical alongside a slicer that can process the settings in the ['Required Settings'](./User%20Guide.md#required-settings) section of the user guide.

### Get EasyConical

The current version of EasyConical for Windows and Mac can be found on the [releases page](https://github.com/DigitalGrin/EasyConical/releases).

### Current Limitations

Certain workarounds, listed in the user guide, must be used in slicers based on Prusaslicer.

EasyConical can only process gcode files with relatve extrusion (e) distances.

EasyConical can only process singular models.

### Feedback

Please report all bugs and suggestions in the [issues page](https://github.com/DigitalGrin/EasyConical/issues)

### License

This program is open source and licensed under the GNU General Public License Version 3.0

[(https://www.gnu.org/licenses/gpl-3.0.en.html)]()

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
