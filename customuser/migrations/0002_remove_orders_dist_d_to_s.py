# Generated by Django 3.2.6 on 2022-01-25 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='dist_d_to_s',
        ),
    ]
