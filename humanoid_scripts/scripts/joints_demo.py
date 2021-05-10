#!/usr/bin/env python

#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py

import rospy
from darwin_gazebo.darwin import Darwin
from movement import Movement
from parser import Parser



if __name__=="__main__":
    
    

    rospy.init_node("joints_demo")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Darwin Joints Demo Starting")

    parser = Parser("src/darwin_gazebo/src/testem.bt")
    data = parser.parseFile()
    
    m = Movement(darwin, rospy)
    s = 0
    a = 0
    roof = False
    m.move_arms('down', 'med', 1)
    print("m.move_arms('down', 'med', 1)")
    for frame in data:
      # figure out how to do the i lol
      # checking for raise the roof
      if frame[6][5] < -1 and frame[13][5] > 0.7:
        # start the raise the roof here - going up
        m.reset_legs(1)
        print("m.reset_legs(1)")
        m.raise_roof(1, 1.5, 1.5)
        print("m.raise_roof(1)")
        roof = True
        if frame[7][1] > -550 and frame[7][1] < -400:
          if frame[14][1] > -550 and frame[14][1] < -400:
            m.move_arms('up', 'high', 1)
            print("m.move_arms('up', 'high', 1)")
      elif frame[7][1] < -300 and frame[14][1] < -300:
        if a == 0:
          m.move_arms('up', 'med', 0)
          print("m.move_arms('up', 'med', 0)")
          a = 1
        if a > 0:
          a += 1
        if a == 4:
          a = 0
      elif frame[7][1] > 300 and frame[14][1] > 300:
        # can't move the arms down if raise roof was called in the same frame
        # (since raise roof automatically lowers arms)
        if roof == False:
          m.move_arms('down', 'low', 0.3)
          print("m.move_arms('down', 'low', 0.3)")
        # resets roof to false since the arms have been lowered
        roof = False
      if s == 0:
        if frame[19][2] < -100 and frame[23][2] < -100:
          if frame[19][1] > 0 and frame[23][1] > 0:
            m.squat(1)
            print("m.squat(1)")
            s = 1
      if s > 0:
        s += 1
      if s == 8:
        s = 0  
    #rospy.sleep(0.6)
    #m.reset_all(0)
    m.reset_all(1)
    m.move_arms('down','high',1)
    print("m.reset_all(1)")


#our hardcode
    #m.move_arms('down', 'med', 1)
    #m.move_arms('up', 'med',0)
    #m.squat(1)
   # m.move_arms('down', 'low',0.3)
    #m.reset_legs(1)
   # m.raise_roof(1)
    #m.move_arms('up', 'high',1)
    #m.squat(1)
    #m.reset_all(1)
    rospy.loginfo("Darwin Joints Demo Finished")


