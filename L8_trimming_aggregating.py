from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import os
import xlrd 
import pytz
from datetime import datetime, timedelta
import time

main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/"
root = main_dir + "00 Data/"

# IMPORT AND DATA --------------------
df = pd.read_csv(root + "L8_sample_30min.csv", header=0, parse_dates=[1])
df_assign = pd.read_csv(root + 'L8_sample_assignments.csv', usecols=[0,1])

df = pd.merge(df, df_assign)
df['date'][0]
df['date'][0].day
df['date'][0].month
df['date'][0].year

# NEW VARIABLES ----------------------- (ananymous function)
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)
df['ymd'] = df['date'].apply(lambda x: x.date)

# AGGREGATION (DAILY) ------------------------
grp = df.groupby(['year', 'day', 'panid', 'assignment'])
grp.groups
agg = grp['kwh'].sum()

# reset index
agg = agg.reset_index()
agg.head()
grp1 = agg.groupby(['year','day','assignment'])
grp1.head()
grp1.groups

## split up into T/C
trt = {()}
