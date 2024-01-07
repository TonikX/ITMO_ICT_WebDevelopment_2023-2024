# Generated by Django 3.2 on 2023-12-07 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='SkillOfWarrior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень освоения умения')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors_app.skill', verbose_name='Умение')),
            ],
        ),
        migrations.CreateModel(
            name='Warrior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('s', 'student'), ('d', 'developer'), ('t', 'teamlead')], max_length=1, verbose_name='Расса')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('level', models.IntegerField(default=0, verbose_name='Уровень')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warriors_app.profession', verbose_name='Профессия')),
                ('skill', models.ManyToManyField(related_name='warrior_skils', through='warriors_app.SkillOfWarrior', to='warriors_app.Skill', verbose_name='Умения')),
            ],
        ),
        migrations.AddField(
            model_name='skillofwarrior',
            name='warrior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warriors_app.warrior', verbose_name='Воин'),
        ),
    ]
