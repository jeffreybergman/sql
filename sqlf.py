# SELECT statement, remove unicode characters

import sqlite3

# create the database connection
with sqlite3.connect("new.db") as connection:
    # create the cursor
    c = connection.cursor()

    # execute the query
    c.execute("SELECT firstname, lastname FROM employees")

    # use fetchall() to retrieve the records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]