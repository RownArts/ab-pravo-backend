# Generated by Django 3.2 on 2021-04-28 23:43

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_page_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageblock',
            name='published',
        ),
        migrations.AddField(
            model_name='pageblock',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title'),
        ),
    ]
