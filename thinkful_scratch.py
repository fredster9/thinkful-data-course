from datetime import datetime
import logging
import collections
import csv
import pandas as pd
import sqlite3 as lite

# actors = {
#     "Kyle MacLachlan": "Dale Cooper",
#     "Sheryl Lee": "Laura Palmer",
#     "Lara Flynn Boyle": "Donna Hayward",
#     "Sherilyn Fenn" : "Audrey Horne"
# }
#
# for x in actors:
#     print x, "played", actors[x]

# miles_run = 0
# running = True
#
# while running:
#     if miles_run <= 10:
#         print ("Still running! On mile {}".format(miles_run))
#         miles_run += 1
#     else:
#         running = False
#
# else:
#     print("Whew! I'm tired")

# miles_walked = 0
# walking = True
# leic = 0
# london = 0
#
# while walking:
#     if leic + london != 102:
#         leic += 2
#         london += 1
#         print("Still walking, total miles is {}".format(leic+london))
#     else:
#         walking = False
#
# else:
#     print ("They met when leic = %s and london = %s" % (leic, london))

# phone_book = {
#     "Sarah Hughes": "01234 567890",
#     "Tim Taylor": "02345 678901",
#     "Sam Smith":  "03456 789012"
# }
#
# try:
#     print phone_book["Jamie Theakson"]
# except KeyError:
#     print "User not found"

# number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
# count_dict = collections.defaultdict(int)
# for i in number_list:
#     count_dict[i] += 1
# print count_dict
# # # same way to do that is
# count = collections.Counter(number_list)
# print count



# def log_handler(msg):
#     """Sends msg to the logging platform"""
#     date = str(datetime.now())
#     msg = date + " - " + msg
#     return logging.info(msg)
#
# def log(msg):
#     """A convenience function. Adds msg to the logs with log_handler"""
#     msg = str(msg)
#     print("Message logged: " + msg)
#     return log_handler(msg)
#
# def addition(a, b):
#     """Adds two numbers and logs the result"""
#     x = a + b
#     log("Adding {0} and {1} = {2}.".format(a, b, x))
#     return x
#
# addition(1, 2)
# addition(2, 3)
# addition(5, addition(3, 5))

# ingredients = {
#     "butter"  : ("butter", 118.3),
#     "sugar"   : ("sugar", 236.6),
#     "vanilla" : ("vanilla", 4.929),
#     "eggs"    : ("eggs", 2), # whole eggs
#     "cocoa"   : ("cocoa", 118.3),
#     "flour"   : ("flour", 118.3)
# }
#
# # The butter was refrigerated, so it's not soft yet.
# butter_soft = False
#
# bowl = []
#
# # To make the cake, we'll need the following functions
# def melt(this):
#     print("Melting {0}.".format(this))
#
# def bake(this, temp):
#     print("Baking {0} at {1}.".format(this, temp))
#
# def mix(this):
#     print("Mixing {0}.".format(this))
#
# def add_to_bowl(ingredient):
#     print("Adding {0} to the bowl.".format(ingredient))
#     return bowl.append(ingredient)
#
#
# ##### Start the algorithm! #####
#
# if butter_soft != True:
#     melt(ingredients["butter"][0])
#     butter_soft = True
#
# add_to_bowl(ingredients["butter"][0])
# add_to_bowl(ingredients["sugar"][0])
#
# mixing_time = 0
# mixture_creamy = False
#
# # Mix until creamy
# while mixture_creamy == False:
#     mix(bowl)
#     mixing_time += 1
#     if mixing_time == 3:
#         # After 3 minutes, the mixture will be creamy,
#         # and our while loop will stop
#         mixture_creamy = True
#
# add_to_bowl(ingredients["eggs"][0])
# add_to_bowl(ingredients["vanilla"][0])
#
# mix(bowl)
#
# add_to_bowl(ingredients["cocoa"][0])
# add_to_bowl(ingredients["flour"][0])
#
# mixing_time = 0
# well_blended = False
#
# # Mix until well-blended
# while well_blended == False:
#     mix(bowl)
#     mixing_time += 1
#     if mixing_time == 4:
#         well_blended = True
#
# # In cooking terms: pour contents of the bowl into a cake pan
# # In Python terms: redefine the bowl variable as cake_pan
# cake_pan = bowl
#
# cooking_temp = 350
# cooking_time = 30
#
# for minute in range(0, cooking_time):
#     bake(cake_pan, cooking_temp)
#
# print("Cake is done!")

## Fibonacci
# def F(n):
#     if n == 0:
#         return 0
#     elif n== 1:
#         return 1
#     else:
#         return F(n-1) + F(n-2)
#
# for x in range(0,10):
#     print F(x)

# for x in range (1,100):
#     if x %3 == 0 and x % 5 == 0: # x % 15 == 0
#         print "FizzBuzz"
#     elif x % 3 == 0:
#         print "Fizz"
#     elif x % 5 == 0:
#         print "Buzz"
#     else:
#         print x

#population_dict = collections.defaultdict(int)
#with open('/Users/fred/Downloads/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
#    header = next(inputFile)    
#    header = header.rstrip().split(',')    
#    
#    for line in inputFile:
#        line = line.rstrip().split(',')        
#        line[5] = int(line[5])
#        if line[1] == 'Total National Population':
#            population_dict[line[0]] += line[5]
#    print population_dict
#    
#with open('/Users/fred/Dropbox/Thinkful/national_population.csv', 'w') as outputFile:
#    outputFile.write('continent,2010_population\n')
#    
#    for k,v in population_dict.iteritems():
#        outputFile.write(k + ',' + str(v) + '\n')

# population density

#population_dict = collections.defaultdict(int)
#landmass_dict = collections.defaultdict(int)
#
#with open('/Users/fred/Downloads/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
#    header = next(inputFile)
#
#    for line in inputFile:
#        line = line.rstrip().split(',')
#        line[5] = int(line[5])
#        line[7] = int(line[7])
#        if line[1] == 'Total National Population':
#            population_dict[line[0]] += line[5]
#            landmass_dict[line[0]] += line[7]

#with open('national_population.csv', 'w') as outputFile:
#    outputFile.write('continent,2010_population\n')

#    for k, v in population_dict.iteritems():
#        print "Population dict", (k + ',' + str(v) + '\n')
#            
#    for k, v in landmass_dict.iteritems():
#        print "Landmass dict", (k + ',' + str(v) + '\n')
        
#for k in population_dict:
#    print "Country: ", k
#    print landmass_dict[k]
        
        
## PANDAS LESSON ##

#with open ('/Users/fred/Downloads/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv', 'rU') as inputFile:
#    inputReader = csv.reader(inputFile)
#    for line in inputReader:
#        print len(line)

#input_dataframe = pd.read_csv('/Users/fred/Downloads/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')
#print input_dataframe['Continent']
#print input_dataframe[0:10]

# create connection object
con = lite.connect('getting_started.db')

with con:
    # create cursor object
    cur = con.cursor()
#    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
#    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
#    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 45)")
#    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 52)")
    cur.execute("SELECT * FROM cities")
    
    rows = cur.fetchall()
#    for row in rows:
#        print row
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows)