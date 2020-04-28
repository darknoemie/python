import socket
import time
import datetime
import postgres.Bme280DAO as Bme280DAO
import psycopg2

host_ip, server_port = "localhost", 3000
date = datetime.datetime.now()
t=str(date).split('.')
dateDuJour = t[0]

print("date du jour = {0}".format(dateDuJour))

# Initialise le client TCP avec SOCK_STREAM 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Etablit la connexion avec le serveur TCP
    tcp_client.connect((host_ip, server_port))

    dao=Bme280DAO.Bme280DAO()


    # Lit les donnees du serveur et ferme la connexion.
    while True:
        try:
            received = tcp_client.recv(1024)
            if len(received) < 1:
                break
            print ("{}".format(str(received)))
            tab=str(received).split(',')
            h=tab[0]
            print("h={0}".format(h))
            temp= tab[1]
            hygro = tab[2]
            pression = tab[3]            
            entity={}
#            entity['timestampmesure']=dateDuJour+" {0}:{1}:{2}".format(h[0:1],h[2:3],h[4:5])
            s=dateDuJour+" "+h[0:1]+":"+h[2:3]+":"+h[4:5]
            print ("s={0}".format(s[0:19]))
            entity['timestampmesure']=s[0:19]
            entity['temperature']=temp
            entity['humidity']=hygro
            entity['pression']=pression
            lastid=dao.save(entity)
            time.sleep(1)
        except psycopg2.IntegrityError as msg:
            print ("Cle en double ")
            
        except psycopg2.InternalError as msg: 
            print ("Internal error ")   
            
        except socket.error as msg:
            print ("Fin du client ")
            break  
except socket.error as msg:  
    print ("Connexion impossible: le message est=<{0}>".format(msg))
finally:

    tcp_client.close()

