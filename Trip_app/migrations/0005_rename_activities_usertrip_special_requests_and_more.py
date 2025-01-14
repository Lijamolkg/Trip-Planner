# Generated by Django 5.1.2 on 2024-12-30 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trip_app', '0004_booking_traveler'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertrip',
            old_name='activities',
            new_name='special_requests',
        ),
        migrations.RemoveField(
            model_name='usertrip',
            name='accommodation',
        ),
        migrations.RemoveField(
            model_name='usertrip',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='usertrip',
            name='start_date',
        ),
    ]
