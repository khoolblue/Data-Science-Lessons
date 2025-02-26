# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:39:53 2025

@author: pushp
"""

import pandas as pd
#IEDITEDTHIS
#import csv file to a dataframe
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
new_df = df.dropna()
print(df)


