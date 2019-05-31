# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:20:34 2019

@author: Puneet
"""

import numpy as np
import pandas as pd

#extracting data from a csv file
df = pd.read_csv("PastHires.csv")


#dealing with the categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
for i in [1,3,4,5,6]:
    df.iloc[:,i] = labelencoder.fit_transform(df.iloc[:,i])
    
features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

#spliting data into training and testing data set    
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size=0.2, random_state=0)

#applying decision tree model
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(features_train,labels_train)

#score of the decision model created
print("score of the decision model created:",classifier.score(features_test,labels_test))

#applying Random Forest model
from sklearn.ensemble import RandomForestClassifier
classifier1 = RandomForestClassifier(n_estimators = 10, random_state = 0)
classifier1.fit(features_train,labels_train)

#score of the random forest model created
print("score of the random forest model created:",classifier1.score(features_test,labels_test))

#predicting the result based on data given
x = [10,1,4,0,1,0]
y = [10,0,4,1,0,1]
x = np.array(x , ndmin = 2)
y = np.array(y , ndmin = 2)
print("prediction from decision tree model of sample1:",classifier.predict(x))
print("prediction from random forest model of sample1:",classifier.predict(x))
print("prediction from decision tree model of sample2:",classifier1.predict(y))
print("prediction from random forest model of sample2:",classifier1.predict(y))
