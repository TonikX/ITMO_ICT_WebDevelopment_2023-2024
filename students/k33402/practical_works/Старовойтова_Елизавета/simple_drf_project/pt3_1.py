import os
import django
from django.utils import timezone
from random import choice
from django.db.models import Min, Max, Count, F

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_drf_project.settings')
django.setup()

from carsapp.models import Owner, Car, DrivingLicense, Ownership

"""Задание 1"""
# Создание автовладельцев
owners_data = [
    {"last_name": "Иванов", "first_name": "Иван", "birth_date": "1990-01-01"},
    {"last_name": "Федоров", "first_name": "Федор", "birth_date": "1990-01-04"},
    {"last_name": "Старовойтов", "first_name": "Анатолий", "birth_date": "1990-05-01"},
    {"last_name": "Сычев", "first_name": "Михаил", "birth_date": "1995-01-01"},
    {"last_name": "Ярошенко", "first_name": "Мария", "birth_date": "2000-01-01"},
    {"last_name": "Исаченко", "first_name": "Дарья", "birth_date": "2004-01-10"},
]

for data in owners_data:
    owner = Owner.objects.create(**data)

# Создание автомобилей
cars_data = [
    {"registration_number": "А111АА77", "brand": "Toyota", "model": "Camry", "color": "Синий"},
    {"registration_number": "А111YU66", "brand": "Toyota", "model": "Corola", "color": "Красный"},
    {"registration_number": "А222АА77", "brand": "Kia", "model": "Rio", "color": "Белый"},
    {"registration_number": "А411АА77", "brand": "BMW", "model": "X5", "color": "Черный"},
    {"registration_number": "А111АА78", "brand": "Lada", "model": "Granta", "color": "Серый"},
]

for data in cars_data:
    car = Car.objects.create(**data)

# Привязка владельцев к автомобилям и создание владений
ownerships_data = [
    {"owner": Owner.objects.get(last_name="Иванов"), "car": Car.objects.get(registration_number="А111АА77"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Иванов"), "car": Car.objects.get(registration_number="А111АА78"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Федоров"), "car": Car.objects.get(registration_number="А111YU66"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Старовойтов"), "car": Car.objects.get(registration_number="А222АА77"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Сычев"), "car": Car.objects.get(registration_number="А411АА77"), "start_date": timezone.now()},

]

for data in ownerships_data:
    ownership = Ownership.objects.create(**data)

# Создание водительских удостоверений
licenses_data = [
    {"owner": Owner.objects.get(last_name="Иванов"), "license_number": "1234567890", "license_type": "A", "issue_date": "2022-01-01"},
    {"owner": Owner.objects.get(last_name="Федоров"), "license_number": "1234567891", "license_type": "A", "issue_date": "2023-01-01"},
    {"owner": Owner.objects.get(last_name="Старовойтов"), "license_number": "1234567892", "license_type": "A", "issue_date": "2021-04-02"},
    {"owner": Owner.objects.get(last_name="Сычев"), "license_number": "1234567893", "license_type": "A", "issue_date": "2020-08-01"},
    {"owner": Owner.objects.get(last_name="Ярошенко"), "license_number": "1234567894", "license_type": "A", "issue_date": "2022-03-08"},
    {"owner": Owner.objects.get(last_name="Исаченко"), "license_number": "1234567895", "license_type": "A", "issue_date": "2022-01-01"},
]

for data in licenses_data:
    license = DrivingLicense.objects.create(**data)

print("Созданные владельцы:")
for owner in Owner.objects.all():
    print(f"{owner.first_name} {owner.last_name}, Дата рождения: {owner.birth_date}")

print("\nСозданные автомобили:")
for car in Car.objects.all():
    print(f"Гос. номер: {car.registration_number}, Марка: {car.brand}, Модель: {car.model}, Цвет: {car.color}")

print("\nПривязка владельцев к автомобилям:")
for ownership in Ownership.objects.all():
    print(f"{ownership.owner.first_name} {ownership.owner.last_name} владеет автомобилем с гос. номером {ownership.car.registration_number}")

print("\nСозданные водительские удостоверения:")
for license in DrivingLicense.objects.all():
    print(f"{license.owner.first_name} {license.owner.last_name}, Номер удостоверения: {license.license_number}, Тип: {license.license_type}, Дата выдачи: {license.issue_date}")


"""Задание 2"""
# Вывести все машины марки "Toyota"
toyota_cars = Car.objects.filter(brand='Toyota')
print("Машины марки Toyota:", toyota_cars)


# Найти всех водителей с именем "Иван"
ivan_drivers = Owner.objects.filter(first_name='Иван')
print("Водители с именем Иван:", ivan_drivers)


# Взять случайного владельца
random_owner = choice(Owner.objects.all())
print("Случайный владелец:", random_owner)
# Получить id владельца
owner_id = random_owner.id
print(f"ID владельца {random_owner}: {owner_id}")
# Получить экземпляр удостоверения по id
driving_licenses = DrivingLicense.objects.filter(owner_id=owner_id)
print(f"Удостоверения владельца {random_owner}: {driving_licenses}")


# Вывести всех владельцев красных машин
red_car_owners = Owner.objects.filter(ownership__car__color='Красный')
print("Владельцы красных машин:", red_car_owners)


# Найти всех владельцев, чей год владения начинается с 2023
owners_2023 = Owner.objects.filter(ownership__start_date__year=2023)
print("Владельцы, чей год владения начинается с 2023:")
for owner in owners_2023:
    for ownership in owner.ownership.filter(start_date__year=2023):
        print(f"{owner.first_name} {owner.last_name} владеет автомобилем, начиная с {ownership.start_date}")


"""Задание 3"""

# Вывод даты выдачи самого старшего водительского удостоверения
oldest_license_issue_date = DrivingLicense.objects.aggregate(Min('issue_date'))
print("Самая старшая дата выдачи водительского удостоверения:", oldest_license_issue_date['issue_date__min'])

# Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
latest_ownership_date = Ownership.objects.filter(car__model__isnull=False).aggregate(Max('start_date'))
print("Самая поздняя дата владения машиной:", latest_ownership_date['start_date__max'])

# Выведите количество машин для каждого водителя
cars_per_owner = Ownership.objects.values('owner').annotate(num_cars=Count('car')).order_by('owner')
for record in cars_per_owner:
    owner = Owner.objects.get(pk=record['owner'])
    print(f"{owner.first_name} {owner.last_name}: {record['num_cars']} машин")

# Подсчитайте количество машин каждой марки
cars_per_brand = Car.objects.values('brand').annotate(num_cars=Count('id')).order_by('num_cars')
for record in cars_per_brand:
    print(f"Марка: {record['brand']}, Количество машин: {record['num_cars']}")

# Отсортируйте всех автовладельцев по дате выдачи удостоверения
owners_sorted_by_license_date = Owner.objects.annotate(license_date=F('driving_license__issue_date')).order_by('license_date')
for owner in owners_sorted_by_license_date:
    license_date = owner.license_date
    print(f"{owner.first_name} {owner.last_name}, Дата выдачи удостоверения: {license_date}")
