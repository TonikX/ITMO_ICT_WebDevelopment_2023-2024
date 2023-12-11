# Generated by Django 4.2.6 on 2023-11-05 20:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип питания')),
            ],
            options={
                'verbose_name': 'Тип питания',
                'verbose_name_plural': 'Типы питания',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название тура')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('available_dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), default=[], size=None, verbose_name='Доступные даты')),
                ('duration', models.IntegerField(verbose_name='Продолжительность')),
                ('tour_agency', models.CharField(max_length=100, verbose_name='Турагенство')),
                ('hotel_category', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]), default=list, size=None, verbose_name='Категория отеля')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание')),
                ('country', models.ManyToManyField(to='tour_agency.country', verbose_name='Страна')),
                ('food_type', models.ManyToManyField(to='tour_agency.foodtype', verbose_name='Тип питания')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_date', models.DateField(verbose_name='Выбранная дата')),
                ('selected_category', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Категория отеля')),
                ('persons_number', models.IntegerField(verbose_name='Количество взрослых')),
                ('children_number', models.IntegerField(verbose_name='Количество детей')),
                ('rooms_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Количество номеров')),
                ('status', models.CharField(choices=[('W', 'Ожидает подтверждения'), ('B', 'Забронирован'), ('C', 'Отказано'), ('D', 'Завершен')], max_length=100, verbose_name='Статус бронирования')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_agency.tour', verbose_name='Тур')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Турист')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Оценка')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_agency.tourbooking', verbose_name='Бронирование')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_agency.tour', verbose_name='Тур')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Турист')),
            ],
        ),
        migrations.AddField(
            model_name='tourist',
            name='tours',
            field=models.ManyToManyField(blank=True, related_name='tourists', through='tour_agency.TourBooking', to='tour_agency.tour', verbose_name='Туры'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
