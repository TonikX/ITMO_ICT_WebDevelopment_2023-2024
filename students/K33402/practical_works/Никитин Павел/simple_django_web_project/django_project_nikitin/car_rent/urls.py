from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars', views.cars),
    path('owner/<int:id>/', views.detail),
    path('drivers', views.DriverList.as_view()),
    path('car/<int:pk>/', views.CarView.as_view()),
    path('example_create', views.create_view),
    path('car/create', views.CarCreate.as_view(success_url="/cars")),
    path('driver/<int:pk>/update/', views.DriverUpdateView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
