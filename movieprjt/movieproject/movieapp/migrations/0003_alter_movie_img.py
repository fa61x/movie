# Generated by Django 4.2.4 on 2023-08-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
