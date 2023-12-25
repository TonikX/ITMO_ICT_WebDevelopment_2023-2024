# Сериалайзеры

Сериалайзеры мои сериалайзеры.

=== "Сериалайзеры для вывода всех записей из таблиц"

    ```Python

    --8<-- "laboratiry_work_3/museum/museum_app/serializers.py:1:68"

    ```

=== "Сериалайзеры для создания новых записей"

    ```Python
    from rest_framework import serializers
    from .models import *


    --8<-- "laboratiry_work_3/museum/museum_app/serializers.py:69:101"
    ```

=== "Сериалайзеры для запросов из задания"

    ```Python
    from rest_framework import serializers
    from .models import *


    --8<-- "laboratiry_work_3/museum/museum_app/serializers.py:101:131"
    ```


