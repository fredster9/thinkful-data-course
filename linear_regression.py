# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:36:39 2015

@author: fred
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


ld = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

## Strip % signs from Interest.Rate
ld['Interest.Rate'] = ld['Interest.Rate'].map(lambda x: x.strip('%'))
ld['Interest.Rate'] = ld['Interest.Rate'].astype(float)

## Remove 'months' from Loan Length and convert to integer - from tutorial
cleanLoanLength = ld['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

ld['Loan.Length'] = cleanLoanLength

## Process FICO score range to get low end into new col
# Add new column
ld['FICO.Score'] = pd.Series('', index=ld.index)

# Convert FICO.Range from object to str
print type(ld['FICO.Range'])
ld['FICO.Range'] = ld['FICO.Range'].map(lambda x: x.split('-'))
ld['FICO.Range'] = ld['FICO.Range'].astype(str)
ld['FICO.Score'] = ld['FICO.Range'].map(lambda x: int(x[2:5]))

#plt.figure()
#graph = ld['FICO.Low'].hist()
#plt.show()

#a = pd.scatter_matrix(ld, alpha = 0.5, figsize=(10,10), diagonal="hist")

## Doing the linear regression
intrate = ld['Interest.Rate']
loanamt = ld['Amount.Requested']
fico = ld['FICO.Score']

# Reshape column data returned as series
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variable reshaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Put columns together to create input matrix w/ one col for each independent variable
x = np.column_stack([x1,x2])

# Create linear model
X = sm.add_constant(x) # add_constants appends col of ones to array if prepend == False
model = sm.OLS(y,X) # OLS = ordinary least squares model
f = model.fit() # fit the model

# Output the results
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

''' Results
Coefficients:  [ 72.88279832  -0.08844242]
Intercept:  0.000210747768548
P-Values:  [  0.00000000e+000   0.00000000e+000   5.96972978e-203]
R-Squared:  0.656632624649 
'''







