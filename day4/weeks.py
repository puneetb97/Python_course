# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:06:29 2019

@author: Puneet
"""
input_tuple = input("enter week days:")
input_list = []
for i in input_tuple:
    input_list.append(i)
print(input_list)
week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for i in range(0,7):
    if week_days[i] != input_list[i]:
        input_list.insert(i,week_days[i])
    else:
        continue
print(tuple(input_list))

