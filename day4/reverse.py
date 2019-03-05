# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:56:07 2019

@author: Puneet
"""

enter_string = input("enter any string:")

def reverse(input_string):
    list_string = list(input_string)
    length = len(list_string)
    output_string = ""
    for i in range(length-1,-1,-1):
        output_string = output_string + list_string.pop(i)
    print(output_string)
reverse(enter_string)
    