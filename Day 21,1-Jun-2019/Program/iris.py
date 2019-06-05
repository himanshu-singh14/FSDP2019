# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:24:34 2019

@author: HIMANSHU SINGH
"""
"""

Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of
    Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features of iris flower and
    one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm 
classifier and use the trained svm model to predict the Iris species type. To begin with let’s
try to load the Iris dataset.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets 
iris = datasets.load_iris()
iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
iris_df['species_type']= iris.target
iris_df.isnull().any(axis=0)

features = iris_df.iloc[:, 0:4].values
labels = iris_df.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Feature Scaling may be applied

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf

#################################### Here Linear is best for this problem
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(labels_test, labels_pred)
ac = accuracy_score(labels_test, labels_pred)
print(cm)
print(ac)
# Model Score
score = classifier.score(features_test,labels_test)
print(score)

