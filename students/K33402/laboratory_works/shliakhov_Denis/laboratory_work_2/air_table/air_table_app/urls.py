from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.flights_list, name="flights_list"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("flights/", views.flights_list, name="flights_list"),
    path("flights/<int:flight_id>/", views.flight_info, name="flight_info"),
    path("flights/<int:flight_id>/reservation", views.reservation_create, name="reservation"),
    path("reservations/", views.reservations_for_user, name="reservations_for_user"),
    path("reservations/<int:reservation_id>/update", views.reservation_update, name="reservation_update"),
    path("reservations/<int:reservation_id>/delete", views.reservation_delete, name="reservation_delete"),
]