# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:00:53 2019

@author: Narayan Devpura
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker

"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('material/Automobile.csv')

makers = df['make'].value_counts()

plt.pie(makers.values[:10], explode = (0.2,0,0,0,0,0,0,0,0,0), labels = makers.index[:10], autopct = '%2.2f%%', shadow = True, startangle = 180)
