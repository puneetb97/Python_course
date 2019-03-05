# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:50:20 2019

@author: Puneet
"""
# car travelled in km
car_kilometer = int(input("car travelled in kilometer:"))
# cost of diesel
cost_diesel = int(input("cost of diesel:"))
# car average
car_average = int(input("average of car:"))
# cost of travelling
total_cost = (car_kilometer/car_average)*cost_diesel
print(total_cost)
