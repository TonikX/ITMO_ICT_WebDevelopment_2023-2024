# Generated by Django 4.2.6 on 2023-10-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=True),
        ),
    ]
