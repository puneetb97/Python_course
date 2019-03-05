# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:27:04 2019

@author: Puneet
"""

# my height in meters
my_height = float(input("height:"))
my_weight = int(input("weight:"))
# my ponderal index values
ponderal_index = ((my_weight/my_height)/my_height)/my_height
print(ponderal_index)