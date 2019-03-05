# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:14:54 2019

@author: Puneet
"""

input_string = input("enter string:")
lower_string = input_string.lower()
print(lower_string)
vowels = ["a","e","i","o","u"," "]
def translate(input_string1):
    new_string = ""
    for i in input_string1:
        if i not in vowels:
            new_string = new_string + i +"o"+i
        else:
            new_string = new_string+i
    print(new_string)
translate(lower_string)
            