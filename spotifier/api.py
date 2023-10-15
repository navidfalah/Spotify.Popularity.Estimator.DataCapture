# views.py
from rest_framework.generics import ListAPIView
from .models import Track
from .serializers import TrackSerializer
from spotifier.utils import get_top_tracks_of_artist, get_and_save_artist, get_access_token
from spotifier.constants import client_id, client_secret
from .crawler import song_downloader
from .singers_constants import artists


def get_json_data():
    artists_data = artists
    array_code_artists = []
    for artist in artists_data:
        array_code_artists.append(artist['id'])
    return array_code_artists


class TopTracksOfArtist(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        array_artists = get_json_data()
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        for artist in array_artists:
            tracks = get_top_tracks_of_artist(access_token, artist)
        return tracks


class DownloaderSong(ListAPIView):
    serializer_class = TrackSerializer
        
    def get_queryset(self):
        list_tracks = Track.objects.all()
        for track in list_tracks:
            song_downloader("https://open.spotify.com/track/"+str(Track.spotify_id))
        