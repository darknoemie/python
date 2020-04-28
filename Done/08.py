import socket

localIP = "127.0.0.1"
localPort = 13000
bufferSize = 1024

msgFromServer = "Hello cher client UDP"
bytesToSend = str.encode(msgFromServer)

# Création d'un socket datagramme
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Affectation d'un nom au socket (affectation d'une adresse)
UDPServerSocket.bind((localIP, localPort))
msg = "Le serveur UDP écoute sur le port {}".format(localPort)
print(msg)
# Le socket est en attente de messages entrant.
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message reçu depuis le client:{}".format(message)
    clientIP = "Addresse IP du client:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Envoie de la réponse au client.
    UDPServerSocket.sendto(bytesToSend, address)
