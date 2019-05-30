# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:35:36 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
df = pd.read_csv("Female_Stats.csv")
features = df.iloc[:,1:3].values
labels = df.iloc[:,0].values




import statsmodels.api as sm
features = sm.add_constant(features)

#removing unneseccaey features
list1 = [0,1,2]
while True:
    features_opt = features[:,list1]
    regressor_ols = sm.OLS(endog=labels,exog=features_opt).fit()
    p = regressor_ols.pvalues
    print(p)
    ind = np.argmax(p)
    print(ind)
    if p[ind]>0.05:
        del(list1[ind])
        print(list1)
    else:
        break

#checking which feature is affecting the label upto which extent
data = regressor_ols.params.tolist()
print("The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height:",data[1])
print("The Average Student Height Increases By How Many Inches For Each One-Inch Increase In father's Height:",data[2])

    
