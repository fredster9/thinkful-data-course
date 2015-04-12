# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:50:20 2015

looking at: http://www.markhneedham.com/blog/2015/04/05/r-markov-chain-wikipedia-example/

@author: fred
"""

import pandas as pd
df = pd.DataFrame({
    'rainy': [.4, .7], 
    'sunny': [.6, .3]
                  }, 
    index=["rainy", "sunny"])
print df

# for two transitions
print df.dot(df)

# below diagram represents whether a hypothetical stock makret is exhibitin bull, bear, or stagnant market rend during a given week

# bull followed by bull 90% of time, bear 7.5%, and stagnant 2.5%

# added the letters so it would index symmetrically

# why is mine flipped 90 degrees from exmaple in url?

df2 = pd.DataFrame({
    'a_bull': [.9, .075, .025],    
    'b_bear': [.15, .8, .05],
    'c_stagnant': [.25, .25, .5 ]
    },
    index = ['a_bull', 'b_bear', 'c_stagnant'])

#trying to switch to match to see if other stuff in example works
df3 = pd.DataFrame({
    'a_bull': [.9, .15, .25],    
    'b_bear': [.075, .8, .25],
    'c_stagnant': [.025, .05, .5 ]
    },
    index = ['a_bull', 'b_bear', 'c_stagnant'])

print df2.dot(df2).dot(df2)
# not at all the answers gotten here 

# still doesn't match.... now it does. This is still 3 weeks>
three_it =  df3.dot(df3).dot(df3)
print three_it
# to see likely hood in three weeks of each type when STARTING WITH bear
print three_it.ix['b_bear']

print "Chance of still being in a bear market is %.2f, with a %.2f chance of being in a bull market, and %.2f chance of being in a stagnant market" % (three_it.ix['b_bear']['b_bear'], three_it.ix['b_bear']['a_bull'], three_it.ix['b_bear']['c_stagnant'])



