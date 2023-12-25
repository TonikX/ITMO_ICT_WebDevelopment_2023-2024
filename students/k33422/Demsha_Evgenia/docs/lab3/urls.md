# Маршруты

Создадим маршрутизацию для проекта. В файле urls.py в одноименной с проектом директории museum будут прописаны пути к 
админке, авторизации, приложению и swagger-документации к его api. В файле urls.py в директории приложения 
укажем пути к страницам, где будут рендериться представления приложения.

=== "museum/urls.py"

    ```Python
    from django.db import models

    --8<-- "laboratiry_work_3/museum/museum/urls.py:1:31"
    ```

    admin/ - админка <br>
    api-auth/ - первая часть url для аутентификации <br>
    api/ - первая часть url к любому пути в приложении museum_app <br>
    auth/ - первая часть url для аутентификации по токенам средствами djoser <br>
    doc/swagger/ - путь к swagger документации <br>
    doc/redoc - путь к swagger документации <br>

=== "museum_app/urls.py"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/urls.py:1:17"
    ```

    foundations/list - посмотреть список фондов <br>
    card/list - посмотреть список картотек <br>
    card/create/ - создать картотеку <br>
    item/list - посмотреть список предметов <br>
    item/create/ - создать предмет <br>
    foundations/exhibitions/ - узнать количество выставок, в которых участвовали предметы каждого фонда <br>
    card/items/ - узнать количество предметов в каждой картотеке <br>
    foundations/ratio/ - узнать процентное отношение объемов фондов <br>
    item/exhibitions/<int:pk> - для выбранного предмета вывести предметы, которые участвовали с ним в одних выставках <br>
