# views.py
from rest_framework.generics import ListAPIView
from .models import Track
from .serializers import TrackSerializer
from spotifier.utils import get_top_tracks_of_artist, get_and_save_artist, get_access_token
from spotifier.constants import client_id, client_secret

class TopTracksOfArtist(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        artist_id = self.kwargs['artist_id']
        access_token = get_access_token(client_id=client_id, client_secret=client_secret)
        tracks = get_top_tracks_of_artist(access_token, artist_id)
        return tracks
