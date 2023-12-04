from django.urls import path
from . import views

urlpatterns = [
    path('owners/<int:car_owner_id>', views.car_owner_detail),
    path('owners', views.car_owners_list_view),
    path('cars', views.CarsList.as_view()),
    path('cars/<int:car_id>', views.car_detail),
]