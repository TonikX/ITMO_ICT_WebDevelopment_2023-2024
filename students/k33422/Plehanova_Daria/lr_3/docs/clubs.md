# Clubs API

## Overview

Этот API предназначен для управления данными альпинистских клубов. Позволяет получать список клубов, создавать новые
клубы, получать детали конкретного клуба, обновлять и удалять информацию о клубах.

### URL

`/api/clubs/`

### Methods

- `GET`: Получение списка клубов или деталей о конкретном клубе.
- `POST`: Создание нового клуба (только для администраторов).
- `PUT`/`PATCH`: Обновление данных клуба (только для администраторов).
- `DELETE`: Удаление клуба (только для администраторов).

### Authentication

- Требуется аутентификация для чтения данных.
- Только администраторы могут создавать, обновлять или удалять данные.

### Filters and Search

- Фильтрация по стране (`country`) и городу (`city`).
- Поиск по названию клуба (`name`), контактному лицу (`contact_person`), электронной почте (`email`) и
  телефону (`phone`).

## Endpoints

### List Clubs

- **URL**: `/api/clubs/`
- **Method**: `GET`
- **Query Parameters**:
    - `country`: Фильтр по стране.
    - `city`: Фильтр по городу.
    - `search`: Строка для поиска.

### Create Club

- **URL**: `/api/clubs/`
- **Method**: `POST`
- **Body Parameters**:
    - `name`: String (Название)
    - `country`: String (Страна)
    - ... (другие поля)

### Retrieve Club

- **URL**: `/api/clubs/{id}/`
- **Method**: `GET`
- **URL Parameters**:
    - `id`: ID клуба

### Update Club

- **URL**: `/api/clubs/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
    - `id`: ID клуба
- **Body Parameters**:
    - ... (поля для обновления)

### Delete Club

- **URL**: `/api/clubs/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
    - `id`: ID клуба

## Examples

### Пример запроса на получение списка клубов

GET /api/clubs/

### Пример ответа

```json
[
  {
    "id": 1,
    "name": "Alpine Adventures",
    "country": "USA",
    ...
  },
  ...
]
```

### Пример запроса на создание клуба

POST /api/clubs/
Content-Type: application/json

```json
{
  "name": "Mountain Explorers",
  "country": "Canada",
  ...
}
```

### Пример ответа

```json
{
  "id": 2,
  "name": "Mountain Explorers",
  "country": "Canada",
  ...
}
```

### Пример запроса на получение деталей о клубе

GET /api/clubs/2/

### Пример ответа

```json
{
  "id": 2,
  "name": "Mountain Explorers",
  "country": "Canada",
  ...
}
```

### Пример запроса на поиск клубов

GET /api/clubs/?search=mountain

### Пример ответа

```json
[
  {
    "id": 2,
    "name": "Mountain Explorers",
    "country": "Canada",
    ...
  },
  ...
]
```
