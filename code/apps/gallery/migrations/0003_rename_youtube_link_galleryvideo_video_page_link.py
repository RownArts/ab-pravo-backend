# Generated by Django 3.2.5 on 2021-07-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_galleryvideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryvideo',
            old_name='youtube_link',
            new_name='video_page_link',
        ),
    ]
