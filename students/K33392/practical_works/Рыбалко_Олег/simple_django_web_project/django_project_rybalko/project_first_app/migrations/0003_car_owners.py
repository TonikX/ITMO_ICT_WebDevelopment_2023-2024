# Generated by Django 4.2.7 on 2023-11-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0002_alter_ownership_end_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="owners",
            field=models.ManyToManyField(through="project_first_app.Ownership", to="project_first_app.carowner"),
        ),
    ]
