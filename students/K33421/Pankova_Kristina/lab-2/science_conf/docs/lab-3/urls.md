# Файл urls.py

## Пути

- salons/ - Путь для получения списка салонов или создания нового салона.
- salons/create/ - Путь для создания нового салона.
- owners/ - Путь для получения списка владельцев салонов или создания нового владельца.
- owners/create/ - Путь для создания нового владельца салона.
- services/ - Путь для получения списка услуг или создания новой услуги.
- services/create/ - Путь для создания новой услуги.
- customers/create/ - Путь для создания нового клиента.
- appointments/ - Путь для получения списка записей в салон на прием или создания новой записи.
- appointments/create/ - Путь для создания новой записи на прием в салоне.
- salons/comments/ - Путь для получения списка комментариев о салонах или создания нового комментария.
- salons/comments/create - Путь для создания нового комментария о салоне.
- services/comments/ - Путь для получения списка комментариев об услугах или создания нового комментария.
- services/comments/create/ - Путь для создания нового комментария об услуге.

## Используемые представления

- SalonListAPIView - Представление для получения списка салонов.
- SalonCreateAPIView - Представление для создания нового салона.
- SalonOwnerListAPIView - Представление для получения списка владельцев салонов.
- SalonOwnerCreateAPIView - Представление для создания нового владельца салона.
- SalonServiceListAPIView - Представление для получения списка услуг.
- SalonServiceCreateAPIView - Представление для создания новой услуги.
- CustomerCreateAPIView - Представление для создания нового клиента.
- SalonAppointmentListAPIView - Представление для получения списка записей в салон на прием.
- SalonAppointmentCreateAPIView - Представление для создания новой записи на прием в салоне.
- SalonCommentsListAPIView - Представление для получения списка комментариев о салонах.
- SalonCommentsCreateAPIView - Представление для создания нового комментария о салоне.
- SalonServiceCommentsListAPIView - Представление для получения списка комментариев об услугах.
- SalonServiceCommentsCreateAPIView - Представление для создания нового комментария об услуге.

```python
from django.urls import path

from .views import *


app_name = "beauty_marketplace_app"


urlpatterns = [
   path('salons/', SalonListAPIView.as_view()),
   path('salons/create/', SalonCreateAPIView.as_view()),
   
   path('owners/', SalonOwnerListAPIView.as_view()),
   path('owners/create/', SalonOwnerCreateAPIView.as_view()),

   path('services/', SalonServiceListAPIView.as_view()),
   path('services/create/', SalonServiceCreateAPIView.as_view()),

   path('customers/create/', CustomerCreateAPIView.as_view()),
   path('customers/create/', CustomerCreateAPIView.as_view()),

   path('appointments/', SalonAppointmentListAPIView.as_view()),
   path('appointments/create/', SalonAppointmentCreateAPIView.as_view()),

   path('salons/comments/', SalonCommentsListAPIView.as_view()),
   path('salons/comments/create', SalonCommentsCreateAPIView.as_view()),

   path('services/comments/', SalonServiceCommentsListAPIView.as_view()),
   path('services/comments/create/', SalonServiceCommentsCreateAPIView.as_view()),

]
```

