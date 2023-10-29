from django.db import models


class Artist(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    genres = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    preview_url = models.URLField(blank=True, null=True) 
    is_local = models.BooleanField(default=True)
    is_playable = models.BooleanField(default=True)
    popularity = models.IntegerField(default=0)
    track_number = models.IntegerField()
    type = models.CharField(max_length=100)
    duration_ms = models.IntegerField(default=0)
    artists = models.ManyToManyField(Artist)  

    def __str__(self):
        return self.name
