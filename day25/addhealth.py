# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:31:33 2019

@author: Puneet
"""

import pandas as pd
import numpy as np

#extracting data
df = pd.read_csv("tree_addhealth.csv")
df = df.fillna(df.max())
features = df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels = df.iloc[:,7].values


#spliting data into training and testing data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size = 0.2, random_state = 0)

# scaling all the colunms normally
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#creating decision tree model for prediction
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(features_train,labels_train)



features1 = df[["BIO_SEX", "VIOL1"]].values
labels1 = df["EXPEL1"].values
features_train1,features_test1,labels_train1,labels_test1 = train_test_split(features1,labels1, test_size = 0.2, random_state = 0)
sc1 = StandardScaler()
features_train1 = sc1.fit_transform(features_train1)
features_test1 = sc1.transform(features_test1)

classifier2 = DecisionTreeClassifier()
classifier2.fit(features_train1,labels_train1)

label_pred2 = classifier2.predict(features_test1)
from sklearn.metrics import confusion_matrix
print("confusion matrix for decision tree model is:",confusion_matrix(labels_test1,label_pred2))

print("score of decision tree model which determine wheather a child is expelled from school on basis of gander:",classifier2.score(features_test1,labels_test1))



#predicting the data by the model created
labels_pred = classifier.predict(features_test)

#creating confusion matrix
from sklearn.metrics import confusion_matrix
print("confusion matrix for decision tree model is:",confusion_matrix(labels_test,labels_pred))

#score of Decision tree model
print("score of decision tree model:",classifier.score(features_test,labels_test))

#creating Random forest model
from sklearn.ensemble import RandomForestClassifier
classifier1 = RandomForestClassifier(n_estimators = 20, random_state=0)
classifier1.fit(features_train,labels_train)

labels_pred1 = classifier1.predict(features_test)

#creating confusion matrix
print("confusion matrix for random forest model is:",confusion_matrix(labels_test,labels_pred1))

#score of Decision tree model
print("score of decision tree model:",classifier.score(features_test,labels_test))


