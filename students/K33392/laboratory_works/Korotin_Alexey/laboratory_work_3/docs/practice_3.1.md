# Практика 3.1
# Задача 1
## Модель
Модель была взята из предыдущей практической работы

```python
from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"Car(license_plate={self.license_plate}, brand={self.brand}, model={self.model}, color={self.color})"


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateTimeField(null=True)
    passport = models.CharField(max_length=10, null=True)
    home_Address = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=100, null=True)
    owner = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return f"CarOwner(first_name={self.first_name}, last_name={self.last_name}, birth_date={self.birth_date}, " \
               f"passport={self.passport}, home_Address={self.home_Address}, nationality={self.nationality})"


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(CarOwner, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

    def __str__(self):
        return f"Ownership(car={self.car}, owner={self.owner}, date_start={self.date_start}, date_end={self.date_end})"


class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

    def __str__(self):
        return f"DriverLicense(owner={self.owner}, number={self.number}, license_type={self.license_type}, issue_date={self.issue_date})"

```
## Запросы

### Автовладельцы

#### Скрипт
```python
owner1 = CarOwner.objects.create(first_name="1", last_name="1", birth_date=datetime.datetime.now(), passport="1", home_Address="1", nationality="1")
owner2 = CarOwner.objects.create(first_name="2", last_name="2", birth_date=datetime.datetime.now(), passport="2", home_Address="2", nationality="2")
owner3 = CarOwner.objects.create(first_name="3", last_name="3", birth_date=datetime.datetime.now(), passport="3", home_Address="3", nationality="3")
owner4 = CarOwner.objects.create(first_name="4", last_name="4", birth_date=datetime.datetime.now(), passport="4", home_Address="4", nationality="4")
owner5 = CarOwner.objects.create(first_name="5", last_name="5", birth_date=datetime.datetime.now(), passport="5", home_Address="5", nationality="5")
owner6 = CarOwner.objects.create(first_name="6", last_name="6", birth_date=datetime.datetime.now(), passport="6", home_Address="6", nationality="6")
```
#### Вывод
```
>>> CarOwner.objects.all()
<QuerySet [<CarOwner: CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1)>, <CarOwner: CarOwner(first_name=2, last_
name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2, home_Address=2, nationality=2)>, <CarOwner: CarOwner(first_name=3, last_name=3, birth_date=2023-11-24 20:58:29.701066+00:0
0, passport=3, home_Address=3, nationality=3)>, <CarOwner: CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4)>, <C
arOwner: CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00:00, passport=5, home_Address=5, nationality=5)>, <CarOwner: CarOwner(first_name=6, last_name=6, birth
_date=2023-11-24 20:58:29.734116+00:00, passport=6, home_Address=6, nationality=6)>]>

```

### Удостоверения

#### Скрипт

```python
DriverLicense.objects.create(owner=owner1, number="1", license_type="B", issue_date=datetime.datetime.now())
DriverLicense.objects.create(owner=owner2, number="2", license_type="B", issue_date=datetime.datetime.now())
DriverLicense.objects.create(owner=owner3, number="3", license_type="B", issue_date=datetime.datetime.now())
DriverLicense.objects.create(owner=owner4, number="4", license_type="B", issue_date=datetime.datetime.now())
DriverLicense.objects.create(owner=owner5, number="5", license_type="B", issue_date=datetime.datetime.now())
DriverLicense.objects.create(owner=owner6, number="6", license_type="B", issue_date=datetime.datetime.now())
```

#### Вывод

```
>>> DriverLicense.objects.all()
<QuerySet [<DriverLicense: DriverLicense(owner=CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1), number=1, licen
se_type=B, issue_date=2023-11-24 21:01:49.146607+00:00)>, <DriverLicense: DriverLicense(owner=CarOwner(first_name=2, last_name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2,
home_Address=2, nationality=2), number=2, license_type=B, issue_date=2023-11-24 21:01:49.193053+00:00)>, <DriverLicense: DriverLicense(owner=CarOwner(first_name=3, last_name=3, birth_date
=2023-11-24 20:58:29.701066+00:00, passport=3, home_Address=3, nationality=3), number=3, license_type=B, issue_date=2023-11-24 21:01:49.208716+00:00)>, <DriverLicense: DriverLicense(owner
=CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4), number=4, license_type=B, issue_date=2023-11-24 21:01:49.2243
37+00:00)>, <DriverLicense: DriverLicense(owner=CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00:00, passport=5, home_Address=5, nationality=5), number=5, lice
nse_type=B, issue_date=2023-11-24 21:01:49.224337+00:00)>, <DriverLicense: DriverLicense(owner=CarOwner(first_name=6, last_name=6, birth_date=2023-11-24 20:58:29.734116+00:00, passport=6,
 home_Address=6, nationality=6), number=6, license_type=B, issue_date=2023-11-24 21:01:52.179825+00:00)>]>
```

