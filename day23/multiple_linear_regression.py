# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:44:35 2019

@author: Puneet
"""

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Classification.csv')
temp = dataset.values
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Predicting the Test set results
Pred = regressor.predict(features_test)
print(Pred)

import statsmodels.formula.api as sm
features = np.append(arr = np.ones((30,1)),values = features, axis = 1)


index = [0,1,2,3,4,5]
while True:
    features_opt = features[:,index]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    p = regressor_OLS.pvalues
    ind = np.argmax(p)
    if p[ind]>0.05:
        del(index[ind])
        print(index)
    else:
        break

features_train1, features_test1, labels_train1, labels_test1 = train_test_split(features_opt, labels, test_size = 0.2, random_state = 0)

score1 = regressor.score(features_test,labels_test)
regressor.fit(features_train1,labels_train1)
score2 = regressor.score(features_test1,labels_test1)
print(score1)
print(score2)

    
    
    