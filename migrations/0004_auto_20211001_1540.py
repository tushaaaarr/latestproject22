# Generated by Django 3.1.7 on 2021-10-01 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_cities_image_personaldetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='lan',
            new_name='lon',
        ),
    ]