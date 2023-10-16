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

def get_and_save_artist(access_token, artist_id):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers)
    artist_data = response.json()

    # Save the artist's data to the database
    artist, created = Artist.objects.get_or_create(spotify_id=artist_data['id'])
    artist.name = artist_data['name']
    artist.popularity = artist_data['popularity']
    artist.followers = artist_data['followers']['total']
    artist.genres = ", ".join(artist_data['genres'])
    
    # Assuming you want the first image as the main image. You can adjust this if needed.
    if artist_data['images']:
        artist.image_url = artist_data['images'][0]['url']

    artist.save()

    return artist_data

def get_top_tracks_of_artist(access_token, artist_id, market="US"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}", headers=headers)
    tracks_data = response.json().get('tracks', [])
    saved_tracks = []
    print(tracks_data)
    print("**********")
    for track_data in tracks_data:
        track, track_created = TrackClone.objects.get_or_create(spotify_id=track_data['id'],
                                                           defaults={
                                                               'name': track_data['name'],
                                                                "is_playable":track_data['is_playable'],
                                                                "name":track_data['name'],
                                                                "popularity":track_data['popularity'],
                                                                "track_number":track_data['track_number'],
                                                                "type":track_data['type'],
                                                                "release_date" : track_data['album']['release_date'],
                                                                "duration_ms": track_data['duration_ms']
                                                           })
        for artist_data in track_data['artists']:
            artist, artist_created = Artist.objects.get_or_create(spotify_id=artist_data['id'],
                                                                  defaults={
                                                                      'name': artist_data['name'],
                                                                      'popularity': artist_data['popularity'],
                                                                      'followers': artist_data['followers'],
                                                                      'genres': artist_data['genres'],
                                                                  })
            track.artists.add(artist)
        saved_tracks.append(track)
    return saved_tracks
