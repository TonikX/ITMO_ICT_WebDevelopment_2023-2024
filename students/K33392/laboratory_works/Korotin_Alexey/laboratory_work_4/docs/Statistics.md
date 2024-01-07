# Statistics
Были реализованы следующие пункты статистики 
(был реализован **RBAC**: статистика доступна только **Директору** - пользователю с соответствущей ролью)

## Какова для каждой породы разница между показателями породы и средними показателями по птицефабрике?

`GET /breeds/statistics`
### Формат ответа
```json
{
    "breed_name1": {
        "weight": 4.0,
        "egg_rate": 0.0
    },
    "breed_name2": {
        "weight": 0.0,
        "egg_rate": -4.0
    }
}
```

## Сколько кур каждой породы в каждом цехе?

`GET /facilities/statistics/chicken_by_breed`

### Формат ответа
```json
{
    "facility_name": [
        {
            "breed_name1": 1
        },
        {
            "breed_name2": 2
        }
    ]
}
```

## Среднее количество яиц, которое получает каждый работник от обслуживаемых им кур?

`GET /staff/statistics`

### Формат ответа
```json
[
    {
        "id": 1,
        "username": "janill",
        "average_eggs": 5.0
    }
]
```

## Отчет о производительности птицефабрики

`GET /report`

### Формат ответа
```json
{
    "total_eggs": 15,
    "total_chickens": 3,
    "average_productivity_per_breed": [
        {
            "name": "breed_1",
            "average_productivity": 5.0
        },
        {
            "name": "breed_2",
            "average_productivity": 5.0
        }
    ]
}
```