# select stament

import sqlite3

# create object database connection and a cursor to execute SQL commands
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	strSQL = "SELECT firstname, lastname FROM employees"
	c.execute(strSQL)

	# fetchall() retrieves all the records from the query
	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1])
