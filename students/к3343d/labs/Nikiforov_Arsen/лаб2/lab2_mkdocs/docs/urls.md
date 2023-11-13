```python

# C:\WEBDJANGO\myproject\myapp\urls.py
from django.urls import path
from .views import add_review, tour_list, register, user_login, reserve_tour, review_tour, user_reservations, confirm_reservation, tour_detail, reject_reservation
from .views import buy_tour, sold_tours
from .views import sold_tours, sell_tour

urlpatterns = [
    path('', tour_list, name='tour_list'),  
    path('register/', register, name='register'),
    path('tour_list/', tour_list, name='tour_list'),
    path('reserve_tour/<int:tour_id>/', reserve_tour, name='reserve_tour'),
    path('review_tour/<int:tour_id>/', review_tour, name='review_tour'),
    path('user_reservations/', user_reservations, name='user_reservations'),
    path('login/', user_login, name='login'),
    path('confirm_reservation/<int:reservation_id>/', confirm_reservation, name='confirm_reservation'),
    path('reject_reservation/<int:reservation_id>/', reject_reservation, name='reject_reservation'),
    path('tour_detail/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('add_review/<int:tour_id>/', add_review, name='add_review'),
    path('sell_tour/<int:tour_id>/', sell_tour, name='sell_tour'),
    path('tour_list/', tour_list, name='tour_list'),
    path('buy_tour/<int:tour_id>/', buy_tour, name='buy_tour'),
    path('sold_tours/', sold_tours, name='sold_tours'),
]
```