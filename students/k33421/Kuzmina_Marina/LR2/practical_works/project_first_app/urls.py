from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('drivers/', views.driver_list, name='driver_list'),
    path('drivers/create/', views.driver_creation, name='driver_creation'),
    path('drivers/<int:driver_id>/update/', views.driver_update, name='driver_update'),
    path('drivers/<int:driver_id>/delete/', views.driver_deletion, name='driver_deletion'),

    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_creation'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='update_car'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_deletion'),
]
