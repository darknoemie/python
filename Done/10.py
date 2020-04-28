import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    """
    Démonstration d'une classe Server TCP.

    Il faut implémenter la méthode handle() pour
    échanger des données avec le client.

    """

    def handle(self):
        # self.request -  socket TCP connecté au client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # Envoie un accusé de réception lors de  l'arrivée des données. 
        self.request.sendall("ACK from TCP Server".encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 3000

    # Initialise l'objet TCPServer et effectue la liaison avec le port 3000
    tcp_server = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print("Le serveur écoute sur le port {}".format(PORT))
    # Active le serveur TCP.
    # Pour interrompre le serveur appuyez sur Ctrl-C.
    tcp_server.serve_forever()
