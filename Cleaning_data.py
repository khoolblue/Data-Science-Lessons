# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:39:53 2025

@author: pushp
"""

import pandas as pd
#IEDITEDTHIS
#import csv file to a dataframe
df = pd.read_csv('data.csv')

#for changing values in original file
#df.dropna(inplace = True)


#for making a copy and doing the changes in the copied file
#new_df = df.dropna()

#replace nan values
#df.fillna(130, inplace = True)


#nan_rows = df[df.isna().any(axis = 1)]#find rows where nan values are
nan_rows_number = df[df.isna().any(axis = 1)].index
#df[i]#will give label named i, wont accept number
print(df[df.isna().any(axis=1)])
#new_df = df[df.columns[0]][df.fillna(130)]
#print(new_df)


x = df["Calories"].mean()
print(x)
print(df) 
df["Calories"] = df["Calories"].fillna(x)
print(df["Calories"])
#print(df)
nan_updated = df[df.isna().any(axis = 1)]
#print(nan_updated)
print(df[df.isna().any(axis = 1)])
