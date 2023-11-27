"""project_first_app URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path('owner/<int:id>', views.owner),
]
