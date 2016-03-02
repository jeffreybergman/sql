# executemany() method

import sqlite3

# create a database connection
with sqlite3.connect("new.db") as connection:
    # get a cursor object
    c = connection.cursor()
    # insert multiple records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000), 
            ('Phoenix', 'AZ', 1500000),
            ]
    # insert data into the table
    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)