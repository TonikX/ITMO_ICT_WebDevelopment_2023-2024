# Generated by Django 4.2.7 on 2023-12-01 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('sex', models.TextField(choices=[('m', 'm'), ('f', 'f')], max_length=2)),
                ('birthdate', models.DateField()),
                ('winter_sleeping', models.IntegerField(blank=True, null=True)),
                ('normal_temperature', models.FloatField(blank=True, null=True)),
                ('owner', models.CharField(max_length=2000)),
                ('previous_owner', models.CharField(max_length=2000)),
                ('in_lease', models.BooleanField()),
                ('where_is_now', models.CharField(max_length=2000)),
                ('since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='system.area')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('characteristic', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WinterPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('date_to', models.DateField()),
                ('date_from', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('birthday', models.DateField()),
                ('passport', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('animals', models.ManyToManyField(related_name='wathers', to='system.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('communal', models.BooleanField()),
                ('additional', models.CharField(blank=True, max_length=2000, null=True)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cages', to='system.building')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalInCage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='where', to='system.animal')),
                ('cage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who', to='system.cage')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='diet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals_on_this_diet', to='system.diet'),
        ),
        migrations.AddField(
            model_name='animal',
            name='winter_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birds_wintering', to='system.winterplace'),
        ),
    ]
