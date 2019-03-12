# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:43:01 2019

@author: Puneet
"""

from bs4 import BeautifulSoup
import requests
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")
right_table = soup.find("table",class_="table")
A,B,C,D,E = [],[],[],[],[]
for rows in right_table.findAll("tr"):
    colm = rows.findAll("td")
    if len(colm)==5:
        A.append(colm[0].text.strip())
        B.append(colm[1].text.strip())
        C.append(colm[2].text.strip())
        D.append(colm[3].text.strip())
        E.append(colm[4].text.strip())
import pandas as pd
df = pd.DataFrame(A,columns=["POS"])
df["Team"]=B
df["Matches"]=C
df["points"]=D
df["rating"]=E
df.to_csv("icc.csv")