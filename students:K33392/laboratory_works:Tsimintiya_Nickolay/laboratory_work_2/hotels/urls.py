from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('reserve/<int:hotel_id>/', views.room_reserve, name='room_reserve'),
    path('review/<int:hotel_id>/', views.write_review, name='write_review'),
    path('lastmonth/', views.last_month_guests, name='last_month_guests'),
]
