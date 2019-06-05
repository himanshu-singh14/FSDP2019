# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:53:23 2019
@author: Narayan Devpura
"""

"""
Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.
"""
import pandas as pd
import numpy as np

# read data
un = pd.read_csv('material/University_data.csv')
un.iloc[:,0].unique()

# features and labels 
features = un.iloc[:, :-1].values
labels = un.iloc[:, -1].values

# Checking for null entries
un.isnull().any(axis=0)

# performing label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

# performing onehot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)

# Predicting the Test set results
Pred = regressor.predict(features)

# Comparing predicted to original
print (pd.DataFrame(Pred, labels))

# Prediction for a new values 
# make this accorifng to the data csv
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap

x = [0,1,0,0,313,3,4,8.6,0]
x = np.array(x)
regressor.predict(x.reshape(1, -1))

# Label and OneHot Encoding
le = labelencoder.transform(['Beaver'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],313,3,4,8.6,0]
x = np.array(x)
y = regressor.predict(x.reshape(1, -1))


# Getting Score for the Multi Linear Reg model
Score = regressor.score(features, labels)
Score = regressor.score(x.reshape(1, -1), y)