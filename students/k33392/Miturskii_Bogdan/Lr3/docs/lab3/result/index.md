# Метод /user/get

```http
GET /user/get
```

## Заголовки запроса

- `authorization` (обязательный): Строка search генерируемая мини-приложением ВКонтакте при входе в него

## Пример ответа

```json
{
  "stats": {
    "wins": 1,
    "losses": 2,
    "draws": 3
  },
  "bonuses": {
    "rewardedGift": {
      "adWatchedTimes": 0,
      "lastUpdate": 1702344596245
    },
    "daily": 1701634904284,
    "subGroup": true,
    "joinChat": true,
    "notificationApp": true,
    "notificationBot": true,
    "addToHomeScreen": false,
    "addToFavorites": true
  },
  "tasks": {
    "completed": [],
    "current": [
      "play10matches",
      "win3MatchesNoPastureAndBeeFarm",
      "open4chests",
      "win3MatchesInRow"
    ],
    "nextUpdateAt": 1702387971270,
    "lastTasksMessageId": 652279
  },
  "_id": 457232519,
  "balance": 4629,
  "history": [
    {
      "userResponse": {
        "status": "win",
        "chest": "common",
        "rating": 280
      },
      "userInfo": {
        "chests": [
          {
            "empty": false,
            "adWatchedTimes": 0,
            "type": "common",
            "status": "idle",
            "willOpenAt": null
          },
          {
            "type": "magic",
            "status": "opening",
            "adWatchedTimes": 0,
            "willOpenAt": 28591663
          },
          {
            "type": "legendary",
            "status": "opening",
            "adWatchedTimes": 0,
            "willOpenAt": -4945825097
          },
          {
            "empty": false,
            "adWatchedTimes": 0,
            "status": "idle",
            "type": "common",
            "willOpenAt": null
          }
        ],
        "rating": 2060,
        "stats": {
          "wins": 107,
          "losses": 117,
          "draws": 3
        },
        "balance": 4629
      },
      "opponentInfo": {
        "id": 347633404,
        "photo_200": "https://sun1-88.userapi.com/s/v1/ig2/CEC2vkJU34yJak3V2OsgZ7bZSLXVNoxWyvixYoMkyQ5KdnD7ikdohxgVQ8ia76CwUm4x48a7AMH80bL7deN9Czcz.jpg?size=200x200&quality=95&crop=689,590,1871,1871&ava=1"
      },
      "id": "65759dabd9f981afa658fe9a"
    }
  ],
  "rating": 2060,
  "chests": [
    {
      "empty": false,
      "adWatchedTimes": 0,
      "status": "idle",
      "type": "common"
    },
    {
      "type": "magic",
      "status": "opening",
      "adWatchedTimes": 0,
      "willOpenAt": -109008975
    },
    {
      "type": "legendary",
      "status": "opening",
      "adWatchedTimes": 0,
      "willOpenAt": -5083425735
    },
    {
      "type": "common",
      "status": "opening",
      "adWatchedTimes": 0,
      "willOpenAt": -73014169
    }
  ],
  "__v": 67,
  "isTutorialPassed": true,
  "name": "Богдан Митурский",
  "photo_200": "https://sun1-19.userapi.com/s/v1/ig2/G9Xro7vK96AEz1hnczYAiXPOsZz9Anp1ACfDoDjRdyYPTSesKlqaVYrfRTHxywcrcvEObDLxHvjNKN-rNZww6ii8.jpg?size=200x200&quality=95&crop=0,688,1700,1700&ava=1",
  "collection": [
    {
      "entity": "sheep"
    },
    {
      "entity": "doubleFarm"
    },
    {
      "entity": "bigSheep"
    },
    {
      "entity": "crashedPlane"
    },
    {
      "entity": "deadFarm"
    },
    {
      "entity": "bee"
    },
    {
      "entity": "beehiveFarm"
    },
    {
      "entity": "necromancerSheep"
    },
    {
      "entity": "teslaTower"
    },
    {
      "entity": "mortar"
    },
    {
      "entity": "potion"
    },
    {
      "entity": "royalSheep",
      "blocked": true,
      "part": 3
    }
  ],
  "deck": [
    {
      "entity": "farm"
    },
    {
      "entity": "fastSheep"
    },
    {
      "entity": "icePeak"
    },
    {
      "entity": "pasture"
    }
  ]
}
```

## Примечание

Запрос не выполнится если ключ авторизации не будет передан или будет подделан

# Метод /user/replaceCard

```http
GET /user/replaceCard
```

## Параметры запроса

- `authorization` (обязательный): Строка search генерируемая мини-приложением ВКонтакте при входе в него
- `position` (обязательный): Позиция от 1 до 4 в которую необходимо переместить карту из колоды
- `entity` (обязательный): Наименование карты из колоды которую необходимо переместить

## Пример ответа

```json
{
  "ok": true
}
```

## Примечание

Запрос не выполнится если ключ авторизации не будет передан или будет подделан
