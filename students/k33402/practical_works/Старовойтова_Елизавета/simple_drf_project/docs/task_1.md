## Задание 1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей.
Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов. 

### Решение
Реализация через менеджер objects.
```python
# Создание автовладельцев
owners_data = [
    {"last_name": "Иванов", "first_name": "Иван", "birth_date": "1990-01-01"},
    {"last_name": "Федоров", "first_name": "Федор", "birth_date": "1990-01-04"},
    {"last_name": "Старовойтов", "first_name": "Анатолий", "birth_date": "1990-05-01"},
    {"last_name": "Сычев", "first_name": "Михаил", "birth_date": "1995-01-01"},
    {"last_name": "Ярошенко", "first_name": "Мария", "birth_date": "2000-01-01"},
    {"last_name": "Исаченко", "first_name": "Дарья", "birth_date": "2004-01-10"},
]

for data in owners_data:
    owner = Owner.objects.create(**data)

# Создание автомобилей
cars_data = [
    {"registration_number": "А111АА77", "brand": "Toyota", "model": "Camry", "color": "Синий"},
    {"registration_number": "А111YU66", "brand": "Toyota", "model": "Corola", "color": "Красный"},
    {"registration_number": "А222АА77", "brand": "Kia", "model": "Rio", "color": "Белый"},
    {"registration_number": "А411АА77", "brand": "BMW", "model": "X5", "color": "Черный"},
    {"registration_number": "А111АА78", "brand": "Lada", "model": "Granta", "color": "Серый"},
]

for data in cars_data:
    car = Car.objects.create(**data)

# Привязка владельцев к автомобилям и создание владений
ownerships_data = [
    {"owner": Owner.objects.get(last_name="Иванов"), "car": Car.objects.get(registration_number="А111АА77"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Иванов"), "car": Car.objects.get(registration_number="А111АА78"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Федоров"), "car": Car.objects.get(registration_number="А111YU66"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Старовойтов"), "car": Car.objects.get(registration_number="А222АА77"), "start_date": timezone.now()},
    {"owner": Owner.objects.get(last_name="Сычев"), "car": Car.objects.get(registration_number="А411АА77"), "start_date": timezone.now()},

]

for data in ownerships_data:
    ownership = Ownership.objects.create(**data)

# Создание водительских удостоверений
licenses_data = [
    {"owner": Owner.objects.get(last_name="Иванов"), "license_number": "1234567890", "license_type": "A", "issue_date": "2022-01-01"},
    {"owner": Owner.objects.get(last_name="Федоров"), "license_number": "1234567891", "license_type": "A", "issue_date": "2023-01-01"},
    {"owner": Owner.objects.get(last_name="Старовойтов"), "license_number": "1234567892", "license_type": "A", "issue_date": "2021-04-02"},
    {"owner": Owner.objects.get(last_name="Сычев"), "license_number": "1234567893", "license_type": "A", "issue_date": "2020-08-01"},
    {"owner": Owner.objects.get(last_name="Ярошенко"), "license_number": "1234567894", "license_type": "A", "issue_date": "2022-03-08"},
    {"owner": Owner.objects.get(last_name="Исаченко"), "license_number": "1234567895", "license_type": "A", "issue_date": "2022-01-01"},
]

for data in licenses_data:
    license = DrivingLicense.objects.create(**data)
```

