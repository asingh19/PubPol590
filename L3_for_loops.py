from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/amitpalsingh/Desktop/Data" 
git_dir = "/Users/amitpalsingh/GitHub"
csv_file = "sample_data_clean.csv"

# FOR LOOPS-----------------------------------
df = pd.read_csv(os.path.join(main_dir, csv_file))

list1 = range(10,15)
list2 = ['a','b','c']
list3 = [1,'a', True]

## iterating over elements (for loops)
# for(name of what you're referencing) in (list)
# internal environment created; must use Print fxn
for v in list1:
    v
    
for v in list1:
    print(v)
    
for v in list2:
    print(v)
    
for v in list3:
    print(v, type(v))


## populationg (empty) lists
list1 # is all int
list4 = [] # empty list
list5 = []

for v in list1:
    v2 = v**2
    list4.extend([v2]) # accepts only 'list' obj
    list5.append(v2) # appends whatever obj as is
    print(v2)
    
[v**2 for v in list1]
list6 = [ v**2 < 144 for v in list1]

## iterating using enumerate
# float allows for decimals
list7 = [ [i,float(v)/2] for i, v in enumerate(list1)] 
list7

# ITERATE THROUGH A SERIES------------------------
s1 = df['consump']
[v > 2 for v in s1]
{{i, float(v)*.3] for i, v in s1.iteritems()1

# ITERATE THROUGH A DATAFRAME----------------------
[v for v in df]
[df[v] for v in df]
[[i,v] for i, v in df.iteritems()]