# django-rest-api
A REST api written in Django

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


* #### Dependencies
    1. Install the dependencies needed to run the app:
        ```bash
            $ pip install django djangorestframework djoser django_filters drf_yasg django-cors-headers
        ```
    2. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://127.0.0.1:8000/admin/
        http://127.0.0.1:8000/api/
        http://127.0.0.1:8000/auth/
    ```