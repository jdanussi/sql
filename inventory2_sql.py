# Este fue un intento fallido de dejar un unico encabezado con 
# Make, Model
# Quqntity
# y luego debajo, cada una de las order_date 
# NO SALIO"!!! 

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT make, model, quantity FROM inventory")
	rows_cab = c.fetchall()

	for r_cab in rows_cab:
		print ("Make: {}, Model: {}".format(r_cab[0], r_cab[1]))
		print("Quantity: " +str(r_cab[2]))

		c.execute("SELECT order_date FROM orders WHERE make = " + r_cab[0])
		#c.execute("SELECT make, model, order_date FROM orders WHERE make = " + r_cab[0] + " AND model =" + r_cab[1])
		rows_det = c.fetchall()

		for r_det in rows_det:
			print("Order_Date: " + r_det[0])
		
		print("")