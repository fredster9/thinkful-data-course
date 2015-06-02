
## Imports
get_ipython().magic(u'matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import sklearn.metrics as skm
import pylab as pl
import numpy as np


## Read in data
data = pd.read_csv("/Users/fred/Dropbox/Thinkful/ideal_weight.csv")

# Remove single quotes from column names
data.columns = data.columns.map(lambda x: (x.replace("'", ''))) 
# Remove single quotes from column values
data.sex = data.sex.map(lambda x: (x.replace("'", '')))

# Make sex a categorical var
#data['sex'] = pd.Categorical(data['sex']).labels
data['sex'] = data['sex'].astype('category')

# Are there more women than men? - Yes
data.groupby(['sex']).size()


data['diff'].hist(bins=20)
data[['actual', 'ideal']].hist()
weights = data[['actual', 'ideal']]
weights
plt.figure;
weights.plot(kind='hist', bins=20, alpha=0.75)

## Fit Naive Bayes classifier of sex to actual weight, ideal weight, and diff.
clf = GaussianNB()
Y = data.sex
Y = np.array(Y)
X = data[['actual', 'ideal', 'diff']]
X = np.array(X)
clf.fit(X,Y)

y_pred = clf.fit(X, Y).predict(X)
print("Number of mislabeled points out of a total %d points : %d"  % (X.shape[0],(Y != y_pred).sum()))
print("Accuracy was %f percent") % (float(correct * 1000) / X.shape[0]) 
#Number of mislabeled points out of a total 182 points : 14
#Accuracy was 76.923077 percent


## Make predictions
print clf.predict([[145, 160, -15]])
print clf.predict(([[160, 145, 15]]))
#['Male']
#['Female']

#data['sex'].cat.codes.head()
# 1 = Male
# 2 = Female
# Alphabetical?
