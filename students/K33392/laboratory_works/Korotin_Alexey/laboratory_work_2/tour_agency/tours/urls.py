from django.urls import path
from .views import *

urlpatterns = [
    path("tours/<int:id>/reserve", ReservationCreationView.as_view()),
    path("tours", ToursListView.as_view()),
    path("tours/<int:pk>/", TourDetailView.as_view())
]
