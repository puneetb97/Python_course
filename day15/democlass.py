# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:07:38 2019

@author: Puneet
"""

class Radio:
    height,length,width = (40,60,20)
    brand = "Phillips"
    def __init__(self,color,antenna,power):
        self.color = color
        self.antenna = antenna
        self.power = power
    
    def on_off_status(self,a):
        self.status_led = a
        print(self.status_led)
    def volume(self,a):
        self.vol = a
        print(self.vol)
    def tunner(self,a):
        self.freq = a
        print(self.freq)
r1 = Radio("red",True,"battery")            
r1.on_off_status(True)
print(r1.height)
print(r1.length)
print(r1.width)
r1.volume(5)
r1.tunner(93.7)
