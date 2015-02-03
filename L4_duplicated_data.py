from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

# DUPLICATED VALUES---------------------------------

## create new dataframe
zip3 = zip(['red', 'green', 'blue', 'orange']*3, [5, 10, 20, 40]*3,
            [':(', ':D', ':D']*4)

df3 = DataFrame(zip3, columns = ['A', 'B', 'C'])

## pandas method 'duplicated'
df3.duplicated() #search from top to bottom by default
df3.duplicated(take_last = True) #searches bottom to top

## subset duplicated values
df3.duplicated(subset = ['A','B'])
df3.duplicated(['A','B'])

## how to get all values that have duplicates (purging)
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # complement where either is true
DataFrame([t_b, b_t])

unique = ~t_b & ~b_t
unique
DataFrame([~t_b, ~b_t])

df3[unique]

# DROPPING DUPLICATES-----------------------------------------------
df3.drop_duplicates()
df3.drop_duplicates(take_last = True)

## this is the same as
t_b = df3.duplicated()
df3[~t_b]
df3.drop_duplicates() == df3[~t_b]

## subset criteria
df3.drop_duplicates(['A', 'B'])

# WHEN TO USE-------------------------------------------------------

## if you want to keep the first (from top) and remove others
df3.drop_duplicates()
## if you want to do the same from bottom
df3.drop_duplicates(take_last = True)

# purge all values that are duplicates
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # complement where either is true
df3[unique] # this just straight up drops any value that are
# duplicates, including first instance
df3.drop_duplicates() # this keeps the first instance, drops rest
