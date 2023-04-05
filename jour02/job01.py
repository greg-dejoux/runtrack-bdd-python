import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='laplateforme.io',
    database='LaPlateforme'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM etudiants")

for x in mycursor:
    print(x)


