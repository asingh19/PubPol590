from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd 

###DATA FILES (ex File1.txt) need to be in last folder mentioned in the main_dir pathway on code line 16
### PLEASE NOTE THAT READING EXCEL FILE REQUIRES XLRD, WHICH MAY NOT BE A CANOPY DEFAULT, USE PACKAGE MANAGER
###This can be run with a CSV of the ID excel sheet, line codes 18, 84-93 need to be activated
### THE CSV FILE IS ALSO IN OUR REPO named "IDS.csv"
### The default is to use the excel file (code starts at line 16 and then again at line 95)

### The final DataFrames are df_csv (made using csv file) and df_excel (made using excel file, which is default)


main_dir = "/Users/amitpalsingh/Documents/Duke Academics/Spring 2015/PubPol 590 Big Data/02 CER_both/CER Electricity Revised March 2012/DATA/"
excel_file = "SME and Residential allocations.xlsx"


#import, iterating through a loop
paths = [main_dir + v for v in os.listdir(main_dir) if v.startswith("File")]
lists = [pd.read_table(v, names = ['panid', 'date', 'kwh'], sep = " ") for v in paths]
dftotal = pd.concat(lists, ignore_index = True)

#####CLEANING DATA####----------------------------------------------------------
#drop pure duplicates-----------------------------------------
#dftotal = dftotal.drop_duplicates()

#seperating hours from days-------------------------
#hours = dftotal['date'] % 100
#days = dftotal['date'] // 100
#dftotal['days'] = days
#dftotal['hours'] = hours
#del dftotal.date


###Day light savings###--------------------------------------------------------------
#dftotal[dftotal.days == 452] #not in data
#dftotal[dftotal.days == 669] #not in data
#dftotal[dftotal.days == 298] #in data

###IMPORTING AND MERGING ID DATA###---------------------------------------------

#Working with excel sheet-----------------------------------------------------
exl = pd.read_excel(main_dir + excel_file, parse_cols = "A:E")
exl.columns = ['panid', 'code', 'tariff', 'stim', 'SME']
del exl['SME']
exl
exl2 = exl[exl.code == 1]
exl2
exl3 = exl2[(exl2.stim == 'E') | ((exl2.stim == '1') & (exl2.tariff == 'A'))]




exl2 = exl[exl.Code == 3]
exl3 = exl.drop(exl2.index)

df_xl = pd.merge(dftotal, exl3, how = "outer")
frtn = df_xl[df_xl.hours == 49]
no_frtn = df_xl.drop(frtn.index)
fty = no_frtn[no_frtn.hours == 50]
df_excel = no_frtn.drop(fty.index)

