# Routes API

## Overview

Этот API предназначен для управления данными маршрутов восхождений. Позволяет получать список маршрутов, создавать новые маршруты, получать детали конкретного маршрута, обновлять и удалять информацию о маршрутах.

### URL

`/api/routes`


### Methods

- `GET`: Получение списка маршрутов или деталей о конкретном маршруте.
- `POST`: Создание нового маршрута (только для администраторов).
- `PUT`/`PATCH`: Обновление данных маршрута (только для администраторов).
- `DELETE`: Удаление маршрута (только для администраторов).

### Authentication

- Требуется аутентификация для чтения данных.
- Только администраторы могут создавать, обновлять или удалять данные.

### Filters and Search

- Фильтрация по сложности (`difficulty`).
- Поиск по названию маршрута (`name`) и названию горы (`mountain__name`).

## Endpoints

### List Routes

- **URL**: `/api/routes/`
- **Method**: `GET`
- **Query Parameters**:
  - `difficulty`: Фильтр по сложности маршрута.
  - `search`: Строка для поиска.

### Create Route

- **URL**: `/api/routes/`
- **Method**: `POST`
- **Body Parameters**:
  - `name`: String (Название)
  - `difficulty`: String (Сложность)
  - ... (другие поля)

### Retrieve Route

- **URL**: `/api/routes/{id}/`
- **Method**: `GET`
- **URL Parameters**:
  - `id`: ID маршрута

### Update Route

- **URL**: `/api/routes/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
  - `id`: ID маршрута
- **Body Parameters**:
  - ... (поля для обновления)

### Delete Route

- **URL**: `/api/routes/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id`: ID маршрута

## Examples

### Пример запроса на получение списка маршрутов

GET /api/routes/

### Пример ответа

```json
[
  {
    "id": 1,
    "name": "Everest Base Camp Trek",
    "difficulty": "Moderate",
    ...
  },
  ...
]
```

### Пример запроса на создание маршрута

POST /api/routes/
Content-Type: application/json

```json
{
  "name": "K2 Advanced Climb",
  "difficulty": "Difficult",
  ...
}
```

### Пример ответа на создание

```json
{
  "id": 2,
  "name": "K2 Advanced Climb",
  "difficulty": "Difficult",
  ...
}
```
