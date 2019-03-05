# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:10:59 2019

@author: Puneet
"""
dict1 = {}
with open("passwd.txt", mode = "rt") as file:
    for line in file:
        content = line.split(":")
        if content[1] == "*":
            dict1[content[0]] = content[2]
    
    for key,value in dict1.items():
        print(key,value)