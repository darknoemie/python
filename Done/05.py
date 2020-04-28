"""
Echo client
    Ce programme créer un socket..socket()
    ouvre une connexion ..........connect()
    envoie des données ...........sendall()
    relit les données envoyées ...recv()
    affiche les données ..........print()
    et s'arrête.
"""
import socket

HOST = "localhost"  # l'hote distant (ou pas ...)
PORT = 13000  # Le meme port que le serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(bytes("Hello, world", "UTF-8"))

""" Les données reçues sont au format byte
    il faut les transormer en string avec la fonction decode.
"""
data = s.recv(1024)
s.close()
print("Données reçues:{" + data.decode("utf-8") + "}")
