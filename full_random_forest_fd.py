# coding: utf-8

'''
## Questions:

Note: this code is almost 100% copied from https://github.com/FrankRuns/Thinkful/blob/master/Unit4/DecisionTrees/random_forest.py

- is there better way to give random column names? my way is unsorted so seems hard to map back
- https://courses.thinkful.com/data-001v1/assignment/4.2.2 they say Plot a histogram of Body Acceleration Magnitude to see how each variable does as a predictor of static versus dynamic activities. -- how do i do this?
- is OOB Score 0 to 1 with 1 being best?
- feature_importances same?
- how to read the confusion matrix chart?
- why are accuracy and recall metrics the same?

- why is the 2nd version (this one) more accurate than prior. all we changed was column names and estimators went from 500 to 50
-- why does https://courses.thinkful.com/data-001v1/project/4.2.4 we're using more/all features now?


'''

## Imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skm
import pylab as pl
import numpy as np

## Activity legend
# 1 = Walking, 2 = Walking Upstairs, 3 = Walking Downstairs, 4 = Sitting, 5 = Standing, 6 = Laying

## Read in data
subjects = pd.read_csv("/Users/fred/Dropbox/Thinkful/UCI HAR Dataset/train/subject_train.txt", header=None, delim_whitespace=True, index_col=False)
feature_names = pd.read_csv("/Users/fred/Dropbox/Thinkful/UCI HAR Dataset/features.txt", header=None, delim_whitespace=True, index_col=False)
x_vars = pd.read_csv("/Users/fred/Dropbox/Thinkful/UCI HAR Dataset/train/X_train.txt", header=None, delim_whitespace=True, index_col=False)
y_vars = pd.read_csv("/Users/fred/Dropbox/Thinkful/UCI HAR Dataset/train/Y_train.txt", header=None, delim_whitespace=True, index_col=False)

## give anonymous names to features
cols = {}
for x in range(1,562):
    cols["x{0}".format(x)]='fill'

## Assign column names
x_vars.columns = cols.keys()
subjects.columns = ['Subject']
y_vars.columns = ['Activity']

## Merge 3 dataframes into 1
data = pd.merge(y_vars, x_vars, left_index=True, right_index=True)
data = pd.merge(data, subjects, left_index=True, right_index=True)

## Make activity a categorical variable
data['Activity'] = pd.Categorical(data['Activity']).labels

## Split out test data
fortrain = data.query('Subject >= 27')
fortest = data.query('Subject<= 6')
forval = data.query("(Subject >= 21) & (Subject < 27)")

## Fit random forest
train_target = fortrain['Activity']
train_data = fortrain.ix[:,1:-2] # slicing columns we don't need
rfc = RandomForestClassifier(n_estimators=50, oob_score=True) # this is 50 now
rfc.fit(train_data, train_target)

## See oob (out of bag) to show accuracty
rfc.oob_score_  # Is this a better score? 

## Determine most important features
importances = rfc.feature_importances_
indices = np.argsort(importances)[::-1] # what is this? np.argsort = Perform an indirect sort along the given axis using the algorithm specified by the kind keyword
for i in range(10): # finding 10 most important
    print("%d. feature %d (%f)" % (i + 1, indices[i], importances[indices[i]]))

## define validation set and make predictions
val_target = forval['Activity']
val_data = forval.ix[:,1:-2] # i changed his code here to match other data slices
val_pred = rfc.predict(val_data)
val_pred

## Define test set and make predictions
test_target = fortest['Activity']
test_data = fortest.ix[:,1:-2]
test_pred = rfc.predict(test_data)
test_pred

## calculate and print accuracy scores
print("mean accuracy score for validation set = %f" % (rfc.score(val_data, val_target)))
print("mean accuracy score for test set = %f" % (rfc.score(test_data, test_target)))

## visualize confusion matrix
test_cm = skm.confusion_matrix(test_target, test_pred)
pl.matshow(test_cm)
pl.title('Confusion matrix for test data')
pl.colorbar()
pl.show()
# confusion matrix lays out instances of predicated class in columns and actual class in row
# i get idea but not how to read

print("Accuracy = %f" %(skm.accuracy_score(test_target, test_pred)))
print("Precision = %f" %(skm.precision_score(test_target, test_pred)))
# Precision = number of true positives vs false positives
print("Recall = %f" %(skm.recall_score(test_target, test_pred)))
print("F1 score = %f" %(skm.f1_score(test_target, test_pred)))
# F1 = weighted average of the precision and the recall. 1 is best value. 


