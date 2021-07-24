# Generated by Django 3.2.5 on 2021-07-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_rename_youtube_link_galleryvideo_video_page_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryalbum',
            options={'ordering': ['my_order'], 'verbose_name': 'Фото альбом', 'verbose_name_plural': 'Фото альбомы'},
        ),
        migrations.AddField(
            model_name='galleryalbum',
            name='my_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
