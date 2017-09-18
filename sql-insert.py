# importar librerías
import sqlite3
import random

# Establecer cońección y cursor a nueva base de datos newnum.db y database:
with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	# crear tabla numbers
	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers(num INT)")

	# Insertar 100 números al azar en la tabla numbers
	for i in range(100):
		c.execute("INSERT INTO numbers(num) VALUES(?)", (random.randint(0,100),))
		print("Registro {}:{}".format(i,(random.randint(0,100))))
