from django.urls import path, include
from spotifier.api import TopTracksOfArtist


urlpatterns = [
    path('artist/<str:artist_id>/top-tracks/', TopTracksOfArtist.as_view(), name='top_tracks'),
]
