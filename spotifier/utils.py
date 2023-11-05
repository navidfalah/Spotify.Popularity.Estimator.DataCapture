import requests
import base64
from spotifier.models import Artist, TrackClone


def get_access_token(client_id, client_secret):
    # Encode client credentials
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        "Authorization": f"Basic {credentials}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json().get('access_token')


from requests.auth import HTTPBasicAuth
import requests

def get_access_token_private(client_id, client_secret, code, redirect_uri):
    token_url = 'https://accounts.spotify.com/api/token'
    
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }
    
    response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data=payload)
    
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        # Handle error appropriately
        response.raise_for_status()
