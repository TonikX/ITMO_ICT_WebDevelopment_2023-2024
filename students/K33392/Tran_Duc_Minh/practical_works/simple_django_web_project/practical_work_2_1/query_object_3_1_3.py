import os
import django
import random
from django.utils import timezone
from django.db.models import Count

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practical_work_2_1.settings")
django.setup()

# Import models after settings are configured
from django_first_app.models import Owner, Car, Own, Driver_license

# Query 1: Date of issuance of the oldest driver's license
oldest_license = Driver_license.objects.order_by('date_issued').first()
oldest_license_date = oldest_license.date_issued if oldest_license else None
oldest_license_owner_name = oldest_license.id_owner.first_name if oldest_license else None
print(f"1. Date of issuance of the oldest driver's license: {oldest_license_owner_name} - {oldest_license_date}")

# Query 2: The latest date of car ownership
latest_car_ownership = Own.objects.order_by('-date_star').first()
latest_car_ownership_date = latest_car_ownership.date_star if latest_car_ownership else None
latest_car_ownership_owner_name = latest_car_ownership.id_owner.first_name if latest_car_ownership else None
print(f"\n2. The latest date of car ownership: {latest_car_ownership_owner_name} - {latest_car_ownership_date}")


# Query 3: Number of cars for each owner
cars_per_owner = Owner.objects.annotate(num_cars=Count('own__id_car')).values('first_name', 'last_name', 'num_cars')
print("\n3. Number of cars for each owner:")
for record in cars_per_owner:
    print(f"{record['first_name']} {record['last_name']} - {record['num_cars']} cars")

# Query 4: Number of cars for each brand
cars_per_brand = Car.objects.values('brand').annotate(num_cars=Count('id_car'))
print("\n4. Number of cars for each brand:")
for record in cars_per_brand:
    print(f"{record['brand']} - {record['num_cars']} cars")

# Query 5: Owners sorted by date of issuance of the driver's license (distinct)
sorted_owners_by_license_date = Owner.objects.order_by('driver_license__date_issued').distinct()
print("\n5. Owners sorted by date of issuance of the driver's license (distinct):")
for owner in sorted_owners_by_license_date:
    date_issued = owner.driver_license_set.first().date_issued if owner.driver_license_set.exists() else None
    print(f"{owner} - Date Issued: {date_issued}")

