import psycopg2


# BDD
cnx = psycopg2.connect(host="localhost", database="formation", user="postgres", password="aleria")

def readall():
    """ Lire toutes les lignes """
    sql = "select * from rasp"
    cursor = cnx.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

