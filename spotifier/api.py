# views.py
from rest_framework.generics import ListAPIView
from .models import TrackClone
from .serializers import TrackSerializer
from spotifier.utils import get_access_token
from spotifier.constants import client_id, client_secret
from .crawler import song_downloader
from .singers_constants import artists as artists_data
import requests
from .models import Artist


def get_json_data():
    array_code_artists = []
    for artist in artists_data:
        array_code_artists.append(artist['id'])
    return array_code_artists

def song_cloner(access_token, artist_id, market="US"):

    headers = {
            "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}", headers=headers)
    tracks_data = response.json().get('tracks', [])
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
            response = requests.get(f"https://api.spotify.com/v1/artists/{artist_data['id']}", headers=headers)
            specific_artist = response.json()
            artist, artist_created = Artist.objects.get_or_create(spotify_id=artist_data['id'],
                                                                    defaults={
                                                                      'name': specific_artist['name'],
                                                                      'popularity': specific_artist['popularity'],
                                                                      'followers': specific_artist['followers']['total'],
                                                                      'genres': specific_artist['genres'],
                                                                  })
            track.artists.add(artist)
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
                                                                  })
                artist.save()
            except:
                pass
        return Artist    


class TopTracksOfArtist_first(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        artists_first = Artist.objects.filter()[0:25]
        for artist in artists_first:
            song_cloner(access_token, artist.spotify_id)




class TopTracksOfArtist_second(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[25:50]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks

class TopTracksOfArtist_third(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[50:75]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks

class TopTracksOfArtist_forth(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists[75:100]:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks
    
class DownloaderSong(ListAPIView):
    serializer_class = TrackSerializer
        
    def get_queryset(self):
        list_tracks = TrackClone.objects.all()
        for track in list_tracks:
            id = track.spotify_id
            song_downloader("https://open.spotify.com/track/"+str(id))
        







# def get_top_tracks_of_artist(access_token, artist_id, market="US"):
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
    
#         for artist_data in track_data['artists']:
#             print(artist_data)
#             response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers)
#             specific_artist = response.json()
#             artist, artist_created = Artist.objects.get_or_create(spotify_id=artist_data['id'],
#                                                                   defaults={
#                                                                       'name': artist_data['name'],
#                                                                       'popularity': specific_artist['popularity'],
#                                                                       'followers': specific_artist['followers']['total'],
#                                                                       'genres': specific_artist['genres'],
#                                                                   })
#             track.artists.add(artist)
#         saved_tracks.append(track)
#     return saved_tracks

