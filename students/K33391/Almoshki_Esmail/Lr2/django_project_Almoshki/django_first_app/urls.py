from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("drivers/<int:id>", views.driver_page, name='driver_page'),
    path("cars/<int:id>", views.car_page, name='car_page'),
    path('drivers/', views.DriverListView.as_view(), name='driver_list'),
    path('cars/', views.CarListView.as_view(), name="car_list"),
    path('drivers/create/', views.DriverCreateView.as_view()),
    path("cars/create/", views.CarCreateView.as_view()),
    path('cars/(?P<pk>\d+)/delete/',
         views.CarDeleteView.as_view(), name="car_delete"),
    path('cars/(?P<pk>\d+)/update/',
         views.CarUpdateView.as_view(), name="car_update")
]
