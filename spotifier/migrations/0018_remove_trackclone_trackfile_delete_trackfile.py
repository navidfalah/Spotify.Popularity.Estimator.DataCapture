# Generated by Django 4.2.6 on 2024-02-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0017_remove_trackclone_artists_trackclone_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackclone',
            name='TrackFile',
        ),
        migrations.DeleteModel(
            name='TrackFile',
        ),
    ]
