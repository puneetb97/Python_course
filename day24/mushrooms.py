# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:26:34 2019

@author: Puneet
"""

import numpy as np
import pandas as pd

#extracting data 
df = pd.read_csv("mushrooms.csv")
features = df.iloc[:,[5,21,22]].values
labels = df.iloc[:,0:1].values

#changing the categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in range(len(features[0])):
    features[:,i] = labelencoder.fit_transform(features[:,i])

labels = labelencoder.fit_transform(labels)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0,1,2])
features = onehotencoder.fit_transform(features).toarray()

#eleminating the dummy variables
features = features[:,[1,2,3,4,5,7,8,9,10,11,12,14,15,16,17,18,19,20,21]]


#scaling all the features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size = 0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(features_train,labels_train)

label_pred = regressor.predict(features_test)


print("score of the logistic model created:",regressor.score(features_test,labels_test)*100,"%")

#applying knn classificatin to check wheather it gives optimal model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier.fit(features_train, labels_train)


label1_pred = classifier.predict(features_test)

print("score of the knn model created:",classifier.score(features_test,labels_test)*100,"%")