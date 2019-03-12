# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:38:14 2019

@author: Puneet
"""
import random
fruit_list = ["apple","banana","pears","watermellon","pineapple","grapes","orange"]
item = random.choice(fruit_list)
item_list = list(item)
print(item_list)
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

if item_list == []:
    print("win")
else:
    print("lose")
        
        