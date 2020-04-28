import psycopg2

cnx = psycopg2.connect(host="localhost", database="formation", user="postgres", password="aleria")
sql = "select * from client where id=1"
cursor = cnx.cursor()
cursor.execute(sql)
row = cursor.fetchone()

""" Lire toutes les lignes """
sql = "select * from client"
cursor = cnx.cursor()
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print("- {0}".format(row))

# raison = "AT&T"
# mnemo = "att"
# adresse = "387 square garden LONDON"
# codeinsee = 10215
# email = "bob@att.com"
#
# sql = f"insert into client (raison,mnemo,adresse1,codeinsee,email) values ('{raison}','{mnemo}','{adresse}','{codeinsee}','{email}')"
# cursor.execute(sql)
# cnx.commit()
#
# sql = "select * from client"
# cursor.execute(sql)
# rows = cursor.fetchall()
#
# for row in rows:
#     print("-> {0}".format(row))

""" Modifier un client """
sql = "delete from client where id=%s"
listValues = []
listValues.append(3)
cursor.execute(sql, listValues)
cnx.commit()
cursor.close()
