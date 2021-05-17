## darwin_gazebo

ROS package providing Gazebo simulation of the Darwin OP robot.
Also provides a Python interface to the joints and some walk capabilities.

These have been tested in simulation and need some work to be used on the real robot, do not use as-is.

![Darwin model in Gazebo](/humanoid_scripts/darwin.png "Darwin model in Gazebo")
    
## Usage

You can launch the simulation with:

    roslaunch darwin_gazebo darwin_gazebo.launch
    
PRESS PLAY IN GAZEBO ONLY WHEN EVERYTHING IS LOADED (wait for controllers)

You can run Alekhya, Ruchi, and Emily's body movement imitation FRI project with:

    rosrun darwin_gazebo joints_demo.py

## Dependencies

The following ROS packages have to be installed:
* gazebo_ros_control
* hector_gazebo

## License

This software is provided by Génération Robots http://www.generationrobots.com and HumaRobotics http://www.humarobotics.com under the Simplified BSD license
