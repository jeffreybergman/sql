# UPDATE and DELETE statments

import sqlite3

# create the database connection
with sqlite3.connect("new.db") as connection:
    # create the cursor
    c = connection.cursor()

    # update data
    c.execute("""UPDATE population SET population = 9000000 WHERE 
        city = 'New York City'""")

    # delete data
    c.execute("DELETE FROM population WHERE city = 'Boston'")

    print "\nNEW DATA:\n"

    # query the table
    c.execute("SELECT * FROM population")

    # get the data rows
    rows = c.fetchall()

    # iterate the rows
    for r in rows:
        print r[0], r[1], r[2]