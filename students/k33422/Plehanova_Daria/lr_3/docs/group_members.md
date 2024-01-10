# Group Members API

## Overview

Этот API предназначен для управления данными членов групп восхождений. Позволяет получать список членов групп, добавлять новых членов, получать детали о конкретном члене группы, обновлять и удалять информацию о членах групп.

### URL

`/api/group_members/`


### Methods

- `GET`: Получение списка членов групп или деталей о конкретном члене группы.
- `POST`: Добавление нового члена группы (доступно только гидам и администраторам).
- `PUT`/`PATCH`: Обновление данных члена группы (доступно только гидам и администраторам).
- `DELETE`: Удаление члена группы (доступно только гидам и администраторам).

### Authentication

- Требуется аутентификация для чтения данных.
- Только гиды и администраторы могут добавлять, обновлять или удалять данные.

### Filters and Search

- Фильтрация по группе (`group`) и альпинисту (`alpinist`).
- Поиск по инциденту (`incident`), электронной почте альпиниста (`alpinist__user__email`), имени альпиниста (`alpinist__user__first_name`), фамилии альпиниста (`alpinist__user__last_name`).

## Endpoints

### List Group Members

- **URL**: `/api/group-members/`
- **Method**: `GET`
- **Query Parameters**:
  - `group`: Фильтр по ID группы.
  - `alpinist`: Фильтр по ID альпиниста.
  - `search`: Строка для поиска.

### Create Group Member

- **URL**: `/api/group-members/`
- **Method**: `POST`
- **Body Parameters**:
  - `alpinist_id`: ID альпиниста (необходимо, если пользователь не является администратором)
  - `group`: ID группы
  - ... (другие поля)

### Retrieve Group Member

- **URL**: `/api/group-members/{id}/`
- **Method**: `GET`
- **URL Parameters**:
  - `id`: ID члена группы

### Update Group Member

- **URL**: `/api/group-members/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
  - `id`: ID члена группы
- **Body Parameters**:
  - ... (поля для обновления)

### Delete Group Member

- **URL**: `/api/group-members/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id`: ID члена группы

## Examples

### Пример запроса на получение списка членов группы

GET `/api/group-members/?group=1`


### Пример ответа

```json
[
  {
    "id": 3,
    "group": 1,
    "alpinist": 3,
    "incident": "None",
    ...
  },
  ...
]
```

### Пример запроса на получение деталей о члене группы

GET `/api/group-members/1/`

### Пример ответа

```json
{
  "id": 1,
  "group": 2,
  "alpinist": 5,
  "incident": "None",
  ...
}
```

### Пример запроса на добавление нового члена группы

POST `/api/group-members/`
Content-Type: application/json

```json
{
  "group": 1,
  ...
}
```

### Пример ответа

```json
{
  "id": 4,
  "group": 1,
  "alpinist": 8,
  "incident": "None",
  ...
}
```

### Пример запроса на обновление данных члена группы

PUT `/api/group-members/4/`

```json
{
  "group": 2,
  ...
}
```

### Пример ответа

```json
{
  "id": 4,
  "group": 2,
  "alpinist": 8,
  "incident": "None",
  ...
}
```
