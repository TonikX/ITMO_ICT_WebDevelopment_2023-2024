# Generated by Django 3.2 on 2023-12-20 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_checkin_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='income',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='staying_days',
        ),
    ]
