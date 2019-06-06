# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:37:13 2019

@author: Puneet
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extracting data
df = pd.read_csv("deliveryfleet.csv")
features = df.iloc[:,1:3].values

#analysing by plotting scatter graph to analyse no. of cluster to form
plt.scatter(features[:,0],features[:,1], color="red")

# creating kmeans model
from sklearn.cluster import KMeans
wcss = []
for i in range(1,6):
    kmeans = KMeans(n_clusters=i, init = "k-means++", random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,6),wcss,color="blue")

print(wcss)
kmeans = KMeans(n_clusters = 2, init = "k-means++", random_state=0)
pred_cluster = kmeans.fit_predict(features)

# plotting the predicted data with featured data
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1], color="red",label="rural")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1], color="green",label="urban")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow")
plt.legend()

# predicting by forming 4 clusters
kmeans1 = KMeans(n_clusters=4, init = "k-means++", random_state=0)
pred_cluster1 = kmeans1.fit_predict(features)

#ploting the predicted data with features
plt.scatter(features[pred_cluster1==0,0],features[pred_cluster1==0,1], color="red")
plt.scatter(features[pred_cluster1==1,0],features[pred_cluster1==1,1], color="green")
plt.scatter(features[pred_cluster1==2,0],features[pred_cluster1==2,1], color="orange")
plt.scatter(features[pred_cluster1==3,0],features[pred_cluster1==3,1], color="purple")
plt.scatter(kmeans1.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow")
plt.legend()

