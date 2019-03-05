# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:35:04 2019

@author: Puneet
"""
from collections import OrderedDict

dict1 = OrderedDict()
while True:
    input_element = input("enter details:")
    if not input_element:
        break
    list1 = input_element.split(" ")
    print(list1)
    value = int(list1.pop(-1))
    key = " ".join(list1)
    dict1[key] = dict1.get(key,0) + value

for key1,value1 in dict1.items():
    print(key1,value1)

      
        
        
    




    