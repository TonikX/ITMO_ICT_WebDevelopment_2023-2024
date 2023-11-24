# Задание 3

???+ question "Задание"

    - Вывод даты выдачи самого старшего водительского удостоверения
    - Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
    - Выведите количество машин для каждого водителя
    - Подсчитайте количество машин каждой марки
    - Отсортируйте всех автовладельцев по дате выдачи удостоверения

## Выполнение

### Query 1

Найдем лицензию с наименьшей датой

```bash
>>> DriverLicense.objects.aggregate(oldest_one=Min("creation_date"))["oldest_one"]
datetime.date(2023, 11, 14)
```

### Query 2

Найдем инстанс владения с самой поздней датой окончания владения

```bash
>>> Ownership.objects.aggregate(latest_one=Max("end"))["latest_one"]
datetime.date(2025, 5, 16)
```

### Query 3

Найдем кол-во машин для каждого из водителей

```bash
>>> Driver.objects.annotate(num_cars=Count('cars')).values('first_name', 'num_cars')
<QuerySet [{'first_name': 'Driver_first_name_0', 'num_cars': 1}, {'first_name': 'Driver_first_name_1', 'num_cars': 1}, {'first_name': 'Driver_first_name_2', 'num_cars': 1}, {'first_name': 'Driver_first_name_3', 'num_cars': 1}, {'first_name': 'Driver_first_name_4', 'num_cars': 1}, {'first_name': 'Driver_first_name_5', 'num_cars': 0}, {'first_name': 'Driver_first_name_6', 'num_cars': 0}, {'first_name': '', 'num_cars': 0}]>
```

### Query 4

Найдем кол-во машин каждой марки

```bash
>>> Car.objects.values('brand').annotate(cars_num=Count('id')).order_by("brand")
<QuerySet [{'brand': 'Brand_0', 'cars_num': 1}, {'brand': 'Brand_1', 'cars_num': 1}, {'brand': 'Brand_2', 'cars_num': 1}, {'brand': 'Brand_3', 'cars_num': 1}, {'brand': 'Brand_4', 'cars_num': 1}]>
```

### Query 5

```bash
>>> DriverLicense.objects.order_by('creation_date').values('driver')
<QuerySet [{'driver': 51}, {'driver': 52}, {'driver': 53}, {'driver': 54}, {'driver': 55}, {'driver': 56}, {'driver': 57}]>
```
