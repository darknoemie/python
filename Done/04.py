"""
Echo serveur
    Ce programme créer un socket..socket()
    affecte un nom au socket......bind()
    écoute sur le port ...........listen()
    accepte la connexion .........accept()
    reçoit un message ............recv()
    re envoie le message .........sendall()
    puis s'arrête.
"""
import socket

HOST = ""  # vide = toutes les interfaces réseau.
PORT = 13000  # Un port non privilégié
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("En attente de connexion sur le port " + repr(PORT))
s.listen(1)
conn, addr = s.accept()
print("Connecté sur le socket {0}:{1} ".format(addr[0], addr[1]))
while 1:
    data = conn.recv(1024)
    if not data:
        break
    data = b"pouet pouet"
    conn.sendall(data)
conn.close()
