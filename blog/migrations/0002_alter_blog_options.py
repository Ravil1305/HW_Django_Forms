# Generated by Django 4.2.3 on 2023-08-05 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
    ]
