import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='laplateforme.io',
    database='Jour2Job7'
)

mycursor = mydb.cursor()

#mycursor.execute("insert into salles (nom, id_etage, capacite) values ('Studio Video', 2, 5)")

mycursor.execute("SHOW TABLES")
mydb.commit()
for x in mycursor:
    print(x)


