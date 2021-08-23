# Generated by Django 3.2.5 on 2021-08-23 21:22

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='slogan',
            field=models.TextField(blank=True, default=None, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='no-image.png', null=True, upload_to='images/comments', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='role',
            field=models.CharField(max_length=200, verbose_name='Должность'),
        ),
    ]