from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/00 Data" 
git_dir = "/Users/amitpalsingh/GitHub"
csv_file = "L4_sample_missing.csv"

# IMPORTING DATA: SETTING MISSING VALUES (SENTINELS)

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.head() # top 5 values
df.head(10) # head(n) given top n rows
df[:10]
df.tail(10) # tail(n) given bottom n rows 
df['consump'].head(10).apply(type) #apply function type to top 10 rows of consump

## we DON' want string data. periods are common placeholders for missing data 
#in some programming languages. so we need to create new missing value sentinels
# use 'na_values' fxn to use sentinels
missing = ['.','NA','NULL','']
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values=missing)
df['consump'].head(10).apply(type)

#MISSING DATA (USING SMALLER DATAFRAME)--------------------------

#QUICK TIP: you can repeat lists by multiplying
[1,2,3]
[1,2,3]*3

# types of missing data
None
np.nan
type(None)
type(np.nan)

## create a sample data set
zip1 = zip([2,4,8], [np.nan, 5, 7], [np.nan, np.nan, 22])
df1 = DataFrame(zip1, columns = ['a','b','c'])

## search for missing data using 
df1.isnull() #pandas method to find missing data