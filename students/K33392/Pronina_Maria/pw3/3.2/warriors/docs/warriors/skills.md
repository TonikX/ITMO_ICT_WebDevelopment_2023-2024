# Показать скиллы всех войнов

Выводит информацию обо всех скиллах всех войнов

***URL*** : `/warriors/profession`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content**:

```json
{
        "name": "Олег",
        "skill": [
            {
                "skill": "Удалять снег",
                "level": 100
            },
            {
                "skill": "Удалять листья",
                "level": 3
            }
        ]
    }
```