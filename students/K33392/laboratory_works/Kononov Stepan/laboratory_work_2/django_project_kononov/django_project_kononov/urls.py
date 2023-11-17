"""
URL configuration for django_project_kononov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from project_first_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:owner_id>/', owner_detail, name='owner_detail'),
    path('all_owners/', all_owners, name='all_owners'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add_car_owner/', add_car_owner, name='add_car_owner'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('car/update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    path('car/delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
]
