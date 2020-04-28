import socket
from threading import Thread

''' Serveur Python multithread:
    Créer un pool de thread pour gérer des socket serveur.
'''


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("\n[+] Nouveau client " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            print("Serveur à reçu :{" + data.decode('utf-8') + "}")
            MESSAGE = input("Serveur : Entrez une reponse depuis le serveur (exit=fin) :")
            if MESSAGE == 'exit':
                print("\nFin du thread " + ip + ":" + str(port))
                break
            print("Le serveur envoie {0} au client {1}:{2}".format(MESSAGE, self.ip, self.port))
            conn.send(bytes(MESSAGE, 'UTF-8'))  # echo


HOST = '0.0.0.0'
PORT = 3004
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((HOST, PORT))
threads = []

while True:
    tcpServer.listen(4)
    print("Serveur multithread : En attente de connexion...")
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)
    tcpServer.close()

