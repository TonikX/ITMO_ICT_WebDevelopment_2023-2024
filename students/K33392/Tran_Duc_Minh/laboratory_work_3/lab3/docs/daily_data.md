# Daily Data

The Daily Data section provides endpoints for managing daily data related to user activities and calories.

## List and Create Daily Data

- **URL:** `/api/daily-data/`
- **Method:** `GET` (List Daily Data), `POST` (Create Daily Data)


## Retrieve, Update, and Delete Daily Data

- **URL:** `/api/daily-data/{dailydata_id}/`
- **Method:** `GET` (Retrieve Daily Data), `PUT` (Update Daily Data), `DELETE` (Delete Daily Data)

## Example
**URL:** `/api/daily-data/`

**Method:** `GET` (List Daily Data)

**Success Responses:**
```json
[
  {
    "id": 1,
    "user": {
      "id": 1,
      "username": "john",
      "first_name": "John",
      "last_name": "Doe"
    },
    "date": "2023-01-01",
    "activities": [
      {
        "id": 1,
        "name": "Running",
        "met_value": 8.0
      },
      {
        "id": 2,
        "name": "Cycling",
        "met_value": 6.0
      }
    ],
    "calories": 500
  },
  {
    "id": 2,
    "user": {
      "id": 2,
      "username": "jane",
      "first_name": "Jane",
      "last_name": "Doe"
    },
    "date": "2023-01-02",
    "activities": [
      {
        "id": 3,
        "name": "Swimming",
        "met_value": 7.0
      }
    ],
    "calories": 300
  }
]
```
