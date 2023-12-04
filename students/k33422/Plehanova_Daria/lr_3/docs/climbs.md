# Climbs API

## Overview

Этот API предназначен для управления данными восхождений. Позволяет получать список восхождений, создавать новые восхождения, получать детали конкретного восхождения, обновлять и удалять информацию о восхождениях.

### URL

`/api/climbs`


### Methods

- `GET`: Получение списка восхождений или деталей о конкретном восхождении.
- `POST`: Создание нового восхождения (доступно только гидам и администраторам).
- `PUT`/`PATCH`: Обновление данных восхождения (доступно только гидам и администраторам).
- `DELETE`: Удаление восхождения (доступно только гидам и администраторам).

### Authentication

- Требуется аутентификация для чтения данных.
- Только гиды и администраторы могут создавать, обновлять или удалять данные.

### Filters and Search

- Фильтрация по гиду (`guide`) и маршруту (`route`).
- Поиск по электронной почте гида (`guide__user__email`), имени гида (`guide__user__first_name`), фамилии гида (`guide__user__last_name`), названию маршрута (`route__name`) и названию горы (`route__mountain__name`).

## Endpoints

### List Climbs

- **URL**: `/api/climbs/`
- **Method**: `GET`
- **Query Parameters**:
  - `guide`: Фильтр по ID гида.
  - `route`: Фильтр по ID маршрута.
  - `search`: Строка для поиска.

### Create Climb

- **URL**: `/api/climbs/`
- **Method**: `POST`
- **Body Parameters**:
  - `guide_id`: ID гида (необходимо, если пользователь не является гидом)
  - `route`: ID маршрута
  - ... (другие поля)

### Retrieve Climb

- **URL**: `/api/climbs/{id}/`
- **Method**: `GET`
- **URL Parameters**:
  - `id`: ID восхождения

### Update Climb

- **URL**: `/api/climbs/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
  - `id`: ID восхождения
- **Body Parameters**:
  - ... (поля для обновления)

### Delete Climb

- **URL**: `/api/climbs/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id`: ID восхождения

## Examples

### Пример запроса на получение списка восхождений

GET /api/climbs/

### Пример ответа

```json
[
  {
    "id": 1,
    "guide": 2,
    "route": 3,
    ...
  },
  ...
]
```

### Пример запроса на получение деталей восхождения

GET /api/climbs/1/

### Пример ответа

```json
{
  "id": 1,
  "guide": 2,
  "route": 3,
  ...
}
```


### Пример запроса на создание восхождения

POST /api/climbs/
Content-Type: application/json

```json
{
  "guide_id": 2,
  "route": 3,
  ...
}
```

### Пример ответа

```json
{
  "id": 5,
  "guide": 2,
  "route": 3,
  ...
}
```


### Пример запроса на обновление восхождения

PUT /api/climbs/5/
Content-Type: application/json

```json
{
  "guide_id": 2,
  "route": 3,
  ...
}
```

### Пример ответа

```json
{
  "id": 5,
  "guide": 2,
  "route": 3,
  ...
}
```