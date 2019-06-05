# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:44:36 2019
@author: Narayan Devpura
"""

"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv
How is the length of a bluegill fish related to its age?
In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)
Response variable(Dependent): length (in mm) of the fish
Potential Predictor (Independent Variable): age (in years) of the fish
    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.
NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data
blue = pd.read_csv("material/bluegills.Csv")

# checking data
blue.isnull().any(axis = 0)

# features and labels
features = blue.iloc[:,0:1].values
labels = blue.iloc[:,1:].values

# train_test_split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


# Using LinearRegression 
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(features_train, labels_train)
pred1 = LR.predict(features_test)
LR_score = LR.score(features_test, labels_test)


# Using Polynomial for degree 2
from sklearn.preprocessing import PolynomialFeatures
ob = PolynomialFeatures(degree= 2)
poly_features = ob.fit_transform(features_train)

PLR = LinearRegression()
PLR.fit(poly_features, labels_train)

pred2 = PLR.predict(ob.transform(features_test))

PLR_score = PLR.score(ob.transform(features_test), labels_test)

if PLR_score > LR_score:
    print("The length of a bluegill fish best related to its age Quadratically")
    
else:
    print("The length of a bluegill fish best related to its age Linearly")


# Plotting Graph showing best fits of Linear and Quadratic Regression
plt.scatter(features, labels)
X = np.arange(min(features), max(features), 0.1)
X = X.reshape(len(X), 1)
plt.plot(X, LR.predict(X), color = 'blue')
plt.plot(X, PLR.predict(ob.transform(X)), color = 'red')
plt.show()
