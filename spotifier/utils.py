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
