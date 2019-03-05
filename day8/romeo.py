# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:13:49 2019

@author: Puneet
"""

with open("romeo.txt", mode = "rt") as romeo1:
    dict1={}
    final_content=[]
    content_list = romeo1.readlines()
    for i in content_list:
        content = i.split(" ")
        final_content.append(content)
    for i in final_content:
        for j in i:
            dict1[j] = dict1.get(j,0) + 1
    print(dict1)
    
    