# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:22:43 2019

@author: HIMANSHU SINGH
"""

# Fizz Buzz

num = 1
while num < 101:
    if num%3 == 0 and num%5 == 0:
        print ("FizzBuzz")
        continue
    elif num%5 == 0:
        print ("Buzz")
    elif num%3 == 0:
        print ("Fizz")
    else:
        print (num)
    
        