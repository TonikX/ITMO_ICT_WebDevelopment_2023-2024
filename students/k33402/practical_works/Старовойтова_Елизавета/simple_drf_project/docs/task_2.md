## Задание 2

По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Где это необходимо, добавьте related_name к полям модели
- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

### Решение
Реализация с помощью итерируемых объектов и методов filter(), all()
```python
# Вывести все машины марки "Toyota"
toyota_cars = Car.objects.filter(brand='Toyota')
print("Машины марки Toyota:", toyota_cars)


# Найти всех водителей с именем "Иван"
ivan_drivers = Owner.objects.filter(first_name='Иван')
print("Водители с именем Иван:", ivan_drivers)


# Взять случайного владельца
random_owner = choice(Owner.objects.all())
print("Случайный владелец:", random_owner)
# Получить id владельца
owner_id = random_owner.id
print(f"ID владельца {random_owner}: {owner_id}")
# Получить экземпляр удостоверения по id
driving_licenses = DrivingLicense.objects.filter(owner_id=owner_id)
print(f"Удостоверения владельца {random_owner}: {driving_licenses}")


# Вывести всех владельцев красных машин
red_car_owners = Owner.objects.filter(ownership__car__color='Красный')
print("Владельцы красных машин:", red_car_owners)


# Найти всех владельцев, чей год владения начинается с 2023
owners_2023 = Owner.objects.filter(ownership__start_date__year=2023)
print("Владельцы, чей год владения начинается с 2023:")
for owner in owners_2023:
    for ownership in owner.ownership.filter(start_date__year=2023):
        print(f"{owner.first_name} {owner.last_name} владеет автомобилем, начиная с {ownership.start_date}")

```
