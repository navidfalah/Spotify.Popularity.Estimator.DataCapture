from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import TrackClone
from .serializers import TrackSerializer
from django.http import JsonResponse
from spotifier.utils import get_access_token
from spotifier.constants import client_id, client_secret, code
from .singers_constants import artists as artists_data
import requests
from .models import Artist
import json
from .models import TrackClone
from rest_framework.response import Response
from urllib.parse import urlparse
import os
import re


def get_json_data():
    array_code_artists = []
    for artist in artists_data:
        array_code_artists.append(artist['id'])
    return array_code_artists

def song_cloner(access_token, artist_id, artist_pk, market="US"):

    headers = {
            "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}", headers=headers)
    tracks_data = response.json().get('tracks', [])
    halfway_point = len(tracks_data) // 2
    # getting 5 track
    for track_data in tracks_data[:halfway_point]:
       
        track, track_created = TrackClone.objects.get_or_create(spotify_id='https://open.spotify.com/track/'+track_data['id'],
            defaults={
            'artist': Artist.objects.get(pk=artist_pk),
            'name': track_data['name'],
            "is_playable":track_data['is_playable'],
            "name":track_data['name'],
            "popularity":track_data['popularity'],
            "track_number":track_data['track_number'],
            "type":track_data['type'],
            "release_date" : track_data['album']['release_date'],
            "duration_ms": track_data['duration_ms']
            })
        artist_names = [artist['name'] for artist in track_data['artists']]
        artist_names_csv = ', '.join(artist_names)
        track.artists_list = artist_names_csv
        track.save()
      

class ArtistCloner(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists:
            headers = {
            "Authorization": f"Bearer {access_token}"
            }
            response = requests.get(f"https://api.spotify.com/v1/artists/{artist}", headers=headers)
            specific_artist = response.json()
            try:
                artist, artist_created = Artist.objects.get_or_create(spotify_id=artist,
                    defaults={
                        'name': specific_artist['name'],
                        'popularity': specific_artist['popularity'],
                        'followers': specific_artist['followers']['total'],
                        'genres': specific_artist['genres'],
                        'main_artist': True
                    })
                artist.save()
            except:
                pass
        return Artist    


class TracksFeatures(ListAPIView):
    serializer_class = TrackSerializer

    def get(self, request, *args, **kwargs):
        all_tracks = TrackClone.objects.all()
        for track in all_tracks:
            if not track.feature_cloned:
                track_ids = urlparse(track.spotify_id).path.split('/')[-1]
                access_token = get_access_token(client_id=client_id, client_secret=client_secret)
                headers = {"Authorization": f"Bearer {access_token}"}
                response = requests.get(f"https://api.spotify.com/v1/audio-features?ids={track_ids}", headers=headers)
                audio_features = response.json()['audio_features'][0]
                track.danceability = audio_features['danceability']
                track.energy = audio_features['energy']
                track.key = audio_features['key']
                track.loudness = audio_features['loudness']
                track.mode = audio_features['mode']
                track.speechiness = audio_features['speechiness']
                track.acousticness = audio_features['acousticness']
                track.instrumentalness = audio_features['instrumentalness']
                track.liveness = audio_features['liveness']
                track.valence = audio_features['valence']
                track.tempo = audio_features['tempo']
                track.track_id = audio_features['id']
                track.duration_ms = audio_features['duration_ms']
                track.time_signature = audio_features['time_signature']
                track.feature_cloned = True
                track.save()
                print("saved")
                print(track.pk)

       
        return Response({"haha"})


class TopTracksOfArtist_first(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        artists_first = Artist.objects.filter(main_artist=True)[0:25]
        for artist in artists_first:
            song_cloner(access_token, artist.spotify_id, artist.pk)

class TopTracksOfArtist_second(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        artists_first = Artist.objects.filter(main_artist=True)[25:50]
        for artist in artists_first:
            song_cloner(access_token, artist.spotify_id, artist.pk)

class TopTracksOfArtist_third(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        artists_first = Artist.objects.filter(main_artist=True)[50:75]
        for artist in artists_first:
            song_cloner(access_token, artist.spotify_id, artist.pk)

class TopTracksOfArtist_forth(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        artists_first = Artist.objects.filter(main_artist=True)[75:100]
        for artist in artists_first:
            song_cloner(access_token, artist.spotify_id, artist.pk)


class GetAllTracks(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        all_cloned_tracks = TrackClone.objects.all()
        return all_cloned_tracks


class DownloaderSong(ListAPIView):
    serializer_class = TrackSerializer
        
    def get_queryset(self):
        list_tracks = TrackClone.objects.all()
        for track in list_tracks:
            id = track.spotify_id
        


class MYLikeCloner(ListAPIView):
    serializer_class = TrackSerializer

    def get_existing_offsets(self):
        """
        Scan the existing JSON files to determine the last fetched offset.
        This helps in resuming the process from where it was interrupted.
        """
        existing_files = os.listdir('.')
        offsets = [int(re.search(r'offset_(\d+).json', file).group(1)) 
                   for file in existing_files if re.match(r'spotify_tracks_offset_\d+.json', file)]
        return sorted(offsets)

    def get_queryset(self):
        access_token = "BQD4uV3EQC9moqBF963IRY8_cQ0GJlopXaclUbvDDV_cyE-u7_9k3VYXgc4GOzn6g5pqq2hM9pr0EWLiMVAxQzdxdgnDWYLg7v-lDnJbfE0te6IVoINxZSzIjz_BRfmrZjBkcFzYril4o0a0kABXy6T6ub8YiZhBfRd6bv936r35nZP6Em_LkVQc13c26Eo8yzodmNCBfSaGaGLyaY3x&token_type=Bearer&expires_in=3600&state=yVdO8AQkI4SW52KChXqEIg"  # Replace with your actual access token
        headers = {"Authorization": f"Bearer {access_token}"}
        limit = 50
        total_tracks = 1900  # Update this if the number of tracks changes
        existing_offsets = self.get_existing_offsets()

        for expected_offset in range(0, total_tracks, limit):
            if expected_offset not in existing_offsets:
                response = requests.get(f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={expected_offset}", headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    items = data['items']
                    if items:
                        filename = f'spotify_tracks_offset_{expected_offset}.json'
                        with open(filename, 'w') as file:
                            json.dump(items, file, indent=4)
                        print(f"Saved {len(items)} tracks to {filename}")
                    else:
                        # If no items are returned for a non-final request, it may indicate an issue or that we have fetched all tracks
                        print(f"No items returned for offset {expected_offset}. May have reached the end of the track list.")
                        break
                else:
                    print(f"Failed to fetch tracks, status code: {response.status_code} at offset {expected_offset}")
                    # You may want to break or implement a retry mechanism here
                    