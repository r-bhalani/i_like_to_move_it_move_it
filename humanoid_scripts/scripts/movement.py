#!/usr/bin/env python
#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py
#import rospy

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

class Movement:

    def __init__(self, darwin, rospy):
        self.d = darwin
        self.r = rospy
  
  # squat
    def squat(self, rest):
        self.d.set_angles({"j_thigh1_l": -0.00319152487})
        self.d.set_angles({"j_thigh1_r": .005037157})
        self.d.set_angles({"j_thigh2_l": 0.553809440820})
        self.d.set_angles({"j_thigh2_r": -0.5465847})
        self.d.set_angles({"j_tibia_l": -1.10478644489})
        self.d.set_angles({"j_tibia_r": 1.10643813})
        self.d.set_angles({"j_ankle1_l": -0.54621655450})
        self.d.set_angles({"j_ankle1_r": 0.5511897})
        self.d.set_angles({"j_ankle2_l": -0.00481687531})
        self.d.set_angles({"j_ankle2_r": 0.00360597753})
        self.r.sleep(rest)


    def move_arms(self, direction, val, rest):
        multiplier = 0
        radian = 0
        if direction == 'down':
            multiplier = 1
        if direction == 'up':
            multiplier = -1
        if val == 'high':
            radian = 1
        if val == 'med':
            radian = 0.8
        if val == 'low':
            radian = 0.6
        self.d.set_angles({"j_high_arm_l": multiplier * radian})
        self.d.set_angles({"j_high_arm_r": multiplier * radian})
        self.r.sleep(rest)

    def raise_roof(self,rest1, rest2, rest3):
        # moves joint from elbow to wrist to face away from the body
        self.d.set_angles({"j_low_arm_l": -.8})
        self.d.set_angles({"j_low_arm_r": .8})
        self.r.sleep(rest1)
        # moves joint from elbow to wrist upwards
        self.d.set_angles({"j_wrist_l": .8})
        self.d.set_angles({"j_wrist_r": .8})
        self.r.sleep(rest2)
        # moves joint from elbow to wrist back to being parallel with body
        # and moves entire arm upwards (halfway)
        self.d.set_angles({"j_low_arm_l": 0})
        self.d.set_angles({"j_low_arm_r": 0})
        self.d.set_angles({"j_high_arm_l": -.5})
        self.d.set_angles({"j_high_arm_r": -.5})
        self.r.sleep(rest3)

    def disco(self,rest):
            #disco
        self.d.set_angles({"j_shoulder_l": -3})
        self.d.set_angles({"j_high_arm_l": 1})
        #rospy.sleep(3)
        self.r.sleep(3)
        self.d.set_angles({"j_shoulder_l": 2})
        self.d.set_angles({"j_high_arm_l": -3})
        self.r.sleep(rest)
        #rospy.sleep(3)

    def kick(self, leg,rest):
        if leg == 'r':
            self.d.set_angles({"j_thigh2_r": -1.5})
            self.r.sleep(1)
            self.d.set_angles({"j_thigh2_r": 0})
        if leg == 'l':
            self.d.set_angles({"j_thigh2_l": -1.5})
            self.r.sleep(1)
            self.d.set_angles({"j_thigh2_l": 0})
        self.r.sleep(rest)
    
    def heart(self,rest):
        self.d.set_angles({"j_high_arm_l": -1.60, "j_high_arm_r": -1.60})
        self.d.set_angles({"j_wrist_l": 1})
        self.d.set_angles({"j_wrist_r": 1})
        self.d.set_angles({"j_shoulder_l": 5})
        self.d.set_angles({"j_shoulder_r": -5})
        self.r.sleep(rest)

        
    def reset_legs(self,rest):
        self.d.set_angles({"j_thigh1_l": 0})
        self.d.set_angles({"j_thigh1_r": 0})
        self.d.set_angles({"j_thigh2_l": 0})
        self.d.set_angles({"j_thigh2_r": 0})
        self.d.set_angles({"j_tibia_l": 0})
        self.d.set_angles({"j_tibia_r": 0})
        self.d.set_angles({"j_ankle1_l": 0})
        self.d.set_angles({"j_ankle1_r": 0})
        self.d.set_angles({"j_ankle2_l": 0})
        self.d.set_angles({"j_ankle2_r": 0})
        self.r.sleep(rest)
    
    def reset_arms(self):
        self.d.set_angles({"j_wrist_l": 0})
        self.d.set_angles({"j_wrist_r": 0})
        self.d.set_angles({"j_high_arm_l": 0})
        self.d.set_angles({"j_high_arm_r": 0})
        self.d.set_angles({"j_low_arm_l": 0})
        self.d.set_angles({"j_low_arm_r": 0})
        self.d.set_angles({"j_gripper_l": 0})
        self.d.set_angles({"j_gripper_r": 0})
        self.d.set_angles({"j_shoulder_l": 0})
        self.d.set_angles({"j_shoulder_r": 0})
    
    def reset_all(self,rest):
        self.reset_arms()
        self.reset_legs(rest)