import os
import django
from django.utils import timezone

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practical_work_2_1.settings")
django.setup()

# Import models after settings are configured
from django_first_app.models import Owner, Car, Own, Driver_license

# Создаем владельцев
owner1 = Owner.objects.create(last_name='Иванов', first_name='Иван', date_of_birth=timezone.now())
owner2 = Owner.objects.create(last_name='Петров', first_name='Петр', date_of_birth=timezone.now())
owner3 = Owner.objects.create(last_name='Сидоров', first_name='Сидор', date_of_birth=timezone.now())
owner4 = Owner.objects.create(last_name='Козлов', first_name='Козел', date_of_birth=timezone.now())
owner5 = Owner.objects.create(last_name='Новиков', first_name='Новик', date_of_birth=timezone.now())
owner6 = Owner.objects.create(last_name='Смирнов', first_name='Смирн', date_of_birth=timezone.now())
owner7 = Owner.objects.create(last_name='Васнецов', first_name='Василий', date_of_birth=timezone.now())

# Создаем автомобили
car1 = Car.objects.create(state_number='ABC123', brand='Toyota', model='Camry', color='Blue')
car2 = Car.objects.create(state_number='XYZ789', brand='Honda', model='Civic', color='Red')
car3 = Car.objects.create(state_number='LMN456', brand='Ford', model='Focus', color='Silver')
car4 = Car.objects.create(state_number='JKL321', brand='Chevrolet', model='Malibu', color='Black')
car5 = Car.objects.create(state_number='PQR987', brand='Nissan', model='Altima', color='White')
car6 = Car.objects.create(state_number='DEF654', brand='Hyundai', model='Elantra', color='Gray')

# Создаем водительские лицензии
license1 = Driver_license.objects.create(id_owner=owner1, license_number='12345', type='A', date_issued=timezone.now())
license2 = Driver_license.objects.create(id_owner=owner2, license_number='67890', type='B', date_issued=timezone.now())
license3 = Driver_license.objects.create(id_owner=owner3, license_number='54321', type='C', date_issued=timezone.now())
license4 = Driver_license.objects.create(id_owner=owner4, license_number='98765', type='A', date_issued=timezone.now())
license5 = Driver_license.objects.create(id_owner=owner5, license_number='24680', type='B', date_issued=timezone.now())
license6 = Driver_license.objects.create(id_owner=owner6, license_number='13579', type='C', date_issued=timezone.now())
license7 = Driver_license.objects.create(id_owner=owner7, license_number='11111', type='A', date_issued=timezone.now())

# Привязываем автомобили к владельцам через ассоциативную сущность
ownership1 = Own.objects.create(id_owner=owner1, id_car=car1, date_star=timezone.now())
ownership2 = Own.objects.create(id_owner=owner2, id_car=car2, date_star=timezone.now())
ownership3 = Own.objects.create(id_owner=owner3, id_car=car3, date_star=timezone.now())
ownership4 = Own.objects.create(id_owner=owner4, id_car=car4, date_star=timezone.now())
ownership5 = Own.objects.create(id_owner=owner5, id_car=car5, date_star=timezone.now())
ownership6 = Own.objects.create(id_owner=owner6, id_car=car6, date_star=timezone.now())

# Выводим созданные объекты
print("Владельцы:")
print(Owner.objects.all())
print("\nАвтомобили:")
print(Car.objects.all())
print("\nВодительские лицензии:")
print(Driver_license.objects.all())
