# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:59:50 2019
@author: Narayan Devpura
"""

"""
tree_addhealth.csv
Q1. (Create a program that fulfills the following specification.)
For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, 
an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:
http://www.cpc.unc.edu/projects/addhealth/.
This large data set is available online from the University of North Carolina’s Carolina Population Center, 
http://www.cpc.unc.edu/projects/addhealth/data.
 
Import tree_addhealth.csv
 
The attributes are:
 
BIO_SEX: 1 = male 0 = female    
HISPANIC: 1=Yes,0=No    
WHITE : 1=Yes,0=No
BLACK : 1=Yes,0=No          
NAMERICAN: 1=Yes,0=No                      
ASIAN: 1=Yes,0=No                      
ALCEVR1: ever drank alcohol(1=Yes,0=No)   
marever1: ever smoked marijuana(1=Yes,0=No)    
cocever1: ever used cocaine(1=Yes,0=No)                
inhever1: ever used inhalants(1=Yes,0=No)             
cigavail: cigarettes available in home(1=Yes,0=No)
PASSIST: parents or public assistance(1=Yes,0=No)
EXPEL1: ever expelled from school(1=Yes,0=No)
TREG1: Ever smoked regularly(1=Yes,0=No)
Explanatory Variables:
Age
ALCPROBS1:alcohol problems 0-6
DEP1: depression scale
ESTEEM1: self esteem scale       
VIOL1:violent behaviour scale
DEVIANT1: deviant behaviour scale     
SCHCONN1: school connectedness scale       
GPA1: gpa scale  4 points)
FAMCONCT: family connectedness scale       
PARACTV:parent activities scale
PARPRES:parental presence scale
 
        Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: 
        gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use, 
        alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, 
        depression, and self-esteem.
    Build a classification tree model evaluation if an adolescent gets expelled or not from school based 
    on their Gender and violent behavior.
    Use random forest in relation to regular smokers as a target and explanatory variable specifically 
    with Hispanic, White, Black, Native American and Asian.
(Please make confusion matrix and also check accuracy score for each and every section)
"""

import pandas as pd
import numpy as np
import seaborn as sns

# Reading data
df = pd.read_csv('material/tree_addhealth.csv')

# cheching data for null values
sns.heatmap(df, cmap='viridis')
df.isnull().any(axis = 0)
df.info()

# handling null values
for i in df:
    df[i] = df[i].fillna(int(df[i].mean()))

#  Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: 
#  gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use,
#  alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, 
#  depression, and self-esteem.
    
# features and labels

X = df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
y = df.iloc[:,7].values

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state= 0)

# performing Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(random_state=0)
DTC.fit(X_train, y_train)
y_predD1 = DTC.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cD1 = confusion_matrix(y_test, y_predD1)

# Score of DTC
score_D1 = DTC.score(X_test, y_test)
print("Accuracy of model: ",score_D1 * 100)



#  Build a classification tree model evaluation if an adolescent gets expelled or not from school based 
#  on their Gender and violent behavior.

# features and columns
X = df.iloc[:,[0,-9]].values
y = df.iloc[:,-4].values

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state= 0)

# performing Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(random_state=0)
DTC.fit(X_train, y_train)
y_predD2 = DTC.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cD2 = confusion_matrix(y_test, y_predD2)

# Score of DTC
score_D2 = DTC.score(X_test, y_test)
print("Accuracy of model: ",score_D2 * 100)



# Use random forest in relation to regular smokers as a target and explanatory variable specifically 
# with Hispanic, White, Black, Native American and Asian.

# features and labels
X = df.iloc[:,[1,2,3,4,5]].values
y = df.iloc[:,7].values

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state= 0)

# performing Decision Tree Model
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(n_estimators= 20 ,random_state=0)
RFC.fit(X_train, y_train)
y_predD2 = RFC.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cR = confusion_matrix(y_test, y_predD2)

# Score of DTC
score_R = RFC.score(X_test, y_test)
print("Accuracy of model: ",score_R * 100)

