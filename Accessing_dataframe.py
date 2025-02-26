# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:39:53 2025

@author: pushp
"""

import pandas as pd
#IEDITEDTHIS
#import csv file to a dataframe
df = pd.read_csv('data.csv')

#for changinng values in original file
#df.dropna(inplace = True)

#print specific element
# .loc is label based indexing
specific_value = df.loc[27 , df.columns[1:2]]#prints 27th row and 1st column
specific_value1 = df.loc[:,:]#all rows and columns
specific_value2 = df.loc[0, df.columns[0]]#shows first row of first solumn
specific_value3 = df.columns[0]#prints first column
specific_value4 = df.columns.tolist()#prints all columns as list
# .iloc position based indexing
specific_value5 = df.iloc[:,2]#.name prints column name of respective column number
specific_value6 = df.iloc[0,2]
print(specific_value6)#prints specific element





