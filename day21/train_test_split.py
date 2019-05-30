# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:24:22 2019

@author: Puneet
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Income_data.csv")
features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
regressor = LinearRegression()
regressor.fit(feature_train,label_train)
a = regressor.predict(feature_test)
plt.scatter(feature_test,label_test, color = 'red')
plt.plot(feature_test, a, color = 'blue')
plt.show()
