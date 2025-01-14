# Generated by Django 5.1.2 on 2024-12-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip_app', '0005_rename_activities_usertrip_special_requests_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='booking',
        ),
        migrations.RenameField(
            model_name='usertrip',
            old_name='special_requests',
            new_name='activities',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='available_from',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='available_to',
        ),
        migrations.AddField(
            model_name='trip',
            name='available_dates',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trip_images/'),
        ),
        migrations.AddField(
            model_name='usertrip',
            name='accommodation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usertrip',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertrip',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='type',
            field=models.CharField(choices=[('adventure', 'Adventure'), ('leisure', 'Leisure')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Traveler',
        ),
    ]