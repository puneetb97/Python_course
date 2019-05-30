# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:09:44 2019

@author: Puneet
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")
df.columns

#total people survived
survived = df.groupby('Survived').size().tolist()
print("people survived:",survived[1])

#total people died
print("people died:",survived[0])

#people survived in percentage
print("percentage of people survived",(df['Survived'].value_counts(normalize = True).tolist()[1])*100)

#males that survived vs male passed away
print("males that survived= ",df['Survived'][(df['Sex'] == 'male') & (df['Survived'] == 1)].value_counts().tolist()[0])
print("males that passed away=",df['Survived'][(df['Sex'] == 'male') & (df['Survived'] == 0)].value_counts().tolist()[0])

#females that survived vs female that passed away
print("females that survived= ",df['Survived'][(df['Sex'] == 'female') & (df['Survived'] == 1)].value_counts().tolist()[0])
print("females that passed away= ",df['Survived'][(df['Sex'] == 'female') & (df['Survived'] == 0)].value_counts().tolist()[0])

#adding another column
df["child"] = df['Age'].map(lambda x: 1 if x<18 else 0)
print("children survived:",df['Survived'][(df['child'] == 1) & (df['Survived'] == 1)].value_counts().tolist()[0])
print("elders survived:",df['Survived'][(df['child'] == 0) & (df['Survived'] == 1)].value_counts().tolist()[0])
