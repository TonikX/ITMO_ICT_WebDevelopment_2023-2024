# Groups API

## Overview

Этот API предназначен для управления данными групп восхождений. Позволяет получать список групп, создавать новые группы, получать детали конкретной группы, обновлять и удалять информацию о группах.

### URL

`/api/groups/`


### Methods

- `GET`: Получение списка групп или деталей о конкретной группе.
- `POST`: Создание новой группы (доступно только гидам и администраторам).
- `PUT`/`PATCH`: Обновление данных группы (доступно только гидам и администраторам).
- `DELETE`: Удаление группы (доступно только гидам и администраторам).

### Authentication

- Требуется аутентификация для чтения данных.
- Только гиды и администраторы могут создавать, обновлять или удалять данные.

### Filters and Search

- Фильтрация по восхождению (`climb`).
- Поиск по названию маршрута (`climb__route__name`), названию горы (`climb__route__mountain__name`), электронной почте гида (`climb__guide__user__email`), имени гида (`climb__guide__user__first_name`), фамилии гида (`climb__guide__user__last_name`).

## Endpoints

### List Groups

- **URL**: `/api/groups/`
- **Method**: `GET`
- **Query Parameters**:
  - `climb`: Фильтр по ID восхождения.
  - `search`: Строка для поиска.

### Create Group

- **URL**: `/api/groups/`
- **Method**: `POST`
- **Body Parameters**:
  - `climb`: ID восхождения
  - `member_count`: Количество членов в группе (опционально, для администраторов)

### Retrieve Group

- **URL**: `/api/groups/{id}/`
- **Method**: `GET`
- **URL Parameters**:
  - `id`: ID группы

### Update Group

- **URL**: `/api/groups/{id}/`
- **Method**: `PUT`/`PATCH`
- **URL Parameters**:
  - `id`: ID группы
- **Body Parameters**:
  - `member_count`: Новое количество членов в группе (опционально)

### Delete Group

- **URL**: `/api/groups/{id}/`
- **Method**: `DELETE`
- **URL Parameters**:
  - `id`: ID группы

## Examples

### Пример запроса на получение списка групп

GET `/api/groups/`

### Пример ответа

```json
[
  {
    "id": 1,
    "climb": 3,
    "member_count": 5,
    ...
  },
  ...
]
```

### Пример запроса на получение деталей группы

GET `/api/groups/1/`

### Пример ответа

```json
{
  "id": 1,
  "climb": 3,
  "member_count": 5,
  ...
}
```

### Пример запроса на создание группы

POST `/api/groups/`

```json
{
  "climb": 3,
  "member_count": 5
}
```

### Пример ответа

```json
{
  "id": 18,
  "climb": 3,
  "member_count": 5,
  ...
}
```