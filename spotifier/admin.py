from django.contrib import admin
from spotifier.models import Artist, TrackFile, TrackClone

admin.site.register(Artist)
admin.site.register(TrackFile)


from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import TrackClone, TrackFile, Artist

class DownloadedFilter(admin.SimpleListFilter):
    title = _('downloaded status')
    parameter_name = 'downloaded'

    def lookups(self, request, model_admin):
        return (
            ('True', _('Downloaded')),
            ('False', _('Not downloaded')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(downloaded=True)
        elif self.value() == 'False':
            return queryset.filter(downloaded=False)

@admin.register(TrackClone)
class TrackCloneAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'downloaded', 'created', 'modified')
    list_filter = (DownloadedFilter,)
    # Additional admin options here

# Optionally, if you want to register TrackFile and Artist, you would also do:
# admin.site.register(TrackFile)
# admin.site.register(Artist)
