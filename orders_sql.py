# import from CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    orders = csv.reader(open("orders.csv", "rU"))

    # create a new table called employees
    c.execute("CREATE TABLE orders(make DATE, model TEXT, order_date DATE)")

    # insert data into table
    c.executemany("INSERT INTO orders(make, model, order_date) values (?, ?, ?)", orders)
