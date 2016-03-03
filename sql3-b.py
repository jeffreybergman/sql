# Assignment 3b - prompt the user

import sqlite3

# create the database connection
conn = sqlite3.connect("newnum.db")

#create the cursor
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until user enters a valid operation
while True:
    # get the user input
    x = raw_input(prompt)

    # if user enters 1-4
    if x in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {1: "AVG", 2:"MAX", 3:"MIN", 4:"SUM"}[int(x)]
        # retrieve the data
        cursor.execute("SELECT {}(num) FROM numbers".format(operation))
        # fetchone() retrieves one record from query
        get = cursor.fetchone()
        # output result to screen
        print operation + ": {}".format(get[0])
    elif x == "5":
        print "Exit"
        # break loop
        break



