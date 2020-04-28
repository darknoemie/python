# Echo server
import socket
import sys

HOST = None  # vide = toutes les interfaces réseau.
PORT = 13000  # Un port non privilégié
s = None
for res in socket.getaddrinfo(
    HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE
):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.bind(sa)
        print("En attente de connexion sur le port " + repr(PORT))
        """ listen(1) : 1 = nombre de connexions non acceptées que le système autorisera 
            avant de refuser de nouvelles connexions
        """
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print("Impossible d'ouvrir le socket")
    sys.exit(1)
conn, addr = s.accept()
# print 'Connected by', addr
print("Connecté sur le socket {0}:{1} ".format(addr[0], addr[1]))
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()
