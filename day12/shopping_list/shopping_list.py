# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:43:38 2019

@author: Puneet
"""

shopping_list = []
print("enter item to pick from the store:")
print("enter DONE after completion:")
def adding_item(item):
    if item is not None:
        global shopping_list
        shopping_list = item.split(",")

def insert(item,index):
    shopping_list.insert(index,item)

def remove(index):
    shopping_list.pop(index)
         
while True:
    data = input("")
    
    if data.lower() == "done":
        break
    elif data.lower() == "show":
        print("items are:")
        for i in range(0,len(shopping_list)):
            print(i+1,":",shopping_list[i])
    elif data.lower() == "help":
        data = None
        print("""this will help to make your kart for shopping
                  just type the name of the item and enter
                  after completion type DONE
                  for getting the items in your kart type SHOW""")
    elif data.lower() == "add":
        index = int(input("enter index:"))
        item = input("enter item name")
        insert(item,index)
    
    elif data.lower() == "delete":
        index = int(input("enter index:"))
        remove(index)
    
    else:
        adding_item(data)

with open("shopping.txt",mode = "wt") as file:
        file.writelines(shopping_list)
    
    
