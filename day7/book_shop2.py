# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:57:20 2019

@author: Puneet
"""
from functools import reduce

input_list = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
list_product = []
list_order = []
result = lambda x :x[1]*x[2] 
for i in range(0,len(input_list)):
    list_product1 = []
    for j in range(1,len(input_list[i])):
        list_product1.append(result( input_list[i][j]))
    list_order.append(input_list[i][0])
    list_product.append(list_product1)

product = []
for i in list_product:
    product.append(reduce(lambda x,y:x+y, i))
    
final_product =list(map(lambda x: x+10 if x<100 else x  , product))
result_list = []
result_list.append((list_order))
result_list.append(final_product)
print(result_list)
