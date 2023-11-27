from project_first_app.models import Car, CarOwner, Ownership, DrivingLicense
from django.db.models import Min, Max, Count

# Вывод даты самого старшего водительского удостоверения
print("Дата самого старшего водительского удостоверение:")
print(DrivingLicense.objects.aggregate(oldest_issue_date=Min("issue_date"))["oldest_issue_date"].strftime("%d.%m.%Y, "
                                                                                                          "%H:%M:%S"))

# Вывод даты самого позднего владения среди всех моделей
print("Дата самого позднего владения:")
print(Ownership.objects.aggregate(latest_end_date=Max("end_date"))["latest_end_date"].strftime("%d.%m.%Y, %H:%M:%S"))

# Вывод количества автомобилей каждого автовладельца
cars_per_owner = CarOwner.objects.annotate(num_cars=Count("cars")).values("id", "num_cars")
print("Количество автомобилей каждого автовладельца:")
for item in cars_per_owner:
    print(CarOwner.objects.get(id=item["id"]), "has", item["num_cars"], "cars")

# Вывод количества автомобилей каждой марки
car_brands_count = Car.objects.values("brand").annotate(Count("id")).order_by("brand")
print("Количество автомобилей каждой марки:")
for item in car_brands_count:
    print(item["brand"], "is presented by", item["id__count"], "cars")

# Сортировка автовладельцев по дате выдачи удостоверения
owners_sorted_by_license_date = CarOwner.objects.filter(
    licenses__isnull=False
).annotate(
    earliest_license_date=Min("licenses__issue_date")
).order_by(
    "earliest_license_date"
)
print("Автовладельцы, отсортированные по дате выдачи водительского удостоверения:")
print(*owners_sorted_by_license_date, sep="\n")
