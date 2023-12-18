from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import (RoomViewSet, ClientViewSet, EmployeeViewSet, FloorViewSet, 
                    DayViewSet, EmployeeFloorViewSet, EmployeeDayViewSet, ClientInfoViewSet)

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'days', DayViewSet)
router.register(r'employee_floors', EmployeeFloorViewSet)
router.register(r'employee_days', EmployeeDayViewSet)
router.register(r'client_info', ClientInfoViewSet)

urlpatterns = [    
    # URL для главной страницы
    path('', views.home, name='home'),
    # URL для страницы входа
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # URL для страницы регистрации
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
]
