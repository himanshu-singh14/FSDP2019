# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:40:49 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

def is_pallindromic(num):
    st = str(num)
    st1 = st[::-1]
    if st == st1:
        return True
    else:
        return False
ls2 = []    
ls = [121,9,61,5,14]
for i in ls:
    ls1 = is_pallindromic(i)
    ls2.append(ls1)
str2 = "False"
for value in ls2:
    if value == True:
        str2 = "True"
        break
print(str2)               
        

    





