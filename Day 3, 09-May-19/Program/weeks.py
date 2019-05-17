# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:45:29 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

tp = ('Monday', 'Wednesday', 'Thursday', 'Saturday')
tpp = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

for item in tpp:
    if item not in tp:
        tp = tp + (item,)
print(tp)