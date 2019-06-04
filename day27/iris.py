# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:53:09 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
from sklearn import datasets

#extracting data from sklearn library
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["type"] = iris.target

features = df.drop("type", axis=1).values
labels = df["type"].values

#spliting data into training set and test set
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size=0.1, random_state=0)

#creating svm model for prediction
from sklearn.svm import SVC
classifier = SVC(kernel = "rbf", random_state=0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

#creating confusion metrics of the model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)

#score of the model created 
print("score of the svm model created with train data:",classifier.score(features_train,labels_train))
print("score of the svm model created with test data:",classifier.score(features_test,labels_test))

#---------------------------------------------------------------------------------------------------------------
#by naive bayes model
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
gnb = GaussianNB()
bnb = BernoulliNB()
mnb = MultinomialNB()
gnb.fit(features_train,labels_train)
bnb.fit(features_train,labels_train)
mnb.fit(features_train,labels_train)

labels_gnb = gnb.predict(features_test)
labels_bnb = bnb.predict(features_test)
labels_mnb = mnb.predict(features_test)

print("score of the GaussianNB model created with train data:",gnb.score(features_train,labels_train))
print("score of the GaussianNB model created with test data:",gnb.score(features_test,labels_test))

print("score of the BernoulliNB model created with train data:",bnb.score(features_train,labels_train))
print("score of the BernoulliNB model created with test data:",bnb.score(features_test,labels_test))

print("score of the MultinomiaNB model created with train data:",mnb.score(features_train,labels_train))
print("score of the MultinomiaNB model created with test data:",mnb.score(features_test,labels_test))