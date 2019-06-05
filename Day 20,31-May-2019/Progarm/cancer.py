# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:02:34 2019

@author: HIMANSHU SINGH
"""
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")
This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter="\s+")

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

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

print (np.mean(dataset.values[:,1]))

----------------------------------------------------------------------------------------------


from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(features_test,labels_test)*100,2))

#Predict on test and training data

predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics

print ("Lasso Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.sqrt(np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2)))

print ("ElasticNet Root Mean Square Error (MSE) for TEST data is")
print (np.sqrt(np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2)))

-------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter="\s+")

avg = np.mean(dataset['lpsa'])
dataset['lpsa'] = dataset['lpsa'].apply(lambda x : 1 if x > avg else 0)

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

score = accuracy_score(labels_test , labels_pred)
print(score)
