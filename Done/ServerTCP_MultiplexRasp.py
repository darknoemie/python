# Python TCP Client A
import socket
import threading

global data_text
threads_list = []


class ThreadClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global data_gps
        host = "82.64.200.215"
        port = 2947
        BUFFER_SIZE = 20000
        tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClient.connect((host, port))
        print(f"Thread rasp is running")
        while True:
            data = tcpClient.recv(BUFFER_SIZE)
            data_text = str(data.decode('utf-8')).split(",")
            if data_text[0] == "$BME280":
                temperature = data_text[1]
                hydrometrie = data_text[2]
                pression = data_text[3]
                data_gps = f"Temperature = {temperature}, hydrometrie = {hydrometrie}, pression = {pression}"


class ThreadServer(threading.Thread):
    global data_gps

    def __init__(self, name: int, ip: str, port: str):
        threading.Thread.__init__(self)
        self.name = f"serveur-{name}"
        self.ip = ip
        self.port = port

    def run(self):

        print(f"Thread {self.name} is running")
        while True:
            message = f"{self.name}: {data_gps}"
            conn.send(bytes(message, "UTF-8"))  # echo


HOST_SERVER = socket.gethostname()
PORT_SERVER = 3004
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((HOST_SERVER, PORT_SERVER))
client_thread = ThreadClient()
client_thread.start()

nb_thread = 0

while True:
    tcpServer.listen(4)
    (conn, (ip, port)) = tcpServer.accept()
    data = conn.recv(2048)
    server_thread = ThreadServer(nb_thread, ip, port)
    server_thread.start()
    nb_thread += 1
