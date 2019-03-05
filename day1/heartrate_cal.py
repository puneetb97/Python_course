# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:32:59 2019

@author: Puneet
"""
# my current age
my_age = int(input("current age:"))
# calculating maximum heart range
max_heart_range = 220 - my_age
# calculating higher and lower value of target heart range
low_target_heart_range = max_heart_range * 0.7
high_target_heart_range = max_heart_range * 0.85
print(low_target_heart_range)
print(high_target_heart_range)