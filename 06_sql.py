# select stament

import sqlite3

# create object database connection and a cursor to execute SQL commands
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# for loop to iterate through the table to print the records line by line
	for row in c.execute("SELECT firstname, lastname FROM employees"):
		print(row)
