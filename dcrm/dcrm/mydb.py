# This code is just for creating a database. Once it is
# run then it is no longer needed and can be deleted. It 
# remains here for demonstration purposes. -Austin Ward

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'austin',
    passwd = 'Halo767900!!'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE austinDB")

print("All Done!")