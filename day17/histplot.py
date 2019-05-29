# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:30:03 2019

@author: Puneet
"""

import matplotlib.pyplot as plt 
customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1]
bins = [25,30,35,40,45,55]
plt.hist(customerWaitTime,bins=bins,alpha = 0.5)
plt.axis([25,60,0,7])
plt.xlabel("seconds")
plt.ylable("customers")
plt.savefig("histplot.jpg")

