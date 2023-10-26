from django.urls import path
from . import views

urlpatterns = [
    path('owners/<int:owner_id>/', views.show_owner),
    path('owners', views.index_owners),
    path('owners/create', views.create_owner),

    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.CarDetails.as_view()),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('cars/create/', views.CarCreateView.as_view()),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
