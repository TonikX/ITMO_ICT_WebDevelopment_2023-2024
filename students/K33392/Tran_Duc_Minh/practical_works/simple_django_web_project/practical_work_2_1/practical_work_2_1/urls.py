from django.contrib import admin
from django.urls import path
from django_first_app import views
from django_first_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('addOwner/', views.addOwner, name="addOwner"),
    path('addCar/', views.addCar, name="addCarr"),
    path('car_list/', views.car_list, name='car_list'),
    path('<int:pk>/', OwnerRetrieveView.as_view()),
    path('delete/<int:pk>/', OwnerDelete.as_view(), name='delete-own'),
    path('update/<int:pk>/', OwnerUpdateView.as_view(), name='update-own'),
]
