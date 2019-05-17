# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:26:07 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

with open("absentee.txt", "wt") as ab:
    num = 1
    while num <= 4:
        user_input = input("Enter name : ")
        if user_input == "":
            break
        else:
            ab.write(user_input+"\n")
        num = num + 1