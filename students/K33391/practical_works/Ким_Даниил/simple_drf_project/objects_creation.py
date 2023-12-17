from students.K33391.practical_works.Ким_Даниил.simple_django_web_project.django_project_Kim.project_first_app.models import *
from django.utils import timezone
from faker import Faker

fake = Faker()

for _ in range(6):
    car_owner = CarOwner.objects.create(
        first_name=fake.first_name(),
        second_name=fake.last_name(),
        birthday=fake.date_of_birth(minimum_age=18, maximum_age=80),
        passport=fake.unique.random_number(digits=10),
        address=fake.address(),
        nationality=fake.country()
    )

    driver_license = DriverLicense.objects.create(
        owner_id=car_owner,
        license_number=fake.unique.random_number(digits=8),
        license_type=fake.random_element(elements=('A', 'B', 'C')),
        issue_date=fake.date_of_birth(minimum_age=18)
    )

    for _ in range(3):
        car = Car.objects.create(
            state_number=fake.unique.random_number(digits=6),
            brand=fake.random_element(elements=('Toyota', 'BMW', 'Exceed')),
            model=fake.word(),
            color=fake.color_name()
        )

        CarOwn.objects.create(
            car_owner=car_owner,
            car=car,
            start_date=timezone.now(),
            end_date=None
        )
