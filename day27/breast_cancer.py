# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:46:25 2019

@author: Puneet
"""
import pandas as pd
import numpy as np

#extracting data from csv file
df = pd.read_csv("breast_cancer.csv")
df.isnull().any()

#dealing with null values
df["G"] = df["G"].fillna(method = "ffill")
df.isnull().any()

features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values



#spliting data into training and testing data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size=0.1, random_state=0)

#performing svm classification model
from sklearn.svm import SVC
classifier = SVC(kernel = "poly", random_state=0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test).tolist()
result = []
for i in labels_pred:
    if i==2:
        result.append("non_cancerous")
    else:
        result.append("cancerous")
result = np.array(result)
print(result)

#calculating score of created model
print("score of the SVC model with train data:",classifier.score(features_train,labels_train))
print("score of the SVC model with test data:",classifier.score(features_test,labels_test))

#prediction for a sample data
x = [6,2,5,3,2,7,9,2,4]
x = np.array(x,ndmin=2)
pred = classifier.predict(x)
if pred==4:
    print("malignant tumor")
else:
    print("Benign tumor")