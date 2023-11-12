from django.urls import path
from . import views
from .views import CarView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('drivers/', views.all_drivers, name='all-drivers'),
    path('drivers/<int:driver_id>', views.get_driver, name='get-driver'),
    path('cars/', CarView.as_view(), name='all-cars'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='get-car'),
    path('drivers/create', views.create_driver, name='create-driver'),
    path('cars/create', CarCreateView.as_view(), name='create-car'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name='update-car'),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name='delete-car'),
]