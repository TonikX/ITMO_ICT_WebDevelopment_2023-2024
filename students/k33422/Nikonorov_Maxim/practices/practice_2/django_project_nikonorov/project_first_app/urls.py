from django.contrib import admin
from django.urls import path, include
from .views import OwnerView, DetailOwnerView, CarView, DetailCarView, HomeView, CreateCar, EditCar, CreateOwner, DeleteCar

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('owners', OwnerView.as_view(), name='owner'), 
    path('owner/<int:pk>', DetailOwnerView.as_view(), name='detail-owner'), 
    path('cars', CarView.as_view(), name='car'), 
    path('car/<int:pk>', DetailCarView.as_view(), name='detail-car'), 
    path('new_car', CreateCar.as_view(), name='new-car'), 
    path('new_owner', CreateOwner.as_view(), name='new-owner'), 
    path('edit_car/<int:pk>', EditCar.as_view(), name='edit-car'), 
    path('delete_car/<int:pk>', DeleteCar.as_view(), name='delete-car'), 
]