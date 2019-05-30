# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:39:57 2019

@author: Puneet
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
print("mean before adding outliers",np.mean(incomes))
print("median before adding outliners",np.median(incomes))
plt.hist(incomes,50)
plt.show
incomes = np.append(incomes,[100000000])
print("mean after adding outliers",np.mean(incomes))
print("median after adding outliers",np.median(incomes))

