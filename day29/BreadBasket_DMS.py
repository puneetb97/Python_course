# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:42:02 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#extracting data from csv file
df = pd.read_csv("BreadBasket_DMS.csv")
tran_no = df["Transaction"].unique().tolist()

#analysing the highest 15 saling items
null_index = df.index[df["Item"]=="NONE"].tolist() 
df = df.drop(null_index,axis=0)
top = df["Item"].value_counts().head(15)
name = top.index.tolist()
plt.pie(top,labels = name,autopct="%1.1f%%",radius=2)


"""transaction = []
for i in tran_no:
    new_list = []
    for j in range(0,21293):
        if df.iloc[j,2] == i:
            new_list.append(df.iloc[j,3])
    transaction.append(new_list)
"""
transactions = []
df.groupby("Transaction")["Item"].apply(lambda x: transactions.append(list(set(x))))

#building an association model by apriori
from apyori import apriori
rules = apriori(transactions, min_support=0.0025, min_confidence=0.2, min_lift=3)
result = list(rules) 

for item in result:
    print("association:",item[0])