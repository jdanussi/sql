# Import from CSV

# import csv library
import csv

import sqlite3


with sqlite3.connect("rrhh.db") as connection:
	c = connection.cursor()

	# open the csv file and assign it to a variable
	empleados = csv.reader(open("rrhh.csv", "rU")) 

	# create a new table empleados
	c.execute("CREATE TABLE empleados(legajo INT, nombre TEXT, sede TEXT)")

	# insert data into table
	c.executemany("INSERT INTO empleados(legajo, nombre, sede) VALUES(?, ?, ?)", empleados)


