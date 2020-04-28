# Python TCP Client A
import socket

host = "82.64.200.215"
port = 2947
BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while True:
    data = tcpClient.recv(BUFFER_SIZE)
    #print(data.decode('utf-8'))
    data_text = str(data.decode('utf-8')).split(",")
    if data_text[0] == "$BME280":
        temperature = data_text[1]
        hydrometrie = data_text[2]
        pression = data_text[3]
        print(f"Temperature = {temperature}, hydrometrie = {hydrometrie}, pression = {pression}")

tcpClient.close()

