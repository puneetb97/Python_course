# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:36:29 2019

@author: Puneet
"""
import numpy as np
x = np.array([1,2,3], ndmin=3, dtype= np.float)
print(x)
print(x.shape)
print(x.dtype)
print(x.size)
print(x.ndim)
print(x.itemsize)
print(x.nbytes)
print(x.strides)