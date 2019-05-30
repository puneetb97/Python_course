# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:18:14 2019

@author: Puneet
"""

import numpy as np
input_string = input("enter input data:")
input_list = input_string.split(" ")
input_list1 = list(map(lambda a:int(a),input_list))
x = np.array(input_list1, ndmin=2).reshape(3,3)
print(x)