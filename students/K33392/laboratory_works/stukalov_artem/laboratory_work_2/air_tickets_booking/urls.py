from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.user_register_view, name="user_register"),
    path("login", views.user_login_view, name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
    path("flights", views.flights_list_view, name="flights_list"),
    path("flights/<int:flight_id>", views.flight_detail_view, name="flight_detail"),
    path("tickets", views.tickets_list_view, name="tickets_list"),
    path(
        "tickets/<int:ticket_id>/update", views.ticket_update_view, name="ticket_update"
    ),
    path("tickets/<int:ticket_id>/delete", views.ticket_delete, name="ticket_delete"),
]
