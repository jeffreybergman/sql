# Assignment 3a - insert random data

import sqlite3
import random

# connect to the database
with sqlite3.connect("newnum.db") as connection:
    # create the cursor
    c = connection.cursor()

    # delete the table if exists
    c.execute("DROP TABLE IF EXISTS numbers")

    # create the table
    c.execute("CREATE TABLE numbers (num int)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", 
                    (random.randint(0,100),))