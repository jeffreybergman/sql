# SQLite Functions

import sqlite3

# connect to the database
with sqlite3.connect("new.db") as connection:
    # create a cursor
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {"average": "SELECT AVG(population) FROM population",
            "maximum": "SELECT MAX(population) FROM population",
            "minimum": "SELECT MIN(population) FROM population",
            "sum": "SELECT SUM(population) FROM population",
            "count": "SELECT COUNT(city) FROM population",}

    # run each query in the dictionary
    for keys, values in sql.iteritems():
        # run the query
        c.execute(values)
        # fetchone() retrieves one record from the query
        result = c.fetchone()
        # print record to screen
        print keys + ":" + str(result[0])