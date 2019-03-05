# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:32:58 2019

@author: Puneet
"""
count = 0
dict1 = {}
input_file = input("enter file name:")
file = open(input_file, mode = "rt")
content = file.read() 
print("Number of characters:",len(content))
data = content.split(" ")
print("Number of words:",len(data))
file = open(input_file, mode = "rt")
line = file.readlines()
print("Number of lines:",len(line))
for i in data:
    dict1[i] = " "
print("Number of unique words",len(dict1))
file.close()    
    
        