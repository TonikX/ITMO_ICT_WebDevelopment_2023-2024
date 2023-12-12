# Авторы 

## Получение списка авторов 
## Получение списка комментариев к посту по id 
**URL**: /api/posts/

**Method**: GET

**Auth required**: YES

**Permissions required**: None

**Success response**:

```
{
    "Authors": [
        {
            "id": 1,
            "password": "pbkdf2_sha256$600000$dtPjZa6bLFtejtulYfeB9i$k9F14VJ+KDHb1iBqpkWtxjiZ47mJduqXuoMnvIByxEw=",
            "last_login": "2023-12-10T11:15:00.019851Z",
            "username": "master",
            "first_name": "",
            "last_name": "",
            "email": "wwwwat@inbox.ru",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2023-12-10T11:14:45.938422Z",
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 2,
            "password": "pbkdf2_sha256$600000$XRtKERyJiaTpqZ3HbcXKQy$7dPDTC6DtuMACtEjySkgo/S/7gE4qavkuqmCDBpWCXo=",
            "last_login": "2023-12-12T09:43:49.898245Z",
            "username": "testUser",
            "first_name": "",
            "last_name": "",
            "email": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-12-12T09:40:12.862142Z",
            "groups": [],
            "user_permissions": []
        }
    ]
}
```