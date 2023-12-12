# Комментарии

## Получение списка комментариев к посту по id 
**URL**: /api/posts/

**Method**: GET

**Auth required**: YES

**Permissions required**: None

**Query parametres**:
- `id` - id поста 

**Success response**:

```
{
    "Commentaries": [
        {
            "id": 1,
            "date": "2023-12-11T13:53:44.294081Z",
            "text": "Nice post!",
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
    ],
    "Count": "1"
}
```

## Создание комментария к посту 
**URL**: /api/posts/commentaries

**Method**: POST

**Auth required**: YES

**Permissions required**: None
