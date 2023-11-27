from django.urls import path
from .views import *

urlpatterns = [
    path("staff/", UserAPIView.as_view()),
    path("staff/<int:pk>", UserExactAPIView.as_view()),
    path("cages/", CageAPIView.as_view()),
    path("cages/<int:pk>", CageExactAPIView.as_view()),
    path("facilities/", FacilityAPIView.as_view()),
    path("facilities/<int:pk>", FacilityExactAPIView.as_view())
]
