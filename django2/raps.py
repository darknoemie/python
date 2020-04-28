import sys
import requests

base_url = "http://127.0.0.1:8000/rasp"


def affichage(client):

    list_key = list(client.keys())
    for eachkey in list_key:
        print(f"{eachkey}: {client[eachkey]}")
    print('-----')


if len(sys.argv) < 2:
    url = base_url
else:
    url = f"{base_url}/{sys.argv[1]}"

try:
    response = requests.get(url=url)
    response.raise_for_status()
    list_response = response.json()

except requests.exceptions.HTTPError as ex:
    sys.exit(f"bad request: {ex}")

except Exception as ex:
    sys.exit(f"ERROR: {ex}")

if type(list_response) is list:
    for each_client in list_response:
        affichage(each_client)
else:
    affichage(list_response)
