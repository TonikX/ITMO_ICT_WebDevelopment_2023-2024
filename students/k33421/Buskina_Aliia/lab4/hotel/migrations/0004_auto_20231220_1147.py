# Generated by Django 3.2 on 2023-12-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_staff_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='check_in_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='check_out_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
