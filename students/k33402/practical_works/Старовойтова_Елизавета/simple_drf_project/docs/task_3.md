## Задание 3

Необходимо реализовать следующие запросы c применением описанных методов:
- Вывод даты выдачи самого старшего водительского удостоверения
- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
- Выведите количество машин для каждого водителя
- Подсчитайте количество машин каждой марки
- Отсортируйте всех автовладельцев по дате выдачи удостоверения 

(Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct())

### Решение
Реализация с помощью агрегации и аннотации запросов.

```python
# Вывод даты выдачи самого старшего водительского удостоверения
oldest_license_issue_date = DrivingLicense.objects.aggregate(Min('issue_date'))
print("Самая старшая дата выдачи водительского удостоверения:", oldest_license_issue_date['issue_date__min'])

# Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
latest_ownership_date = Ownership.objects.filter(car__model__isnull=False).aggregate(Max('start_date'))
print("Самая поздняя дата владения машиной:", latest_ownership_date['start_date__max'])

# Выведите количество машин для каждого водителя
cars_per_owner = Ownership.objects.values('owner').annotate(num_cars=Count('car')).order_by('owner')
for record in cars_per_owner:
    owner = Owner.objects.get(pk=record['owner'])
    print(f"{owner.first_name} {owner.last_name}: {record['num_cars']} машин")

# Подсчитайте количество машин каждой марки
cars_per_brand = Car.objects.values('brand').annotate(num_cars=Count('id')).order_by('num_cars')
for record in cars_per_brand:
    print(f"Марка: {record['brand']}, Количество машин: {record['num_cars']}")

# Отсортируйте всех автовладельцев по дате выдачи удостоверения
owners_sorted_by_license_date = Owner.objects.annotate(license_date=F('driving_license__issue_date')).order_by('license_date')
for owner in owners_sorted_by_license_date:
    license_date = owner.license_date
    print(f"{owner.first_name} {owner.last_name}, Дата выдачи удостоверения: {license_date}")

```
