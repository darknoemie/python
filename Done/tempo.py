# Python TCP Client A
import socket
import time

host = socket.gethostname()
port = 3004
BUFFER_SIZE = 20000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while True:
    tcpClient.send(bytes("MESSAGE", 'UTF-8'))
    time.sleep(3)
    data = tcpClient.recv(BUFFER_SIZE)
    print(data.decode('utf-8'))
