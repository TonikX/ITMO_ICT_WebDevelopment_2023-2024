import os

from faker_vehicle import VehicleProvider

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_kononov.settings")

import django

django.setup()

import random

from datetime import datetime, timedelta, date

from faker import Faker

from project_first_app.models import Car, CarOwner, Ownership, DrivingLicense

fake = Faker()
fake.add_provider(VehicleProvider)

def format_datetime(input_date):
    if isinstance(input_date, date):
        return datetime.combine(input_date, datetime.min.time())
    elif isinstance(input_date, datetime):
        return input_date


def create_car_owners(num_owners=6):
    owners = []

    for _ in range(num_owners):
        birth_date = fake.date_of_birth()
        owner = CarOwner.objects.create(
            username=fake.user_name(),
            password=fake.password(),
            passport_number=fake.random_number(digits=10),
            home_address=fake.address(),
            nationality=fake.country(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            birth_date=format_datetime(birth_date),
        )
        owners.append(owner)
        create_driving_license(owner, birth_date)

    return owners


def create_driving_license(owner, birth_date):
    issue_date = fake.date_time_this_decade()

    DrivingLicense.objects.create(
        owner=owner,
        license_number=fake.random_number(digits=8),
        license_type=random.choice(['A', 'B', 'C']),
        issue_date=issue_date,
    )


def create_cars(num_cars=5):
    cars = []

    for _ in range(num_cars):
        car = Car.objects.create(
            registration_number=fake.random_number(digits=6),
            brand=fake.vehicle_make(),
            model=fake.vehicle_model(),
            color=fake.color_name(),
        )
        cars.append(car)

    return cars


def assign_cars_to_owners(owners, cars):
    for owner in owners:
        num_assigned_cars = random.randint(1, 3)
        assigned_cars = random.sample(cars, num_assigned_cars)

        for car in assigned_cars:
            start_date = fake.date_time_this_decade()
            end_date = start_date + timedelta(days=random.randint(30, 365))
            Ownership.objects.create(
                owner=owner,
                car=car,
                start_date=format_datetime(start_date),
                end_date=format_datetime(end_date),
            )


def main():
    owners = create_car_owners()
    cars = create_cars()
    assign_cars_to_owners(owners, cars)


if __name__ == "__main__":
    main()
