# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:07:31 2019

@author: Puneet
"""

name = input("enter name:")
index_info = name.index(" ")
print(name[index_info+1::],"",name[0:index_info:])