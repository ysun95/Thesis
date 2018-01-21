#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:45:04 2018

@author: YS
"""

from __future__ import division
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import numpy as np

df_data= pd.read_excel('USGSBLWHooverDam.xlsx',sheetname ='1967-2018')
df_data1= pd.read_excel('USGSBLWHooverDam.xlsx',sheetname ='1967-2018Adj')
df_data.columns = ['month','day','year','discharge']
df_data1.columns = ['year', 'discharge']

#extract 1967-2018 Hoover discharge data
years = range(1967,2017)
months = range(1,13)

# monthly data
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
               summed_flow = summed_flow + df_data.loc[e,'discharge']
                
           e = e + 1
        
      data_monthly = np.append(data_monthly,summed_flow)
                     

#yearly data
num_years = int(len(data_monthly)/12)
yearlySum=[]
yearlyData=[]

for i in range(0,num_years):

    yearlySum = np.sum(data_monthly[i*12:i*12+12])
    yearlyData = np.append(yearlyData,yearlySum)


#extract 1967-2016 yearly discharge data
s = df_data1.year[df_data1.year == '1/1/1967 00:00:00'].index
s = s[0]

e = df_data1.year[df_data1.year == '1/1/2016 00:00:00'].index
e = e[0]

data = []
for i in range(s,e+1):
    data = np.append(data,df_data.loc[i,'discharge'])
    
#histogram
plt.figure()
plt.hist(data)
plt.xlabel('Yearly Discharge',fontsize=10)
plt.ylabel('Frequency',fontsize=10)

# 12 x N matrix
# annual profile
def vec2mat(d,rows):
    
    #number of years in record
    columns = int(len(d)/rows)
    
    #output matrix of zeros
    output = np.zeros((rows,columns))
    
    #nested for loop
    for i in range(0,columns):
        for j in range(0,rows):
            output[j,i] = d[i*rows+j]

    return output
#call annual profile function
x = vec2mat(data_monthly,12)

#use the boxplot fnt to plot log transformed data
#take transformed data and make into a 12xN matrix---make a boxplot of this

boxplotdata = [x[0,:],x[1,:],x[2,:],x[3,:],x[4,:],x[5,:],x[6,:],x[7,:],x[8,:],x[9,:],x[10,:],x[11,:]]
plt.figure()
plt.boxplot(boxplotdata)
plt.xlabel('Month',fontsize=10)
plt.ylabel('Discharge (cubic feet)',fontsize=10)
