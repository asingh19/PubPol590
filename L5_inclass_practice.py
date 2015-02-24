from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/00 Data/"
root = main_dir + "L5_DATA"

# PATHING----------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT AND STACH
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths], ignore_index = True)

df_assign = pd.read_csv(root + "/sample_assignments.csv", usecols = [0,1])

# MERGE ------------
df = pd.merge(df,df_assign)
 
 #GROUPBY aka "split, apply, combine"
 ## see more at htt[://pandas/pydata.org/pandas-docs/stabel/groupby.html
 
 # split by C/T, pooled w/o time
groups1 = df.groupby(['assignment']) # splitting by assignment 
groups1.groups

# apply the mean
groups1['kwh'].apply(np.mean)  #.apply is to "apply" ANY type of function
groups1['kwh'].mean() # .mean() is an internal method (faster)

%timeit -n 100 groups1['kwh'].apply(np.mean)  #.apply is to "apply" ANY type of function
%timeit -n 100 groups1['kwh'].mean() # .mean() is an internal method (faster)

#Series. then press tab to find out what functions are available

# split by C/T, pooling w time
groups2 = df.groupby(['assignment', 'date']) # splitting by assignment 
groups2.groups

# apply the mean
groups2['kwh'].mean() # .mean() is an internal method (faster)


#### the order matters
groups2 = df.groupby(['date','assignment']) # splitting by assignment 
groups2.groups

## UNSTACK------------
gp_mean = groups2['kwh'].mean()
gp_unstack = gp_mean.unstack('assignment')
gp_unstack['T'] # mean, over tiem, of all treated panids
