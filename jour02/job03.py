import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='laplateforme.io',
    database='LaPlateforme'
)

mycursor = mydb.cursor()

#mycursor.execute("insert into salles (nom, id_etage, capacite) values ('Studio Video', 2, 5)")
#mydb.commit()
mycursor.execute("select * from salles;")

for x in mycursor:
    print(x)


