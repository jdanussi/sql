# executemany() method

# import sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [('Boston','MA',10000), ('Chicago', 'IL', 20000), ('Houston', 'TX', 30000), ('Phoenix', 'AZ', 40000)]

	# insert data into table
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
