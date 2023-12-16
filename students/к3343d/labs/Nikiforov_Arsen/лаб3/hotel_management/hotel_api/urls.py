# hotel_management/hotel_api/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('rooms/', views.rooms_list, name='rooms_list'),  # Список комнат
    path('clients/', views.clients_list, name='clients_list'),  # Список клиентов
    path('employees/', views.employees_list, name='employees_list'),  # Список сотрудников
    path('floors/', views.floors_list, name='floors_list'),  # Информация об этажах
    path('client-info/', views.client_info_list, name='client_info_list'),  # Информация о клиентах
    path('days/', views.days_list, name='days_list'),  # Информация о днях
    path('employee-floors/', views.employee_floors_list, name='employee_floors_list'),  # Список сотрудников по этажам
    path('employee-days/', views.employee_days_list, name='employee_days_list'),  # Расписание сотрудников
    path('bookings/', views.bookings_list, name='bookings_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
