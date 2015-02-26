from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd
import matplotlib.pyplot as plt

main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/00 Data/"
root = main_dir + "L5_DATA"

# PATHING----------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT AND STACK
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh'], parse_dates = [1]) for v in paths], ignore_index = True)
### can use parse dates to convert the previous date type (string) into a datetime type

df_assign = pd.read_csv(root + "/sample_assignments.csv", usecols = [0,1])

# MERGE ------------
df = pd.merge(df,df_assign)
 
 #GROUPBY aka "split, apply, combine"
 ## see more at htt[://pandas/pydata.org/pandas-docs/stabel/groupby.html
 # not a list, so can do really quick calculations on it, for example:
grp1.mean()

# will return all the groups internally and what index values assigned to groups
grp1.groups # CAUTION: don't do this with super big data. it will crash.it's a way to look at the data
# the { means its a dictionary
gd1 = grp1.groups
#grp1 is a pandas function that is efficienct and optimized

 
## peek inside gd1 (dictionary)
gd1.keys()
gd1.values() # this produces a list
gd1['C'] # gd1 is a dict, so must use keys to get data
gd1.values()[0] # gd1.vaules() is a list, so we can use numerical indeces
gd1.viewvalues() # see all the values of the dictionary, gd1 # shows 
#in vector notation instead of list notation

## iteration properties of a dictionary
gd1.itervalues() # useful when you do for loops
[ v for v in gd1.itervalues()]
gd1.values() # returns two lists that look at only the values of the object, equal to the loop above

## other internal dictionary commands
[ v for v in gd1.iterkeys()]
gd1.keys() # equivalent to above

[(k,v) for k,v in gd1.iteritems()]

## split and apply (pooled data)
grp1.mean()
grp1['kwh'].mean()
# we don't pool data when looking at data over time; probably won't use this

## split and apply (panel/time series data)
grp2 = df.groupby(['assignment','date'])
gd2 = grp2.groups
gd2.keys()
gd2 # line 1: key created for assignment and date; every value that matches that
# shows up
df[38:39]
df[68:69]

grp2['kwh'].mean()
grp2

## TESTING FOR BALANCE (OVER-TIME)
from scipy.stats import ttest_ind
from scipy.special import stdtr

# example
a = [1, 4, 9, 2]
b = [1, 7, 8, 9]

t = ttest_ind(a,b, equal_var = False) # first value is t-stat, 2nd is p-value
# can also do:
t,p = ttest_ind(a,b, equal_var = False) 

# set up data
grp = df.groupby(['assignment', 'date']) # we now have a groupby object

# getting a set of all treatments by date (k = key, v = value)
trt = { k[1]: df.kwh[v] for k, v in grp.groups.iteritems() if k[0] == 'T'}

########## all below is to help understand the loop fxn above#########
grp.groups.keys()[0]
grp.groups.keys()[0][0]
grp.groups

v = [30, 60]
df.kwh[v] # however, we don't want a series, we want a list of data
df.kwh[v].values # now we have an array

grp.groups.keys()[0] # this key (k) us sent
k = grp.groups.keys()[0]
k[1]
#############################################
# now make a control group
ctrl = { k[1]: df.kwh[v] for k, v in grp.groups.iteritems() if k[0] == 'C'}
keys = trt.keys()

# create dataframes of information
tstats = DataFrame([(k, np.abs(ttest_ind(trt[k], ctrl[k], equal_var = False)[0])) for k in keys], 
    columns = ['date', 'tstat'])
    
p_vals = DataFrame([(k, np.abs(ttest_ind(trt[k], ctrl[k], equal_var = False)[1])) for k in keys], 
    columns = ['date', 'p_vals'])

t_p = pd.merge(tstats, p_vals)

## sort and reset_index
t_p.sort(['date'], inplace=True)
t_p = t_p.sort(['date']) # equivalent, but slow
t_p.reset_index(inplace=True, drop = True)
    

# comparisons of the two data sets (ctrl and trtment)
diff = {k: (trt[k].mean() - ctrl[k].mean()) for k in keys}
tstats = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[0]) for k in keys}
pvals = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[1]) for k in keys}
t_p = {k: (tstats[k], pvals[k]) for k in keys}

# PLOTTING ---------------------------------
fig1 = plt.figure() # initializing the plot
ax1 = fig1.add_subplot(2,1,1) # two rows, one column, first plot
ax1.plot(t_p['tstat'])
ax1.axhline(2, color='r', linestyle = '--')
ax1.set_title('t-stats over-time')


ax2 = fig1.add_subplot(2,1,2) # two rows, one column, second plot
ax2.plot(t_p['p_vals'])
ax2.axhline(0.05, color='g', linestyle = '--')
ax2.set_title('p_vals over-time')


