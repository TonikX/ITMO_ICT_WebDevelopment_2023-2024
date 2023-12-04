# Alpinists API

## Overview

Этот API предназначен для управления данными альпинистов. Позволяет получать список альпинистов, создавать новых
альпинистов, получать детали конкретного альпиниста, обновлять и удалять информацию об альпинистах.

### URL

`/api/alpinists/`

### Methods

- `GET`: Получение списка альпинистов или деталей об одном альпинисте.
- `POST`: Создание нового альпиниста.
- `PUT`/`PATCH`: Обновление данных альпиниста.
- `DELETE`: Удаление альпиниста.

### Authentication

- Требуется аутентификация для доступа ко всем методам.
- Только владельцы профиля или администраторы могут обновлять или удалять профили.

### Filters and Search

- Фильтрация по уровню (`level`) и клубу (`club`).
- Поиск по электронной почте (`user__email`), имени (`user__first_name`), фамилии (`user__last_name`) и
  адресу (`address`).

## Endpoints

### List Alpinists

- **URL**: `/api/alpinists/`
- **Method**: `GET`
- **Query Parameters**:
    - `level`: Фильтр по уровню альпиниста.
    - `club`: Фильтр по клубу.
    - `search`: Строка для поиска.

### Create Alpinist

- **URL**: `/api/alpinists/`
- **Method**: `POST`
- **Body Parameters**:
    - `first_name`: String (Имя)
    - `last_name`: String (Фамилия)
    - ... (другие поля)

### Retrieve Alpinist

- **URL**: `/api/alpinists/{id}/`
- **Method**: `GET`
- **URL Parameters**:
    - `id`: ID альпиниста

### Update Alpinist

- **URL**: `/api/alpinists/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
    - `id`: ID альпиниста
- **Body Parameters**:
    - ... (поля для обновления)

### Delete Alpinist

- **URL**: `/api/alpinists/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
    - `id`: ID альпиниста

## Examples

### Пример запроса на получение списка альпинистов

## GET `/api/alpinists/`

### Пример ответа

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    ...
  },
  ...
]
```

## POST /api/alpinists/
### Content-Type: application/json

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  ...
}
```

### Пример ответа

```json
{
  "id": 2,
  "first_name": "Jane",
  "last_name": "Doe",
  ...
}
```