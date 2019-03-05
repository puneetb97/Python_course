# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:33:26 2019

@author: Puneet
"""

input_length = int(input("enter length of list:"))
input_list = []
for i in range(0,input_length):
    input_element =int(input("enter element:"))
    input_list.append(input_element)

def add(list1):
    addition = 0
    for i in range(0,len(list1)):
        addition = addition + list1[i]
    return "add :{}".format(addition)
    


def multiply(list1):
    summition = 1
    for i in range(0,len(list1)):
        summition = summition*list1[i]
    return "multiplication is:{}".format(summition)

def largest(list1):
    maximum = 0
    for i in list1:
        if i>maximum:
            maximum = i
    return "maximum is:{}".format(maximum)        
    

def smallest(list1):
    smaller = list1[0]
    for i in list1:
        if i<=smaller:
            smaller = i
    return "smallest is: {}".format(smaller)
    

def sorting(list1):
    a=0
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            
            if list1[i]>=list1[j]:
                a=list1[i]
                list1[i] = list1[j]
                list1[j] = a
            else:
                continue
    return "sorted list is:{}".format(list1)

def remove_duplicate(list1):
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                del(list1[j])
            else:
                continue
    return "after deleting dupliacte values: {}".format(list1)

def Print():
    print(add(input_list))
    print(multiply(input_list))
    print(largest(input_list))
    print(smallest(input_list))
    print(sorting(input_list))
    print(remove_duplicate(input_list))
  

Print()

        
    


    