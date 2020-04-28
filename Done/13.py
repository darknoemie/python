# Python TCP Client A
import socket

host = socket.gethostname()
port = 3004
BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while MESSAGE != 'exit':
    tcpClient.send(bytes(MESSAGE, 'UTF-8'))
    data = tcpClient.recv(BUFFER_SIZE)
    print(" Client a reçu:" + data.decode('utf-8'))
print(" Fin du programme client.")
tcpClient.close()
