# Error Handler

# import sqlite3 library
import sqlite3

from sqlite3 import OperationalError

# create connection object to the database
conn = sqlite3.connect("new.db")

# create a cursor to the database to excute SQL commands
cursor = conn.cursor()

try:
	# insert data into table population
	cursor.execute("INSERT INTO populations VALUES ('Buenos Aires', 'BA', 155000)")
	cursor.execute("INSERT INTO populations VALUES ('Cordoba', 'CB', 130000)")

	# commit the changes
	conn.commit()

except sqlite3.OperationalError:
	#print("Ha ocurido un error SQL")
	raise
	

# close the database connection
conn.close()
