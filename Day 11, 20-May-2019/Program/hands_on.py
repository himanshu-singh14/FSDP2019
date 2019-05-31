# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:08:02 2019

@author: HIMANSHU SINGH
"""

# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8

import numpy as np
x = [13, 18, 13, 14, 13, 16, 14, 21, 13]
arr = np.array(x)
print(arr.mean())
print(np.median(arr))

from scipy import stats
print(stats.mode(arr))
