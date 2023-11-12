import datetime
from practice.models import *

temp = datetime.datetime.now()
names = (
    ('Кирюша', 'Билибдович', temp),
    ('Симеон', 'Гидеонович', temp),
    ('Стас', 'Редько', temp),
    ('Тоха', 'Противогаз', temp),
    ('Наталья', 'Оникиенко', temp),
    ('Клара', 'Укралова', temp))

tup_cars = (
    ('А228УЕ', 'ВАЗ', '2121', 'Баклажановый'),
    ('В666АД', 'ВАЗ', '1111', 'Синий'),
    ('Д420УЙ', 'Феррари', '812', 'Красный'),
    ('Н282ЕТ', 'Додж', 'Челенджер 1982', 'Черный, синяя полоса'),
    ('Е100ГЭ', 'КАМАЗ', 'М65952', 'Оранжевый'),
    ('УД777А', 'ХЁНДАЙ', 'Солярис', 'Белый')
    )

tup_licence = (
    [0, '1337БУ', 'A1', temp],
    [0, '1488КУ', 'C', temp],
    [0, '6969ДУ', 'D1', temp],
    [0, '7101ФУ', 'B1', temp],
    [0, '2000ЗУ', 'M', temp],
    [0, '2069ХУ', 'A1', temp])

for i in range(6):
    owner = CarOwner.objects.create(name=names[i][0], surname=names[i][1], birthdate=names[i][2])
    licence = DriverLicence.objects.create(owner_id=owner, licence_id=tup_licence[i][1], licence_type=tup_licence[i][2], recieved_date=tup_licence[i][3])
    car = Car.objects.create(plate=tup_cars[i][0], brand=tup_cars[i][1], model=tup_cars[i][2], color=tup_cars[i][3])
    ownership = Ownership.objects.create(car_id=car, start_date=temp, end_date=temp)
    ownership.owner_id.add(owner)

# использовал exec("текст") для заполнения

# 2 задание
# Сar.objects.filter(brand="ВАЗ")