# Generated by Django 3.2.5 on 2021-07-25 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20210724_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryphoto',
            name='description',
        ),
    ]
