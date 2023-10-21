from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/add", views.add_driver, name="add_driver"),
    path("drivers/<int:id>/", views.driver, name="driver"),
    path(
        "drivers/delete/<int:pk>",
        views.DriverDeleteView.as_view(),
        name="driver_delete",
    ),
    path(
        "drivers/update/<int:pk>",
        views.DriverUpdateView.as_view(),
        name="driver_update",
    ),
    path("cars/add", views.add_car, name="add_car"),
]
