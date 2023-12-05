from django.urls import path

from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view(), name='warrior-list'),
    path('warriors/<int:pk>/', WarriorDetailAPIView.as_view(), name='warrior-detail'),
    path('warriors/professions/', WarriorProfessionsAPIView.as_view(), name='warrior-professions'),
    path('warriors/skills/', WarriorSkillsAPIView.as_view(), name='warrior-skills'),
    path('warriors/<int:pk>/info/', WarriorDetailInfoAPIView.as_view(), name='warrior-info'),
    path('warriors/create/', WarriorCreateAPIView.as_view(), name='warrior-create'),
]
