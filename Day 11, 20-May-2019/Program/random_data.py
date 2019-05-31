# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:33:27 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import numpy as np
import random
import collections
arr = np.random.randint(5,15,40)
arr
arrr = collections.Counter(arr)
value = arrr.values()
maxx = max(list(value))
maxx
dc = dict(arrr)
dc
for ky,val in dc.items():
    if val==maxx:
        print (ky)

---------------------------------------------------------------------------

arr = np.array([2,2,2,2,3,3,3,3,4,5])
arrr = collections.Counter(arr)
arrr
value = arrr.values()
maxx = max(list(value))
maxx
dc = dict(arrr)
dc
for ky,val in dc.items():
    if val==maxx:
        print (ky)

------------------------------------------------------------------------

arr = np.array([2,2,2,2,2,3,3,3,3,4,5])
np.bincount(arr).argmax()

-----------------------------------------------------------------------


