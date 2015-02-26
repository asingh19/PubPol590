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
df.head(40)

# NEW VARIABLES ----------------------- (anonmyous function)
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)

df.head(40)

# AGGREGATION (DAILY) ------------------------
grp = df.groupby(['year','month', 'day', 'panid', 'assignment'])
grp.groups
agg = grp['kwh'].sum()
type(agg)

# reset index # want the index to be 0,1,2,3,...
agg = agg.reset_index()
agg.head()
grp1 = agg.groupby(['year','month','day','assignment'])
grp1.head(10)
grp1.groups
grp1.groups

# split up into T/C
trt = {(k[0],k[1],k[2]): agg.kwh[v].values for k, 
    v in grp1.groups.iteritems() if k[3] == 'T'}
    
ctrl = {(k[0],k[1],k[2]): agg.kwh[v].values for k, 
    v in grp1.groups.iteritems() if k[3] == 'C'}

keys = ctrl.keys()

# tstats and pvals
tstats = DataFrame([(k, np.abs(float(ttest_ind(trt[k], ctrl[k], equal_var=False)[0])))
        for k in keys], columns = ['ymd','tstat'])
        
pvals = DataFrame([(k,(ttest_ind(trt[k], ctrl[k], equal_var=False)[1]))
        for k in keys], columns = ['ymd','pvals'])
        
t_p = pd.merge(tstats, pvals)

# sort and reset
t_p.sort(['ymd'], inplace=True)
t_p.reset_index(inplace=True, drop=True)

# PLOTTING ---------------------------------
fig1 = plt.figure() # initializing the plot
ax1 = fig1.add_subplot(2,1,1) # two rows, one column, first plot
ax1.plot(t_p['tstat'])
ax1.axhline(2, color='r', linestyle = '--')
ax1.axvline(14, color='g', linestyle = '--')
ax1.set_title('t-stats over-time')


ax2 = fig1.add_subplot(2,1,2) # two rows, one column, second plot
ax2.plot(t_p['pvals'])
ax2.axhline(0.05, color='g', linestyle = '--')
ax2.axvline(14, color='g', linestyle = '--')
ax2.set_title('pvals over-time')
plt.show()
fig1





