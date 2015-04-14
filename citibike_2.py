# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 07:48:31 2015

@author: fred
"""

import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import time
from dateutil.parser import parse
import collections

# API call
r = requests.get('http://www.citibikenyc.com/stations/json')

# Create dataframe
df = json_normalize(r.json()['stationBeanList'])

# DB connection
con = lite.connect('citi_bike_3.db')
cur = con.cursor()

# create tables
with con:
    cur.execute('CREATE TABLE IF NOT EXISTS citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')
    
    sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
    
    # wrapped this in data check to see if there is data in table, if so don't run
    populated_check = cur.execute('SELECT rowid FROM citibike_reference WHERE rowid = 1;').fetchone()
    try:
        if populated_check[0] > 1:
            for station in r.json()['stationBeanList']:
                cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
    except:
        print "Column data has already been populated"
        
# extract column from dataframe and put in list
station_ids = df['id'].tolist()
# add '_' to station name + ad ddata type
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

# create the available bikes table
with con:
    cur.execute("CREATE TABLE IF NOT EXISTS available_bikes ( execution_time INT, " + ", ".join(station_ids) + ");")

def update_available_bikes():    
    # API call
    r = requests.get('http://www.citibikenyc.com/stations/json')    
    # take the string and parse to py datetime
    exec_time = parse(r.json()['executionTime'])
    print exec_time
    print exec_time.strftime('%s')
    
    # create entry for exeuction time by inserting into db
    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    
    # iterate through stations in list
    id_bikes = collections.defaultdict(int) # defaultdict to store available bikes by station
    
    # loop through stations in station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']
    
    # iterate through defaultdict to update values in db
    with con:
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
 
times_ran = 0
while times_ran < 61:
    update_available_bikes()
    times_ran += 1
    print "Script has run %r / 60 times" % times_ran
    time.sleep(60)
  

