# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:03:40 2019

@author: Puneet
"""
from selenium import webdriver
import pandas as pd
from time import sleep


url = "https://www.amazon.in/"
driver = webdriver.Chrome("C:/Users/Puneet/Downloads/chromedriver_win32/chromedriver.exe")

driver.get(url)

search = driver.find_element_by_xpath('''//*[@id="twotabsearchtextbox"]''').send_keys("iphone")

sleep(5)

button = driver.find_element_by_xpath('''//*[@id="nav-search"]/form/div[2]/div/input''')
button.click()
sleep(5)

data = driver.find_element_by_xpath('//*[@id="atfResults"]')

a,b = [],[]
for item in data.find_elements_by_tag_name("h2"):    
    a.append(item.text.strip())

for item in data.find_elements_by_class_name("a-size-base"):
    b.append(item.text.strip())

from collections import OrderedDict
col_name = ["search_result","price"]
col_data = OrderedDict(zip(col_name,[a,b]))
data = pd.DataFrame(col_data)
data.to_csv("amazon.csv")

