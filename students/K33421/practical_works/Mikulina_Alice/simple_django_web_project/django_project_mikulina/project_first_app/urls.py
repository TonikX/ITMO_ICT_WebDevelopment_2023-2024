from django.urls import path 
from . import views
from .views import *


urlpatterns = [
    path('driver/<int:driver_id>/', views.show_driver),
    path('time/', views.show_time),
    path('driver/all', views.list_drivers),
    path('driver/create', views.create_driver),
    path('car/all', CarList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/list/', CarListView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]