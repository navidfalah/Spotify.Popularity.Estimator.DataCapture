# Generated by Django 4.2.6 on 2023-10-15 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0006_track_is_local_track_is_playable_track_track_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='release_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CloneTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotifier.track')),
            ],
        ),
    ]