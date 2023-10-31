from django.urls import path
from .views import *
urlpatterns = [
    path('carowners/<int:carowner_id>/', owner_detail),
    path('time/', example_view),
    path('carowners/all/', list_carowners_view),
    path('cars/all/', CarList.as_view()),
    path('cars/<int:pk>/', CarRetrieveView.as_view()),
    path('cars/list/', CarsOfOwnerListView.as_view()),
    path('cars/list/<int:pk>', CarsOfOwnerListView.as_view()),
    path('carowners/create/', create_car_owner_view),
    path('cars/<int:pk>/update/', CarUpdateView.as_view()),
    path('cars/create/', CarCreateView.as_view(success_url="/cars/list")),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view()),
]