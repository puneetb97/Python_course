# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:05:45 2019

@author: Puneet
"""
import matplotlib.pyplot as plt
labels = ["python","c++","java","perl","scala","lisp"]
performance = [10,8,6,4,2,1]

plt.bar([0,1,2,3,4,5],performance,align="center",alpha = 0.5)
plt.xticks([0,1,2,3,4,5],labels)
plt.ylabel("usage")
plt.title("programming language usage")
plt.savefig("barplot.jpg")

