# Generated by Django 4.2.7 on 2023-11-04 13:47

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0005_remove_carowner_name_remove_carowner_surname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carowner",
            name="date_of_birth",
            field=models.DateField(default=datetime.date(1970, 1, 1)),
        ),
        migrations.AlterField(
            model_name="carowner",
            name="home_address",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="carowner",
            name="nationality",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AlterField(
            model_name="carowner",
            name="passport_number",
            field=models.CharField(default="", max_length=30),
        ),
    ]
