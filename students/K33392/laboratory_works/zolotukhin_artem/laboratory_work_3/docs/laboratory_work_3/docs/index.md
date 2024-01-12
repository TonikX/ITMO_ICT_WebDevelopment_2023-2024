# Animals API Endpoints

## List Animals

`GET /system/animals/`
Returns a list of all animals.

### Permissions

Authenticated Users: Can view the list of animals.
Admin Users: Can view the list of animals.

## Retrieve Animal

`GET /system/animals/{id}/`
Retrieves a specific animal by ID.

### Permissions

Authenticated Users: Can view the animal details.
Admin Users: Can view the animal details.

## Animals In Lease

`GET /system/animals/animals_in_lease/`
Returns a list of animals that are currently in lease.

### Permissions

Authenticated Users: Can view the list of animals in lease.
Admin Users: Can view the list of animals in lease.

## Animals In Communal Cages

`GET /system/animals/animals_in_communas/`
Returns a list of animals that are in communal cages.

### Permissions

Authenticated Users: Can view the list of animals in communal cages.
Admin Users: Can view the list of animals in communal cages.

## Animals Leaving Together

`GET /system/animals/{id}/leaving_together/`
Returns a list of animals leaving together in the same area as the animal with the specified ID.

### Permissions

Authenticated Users: Can view the list of animals leaving together.
Admin Users: Can view the list of animals leaving together.

... and so on for each action in your `AnimalViewSet`.
