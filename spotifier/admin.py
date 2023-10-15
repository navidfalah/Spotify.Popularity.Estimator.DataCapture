from django.contrib import admin
from spotifier.models import Artist, TrackFile, TrackClone

admin.site.register(Artist)
admin.site.register(TrackClone)
admin.site.register(TrackFile)
