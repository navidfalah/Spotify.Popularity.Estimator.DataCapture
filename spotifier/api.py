import requests
import base64



import requests
import base64

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

def get_top_tracks_of_artist(access_token, artist_id, market="US"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}", headers=headers)
    return response.json().get('tracks')

client_id = "6cffce53882c4c3494bc6e258fc44cb0"
client_secret = "4fb8c7af4b23477c9afa930fbfaaa6d6"
artist_id = "1Xyo4u8uXC1ZmMpatF05PJ"

access_token = get_access_token(client_id, client_secret)
top_tracks = get_top_tracks_of_artist(access_token, artist_id)

for track in top_tracks:
    print(track)
