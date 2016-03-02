# INSERT Command

# import the sqlite3 library
import sqlite3

# use the with keyword to create the connection
with sqlite3.connect("new.db") as connection:
    # get a cursor object
    c = connection.cursor()
    # insert data
    c.execute("INSERT INTO population VALUES('New York City', \
        'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \
        'CA', 800000)")
