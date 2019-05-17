# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:12:07 2019

@author: HIMANSHU SINGH
"""

# Printing Checkerboard Pattern

num = 1 
while num < 8:
    if num%2 == 0:
        print(" *"*8)
    else:
        print("* "*8)
    num += 1