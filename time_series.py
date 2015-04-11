# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:36:52 2015

1. Is the series stationary? If not, what would you do to transform it into a stationary series?
- I don't know. Not sure how you can tell seasonality with 12 months of data
- No pattern of significant autocorrelation across 
all lags so would say no
- Dividing each point by media or mean would be one way to make stationary?

2. Plot out the ACF (statsmodels.api.graphics.tsa.plot_acf()) and PACF (statsmodels.api.graphics.tsa.plot_pacf()) of the series (or the transformed series). Are there any autocorrelated structures in the series? How would you have a model address these structures?
- No clue


QUESTIONS:
- Why doesn't week count work when added to lcdf?
- How to change date formatting in 

@author: fred
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('LoanStats3b.csv', low_memory=False)

# converts tring to datetime object in pandas
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dtfs = df.set_index('issue_d_format') 
# setting it as index
year_month_summary = dtfs.groupby(lambda x: x.year * 100 + x.month).count()
#week_month_summary = dtfs.groupby(lambda x: x.year * 100 + x.week).count()
loan_count_summary = year_month_summary['issue_d']
#loan_count_summary_week = week_month_summary['issue_d']


# reindex loan by month by year as dataframe
lcdf = pd.DataFrame(loan_count_summary)
lcdf = lcdf.rename(columns={'issue_d': 'month_count'})

#lcw = pd.DataFrame(loan_count_summary_week)
#lcw = lcw.rename(columns={'issue_d': 'week_count'})
#lcdf['week_count'] = pd.Series(lcw['week_count'])
## adding MoM change column and times result by 100 so reads as % not int
#lcdf['MoM_pct'] = pd.Series(100*(lcdf.month_count.pct_change()), index=lcdf.index)

lcdf.plot()
#x = dtfs.index
#y = dtfs.count(dtfs.id)
#dtfs.plot(x,y)

sm.graphics.tsa.plot_acf(loan_count_summary)
sm.graphics.tsa.plot_pacf(loan_count_summary)

fig = sm.graphics.tsa.plot_acf(df['loan_amnt'])
fig.set_size_inches = (18.5,10.5)
fig.show()
fig.savefig('loan_amnt_acf.png', dpi=100)

#  FOR SOME REASON THIS DOESN'T WORK
fig2 = sm.graphics.tsa.plot_pacf(df['loan_amnt'])
fig2.set_size_inches(18.5, 10.5)
fig.savefig('loan_amnt_pacf.png', dpi=100)