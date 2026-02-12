#Course: COMP 2113 WI01 Data Structures and Algorithms 2026
#Assignment 1, Question 1
#Author: Catherine Nixon
#Student ID: 0311174
#Email address: 0311174n@acadiau.ca
#Date: 2026 - 01 - 26
#I certify that this code is my own.
#I have not broken any rules concerning Academic Dishonesty.

import random

#Generating the random numbers and save them to a file
print("Random Number Generator")
file = input("Enter the file name to save the numbers: ")
total_numbers = int(input("how many numbers to generate? "))
min_num = int(input("Enter the smallest number: "))
max_num = int(input("Enter the largest number: "))

with open(file, 'w') as output:
    for _ in range(total_numbers):
        random_number = random.randint(min_num, max_num)
        output.write(f"{random_number}\n")
        
print(f"{total_numbers} numbers saved to {file}.")
