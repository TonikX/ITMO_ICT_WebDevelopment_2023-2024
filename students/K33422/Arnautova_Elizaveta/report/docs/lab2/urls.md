# Пути

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>/', views.flight_info, name='flight_info'),
    path('list_reservations/', views.list_reservations, name='list_reservations'),
    path('make_reservation/<int:flight_id>/', views.make_reservation, name='create_reservation'),
    path('make_reservation/<int:flight_id>/<int:reservation_id>/', views.make_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('make_review/<int:flight_id>/', views.make_review, name='make_review')
]

```
