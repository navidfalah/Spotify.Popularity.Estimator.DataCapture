from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import requests
from urllib.parse import urlencode
import json
import json
from .models import TrackClone, Artist
from constants import client_id, client_secret


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
    file_path = ""
    for x in range(0, 16):
        with open(file_path+f"spotify_tracks{x}.json", 'r') as json_file:
            data = json.load(json_file)
        for item in data['items']:
            try:
                track_info = item['track']
                artist = Artist.objects.filter(spotify_id=track_info['artists'][0]['id']).first()
                track_file_instance = None
                track_clone = TrackClone(
                    TrackFile=track_file_instance,
                    spotify_id=track_info['id'],
                    name=track_info['name'],
                    is_local=track_info['is_local'],
                    is_playable=True,  # Assuming all tracks are playable for this example
                    popularity=track_info['popularity'],
                    track_number=track_info['track_number'],
                    type=track_info['type'],
                    duration_ms=track_info['duration_ms'],
                    artist=artist,
                    artists_list=','.join([artist['name'] for artist in track_info['artists']]),
                    release_date=track_info['album']['release_date']
                )
                if artist=="":
                    pass
                else:
                    track_clone.save()
            except:
                pass
    return HttpResponse('successful!')
