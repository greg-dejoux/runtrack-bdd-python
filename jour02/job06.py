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
mycursor.execute("SELECT SUM(capacite) FROM salles")

for x in mycursor:
    print("La capacité de toutes les salles est de :", x[0])


