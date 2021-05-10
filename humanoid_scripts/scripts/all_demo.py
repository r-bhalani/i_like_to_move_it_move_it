#!/usr/bin/env python

#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py

import rospy
from darwin_gazebo.darwin import Darwin
from movement import Movement


if __name__=="__main__":
    rospy.init_node("all_demo")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Demonstrating all motions in library! Starting demo")
    
    

    #heart


    m = Movement(darwin, rospy)
    m.heart(3)
    m.move_arms('down', 'med', 1)
    m.move_arms('up', 'med',0)
    m.squat(1)
    m.move_arms('down', 'low',0.3)
    m.reset_legs(1)
    m.raise_roof(1)
    m.move_arms('up', 'high',1)
    m.squat(1)
    m.kick('r',1)
    m.disco(1)
    m.kick('l',1)
    

   # m.reset_all(1)

    rospy.loginfo("Darwin all Demo Finished")


