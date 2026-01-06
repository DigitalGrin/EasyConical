<!-- image files here: https://imgur.com/a/HJDDpfY -->

# User Guide
EasyConical is meant to be used alongside a regular 3D print slicer for the best results. This guide will explain how to use our software along with the steps you need to take in the slicer you are using. All photos in this guide were taken in OrcaSlicer.
## Initial Slicer Setup
Before you begin, make sure the slicer you are using is able to use relative E distances. If it cannot, you must use another slicer, as EasyConical can only process relative E distances, not absolute.

EasyConical works by warping the print file around the vertical origin axis(usually Z). Unless your slicer can process parts outside of the buildplate, you will need to move the origin to the center of the buildplate. This can be done by setting the origin X and Y positions to exactly half of the buildplate’s X and Y size. Most slicers give you the ability to customize the buildplate settings, including moving the origin. 
![The buildplate customization menu in OrcaSlicer, with the origin set to the center of the buildplate.](https://i.imgur.com/VVbtjjM.png)
