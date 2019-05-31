# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:25:43 2019

@author: HIMANSHU SINGH
"""

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""


#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Foodtruck.csv')  

#explore the dataset
print dataset.shape
print dataset.ndim
print dataset.head()

print dataset.describe()

plt.boxplot(dataset.values)

#let's plot our data points on 2-D graph to eyeball our dataset and see if we can manually find any relationship between the data. We can create the plot with the following script:
dataset.plot(x='Population', y='Profit', style='o')  
plt.title('Poplulation vs Profit')  
plt.xlabel('Population')  
plt.ylabel('Profit')  
plt.show()

#prepare the data to train the model
features = dataset.iloc[:, 0].values  # iloc[: , :-1]
features=features.reshape(97,1) 
labels = dataset.iloc[:, 1].values 
labels.shape

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
x = 3073000                          # x = [[3073000]]
out = np.array(x).reshape(1,1)
print (regressor.predict(out))      # predict(x)






