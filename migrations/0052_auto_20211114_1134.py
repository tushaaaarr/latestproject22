# Generated by Django 3.1.7 on 2021-11-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0051_notificationreminder_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationreminder',
            name='store_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationreminder',
            name='store_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationreminder',
            name='user_first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationreminder',
            name='user_fourth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationreminder',
            name='user_second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notificationreminder',
            name='user_third',
            field=models.BooleanField(default=False),
        ),
    ]
