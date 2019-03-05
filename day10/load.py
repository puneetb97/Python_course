# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:40:20 2019

@author: Puneet
"""
import json
with open("faculty.json", "r") as file:
    data = json.load(file)
print(data)