# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:29:47 2019

@author: Puneet
"""

from collections import OrderedDict
od = OrderedDict()
input_string = input("enter string:")
for i in input_string:
    od[i] = od.get(i,0) + 1
print(od)