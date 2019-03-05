# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:22:11 2019

@author: Puneet
"""
# taking radius from user
radius = float(input("enter radius:"))
# calculating area and parameter
import math
area = math.pi*radius**2
parameter = 2*math.pi*radius
print("area of circle is:",area)
print("parameter of circle is:",parameter)