# kinect_sources

Output from the Azure Kinect Body Tracking SDK read in from the video files

Text in the .bt files are in the following format:

Each bt file header includes
```
[number of joints]
```
followed by the following information for each individual frame:
```
[timestamp]
[number of bodies]
[body index]
[x value for joint[0]]
[y value for joint[0]]
[z value for joint[0]]
[qx value for joint[0]]
[qy value for joint[0]]
[qz value for joint[0]]
[qw value for joint[0]]
```
