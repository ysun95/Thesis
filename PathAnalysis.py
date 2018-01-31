#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:15:23 2018

@author: YS
"""
from __future__ import division
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import numpy as np

df_data= pd.read_excel('46vHoover.xlsx',sheetname ='Path')
df_data1= pd.read_excel('46vHoover.xlsx',sheetname ='Hoover')
df_data.columns = ['month','day','year','MW']
df_data1.columns = ['month','day','year','discharge']

#extract 2006-2012 Path data
years = range(2006,2013)
months = range(1,13)

# PATHmonthly data
data_monthly = []

for i in years:
    
    for j in months:

      e = df_data.loc[(df_data['month'] == j) & (df_data['day'] == 1) & (df_data['year'] == i)].index
      e = e[0]
       
      trigger = 0
      summed_flow = 0
       
      while trigger < 1:
           
           if df_data.loc[e,'month'] != j:
               trigger = 1
        
           if trigger < 1:
               summed_flow = summed_flow + df_data.loc[e,'MW']
                
           if e < len(df_data) - 1:
               e = e + 1
           else: 
               trigger = 1
        
      data_monthly = np.append(data_monthly,summed_flow)
                     

#HOOVERyearly data
num_years = int(len(data_monthly)/12)
yearlySum=[]
yearlyData=[]

for i in range(0,num_years):

    yearlySum = np.sum(data_monthly[i*12:i*12+12])
    yearlyData = np.append(yearlyData,yearlySum)


#extract 2006-2012 HOOVER data
years1 = range(2006,2011)
months1 = range(1,13)

# PATHmonthly data
data_monthly1 = []

for i in years1:
    
    for j in months1:

      e = df_data1.loc[(df_data1['month'] == j) & (df_data1['day'] == 1) & (df_data1['year'] == i)].index
      e = e[0]
       
      trigger = 0
      summed_flow = 0
       
      while trigger < 1:
           
           if df_data1.loc[e,'month'] != j:
               trigger = 1
        
           if trigger < 1:
               summed_flow = summed_flow + df_data1.loc[e,'discharge']
                
           if e < len(df_data) - 1:
               e = e + 1
           else: 
               trigger = 1
        
      data_monthly1 = np.append(data_monthly1,summed_flow)
                     

#HOOVERyearly data
num_years1 = int(len(data_monthly1)/12)
yearlySum1=[]
yearlyData1=[]

for i in range(0,num_years1):

    yearlySum1 = np.sum(data_monthly1[i*12:i*12+12])
    yearlyData1 = np.append(yearlyData1,yearlySum1)
