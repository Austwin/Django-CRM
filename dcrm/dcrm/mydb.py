import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'austin',
    passwd = 'Halo767900!!'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE austinDB")

print("All Done!")