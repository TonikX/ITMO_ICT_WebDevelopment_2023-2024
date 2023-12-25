# Представления

Создадим представления на основе стандартных Generic классов.

=== "Представления, необходимые для обработки запросов, указанных во варианте"

    ```Python
    from rest_framework import generics
    from .serializers import *
    from .models import *
    from django.db.models import Count, F

    --8<-- "laboratiry_work_3/museum/museum_app/views.py:71:97"
    ```

=== "Остальные представления, для вывода в виде списка, детального вывода и создания объектов"

    ```Python
    from rest_framework import generics
    from .serializers import *
    from .models import *

    --8<-- "laboratiry_work_3/museum/museum_app/views.py:6:71"
    ```

