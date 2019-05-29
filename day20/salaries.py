# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:54:48 2019

@author: Puneet
"""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Salaries.csv")
print(df)
#challange1
female_professor = df[(df['sex'] == 'Female') &
   (df['rank']=='Prof')]


male_professor = df[(df['sex']=='Male') & (df['rank'] == 'Prof')]

print(female_professor[female_professor["salary"]==female_professor["salary"].max()])
print(female_professor[female_professor["salary"]==female_professor["salary"].min()])
print(male_professor[male_professor["salary"]==male_professor["salary"].max()])
print(male_professor[male_professor["salary"]==male_professor["salary"].min()])


#challenge2
sample_data = df[df['rank'] == 'Prof' ]  
print(sample_data[sample_data['salary'] == sample_data['salary'].max()])
print(sample_data[sample_data['salary'] == sample_data['salary'].min()])

# challenge3
demo_data = df[df['salary'].isnull()]
service1 = demo_data.iloc[0,3]
service2 = demo_data.iloc[1,3]
index = demo_data.index.tolist()
salary1 = df[df['service'] == service1]['salary'].mean()
salary2 = df[df['service'] == service2]['salary'].mean()

df.loc[index[0],['salary']] = df.loc[index[0],['salary']].fillna(salary1)
df.loc[index[1],['salary']] = df.loc[index[1],['salary']].fillna(salary2)

#challenge4
demo_data = df[df['phd'].isnull()]
service1 = demo_data.iloc[0,3]
service2 = demo_data.iloc[1,3]
index = demo_data.index.tolist()
phd1 = df[df['service'] == service1]['phd'].mean()
phd2 = df[df['service'] == service2]['phd'].mean()
df.loc[index[0],['phd']] = df.loc[index[0],['phd']].fillna(phd1)
df.loc[index[1],['phd']] = df.loc[index[1],['phd']].fillna(phd2)

#challenge5
demo_data = df.groupby('sex')
group = demo_data.size()
print(group)
size = group.tolist()
plt.pie(size,labels = ["female","male"],colors = ["yellow","green"],shadow = True,startangle = 90,autopct ='%1.1f%%')
plt.show()

#challenge6
demo_data = df.groupby('rank')
group = demo_data.size()
print(group)
size = group.tolist()
plt.pie(size,labels = ["Assocprof","AsstProf",'Prof'],colors = ["yellow","green","red"],shadow = True,startangle = 90,autopct ='%1.1f%%')
plt.show()

#challenge7
print(df[df['service'] == df['service'].max()])
print(df[df['service'] == df['service'].min()])

#challenge8
min_sal = df['salary'].min()
max_sal = df['salary'].max()
salary = df['salary'].tolist
plt.hist(salary,bins = range(50000,19000,15000),facecolor = "g")
plt.show()
