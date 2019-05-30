# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:54:55 2019

@author: Puneet
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(150,20,10,dytpe = int)
plt.hist(x,100)
plt.show
print("variance is:",(np.std(x))**2)
print("standard deviation is:",np.std(x))