### Автомобили

#### Скрипт
```python
car1 = Car.objects.create(license_plate="1", brand="Toyota", model="Camry", color="black")
car2 = Car.objects.create(license_plate="2", brand="Toyota", model="Corolla", color="black")
car3 = Car.objects.create(license_plate="3", brand="Lada", model="Vesta", color="black")
car4 = Car.objects.create(license_plate="4", brand="Mitsubishi", model="Lancer", color="black")
car5 = Car.objects.create(license_plate="5", brand="Honda", model="Civic", color="black")
```
#### Вывод
```
>>> Car.objects.all()
<QuerySet [<Car: Car(license_plate=1, brand=Toyota, model=Camry, color=black)>, <Car: Car(license_plate=2, brand=Toyota, model=Corolla, color=black)>, <Car: Car(license_plate=3, brand=Lad
a, model=Vesta, color=black)>, <Car: Car(license_plate=4, brand=Mitsubishi, model=Lancer, color=black)>, <Car: Car(license_plate=5, brand=Honda, model=Civic, color=black)>]>
```

### Владение

#### Скрипт
```python
ownership1 = Ownership.objects.create(owner=owner1, car=car1, date_start=datetime.datetime.now())
ownership2 = Ownership.objects.create(owner=owner2, car=car2, date_start=datetime.datetime.now())
ownership3 = Ownership.objects.create(owner=owner3, car=car3, date_start=datetime.datetime.now())
ownership4 = Ownership.objects.create(owner=owner4, car=car4, date_start=datetime.datetime.now())
ownership5 = Ownership.objects.create(owner=owner5, car=car5, date_start=datetime.datetime.now())
ownership6 = Ownership.objects.create(owner=owner6, car=car5, date_start=datetime.datetime.now())
```

### Вывод

```
>>> Ownership.objects.all()
<QuerySet [<Ownership: Ownership(car=Car(license_plate=1, brand=Toyota, model=Camry, color=black), owner=CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, p
assport=1, home_Address=1, nationality=1), date_start=2023-11-24 21:19:20.875803+00:00, date_end=None)>, <Ownership: Ownership(car=Car(license_plate=2, brand=Toyota, model=Corolla, color=
black), owner=CarOwner(first_name=2, last_name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2, home_Address=2, nationality=2), date_start=2023-11-24 21:19:20.960060+00:00, dat
e_end=None)>, <Ownership: Ownership(car=Car(license_plate=3, brand=Lada, model=Vesta, color=black), owner=CarOwner(first_name=3, last_name=3, birth_date=2023-11-24 20:58:29.701066+00:00,
passport=3, home_Address=3, nationality=3), date_start=2023-11-24 21:19:20.960060+00:00, date_end=None)>, <Ownership: Ownership(car=Car(license_plate=4, brand=Mitsubishi, model=Lancer, co
lor=black), owner=CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4), date_start=2023-11-24 21:19:20.975719+00:00,
 date_end=None)>, <Ownership: Ownership(car=Car(license_plate=5, brand=Honda, model=Civic, color=black), owner=CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00
:00, passport=5, home_Address=5, nationality=5), date_start=2023-11-24 21:19:20.975719+00:00, date_end=None)>, <Ownership: Ownership(car=Car(license_plate=5, brand=Honda, model=Civic, col
or=black), owner=CarOwner(first_name=6, last_name=6, birth_date=2023-11-24 20:58:29.734116+00:00, passport=6, home_Address=6, nationality=6), date_start=2023-11-24 21:19:25.046156+00:00,
date_end=None)>]>

```

# Задача 2
## Выведете все машины марки “Toyota”
### Скрипт
```python
Car.objects.filter(brand="Toyota")
```
### Вывод
```
<QuerySet [<Car: Car(license_plate=1, brand=Toyota, model=Camry, color=black)>, <Car: Car(license_plate=2, brand=Toyota, model=Corolla, color=black)>]>
```


## Найти всех водителей с именем “1”
### Скрипт
```python
CarOwner.objects.filter(first_name="1")
```
### Вывод
```
<QuerySet [<CarOwner: CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1)>]>
```


## Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели
### Скрипт
```python
desired_owner_id = CarOwner.objects.get(first_name="1").id
DriverLicense.objects.get(owner__id=desired_owner_id)
```
### Вывод
```
<DriverLicense: DriverLicense(owner=CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1), number=1, license_type=B,
issue_date=2023-11-24 21:01:49.146607+00:00)>
```

## Вывести всех владельцев черных машин
### Скрипт
```python
CarOwner.objects.filter(ownership__car__color="black")
```
### Вывод
```
<QuerySet [<CarOwner: CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1)>, <CarOwner: CarOwner(first_name=2, last_
name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2, home_Address=2, nationality=2)>, <CarOwner: CarOwner(first_name=3, last_name=3, birth_date=2023-11-24 20:58:29.701066+00:0
0, passport=3, home_Address=3, nationality=3)>, <CarOwner: CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4)>, <C
arOwner: CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00:00, passport=5, home_Address=5, nationality=5)>, <CarOwner: CarOwner(first_name=6, last_name=6, birth
_date=2023-11-24 20:58:29.734116+00:00, passport=6, home_Address=6, nationality=6)>]>
```


## Найти всех владельцев, чей год владения машиной начинается с 2023
### Скрипт
```python
CarOwner.objects.filter(driverlicense__issue_date__year=2023)
```
### Вывод
```
<QuerySet [<CarOwner: CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1)>, <CarOwner: CarOwner(first_name=2, last_
name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2, home_Address=2, nationality=2)>, <CarOwner: CarOwner(first_name=3, last_name=3, birth_date=2023-11-24 20:58:29.701066+00:0
0, passport=3, home_Address=3, nationality=3)>, <CarOwner: CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4)>, <C
arOwner: CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00:00, passport=5, home_Address=5, nationality=5)>, <CarOwner: CarOwner(first_name=6, last_name=6, birth
_date=2023-11-24 20:58:29.734116+00:00, passport=6, home_Address=6, nationality=6)>]>
```

# Задача 3

## Вывод даты выдачи самого старшего водительского удостоверения
### Скрипт
```python
from django.db.models import Min

DriverLicense.objects.aggregate(earliest_date=Min("issue_date"))
```
### Вывод
```
{'earliest_date': datetime.datetime(2023, 11, 24, 21, 1, 49, 146607, tzinfo=datetime.timezone.utc)}
```


## Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
### Скрипт
```python
from django.db.models import Max

Ownership.objects.aggregate(latest_ownership=Max("date_end"))
```
### Вывод
```
{'latest_ownership': None}
```

## Выведите количество машин для каждого водителя
### Скрипт
```python
from django.db.models import Count

annotated = CarOwner.objects.annotate(Count("owner"))
for owner in annotated:
    print(owner.first_name, owner.owner__count)
```
### Вывод
```
1 1
2 1
3 1
4 1
5 1
6 1

```

## Подсчитайте количество машин каждой марки
### Скрипт
```python
from django.db.models import Count

Car.objects.values("brand").annotate(Count("id"))
```
### Вывод
```
<QuerySet [{'brand': 'Honda', 'id__count': 1}, {'brand': 'Lada', 'id__count': 1}, {'brand': 'Mitsubishi', 'id__count': 1}, {'brand': 'Toyota', 'id__count': 2}]>
```

## Отсортируйте всех автовладельцев по дате выдачи удостоверения 
### Скрипт
```python
CarOwner.objects.order_by("driverlicense__issue_date")
```
### Вывод
```
<QuerySet [<CarOwner: CarOwner(first_name=1, last_name=1, birth_date=2023-11-24 20:56:30.905200+00:00, passport=1, home_Address=1, nationality=1)>, <CarOwner: CarOwner(first_name=2, last_
name=2, birth_date=2023-11-24 20:58:29.691257+00:00, passport=2, home_Address=2, nationality=2)>, <CarOwner: CarOwner(first_name=3, last_name=3, birth_date=2023-11-24 20:58:29.701066+00:0
0, passport=3, home_Address=3, nationality=3)>, <CarOwner: CarOwner(first_name=4, last_name=4, birth_date=2023-11-24 20:58:29.717073+00:00, passport=4, home_Address=4, nationality=4)>, <C
arOwner: CarOwner(first_name=5, last_name=5, birth_date=2023-11-24 20:58:29.725866+00:00, passport=5, home_Address=5, nationality=5)>, <CarOwner: CarOwner(first_name=6, last_name=6, birth
_date=2023-11-24 20:58:29.734116+00:00, passport=6, home_Address=6, nationality=6)>]>
```

