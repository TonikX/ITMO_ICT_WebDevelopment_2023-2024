from django.urls import path
from .views import *

urlpatterns = [
    path("register", TouristCreateView.as_view()),
]
