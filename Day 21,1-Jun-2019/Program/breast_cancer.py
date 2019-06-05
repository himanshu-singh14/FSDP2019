# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:34:52 2019

@author: HIMANSHU SINGH
"""
"""
Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

 Impute the missing values with the most frequent values.
 Perform Classification on the given data-set to predict if the tumor is cancerous or not.[6,2,5,3,2,7,9,2,4]
 Check the accuracy of the model.
 Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv", delimiter=",")
dataset.isnull().any(axis=0)

dataset["G"] = dataset["G"].fillna(dataset["G"].mode()[0])

features = dataset.iloc[:, 1:10].values
labels = dataset.iloc[:, 10].values

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

x = [6,2,5,3,2,7,9,2,4]
x = np.array(x)
classifier.predict(x.reshape(1, -1))[0]


-----------------------------------------------------------------------------------------

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(dataset, test_size=0.5, random_state=0)

####################################### It is best in this Problem in Naive_bayes
gnb = GaussianNB()
used_features =["B","C","D","E","F","G","H","I","J"]

# Train classifier
gnb.fit(
    features_train[used_features].values,
    features_train["K"].values
)
labels_pred = gnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm_gnb = confusion_matrix(features_test["K"], labels_pred)
ac_mnb = accuracy_score(features_test["K"], labels_pred)
print(cm_gnb)
print(ac_mnb)

----------------------------------------------------

mnb = MultinomialNB()

mnb.fit(
    features_train[used_features].values,
    features_train["K"].values
)
labels_pred = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm_mnb = confusion_matrix(features_test["K"], labels_pred)
ac_mnb = accuracy_score(features_test["K"], labels_pred)
print(cm_mnb)
print(ac_mnb)

--------------------------------------------------------

bnb = BernoulliNB()

bnb.fit(
    features_train[used_features].values,
    features_train["K"].values
)
labels_pred = bnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm_bnb = confusion_matrix(features_test["K"], labels_pred)
ac_bnb = accuracy_score(features_test["K"], labels_pred)
print(cm_bnb)
print(ac_bnb)
