# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:59:48 2019
@author: Narayan Devpura
"""

"""
Q2. (Create a program that fulfills the following specification.)
mushrooms.csv
Import mushrooms.csv file
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.
 
Attribute Information:
classes: edible=e, poisonous=p (outcome)
cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
bruises: bruises=t, no=f
odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
gill-attachment: attached=a,descending=d,free=f,notched=n
gill-spacing: close=c,crowded=w,distant=d
gill-size: broad=b,narrow=n\
gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,
green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
stalk-shape: enlarging=e,tapering=t
stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
veil-type: partial=p,universal=u
veil-color: brown=n,orange=o,white=w,yellow=y
ring-number: none=n,one=o,two=t
ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d
Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.
(you can perform on habitat, population and odor as the predictors)
Check accuracy of the model.
"""

import pandas as pd

full_df = pd.read_csv('material/mushrooms.csv')

# required df
df = full_df.iloc[:,[0,5,21,22]]
df.isnull().any(axis = 0)

# features and labels
X = df.iloc[:, 1:].values
y = df.iloc[:, 0:1].values

# Applying Label Encoding
from sklearn.preprocessing import LabelEncoder
cols = [0, 1, 2]
lab_enc = []

for i in range(len(cols)):
    label_encoder = LabelEncoder()
    lab_enc.append(label_encoder)

for col, LE in zip(cols,lab_enc):
    X[:,col] = LE.fit_transform(X[:,col])

LE = LabelEncoder()
y = LE.fit_transform(y)


# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 101)


# Applying LogisticRegression
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train, y_train)
y_pred = log.predict(X_test)
print("Accuracy of Logistic Model: ",log.score(X_test, y_test) * 100)


# Finding confusion_matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print("Confusion matrix of LR Model: ", cm)


# Applying KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_preds = knn.predict(X_test)
print("Accuacy of KNN Model: ", knn.score(X_test, y_test) * 100)


# Finding confusion_matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_preds)
print("Confusion matrix of KNN Model: ", cm)

