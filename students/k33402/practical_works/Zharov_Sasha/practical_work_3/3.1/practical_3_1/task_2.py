import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_3_1.settings')
django.setup()

from django.utils import timezone
from main.models import *

# Задание 1. Найти автомобили марки Toyota
cars = Car.objects.filter(brand='Toyota')
print(cars)

# Задание 2. Найти водителей с именем John
drivers = Driver.objects.filter(first_name='John')
print(drivers)


# Задание 3. Получить случайного владельца и получить экземпляр удостоверения по id владельца
random_owner = random.choice(Driver.objects.all())

licence = DriverLicence.objects.get(owner_id=random_owner.id)

print(licence)

# Задание 4. Вывести всех владельцев красных автомобилей
red_car_owners = Driver.objects.filter(cars__color='Red')

print(red_car_owners)

# Задание 5. Вывести всех владельцев, срок владения машиной которых начинается с 2010
owners_2010 = Driver.objects.filter(ownership__date_start__year=2023)

print(owners_2010)