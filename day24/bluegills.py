# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:20:09 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extracting the data from excel file
df = pd.read_csv("bluegills.csv")
features = df.iloc[:,:-1].values
labels = df.iloc[:,1].values

#spliting the data into trainig and testing data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size = 0.1, random_state = 0) 

#creating model using linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

#analysing the effectiveness of the model created
plt.scatter(features_test,labels_test,color = 'red')
plt.plot(features_test,regressor.predict(features_test),color='blue')
plt.xlabel("age")
plt.ylabel("size")

#creating model using polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_obj = PolynomialFeatures(degree=5)
features_poly = poly_obj.fit_transform(features)

#spliting the data into trainig and testing data
from sklearn.model_selection import train_test_split
features_poly_train,features_poly_test,labels_poly_train,labels_poly_test = train_test_split(features_poly,labels, test_size = 0.1, random_state = 0)

#training data using polynomial regression
regressor2 = LinearRegression()
regressor2.fit(features_poly_train,labels_poly_train)


#analysing the effectiveness of the model created
plt.scatter(features_poly_test[:,0],labels_poly_test,color = 'red')
plt.plot(features_poly_test[:,0],regressor2.predict(features_poly_test),color='blue')
plt.xlabel("age")
plt.ylabel("size")
 