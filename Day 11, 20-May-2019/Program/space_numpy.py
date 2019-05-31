# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:21:16 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

import numpy as np
ls = list(map(int,input("Enter 9 sapce seperated numbers : ").split(" ")))
arr = np.array(ls)
arr.reshape(3,3)



