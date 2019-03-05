# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:55:58 2019

@author: Puneet
"""
import csv
list1 = []
with open("passwd.txt", mode = "rt") as file:
    content = file.readlines()
    for i in content:
        list1.append(i.split(":"))
    print(list1)
with open("passwd.csv",mode = "w") as file:
    write = csv.writer(file,delimiter="\t")
    for i in range(0,len(list1)):
        if list1[i][1] == "#":
            pass
        else:
            list2 = [list1[i][0]," ",list1[i][2]]
            write.writerow(list2)
