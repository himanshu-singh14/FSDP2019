# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:05:39 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

user_input = input("Enter file name with txt extention in double quoted comma :")
with open(user_input, 'rt') as file :
    print(file.readlines()[-1])
    
    