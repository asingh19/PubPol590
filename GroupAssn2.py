from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

# SETTING DIRECTORIES
main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/" 
git_dir = "/Users/amitpalsingh/GitHub"
txt1 = "/00 Data/CER_File1.txt"
txt2 = "/00 Data/CER_File2.txt"
txt3 = "/00 Data/CER_File3.txt"
txt4 = "/00 Data/CER_File4.txt"
txt5 = "/00 Data/CER_File5.txt"
txt6 = "/00 Data/CER_File6.txt"


# IMPORTING DATA
missing = ['.','NA','NULL','','-', '999999999']
df1 = pd.read_table(main_dir + txt1, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)
df2 = pd.read_table(main_dir + txt2, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)
df3 = pd.read_table(main_dir + txt3, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)
df4 = pd.read_table(main_dir + txt4, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)
df5 = pd.read_table(main_dir + txt5, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)
df6 = pd.read_table(main_dir + txt6, names = ['panid', 'date', 'kwh'], sep = ' ', na_values=missing)

list_of_dfs = [df1, df2, df3, df4, df5, df6]
df_merge = pd.concat(list_of_dfs, ignore_index = True)
df_merge = pd.merge(df1, df2, df3, df4, df5, df6)

df_null = df_merge.isnull()
df_merge[df_null]

df_merge.date[45200:45248]


df_merge = df_merge.drop_duplicates() # drop dups

df_merge.kwh.count()
df_merge.panid.count()
df_merge.date.count()