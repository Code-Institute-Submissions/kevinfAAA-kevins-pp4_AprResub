# Generated by Django 4.0 on 2021-12-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_remove_reservations_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='title',
            field=models.CharField(default=1, max_length=200, unique=True),
        ),
    ]
