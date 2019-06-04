# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:19:13 2019

@author: Puneet
"""

import pandas as pd
import numpy as np

#extracting data from excel file
df = pd.read_csv("kc_house_data.csv")
df['date'] = pd.to_numeric(df['date'].apply(lambda x: x[:4]))
df['sqft_above'] = df.fillna(df['sqft_above'].mode())
df = df.drop("id", axis=1)
features = df.drop("price", axis=1).values
labels = df['price'].values

#applying OLS model to remove unnecessary fetaures
import statsmodels.api as sm
features = sm.add_constant(features)

list1 = list(range(0,20))
while True:
    features_opt = features[:,list1]
    regressor_ols = sm.OLS(endog=labels,exog=features_opt).fit()
    p = regressor_ols.pvalues
    ind = np.argmax(p)
    print(ind)
    if p[ind]>0.05:
        del(list1[ind])
        print(list1)
    else:
        break

#now scaling the column data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features_opt)

#spliting data into training and testing data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

#building a linear regression model to predict test data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

#calculating score of the model created
print("printing the score of the linear regression model with train data:",regressor.score(features_train,labels_train))
print("printing the score of the linear regression model with test data:",regressor.score(features_test,labels_test))

from sklearn import metrics
print("the mean square error of the linear model:",metrics.mean_squared_error(labels_test,labels_pred))

#building lasso and ridge model
from sklearn.linear_model import Lasso, Ridge
lasso = Lasso()
ridge = Ridge()

lasso.fit(features_train,labels_train)
ridge.fit(features_train,labels_train)

lasso_pred = lasso.predict(features_test)
ridge_pred = ridge.predict(features_test)

#calculating score of the model created
print("printing the score of the lasso model with train data:",lasso.score(features_train,labels_train))
print("printing the score of the lasso model with test data:",lasso.score(features_test,labels_test))
print("printing the score of the ridge model with train data:",ridge.score(features_train,labels_train))
print("printing the score of the ridge model with test data:",ridge.score(features_test,labels_test))

#calculating mean square error
print("the mean square error of the lasso model:",metrics.mean_squared_error(labels_test,lasso_pred))
print("the mean square error of the linear model:",metrics.mean_squared_error(labels_test,ridge_pred))




 