# importar librerias
import sqlite3

# Establecer conexión con la base de datos newnum.db
connection = sqlite3.connect("newnum.db")

# Establecer cursor
c = connection.cursor()


# Solicitar leccion al usuario
prompt = """
Ingrese una Opción:
1. Avgerage
2. Min
3. Max
4: Sum
5. Exit
"""

# loop infinito hasta que el usuario seleccione opción válida
while True:
	x = input(prompt)

	if x in set(["1", "2", "3", "4"]):
		operation = {1:"avg", 2:"min", 3:"max", 4:"sum"}[int(x)]
		

		c.execute("SELECT {}(num) FROM  numbers".format(operation))

		# fechone() registro
		get = c.fetchone()

		# imprimimos el resultado
		print(operation + ":  %f" % get[0])

	# Si el usuario elige 5	
	elif x == "5":
		print("Exit")
		break

connection.close()



