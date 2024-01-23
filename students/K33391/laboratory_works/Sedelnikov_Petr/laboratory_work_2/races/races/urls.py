"""
URL configuration for races project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from racestables import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.dashboard, name='dashboard'),
    path("registrate/", views.register, name="registrate"),
    path("registrate_racer/", views.register_racer, name="registrate_racer"),
    path("redact_user/", views.redact_user, name="redact_user"),
    path("change_password/", views.change_password, name="change_password"),
    path("redact_racer/", views.redact_racer, name="redact_racer"),
    path("races/comments/<int:race_id>/", views.race_comments, name="race_comments"),
    path("races/", views.races_list, name="races_list"),
    path("profile/delete/", views.delete_user, name="delete_user"),
    path("create_race_connection/<int:race_id>/", views.create_race_connection, name="create_race_connection"),
    path("delete_race_connection/<int:race_id>", views.delete_race_connection, name="delete_race_connection"),
]
