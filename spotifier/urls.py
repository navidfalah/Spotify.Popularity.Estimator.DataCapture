from django.urls import path, include
from spotifier.api import TopTracksOfArtist


urlpatterns = [
    path('artist/top-tracks/', TopTracksOfArtist.as_view(), name='top_tracks'),
]
