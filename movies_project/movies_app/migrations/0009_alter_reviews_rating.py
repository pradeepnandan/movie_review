# Generated by Django 5.0.2 on 2024-03-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0008_alter_reviews_date_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(max_length=5),
        ),
    ]
