# Generated by Django 3.2 on 2021-04-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_siteconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='contacts_text',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
