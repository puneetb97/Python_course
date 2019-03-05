# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:58:51 2019

@author: Puneet
"""
# list of states
state_name = ["Alabama","California","Oklahoma","Florida"]
vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
new_list = []
for name in state_name:
    new_string=""
    for letter in name:
        if letter not in vowel_list:
            new_string = new_string + letter
    new_list.append(new_string)            
print(new_list)        

            