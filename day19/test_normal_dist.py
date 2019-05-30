# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:08:53 2019

@author: Puneet
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#opening csv file
with open("human_body_temperature.csv",mode = "rt") as file:
    data = file.readlines()
    
#deleting column name from etracted data
del(data[0])

#creating list of temperature
list1 = []
for i in data:
    a = i.split(",")
    list1.append(a[0])
    
#creating array of data
x = np.array(list1, dtype = float)
plt.hist(x,7)
plt.show
print("mean is:",np.mean(x))
print("median is",np.median(x))
print("mode is",stats.mode(x))


    