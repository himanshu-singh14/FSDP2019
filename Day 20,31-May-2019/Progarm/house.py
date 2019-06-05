# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:37:54 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv("kc_house_data.csv", delimiter=",")

dataset['date'] = dataset['date'].apply(lambda x : x[0:4])
dataset["date"] = pd.to_numeric(dataset["date"])
dataset.isnull().any(axis=0)

dataset["sqft_above"] = dataset["sqft_above"].fillna(np.mean(dataset["sqft_above"]))
 
features = dataset.drop(["price","id"],axis=1).values
labels = dataset.iloc[:, 2].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

labels_pred = regressor.predict(features_test) 

TrainScore = regressor.score(features_train, labels_train)
TestScore = regressor.score(features_test, labels_test)

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred))) 

print (np.mean(dataset.values[:,2]))


