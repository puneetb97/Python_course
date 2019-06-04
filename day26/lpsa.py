# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:56:21 2019

@author: Puneet
"""

import pandas as pd
import numpy as np

#extracting data
df = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter = " ")
features = df.iloc[:,0:-1].values
labels = df.iloc[:,-1].values

#spiting features and labels in training and test data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state=0)

#creating an linear model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

#score of the model created
print("score of the model created with train data:",regressor.score(features_train,labels_train))
print("score of the model created with test data:",regressor.score(features_test,labels_test))

labels_pred = regressor.predict(features_test)

# mean square error of the model created
from sklearn import metrics
print("mean square error of the linear model created:",metrics.mean_squared_error(labels_test,labels_pred))

#using regulariztion model
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

regressor_lasso = Lasso()
regressor_ridge = Ridge()
regressor_elasticnet = ElasticNet()

regressor_lasso.fit(features_train,labels_train)
regressor_ridge.fit(features_train,labels_train)
regressor_elasticnet.fit(features_train,labels_train)

labels_lasso = regressor_lasso.predict(features_test)
labels_ridge = regressor_ridge.predict(features_test)
labels_elasticnet = regressor_elasticnet.predict(features_test)

#calculating score of regularization model created
print("mean square error of lasso model:",metrics.mean_squared_error(labels_test,labels_lasso))
print("maen quare error of ridge model:",metrics.mean_squared_error(labels_test,labels_ridge))
print("maen quare error of ridge model:",metrics.mean_squared_error(labels_test,labels_elasticnet))

#-------------------------------------------------------------------------------------------
mean = df["lpsa"].mean()
labels = np.where(labels<mean,0,labels)
labels = np.where(labels >= mean,1,labels)

from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test = train_test_split(features,labels, test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(f_train,l_train)

l_pred = classifier.predict(f_test)

print("mean square error of Random forest model:",metrics.mean_squared_error(l_test,l_pred))
print(pd.DataFrame({"l_test":l_test,"l-pred":l_pred}))




