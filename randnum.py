######################### 
# Course: COMP 2113 WI01, 2026 
# Assignment 1 
# Author: Traci Pillarina 
# Student ID: 0310439p 
# email address: 0310439p@acadiau.ca 
# Date: 2026-01-22 / 2026-01-27
# I certify that this code is my own. 
# I have not broken any rules concerning Academic Dishonesty. 
#########################

import random
import sys

#terminates program if number of arguments isn't 5
if (len(sys.argv) != 5):
    print("Must have 5 arguments: 'program_name', 'min_range', 'max_range', 'total_num', 'file_name'")
    sys.exit()

#set variables for the user input / arguments in the command line 
min_range = int(sys.argv[1])
max_range = int(sys.argv[2])
total_num = int(sys.argv[3])
file_name = sys.argv[4]

#checks if min_range is smaller than max_range
if (min_range >= max_range or max_range <= min_range):
    print("Error: minimum range must be smaller than maximum range.")
    sys.exit()

#generates the random numbers in a new file named by user 
with open(file_name, 'w') as file: 
    for i in range(total_num):
        num = random.randrange(min_range, max_range + 1)
        #writes to file
        file.write(str(num) + "\n")
