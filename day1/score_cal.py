# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:00:34 2019

@author: Puneet
"""
# marks in assignment and exams
assignment1_marks = int(input("marks in assignment1:"))
assignment2_marks = int(input("marks in assignment2:"))
assignment3_marks = int(input("marks in assignment3:"))
exam1_marks = int(input("marks in exam1:"))
exam2_marks = int(input("marks in exam2:"))
# calculation of weighted score
weighted_score = (assignment1_marks + assignment2_marks + assignment3_marks)* 0.1 + (exam1_marks + exam2_marks)*0.35
print("weighted score:",weighted_score)
