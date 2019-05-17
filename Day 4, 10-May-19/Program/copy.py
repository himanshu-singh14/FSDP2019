# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:50:38 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

with open('himanshu.txt', 'wt') as file :
    file.write("This is my new file")
    
with open("himanshu.txt", "rt") as him :
    with open ("copy_himanshu.txt", "wt") as new_him :
        for line in him:
            new_him.write(line)
     









