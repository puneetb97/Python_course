# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:28:06 2019

@author: Puneet
"""


input_list = [["34587", "Learning Python", "Mark Lutz", 4, 40.95],["98762", "ProgrammingPython", "Mark Lutz", 5, 56.80],["77226", "Head FirstPython", "PaulBarry", 3, 32.95],["88112", "EinführunginPython3", "BerndKlein", 3, 24.99]]


list_product = []
list_order = []
result = lambda x: x[3]*x[4]
for i in range(0,len(input_list)):
    list_product.append(result(input_list[i]))
    list_order.append(input_list[i][0])
print(list_product)

tuple_product = tuple(map(lambda x: x+10 if x<100 else x  , list_product))
tuple_order = tuple(list_order)
result_list = []
result_list.append(tuple_order)
result_list.append(tuple_product)
print(result_list)

