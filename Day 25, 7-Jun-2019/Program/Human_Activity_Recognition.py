# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:11:29 2019

@author: HIMANSHU SINGH
"""
"""
Q1. Human Activity Recognition

Human Activity Recognition with Smartphones
(Recordings of 30 study participants performing activities of daily living)
(Click Here To Download Dataset): https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip

In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, each person performed
 six activities (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a
 smartphone (Samsung Galaxy S II) on the waist. The experiments have been video-recorded to label the data 
 manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected
 for generating the training data and 30% the test data.

Attribute information 

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:
  (a) a decision tree approach,
  (b) a random forest approach and
  (c) a logistic regression.
  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set.
 Compare the results. Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature 
        selection.
        
"""
import pandas as pd
import numpy as np
import matplotlib as plt

dataset_train = pd.read_csv("train.csv")
dataset_test = pd.read_csv("test.csv")

features_train = dataset_train.iloc[:,0:561]
features_test = dataset_test.iloc[:,0:561]
labels_train = dataset_train.iloc[:,562]
labels_test = dataset_test.iloc[:,562]

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

=================================================================================================

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

=================================================================================================
####################### BEST BEST BEST ##########################################################

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test, labels_pred))
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

===================================================================================================

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test, labels_pred))
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))

=================================================================================================
==================================================================================================

import pandas as pd
import numpy as np
import matplotlib as plt

dataset_train = pd.read_csv("train.csv")
dataset_test = pd.read_csv("test.csv")

features_train = dataset_train.iloc[:,0:561].values
features_test = dataset_test.iloc[:,0:561].values
labels_train = dataset_train.iloc[:,562].values
labels_test = dataset_test.iloc[:,562].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train= labelencoder.fit_transform(labels_train)
labels_test = labelencoder.fit_transform(labels_test)


import statsmodels.api as sm
features_train = sm.add_constant(features_train)
features_test = sm.add_constant(features_test)
cols = list(range(562))
while True:
    features_opt = features_train[:,cols]
    regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
    listt = list(regressor_OLS.pvalues)
    val = max(listt)
    if val > 0.05:
        indexx = listt.index(val)
        del(cols[indexx])
        features_train = np.delete(features_train, indexx, 1)
        features_test = np.delete(features_test, indexx, 1)
    else:
        break

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))













