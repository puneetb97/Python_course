# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:41:55 2019

@author: Puneet
"""
import requests
url1= "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR&compact=y"
url3 = "&apiKey=b8f5237f685994440550"
url = url1+url2+url3
response = requests.get(url)
jsondata = response.json()
print("USD to INR:",jsondata["USD_INR"]["val"])