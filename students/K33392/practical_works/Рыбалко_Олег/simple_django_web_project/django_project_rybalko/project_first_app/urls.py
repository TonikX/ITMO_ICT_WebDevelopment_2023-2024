from django.urls import path

from . import views

urlpatterns = [path("car_owner/<int:owner_id>", views.car_owner), path("car_owners", views.all_owners)]
