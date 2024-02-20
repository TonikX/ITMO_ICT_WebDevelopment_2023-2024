from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('skill/generic_create/', SkillCreateAPIView.as_view()),
    path("skills/", SkillList.as_view(), name="skill-list"),
    path("warriors/", WarriorList.as_view(), name="warrior-list"),
    path("warriors/<int:pk>/", WarriorDetail.as_view(), name="warrior-detail"),
]