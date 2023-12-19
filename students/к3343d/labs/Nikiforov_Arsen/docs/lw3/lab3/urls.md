### urls.py


# Обзор urls.py

Файл `urls.py` отвечает за маршрутизацию в Django-приложении. Здесь определяются URL-адреса для различных представлений, включая те, что используются в REST API.

## Импорты

```python
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import (RoomViewSet, ClientViewSet, EmployeeViewSet, FloorViewSet, 
                    DayViewSet, EmployeeFloorViewSet, EmployeeDayViewSet, ClientInfoViewSet)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
```

Здесь мы импортируем необходимые модули для маршрутизации, включая `path` и `include` из `django.urls`, а также `DefaultRouter` из `rest_framework.routers`.

## Настройка роутера для API
Это маршрутизация в Django REST Framework для автоматического определения URL-адресов API на основе представлений. 
В данном случае, создается объект DefaultRouter, к которому регистрируются ViewSet (наборы представлений) для моделей, такие как RoomViewSet, ClientViewSet, EmployeeViewSet и другие. 
После этого, через urlpatterns эти URL-адреса включаются в основной URL-конфигурационный файл Django. 
Маршрутизаторы в Django REST Framework позволяют автоматически создавать URL-адреса на основе зарегистрированных представлений.
```python
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'days', DayViewSet)
router.register(r'employee_floors', EmployeeFloorViewSet)
router.register(r'employee_days', EmployeeDayViewSet)
router.register(r'client_info', ClientInfoViewSet)
```

`DefaultRouter` автоматически создает маршруты для CRUD-операций на основе представлений, созданных с помощью `viewsets` из Django REST Framework.

## URL-маршруты

```python  
urlpatterns = [    
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),    
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('clients/', views.clients_list, name='clients_list'),
    path('employees/', views.employees_list, name='employees_list'),
    path('floors/', views.floors_list, name='floors_list'),
    path('client-info/', views.client_info_list, name='client_info_list'),
    path('days/', views.days_list, name='days_list'),
    path('employee-floors/', views.employee_floors_list, name='employee_floors_list'),
    path('employee-days/', views.employee_days_list, name='employee_days_list'),
    path('bookings/', views.bookings_list, name='bookings_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('api/', include(router.urls)),  # Пути API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
```

`urlpatterns` определяет URL-адреса для приложения. Включены как стандартные представления Django, так и представления API, а также документация API с помощью `swagger` и `redoc`.


