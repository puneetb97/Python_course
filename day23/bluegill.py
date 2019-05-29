# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:38:55 2019

@author: Puneet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bluegills.csv")
features = df.iloc[:,0:1].values
labels = df.iloc[:,1]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size = 0.3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict([[5]]) 

plt.scatter(features_train,labels_train, color='red')
plt.plot(features_train,regressor.predict(features_train))


from sklearn.preprocessing import PolynomialFeatures
pol_obj = PolynomialFeatures(degree=4)

features_pol = pol_obj.fit_transform(features)

regressor.fit(features_pol,labels)
regressor.predict(pol_obj.fit_transform([[5]]))