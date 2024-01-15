from django.urls import path
from .views import (
    add_review, tour_list, register, user_login, reserve_tour, review_tour, 
    user_reservations, confirm_reservation, tour_detail, reject_reservation,
    buy_tour, sold_tours, sell_tour, home, menu 
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_review/<int:tour_id>/', add_review, name='add_review_with_id'),
    path('add_review/', add_review, name='add_review_without_id'),
    path('', tour_list, name='tour_list'),  
    path('register/', register, name='register'),
    path('reserve_tour/<int:tour_id>/', reserve_tour, name='reserve_tour'),
    path('review_tour/<int:tour_id>/', review_tour, name='review_tour'),
    path('user_reservations/', user_reservations, name='user_reservations'),
    path('login/', user_login, name='login'),
    path('confirm_reservation/<int:reservation_id>/', confirm_reservation, name='confirm_reservation'),
    path('reject_reservation/<int:reservation_id>/', reject_reservation, name='reject_reservation'),
    path('tour_detail/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('sell_tour/<int:tour_id>/', sell_tour, name='sell_tour'),
    path('buy_tour/<int:tour_id>/', buy_tour, name='buy_tour'),
    path('sold_tours/', sold_tours, name='sold_tours'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
