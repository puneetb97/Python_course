# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:13:19 2019

@author: Puneet
"""

import numpy as np
import pandas as pd

#extracting data 
df = pd.read_csv("Auto_mpg.txt", delimiter="\s+", names = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])
a = df['mpg'].idxmax()
print("car name with highest mpg value is",df.iloc[a,-1])
df = df.replace('?','0')
df['horsepower'] = pd.to_numeric(df['horsepower']) 

features = df.iloc[:,1:-1].values
labels = df.iloc[:,0].values

#sclaing the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

#splitting data into training and testing
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size=0.1, random_state=0)

#creating decision tree model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(features_train,labels_train)

b = regressor.score(features_test,labels_test)

#calculating the score of decision model created
print("score of decision model created",regressor.score(features_test,labels_test))

#creating random forest model
from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators=25 , random_state=0 )
regressor1.fit(features_train,labels_train)

c = regressor1.score(features_test,labels_test)

#calculating the score of decision model created
print("score of decision model created",regressor1.score(features_test,labels_test))

if b>c:
    print("Decision tree model is better")
else:
    print("Random forest model is better")
    
# resulting data of a sample
x = [6,215,100,2630,22.2,80,3]
x = np.array(x,ndmin=2)
y = sc.transform(x)
print("result of the sample using decision tree:",regressor.predict(y))
print("result of the sample using random forest:",regressor1.predict(y))

