# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:09:20 2015

@author: fred
"""

import pandas as pd
import math

un_data =  pd.read_csv('un.csv')
gdp_data = pd.read_csv('gdp_data/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv', skiprows = [0,1])

## Set indexes for both dfs to country

print gdp_data.head()

## UN Data
del un_data['#']
un_data.set_index('Country', inplace = True)
un_data['Gap ann_gdp'] = 0
#print un_data.head(10)

## GDP Data - strip unnecessay columns
gdp_data.fillna(value=0, inplace=True)
gdp_data.set_index('Country Name', inplace = True)
del gdp_data['Country Code']
del gdp_data['Indicator Name']
del gdp_data['Indicator Code']
#print gdp_data.head()

## write the GDP to UN df
for country in un_data.index:
    year = un_data.ix[country]['Year']
    if country in gdp_data.index:
        un_data.ix[country]['Gap ann_gdp'] = gdp_data.ix[country][str(year)]
#print un_data.head(10)
        
## Add a column wtih the log(10) of GDP
un_data['Log_GDP'] = 0
## Add avg column
un_data['Ed_Avg'] = (un_data['M'] + un_data['F']) / 2

def get_log(x):
    if x > 0:
        return math.log(x)
    else:
        return 0

un_data['Log_GDP'] = un_data['Gap ann_gdp'].apply(get_log)

un_data_corr = un_data[['M', 'F', 'Ed_Avg', 'Log_GDP']]
un_data_corr = un_data_corr[un_data_corr['Log_GDP'] > 0]
print un_data_corr.corr()

## Turns out education length is only moderately correlated with annual GDP