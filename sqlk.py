# JOINing data from multiple tables - cleanup

import sqlite3

# connect to the database
with sqlite3.connect("new.db") as connection:
    # create a cursor
    c = connection.cursor()

    # retrieve the data from the tables
    c.execute("""SELECT DISTINCT population.city, 
                population.population, regions.region 
                FROM population, regions 
                WHERE population.city = regions.city 
                ORDER BY population.city ASC""")
    # get the records from the cursor
    rows = c.fetchall()
    # print the record values
    for row in rows:
        print "City: " + row[0]
        print "Population: " + str(row[1])
        print "Region: " + row[2]
        print 