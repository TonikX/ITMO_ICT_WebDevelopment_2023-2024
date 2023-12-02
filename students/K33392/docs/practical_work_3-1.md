# Практическая работа 3.1

## Задание 1
_Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей._

Для начала создадим 6 владельцев автомобилей. Для создания объекта в базе данных воспользуемся методом `CarOwner.objects.create`. Данные я сохранил в списке `owners_data`
```python
# Create 6 car owners
owners_data = [
  {
    "username": "owner1",
    "password": "password1",
    "first_name": "John",
    "last_name": "Doe",
  },
  {
    "username": "owner2",
    "password": "password2",
    "first_name": "Jane",
    "last_name": "Doe",
  },
  {
    "username": "owner3",
    "password": "password3",
    "first_name": "Alice",
    "last_name": "Smith",
  },
  {
    "username": "owner4",
    "password": "password4",
    "first_name": "Bob",
    "last_name": "Johnson",
  },
  {
    "username": "owner5",
    "password": "password5",
    "first_name": "Eva",
    "last_name": "Brown",
  },
  {
    "username": "owner6",
    "password": "password6",
    "first_name": "Charlie",
    "last_name": "Miller",
  },
]

owners = [CarOwner.objects.create(**data) for data in owners_data]
```

После создания владельцев создадим автомобили и присвоим каждому владельцу свой автомобиль
```python
# Create 6 cars
cars_data = [
  {"number": "ABC123", "model": "Toyota", "color": "Blue"},
  {"number": "XYZ456", "model": "Honda", "color": "Red"},
  {"number": "DEF789", "model": "Ford", "color": "Green"},
  {"number": "GHI123", "model": "Chevrolet", "color": "Black"},
  {"number": "JKL456", "model": "Tesla", "color": "White"},
  {"number": "MNO789", "model": "BMW", "color": "Silver"},
]

for data in cars_data:
  Car.objects.create(**data)

# Assign 1 to 3 cars for each owner
for owner, car in zip(CarOwner.objects.all(), Car.objects.all()):
  Ownership.objects.create(
    owner=owner,
    car=car,
    start_date=timezone.now(),
    end_date=timezone.now() + timedelta(days=365),
  )
```

И еще нам необходимо создать права на вождение автомобиля для каждого владельца
```python
# Create driver's licenses for each owner
licenses_data = [
  {
    "owner": owner,
    "number": f"DL{index + 1}",
    "_type": "A",
    "issue_date": timezone.now(),
  }
  for index, owner in enumerate(owners)
]

for data in licenses_data:
  DriversLicence.objects.create(**data)

```

Чтобы выполнить данный скрипт воспользуемся следующей командой:
```sh
./manage.py shell < 3.1/ex1.py
```

# Задание 2
- Где это необходимо, добавьте related_name к полям модели
- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

Для получения всех автомобилей марки Toyota воспользуемся методом `Car.objects.filter`

```python
toyota_cars = Car.objects.filter(model="Toyota")

for car in toyota_cars:
  print(f"Car Number: {car.number}")
  print(f"Model: {car.model}")
  print(f"Color: {car.color}")
  print("--------------------")
```

Для поиска водителей с именем Alice воспользуемся методом ` CarOwner.objects.filter`
```python
alice_drivers = CarOwner.objects.filter(first_name="Alice")
for driver in alice_drivers:
  print(f"Driver Name: {driver.first_name}")
  print(f"Date of Birth: {driver.date_of_birth}")
  print("--------------------")
```

Для фильтрации прав по владельцу выполним два запроса при помощи методов `CarOwner.objects.get` и `DriversLicence.objects.filter`
```python
driver = CarOwner.objects.get(first_name="Jane")

print(f"Driver Name: {driver.first_name}")
print(f"Date of Birth: {driver.date_of_birth}")
print("--------------------")

driver_licenses = DriversLicence.objects.filter(owner=driver)
for license in driver_licenses:
  print(f"License Number: {license.number}")
  print(f"License Type: {license._type}")
  print(f"Issue Date: {license.issue_date}")
  print("--------------------")
```

Для получения всех красных машин воспользуемся методом `Car.objects.filter`
```python
# Query all car owners with red cars
red_cars = Car.objects.filter(color="Red")
for car in red_cars:
  print(f"Car Number: {car.number}")
  print(f"Model: {car.model}")
  print(f"Color: {car.color}")
  print("--------------------")
```

Для получения всех владельцев, которые владеют автомобилем начиная с 2023 года воспользуемся методом `CarOwner.objects.filter`
```python
target_year = 2023
owners_with_cars_from_year = CarOwner.objects.filter(
    ownership__start_date__year=target_year
).distinct()

for owner in owners_with_cars_from_year:
  print(f"Owner Name: {owner.first_name}")
  print(f"Date of Birth: {owner.date_of_birth}")
  print("--------------------")
```

# Задание 3
- Вывод даты выдачи самого старшего водительского удостоверения
- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
- Выведите количество машин для каждого водителя
- Подсчитайте количество машин каждой марки
- Отсортируйте всех автовладельцев по дате выдачи удостоверения 

Вывод даты выдачи самого старшего водительского удостоверения
```python
# query the oldest drivers license
oldest_license = DriversLicence.objects.order_by("issue_date").first()
print(f"License Number: {oldest_license.number}")
```

Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
```python
# query the oldest ownership date
oldest_ownership = Ownership.objects.order_by("start_date").first()
print(f"Oldest ownership: {oldest_ownership.start_date}")
```

Выведите количество машин для каждого водителя
```python
# query the number of cars for each driver using Count annotate
owners_with_car_count = CarOwner.objects.annotate(car_count=Count("ownership"))
for owner in owners_with_car_count:
    print(f"Owner Name: {owner.first_name}")
    print(f"Number of cars: {owner.car_count}")
    print("--------------------")
```

Подсчитайте количество машин каждой марки
```python
# query number of cars by model
cars_by_model = Car.objects.values("model").annotate(car_count=Count("ownership"))
for car in cars_by_model:
    print(f"Car Model: {car['model']}")
    print(f"Number of cars: {car['car_count']}")
    print("--------------------")
```

Отсортируйте всех автовладельцев по дате выдачи удостоверения 
```python
# query all car owners sorted by drivers license issue date
owners_by_license_issue_date = CarOwner.objects.order_by("driverslicence__issue_date")
for owner in owners_by_license_issue_date:
    print(f"Owner Name: {owner.first_name}")
    print(f"License Issue Date: {owner.driverslicence.get().issue_date}")
    print("--------------------")
```