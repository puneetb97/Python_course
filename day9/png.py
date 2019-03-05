# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:51:52 2019

@author: Puneet
"""
from PIL import Image
import os
os.chdir("H:/forsk/day9/images")
list1 = []
for i in os.listdir("."):
    list1.append(i.split(".")[0])
for i in range(0,len(list1)):
    img = Image.open(list1[i])
    img.save("{}.png",list1[i])