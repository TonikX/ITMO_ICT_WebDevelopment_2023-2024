# Generated by Django 4.2.6 on 2023-10-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0005_rename_subject_id_homework_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
