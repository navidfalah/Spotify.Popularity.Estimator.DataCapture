from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return self.title
