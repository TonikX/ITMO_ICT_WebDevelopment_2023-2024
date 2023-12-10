# Добавление Swagger в проект Django с использованием drf-yasg

## Введение

Swagger - это инструмент для документирования и тестирования API. Для интеграции Swagger в проект Django с использованием Django REST Framework (DRF), мы будем использовать пакет `drf-yasg`, который предоставляет интеграцию Swagger для DRF.

## Шаг 1: Установка drf-yasg

Для начала установим `drf-yasg` с помощью следующей команды:

```bash
pip install drf-yasg
```

## Шаг 2: Настройка в файле urls.py
Добавим необходимые зависимости и создадим schema_view:

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


## Шаг 3: Настройка роутинга
Добавим пути для Swagger и redoc:
```
from django.urls import path

urlpatterns = [
    # Другие пути...
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
Теперь Swagger доступен по URL-адресу /doc/swagger/, а Redoc - по URL-адресу /doc/redoc/.

# Заключение
Теперь проект Django имеет интегрированный Swagger для удобного просмотра и тестирования API. Используя drf-yasg, я создал красивую и информативную документацию к своему проекту.