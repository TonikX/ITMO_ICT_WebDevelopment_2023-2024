# Практическая 3.1
## Особенности выполнения работы
Чтобы использовать все необходимые для выполнения практической работы команды, необходимо запускать их через shell и команду exec(). Таким образом можно делать запросы на получение и создание необходимых данных в таблицах, не используя IDE.
## Код для генерации данных
```Python
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

```
## Код для второй части задания
```Python
from practice.models import Car, CarOwner, DriverLicence, Ownership
# Все ВАЗы
print(Car.objects.filter(brand="ВАЗ"))

# Все водители Симеоны
print(CarOwner.objects.filter(name="Симеон"))

# Лицензия по водителю
owner = getattr(CarOwner.objects.first(), 'id')
print(DriverLicence.objects.filter(owner_id=owner))

# хозяева баклажановых машин
eggplant = Ownership.objects.filter(car_id__color="Баклажановый").values("owner_id__name", "owner_id__surname")
print(eggplant)

# владеющие авто с 2010
import datetime

datetime_object = datetime.date(2010, 10, 12)

ownership = Ownership.objects.filter(start_date__gte=datetime_object)
print(ownership)
```
## Код запросов для третьей части задания
```Python
from practice.models import Car, CarOwner, DriverLicence, Ownership
from django.db.models import Max, Count

# Самая старая лицензия
oldest_licence = DriverLicence.objects.aggregate(oldest=Max("recieved_date"))
print(oldest_licence)

# Самое новое приобретение
ownership = Ownership.objects.aggregate(Max("start_date"))
print(ownership)

# Количество машин во владении каждого владельца
car_owners = CarOwner.objects.annotate(cnt=Count('ownership'))
print([f"Количество машин во владении {i.name} {i.surname} составляет {i.cnt}" for i in car_owners])

# Количество по брендам
car_dict = Car.objects.values("brand").annotate(cnt=Count("id"))
print([f"Количество машин {i['brand']} составляет {i['cnt']}" for i in car_dict])

sort_owners = DriverLicence.objects.order_by("recieved_date").all()
print([f"Владелец {i.id} получил лицензию {i.recieved_date}" for i in sort_owners])
```