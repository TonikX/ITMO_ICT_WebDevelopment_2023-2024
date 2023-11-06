from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [

    path('register/', register, name='register'),

    path('hotels/', hotel_list, name='hotel_list'),

    path('reservations/', reservation_list, name='reservation_list'),

    path('reservations/edit/<int:reservation_id>/',
         reservation_edit, name='reservation_edit'),

    path('reservations/delete/<int:reservation_id>/',
         reservation_delete, name='reservation_delete'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    path('reservations/<int:user_id>/', admin_reservation_list, name='admin_reservation_list'),

    path('reservations/<int:reservation_id>/review/', review, name='review'),

    path('hotel-guests/', hotel_guests, name='hotel_guests'),

]