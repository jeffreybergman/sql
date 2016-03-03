# JOINing data from multiple tables

import sqlite3

# connect to the database
with sqlite3.connect("new.db") as connection:
    # create a cursor
    c = connection.cursor()

    # retrieve the data from the tables
    c.execute("""SELECT population.city, population.population,
                regions.region FROM population, regions 
                WHERE population.city = regions.city""")
    # get the records from the cursor
    rows = c.fetchall()
    # print the record values
    for row in rows:
        print row[0], row[1], row[2]