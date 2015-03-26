# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:01:17 2015

@author: fred

Challenge: Write a script called "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson. Make sure your plots have names that are reasonably descriptive.

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.stats as stats
import collections
import pandas as pd

data_set = np.random.normal(size=1000)

def prob(data_set):
    
    # output frequencies
    c = collections.Counter(data_set)
    count_sum = sum(c.values())
    for k, v in c.iteritems():
        print "The frequency of number " + str(k) + " is " + str(float(v)/count_sum)
    print "\nThere are %d values in the data." % count_sum
    print "There are %r unique values." % len(set(c))
    df = pd.DataFrame(data_set)
    print "Stats describing the data set \n", df.describe()
    print "Variance is ", df.var()
    
    # create and save boxplot
    vals = list(c.iterkeys())  
    plt.boxplot(vals)
    plt.suptitle("Boxplot to show value distribution")
    plt.savefig("prob_boxplot.png") # needs to be before show
    plt.show()
    
    # create and save histogram
    plt.suptitle("Histogram showing frequency distribution")    
    plt.hist(vals, histtype="bar")
    plt.savefig("prob_histplot.png")
    plt.show()
    
    # create and save QQ plot
    plt.figure()
    plt.suptitle("QQ Plot showing probability density")
    graph1 = stats.probplot(data_set, dist="norm", plot = plt)
    plt.savefig("prob_qqplot.png")    
    plt.show()

    
prob(data_set)