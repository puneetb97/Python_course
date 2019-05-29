# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]
plt.title("line graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis([0,10,0,10])
plt.scatter(x,y)
plt.plot(x,y)
plt.savefig("scatter.jpg")