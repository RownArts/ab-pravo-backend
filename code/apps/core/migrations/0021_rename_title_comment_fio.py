# Generated by Django 3.2.5 on 2021-07-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_pageblock_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='fio',
        ),
    ]
