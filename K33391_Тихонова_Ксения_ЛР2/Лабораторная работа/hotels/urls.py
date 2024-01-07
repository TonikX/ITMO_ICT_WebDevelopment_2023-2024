from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="logout"),

    path("hotels", views.hotel_list, name="hotel_list"),
    path("hotels/<int:hotel_id>", views.hotel_detail, name="hotel_detail"),
    path("hotels/<int:hotel_id>/comment", views.leave_comment, name="leave_comment"),
    path("hotels/<int:hotel_id>/reserve", views.reserve_room, name="reserve_room"),


    path("reservations/", views.reservations_for_user, name="reservations_for_user"),
    path("reservations/<int:reservation_id>/", views.reservation_update, name="reservation_update"),
    path("reservations/<int:reservation_id>/delete", views.reservation_delete, name="reservation_delete"),
    path("list_reservs/<int:hotel_id>", views.list_passengers, name="list_users"),
]
