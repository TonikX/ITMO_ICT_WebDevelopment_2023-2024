# Generated by Django 4.2.7 on 2023-11-26 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="mail",
        ),
    ]
