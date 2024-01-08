from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="user_register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("races/", views.races_list, name="races_list"),
    path("races/<int:race_id>/", views.race_detail, name="race_detail"),
    path("registrations/", views.regs_for_user, name="your_regs"),
    path("registrations/<int:reg_id>/delete", views.reg_delete, name="reg_delete"),
    
]