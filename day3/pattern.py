# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:39:01 2019

@author: Puneet
"""
input_value = int(input("enter number of rows:"))
for i in range(1,input_value+1):
    print("* "*i)
for i in range(input_value-1,0,-1):
    print("* "*i)