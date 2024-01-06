"""
URL configuration for flight_info2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.md import include, path
    2. Add a URL to urlpatterns:  path('blo
g/', include('blog.urls.md'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
# from django.urls.md import include, path


from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('personal_space/', personal_space_view, name='personal_space'),
    path('user_reservations/', show_user_reservations, name='user_reservations'),
    path('edit_reservation/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
    path('flight_passengers/<int:flight_id>/', flight_passengers, name='flight_passengers'),
    path('personal_space/create_review/<int:flight_id>/', create_review, name='create_review'),
    path('flight_reviews/<int:flight_id>/', flight_reviews, name='flight_reviews'),
    path('all_flights', flights_list, name="flights_list"),
    path('', home, name='home'),
]
