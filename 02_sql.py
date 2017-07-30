# import sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object to the new.db database, used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES ('New York City', 'NY', 84000)")
cursor.execute("INSERT INTO population VALUES ('San Francisco', \
				'CA', 24000)")

# commit the changes
conn.commit()

# close the database connecion
conn.close()
