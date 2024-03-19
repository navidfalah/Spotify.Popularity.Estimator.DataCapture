import requests
import base64
from requests.auth import HTTPBasicAuth
import requests
import csv


def get_access_token(client_id, client_secret):
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        "Authorization": f"Basic {credentials}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json().get('access_token')


def remove_first_column(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as infile:
        with open(output_csv, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                del row[0]
                writer.writerow(row)
