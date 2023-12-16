import os

import django
from django.db.models import Min, Max, Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_first_app.settings")
django.setup()

from blog.models import CustomUser, Auto, Ownership, DrivingLicence

oldest_licence = DrivingLicence.objects.aggregate(max_start_date=Min("start_date"))["max_start_date"]

newest_ownership = Ownership.objects.aggregate(max_start_date=Max("start_date"))["max_start_date"]

ownerships_counts = CustomUser.objects.annotate(count=Count("ownerships"))
ownerships_counts_str = [f"{owner.full_name}: {owner.count}" for owner in ownerships_counts]

cars_count_by_brands = Auto.objects.values("brand").annotate(count=Count("id"))
cars_count_by_brands_str = [f"{car['brand']}: {car['count']}" for car in cars_count_by_brands]

sorted_owners = CustomUser.objects.order_by("ownerships__start_date").all()

print(
    f"Дата самого старшего удостоверения: {oldest_licence}",
    f"Самая поздняя дата авто владения: {newest_ownership}",
    f"Количество машин для каждого водителя: {ownerships_counts_str}",
    f"Количество машин каждой марки: {cars_count_by_brands_str}",
    f"Автовладельцы, отсортированные по дате выдачи удостоверения: {sorted_owners}",
    sep="\n\n",
)