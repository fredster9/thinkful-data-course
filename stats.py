# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:05:34 2015

@author: fred
"""

import pandas as pd
#from collections import Counter
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()

data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1::] # all the following rows
df = pd.DataFrame(data_rows, columns = column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#print "MODE " stats.mode(df['Alcohol'])
print "Alcohol Mode: ", stats.mode(df['Alcohol'])

# mean, median, mode, range, std, var

def calcs (col_name):
    val_mean = df[col_name].mean()
    val_median = df[col_name].median()    
    val_mode = stats.mode(df[col_name])  
    val_range = df[col_name].max() - df[col_name].min()
    val_std = df[col_name].std()
    val_var = df[col_name].var()
    
    print "For the %s dataset: " % col_name    
    print "  The mean is: %r " % val_mean
    print "  The median is: %r " % val_median
    print "  The mode is: ", val_mode
    print "  The range is: %r " % val_range
    print "  The standard deviation is: %r " % val_std
    print "  The variance is: %r " % val_var


calcs('Alcohol')
calcs('Tobacco')