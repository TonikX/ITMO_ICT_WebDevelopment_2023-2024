# Регистрация пользователя

``` 
URL: /auth/users/login/

Method: POST

Auth required: Нет

Permissions required: Нет

Data constraints:


    "username": "[string, required]",
    "email": "[string, required]",
    "password": "[string, required]"


Success Responses:

Code: 201 CREATED

Content:


    "id": "[integer]",
    "username": "[string]",
    "email": "[string]"

``` 


# Авторизация пользователя

``` 

URL: /auth/users/

Method: POST

Auth required: Нет

Permissions required: Нет

Data constraints:


    "username": "[string, required]",
    "password": "[string, required]"


Success Responses:

Code: 200 OK

Content:


    "token": "[string]"

``` 


# Изменение учетных данных пользователя

``` 

URL: /auth/user/<int:pk>/

Method: PUT

Auth required: Да

Permissions required: IsAuthenticated

Data constraints:


    "username": "[string, optional]",
    "email": "[string, optional]",
    "password": "[string, optional]"


Success Responses:

Code: 200 OK

Content:


    "id": "[integer]",
    "username": "[string]",
    "email": "[string]"


``` 