# Generated by Django 4.2.3 on 2023-08-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_productversion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productversion',
            name='sign_of_version',
        ),
        migrations.AddField(
            model_name='productversion',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
    ]
