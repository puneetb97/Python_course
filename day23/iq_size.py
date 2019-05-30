# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:11:08 2019

@author: Puneet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#extracting the data from excel file
df = pd.read_csv("iq_size.csv")
features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)
x = [90,70,150]
x = np.array(x,ndmin = 2)
print("prediction before eleminating the redundent features:",regressor.predict(x))

import statsmodels.api as sm
features = sm.add_constant(features)

#removing unneseccaey features
list1 = [0,1,2,3]
while True:
    features_opt = features[:,list1]
    regressor_ols = sm.OLS(endog=labels,exog=features_opt).fit()
    p = regressor_ols.pvalues
    ind = np.argmax(p)
    if p[ind]>0.05:
        del(list1[ind])
        print(list1)
    else:
        break
    
print ("Output : Brain Size is the only factor which is more useful in predicting intelligence.")

#spliting the data into trainig and testing data
#from sklearn.model_selection import train_test_split
#features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size = 0.2, random_state = 0)

#creating model using linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_opt,labels)
x = [90]
x = np.array(x,ndmin = 2)
print("prediction after eleminating the redundent features:",regressor.predict(x))

#analysing the effectiveness of the model created
plt.scatter(features_opt[:11,],labels[:11,],color = 'red')
plt.plot(features_opt[:11,],regressor.predict(features_opt[:11,]),color='blue')
plt.xlabel("age")
plt.ylabel("size")
plt.show()

#creating model using polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_obj = PolynomialFeatures(degree=5)
features_poly = poly_obj.fit_transform(features_opt)

#spliting the data into trainig and testing data
#from sklearn.model_selection import train_test_split
#features_poly_train,features_poly_test,labels_poly_train,labels_poly_test = train_test_split(features_poly,labels, test_size = 0.2, random_state = 0)

#training data using polynomial regression
regressor2 = LinearRegression()
regressor2.fit(features_poly,labels)

regressor2.predict("prediction by using polynomial regression:",poly_obj.transform(x))

#analysing the effectiveness of the model created
plt.scatter(features_poly[:11,1:2],labels[:11,],color = 'red')
plt.plot(features_poly[:11,1:2],regressor2.predict(features_poly[:11,]),color='blue')
plt.xlabel("age")
plt.ylabel("size")
plt.show()
