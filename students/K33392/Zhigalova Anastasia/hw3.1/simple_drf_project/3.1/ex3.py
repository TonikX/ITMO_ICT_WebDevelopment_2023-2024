from project_first_app.models import *
from django.db.models import Count, Min

oldest_license = driver_license.objects.order_by('date_issue').first()
print(f"Oldest Driver's License: {oldest_license.id_number} - Type: {oldest_license.type} - Date of Issue: {oldest_license.date_issue}")

oldest_possession = possession.objects.order_by('date_start').first()
print(f"Oldest Possession: Car ID {oldest_possession.id_car.id} by Owner ID {oldest_possession.id_owner.id} - Start Date: {oldest_possession.date_start}")

# Query cars count by user
users_with_car_count = carOwner.objects.annotate(car_count=Count('car'))

# Print information about each user and their car count
for user in users_with_car_count:
    print(f"User: {user.username} - Car Count: {user.car_count}")

# Query cars count by brand
cars_by_brand_count = car.objects.values('brand').annotate(car_count=Count('brand'))

# Print information about each brand and its car count
for brand_info in cars_by_brand_count:
    print(f"Brand: {brand_info['brand']} - Car Count: {brand_info['car_count']}")

# Query users sorted by driver's license issue date
users_sorted_by_license_issue_date = carOwner.objects.annotate(
    min_license_issue_date=Min('driver_license__date_issue')
).order_by('min_license_issue_date')

# Print information about each user and their driver's license issue date
for user in users_sorted_by_license_issue_date:
    print(f"User: {user.username} - Oldest Driver's License Issue Date: {user.min_license_issue_date}")