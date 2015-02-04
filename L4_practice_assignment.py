# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

# SETTING DIRECTORIES
main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/00 Data" 
git_dir = "/Users/amitpalsingh/GitHub"
csv_file = "L4_small_data_w_missing_duplicated.csv"

# IMPORTING DATA
df = pd.read_csv(os.path.join(main_dir, csv_file))
#459 rows X 3 columns

# viewing data
df.head()
df.tail()

# viewing my function types
df['consump'].head(10).apply(type)

#1 REPLACING MISSING VALUES WITH SENTINELS
missing = ['.','NA','NULL','','-']
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values=missing)
# still 459 rows × 3 columns; nothing removed

df['consump'].head(10).apply(type)
df.isnull()

#2 DROP (NOT PURGE) DUPLICATED ROWS
df.drop_duplicates()

df2 = df.drop_duplicates()
# 416 rows × 3 columns; dropped 43 rows

#3 EXTRACTING ROWS WHERE CONSUMP HAS MISSING DATA
df2
df2['consump'].isnull()
rows = df2['consump'].isnull()
df2[rows]
df.consump.missing = df2[rows]
df2
df.consump.missing

############### IGNORE ########################
##seeing if panid or date has any missing values
cols = ['panid','date']
df2[cols]
df2[cols].isnull()
rows1 = df2[cols].isnull()
df2[rows1]
df2
#FAIL
##############################################

#4 Check for duplicated values on Subset of PANID and DATE
df2.duplicated(['panid','date'])

t_b = df2.duplicated(['panid','date'])
b_t = df2.duplicated(['panid','date'], take_last = True)
unique = ~(t_b | b_t) # complement where either is true; ~ is a NOT operator

duplicated = (t_b | b_t)
DataFrame([t_b, b_t])
df2[unique]

final = ~unique & rows
cleaned_data = df2[~final]

consump_mean = cleaned_data.consump.mean()
