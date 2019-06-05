# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:33:47 2019
@author: Narayan Devpura
"""
"""
Create a program that fulfills the following specification.
PastHires.csv
Here, we are building a decision tree to check if a person is hired or not based on certain predictors.
Import PastHires.csv File.
scikit-learn needs everything to be numerical for decision trees to work.
So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.
Build and perform Decision tree based on the predictors and see how accurate your prediction 
is for a being hired.
Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:
Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, 
having Bachelor's Degree without Internship.
Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, 
having Master's Degree with Internship.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Reading data
df = pd.read_csv('material/PastHires.csv')

# checking data
df.isnull().any(axis = 0)
df['Level of Education'].value_counts()

# features and lbels
X = df.drop('Hired', axis = 1).values
y = df['Hired'].values

# Applying label encoding

cols = [1, 3, 4, 5]
lab_enc = []

for i in range(len(cols)):
    label_encoder = LabelEncoder()
    lab_enc.append(label_encoder)

for col, LE in zip(cols,lab_enc):
    X[:,col] = LE.fit_transform(X[:,col])

LE = LabelEncoder()
y = LE.fit_transform(y)

# Employee1
emp1 = [10, 'Y', 4, 'BS', 'Y', 'N']
emp1 = np.array(emp1).reshape(1, -1)
for col, LE in zip(cols,lab_enc):
    emp1[:,col] = LE.transform(emp1[:,col])

# Employee2
emp2 = [10, 'N', 4, 'MS', 'N', 'Y']
emp2 = np.array(emp2).reshape(1, -1)
for col, LE in zip(cols,lab_enc):
    emp2[:,col] = LE.transform(emp2[:,col])

# performing Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(random_state= 0)
DTC.fit(X, y)

# prediction through DTC
emp1_predD = LE.inverse_transform(DTC.predict(emp1))
emp2_predD = LE.inverse_transform(DTC.predict(emp2))

if emp1_predD[0] == 'Y':
    print("Employee1 will be hired")
else:
    print("Employee1 will not be hired")
    
if emp2_predD[0] == 'Y':
    print("Employee1 will be hired")
else:
    print("Employee1 will not be hired")
    
# performin Random Forest Model
from sklearn.ensemble import RandomForestClassifier
RTC = RandomForestClassifier(n_estimators= 10, random_state= 0)
RTC.fit(X, y)

# prediction through RTC
emp1_predR = LE.inverse_transform(RTC.predict(emp1))
emp2_predR = LE.inverse_transform(RTC.predict(emp2))

if emp1_predR[0] == 'Y':
    print("Employee1 will be hired")
else:
    print("Employee1 will not be hired")

if emp2_predR[0] == 'Y':
    print("Employee1 will be hired")
else:
    print("Employee1 will not be hired"

