# Generated by Django 3.2.7 on 2023-10-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20231005_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='job',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
