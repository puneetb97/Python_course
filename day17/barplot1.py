# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:17:20 2019

@author: Puneet
"""
import matplotlib.pyplot as plt
label = ['Adventure', 'Action', 'Drama', 'Comedy', \
         'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical', \
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', \
         'Multiple Genres', 'Reality']

no_movies = [941,854,4595,2125,942,509,548,149,1952,161,64,61,35,5]

index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.bar(index,no_movies)
plt.xticks(index,label,fontsize=10,rotation=90)
plt.ylabel("no of movies")
plt.title("market share for each genre 1995-2017")
plt.savefig("barplot1.jpg")


