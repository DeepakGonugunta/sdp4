# Generated by Django 4.0.4 on 2022-05-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_image',
        ),
    ]
