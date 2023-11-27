import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_first_app.settings")
django.setup()

from django.utils import timezone
from blog.models import CustomUser, Auto, Ownership, DrivingLicence


owners = CustomUser.objects.bulk_create(
    [
        CustomUser(last_name="Кулагина", first_name="Ирина", birthdate=timezone.now()),
        CustomUser(last_name="Наумова", first_name="Анна", birthdate=timezone.now()),
        CustomUser(last_name="Крикунов", first_name="Павел", birthdate=timezone.now()),
        CustomUser(last_name="Лобов", first_name="Максим", birthdate=timezone.now()),
        CustomUser(last_name="Алешкин", first_name="Евгений", birthdate=timezone.now()),
        CustomUser(last_name="Дмитриева", first_name="Юлия", birthdate=timezone.now()),
    ]
)


cars = Auto.objects.bulk_create(
    [
        Auto(state_number="E321АА70", brand="Lada", model="Vesta", color="серебристый"),
        Auto(state_number="В222ВВ70", brand="Hyundai", model="Solaris", color="синий"),
        Auto(state_number="В533ВС70", brand="Toyota", model="Corolla", color="черный"),
        Auto(state_number="К444МС70", brand="Hyundai", model="Solaris", color="серый"),
        Auto(state_number="Т555ТТ70", brand="Kia", model="Rio", color="черный"),
        Auto(state_number="О266ОМ70", brand="Toyota", model="Corolla", color="зеленый"),
    ]
)

ownerships = Ownership.objects.bulk_create(
    [Ownership(owner=owners[i], auto=cars[i], start_date=timezone.now()) for i in range(6)]
)

licences = DrivingLicence.objects.bulk_create(
    [DrivingLicence(owner=owners[i], number=str(i + 1) * 10, type="B", start_date=timezone.now()) for i in range(6)]
)

print("Автовладельцы:")
for owner in owners:
    print(f"{owner.full_name} - {owner.birthdate}")

print("\nАвтомобили:")
for car in cars:
    print(f"{car.brand} {car.model} ({car.state_number})")

print("\nВладения:")
for ownership in ownerships:
    print(f"{ownership.owner.full_name} владеет {ownership.auto.brand} {ownership.auto.model}")

print("\nЛицензии:")
for licence in licences:
    print(f"{licence.owner.full_name} - {licence.number}")
