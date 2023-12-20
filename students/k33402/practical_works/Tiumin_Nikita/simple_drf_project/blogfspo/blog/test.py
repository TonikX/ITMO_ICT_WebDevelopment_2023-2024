from models import *
from django.utils import timezone


cars = []

cars.append(Car.objects.create(license_plate='x231qw', brand='honda', model='civic'))
cars.append(Car.objects.create(license_plate='r627tn', brand='honda', model='civic'))
cars.append(Car.objects.create(license_plate='l095ns', brand='honda', model='civic'))
cars.append(Car.objects.create(license_plate='l753nd', brand='honda', model='civic'))
cars.append(Car.objects.create(license_plate='p016gf', brand='honda', model='civic'))

for car in cars:
    car.save()

owners = []

owners.append(Owner.objects.create(first_name='victor', last_name='sokolov'))
owners.append(Owner.objects.create(first_name='petr', last_name='porechenko'))
owners.append(Owner.objects.create(first_name='diana', last_name='kekeke'))
owners.append(Owner.objects.create(first_name='elizaveta', last_name='davydova'))
owners.append(Owner.objects.create(first_name='ekaterina', last_name='kulakova'))

for owner in owners:
    owner.save()

car_ownerships = []

car_ownerships.append(CarOwnership.objects.create(owner=owners[0], car=cars[0], starts_at=timezone.now()))
car_ownerships.append(CarOwnership.objects.create(owner=owners[1], car=cars[1], starts_at=timezone.now()))
car_ownerships.append(CarOwnership.objects.create(owner=owners[2], car=cars[2], starts_at=timezone.now()))
car_ownerships.append(CarOwnership.objects.create(owner=owners[3], car=cars[3], starts_at=timezone.now()))
car_ownerships.append(CarOwnership.objects.create(owner=owners[4], car=cars[4], starts_at=timezone.now()))

print('hahah')
