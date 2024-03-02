# Existing Endpoints

## Registration Endpoint

This endpoint allows users to register for a new account in the system.

### URL

POST /api/register/


### Request Body

{
  "username": "example",
  "password": "password123",
  "email": "example@example.com"
}
### Response


{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "example",
    "email": "example@example.com"
  }
}
