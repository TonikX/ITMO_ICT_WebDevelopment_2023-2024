from django.contrib.auth import views as auth_views
from django.urls import path

import racing_club.views as views

urlpatterns = [
    path("", views.base, name="base"),
    path("register_racer/", views.register_racer, name="register_racer"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("races/", views.races_list, name="races_list"),
    path("races/<int:race_id>/comments/", views.race_comments, name="race_comments"),
    path("profile/", views.profile, name="profile"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),
    path("profile/logout", views.user_logout, name="logout")
]