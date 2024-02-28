from django.urls import path
from . import views


urlpatterns = [
    path('owners/', views.owners),
    path('owner/<int:pk>/', views.owner),
    path('owner/create/', views.create_owner_view),
    path('cars/', views.CarsView.as_view()),
    path('car/<int:pk>/', views.CarView.as_view()),
    path('car/create/', views.CreateCar.as_view()),
    path('car/<int:pk>/update/', views.UpdateCarView.as_view()),
    path('car/<int:pk>/delete/', views.DeleteCarView.as_view()),
]