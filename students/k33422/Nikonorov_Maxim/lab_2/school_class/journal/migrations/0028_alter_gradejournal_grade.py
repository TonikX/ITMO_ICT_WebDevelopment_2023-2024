# Generated by Django 4.2.6 on 2023-10-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0027_alter_submittedhomework_submitted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradejournal',
            name='grade',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
