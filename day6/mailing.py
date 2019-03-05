# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:54:43 2019

@author: Puneet
"""

old_list = ["puneetb001@gmail.com","jayeshjain98@gmail.com","arpanjain67@gmail.com","nmnthk17@gmail.com","adidel76@gmail.com","shubham21@gmail.com","chelu76@gmail.com","harshitsharma54@gmail.com","pandey21@gmail.com","raviraj54@gmail.com","shivamsingh43@gmail.com"]
new_list = ["puneetb001@gmail.com","jayeshjain98@gmail.com","arpanjain67@gmail.com","nmnthk17@gmail.com",] 
result_set = set(old_list).difference(new_list)
print(list(result_set))