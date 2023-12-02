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