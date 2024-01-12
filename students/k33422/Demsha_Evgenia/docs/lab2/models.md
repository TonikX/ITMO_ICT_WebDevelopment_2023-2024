# Модели

Нам необходимо описать БД средствами Django ORM, для этого перейдём в файл `models.py` в нашем приложении и 
создадим несколько классов, наследуемых от `django.db.models.Model`.

=== "Отель"

    ```Python
    from django.db import models

    --8<-- "laboratory_work_2/hotelProject/hotel_app/models.py:4:16"
    ```

=== "Комната"

    ```Python
    from django.db import models


    --8<-- "laboratory_work_2/hotelProject/hotel_app/models.py:18:33"
    ```

=== "Бронирование"

    ```Python
    from django.contrib.auth.models import User
    from django.db import models

    --8<-- "laboratory_work_2/hotelProject/hotel_app/models.py:34:40"
    ```

=== "Отзыв"

    ```Python
    from django.contrib.auth.models import User
    from django.db import models


    --8<-- "laboratory_work_2/hotelProject/hotel_app/models.py:42:51"
    ```

После создания всех моделей нужно обязательно сделать миграции:

```commandline
python manage.py makemigrations
python manage.py migrate
```

А так же создать суперпользователя:

```commandline
python manage.py createsuperuser
```
