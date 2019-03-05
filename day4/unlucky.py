# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:15:39 2019

@author: Puneet
"""

number = int(input("enter number of elements:"))
input_list = []
add = 0
for i in range(0,number):
    element = int(input("enter element:"))
    input_list.append(element)
    
for i in range(0,len(input_list)):
    if input_list[i] == 13:
        continue
    elif input_list[i-1] == 13:
        continue
    else:
        add = add + input_list[i]
        
    
print("addition:",add)