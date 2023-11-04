from django.urls import path
from Levashova_app import views

urlpatterns = [
    path('owners/<int:car_owner_id>', views.car_owner_detail),
    path('owners', views.car_owners_list_view),
    path('cars', views.CarsList.as_view()),
    path('cars/<int:car_id>', views.car_detail),
    path('owners/create', views.create_owner),
    path('cars/create', views.CreateCar.as_view()),
    path('cars/update/<int:pk>', views.UpdateCar.as_view()),
    path('cars/delete/<int:pk>', views.DeleteCar.as_view())
]
