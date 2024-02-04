from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
import csv
from .models import TrackClone, Artist


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=TrackClones.csv'
    writer = csv.writer(response)

    # Define the headers for CSV (excluding spotify_id and some other fields)
    track_clone_fields = ['name', 'popularity', 'track_number', 'type', 'duration_ms', 'artists_list', 'release_date']
    artist_fields = ['artist_name', 'artist_popularity', 'artist_followers', 'artist_genres', 'artist_main_artist']
    writer.writerow(track_clone_fields + artist_fields)

    # Write data rows
    for obj in queryset:
        row = [getattr(obj, field) for field in track_clone_fields]

        # Append data from the related Artist object
        artist = obj.artist
        artist_data = [
            artist.name, 
            artist.popularity, 
            artist.followers, 
            artist.genres, 
            artist.main_artist
        ]
        row.extend(artist_data)

        writer.writerow(row)

    return response


export_to_csv.short_description = "Export Selected to CSV"

# class DownloadedFilter(admin.SimpleListFilter):
#     title = _('downloaded status')
#     parameter_name = 'downloaded'

#     def lookups(self, request, model_admin):
#         return (
#             ('True', _('Downloaded')),
#             ('False', _('Not downloaded')),
#         )

#     def queryset(self, request, queryset):
#         if self.value() == 'True':
#             return queryset.filter(downloaded=True)
#         elif self.value() == 'False':
#             return queryset.filter(downloaded=False)

@admin.register(TrackClone)
class TrackCloneAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist')
    # list_filter = (DownloadedFilter,)
    search_fields = ['name']
    actions = [export_to_csv]  # Adding the export to CSV action

# Register other models
admin.site.register(Artist)
