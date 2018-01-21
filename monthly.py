# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 21:16:26 2018

@author: jdkern
"""

from __future__ import division
from pandas import ExcelWriter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data= pd.read_excel('USGSBLWHooverDam.xlsx',sheetname ='1967-2018')
df_data.columns = ['month','day','year','discharge']

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
                     
    
