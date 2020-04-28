import socket

host_ip, server_port = "127.0.0.1", 3004
data = " Hello wild world... best regards ..!\n"

# Initialise le client TCP avec SOCK_STREAM 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Etablit la connexion avec le serveur TCP
    tcp_client.connect((host_ip, server_port))
    # Envoie des données au serveur
    tcp_client.sendall(data.encode())

    # Lit les données du serveur et ferme la connexion.
    received = tcp_client.recv(1024)
finally:
    tcp_client.close()

print("Bytes Sent:     {}".format(data))
print("Bytes Received: {}".format(received.decode()))
