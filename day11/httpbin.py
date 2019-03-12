# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:59:19 2019

@author: Puneet
"""
import json
import requests
dict1 = {"firstname":"chris","language":"english"}
headers = {"Content-Type":"application/json","Content-Length":len(dict1),"data":json.dumps(dict1)}
post = requests.post("http://httpbin.org/post",dict1,headers)
response = requests.get("http://httpbin.org/get?firstname=chris&language=english")
#jsondata = response.json()
#print(jsondata)
print(response.text)