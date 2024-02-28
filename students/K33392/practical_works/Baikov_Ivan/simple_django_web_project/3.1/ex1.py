from datetime import datetime, timedelta
from django.utils import timezone
from project_first_app.models import *

# Create 7 car owners
owners_data = [
  {
    "username": "owner1",
    "password": "password1",
    "first_name": "John",
    "last_name": "Doe",
  },
  {
    "username": "owner2",
    "password": "password2",
    "first_name": "Jane",
    "last_name": "Doe",
  },
  {
    "username": "owner3",
    "password": "password3",
    "first_name": "Alice",
    "last_name": "Smith",
  },
  {
    "username": "owner4",
    "password": "password4",
    "first_name": "Bob",
    "last_name": "Johnson",
  },
  {
    "username": "owner5",
    "password": "password5",
    "first_name": "Eva",
    "last_name": "Brown",
  },
  {
    "username": "owner6",
    "password": "password6",
    "first_name": "Charlie",
    "last_name": "Miller",
  },
]

owners = [CarOwner.objects.create(**data) for data in owners_data]

# Create 6 cars
cars_data = [
  {"number": "ABC123", "model": "Toyota", "color": "Blue"},
  {"number": "XYZ456", "model": "Honda", "color": "Red"},
  {"number": "DEF789", "model": "Ford", "color": "Green"},
  {"number": "GHI123", "model": "Chevrolet", "color": "Black"},
  {"number": "JKL456", "model": "Tesla", "color": "White"},
  {"number": "MNO789", "model": "BMW", "color": "Silver"},
]

for data in cars_data:
  Car.objects.create(**data)

# Create driver's licenses for each owner
licenses_data = [
  {
    "owner": owner,
    "number": f"DL{index + 1}",
    "_type": "A",
    "issue_date": timezone.now(),
  }
  for index, owner in enumerate(owners)
]

for data in licenses_data:
  DriversLicence.objects.create(**data)

# Assign 1 to 3 cars for each owner
for owner, car in zip(CarOwner.objects.all(), Car.objects.all()):
  Ownership.objects.create(
    owner=owner,
    car=car,
    start_date=timezone.now(),
    end_date=timezone.now() + timedelta(days=365),
  )
