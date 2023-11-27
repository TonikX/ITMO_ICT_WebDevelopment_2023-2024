import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_nesterenko.settings')
django.setup()

from datetime import date
from project_first_app.models import *


#   All Toyotas
toyotas = Car.objects.filter(brand='Toyota')
print("All Toyota cars")
for t in toyotas:
    print(t.license_plate, t.brand, t.model, t.color)
print()

#   All owners named James
js = Owner.objects.filter(first_name='James')
print("All owners named James")
for j in js:
    print(j.first_name, j.last_name)
print()

#   Leo Tolstoy's license
leo = Owner.objects.get(first_name='Leo').id
license = License.objects.get(owner__id=leo)
print("Leo Tolstoy's license")
print(license.number, license.type, license.issue_date)
print()

#   All owners of a black car
blcar = Owner.objects.filter(as_car_owner__car__color='Black')
print("All owners of a black car")
for b in blcar:
    print(b.first_name, b.last_name)
print()

#   Ownership started in 1950 or later
ownerships = Ownership.objects.filter(date_from__gte=date(1950, 1, 1))

print("All owners whose car ownership started in 1950 or later")
for o in ownerships:
    print(o.owner.first_name, o.owner.last_name, '-',
          o.car.license_plate, o.car.brand, o.car.model, o.car.color)
print()