# Generated by Django 4.2.6 on 2023-10-28 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_firts_app', '0002_delete_testtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='cars',
            field=models.ManyToManyField(through='project_firts_app.Ownership', to='project_firts_app.car'),
        ),
    ]
