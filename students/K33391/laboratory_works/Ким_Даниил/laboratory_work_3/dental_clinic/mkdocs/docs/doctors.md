# Доктора

## API Для Докторов

### Получение списка докторов

**Запрос:**

```http
GET /api/doctors/
```

**Ответ:**

```json
[
    {
        "ID": 1,
        "Name": "Доктор",
        "Surname": "Примеров",
        "Specialization": "Терапевт",
        "Contacts": "Телефон: 123-456-7890, Эл. почта: doctor@example.com"
    },
    {
        "ID": 2,
        "Name": "Доктор",
        "Surname": "Исследований",
        "Specialization": "Хирург",
        "Contacts": "Телефон: 987-654-3210, Эл. почта: surgeon@example.com"
    }
]
```

### Получение информации о конкретном докторе

**Запрос:**

```http
GET /api/doctors/{id}/
```

**Ответ:**
```json
{
    "ID": 1,
    "Name": "Доктор",
    "Surname": "Примеров",
    "Specialization": "Терапевт",
    "Contacts": "Телефон: 123-456-7890, Эл. почта: doctor@example.com"
}
```

### Создание нового доктора

**Запрос:**

```http
POST /api/doctors/
Content-Type: application/json

{
    "Name": "Новый",
    "Surname": "Доктор",
    "Specialization": "Новая Специализация",
    "Contacts": "Телефон: 111-222-3333, Эл. почта: newdoctor@example.com"
}

```

**Ответ:**
```json
{
    "ID": 3,
    "Name": "Новый",
    "Surname": "Доктор",
    "Specialization": "Новая Специализация",
    "Contacts": "Телефон: 111-222-3333, Эл. почта: newdoctor@example.com"
}

```

### Обновление информации о докторе

**Запрос:**

```http
PUT /api/doctors/{id}/
Content-Type: application/json

{
    "Name": "Обновленный",
    "Specialization": "Новая Специализация"
}

```

**Ответ:**

```json
{
  "ID": 3,
  "Name": "Обновленный",
  "Surname": "Доктор",
  "Specialization": "Новая Специализация",
  "Contacts": "Телефон: 111-222-3333, Эл. почта: newdoctor@example.com"
}
```

### Удаление доктора

**Запрос:**

```http
DELETE /api/doctors/{id}/

```

**Ответ:**

```json
{
    "message": "Доктор успешно удален."
}

```