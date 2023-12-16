from django.urls import path
from .views import *


urlpatterns = [
    path("chickens/", ChickenAPIView.as_view()),
    path("chickens/<int:pk>", ChickenExactAPIView.as_view()),
    path("breeds/", BreedAPIView.as_view()),
    path("breeds/<int:pk>", BreedExactAPIView.as_view()),
    path("diets/", DietAPIView.as_view()),
    path("diets/<int:pk>", DietExactAPIView.as_view()),
    path("breeds/statistics", get_differences_by_breed)
]
