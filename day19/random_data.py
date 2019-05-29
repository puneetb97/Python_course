# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:04:15 2019

@author: Puneet
"""

import numpy as np
from scipy import stats
from collections import Counter

x = np.random.randint(5,15,40)
print(x)
a = stats.mode(x)
print("using numpy mode is:",a)
dict1 = Counter(x)
print(dict1)
list1 = []
list2 = []
for key,value in dict1.items():
    list1.append(value)
    list2.append(key)
maximum = max(list1)
b= list1.index(maximum)
print("mode without using numpy is:",list2[b])