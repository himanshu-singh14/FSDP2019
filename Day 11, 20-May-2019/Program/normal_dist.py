# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:03:25 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150, 20, 1000)
print (incomes)
plt.hist(incomes, normed=True, bins=100)

print(np.std(incomes))
print(np.var(incomes))

