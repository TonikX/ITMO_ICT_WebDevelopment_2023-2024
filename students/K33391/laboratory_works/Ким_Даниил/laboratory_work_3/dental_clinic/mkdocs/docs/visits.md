# Визиты

## API Для Визитов

### Получение списка визитов

**Запрос:**

```http
GET /api/visits/
```

**Ответ:**
```json
[
    {
        "ID": 1,
        "ID_Patient": 1,
        "ID_Doctor": 1,
        "Date": "2022-01-01T10:00:00Z",
        "Diagnoz": "Общий диагноз",
        "Appointment": "Назначение визита",
        "ID_Service": 1
    },
    {
        "ID": 2,
        "ID_Patient": 2,
        "ID_Doctor": 2,
        "Date": "2022-01-02T11:00:00Z",
        "Diagnoz": "Дополнительный диагноз",
        "Appointment": "Дополнительное назначение",
        "ID_Service": 2
    }
]

```

### Получение информации о конкретном визите

**Запрос:**

```http
GET /api/visits/{id}/
```

**Ответ:**

```json
{
    "ID": 1,
    "ID_Patient": 1,
    "ID_Doctor": 1,
    "Date": "2022-01-01T10:00:00Z",
    "Diagnoz": "Общий диагноз",
    "Appointment": "Назначение визита",
    "ID_Service": 1
}
```

### Создание нового визита

**Запрос:**

```http
POST /api/visits/
Content-Type: application/json

{
    "ID_Patient": 1,
    "ID_Doctor": 1,
    "Date": "2022-02-01T14:30:00Z",
    "Diagnoz": "Новый диагноз",
    "Appointment": "Новое назначение",
    "ID_Service": 1
}
```

**Ответ:**

```json
{
    "ID": 3,
    "ID_Patient": 1,
    "ID_Doctor": 1,
    "Date": "2022-02-01T14:30:00Z",
    "Diagnoz": "Новый диагноз",
    "Appointment": "Новое назначение",
    "ID_Service": 1
}
```

### Обновление информации о визите

**Запрос:**

```http
PUT /api/visits/{id}/
Content-Type: application/json

{
    "Diagnoz": "Обновленный диагноз",
    "Appointment": "Обновленное назначение"
}
```

**Ответ:**

```json
{
    "ID": 3,
    "ID_Patient": 1,
    "ID_Doctor": 1,
    "Date": "2022-02-01T14:30:00Z",
    "Diagnoz": "Обновленный диагноз",
    "Appointment": "Обновленное назначение",
    "ID_Service": 1
}
```

### Удаление визита

**Запрос:**

```http
DELETE /api/visits/{id}/
```

**Ответ:**

```json
{
    "message": "Визит успешно удален."
}
```