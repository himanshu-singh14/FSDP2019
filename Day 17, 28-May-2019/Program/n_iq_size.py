# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:44:53 2019
@author: Narayan Devpura
"""

"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv
Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?
Import the iq_size.csv file
It Contains the details of 38 students, where
Column 1: The intelligence (PIQ) of students
Column 2:  The brain size (MRI) of students (given as count/10,000).
Column 3: The height (Height) of students (inches)
Column 4: The weight (Weight) of student (pounds)
    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data
iq = pd.read_csv('material/iq_size.csv')

# features and labels
features = iq.iloc[:,-3:]
labels = iq.iloc[:,:1]


#plt.scatter(features.iloc[:,0], labels)
#plt.scatter(features.iloc[:,1], labels)
#plt.scatter(features.iloc[:,2], labels)
#plt.plot(features.iloc[:,0], LR.predict(labels))

# Applying LinearRegression
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(features, labels)
LR.predict(np.array([90, 70, 150]).reshape(1,-1))

# Plotting graph

plt.scatter(features, labels)
plt.plot(features, LR.predict(features))

plt.scatter(features.iloc[:,1], labels)
plt.plot(features.iloc[:,1], LR.predict(features))

plt.scatter(features.iloc[:,2], labels)
plt.plot(features.iloc[:,2], LR.predict(features))
plt.show()


# Applying OLS 
import statsmodels.api as sms

features = sms.add_constant(features)

features_OLS = features.iloc[:, [0,1,2,3]]

regressor = sms.OLS(endog= labels, exog= features_OLS).fit()

regressor.summary()

# WEight has high pvalue so remove col 3

features_OLS = features.iloc[:, [0,1,2]]

regressor = sms.OLS(endog= labels, exog= features_OLS).fit()

regressor.summary()

# Heigth has high pvalue so remove col 2

features_OLS = features.iloc[:, [0,1]]

regressor = sms.OLS(endog= labels, exog= features_OLS).fit()

regressor.summary()

# Const has high pvalue so remove col 0

features_OLS = features.iloc[:, [1]]

regressor = sms.OLS(endog= labels, exog= features_OLS).fit()

regressor.summary()
