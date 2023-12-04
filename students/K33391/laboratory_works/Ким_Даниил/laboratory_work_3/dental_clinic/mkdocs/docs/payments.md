# Платежи

## API Для Платежей

### Получение списка платежей

**Запрос:**

```http
GET /api/payments/
```

**Ответ:**
```json
[
    {
        "ID": 1,
        "ID_Patient": 1,
        "Date": "2022-01-05",
        "Price": 100.00
    },
    {
        "ID": 2,
        "ID_Patient": 2,
        "Date": "2022-01-10",
        "Price": 50.00
    }
]
```

### Получение информации о конкретном платеже

**Запрос:**

```http
GET /api/payments/{id}/
```

**Ответ:**

```json
{
    "ID": 1,
    "ID_Patient": 1,
    "Date": "2022-01-05",
    "Price": 100.00
}
```

### Создание нового платежа

**Запрос:**

```http
POST /api/payments/
Content-Type: application/json

{
    "ID_Patient": 1,
    "Date": "2022-02-15",
    "Price": 75.00
}
```

**Ответ:**

```json
{
    "ID": 3,
    "ID_Patient": 1,
    "Date": "2022-02-15",
    "Price": 75.00
}
```

### Обновление информации о платеже

**Запрос:**

```http
PUT /api/payments/{id}/
Content-Type: application/json

{
    "Price": 80.00
}
```

**Ответ:**

```json
{
    "ID": 3,
    "ID_Patient": 1,
    "Date": "2022-02-15",
    "Price": 80.00
}
```

### Удаление платежа

**Запрос:**

```http
DELETE /api/payments/{id}/
```

**Ответ:**

```json
{
    "message": "Платеж успешно удален."
}
```