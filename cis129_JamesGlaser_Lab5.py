#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:51:47 2025
Module 5 Lab
CIS129
@author: glaserj0
"""

# Lab 5 The Bottle Return Program

# Step 1: Declare variable to start loop 
keepGoing = 'y'
# Step 2: Loop to run program again
while(keepGoing == 'y'):
    # Declare initial values for variables for program
    NBR_OF_DAYS = 7
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    counter = 0
    while (counter < NBR_OF_DAYS): # to repeat code for 7 days
        # code to set value of variable totalBottles
        todayBottles = int(input(f'Enter number of bottles for day {counter + 1}: '))
        totalBottles += todayBottles
        counter += 1
    # code to set value of variable totalPayout
    totalPayout = (totalBottles * 0.10)
	# code to print the number of total bottles and total payout
    print(f'The total number of bottles collected is {totalBottles}')
    print(f'The total paid out is ${totalPayout:.2f}')
    # code to display message asking if you want to repeat the program
    print("Do you want to enter another week’s worth of data?")
    print("Enter y for yes or n for no")
    # code to change the value of keepGoing to either continue or end the loop
    keepGoing = input()