# Generated by Django 4.0.4 on 2022-06-18 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_event_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='events',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
