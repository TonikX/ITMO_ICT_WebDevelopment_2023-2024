# Generated by Django 4.2.6 on 2023-11-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_tour_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldtour',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
