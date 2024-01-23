# Показать информацию о войне

Выводит полную информацию о войне по id, возможность обновить информацию, удалить война

***URL*** : `/warriors/<int:pk>`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content**:

```json
{
    "id": 1,
    "skill": [
        {
            "skill": "Удалять снег",
            "level": 100
        },
        {
            "skill": "Удалять листья",
            "level": 3
        }
    ],
    "race": "teamlead",
    "profession": {
        "id": 1,
        "title": "Дворник",
        "description": "Дворнит"
    },
    "name": "Олег",
    "level": 100
}
```