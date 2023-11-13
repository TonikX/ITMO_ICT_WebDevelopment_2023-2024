import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_3_1.settings')
django.setup()

from django.utils import timezone
from main.models import *


# Создаем автовладельцев
drivers_data = [
    {"first_name": "John", "last_name": "Doe", "birth_date": timezone.now()},
    {"first_name": "Alice", "last_name": "Smith", "birth_date": timezone.now()},
    {"first_name": "Bob", "last_name": "Johnson", "birth_date": timezone.now()},
    {"first_name": "Eva", "last_name": "Williams", "birth_date": timezone.now()},
    {"first_name": "Michael", "last_name": "Brown", "birth_date": timezone.now()},
    {"first_name": "Olivia", "last_name": "Jones", "birth_date": timezone.now()},
]


created_drivers = []
for data in drivers_data:
    driver = Driver.objects.create(**data)
    created_drivers.append(driver)
    print(f"Создан владелец: {driver}")

# Создаем автомобили
cars_data = [
    {"number": "ABC123", "brand": "Toyota", "car_model": "Camry", "color": "Blue"},
    {"number": "XYZ456", "brand": "Honda", "car_model": "Accord", "color": "Red"},
    {"number": "DEF789", "brand": "Ford", "car_model": "Focus", "color": "Silver"},
    {"number": "GHI012", "brand": "Chevrolet", "car_model": "Malibu", "color": "White"},
    {"number": "JKL345", "brand": "Nissan", "car_model": "Altima", "color": "Black"},
    {"number": "MNO678", "brand": "Hyundai", "car_model": "Elantra", "color": "Gray"},
]

created_cars = []
for data in cars_data:
    car = Car.objects.create(**data)
    created_cars.append(car)
    print(f"Создан автомобиль: {car}")

# Назначаем удостоверение каждому владельцу
for driver in created_drivers:
    licence_data = {"owner": driver, "number": "12345", "type": "B", "release_date": timezone.now()}
    driver_licence = DriverLicence.objects.create(**licence_data)
    print(f"Владелец {driver} получил удостоверение: {driver_licence}")


    for car in created_cars[:2]: 
        ownership_data = {"car": car, "driver": driver, "date_start": timezone.now(), "date_end": timezone.now()}
        ownership = Ownership.objects.create(**ownership_data)
        print(f"{driver} стал владельцем автомобиля {car}: {ownership}")
