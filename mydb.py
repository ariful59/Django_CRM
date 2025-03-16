import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rumidu@22"
)

curObject = database.cursor()

curObject.execute("CREATE DATABASE IF NOT EXISTS demoCode")

print("Hello!!!")
