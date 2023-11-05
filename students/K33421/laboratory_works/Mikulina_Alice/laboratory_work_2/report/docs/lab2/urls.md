# Urls


```
from django.urls import path 
from . import views
from .views import *


urlpatterns = [
    path('auth/reg', views.register, name='Registration'),
    path('auth/login', views.user_login, name='Log in'),
    path('auth/logout', views.user_logout, name='Log out'),
    path('profile', views.profile, name='Profile'),
    path('profile/delete', views.delete_profile, name='Delete profile'),
    path('profile/edit', views.edit_profile, name='Edit profile'),
    path('profile/reservations', ReservationListView.as_view(), name='Show_reservations'),
    path('profile/reservation/<int:pk>', ReservationDetailView.as_view(), name='Reservation_detail'),
    path('main', views.list_rooms, name='List rooms'),
    path('main/room/<int:room_id>', views.show_room, name='Show room'),
    path('main/hotels', views.list_hotels, name='List hotels'),
    path('main/hotel/<int:hotel_id>', views.show_hotel, name='Show hotel'),
    path('profile/review/<int:pk>/update', ReviewUpdateView.as_view(), name='Update review'),
    path('profile/review/<int:pk>/delete', ReviewDeleteView.as_view(), name='Delete review'),
    path('user/<int:user_id>', views.show_user, name='Show user'),
    path('reservation/<int:room_id>/create', ReservationCreate.as_view(), name='Reserve_room'),
    path('reservation/<int:pk>/update', ReservationUpdateView.as_view(), name='Update room'),
    path('reservation/<int:pk>/delete', ReservationDeleteView.as_view(), name='Delete room'),
]
```