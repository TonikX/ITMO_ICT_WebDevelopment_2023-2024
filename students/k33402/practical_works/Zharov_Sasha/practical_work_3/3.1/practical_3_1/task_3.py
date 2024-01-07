import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_3_1.settings')
django.setup()

from django.db.models import Count
from main.models import *

# Задание 1. Вывод даты выдачи самого старшего водительского удостоверения
oldest_licence_date = DriverLicence.objects.all().order_by('release_date').first().release_date

print(oldest_licence_date)
# Задание 2. Укажите самую позднюю дату владения машиной существующей моделью
latest_ownership_date = Ownership.objects.filter(car__isnull=False).order_by('-date_end').first().date_end

print(latest_ownership_date)
# Задание 3. Выведите количество машин для каждого водителя
cars_per_driver = Driver.objects.annotate(num_cars=Count('cars'))

print(cars_per_driver)
# Задание 4. Подсчитайте количество машин каждой марки
cars_count_by_brand = Car.objects.values('brand').annotate(num_cars=Count('id'))

print(cars_count_by_brand)
# Задание 5. Отсортируйте всех автовладельцев по дате выдачи удостоверения (исключив дубликаты)
sorted_drivers = Driver.objects.order_by('driverlicence__release_date').distinct()

print(sorted_drivers)