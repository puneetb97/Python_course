# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:10:36 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Foodtruck.csv")
features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values
regressor = LinearRegression()
regressor.fit(features,labels)
x = np.array([3.073,], ndmin = 2)
print(x)
regressor.predict(x)

