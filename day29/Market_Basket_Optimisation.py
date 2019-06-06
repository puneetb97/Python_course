# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:33:50 2019

@author: Puneet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori
from collections import OrderedDict

# extracting data from csv file
df = pd.read_csv("Market_Basket_Optimisation.csv", header = None)

transactions = df.apply(lambda x: x.dropna().tolist(),axis=1).tolist()

#building the association model using apriori method
rules = apriori(transactions, min_support=0.0025,min_confidence=0.2, min_lift=3)
result = list(rules)
for item in result:
    print("association is:",item[0])

# annalysing the highest purchasing items
dict1 = OrderedDict()
def count(x):
    for i in x:
        dict1[i] = dict1.get(i,0) +1
df.apply(lambda x:count(x),axis=0)

del dict1[np.nan]
items = []
values = []
for key, value in sorted(dict1.items(), key = lambda item:item[1]):
    items.append(key)
    values.append(value)
    
#visualizing the top 10 selling edibles
index = range(0,10)
plt.bar(items[110:],values[110:])
plt.xticks(index,items[110:],fontsize=10,rotation=90)

