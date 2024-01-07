# CRUD

Endpoints доступны всем **авторизованным** пользователям при помощи JWT token 
(заголовок _Authorization: JWT {your token}_)
## Chicken
- `POST /chickens` - создание
- `GET /chickens` - получение всех объектов
- `GET /chickens/{id}` - получение конкретного объекта
- `PUT /chickens/{id}` - изменение конкретного объекта
- `DELETE /chickens/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "id": 1,
    "weight": 1,
    "birth_date": "2023-11-28",
    "monthly_egg_rate": 5,
    "breed": 1,
    "cage": 1
}
```

## Staff 
- `POST /staff` - создание
- `GET /staff` - получение всех объектов
- `GET /staff/{id}` - получение конкретного объекта
- `PUT /staff/{id}` - изменение конкретного объекта
- `DELETE /staff/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "username": "janill",
    "role": "Worker",
    "passport": "1234",
    "salary": 1,
    "employment_contract_id": 1,
    "dismissal_agreement_id": 1
}
```

## Cage
- `POST /cages` - создание
- `GET /cages` - получение всех объектов
- `GET /cages/{id}` - получение конкретного объекта
- `PUT /cages/{id}` - изменение конкретного объекта
- `DELETE /cages/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "id": 1,
    "facility": {
        "id": 1,
        "name": "Main",
        "_longitude": 89.0,
        "_latitude": 89.0
    },
    "responsible": {
        "username": "janill",
        "role": "Worker",
        "passport": "1234",
        "salary": 1,
        "employment_contract_id": 1,
        "dismissal_agreement_id": 1
    },
    "row": 1,
    "column": 1
}
```

## Facility
- `POST /facilities` - создание
- `GET /facilities` - получение всех объектов
- `GET /facilities/{id}` - получение конкретного объекта
- `PUT /facilities/{id}` - изменение конкретного объекта
- `DELETE /facilities/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "id": 1,
    "name": "Main",
    "_longitude": 89.0,
    "_latitude": 89.0
}
```
## Diet
- `POST /diets` - создание
- `GET /diets` - получение всех объектов
- `GET /diets/{id}` - получение конкретного объекта
- `PUT /diets/{id}` - изменение конкретного объекта
- `DELETE /diets/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "id": 1,
    "name": "Default diet",
    "content": "Zerno"
}
```

## Breed
- `POST /breeds` - создание
- `GET /breeds` - получение всех объектов
- `GET /breeds/{id}` - получение конкретного объекта
- `PUT /breeds/{id}` - изменение конкретного объекта
- `DELETE /breeds/{id}` - удаление конкретного объекта

Модель данных объекта:
```json
{
    "id": 1,
    "name": "Default",
    "average_monthly_egg_rate": 5,
    "average_weight": 5,
    "recommended_diet": 2
}
```