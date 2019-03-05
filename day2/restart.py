# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:39:49 2019

@author: Puneet
"""
input_string = "RESTART"
dir(str)
help(str.replace)
new_string = input_string[::-1].replace("R","$",1)
print("new string:",new_string[::-1])