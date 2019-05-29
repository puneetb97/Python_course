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
x = [0,0,1150,3,4]
x = np.array(x)
regressor.predict(x.reshape(1, -1))