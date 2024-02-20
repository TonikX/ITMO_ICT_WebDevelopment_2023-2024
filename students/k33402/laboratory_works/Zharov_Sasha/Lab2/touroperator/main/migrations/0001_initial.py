# Generated by Django 4.2.6 on 2023-10-22 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Ожидает подтверждения', 'Ожидает подтверждения'), ('Подтвержден', 'Подтвержден')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('agency_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('reserved_tours', models.ManyToManyField(through='main.Reservation', to='main.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
    ]
