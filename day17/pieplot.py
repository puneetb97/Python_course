# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:46:06 2019

@author: Puneet
"""
import matplotlib.pyplot as plt
labels = ["cricket","football","hockey","tennis"]
sizes = [15,30,25,10]
colors = ["gold","yellowgreen","lightcoral","lightskyblue"]
explode = (0.1,0,0,0)
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',shadow = True,startangle=90)
plt.savefig("piechart.jpg")