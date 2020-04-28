import socket

host_ip, server_port = "82.64.200.215", 2947
#host_ip, server_port = "localhost", 3000

# Initialise le client TCP avec SOCK_STREAM 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Etablit la connexion avec le serveur TCP
    tcp_client.connect((host_ip, server_port))

    # Lit les donnees du serveur et ferme la connexion.
    while True:
        received = tcp_client.recv(1024)
        #$GPRMC
        if received[:6] == b'$GPRMC':
            print ("{}".format(str(received)))
            strRMC=str(received)
            tab=strRMC.split(',')
            heure=tab[1]
            #print("heure={0}".format(tab[1]))
        if received[:7] == b'$BME280':
            print ("{}".format(str(received)))
finally:
    tcp_client.close()

#print ("Bytes Received: {}".format(received.decode()))