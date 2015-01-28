from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/amitpalsingh/Desktop/Data" 
git_dir = "/Users/amitpalsingh/GitHub"
csv_file = "sample_data_clean.csv"

#OS MODULE

df = pd.read_csv(os.path.join(main_dir, csv_file))

# PYTHON DATA TYPES ---------------------------

## strings, can be in single or double quotes
str1 = "hello,computer"
str2 = "hello, human"
str3 = u'eep'

type(str1) # type str
type(str2) # type str
type(str3) # type unicode

## numeric
int1 = 10
float1 = 20.56 # is for decimal numbers
long1 = 34093859823599598999999 #is for long integers

## logical
bool1 = True
nonbool1 = 0 #not bool, technically an integer
bool2 = bool(nonbool1)

# CREATING LISTS AND TUPLES------------------

## in brief, list can be changed, turples cannot
## we almost exclusively use lists

list1 = []
list1
list2 = [1,2,3] 
list2[2] # output 3 because starts with 0
list2[2] = 5
list[2]

## tuples, cant change
tup1 = (8, 3, 19)
tup1[2] # output is 19
tup1[2] = 5

## convert
list2 = list(tup1)
tup2 = tuple(list2)
list2
tup2

## lists can be appended and extended
list2.append([3,90])
list2
list2 = [8, 3, 90]
list2.extend([6,88])
list2
len(list2) #tells you the length of the list

# CONVERTING LISTS TO SERIES AND DATAFRAMES

list3 = range(5,10) # range(n,m) -- givens a list from n to m-1
list4 = range(5) # range(m) -- gives list from 0 to m-1
list4 # [0,1,2,3,4]
list5 = ['q','r','s','t','u']

## list to series
s1 = Series(list3)
s2 = Series(list4)
s3 = Series(list5)



