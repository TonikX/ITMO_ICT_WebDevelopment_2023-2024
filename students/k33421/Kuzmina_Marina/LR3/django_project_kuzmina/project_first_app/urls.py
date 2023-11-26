from django.urls import path
from project_first_app import views

urlpatterns = [
    path('', views.index, name='index'),

    path('drivers/', views.driver_list, name='driver_list'),
    path('drivers/create/', views.create_driver, name='create_driver'),
    path('drivers/<int:driver_id>/update/', views.update_driver, name='update_driver'),
    path('drivers/<int:driver_id>/delete/', views.delete_driver, name='delete_driver'),

    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreateView.as_view(), name='create_car'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='update_car'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='delete_car'),
]