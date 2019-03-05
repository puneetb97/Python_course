# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:18:11 2019

@author: Puneet
"""

input_dict = {"a" : 2, "b" : 15, "c" : 13}
list1 = [13,14,17,18,19]
Sum = 0
def fix_teen(n):
    if n not in list1:
        return n
    else:
        return 0
for value in input_dict.values():
    Sum = Sum + fix_teen(value)
print("Sum:",Sum)
    
    
