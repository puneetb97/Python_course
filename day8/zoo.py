# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:09:39 2019

@author: Puneet
"""

def read():
    dict1 = {}
    with open("zoo.csv",mode="rt") as zoo1:
        content = zoo1.readlines()
        print(content)
        for i in range(1,len(content)):
            index = content[i].find(",")
            dict1[content[i][0:index]] = ""
    for key in dict1.keys():
        print(key)
read()
                
def water():
    dict1 ={}
    with open("zoo.csv",mode="rt") as zoo1:
        content = zoo1.readlines()
        for i in range(1,len(content)):
            index = content[i].find(",")
            index1 = content[i].rfind(",")
            dict1[content[i][0:index]] = dict1.get(content[i][0:index],0) + int(content[i][index1+1:])
    for key,value in dict1.items():
        print(key,value)
water()
    
def total_water():
    add = 0
    with open("zoo.csv",mode="rt") as zoo1:
        content = zoo1.readlines()
        for i in range(1,len(content)):
            index = content[i].rfind(",")
            add +=int(content[i][index+1:])
        print(add)

total_water()
    
            
                        


