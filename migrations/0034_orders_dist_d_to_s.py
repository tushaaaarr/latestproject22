# Generated by Django 3.1.7 on 2021-11-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0033_auto_20211105_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='dist_d_to_s',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
