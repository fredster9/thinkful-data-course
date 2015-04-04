# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:09:23 2015

@author: fred
"""

import pandas as pd
import statsmodels.api as sm
import math

df = pd.read_csv('loansData_clean.csv')

# Add 'Interest Rate Less Than 12%' column
df['IR_TF'] = pd.Series('', index=df.index)
df['Intercept'] = pd.Series(1.0, index=df.index)

# Populate column
df['IR_TF'] = df['Interest.Rate'].map(lambda x: True if x < 12 else False)

# create list of ind var col names
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept'] 

# define the logistic regression model
logit = sm.Logit(df['IR_TF'], df[ind_vars])
# fit hte model
result = logit.fit()
#get the fitted coefficients from the results
coeff = result.params
#print coeff # gives coeff of each ind/predictor var

print coeff

FICO_coeff = coeff[0]
AmtReq_coeff = coeff[1]
intercept = coeff[2]

# take FICO and loan amount of linear predictor and return p - likelihood interest rate will be under 12%
def logistic_function(FICOScore, LoanAmount):
    FICO_coeff = coeff[0]
    AmtReq_coeff = coeff[1]
    intercept = coeff[2]
    #print "coefficients", FICO_coeff, AmtReq_coeff, intercept
    logit_result = 1/(1 + math.exp(-1*(intercept + FICO_coeff*FICOScore + AmtReq_coeff*LoanAmount)))
    print logit_result
    pred(logit_result)

def pred(logit_result):
    if logit_result >= 0.7:
        print "Loan with interest rate of 12% or lower will be approved"
    else:
        print "Loan with interest rate of 12% or lower will not be approved"
    
print "750 / 10,000:"
logistic_function(750, 10000)
print "720 / 10,000:"
logistic_function(720, 10000)
print "810 / 15,000:"
logistic_function(810, 15000)
print "700 / 10,000:"
logistic_function(700, 10000)
print "810 / 45,000:"
logistic_function(810, 45000)
print "810 / 100,000:"
logistic_function(810, 100000)
