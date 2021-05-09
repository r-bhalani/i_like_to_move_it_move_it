#!/usr/bin/env python

#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py

import rospy
from darwin_gazebo.darwin import Darwin


if __name__=="__main__":
    rospy.init_node("motion_tester")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Darwin motion testing Starting")

    # head j_pan moves head left and right j_tilt moves head up and down 
    # arm j_shoulder_l(or r) rotates arm around shoulder socket positive counterclockwise neg clockwise
    # high arm moves entire arm up and down
    # low arm moves beneath elbow left and right
    # wrist moves beneath elbow up and down
    # gripper moves the white part of gripper up and down
    # pelvis rotates leg about the pelvis socket
    # thigh1 moves leg outwards
    # thigh 2 moves leg so that heel is propped up
    # tibia moves knee joint out or in
    # ankle1 moves ankle forwards and backwards
    # ankle 2 moves ankle left and right
  
    darwin.set_angles({"j_thigh2_l": 2})
    rospy.sleep(1)
    darwin.set_angles({"j_thigh2_l": 0})
    rospy.sleep(3)
    darwin.set_angles({"j_thigh2_r": -2})
    rospy.sleep(1)
    darwin.set_angles({"j_thigh2_r": 0})
    rospy.sleep(3)
    

    rospy.loginfo("Darwin motion testing Finished")