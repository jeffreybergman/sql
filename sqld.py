# import from csv

import csv
import sqlite3

# create the database connection
with sqlite3.connect("new.db") as connection:
    # create a cursor object
    c = connection.cursor()

    # open the employees.csv file and assign to variable
    employees = csv.reader(open("employees.csv", "rU"))

    # create a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert the data into the table
    c.executemany("INSERT INTO employees VALUES(?, ?)", employees)
    