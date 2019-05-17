# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:47:03 2019

@author: HIMANSHU SINGH
"""

# Hands On  1
# Print all the numbers from 1 to 10 using condition in while loop

num = 1
while num < 11:
    print(num)
    num = num + 1

# Hands On  2
#  Print all the numbers from 1 to 10 using while True loop
    
num = 1
while True:
    print(num)
    num = num + 1
    if num == 11:
        break

# Hands On 3
#  Print all the even numbers from 1 to 10 using condition in while loop
        
num = 1
while num < 11:
    if num%2 == 0:
        print(num)
    num = num + 1   

# Hands On 4
#  Print all the even numbers from 1 to 10 using while True loop
    
num = 1
while True:
    if num%2 == 0:
        print(num)
    num = num + 1
    if num == 11:
        break

# Hands On 5
#  Print all the odd numbers from 1 to 10 using condition in while loop

num = 1
while num < 11:
    if num%2 != 0:
        print(num)
    num = num + 1 
    
# Hands On 6
#  Print all the odd numbers from 1 to 10 using while True loop
    
num = 1
while True:
    if num%2 != 0:
        print(num)
    num = num + 1
    if num == 11:
        break