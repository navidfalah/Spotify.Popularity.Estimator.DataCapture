# Generated by Django 4.2.6 on 2024-02-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0023_remove_trackclone_music_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackclone',
            name='track_number',
        ),
    ]
