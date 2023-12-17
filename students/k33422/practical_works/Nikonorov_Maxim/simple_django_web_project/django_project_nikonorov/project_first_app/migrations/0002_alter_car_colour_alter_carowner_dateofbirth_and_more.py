# Generated by Django 4.2.6 on 2023-10-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Colour',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='EndDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
