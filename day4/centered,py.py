# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:37:38 2019

@author: Puneet
"""

input_list = list(input("enter elements:").split(","))
print(input_list)
maximum = 0
for i in range(0,len(input_list)):
    if int(input_list[i])>=maximum:
        maximum=i
del(input_list[maximum])
minimum = int(input_list[0])
for i in range(0,len(input_list)):
    if int(input_list[i])<=minimum:
        minimum=i
del(input_list[minimum])
print(input_list)
a = len(input_list)//2
print(int(input_list[a]))
    
    