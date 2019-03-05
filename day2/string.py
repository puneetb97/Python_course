# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:02:24 2019

@author: Puneet
"""

name = input("enter name:")

index_info = name.index(" ")
print(index_info)
print(name[index_info+1::],"",name[0:index_info:])