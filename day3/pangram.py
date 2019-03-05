# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:06:10 2019

@author: Puneet
"""

input_string = "The quick brown fox jumps over the lazy dog"
input_string1 = input_string.lower()
print(input_string1)
input_string2 = input_string1.replace(" ","")
new_list = list(input_string2)
print(new_list)
count = 0
for i in range(97,122):
    print(chr(i))
    if chr(i) not in new_list:
        print("NOT PANGRAM")
        break
else:
    print("PANGRAM")
