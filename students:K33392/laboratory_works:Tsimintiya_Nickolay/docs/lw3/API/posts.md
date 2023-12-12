# Посты 

## Получение списка постов 
**URL**: /api/posts/

**Method**: GET

**Auth required**: YES

**Permissions required**: None

**Payload**: None

**Success response**:

```JSON
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Posts": [
        {
            "id": 1,
            "title": "Kek",
            "description": "Lol",
            "text": "Korvalol",
            "date": "2023-12-10T11:15:16.917815Z",
            "imageURL": "https://icdn.lenta.ru/images/2014/11/24/17/20141124172227866/detail_a846c540032e66cd055b47c26bacabd5.jpg",
            "author": {
                "id": 1,
                "password": "pbkdf2_sha256$600000$dtPjZa6bLFtejtulYfeB9i$k9F14VJ+KDHb1iBqpkWtxjiZ47mJduqXuoMnvIByxEw=",
                "last_login": "2023-12-10T11:15:00.019851Z",
                "is_superuser": true,
                "username": "master",
                "first_name": "",
                "last_name": "",
                "email": "wwwwat@inbox.ru",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2023-12-10T11:14:45.938422Z",
                "groups": [],
                "user_permissions": []
            }
        }
    ]
}
```

## Получение списка постов определенного автора 
**URL**: /api/posts/

**Method**: GET

**Auth required**: YES

**Permissions required**: None

**Payload**: None

**Query parametres**:
- `author` - имя автора постов

**Success response**:

```
{
    "Posts": [
        {
            "id": 1,
            "title": "Kek",
            "description": "Lol",
            "text": "Korvalol",
            "date": "2023-12-10T11:15:16.917815Z",
            "imageURL": "https://icdn.lenta.ru/images/2014/11/24/17/20141124172227866/detail_a846c540032e66cd055b47c26bacabd5.jpg",
            "author": {
                "id": 1,
                "password": "pbkdf2_sha256$600000$dtPjZa6bLFtejtulYfeB9i$k9F14VJ+KDHb1iBqpkWtxjiZ47mJduqXuoMnvIByxEw=",
                "last_login": "2023-12-10T11:15:00.019851Z",
                "is_superuser": true,
                "username": "master",
                "first_name": "",
                "last_name": "",
                "email": "wwwwat@inbox.ru",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2023-12-10T11:14:45.938422Z",
                "groups": [],
                "user_permissions": []
            }
        }
    ]
}
```
## Создание поста 
**URL**: /api/posts/

**Method**: POST

**Auth required**: YES

**Permissions required**: None
