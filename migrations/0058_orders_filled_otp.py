# Generated by Django 3.1.7 on 2021-11-18 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0057_orders_customer_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='filled_otp',
            field=models.BooleanField(default=False),
        ),
    ]
