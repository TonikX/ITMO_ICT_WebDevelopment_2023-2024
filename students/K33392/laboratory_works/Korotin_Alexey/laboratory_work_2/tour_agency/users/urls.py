from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path("register", TouristCreateView.as_view()),
    path("accounts/login/", LoginView.as_view())
]
