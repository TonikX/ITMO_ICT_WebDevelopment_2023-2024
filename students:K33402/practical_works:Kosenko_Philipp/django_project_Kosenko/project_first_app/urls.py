from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drivers", views.list_drivers, name="list_drivers"),
    path("drivers/<int:driver_id>", views.get_driver, name="get_driver"),
    path("drivers/create", views.create_driver, name="create_driver"),
    path("cars", views.CarListView.as_view(), name="cars_list_view"),
    path("cars/<int:pk>", views.CarDetailView.as_view(), name="car_detail_view"),
    path("cars/create", views.CarCreateView.as_view(), name="car_create_view"),
    path("cars/<int:pk>/update", views.CarUpdateView.as_view(), name="car_update_view"),
    path("cars/<int:pk>/delete", views.CarDeleteView.as_view(), name="car_delete_view"),
]
