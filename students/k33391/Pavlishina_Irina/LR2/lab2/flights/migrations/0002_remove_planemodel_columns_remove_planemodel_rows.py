# Generated by Django 4.2.7 on 2023-11-02 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planemodel',
            name='columns',
        ),
        migrations.RemoveField(
            model_name='planemodel',
            name='rows',
        ),
    ]
