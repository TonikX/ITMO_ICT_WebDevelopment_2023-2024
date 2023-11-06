from django.urls import path
from .views import *

urlpatterns = [
    path("tours/<int:id>/reserve", ReservationCreationView.as_view()),
    path("tours", ToursListView.as_view()),
    path("", ToursListView.as_view()),
    path("tours/<int:pk>/", TourDetailView.as_view()),
    path("reservations/<int:pk>/edit", ReservationUpdateView.as_view()),
    path("reservations/<int:pk>/delete", ReservationDeleteView.as_view()),
    path("reservations/<int:pk>", ReservationDetailView.as_view()),
    path("reservations/", ReservationListView.as_view()),
    path("reservations/<int:id>/review", ReviewCreateView.as_view()),
    path("tours/<int:id>/reviews", ReviewListView.as_view())
]
