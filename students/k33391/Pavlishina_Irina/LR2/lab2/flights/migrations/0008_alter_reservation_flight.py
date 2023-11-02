# Generated by Django 4.2.7 on 2023-11-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_alter_flight_plane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_reservations', to='flights.flight'),
        ),
    ]
