from django.urls import path

from . import views

urlpatterns = [
    path("car_owner/<int:owner_id>", views.car_owner),
    path("car/<int:car_id>/owners", views.all_owners),
]
