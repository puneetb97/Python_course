# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:11:00 2019

@author: Puneet
"""
i = 1
while i<101:
    if (i%3==0 and i%5==0):
        print("fizzbuzz")
    elif (i%5==0):
        print("buzz")
    elif (i%3==0):
        print("fizz")
    else:
        print(i)
    i+=1
    