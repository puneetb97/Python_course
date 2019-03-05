# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:49:17 2019

@author: Puneet
"""
number_element = int(input("enter number of element:"))
number_list = []
for i in range(number_element):
    element = int(input("enter element:"))
    number_list.append(element)
for i in number_list:
    new_string = str(i)
    if new_string == new_string[::-1]:
        print("true")
        break