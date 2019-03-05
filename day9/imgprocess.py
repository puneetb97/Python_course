# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:29:23 2019

@author: Puneet
"""

from PIL import Image
input_file = input("enter file name:")
img = Image.open(input_file).convert("LA")
img = img.rotate(270)
w,h = img.size
img = img.crop((80,102,w-80,h-102))
img.thumbnail((75 , 75))
img.save("image1.png")



