#!/usr/bin/env python

#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py

import rospy
from darwin_gazebo.darwin import Darwin


if __name__=="__main__":
    rospy.init_node("joints_demo")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Darwin Joints Demo Starting")

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
  
  # moves the arms down to be beside the legs (starting pos in vid)
    darwin.set_angles({"j_high_arm_l": .8})
    darwin.set_angles({"j_high_arm_r": .8})
    rospy.sleep(1)

    # moves arms to be beside the head
    darwin.set_angles({"j_high_arm_l": -.8})
    darwin.set_angles({"j_high_arm_r": -.8})
    #rospy.sleep(1)
    #squat
    darwin.set_angles({"j_thigh1_l": -0.00319152487})
    darwin.set_angles({"j_thigh1_r": .005037157})
    darwin.set_angles({"j_thigh2_l": 0.553809440820})
    darwin.set_angles({"j_thigh2_r": -0.5465847})
    darwin.set_angles({"j_tibia_l": -1.10478644489})
    darwin.set_angles({"j_tibia_r": 1.10643813})
    darwin.set_angles({"j_ankle1_l": -0.54621655450})
    darwin.set_angles({"j_ankle1_r": 0.5511897})
    darwin.set_angles({"j_ankle2_l": -0.00481687531})
    darwin.set_angles({"j_ankle2_r": 0.00360597753})
    rospy.sleep(1)

    # moves the arms back down again
    darwin.set_angles({"j_high_arm_l": .6})
    darwin.set_angles({"j_high_arm_r": .6})
    rospy.sleep(0.3)
    darwin.set_angles({"j_thigh1_l": 0})
    darwin.set_angles({"j_thigh1_r": 0})
    darwin.set_angles({"j_thigh2_l": 0})
    darwin.set_angles({"j_thigh2_r": 0})
    darwin.set_angles({"j_tibia_l": 0})
    darwin.set_angles({"j_tibia_r": 0})
    darwin.set_angles({"j_ankle1_l": 0})
    darwin.set_angles({"j_ankle1_r": 0})
    darwin.set_angles({"j_ankle2_l": 0})
    darwin.set_angles({"j_ankle2_r": 0})
    rospy.sleep(1)

    # moves joint from elbow to wrist to face away from the body
    darwin.set_angles({"j_low_arm_l": -.8})
    darwin.set_angles({"j_low_arm_r": .8})
    rospy.sleep(1)
    
    # moves joint from elbow to wrist upwards
    darwin.set_angles({"j_wrist_l": .8})
    darwin.set_angles({"j_wrist_r": .8})
    rospy.sleep(1)

    # moves joint from elbow to wrist back to being parallel with body
    # and moves entire arm upwards (halfway)
    darwin.set_angles({"j_low_arm_l": 0})
    darwin.set_angles({"j_low_arm_r": 0})
    darwin.set_angles({"j_high_arm_l": -.5})
    darwin.set_angles({"j_high_arm_r": -.5})
    rospy.sleep(1)

    # arm up again
    darwin.set_angles({"j_high_arm_l": -1})
    darwin.set_angles({"j_high_arm_r": -1})
    #rospy.sleep(1)

    #squat
    darwin.set_angles({"j_thigh1_l": -0.00319152487})
    darwin.set_angles({"j_thigh1_r": .005037157})
    darwin.set_angles({"j_thigh2_l": 0.553809440820})
    darwin.set_angles({"j_thigh2_r": -0.5465847})
    darwin.set_angles({"j_tibia_l": -1.10478644489})
    darwin.set_angles({"j_tibia_r": 1.10643813})
    darwin.set_angles({"j_ankle1_l": -0.54621655450})
    darwin.set_angles({"j_ankle1_r": 0.5511897})
    darwin.set_angles({"j_ankle2_l": -0.00481687531})
    darwin.set_angles({"j_ankle2_r": 0.00360597753})
    rospy.sleep(1)
    

    # resets everything else
    darwin.set_angles({"j_wrist_l": 0})
    darwin.set_angles({"j_wrist_r": 0})
    darwin.set_angles({"j_high_arm_l": 0})
    darwin.set_angles({"j_high_arm_r": 0})
    darwin.set_angles({"j_thigh1_l": 0})
    darwin.set_angles({"j_thigh1_r": 0})
    darwin.set_angles({"j_thigh2_l": 0})
    darwin.set_angles({"j_thigh2_r": 0})
    darwin.set_angles({"j_tibia_l": 0})
    darwin.set_angles({"j_tibia_r": 0})
    darwin.set_angles({"j_ankle1_l": 0})
    darwin.set_angles({"j_ankle1_r": 0})
    darwin.set_angles({"j_ankle2_l": 0})
    darwin.set_angles({"j_ankle2_r": 0})
    rospy.sleep(1)

    rospy.loginfo("Darwin Joints Demo Finished")