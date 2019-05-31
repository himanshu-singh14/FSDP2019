# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:38:29 2019

@author: HIMANSHU SINGH
"""
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students


Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""

#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_csv('Female_Stats.csv') 

#prepare the data to train the model
features = dataset.iloc[:,1:3].values 

"""
mom = dataset.iloc[:,1:2].values  #mom
dad = dataset.iloc[:,2:3].values  #dad
"""

labels = dataset.iloc[:,0:1].values 

dataset.isnull().any(axis=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)
"""
from sklearn.linear_model import LinearRegression
regressormom = LinearRegression()
regressormom.fit(mom, labels)

from sklearn.linear_model import LinearRegression
regressordad = LinearRegression()
regressordad.fit(dad, labels)
"""

print(regressor.intercept_)  
print (regressor.coef_)

plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(features), color = 'blue')
plt.show()
"""
plt.scatter(mom, labels, color = 'red')
plt.plot(mom, regressormom.predict(mom), color = 'blue')
plt.scatter(dad, labels, color = 'blue')
plt.plot(dad, regressordad.predict(dad), color = 'red')
plt.show()

"""
x = [60,67]
out = np.array(x).reshape(1,-1)
print(regressor.predict(out))

-----------------------------------------------------------------------

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 100)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

print(lin_reg_2.predict(poly_object.transform(out)))

-----------------------------------------------------------------------

import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

print(regressor_OLS.pvalues)

print (regressor.coef_)







