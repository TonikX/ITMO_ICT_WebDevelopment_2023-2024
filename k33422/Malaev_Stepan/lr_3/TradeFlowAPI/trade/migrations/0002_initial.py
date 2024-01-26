# Generated by Django 5.0.1 on 2024-01-26 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    
    dependencies = [
        ('trade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    
    operations = [
        migrations.AddField(
            model_name='broker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='broker',
            name='firm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.firm'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.manufacturer'),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.product'),
        ),
        migrations.AddField(
            model_name='trade',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.broker'),
        ),
        migrations.AddField(
            model_name='trade',
            name='product_batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.productbatch'),
        ),
    ]
