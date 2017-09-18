import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT make, model, COUNT(order_date) FROM orders GROUP BY make, model")

	rows = c.fetchall()

	for r in rows:

		print ("Make: {}, Model: {}".format(r[0], r[1]))
		print("Total de Ordenes: " +str(r[2]))
		print("")