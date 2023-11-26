import os
import django
import random
from django.utils import timezone

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practical_work_2_1.settings")
django.setup()

# Import models after settings are configured
from django_first_app.models import Owner, Car, Own, Driver_license

# Query 1: All cars of brand 'Toyota'
toyota_cars = Car.objects.filter(brand='Toyota')
print("1. All cars of brand 'Toyota':")
for car in toyota_cars:
    print(car.model)

# Query 2: All owners with the first name 'Иван'
ivan_drivers = Owner.objects.filter(first_name='Иван')
print("\n2. All owners with the first name 'Иван':")
for owner in ivan_drivers:
    print(owner, owner.last_name)

# Query 3: Random owner and their driver license
random_owner = random.choice(Owner.objects.all())
driver_license = Driver_license.objects.filter(id_owner=random_owner).first()
print(f"\n3. Driver license of a random owner ({random_owner}):")
print(f"{driver_license.license_number} {random_owner.first_name} {random_owner.last_name}")

# Query 4: All owners of red cars
red_car_owners = Owner.objects.filter(car__color='Red')
print("\n4. All owners of red cars:")
for owner in red_car_owners:
    print(owner, owner.last_name)

# Query 5: Owners with cars purchased since 2010
owners_2010 = Owner.objects.filter(own__date_star__year__gte=2010)
print("\n5. Owners with cars purchased since 2010:")
for owner in owners_2010:
    date_start = Own.objects.filter(id_owner=owner).first().date_star
    print(f"{owner} - Date Star: {date_start}")
