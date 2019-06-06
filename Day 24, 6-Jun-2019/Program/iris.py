# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:22:08 2019

@author: HIMANSHU SINGH
"""
"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica
 and Iris versicolor).

    Four features were measured from each sample: the length and the width of the sepals and petals, in
    centimetres (iris.data). Import the iris dataset already in sklearn module using the following command:\

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.

"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
from sklearn.datasets import load_iris
iris = load_iris()
dataset = iris.data
features = dataset[:, 0:4]

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_


plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

from sklearn.metrics import silhouette_score

for n_clusters in range(2, 11):
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(features)
    centers = clusterer.cluster_centers_

    score = silhouette_score (features, preds, metric='euclidean')
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", score)

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()


