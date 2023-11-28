from django.urls import path
from .views import *

urlpatterns = [
    path("staff/", UserAPIView.as_view()),
    path("staff/statistics", average_eggs_by_worker),
    path("staff/<int:pk>", UserExactAPIView.as_view()),
    path("cages/", CageAPIView.as_view()),
    path("cages/<int:pk>", CageExactAPIView.as_view()),
    path("facilities/", FacilityAPIView.as_view()),
    path("facilities/statistics/chicken_by_breed", chickens_by_breed_in_facilities),
    path("facilities/<int:pk>", FacilityExactAPIView.as_view()),
    path("report", report)
]
