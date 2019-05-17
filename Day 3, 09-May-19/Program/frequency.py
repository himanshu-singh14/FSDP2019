# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:29:51 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

dic = {}
    user_input = input()
    ls = user_input.split()
    if user_input != "":
        if ' '.join(ls) in dic:
            dic[' '.join(ls)] += int(values)
        else:
            dic[' '.join(ls)] = int(values)
    if not user_input:
        break
print(dic)








