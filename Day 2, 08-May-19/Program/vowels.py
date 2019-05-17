# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:36:40 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list2 = []
for num in state_name:
    str1 = ""
    list1 = list(num)
    for num1 in list1:
        if num1 not in "aieouAIEOU":
            str1 = str1+num1
    list2.append(str1)
list2    
   


list1
str1 = "himanshu"
list1 = list(str1)
list1.remove('h')
str2 = "".join(list1)
str2