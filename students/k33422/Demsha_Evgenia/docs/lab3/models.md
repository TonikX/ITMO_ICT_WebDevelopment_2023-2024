# Модели

Нам необходимо описать БД средствами Django ORM, для этого перейдём в файл `models.py` в нашем приложении и 
создадим несколько классов, наследуемых от `django.db.models.Model`.

=== "Музей и Автор"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/models.py:1:20"
    ```

=== "Предмет и Картотека"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/models.py:21:45"
    ```

=== "Фонд и Выставка"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/models.py:46:71"
    ```

=== "Помещение в Фонд и Отправка на Выставку"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/models.py:72:94"
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

