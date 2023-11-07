from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('', views.home, name='home'),
    path('reservations/', views.reservations_list, name='reservations_list'),
    path('reservations/create/', views.create_reservation, name='create_reservation'),
    path('reservations/edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('tours/create', views.create_tour, name='create_tour'),
    path('add_review/<int:tour_id>/', views.add_review, name='add_review'),
    path('tours_with_reservation_count/', views.tours_with_reservation_count, name='tours_with_reservation_count'),
]