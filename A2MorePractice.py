from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORTING DATA-------------------------

## assigning file paths
main_dir = "/Users/amitpalsingh/GitHub/PubPol590/01A2IntroPandas" 
txt_file = "/File1_small.txt"

#import data with pd.read_table
df = pd.read_table(main_dir+txt_file, sep =" ")

#extract rows 60-99
df[60:100]

#extract rows where elec consump is >30
list(df)
df[df.kwh>30]

