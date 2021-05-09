#!/usr/bin/env python

import rospy
from darwin_gazebo.darwin import Darwin


if __name__=="__main__":
    rospy.init_node("leg_directions")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Darwin Leg Directions Demo Starting")


    darwin.set_angles({"j_thigh1_l": -1})
    rospy.sleep(3)
    darwin.set_angles({"j_thigh1_l": 1})
    rospy.sleep(3)
    darwin.set_angles({"j_thigh1_l": 0})
    rospy.sleep(3)

    """
    darwin.set_angles({"j_thigh2_l": -1})
    rospy.sleep(3)
    darwin.set_angles({"j_thigh2_l": 1})
    rospy.sleep(3)
    darwin.set_angles({"j_thigh2_l": 0})
    rospy.sleep(2)
    darwin.set_angles({"j_ankle1_l": -1})
    rospy.sleep(2)
    darwin.set_angles({"j_ankle1_l": 1})
    rospy.sleep(2)
    darwin.set_angles({"j_ankle1_l": 0})
    rospy.sleep(2)
    darwin.set_angles({"j_ankle2_l": -1})
    darwin.set_angles({"j_ankle2_l": 1})
    darwin.set_angles({"j_ankle2_l": 0})
    rospy.sleep(2)
    darwin.set_angles({"j_pelvis_l": -1})
    rospy.sleep(2)
    darwin.set_angles({"j_pelvis_l": 1})
    rospy.sleep(2)
    darwin.set_angles({"j_pelvis_l": 0})
    rospy.sleep(2)
    darwin.set_angles({"j_tibia_l": -1})
    rospy.sleep(2)
    darwin.set_angles({"j_tibia_l": 1})
    rospy.sleep(2)
    darwin.set_angles({"j_tibia_l": 0})
    rospy.sleep(2)
    """
    
    rospy.loginfo("Darwin Leg Directions Demo Finished")