# Generated by Django 3.2.5 on 2021-07-25 12:55

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_comment_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageblock',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='no-image.png', upload_to='images/pageblock'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='no-image.png', null=True, upload_to='images/comments'),
        ),
    ]
