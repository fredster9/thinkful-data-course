# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:51:01 2015

@author: fred
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('sqlite_exercise.db')

cities = (
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')
)

weather = (
    ('New York City', 2013, 'July', 'January', 62 ),
    ('Boston', 2013, 'July', 'January', 59 ),
    ('Chicago', 2013, 'July', 'January', 59 ),
    ('Miami', 2013, 'august', 'January', 84 ),
    ('Dallas', 2013, 'July', 'January', 77 ),
    ('Seattle', 2013, 'July', 'January', 61 ),
    ('Portland', 2013, 'July', 'December', 63 ),
    ('San Francisco', 2013, 'September', 'December', 64 ),
    ('Los Angeles', 2013, 'September', 'December', 75 )
)

with con:
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cities(
            name TEXT PRIMARY KEY,
            state TEXT
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS weather(
            city TEXT PRIMARY KEY,
            year INTEGER,
            warm_month TEXT,
            cold_month TEXT,
            average_high INTEGER        
        )    
    ''')
    
    cur.executemany("INSERT OR IGNORE INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT OR IGNORE INTO weather VALUES(?,?,?,?,?)", weather)

    cur.execute('''
        SELECT name, state, year, warm_month, cold_month,average_high FROM cities INNER JOIN weather ON name = city;
    ''')
    combined_tables = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    #print cols
    df = pd.DataFrame(combined_tables)    
    #df2 = pd.DataFrame(combined_tables, columns = cols) # adds header 
    
    # using iterrrows
    city_list = []
    for row_index, row, in df.iterrows():
        if row[3] == 'July':
            city_list.append((row[0], row[1]))
    print type(city_list)
    print "The cities that are warmest in July are: ", city_list
    
    # using pandas slice
#    data = df2[['name', 'state']]
#    print data
#    print list(data)
#    print df2.describe()

print "Program done"