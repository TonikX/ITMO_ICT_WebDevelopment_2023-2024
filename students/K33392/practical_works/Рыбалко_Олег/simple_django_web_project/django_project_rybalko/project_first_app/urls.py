from django.urls import path

from . import views

urlpatterns = [
    path("car_owner/<int:owner_id>", views.car_owner),
    path("car_owners", views.all_car_owners),
    path("create_car_owner", views.create_car_owner),
    path("car/<int:car_id>/owners", views.all_owners),
    path("car/<int:pk>", views.CarDetailView.as_view()),
    path("create_car", views.CarCreateView.as_view()),
    path("car/<int:pk>/update", views.CarUpdateView.as_view()),
    path("car/<int:pk>/delete", views.CarDeleteView.as_view()),
    path("cars", views.CarListView.as_view()),
]
