# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:47:12 2015

FROM http://www.datarobot.com/blog/ordinary-least-squares-in-python/

@author: fred
"""

# load numpy and pandas for data manipulation
import numpy as np
import pandas as pd

# load statsmodels as alias ``sm``
import statsmodels.api as sm
import matplotlib.pyplot as plt

# load the longley dataset into a pandas data frame - first column (year) used as row labels
df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/datasets/longley.csv', index_col=0)

# will use Employed as y/response and GNP as preditor/X

# break out single response variable and store separately. add constnat to fit intecept of model.

y = df.Employed # response
X = df.GNP # predictor
X = sm.add_constant(X) # add constant

# perform regression fo the predictor on the response 
est = sm.OLS(y, X)

# fit the model
est = est.fit()
print "GNP rsquared = ", est.rsquared


## pick 100 points equally spaced from min to max but since we only have 16 points only get that many here
#X_prime = np.linspace(X.GNP.min(), X.GNP.max(), 100)[:, np.newaxis]
#X_prime = sm.add_constant(X_prime) # add constant
#
## caluclate the predicted values
#y_hat = est.predict(X_prime)
#
## plot these estimations
#plt.scatter(X.GNP, y, alpha=0.3) # plot the raw data
#plt.xlabel("Gross National Product")
#plt.ylabel("Total Employment")
#plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9) # Add the regression line colored in red
## alpha refers to color


### Add variable Armed Forces to model for practice ###
y = np.matrix(df.Employed).transpose()
x1 = np.matrix(df.GNP).transpose()
x2 = np.matrix(df['Armed.Forces']).transpose()

x = np.column_stack([x1, x2])

X1 = sm.add_constant(x)
model = sm.OLS(y,X1)
f = model.fit()

print "GNP and Armed Forces rsquared = ", f.rsquared

if est.rsquared > f.rsquared:
    print "Univariate wins"
else:
    print "Multivariate wins"
