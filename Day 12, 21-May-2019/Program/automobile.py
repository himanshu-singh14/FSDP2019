# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:50:21 2019

@author: Narayan Devpura
"""


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np

df = pd.read_csv('material/Automobile.csv')

#  Handle the missing values for Price column
df['price'] = df['price'].fillna(round(df['price'].mean(),1))

# Get the values from Price column into a numpy.ndarray
nd_array = np.array(df['price'])

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
min_price = np.min(nd_array)
max_price = np.max(nd_array)
mean_price = np.mean(nd_array)
std_price = np.std(nd_array)
