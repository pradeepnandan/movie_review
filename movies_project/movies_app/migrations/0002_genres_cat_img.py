# Generated by Django 5.0.2 on 2024-03-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='cat_img',
            field=models.ImageField(blank=True, upload_to='cat_img'),
        ),
    ]
