# import sqlite3 library
import sqlite3

# create the database "cars.db"
conn = sqlite3.connect("cars.db")

# get the cursor to the database
cursor = conn.cursor()

# create the table "inventory"
cursor.execute("""CREATE TABLE inventory (make DATE, model TEXT, quantity INT)""")

# close the connection
conn.close()

