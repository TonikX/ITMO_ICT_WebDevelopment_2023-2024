from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("warriors/skills", WarriorSkillsAPIView.as_view()),
    path("warriors/profession", WarriorProfessionListAPIView.as_view()),
    path("warriors/skill", WarriorSkillListApiView.as_view()),
    path("warriors/<int:pk>", GetWarriorAPIView.as_view()),
    path("warriors/<int:pk>/update", UpdateWarriorAPIView.as_view()),
    path("warriors/<int:pk>/delete", DeleteWarriorAPIView.as_view()),

]
