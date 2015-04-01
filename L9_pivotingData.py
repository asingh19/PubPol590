from __future__ import division
from pandas import Series, DataFrame
from scipy.stats import ttest_ind
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from dateutil import parser # use this to ensure dates are parsed correctly
import os
import xlrd
import pytz 
import time
import matplotlib.pyplot as plt

main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/00 Data/"
root = main_dir + "data_all/"

# import data ------------------
df = pd.read_csv(root + "sample_30min.csv", header = 0, parse_dates =[1],
    date_parser=parser.parse)
# when you want to parse dates, use this

df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])

# merge data ----------------
df = pd.merge(df, df_assign)

# add/drop variables ---------------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)
df['ymd'] = df['date'].apply(lambda x: x.date())

# daily aggregation
grp = df.groupby(['year', 'month', 'day', 'panid', 'assignment'])
grp = df.groupby(['ymd', 'panid', 'assignment'])
df1 = grp['kwh'].sum().reset_index()

# PIVOT DATA --------------
# go from long to wide

## 1. create column names for wide data
# create string names and denote consumption and date
# use ternary expression: [true-expr(x) if condition else false-exp(x) for x in list]
#df1['day_str'] = ['0' + str(v) if v < 10 else str(v) for v in df1['date']] # add '0' to < 10
#df1['kwh_ymd'] = 'kwh_' + df1.year.apply(str) + '_' + df1.month.apply(str) + 
#    '_' + df1.day_str.apply(str)
    
df1['kwh_ymd'] = 'kwh_' + df1['ymd'].apply(str)

# 2. pivot! aka long to wide
df1_piv = df1.pivot('panid', 'kwh_ymd', 'kwh')

# clean up for making things pretty
df1_piv.reset_index(inplace = True) # this makes panid its own variable
df1_piv.columns.name = None

# MERGE TIME invariant data ------------
df2 = pd.merge(df_assign, df1_piv) # this attaching order looks better

## export data for regression
df2.to_csv(root + "kwh_wide.csv", sep = ",", index = False)

