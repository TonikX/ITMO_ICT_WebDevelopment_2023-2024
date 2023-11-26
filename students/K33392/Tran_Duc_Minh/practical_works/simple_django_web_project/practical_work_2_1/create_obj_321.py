from datetime import datetime
from django.utils import timezone
import os
import django
import random

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practical_work_2_1.settings")
django.setup()

# Import models after settings are configured
from django_first_app.models import Owner, Car, Own, Driver_license

# Создаем 6-7 новых автовладельцев
owners_data = [
    {'last_name': 'Smith', 'first_name': 'John', 'date_of_birth': datetime(1985, 5, 15, tzinfo=timezone.utc)},
    {'last_name': 'Hai', 'first_name': 'Xuan', 'date_of_birth': datetime(2002, 1, 14, tzinfo=timezone.utc)},
    {'last_name': 'Dung', 'first_name': 'Hoang', 'date_of_birth': datetime(2002, 11, 3, tzinfo=timezone.utc)},
    {'last_name': 'Truong', 'first_name': 'Hoang', 'date_of_birth': datetime(2002, 11, 15, tzinfo=timezone.utc)},
    {'last_name': 'Sam', 'first_name': 'Thanh', 'date_of_birth': datetime(2002, 2, 11, tzinfo=timezone.utc)},
    {'last_name': 'Bao', 'first_name': 'Gia', 'date_of_birth': datetime(2002, 5, 15, tzinfo=timezone.utc)},
]

for owner_data in owners_data:
    owner = Owner.objects.create(**owner_data)

# Создаем 5-6 автомобилей
cars_data = [
    {'state_number': 'ABC123', 'brand': 'Toyota', 'model': 'Camry', 'color': 'Blue'},
    {'state_number': 'ABC456', 'brand': 'Honda', 'model': 'Civic', 'color': 'Red'},
    {'state_number': 'ABC789', 'brand': 'Ford', 'model': 'Focus', 'color': 'Blue'},
    {'state_number': 'XYZ123', 'brand': 'Chevrolet', 'model': 'Malibu', 'color': 'Gray'},
    {'state_number': 'XYZ456', 'brand': 'Nissan', 'model': 'Altima', 'color': 'Pink'},
    {'state_number': 'XYZ789', 'brand': 'Hyundai', 'model': 'Elantra', 'color': 'Black'},

]

for car_data in cars_data:
    car = Car.objects.create(**car_data)

    # Назначаем случайному владельцу от 1 до 3 автомобилей
    num_owners = random.randint(1, 3)
    for _ in range(num_owners):
        owner = random.choice(Owner.objects.all())
        own_date = datetime.now(tz=timezone.utc)
        car.owners.add(owner, through_defaults={'date_star': own_date})
        # Создаем запись владения
        Own.objects.create(id_owner=owner, id_car=car, date_star=own_date)

# Создаем удостоверения для каждого владельца
licenses_data = [
    {'id_owner': owner, 'license_number': '123456', 'type': 'A', 'date_issued': datetime(2020, 1, 1)},
    {'id_owner': owner, 'license_number': '333222', 'type': 'A', 'date_issued': datetime(2020, 1, 1)},
    {'id_owner': owner, 'license_number': '444444', 'type': 'B', 'date_issued': datetime(2020, 1, 1)},
    {'id_owner': owner, 'license_number': '555555', 'type': 'B', 'date_issued': datetime(2020, 1, 1)},
    {'id_owner': owner, 'license_number': '666666', 'type': 'C', 'date_issued': datetime(2020, 1, 1)},
    {'id_owner': owner, 'license_number': '777777', 'type': 'A', 'date_issued': datetime(2020, 1, 1)},

]

for license_data in licenses_data:
    Driver_license.objects.create(**license_data)
