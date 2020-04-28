import socket
import psycopg2
import time

from datetime import datetime

# Network config
host = "82.64.200.215"
port = 2947
BUFFER_SIZE = 2000
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))


# BDD Config
now = datetime.now().strftime('%Y-%m-%d')
cnx = psycopg2.connect(host="localhost", database="formation", user="postgres", password="aleria")
cursor = cnx.cursor()

global timestamp

timestamp = str(datetime.now().strftime('%H%M%S'))
count_error = 0
count = 0

while True:
    data = tcpClient.recv(BUFFER_SIZE)
    # print(data.decode('utf-8'))
    data_text = str(data.decode('utf-8')).split(",")

    if data_text[0] == "$GPRMC":
        stamp = str(data_text[1]).split(".")
        timestamp = str(int(stamp[0]) + 20000)

    if data_text[0] == "$BME280":
        temperature = data_text[1]
        hygrometrie = data_text[2]
        value_presure = str(data_text[3]).split('*')
        pression = value_presure[0]

        print(f"{timestamp} - Temperature = {temperature}, hygrometrie = {hygrometrie}, pression = {pression}")
        sql = f"insert into rasp (date,timestamp,type,temperature,hygrometrie, pression) " \
              f"values ('{now}','{timestamp}','BME280','{temperature}','{hygrometrie}', '{pression}')"
        count += 1
        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
        except Exception as ex:
            count_error += 1
            print(f"{count_error} mesures ont été perdus sur {count}")
            cursor.close()
        finally:
            cnx.commit()
            cursor.close()
tcpClient.close()
cursor.close()