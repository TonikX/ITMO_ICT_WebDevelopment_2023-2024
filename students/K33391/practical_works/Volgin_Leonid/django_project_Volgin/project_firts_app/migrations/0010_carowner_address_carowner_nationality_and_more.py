# Generated by Django 4.2.6 on 2023-11-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_firts_app', '0009_alter_carowner_options_alter_carowner_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='carowner',
            name='nationality',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='carowner',
            name='passport',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
