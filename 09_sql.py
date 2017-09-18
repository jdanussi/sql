import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT i.make, i.model, i.quantity, o.order_date FROM inventory i, orders o WHERE i.make = o.make AND i.model = o.model")

	rows = c.fetchall()

	for r in rows:
		print ("Make: {}, Model: {}".format(r[0], r[1]))
		print("Quantity: " +str(r[2]))
		print("Order_Date: " + r[3])
		print("")