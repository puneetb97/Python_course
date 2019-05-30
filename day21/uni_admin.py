# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:35:47 2019

@author: Puneet
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("University_data.csv")
features = df.iloc[:,0:6].values
labels = df.iloc[:,-1].values

labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

features = features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_tests = train_test_split(features,labels, test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)
result = regressor.predict(features_test)

print(pd.DataFrame(labels_tests,result))

import matplotlib.pyplot as plt
plt.scatter(features_test[:,0],labels_tests, color='red')
plt.plot(features_test[:,0],result,color='blue')

x = [0,0,1,0,320,4,4,8.15,0]
x = np.array(x,ndmin=2)
print(regressor.predict(x))