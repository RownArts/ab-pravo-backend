# Generated by Django 3.2 on 2021-04-28 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210428_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
    ]
