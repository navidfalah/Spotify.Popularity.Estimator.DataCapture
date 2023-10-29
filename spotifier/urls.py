from django.urls import path, include
from spotifier.api import(
    TopTracksOfArtist_first, TopTracksOfArtist_second,
    TopTracksOfArtist_third, TopTracksOfArtist_forth,
    DownloaderSong, ArtistCloner)

urlpatterns = [
    path('artist/clone/', ArtistCloner.as_view(), name='artist_cloner'),
    path('artist/tone/', TopTracksOfArtist_first.as_view(), name='top_tracks'),
    path('artist/tsecond/', TopTracksOfArtist_second.as_view(), name='top_tracks'),
    path('artist/tthird/', TopTracksOfArtist_third.as_view(), name='top_tracks'),
    path('artist/tfour/', TopTracksOfArtist_forth.as_view(), name='top_tracks'),
    path('artist/downlaoder/', DownloaderSong.as_view(), name='downlaod_tracks'),
]
