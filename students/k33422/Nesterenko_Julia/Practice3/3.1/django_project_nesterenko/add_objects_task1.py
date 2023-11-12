import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_nesterenko.settings')
django.setup()

from datetime import date
from project_first_app.models import *


#   Owners
first_names = ['Anna', 'James', 'Bill', 'Jane', 'Leo', 'Willy']
last_names = ['Pavlova', 'Bond', 'Clinton', 'Austen', 'Tolstoy', 'Wonka']
birthdays = [date(1903, 12, 1), date(1920, 11, 2), date(1948, 3, 15),
             date(1775, 12, 16), date(1850, 2, 24), date(1900, 1, 1)]

#   Licences
numbers = ['9324311290', '8842451291', '0288872181',
           '5369135664', '7458252854', '0929424112']
types = ['C', 'B', 'A', 'B', 'C', 'D']
dates = [date(1930, 1, 1), date(1960, 1, 1), date(1990, 1, 1),
         date(1800, 1, 1), date(1890, 1, 1), date(1920, 1, 1)]

#   Cars
plates = ['k333kk178', 'p434pp178', 'k126oo178',
          'm909mm178', 'a565ka178', 'c778cc178']
brands = ['Toyota', 'Audi', 'Toyota', 'Kia', 'Toyota', 'Peugeot']
models = ['Land Cruiser', 'F300', 'Corolla', 'Rio', 'Crown', '3008']
colors = ['Blue', 'Red', 'Black', 'Green', 'Black', 'White']

#   Ownerships
dfrom = [date(1930, 11, 1), date(1960, 11, 1), date(1990, 11, 1),
         date(1800, 11, 1), date(1890, 11, 1), date(1920, 11, 1)]
duntil = [date(1932, 12, 1), date(1962, 12, 1), date(1992, 12, 11),
          date(1802, 12, 1), date(1892, 12, 1), date(1922, 12, 1)]

for (fn, ln, b,
     n, t, d,
     p, br, m, c,
     df, du) in zip(first_names, last_names, birthdays,
                    numbers, types, dates,
                    plates, brands, models, colors,
                    dfrom, duntil):
    o = Owner(first_name=fn, last_name=ln, birthday=b)
    o.save()
    l = License(owner=o, number=n, type=t, issue_date=d)
    l.save()
    c = Car(license_plate=p, brand=br, model=m, color=c)
    c.save()
    os = Ownership(owner=o, car=c, date_from=df, date_until=du)
    os.save()

