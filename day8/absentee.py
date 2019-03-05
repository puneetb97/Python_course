# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:52:05 2019

@author: Puneet
"""
list_input = []
for i in range(0,25):
    input_name = input("enter name:")
    list_input.append(input_name)
    if not input_name:
        break
    

with open("absentee.txt", mode="w+") as absent:
    for i in list_input:
        absent.write(i)
    absent.seek(0)
    text = absent.read()
    print(text)
    