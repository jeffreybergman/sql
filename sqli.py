# create a table and populate with data

import sqlite3

# create a database connection
with sqlite3.connect("new.db") as connection:
    # create a cursor
    c = connection.cursor()

    # create new table
    c.execute("""CREATE TABLE regions 
                (city TEXT, region TEXT)
                """)
    # insert multiple records using a tuple
    cities = [
                ('New York City', 'Northeast'),
                ('San Francisco', 'West'),
                ('Chicago', 'Midwest'),
                ('Houston', 'South'),
                ('Phoenix', 'West'),
                ('Boston', 'Northeast'),
                ('Los Angeles', 'West'),
                ('Houston', 'South'),
                ('Philadelphia', 'Northeast'),
                ('San Antonio', 'South'),
                ('San Diego', 'West'),
                ('Dallas', 'South'),
                ('San Jose', 'West'),
                ('Jacksonville', 'South'),
                ('Indianapolis', 'Midwest'),
                ('Austin', 'South'),
                ('Detroit', 'Midwest'),
            ]
    # insert tuple values into regions table
    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
    # select records from regions table into cursor
    c.execute("SELECT * FROM regions ORDER BY region ASC")
    # get all records from cursor
    rows = c.fetchall()
    # display record values
    for row in rows:
        print row[0], row[1]
