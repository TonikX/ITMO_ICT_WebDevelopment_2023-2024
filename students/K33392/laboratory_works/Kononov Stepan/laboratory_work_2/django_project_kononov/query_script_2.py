import os

from django.db.models import Count, Min, Max

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_kononov.settings")

import django

django.setup()

from project_first_app.models import Car, CarOwner, DrivingLicense, Ownership


def display_query_result(query_name, result):
    print(f"\nResults for {query_name}:\n")
    for item in result:
        print(item)
    print("\n" + "=" * 50 + "\n")


def main():
    # 1. Вывести дату выдачи самого старшего водительского удостоверения:
    oldest_license_date = DrivingLicense.objects.aggregate(oldest_date=Min('issue_date'))
    display_query_result("Oldest Driving License Issue Date",
                         [f"Oldest License Issue Date: {oldest_license_date['oldest_date']}"])

    # 2. Самая поздняя дата владения машиной существующей модели:
    latest_ownership_date = Ownership.objects.filter(car__model__isnull=False).aggregate(latest_date=Max('end_date'))
    display_query_result("Latest Ownership Date for Existing Car Model",
                         [f"Latest Ownership Date: {latest_ownership_date['latest_date']}"])

    # 3. Вывести количество машин для каждого водителя:
    owners_with_car_count = CarOwner.objects.annotate(car_count=Count('cars'))
    car_count_results = [f"{owner} - {owner.car_count} машин" for owner in owners_with_car_count]
    display_query_result("Car Count for Each Owner", car_count_results)

    # 4. Количество машин каждой марки:
    car_brand_count = Car.objects.values('brand').annotate(brand_count=Count('id'))
    brand_count_results = [f"{item['brand']} - {item['brand_count']} машин" for item in car_brand_count]
    display_query_result("Car Count for Each Brand", brand_count_results)

    # 5. Сортировка всех автовладельцев по дате выдачи удостоверения:
    distinct_owners = CarOwner.objects.distinct().order_by('drivinglicense__issue_date')
    sorted_owners_results = [f"{owner} - {owner.drivinglicense.issue_date}" for owner in distinct_owners if
                             owner.drivinglicense]
    display_query_result("Sorted Owners by Driving License Issue Date", sorted_owners_results)




if __name__ == "__main__":
    main()
