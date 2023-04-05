import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='laplateforme.io',
    database='LaPlateforme'
)

mycursor = mydb.cursor()

#mycursor.execute("insert into salles (nom, id_etage, capacite) values ('Studio Video', 2, 5)")
mydb.commit()
mycursor.execute("SELECT SUM(superficie) FROM etage")

for x in mycursor:
    print("La superficie de La Plateforme est de", x[0], "m2")


