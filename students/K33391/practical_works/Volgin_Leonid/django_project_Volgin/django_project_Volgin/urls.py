"""
URL configuration for django_project_Volgin project.

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

from project_firts_app.views import *

urlpatterns = [
     path('admin/', admin.site.urls),
     path('owner/<int:driver_id>', get_car_owner),
     path('list_of_car_owners',get_car_owners_list),
     path('list_of_cars',CarListView.as_view()),
     path('car/<int:pk>', CarDetailView.as_view()),
     path('update_car/<int:pk>', CarUpdateView.as_view()),
     path('create_car_owner', create_car_owner),
     path('create_car', CarCreateView.as_view()),
     path('update_car_with_form/<int:pk>', CarUpdateViewWithForm.as_view()),
     path('delete_car/<int:pk>', CarDeleteView.as_view()),
]
