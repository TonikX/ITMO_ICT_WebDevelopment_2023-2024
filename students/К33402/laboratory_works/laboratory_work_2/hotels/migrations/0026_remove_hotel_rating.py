# Generated by Django 4.2.7 on 2023-11-06 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0025_remove_review_bookingid_remove_review_room_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rating',
        ),
    ]
