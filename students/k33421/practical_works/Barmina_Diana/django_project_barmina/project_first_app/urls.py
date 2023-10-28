from django.urls import path
from . import views
from .views import AutoView, AutoDetailView, AutoCreateView, AutoUpdateView, AutoDeleteView

urlpatterns = [
    path('', views.home, name="home"),
    path('drivers/', views.all_drivers, name='all-drivers'),
    path('drivers/<int:driver_id>', views.get_driver, name='get-driver'),
    path('autos/', AutoView.as_view(), name='all-autos'),
    path('autos/<int:pk>', AutoDetailView.as_view(), name='get-auto'),
    path('drivers/create', views.create_driver, name='create-driver'),
    path('autos/create', AutoCreateView.as_view(), name='create-auto'),
    path('autos/<int:pk>/update', AutoUpdateView.as_view(), name='update-auto'),
    path('autos/<int:pk>/delete', AutoDeleteView.as_view(), name='delete-auto'),
]
