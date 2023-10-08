from django.urls import path, include
from spotifier.api import TopTracksOfArtist, DownloaderSong


urlpatterns = [
    path('artist/top-tracks/', TopTracksOfArtist.as_view(), name='top_tracks'),
    path('artist/downlaoder/', DownloaderSong.as_view(), name='downlaod_tracks'),
]
