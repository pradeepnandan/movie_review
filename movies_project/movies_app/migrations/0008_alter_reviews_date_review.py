# Generated by Django 5.0.2 on 2024-03-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0007_alter_reviews_date_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date_review',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
