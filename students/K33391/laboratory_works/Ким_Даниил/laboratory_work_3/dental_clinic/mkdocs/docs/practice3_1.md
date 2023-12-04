# Практика 3.1 

### Упражнение 1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов. 

Код:
```python 
from students.K33391.practical_works.Ким_Даниил.simple_django_web_project.django_project_Kim.project_first_app.models import *
from django.utils import timezone
from faker import Faker

fake = Faker()

for _ in range(6):
    car_owner = CarOwner.objects.create(
        first_name=fake.first_name(),
        second_name=fake.last_name(),
        birthday=fake.date_of_birth(minimum_age=18, maximum_age=80),
        passport=fake.unique.random_number(digits=10),
        address=fake.address(),
        nationality=fake.country()
    )

    driver_license = DriverLicense.objects.create(
        owner_id=car_owner,
        license_number=fake.unique.random_number(digits=8),
        license_type=fake.random_element(elements=('A', 'B', 'C')),
        issue_date=fake.date_of_birth(minimum_age=18)
    )

    for _ in range(3):
        car = Car.objects.create(
            state_number=fake.unique.random_number(digits=6),
            brand=fake.random_element(elements=('Toyota', 'BMW', 'Exceed')),
            model=fake.word(),
            color=fake.color_name()
        )

        CarOwn.objects.create(
            car_owner=car_owner,
            car=car,
            start_date=timezone.now(),
            end_date=None
        )
```

Результат:
```python
Car.objects.all()
<QuerySet [<Car: Car object (1)>, <Car: Car object (2)>, 
<Car: Car object (3)>, <Car: Car object (4)>, 
...

CarOwner.objects.all()
<QuerySet [<CarOwner: admin>, <CarOwner: Mikhail>, <CarOwner: >, <CarOwner: 0>, 
<CarOwner: 1>, <CarOwner: 2>, <CarOwner: 3>, <CarOwner: 4>, <CarOwner: 5>]>


CarOwn.objects.all()
<QuerySet [<CarOwn: CarOwn object (1)>, <CarOwn: CarOwn object (2)>, 
<CarOwn: CarOwn object (3)>, <CarOwn: CarOwn object (4)>,
...
```


### Задание 2

Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
```python
Car.objects.filter(model='Toyota')

<QuerySet []>
```



Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
```python
CarOwner.objects.filter(first_name='James')

<QuerySet [<CarOwner: 2>]>
```

Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
```python
from random import choice
rand_user = choice(CarOwner.objects.all())
_id = rand_user.id
driver_license_instance = DriverLicense.objects.filter(owner_id=_id).first()

driver_license_instance
<DriverLicense: DriverLicense object (7)>

driver_license_instance.license_type
'C'
```



Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
```python
CarOwner.objects.filter(cars__color='DarkBlue')

<QuerySet [<CarOwner: 5>]>
```



Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)
```python
CarOwner.objects.filter(carown__start_date__year='2023').distinct()
<QuerySet [<CarOwner: admin>, <CarOwner: Mikhail>, <CarOwner: >,
<CarOwner: 0>, <CarOwner: 1>, <CarOwner: 2>, <CarOwner: 3>, <CarOwner: 4>, <CarOwner: 5>]>
```



### Задание 3
Вывод даты выдачи самого старшего водительского удостоверения

```python
DriverLicense.objects.aggregate(max_issue_date = models.Max('issue_date'))
{'max_issue_date': datetime.date(2023, 11, 6)}
```


Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
```python
CarOwn.objects.aggregate(latest_start_date=models.Max('start_date'))
{'latest_start_date': datetime.date(2023, 12, 3)}
```

Выведите количество машин для каждого водителя
```python
count_by_user = CarOwner.objects.annotate(count=models.Count('car'))
for user_count in count_by_user:
    print(user_count.first_name, user_count.count)
    
Linda 3
Jessica 3
Christopher 3
James 3
Stephen 3
Brian 3
Miranda 3
Mikhail 3
```

Подсчитайте количество машин каждой марки
```python
count_by_brand = Car.objects.values('brand').annotate(count=models.Count('id'))
for brand_counter in count_by_brand:
    print(model_counter['brand'], model_counter['count'])
    
BMW 8
Exceed 8
Kia 1
Mercedes-Benz 1
Toyota 7
```

Отсортируйте всех автовладельцев по дате выдачи удостоверения 
```python
DriverLicence.objects.order_by('issue_date')
<QuerySet [<DriverLicense: DriverLicense object (8)>, <DriverLicense: DriverLicense object (3)>, 
<DriverLicense: DriverLicense object (6)>, <DriverLicense: DriverLicense object (9)>, 
...
```