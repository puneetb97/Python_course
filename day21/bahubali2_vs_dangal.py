# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:42:54 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Bahubali2_vs_Dangal.csv")
features = df.iloc[:,0:1].values
label = df.iloc[:,1:].values

regressor = LinearRegression()
regressor.fit(features,label)
x = np.array([10] , ndmin=2)
data = regressor.predict(x)
if data[0][0] > data[0][1]:
    print("bahubali2 is earning more")
else:
    print("dangal is earning more")

