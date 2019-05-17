# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:55:29 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

user_input = input("Enter values : ")
ls = user_input.split(",")
tp = tuple(ls)
print("List : ",ls)
print("List : ",tp)