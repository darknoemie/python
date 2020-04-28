import socket
import time

host_ip, server_port = "localhost", 3000

# Initialise le client TCP avec SOCK_STREAM 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Etablit la connexion avec le serveur TCP
    tcp_client.connect((host_ip, server_port))

    # Lit les donnees du serveur et ferme la connexion.
    while True:
        try:
            received = tcp_client.recv(1024)
            if len(received) < 1:
                break
            print ("{}".format(str(received)))
            time.sleep(1)
        except socket.error as msg:
            print ("Fin du client ")
            break  
except socket.error as msg:  
    print ("Connexion impossible: le message est=<{0}>".format(msg))
finally:
    tcp_client.close()

#print ("Bytes Received: {}".format(received.decode()))