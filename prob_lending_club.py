# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:13:44 2015

@author: fdintenfass
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)
    
def vis_data(data_column):    
    #print "Null vals",  pd.isnull(loansData) == True # Tried to find null values and failed. Why no work?
    
    print "Size of dataset pre-clean", len(loansData)
    loansData.dropna(inplace=True) # remove rows with null values
    print "Size of dataset post-clean", len(loansData) # apparently there were null values

    print "Data details: \n", loansData[data_column].describe()    
    
    loansData.boxplot(column=data_column)
    plt.show()
    loansData.hist(column=data_column)
    plt.show()
    plt.figure()
    graph = stats.probplot(loansData[data_column], dist='norm', plot=plt)
    plt.show()


vis_data('Amount.Requested')
vis_data('Amount.Funded.By.Investors')


# boxplot comparing the two 
dc1 = list(loansData['Amount.Requested'])
dc2 = list(loansData['Amount.Funded.By.Investors'])
chart_data = [dc1, dc2]
plt.boxplot(chart_data)
plt.grid()
plt.xticks([1,2], ["Amount Requested", "Amount Funded By Investors"])
print loansData['Amount.Requested'].describe()
print loansData['Amount.Funded.By.Investors'].describe()

