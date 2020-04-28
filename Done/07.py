# Echo client
import socket
import sys

HOST = "localhost"  # l'hote distant (ou pas ...)
PORT = 13000  # Le meme port que le serveur
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print("Impossible d'ouvrir le socket")
    sys.exit(1)
s.sendall(bytes("Hello, world", "UTF-8"))
data = s.recv(1024)
s.close()
print("Données reçues:{" + data.decode("utf-8") + "}")
