# Generated by Django 3.2 on 2021-05-08 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_siteconfig_contacts_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='button',
            options={'verbose_name': 'Кнопка', 'verbose_name_plural': 'Кнопки'},
        ),
        migrations.AlterModelOptions(
            name='pageblock',
            options={'ordering': ['my_order'], 'verbose_name': 'Блок страницы', 'verbose_name_plural': 'Блоки страниц'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['my_order'], 'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='siteconfig',
            options={'verbose_name': 'Дополнительные настройки', 'verbose_name_plural': 'Дополнительные настройки'},
        ),
    ]
