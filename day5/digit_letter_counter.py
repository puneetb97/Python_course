# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:21:32 2019

@author: Puneet
"""

dict1 = {}
input_string = input("enter string:")
for i in input_string:
    if ord(i) in range(97,123):
        dict1["letters"] = dict1.get("letters",0) + 1
    elif ord(i) in range(48,58):
        dict1["digits"] = dict1.get("digits",0) + 1
    else:
        pass
print(dict1)
for key,value in dict1.items():
    print(key,value)