from django.db import models


class Artist(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    genres = models.TextField(blank=True, null=True)  # You can store genres as a comma-separated string or use another model and ForeignKey for a more normalized approach

    def __str__(self):
        return self.name

class TrackFile(models.Model):
    File = models.FileField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    

class TrackClone(models.Model):
    TrackFile = models.ForeignKey(TrackFile, on_delete=models.CASCADE, blank=True, null=True)
    spotify_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Spotify's track ID
    name = models.CharField(max_length=255)
    is_local = models.BooleanField(default=True)
    is_playable = models.BooleanField(default=True)
    popularity = models.IntegerField(default=0)
    track_number = models.IntegerField()
    type = models.CharField(max_length=100)
    duration_ms = models.IntegerField(default=0)
    artists = models.ManyToManyField(Artist)
    release_date = models.CharField(max_length=30, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # You can add more fields if needed, e.g., album, artists, etc.

    def __str__(self):
        return self.name
    