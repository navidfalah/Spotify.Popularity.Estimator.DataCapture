from rest_framework import serializers
from .models import Artist, TrackClone

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'spotify_id', 'name')

class TrackSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = TrackClone
        fields = ('id', 'spotify_id', 'name', 'artists')
