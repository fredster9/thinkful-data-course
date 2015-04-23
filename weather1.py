# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:27:24 2015

TIME FORMATTING
TIME should either be a UNIX time (that is, seconds since midnight GMT on 1 Jan 1970) or a string formatted as follows: [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] (with an optional time zone formatted as Z for GMT time or {+,-}[HH][MM] for an offset in hours or minutes). For the latter format, if no timezone is present, local time (at the provided latitude and longitude) is assumed.

API CALL FORMAT
https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME

@author: fred
"""

import requests
import datetime
from pandas.io.json import json_normalize
import json
from dateutil.parser import *
import time
import pandas as pd
import sqlite3 as lite
from pandas import Series, DataFrame, Panel
import collections
import pdb

con = lite.connect("weather1.db")
cur = con.cursor()

startpoint = "https://api.forecast.io/forecast/"
API_KEY = "eecedeb1c15c3e42015332728d8f4804"

cities = { "Chicago": '41.837551,-87.681844',
            "Washington": '38.904103,-77.017229',
            "Boston": '42.331960,-71.020173',
            "Philadelphia": '40.009376,-75.133346',
            "New York": '40.663619,-73.938589'
        }
        
###temp_dict = {'date': ['city', 'max_temp']}
temp_dict = {}

for k,v in cities.iteritems():
    city = k
    latlong = v
    print "city + lat, long", city, latlong
    day_counter = 30
    while day_counter > 0:
        start_date = datetime.datetime.now() - datetime.timedelta(days=day_counter)
        start_stamp = int(time.mktime(start_date.timetuple()))
        r_url = (startpoint+API_KEY+"/"+latlong+","+str(start_stamp))
        r = requests.get(r_url)
        rj = r.json()
        max_temp = rj['daily']['data'][0]['apparentTemperatureMax']
        print "on %s max temp in %s was %s" % (start_date,  k, max_temp)
        temp_dict.setdefault(start_date.strftime('%Y%m%d'),[]).append([k, max_temp])
        day_counter -= 1

#pdb.set_trace()

df = pd.DataFrame.from_dict(temp_dict, orient="index")
cols = df[0][0][0],df[1][0][0],df[2][0][0],df[3][0][0], df[4][0][0]
df.columns = cols

### Add for loop to only run when length is 2
for city in cols:
    print city
    if len(df[city][0]) > 1:    
        df[city] = df[city].map(lambda x: x.pop(1))
    
start_index = df.index[0]
rng = pd.date_range(start_index, periods=30, freq='D')

df.index = rng

## THIS IS WHERE THE PROBLEM IS - adding if_exists='replace' DOES NOT WORK
df.to_sql(con=con, name='max_temp')

day_change = collections.defaultdict(int) # currently empty. will become dictionary where k is list of station ids and v is abs change over time

col_count=0
city_change = []   
 
for col in df.columns:
    daily_vals = df[col].tolist()
    temp_change = 0
    #pdb.set_trace()    
    for k,v in enumerate(daily_vals): 
        if k < len(daily_vals) - 1: 
            temp_change += abs(daily_vals[k] - daily_vals[k+1]) 
    print "CITY", df.columns[col_count]
    print "TEMP CHANGE", temp_change
    city_change.append([df.columns[col_count], temp_change])
    col_count += 1

city_zip = zip(*city_change)
winner = map(max, city_zip)

print "The city with the biggest change is %s, with a total change of %s degrees" % (winner[0], winner[1])
        
## Other analsysis: Range, variance, mean

col_count = 0
for col in df.columns:
    print "For the city of ", df.columns[col_count]
    print "Range = ", max(df[col]) - min(df[col])
    print "Mean = ", float("{0:.2f}".format(df[col].mean()))
    print "Variance = ", float("{0:.2f}".format(df[col].var()))
    col_count += 1