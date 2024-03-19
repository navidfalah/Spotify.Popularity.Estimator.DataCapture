from django.db import models


class Artist(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    genres = models.TextField(blank=True, null=True)  # You can store genres as a comma-separated string or use another model and ForeignKey for a more normalized approach
    main_artist = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    

class TrackClone(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Spotify's track ID
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    duration_ms = models.IntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artists_list = models.TextField()
    release_date = models.CharField(max_length=30, blank=True, null=True)
    acousticness = models.CharField(max_length=10, blank=True, null=True)
    danceability = models.CharField(max_length=10, blank=True, null=True)
    duration_ms = models.CharField(max_length=10, blank=True, null=True)
    energy = models.CharField(max_length=10, blank=True, null=True)
    instrumentalness = models.CharField(max_length=10, blank=True, null=True)
    key = models.CharField(max_length=10, blank=True, null=True)
    liveness = models.CharField(max_length=10, blank=True, null=True)
    loudness = models.CharField(max_length=10, blank=True, null=True)
    mode = models.CharField(max_length=10, blank=True, null=True)
    speechiness = models.CharField(max_length=10, blank=True, null=True)
    tempo = models.CharField(max_length=10, blank=True, null=True)
    time_signature = models.CharField(max_length=10, blank=True, null=True)
    valence = models.CharField(max_length=10, blank=True, null=True)
    downloaded = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name 
    