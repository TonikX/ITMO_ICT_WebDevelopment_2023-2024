"""
URL configuration for django_project_Sedelnikov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from project_first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:driver_id>', views.get_car_owner),
    path('owners_list', views.get_car_owners_list),
    path('car/<int:pk>', views.CarDetailView.as_view()),
    path('cars_list', views.CarListView.as_view()),
    path('create_owner', views.create_car_owner),
    path('create_car', views.CarCreateView.as_view()),
    path('update_car/<int:pk>', views.CarUpdateView.as_view()),
    path('delete_car/<int:pk>', views.CarDeleteView.as_view()),
]
