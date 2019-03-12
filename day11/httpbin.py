# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:59:19 2019

@author: Puneet
"""
import json
import requests

host = "http://httpbin.org/post"
data = {"firstname":"chris","language":"english"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method(host,data,headers):
    post = requests.post(host,data,headers)
    return post

def get_method():
    response = requests.get("http://httpbin.org/get?firstname=chris&language=english")
    return response.text

post_method(host,data,headers)
print(get_method())