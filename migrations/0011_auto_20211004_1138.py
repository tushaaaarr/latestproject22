# Generated by Django 3.1.7 on 2021-10-04 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0010_auto_20211004_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_type',
            old_name='is_student',
            new_name='is_store',
        ),
        migrations.RenameField(
            model_name='user_type',
            old_name='is_teach',
            new_name='is_user',
        ),
    ]
