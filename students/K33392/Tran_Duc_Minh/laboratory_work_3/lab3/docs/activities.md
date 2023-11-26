# Activities

The Activities section provides endpoints for managing activity information.

## List and Create Activities

- **URL:** `/api/activities/`
- **Method:** `GET` (List Activities), `POST` (Create Activity)


## Retrieve, Update, and Delete Activity

- **URL:** `/api/activities/{activity_id}/`
- **Method:** `GET` (Retrieve Activity), `PUT` (Update Activity), `DELETE` (Delete Activity)

## Example
### 1. Create activities
**URL:** `/api/activities/`

**Method:** `POST ` (Create Activity)

**Request:** 
```json
{
  "name": "Swimming",
  "met_value": 7.0
}
```
**Success Responses:**
```json
{
  "id": 3,
  "name": "Swimming",
  "met_value": 7.0
}
```
### 2. List activities

**URL:** `/api/activities/`

**Method:** `GET` (List Activities)

**Success Responses:**
```json
[
  { 
    "id": 1,
    "name": "Running",
    "met_value": 8.0
  },
  {
    "id": 2,
    "name": "Cycling",
    "met_value": 6.0
  },
  {
    "id": 3,
    "name": "Swimming",
    "met_value": 7.0
  }
]
```
