# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:53:07 2019

@author: Puneet
"""
import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1+url2+url3
response = requests.get(url)
jsondata = response.json()
print("lattitudes:",jsondata["coord"]["lat"]," ","longitude:",jsondata["coord"]["lon"])
print("weather condition:",jsondata["weather"][0]["description"])
print("wind speed:",jsondata["wind"]["speed"])
print("sunrise timing:",jsondata["sys"]["sunrise"]," ","sunset timing:",jsondata["sys"]["sunset"])