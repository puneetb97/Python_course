# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:31:29 2019

@author: Puneet
"""
list1 = []
while True:
    elements = input("enter details:")
    if not elements:
        break
    name, age, marks = elements.split(",")
    list1.append((name,int(age),int(marks)))

list1.sort()
print(list1)
    
    