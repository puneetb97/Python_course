# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:08:32 2019

@author: Puneet
"""

input_file = input("enter file name:")
with open(input_file, mode = "rt") as file:
    data = file.readlines()
    print(data[-1])
    