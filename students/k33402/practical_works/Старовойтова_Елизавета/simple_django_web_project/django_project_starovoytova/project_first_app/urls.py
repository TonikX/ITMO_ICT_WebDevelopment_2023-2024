from django.urls import path
from . import views
from .views import CarListView, CarDetailView, CarUpdateView, CarCreateView

urlpatterns = [
    path('add_owner/', views.add_owner, name='add_owner'),
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owners/', views.owner_list, name='owner_list'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('index/', views.index, name='index'),
    path('cars/create/', CarCreateView.as_view(), name='car_form'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/delete/<int:car_id>/', views.CarDeleteByIdView.as_view(), name='car_delete_by_id'),
]
