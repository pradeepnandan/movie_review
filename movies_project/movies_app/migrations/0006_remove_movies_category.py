# Generated by Django 5.0.2 on 2024-03-20 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0005_movies_banner_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='category',
        ),
    ]
