from django.urls import path
from .views import (HotelListView, UserRegistrationView,
                    ReservationEditView, ReservationDeleteView,
                    ReservationListView)

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('reservations/', ReservationListView.as_view(), name='reservations_list'),
    path('reservations/<int:pk>/edit/', ReservationEditView.as_view(), name='reservation_edit'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
]
