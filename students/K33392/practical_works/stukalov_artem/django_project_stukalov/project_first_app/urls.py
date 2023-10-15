from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/<int:driver_id>", views.get_driver, name="get_driver"),
]
