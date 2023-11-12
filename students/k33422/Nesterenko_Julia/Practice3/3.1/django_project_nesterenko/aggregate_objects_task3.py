import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_nesterenko.settings')
django.setup()

from datetime import date
from django.db.models import Max, Count
from project_first_app.models import *


#   Oldest license
oldest = License.objects.order_by('issue_date')[0]
print("The oldest license")
print(oldest.issue_date)
print()

#   Latest ownership date
max_dates = Ownership.objects.aggregate(Max('date_from'), Max('date_until')).values()
print("The latest ownership date")
print(max(max_dates))
print()

#   Car count for all owners
car_counter = Owner.objects.annotate(Count("owned_cars"))
print("Car count for all owners")
for cr in car_counter:
    print(cr.first_name, cr.last_name, cr.owned_cars__count)
print()

#   Car count for every brand
brand_counter = Car.objects.values('brand').annotate(Count('id'))
print("Car count for every brand")
for bc in brand_counter:
    print(bc['brand'], bc['id__count'])
print()

#   Owners ordered by license issue date
ordered_license = Owner.objects.order_by("driver_license__issue_date")

print("Owners ordered by license issue date")
for ol in ordered_license:
    print(ol.first_name, ol.last_name)
print()
