import socket
import xml.etree.ElementTree as ET
from datetime import datetime

# Network config
host = "82.64.200.215"
port = 2947
BUFFER_SIZE = 2000
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

#XML Config
now = datetime.now().strftime('%Y-%m-%d')
racine = ET.Element("releves")
name = ET.SubElement(racine, "Type", nom=f"BME280-{now}")

global timestamp

timestamp = str(datetime.now().strftime('%H%M%S'))

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

        value = ET.SubElement(name, "Releve", timestamp=timestamp)
        ET.SubElement(value, "temperature").text = temperature
        ET.SubElement(value, "hygrometrie").text = hygrometrie
        ET.SubElement(value, "pression").text = pression
        print(f"{timestamp} - Temperature = {temperature}, hygrometrie = {hygrometrie}, pression = {pression}")
        tree = ET.ElementTree(racine)
        tree.write("releves.xml")

tcpClient.close()
