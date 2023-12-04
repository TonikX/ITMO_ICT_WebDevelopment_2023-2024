# Пациенты

## API Для Пациентов

### Получение списка пациентов

**Запрос:**

```http
GET /api/patients/
```

**Ответ:**
```json
[
    {
        "ID": 1,
        "Name": "Пациент",
        "Surname": "Примеров",
        "Birth_Date": "1990-01-01",
        "Sex": "Мужской",
        "Contacts": "Телефон: 123-456-7890, Эл. почта: patient@example.com"
    },
    {
        "ID": 2,
        "Name": "Пациент",
        "Surname": "Исследований",
        "Birth_Date": "1985-05-05",
        "Sex": "Женский",
        "Contacts": "Телефон: 987-654-3210, Эл. почта: patient2@example.com"
    }
]

```

### Получение информации о конкретном пациенте

**Запрос:**

```http
GET /api/patients/{id}/
```

**Ответ:**

```json
{
    "ID": 1,
    "Name": "Пациент",
    "Surname": "Примеров",
    "Birth_Date": "1990-01-01",
    "Sex": "Мужской",
    "Contacts": "Телефон: 123-456-7890, Эл. почта: patient@example.com"
}

```

### Создание нового пациента

**Запрос:**

```http
POST /api/patients/
Content-Type: application/json

{
    "Name": "Новый",
    "Surname": "Пациент",
    "Birth_Date": "2000-12-31",
    "Sex": "Мужской",
    "Contacts": "Телефон: 111-222-3333, Эл. почта: newpatient@example.com"
}

```

**Ответ:**

```json
{
    "ID": 3,
    "Name": "Новый",
    "Surname": "Пациент",
    "Birth_Date": "2000-12-31",
    "Sex": "Мужской",
    "Contacts": "Телефон: 111-222-3333, Эл. почта: newpatient@example.com"
}

```

### Обновление информации о пациенте

**Запрос:**

```http
PUT /api/patients/{id}/
Content-Type: application/json

{
    "Name": "Обновленный",
    "Birth_Date": "1995-06-15"
}

```

**Ответ:**

```json
{
    "ID": 3,
    "Name": "Обновленный",
    "Surname": "Пациент",
    "Birth_Date": "1995-06-15",
    "Sex": "Мужской",
    "Contacts": "Телефон: 111-222-3333, Эл. почта: newpatient@example.com"
}

```

### Удаление пациента

**Запрос:**

```http
DELETE /api/patients/{id}/

```

**Ответ:**

```json
{
    "message": "Пациент успешно удален."
}

```