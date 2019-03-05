# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:46:22 2019

@author: Puneet
"""

input_string = """ 
                    This is a multi line string. This code challenge is to 
                    test your understanding about strings.
                    You need to print some part of this string.
                    From here print this text without manually counting the indexes,"""
index_info = input_string.index("From")
print(input_string[index_info::])