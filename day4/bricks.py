# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:42:46 2019

@author: Puneet
"""

def calculate_result(number_smallbricks,number_bigbricks,total_inches):
    result_inches = number_smallbricks*1 + number_bigbricks*5
    if total_inches <= result_inches:
        print("true")
    else:
        print("false")

small_bricks = int(input("enter number of small bricks:"))
big_bricks = int(input("enter number of big bricks:"))
total_length = int(input("enter total length of row:"))
calculate_result(small_bricks,big_bricks,total_length)