import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""SELECT i.make, i.model, i.quantity, o.Total_Ordenes FROM inventory i INNER JOIN

	(SELECT make, model, COUNT(order_date) Total_Ordenes FROM orders GROUP BY make, model) o 
	ON i.make = o.make AND i.model = o.model""")

	rows = c.fetchall()

	for r in rows:

		print ("Make: {}, Model: {}".format(r[0], r[1]))
		print("Quantity: " + str(r[2]))
		print("Total de Ordenes: " + str(r[3]))
		print("")