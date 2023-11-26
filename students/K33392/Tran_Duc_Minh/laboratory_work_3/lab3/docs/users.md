# Users

The Users section provides endpoints for managing user information.

## List and Create Users

- **URL:** `/users/`
- **Method:** `GET` (List Users), `POST` (Create User)


## Retrieve, Update, and Delete User

- **URL:** `/api/users/{user_id}/`
- **Method:** `GET` (Retrieve User), `PUT` (Update User), `DELETE` (Delete User)

## Example
**URL:** `/api/users/`

**Method:** `GET` (Retrieve User)

**Success Responses:**
```json
[
  { 
    "id": 1,
    "username": "john",
    "first_name": "John",
    "last_name": "Doe"
  },
  {
    "id": 2,
    "username": "jane",
    "first_name": "Jane",
    "last_name": "Doe"  
  }
]
```
