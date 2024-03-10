from project_first_app.models import Owner, DriverLicense, Car, Ownership
from datetime import date


owner1 = Owner.objects.create_user(owner_id = 1, username='owner1', password = 'password', first_name='Саша', last_name='Вильнюс', birth_date=date(1985, 5, 15), passport='AB123456', address='г. Москва, ул. Примерная, д. 123', nationality='RU')
owner2 = Owner.objects.create_user(owner_id = 2, username='owner2', first_name='Михаил', last_name='Галустян', birth_date=date(1990, 8, 20), passport='CD789012', address='г. Санкт-Петербург, ул. Образцовая, д. 456', nationality='RU')
owner3 = Owner.objects.create_user(owner_id = 3, username='owner3', first_name='Александр', last_name='Сидоров', birth_date=date(1988, 3, 10), passport='EF456789', address='г. Екатеринбург, ул. Практичная, д. 789', nationality='RU')
owner4 = Owner.objects.create_user(owner_id = 4, username='owner4', first_name='Мария', last_name='Кюри', birth_date=date(1995, 11, 25), passport='GH123456', address='г. Казань, ул. Просторная, д. 101', nationality='RU')
owner5 = Owner.objects.create_user(owner_id = 5, username='owner5', first_name='Евгения', last_name='Кури', birth_date=date(1982, 9, 8), passport='IJ789012', address='г. Нижний Новгород, ул. Березовая, д. 202', nationality='RU')
owner6 = Owner.objects.create_user(owner_id = 6, username='owner6', first_name='Дмитрий', last_name='Денисов', birth_date=date(1993, 7, 2), passport='KL456789', address='г. Ростов-на-Дону, ул. Кленовая, д. 303', nationality='RU')
owner7 = Owner.objects.create_user(owner_id = 7, username='owner7', first_name='Галина', last_name='Миллер', birth_date=date(1987, 12, 18), passport='MN123456', address='г. Владивосток, ул. Кедровая, д. 404', nationality='RU')

car1 = Car.objects.create(car_id = 1, license_plate='ABC123', brand='Toyota', model='Camry', color='Синий')
car2 = Car.objects.create(car_id = 2, license_plate='DEF456', brand='Honda', model='Civic', color='Красный')
car3 = Car.objects.create(car_id = 3, license_plate='GHI789', brand='Ford', model='Focus', color='Зелёный')
car4 = Car.objects.create(car_id = 4, license_plate='JKL012', brand='Chevrolet', model='Malibu', color='Серебристый')
car5 = Car.objects.create(car_id = 5, license_plate='MNO345', brand='Nissan', model='Altima', color='Чёрный')
car6 = Car.objects.create(car_id = 6, license_plate='PQR678', brand='BMW', model='X5', color='Белый')

Ownership.objects.create(car_owner_id=1, owner=owner1, car=car1, start_date=date(2020, 1, 1), end_date=date(2021, 12, 31))
Ownership.objects.create(car_owner_id=2, owner=owner1, car=car2, start_date=date(2019, 6, 1), end_date=date(2022, 6, 1))
Ownership.objects.create(car_owner_id=3, owner=owner2, car=car3, start_date=date(2022, 3, 15), end_date=date(2023, 3, 15))
Ownership.objects.create(car_owner_id=4, owner=owner3, car=car4, start_date=date(2021, 8, 10), end_date=date(2024, 8, 10))
Ownership.objects.create(car_owner_id=5, owner=owner4, car=car5, start_date=date(2020, 5, 1), end_date=date(2023, 5, 1))
Ownership.objects.create(car_owner_id=6, owner=owner5, car=car6, start_date=date(2019, 12, 1), end_date=date(2022, 12, 1))
Ownership.objects.create(car_owner_id=7, owner=owner6, car=car2, start_date=date(2019, 6, 1), end_date=date(2022, 6, 1))
Ownership.objects.create(car_owner_id=8, owner=owner7, car=car5, start_date=date(2020, 5, 1), end_date=date(2023, 5, 1))

DriverLicense.objects.create(license_id=1, owner_id=owner1, license_number='DL12345', type='A', registration_date=date(2018, 5, 1))
DriverLicense.objects.create(license_id=2, owner_id=owner2, license_number='DL67890', type='B', registration_date=date(2019, 3, 10))
DriverLicense.objects.create(license_id=3, owner_id=owner3, license_number='DL23456', type='C', registration_date=date(2020, 7, 15))
DriverLicense.objects.create(license_id=4, owner_id=owner4, license_number='DL78901', type='A', registration_date=date(2017, 9, 20))
DriverLicense.objects.create(license_id=5, owner_id=owner5, license_number='DL34567', type='B', registration_date=date(2016, 4, 5))
DriverLicense.objects.create(license_id=6, owner_id=owner6, license_number='DL89012', type='C', registration_date=date(2015, 8, 30))