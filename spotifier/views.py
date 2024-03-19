from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import requests
from urllib.parse import urlencode
import json
import json
from .models import TrackClone, Artist
from .constants import client_id, client_secret


def auth(request):
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': "http://127.0.0.1:8000/spotifier/callback/",
        'scope': 'user-library-read',
    }
    return redirect(f'https://accounts.spotify.com/authorize?{urlencode(params)}')

def spotify_callback(request):
    error = request.GET.get('error')
    code = request.GET.get('code')
    if error:
        return HttpResponse(f'Error received from Spotify: {error}', status=400)
    if code:
        access_token = get_access_token_private(client_id, client_secret, code, request.build_absolute_uri(reverse('spotify_callback')))
        headers = {
            "Authorization": f"Bearer {access_token}"
            }
        offset = 0
        for x in range(0, 16):
            response = requests.get(f"https://api.spotify.com/v1/me/tracks?limit=50&offset={offset}", headers=headers)
            offset += 50
            with open(f'spotify_tracks{x}.json', 'w') as file:
                json.dump(response.json(), file, indent=4)
        return HttpResponse('Authorization successful!')
    return HttpResponse('No code provided by Spotify.', status=400)

def get_access_token_private(client_id, client_secret, code, redirect_uri):
    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }
    response = requests.post(token_url, auth=(client_id, client_secret), data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        response.raise_for_status()


def like_spotifier_json(request):
    # You may need to adjust the file path depending on where your files are stored
    file_path = "/home/navid/Desktop/Spotify-Popularity-Estimator/"
    
   
    # Change the range according to your JSON files count and offsets.
    for offset in range(0, 1900, 50):
        try:
            file_name = f"spotify_tracks_offset_{offset}.json"
            with open(file_path + file_name, 'r') as json_file:
                data = json.load(json_file)

            # Check if the JSON data is a list or a dict with an 'items' key.
            tracks = data if isinstance(data, list) else data.get('items', [])
            
            for item in tracks:
                try:
                    track_info = item['track']
                    artist_spotify_id = track_info['artists'][0]['id'] if track_info['artists'] else None
                    artist = Artist.objects.filter(spotify_id=artist_spotify_id).first() if artist_spotify_id else None
                    if not artist:
                        continue

                    track_file_instance = None  # Define how to handle TrackFile instance
                    track_clone = TrackClone(
                        spotify_id=track_info['id'],
                        name=track_info['name'],
                        popularity=track_info['popularity'],
                        duration_ms=track_info['duration_ms'],
                        artist=artist,
                        artists_list=','.join([artist['name'] for artist in track_info['artists']]),
                        release_date=track_info['album']['release_date'],
                        downloaded=False
                    )
                    track_clone.save()
                except Exception as e:
                    print(e)
                    # Here you should log the exception or handle it accordingly
                    # Example: print(f"Error processing track: {e}")
                    pass
        except FileNotFoundError:
            # If a file doesn't exist, log the error or handle it
            # Example: print(f"File {file_name} not found.")
            pass

    return HttpResponse('successful!')