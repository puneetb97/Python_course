# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:01:37 2019

@author: Puneet
"""

import numpy as np
import pandas as pd

#extracting the dataset
df = pd.read_csv("affairs.csv")
features = df.iloc[:,0:8].values
labels = df.iloc[:,8].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[6,7])
features = onehotencoder.fit_transform(features).toarray()

features = features[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]

#spliting data into training and testing data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size = 0.1, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#applying linear regression model
from sklearn.linear_model import LogisticRegression
regression = LogisticRegression()
regression.fit(features_train,labels_train)
labels_pred = regression.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
print("confusion matrix is:",confusion_matrix(labels_test, labels_pred))

print("score of the model created:",regression.score(features_test,labels_test))

print("percentage of women having affair:",df['affair'].value_counts(normalize=True)[1])

x = [3,25,3,1,4,14,4,2]
x = np.array(x , ndmin=2)
y = onehotencoder.transform(x).toarray()
y = y[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]] 
result = regression.predict(sc.transform(y))
print(" prediction for a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer is:",result)

