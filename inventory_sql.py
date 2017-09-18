import csv
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	inventory = csv.reader(open("inventory.csv", "rU"))

	c.executemany("INSERT INTO inventory(make, model, quantity) VALUES (?, ?, ?)", inventory)

