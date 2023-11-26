# User Foods

The User Foods section provides endpoints for managing user-specific food consumption data.

## List and Create User Foods

- **URL:** `/api/user-foods/`
- **Method:** `GET` (List User Foods), `POST` (Create User Food)


## Retrieve, Update, and Delete User Food

- **URL:** `/api/user-foods/{userfood_id}/`
- **Method:** `GET` (Retrieve User Food), `PUT` (Update User Food), `DELETE` (Delete User Food)

## Example
### 1. Retrieve User Food
**URL:** `/api/user-foods/1/`

**Method:** `GET` (Retrieve User Food)

**Success Responses:**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "john",
    "first_name": "John",
    "last_name": "Doe"
  },
  "food": {
    "id": 1,
    "name": "Apple",
    "calories": 95,
    "protein": 0.5,
    "carbs": 25.0,
    "fat": 0.3
  },
  "date": "2023-01-01",
  "amount": 2.0
}

```
### 2. Update User Food

**URL:** `/api/user-foods/1/`

**Method:** `PUT ` (Update User Food)

**Request:** 
```json
{
  "amount": 2.5
}
```
**Success Responses:**
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "john",
    "first_name": "John",
    "last_name": "Doe"
  },
  "food": {
    "id": 1,
    "name": "Apple",
    "calories": 95,
    "protein": 0.5,
    "carbs": 25.0,
    "fat": 0.3
  },
  "date": "2023-01-01",
  "amount": 2.5
}
```
