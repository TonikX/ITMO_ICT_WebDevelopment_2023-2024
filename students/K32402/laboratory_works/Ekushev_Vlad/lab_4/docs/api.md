# Документация API (/api)

> 🔐 — для запроса требуется хедер `Authorization` с `accessToken` или `refreshToken`.

### POST /auth/login

Запрос производит аутентификацию пользователя по комбинаци email и паролю, возвращая JWT токены для дальнейшей работы с API.


*Запрос*
```json
{
  "email": "string",
  "password": "string"
}
```

*Ответ:*
```json
{
  "user": {
    "email": "string",
    "fullname": "string",
    "id": "string",
    "avatarUrl": "string?"
  },
  "tokens": {
    "accessToken": "string",
    "refreshToken": "string"
  }
}
```

### 🔐 GET /auth/logout

Удаляет текущие JWT токены из базы

*Ответ:*
```json
{
  "ok": true
}
```

### POST /auth/register

Регистрирует пользователя в системе. Возвращает тот же набор данных, что и /auth/login

*Запрос:*
```json
{
  "email": "string",
  "password": "string",
  "fullname": "string",
  "avatarUrl": "string?"
}
```

*Ответ:*
```json
{
  "user": {
    "email": "string",
    "fullname": "string",
    "id": "string",
    "avatarUrl": "string?"
  },
  "tokens": {
    "accessToken": "string",
    "refreshToken": "string"
  }
}
```

### 🔐 GET /auth/refresh

Обновляет текущие JWT токены по refresh токену

*Ответ:*
```json
{
  "accessToken": "string",
  "refreshToken": "string"
}
```
___

### 🔐 GET /user

Данные о пользователе

*Ответ:*
```json
{
  "user": {
    "email": "string",
    "fullname": "string",
    "id": "string",
    "avatarUrl": "string?"
  },
}
```

### 🔐 POST /user/update

Обновление данных о пользователе

*Запрос:*
```json
{
  "email": "string",
  "fullname": "string",
  "avatarUrl": "string?"
}
```

*Ответ:*
```json
{
  "user": {
    "email": "string",
    "fullname": "string",
    "id": "string",
    "avatarUrl": "string?"
  },
}
```

### 🔐 POST /user/uploadAvatar

Загрузка и обновление аватарки пользователя. Файл передаётся в формате `multipart/data`

*Запрос:*
```json
{
  "file": "multipart/data"
}
```

*Ответ:*
```json
{
  "avatarUrl": "string"
}
```
___

### 🔐 GET /devices

Данные о девайсах пользователя.

*Ответ:*
```json
{
  "devices": Device[]
}
```

Модель `Device`:

```typescript
enum DeviceType {
  LIGHT_BULB = 'light_bulb',
  KETTLE = 'kettle',
  THERMOSTAT = 'thermostat',
  CAMERA_OUTDOOR = 'camera_outdoor',
}

class Device {
  name: string
  type: DeviceType
  state: 0 | 1
  favorite: boolean
  userId: string
  capabilities: object
}
```

Для детального обзора поля `capabilities`, смотри страницу с [реализацией базы данных](/db).

### 🔐 GET /devices/favorites

Данные об избранных девайсах пользователя.

*Ответ:*
```json
{
  "devices": Device[]
}
```

### 🔐 GET /devices/{id}/favorite

Отмечает девайс с `ID={id}` избранным.

*Ответ:*
```json
{
  "ok": true
}
```

### 🔐 GET /devices/{id}/onOff/toggle

Включает или выключает девайс с `ID={id}`. Требуется поддержка `capabilities: { onOff: ... }` у девайса.

*Ответ:*
```json
{
  "ok": true
}
```

### 🔐 GET /devices/{id}/delete

Удаляет девайс с `ID={id}`.

*Ответ:*
```json
{
  "ok": true
}
```

### 🔐 POST /devices/add

Добавляет девайс по заданной схеме

*Запрос:*
```json
{
  "name": "string",
  "type": "DeviceType",
  "state": "0 | 1",
  "capabilities": "object"
}
```

*Ответ:*
```json
{
  "device": Device
}
```

## Ошибки

Отсутствует авторизация для защищённых роутов.

```json
{
  "message": "Unauthorized",
  "statusCode": 401
}
```

У девайса отсутствует данная возможность (список `capabilities`)

```json
{
  "message": "Unsupported device feature",
  "statusCode": 403
}
```
