from django.utils import timezone
from project_first_app.models import *

owners_data = [
    {"username": "owner1", "password": "pass1", "surname": "Smith", "name": "John", "date_Birth": "1990-01-01", "passport": "ABC123456", "address": "123 Main St", "nationality": "US"},
    {"username": "owner2", "password": "pass2", "surname": "Johnson", "name": "Emily", "date_Birth": "1985-05-15", "passport": "XYZ789012", "address": "456 Oak St", "nationality": "CA"},
    {"username": "owner3", "password": "pass3", "surname": "Miller", "name": "Chris", "date_Birth": "1988-11-20", "passport": "PQR456789", "address": "789 Maple St", "nationality": "AU"},
    {"username": "owner4", "password": "pass4", "surname": "Davis", "name": "Sophia", "date_Birth": "1992-03-10", "passport": "LMN567890", "address": "101 Pine St", "nationality": "UK"},
    {"username": "owner5", "password": "pass5", "surname": "Martinez", "name": "Daniel", "date_Birth": "1987-07-05", "passport": "JKL123456", "address": "202 Elm St", "nationality": "JP"},
    {"username": "owner6", "password": "pass6", "surname": "Jones", "name": "Olivia", "date_Birth": "1995-09-25", "passport": "FGH234567", "address": "303 Birch St", "nationality": "IN"},
]

for owner_data in owners_data: 
    car_owner = carOwner.objects.create(**owner_data)

cars_data = [
    {"state_number": "ABC123", "brand": "Toyota", "model": "Camry", "color": "Blue"},
    {"state_number": "XYZ789", "brand": "Honda", "model": "Accord", "color": "Red"},
    {"state_number": "LMN456", "brand": "Ford", "model": "Mustang", "color": "Black"},
    {"state_number": "PQR789", "brand": "Chevrolet", "model": "Cruze", "color": "Silver"},
    {"state_number": "JKL234", "brand": "Nissan", "model": "Altima", "color": "White"},
    {"state_number": "IJK567", "brand": "BMW", "model": "X5", "color": "Gray"},
]

for i, car_data in enumerate(cars_data):
    car_instance = car.objects.create(**car_data)

for owner in carOwner.objects.all():
    driver_license_instance = driver_license.objects.create(
        id_owner=owner,
        id_number=f"DL-{owner.id}",
        type="A",
        date_issue=timezone.now()
    )

for car_instance, owner in zip(car.objects.all(), carOwner.objects.all()):
    possession.objects.create(
        id_owner=owner,
        id_car=car_instance,
        date_start=timezone.now(),
        date_end=None
    )
