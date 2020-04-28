import socket 
import time
from threading import Thread 
import threading

''' Serveur Python multithread:
    Créer un pool de thread pour gérer des socket serveur.
'''
trame = "xx"

class ClientThread(Thread): 
    global trame
    def __init__(self,ip,port,conn): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        print ("\n[+] Nouveau client " + ip + ":" + str(port) )
 
    def run(self): 
        while True : 
            print ("Le serveur envoie {0} au client {1}:{2}".format(trame,self.ip,self.port))
            try:
                trameLock.acquire()
                self.conn.send(bytes(trame,'UTF-8'))
            except socket.error as msg:
                self.conn.close()
                self.conn = None 
                print ("Fin du client {0}:{1}".format(self.ip,self.port))
                break   
            finally:  
                trameLock.release()
            time.sleep(1)


class ReaderThread(Thread): 
    
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
 
    def run(self): 
        global trame
        heure = "000000.00"
        
        host_ip, server_port = self.ip, self.port
        # Initialise le client TCP avec SOCK_STREAM 
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Etablit la connexion avec le serveur TCP
            tcp_client.connect((host_ip, server_port))

            # Lit les donnees du serveur et ferme la connexion.
            while True:
                received = tcp_client.recv(1024)
                if received[:6] == b'$GPRMC':
                    #print ("{}".format(str(received)))
                    strRMC=str(received)
                    tab=strRMC.split(',')
                    heure=tab[1]
                    #print("heure={0}".format(tab[1]))
                if received[:7] == b'$BME280':
                    #print ("{}".format(str(received)))
                    strBME=str(received)
                    tab=strBME.split(',')
                    temperature=tab[1]
                    hygrometrie=tab[2]
                    tab2=tab[3].split('*')
                    pression=tab2[0]
                    t={'heure': heure,'temperature': temperature,'hygrometrie': hygrometrie,'pression': pression}
                    trameLock.acquire()
                    trame=t['heure']+','+t['temperature']+','+t['hygrometrie']+','+t['pression']
                    trameLock.release()
                    print("trame={0}".format(trame))
                    
        finally:
            tcp_client.close()


HOST = '0.0.0.0' 
PORT = 3000 
BUFFER_SIZE = 20  

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((HOST, PORT)) 

threads = [] 

''' Lance le module de lecture'''
lecteur=ReaderThread("82.64.200.215", 2947)
lecteur.start()

trameLock = threading.Lock()

while True: 
    tcpServer.listen(4) 
    print ("Serveur NMEA : En attente de connexion..." )
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port,conn) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join()
    
    