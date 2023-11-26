from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorsWithProfessionsAPIView.as_view(), name='warrior-list'),
    path('warriors/<int:pk>/', WarriorDetailAPIView.as_view(), name='warrior-detail'),
    path('warriors/<int:pk>/full-info/', WarriorFullInfoAPIView.as_view(), name='warrior-full-info'),
    path('warriors/<int:pk>/delete/', WarriorDetailAPIView.as_view(), name='warrior-delete'),
    # Add more URL patterns for other views if needed
]
