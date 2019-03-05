# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:40:49 2019

@author: Puneet
"""
# todays temperature in centigrade
temp_centigrade = int(input("temperature in jaipur:"))
# temperature in fahrenheit and kelvin
temp_fahrenheit = temp_centigrade*(9/5)+32
temp_kelvin = temp_centigrade + 273
print("temperature in fahrenheit",temp_fahrenheit)
print("temperature in kelvin",temp_kelvin)
