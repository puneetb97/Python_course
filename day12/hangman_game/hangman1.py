# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:32:54 2019

@author: Puneet
"""

import random
fruit_list = ["apple","banana","pears","watermellon","pineapple","grapes","orange"]
item = random.choice(fruit_list)
item_list = list(item)
print(item_list)
output_list = []
for i in range(0,len(item_list)):
    output_list.append("_")
print(output_list)
print("enter any character of your choice")
for i in range(0,len(item)+3):
    if item_list != []:
        char = input("")
        if char in item_list:
            item_list.remove(char)
        elif char not in item_list: 
            print("wrong character")
    else:
        break
