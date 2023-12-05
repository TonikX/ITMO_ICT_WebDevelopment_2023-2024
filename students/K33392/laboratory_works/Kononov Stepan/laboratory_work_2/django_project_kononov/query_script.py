import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_kononov.settings")

import django

django.setup()

from project_first_app.models import Car, CarOwner, DrivingLicense


def display_query_result(query_name, result):
    print(f"\nResults for {query_name}:\n")
    for item in result:
        print(item)
    print("\n" + "=" * 50 + "\n")


def main():
    # 1. Вывести все машины марки "Toyota" (или любой другой марки):
    toyota_cars = Car.objects.filter(brand='Toyota')
    display_query_result("Toyota Cars", toyota_cars)

    # 2. Найти всех водителей с именем "Robert" (или любым другим именем):
    robert_drivers = CarOwner.objects.filter(first_name='Robert')
    display_query_result("Drivers named Robert", robert_drivers)

    # 3. Взять случайного владельца, получить его id и по этому id получить экземпляр удостоверения (в 2 запроса):
    owner_with_license = None
    while not owner_with_license:
        random_owner = CarOwner.objects.order_by('?').first()
        if random_owner.drivinglicense_set.exists():
            owner_with_license = random_owner

    owner_id = owner_with_license.id
    license_instance = DrivingLicense.objects.get(owner_id=owner_id)
    display_query_result("Random Owner and License", [f"Owner: {owner_with_license}", f"License: {license_instance}"])

    # 4. Вывести всех владельцев красных машин (или любого другого цвета):
    indigo_car_owners = CarOwner.objects.filter(cars__color='Indigo')
    display_query_result("Owners of Indigo Cars", indigo_car_owners)

    # 5. Найти всех владельцев, чей год владения машиной начинается с 2023 (или любой другой год):
    owners_2023 = CarOwner.objects.filter(ownership__start_date__year__gte=2023)
    display_query_result("Owners from 2022", owners_2023)


if __name__ == "__main__":
    main()
