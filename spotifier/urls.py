from django.urls import path, include
from spotifier.api import(
    TopTracksOfArtist_first, TopTracksOfArtist_second,
    TopTracksOfArtist_third, TopTracksOfArtist_forth,
    DownloaderSong, ArtistCloner, MYLikeCloner, GetAllTracks)
from spotifier import views

urlpatterns = [
    path('artist/clone/', ArtistCloner.as_view(), name='artist_cloner'),
    path('artist/tone/', TopTracksOfArtist_first.as_view(), name='top_tracks'),
    path('artist/tsecond/', TopTracksOfArtist_second.as_view(), name='top_tracks'),
    path('artist/tthird/', TopTracksOfArtist_third.as_view(), name='top_tracks'),
    path('artist/tfour/', TopTracksOfArtist_forth.as_view(), name='top_tracks'),
    path('track/downlaoder/', DownloaderSong.as_view(), name='downlaod_tracks'),
    path('track/all/', GetAllTracks.as_view(), name='all_tracks'),
    path('artist/downlaoder/', DownloaderSong.as_view(), name='downlaod_tracks'),
    path('my/songs/', MYLikeCloner.as_view(), name='my_tracks'),
    path('auth/', views.auth, name='spotify_auth'),
    path('callback/', views.spotify_callback, name='spotify_callback'),
    path('like/json', views.like_spotifier_json, name='json_liker'),
]
