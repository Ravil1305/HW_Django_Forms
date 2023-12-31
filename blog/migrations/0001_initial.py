# Generated by Django 4.2.3 on 2023-08-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='превью')),
                ('date_of_creation', models.DateField(verbose_name='дата создания')),
                ('sign_of_publication', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
