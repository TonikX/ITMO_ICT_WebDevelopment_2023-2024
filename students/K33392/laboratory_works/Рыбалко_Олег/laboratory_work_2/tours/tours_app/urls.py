from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.create_traveler_view),
    path("login", views.login_traveler_view),
    path("profile/<int:pk>", views.traveler_profile_view),
    path("profile", views.traveler_profile_view),
    path("tours", views.all_tours_view),
    path("reserve/<int:pk>", views.reserve_tour_date_view),
    path("cancel_reservation/<int:pk>", views.cancel_reservation_view),
]
