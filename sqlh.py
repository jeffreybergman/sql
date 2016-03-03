#executemany() method

import sqlite3

# create a database connection
with sqlite3.connect("new.db") as connection:
    # create a cursor
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
                ('Boston', 'MA', 600000),
                ('Los Angeles', 'CA', 38000000),
                ('Houston', 'TX', 2100000),
                ('Philadelphia', 'PA', 1500000),
                ('San Antonio', 'TX', 1400000),
                ('San Diego', 'CA', 130000),
                ('Dallas', 'TX', 1200000),
                ('San Jose', 'CA', 900000),
                ('Jacksonville', 'FL', 800000),
                ('Indianapolis', 'IN', 800000),
                ('Austin', 'TX', 800000),
                ('Detroit', 'MI', 700000),
            ]
    # insert tuple values into population table
    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
    # select records from population > 1M
    c.execute("SELECT * FROM population WHERE population > 1000000")
    # get all records from cursor
    rows = c.fetchall()
    # display record values
    for row in rows:
        print row[0], row[1], row[2]
