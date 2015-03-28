# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:30:24 2015

@author: fred
"""

from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
# print freq
print "There are %d rows in the dataset." % len(loansData)
print "There are %d unique values in the data." %  len(freq)
print "The most frequent number is: ",  max(freq.itervalues())

loansData.hist(column = 'Open.CREDIT.Lines') # column names are case sensitive

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# chi-squared answers is if data is evenly distributed
chi, p = stats.chisquare(freq.values())
print "Chi: ", chi
print "P-value: ", p

# if p <= 0.05 (typically), then reject null hypothesis