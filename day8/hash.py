# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:44:46 2019

@author: Puneet
"""

import hashlib
with open("image.jpg" , mode="rb") as file:
    data = 0
    h = hashlib.sha1()
    while data!=b'':
        data = file.read(1024)
        h.update(data)   
print(h.hexdigest())