# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:45:13 2019

@author: Puneet
"""

file1 = open("word.txt","rt")
file2 = open("word1.txt","wt")
for line in file1:
    file2.write(line)
file = open("word1.txt","rt")
file.read()

