# Mountains API

## Overview

Этот API предназначен для управления данными гор. Позволяет получать список гор, создавать новые горы, получать детали конкретной горы, обновлять и удалять информацию о горах.

### URL

`/api/mountains`


### Methods

- `GET`: Получение списка гор или деталей о конкретной горе.
- `POST`: Создание новой горы (только для администраторов).
- `PUT`/`PATCH`: Обновление данных горы (только для администраторов).
- `DELETE`: Удаление горы (только для администраторов).

### Authentication

- Требуется аутентификация для чтения данных.
- Только администраторы могут создавать, обновлять или удалять данные.

### Filters and Search

- Фильтрация по стране (`country`) и региону (`region`).
- Поиск по названию горы (`name`).

## Endpoints

### List Mountains

- **URL**: `/api/mountains/`
- **Method**: `GET`
- **Query Parameters**:
  - `country`: Фильтр по стране.
  - `region`: Фильтр по региону.
  - `search`: Строка для поиска.

### Create Mountain

- **URL**: `/api/mountains/`
- **Method**: `POST`
- **Body Parameters**:
  - `name`: String (Название)
  - `height`: Integer (Высота)
  - ... (другие поля)

### Retrieve Mountain

- **URL**: `/api/mountains/{id}/`
- **Method**: `GET`
- **URL Parameters**:
  - `id`: ID горы

### Update Mountain

- **URL**: `/api/mountains/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
  - `id`: ID горы
- **Body Parameters**:
  - ... (поля для обновления)

### Delete Mountain

- **URL**: `/api/mountains/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id`: ID горы

## Examples

### Пример запроса на получение списка гор

GET /api/mountains/

### Пример ответа

```json
[
  {
    "id": 1,
    "name": "Everest",
    "height": 8848,
    ...
  },
  ...
]


### Пример запроса на создание горы

POST /api/mountains/
Content-Type: application/json

```json
{
  "name": "K2",
  "height": 8611,
  ...
}
```

### Пример ответа

```json
{
  "id": 2,
  "name": "K2",
  "height": 8611,
  ...
}
```
