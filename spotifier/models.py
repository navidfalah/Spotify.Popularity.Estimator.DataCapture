from django.db import models



class Artist(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)  # Spotify's artist ID
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    genres = models.TextField(blank=True, null=True)  # You can store genres as a comma-separated string or use another model and ForeignKey for a more normalized approach
    image_url = models.URLField(blank=True, null=True)  # Assuming you want to store the main artist image

    def __str__(self):
        return self.name


class Track(models.Model):
    spotify_id = models.CharField(max_length=255, unique=True)  # Spotify's track ID
    name = models.CharField(max_length=255)
    preview_url = models.URLField(blank=True, null=True)  # Some tracks might not have a preview URL
    is_local = models.BooleanField(default=True)
    is_playable = models.BooleanField(default=True)
    popularity = models.IntegerField(default=0)
    track_number = models.IntegerField()
    type = models.CharField(max_length=100)
    duration_ms = models.IntegerField(default=0)
    artists = models.ManyToManyField(Artist)  
    # You can add more fields if needed, e.g., album, artists, etc.

    def __str__(self):
        return self.name

   #   "is_local":false,
    #   "is_playable":true,
    #   "name":"Columbia",
    #   "popularity":96,
    #   "track_number":1,
    #   "type":"track",