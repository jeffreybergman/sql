# import the sqlite3 library
import sqlite3

# create or connect to the database
conn = sqlite3.connect("cars.db")

# create a cursor
cursor = conn.cursor()

# create the inventory table
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT)
                """)

#close the connection
conn.close()