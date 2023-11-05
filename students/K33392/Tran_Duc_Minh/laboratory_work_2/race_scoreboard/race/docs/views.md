# Django Views

Below are the views defined in your Django project:

## `home`

- **Description:** Renders the 'home.html' template.
- **HTTP Method:** GET.

## `login_view`

- **Description:** Handles user login. If the form is submitted with valid credentials, it logs in the user and redirects to the 'home' view.
- **HTTP Methods:** GET, POST.

## `register_user`

- **Description:** Handles user registration. If the form is submitted with valid data, it creates a new user and logs them in, then redirects to the 'home' view.
- **HTTP Methods:** GET, POST.

## `race_list`

- **Description:** Lists races, filtering for races occurring in the future and displaying races the current user has registered for.
- **HTTP Method:** GET.

## `view_race`

- **Description:** Displays race details and handles race registration and comment submission. It also checks if the user is registered for the race and, if so, allows them to comment.
- **HTTP Methods:** GET, POST.

## `race_result_list`

- **Description:** Lists unique race results.
- **HTTP Method:** GET.

## `race_result_detail`

- **Description:** Displays detailed race results for a specific race.
- **HTTP Method:** GET.

## `unregister_from_race`

- **Description:** Handles user's race unregistration. If the user is registered for the race, it removes their registration and redirects to the 'view_race' view.
- **HTTP Method:** GET.

## `view_profile`

- **Description:** Renders the user's profile.
- **HTTP Method:** GET.

These views handle various functionalities of your Django project, including user authentication, race registration, race result listing, and profile viewing.
