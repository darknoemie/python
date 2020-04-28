import socket
import time
import datetime
import xml.etree.ElementTree as ET


host_ip, server_port = "localhost", 3000
date = datetime.datetime.now()
dateDuJour = str(date).split('.')[0]
filename='bme280-'+dateDuJour+'.xml'

# Initialise le client TCP avec SOCK_STREAM 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Etablit la connexion avec le serveur TCP
    tcp_client.connect((host_ip, server_port))

    racine = ET.Element("bme280",date=dateDuJour)


    # Lit les donnees du serveur et ferme la connexion.
    while True:
        try:
            received = tcp_client.recv(1024)
            if len(received) < 1:
                break
            print ("{}".format(str(received)))
            tab=str(received).split(',')
            mesure = ET.SubElement(racine, "mesure", heure=tab[0])
            temp=ET.SubElement(mesure, "temp")
            temp.text = tab[1]
            hygro=ET.SubElement(mesure, "hygro")
            hygro.text = tab[2]
            pression=ET.SubElement(mesure, "pression")
            pression.text = tab[3]
            #print ("temp={}".format(tab[1]))
            time.sleep(1)
        except socket.error as msg:
            tree = ET.ElementTree(racine)
            tree.write(filename)
            print ("Fin du client ")
            break  
except socket.error as msg:  
    print ("Connexion impossible: le message est=<{0}>".format(msg))
finally:
    tree = ET.ElementTree(racine)
    tree.write(filename)
    tcp_client.close()

