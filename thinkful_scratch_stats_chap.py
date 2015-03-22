# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:29:13 2015

@author: fred
"""

import pandas as pd
from collections import Counter
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
#print df.dtypes
#print data_rows

## find mean, median, and mode
## DONE BY HAND

#def calc_mean(col_name, col_position):
#    i = 0
#    vals = []
#    for x in data_rows:
#        vals.append(float(x[col_position]))
#        i += 1
#    vals.sort()
#    
##    #Mode    
#    vals_count = Counter(vals)
#    if len(vals_count.most_common()) > 1:
#        print col_name, "has multiple modes"
#    else:
#        mode = vals_count.most_common()
#        print "Mode %s: %r" % (col_name, mode)
##        
##    # Median    
#    off_pos_down = int((i/2) - .5)
#    off_pos_up = int((i/2) + .5)
#    off_pos_down_val = vals[off_pos_down]
#    off_pos_up_val = vals[off_pos_up]    
#    if i % 2 == 0:
#        print "List is even number of vals"
#        median = (off_pos_down_val + off_pos_up_val) / 2.0
#        
#    else:   
#        median = off_pos_up_val
#
##        
##    # Mean
#    print "Mean %s: %r" % (col_name, sum(vals)/i)    
#    print "Median %s: %r" % (col_name, median)
#
#calc_mean('Alcohol', 1)
#calc_mean('Tobacco', 2)

## find mean, median, and mode
## USING BUILT-IN FUNCTIONS

#print "Alcohol Mean: ", df['Alcohol'].mean()
#print "Alcohol Median: ", df['Alcohol'].median()
print "Alcohol Mode: ", stats.mode(df['Alcohol']) # if all occur equally stats will return lowest number
#
#print "Tobacco Mean: ", df['Tobacco'].mean()
#print "Tobacco Median: ", df['Tobacco'].median()
#print "Tobacco Mode: ", stats.mode(df['Tobacco'])

# Range
val_range = max(df['Alcohol']) - min(df['Alcohol'])
val_std = df['Alcohol'].std()
val_var = df['Alcohol'].var()

