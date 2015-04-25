# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:17:18 2015

@author: fdintenfass
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import csv
import sqlite3 as lite

con = lite.connect("gdp.db")
cur = con.cursor()



#url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
#
#r = requests.get(url)
#
#soup = BeautifulSoup(r.content)
#data = soup('table')[6].find_all('tr')
#data = data[3]
#data = data('table')[0]
#data = data('tr')
#
#datarows = []
#for i in range(4, len(data)):
#	tags = data[i]
#	values = [tag.string for tag in tags('td')]
#	datarows.append(list(values[i] for i in [0, 1, 7, 10]))
#
## convert the list of lists to a list of tuples
#datarows = [tuple(element) for element in datarows]
#
#cols = ["Country", "Year", "M", "F"]
#df = pd.DataFrame(datarows, columns=cols)
#df.M = df.M.astype(int)
#df.F = df.F.astype(int)
#print "Men: median is %f and mean is %f" % (df.M.median(), df.M.mean())
#print "Women: median is %f and mean is %f" % (df.F.median(), df.F.mean())
### Mean more appropriate??
### Not necessarily, median is less likely to move around due to outliers
### Median is more robust statistic than mean
#
### Create gap columns, higher the # the less ed women get
#df['Gap'] = pd.Series(df.M - df.F, index=df.index)
#df.sort('Gap', ascending=False, inplace=True)
#
#print "Countries where men get more education", df[:10]
#
#df.sort('Gap', ascending=True, inplace=True)
#
#print "Countries where women get more education", df[:10]

with open('gdp_data/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
       next(inputFile)
    header = csv.reader(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('CREATE TABLE IF NOT EXISTS gdp(country_name TEXT PRIMARY KEY, _1999 INT, _2000 REAL, _2001 REAL, _2002 REAL, _2003 REAL, _2004 REAL, _2005 REAL, _2006 REAL, _2007 REAL, _2008 REAL, _2009 REAL, _2010 REAL, STH BLOG, ST2 BLOB);')
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-5]) + '");')
