from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warriors/profession', WarriorsProfessionListAPIView.as_view()),
    path('warriors/skills', WarriorsSkillsListAPIView.as_view()),
    path('warriors/<int:pk>', WarriorAPIView.as_view()),
]
