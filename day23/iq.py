# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:02:46 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
df = pd.read_csv("iq_size.csv")
features = df.iloc[:,1:4].values
labels = df.iloc[:,0].values

regressor = LinearRegression()
regressor.fit(features,labels)
regressor.predict([[90,70,150]])

import statsmodels.formula.api as sm
features = np.append(arr=np.ones((38,1)), values=features, axis=1)

index = [0,1,2,3]
while(True):
    features_opt = features[:,index]
    regressor_OLS = sm.OLS(endog=labels, exog=features_opt).fit()
    p = regressor_OLS.pvalues
    print(p)
    ind = np.argmax(p)
    print(ind)
    if(p[ind]>0.05):
        del(index[ind])
        print(index)
    else:
        break

regressor.fit(features_opt,labels)
regressor.predict([[90]])