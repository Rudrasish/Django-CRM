import mysql.connector

#create a db connection
dataBase=mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'password123',
)


#prepare a cursor object
cursorObject= dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done")