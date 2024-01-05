from blog.models import *
from django.utils import timezone
from django.db.models import Min, Max, Count, Avg, Sum


def pr1():
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


def pr2():
    hondas = Car.objects.filter(brand='honda').all()
    olegs = Owner.objects.filter(first_name='oleg').all()
    ownership = CarOwnership.objects.filter(owner_id=olegs[0]).all()
    red_cars = Car.objects.filter(color='red').all()

    red_car_owners = list(map(
        lambda x: x.owner_id,
        CarOwnership.objects.filter(car_id__in=map(lambda x: x.id, red_cars)).all()
    ))

    print('hondas:')
    print(hondas)
    print('olegs:')
    print(olegs)
    print('ownership:')
    print(ownership)
    print('red_cars:')
    print(red_cars)
    print('red_car_owners:')
    print(red_car_owners)


def pr3():
    oldest_licence = DriverLicense.objects.order_by('-issued_at').first().id
    owners = Owner.objects.annotate(Count('cars'))
    cars = Car.objects.values('brand').annotate(Count('id'))
    owners_ordered = Owner.objects.order_by('licence').distinct

    print('oldest_licence:')
    print(oldest_licence)
    print('owners\' cars')
    print(list(map(lambda x: x.first_name + ' ' + x.last_name + ': ' + str(x.cars__count), owners)))
    print('cars count by brand:')
    print(cars)
    print('ordered owners:')
    print(owners_ordered)



if __name__ == '__main__':
    pass
