from project_first_app.models import Car, CarOwner, DrivingLicense

# Вывести все машины марки Toyota
print("Машины марки Toyota:")
print(Car.objects.filter(brand="Toyota"))

# Найти всех водителей с именем "Олег"
print("Водители с именем Олег:")
print(CarOwner.objects.filter(first_name="Олег"))

# Взять случайного автовладельца, получить по его id удостоверение
car_owner_john_id = CarOwner.objects.filter(first_name="Джон", last_name="Смит")[0].id
print("Удостоверение Джона Смита:")
print(DrivingLicense.objects.filter(owner_id=car_owner_john_id))

# Вывести всех владельцев красных машин
print("Владельцы красных машин:")
print(CarOwner.objects.filter(cars__color='Red').distinct())

# Вывести всех владельцем машин с годом владения 2023
print("Владельцы машин с 2023 года:")
print(CarOwner.objects.filter(ownerships__start_date__year__gte=2023).distinct())
