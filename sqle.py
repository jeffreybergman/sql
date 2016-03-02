# SELECT statement

import sqlite3

# create the database connection
with sqlite3.connect("new.db") as connection:
    # create the cursor
    c = connection.cursor()

    # use a for loop to iterate the database and print results
    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print row