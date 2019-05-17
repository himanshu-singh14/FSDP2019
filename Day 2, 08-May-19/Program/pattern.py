# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:22:59 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

for num in range(1,10):
        if num < 6:
            print("* "*num)
        else:
            print("* "*(10-num))













