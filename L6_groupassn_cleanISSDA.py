## importing pandas
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

## setting directories
main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/"

# IMPORTING DATA ------------------------------------
## making a list of file paths using loops
# we want to import files 'file_rand_1' to 'file_rand_4'. note the pattern of 'file_rand_i' where i = 1 - 4
# we can make a list of file names by combining strings based on the pattern.
root = main_dir + "00 Data/"
paths0 = [ root + "CER_File" + str(v) + ".txt" for v in range(1,7) ]
paths1 = [ os.path.join(root, "CER_File%s.txt") % v for v in range(1,7) ]
paths2 = [ (root + "CER_File%s.txt") % v for v in range(1,7) ]


## super pro way
[ v for v in os.listdir(root) ]
[ v for v in os.listdir(root) if v.startswith("CER_File") ]
[ os.path.join(root, v) for v in os.listdir(root) if v.startswith("CER_File") ]
paths3 = [ os.path.join(root, v) for v in os.listdir(root) if v.startswith("CER_File") ]

# IMPORT DATA ------------------------------------
# create list of DataFrames
## VERY IMPORTANT to name the dataframe. need keys to stack.
list_of_dfs = [ pd.read_table(v,sep = '/s') for v in paths3]


len(list_of_dfs)
type(list_of_dfs)
type(list_of_dfs[0])