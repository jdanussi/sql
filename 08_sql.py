import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# update data
	c.execute("UPDATE population SET population = 300 WHERE city = 'Cordoba'")

	# delete data
	c.execute("DELETE FROM population WHERE city = 'Buenos Aires'")

	# print data
	print("\nNEW DATA:\n")

	c.execute("SELECT * FROM population")
	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])

