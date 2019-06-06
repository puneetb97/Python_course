# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:42:44 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extracting data from csv file
df = pd.read_csv("tshirts.csv")

features = df.iloc[:,1:].values

# analysing the no of cluster to form using k-means
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)        

plt.plot(range(1,11),wcss,color="blue")

# creating model with 3 clusters
kmeans = KMeans(n_clusters=3, init = "k-means++", random_state=0)
pred_cluster = kmeans.fit_predict(features)

#ploting the predicted cluster on the graph
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="red")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="green")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="blue")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow")

# results
print("the average size for small size clothing:",kmeans.cluster_centers_[:,1][2])
print("the average size for medium size clothing:",kmeans.cluster_centers_[:,1][0])
print("the average size for large size clothing:",kmeans.cluster_centers_[:,1][1])