#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:37:59 2017

@author: YS
"""
from __future__ import division
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import numpy as np

# Pull the data
df_data = pd.read_excel('Path1999to2012.xlsx',sheetname ='2006-2012')
df_data1 = pd.read_excel('USGSBLWHooverDam.xlsx',sheetname ='2006-2012')
df_data2= pd.read_excel('USGSBLWHooverDam.xlsx',sheetname ='1967-2018')

dfHoover = df_data1[1:]

# Group by and sum over years
df = df_data.groupby('Date ').sum()
diff_46_49 = df['Path 46'] - df['Path 49']  
df['Diff4649'] = diff_46_49

# Housekeeping
df = df.reset_index()

# write these tabs to Excel
writer = ExcelWriter('Path_processed.xlsx')
df.to_excel(writer, 'PathDaily')

# Write years to excel
years = range(2006,2013)
current_dates = []
for year in years:
    for date in df['Date ']:
        if date.year == year:
            current_dates.append(True)
        else:
            current_dates.append(False)
    df_current_year = df[current_dates]
    df_current_year.to_excel(writer, str(year))
    current_dates = []
    
writer.save()

# write these tabs to Excel
writer = ExcelWriter('Hoover_processed.xlsx')

# Write years to excel
years = range(2006,2013)
current_dates = []
for year in years:
    for date in dfHoover['datetime']:
        if date.year == year:
            current_dates.append(True)
        else:
            current_dates.append(False)
    df_current_year = dfHoover[current_dates]
    df_current_year.to_excel(writer, str(year))
    current_dates = []
    
writer.save()

#Hoover yearly total 
yrlyHoover = df_data2.groupby('datetime').sum()
