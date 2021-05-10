#!/usr/bin/env python
#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py

# Parses data returned from azure body tracking and stores it in a 3D array
# Measures the differences between the specified frames in order to provide a more accurate portrayal
# of positional differences and track the amount of movement of 1 body

import numpy as np
class Parser:

    def __init__(self, readfile):
        self.filename = readfile

    def write(self):
        # Opening a file
        file1 = open(self.filename, 'w')
        L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
        s = "Hello\n"
        
        # Writing a string to file
        file1.write(s)
        
        # Writing multiple strings
        # at a time
        file1.writelines(L)
        
        # Closing file
        file1.close()
    
    def parseFile(self):

        #FOR GENERIC USE
        # set the number of joints you're taking in
        num_joints = 32
        # set the number of coordinates you're taking in for each joint
        num_coordinates = 7
        # set the size of the header for each frame (number lines to skip when reading data)
        header_size = 3
        # frame read rate (number of frames in each frame section)
        frame_rate = 10


        coordinate_values = [] #the cells; size should be 7
        all_joints = [] #collection of cells for all the joints; size should be 32
        #current_frame_section = [] #store the difference between the 1st and last frames
        complete_db = [] #the full database of information; return value
        
        current_frame_index = 0 #store in the 1st frame, then subtract when you reach 10th frame
        skip_line_index = 0 #skip line, -1 if you have to read it in
        first = True


        # read in every ten frames, and calculate the difference in all the values
        #store the difference in a 2d array
        #each row in the array represents 10 frames
        # each row has 7 columns, each representing the difference in the values
        #skip the first line, because that's just the number of joints
        #skip each frame header (3 lines with timestamp, # bodies, and body index)
        with open(self.filename, "r") as input_file:
            for line in input_file:
                num = line.strip() #get rid of trailing newline characters at the end of the line
                if first == True:
                    first = False
                    continue
                if skip_line_index != -1:
                    if skip_line_index == header_size - 1:
                        skip_line_index = -1
                    else:
                        skip_line_index+=1
                else:
                    # this is a line we have to read in
                    coordinate_values.append(float(num)) #converts the value to a float type
                    if len(coordinate_values) == num_coordinates:
                        # all filled up
                        all_joints.append(coordinate_values)
                        if len(all_joints) == num_joints:
                            #all filled up
                            if current_frame_index == 0:
                                complete_db.append(all_joints)
                            if current_frame_index == frame_rate - 1:
                                complete_db[len(complete_db) - 1] = np.subtract(all_joints, complete_db[len(complete_db) - 1])
                            #if it's neither of these things then ignore it and move onto the next one`
                            skip_line_index = 0
                            if current_frame_index < 9:
                                current_frame_index += 1
                            else:
                                current_frame_index = 0
                            all_joints = []
                        
                        coordinate_values = []
        
        return complete_db