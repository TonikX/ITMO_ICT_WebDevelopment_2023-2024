# Generated by Django 3.2 on 2023-12-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_checkin_staying_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
