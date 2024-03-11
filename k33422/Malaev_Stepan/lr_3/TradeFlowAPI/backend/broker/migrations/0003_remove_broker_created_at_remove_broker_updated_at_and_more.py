# Generated by Django 4.0.10 on 2024-02-03 09:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broker', '0002_initial'),
    ]
    
    operations = [
        migrations.RemoveField(
            model_name='broker',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='broker',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='firm',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='firm',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='broker',
            name='firm',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='brokers', to='broker.firm'
            ),
        ),
        migrations.AlterField(
            model_name='broker',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name='broker', to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
