# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:15:34 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

#let's plot our data points on 2-D graph to eyeball our dataset and see if we can manually find any relationship between the data. We can create the plot with the following script:
dataset.plot(x='Days', y='Bahubali_2_Collections_Per_day', style='o')  
plt.title('Days vs Bahubali_2_Collections_Per_day')  
plt.xlabel('Days')  
plt.ylabel('Bahubali_2_Collections_Per_day')  
plt.show()

#prepare the data to train the model
features = dataset.iloc[:, :-2].values  # for dangal iloc[:,:[0,2]]
labels = dataset.iloc[:, 1].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
day = np.array(10).reshape(1,-1)
print (regressor.predict(day))

---------------------------------------------------------------------------------------


#prepare the data to train the model
features = dataset.iloc[:,:-2].values  
labels = dataset.iloc[:,1:3].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
day = np.array(10).reshape(1,-1)
print (regressor.predict(day))