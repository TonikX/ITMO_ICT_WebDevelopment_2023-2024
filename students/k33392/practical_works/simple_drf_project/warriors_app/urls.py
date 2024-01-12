from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path("warriors/", WarriorListAPIView.as_view()),
    path("profession/create/", ProfessionCreateAPIView.as_view()),
    path("skills/", SkillAPIView.as_view()),
    path("skill/create/", SkillCreateView.as_view()),
    path('warriors-with-professions/', WarriorWithProfessionsView.as_view()),
    path('warriors-with-skills/', WarriorWithSkillsView.as_view()),
    path('warriors/<int:pk>/', WarriorDetail.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdate.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDelete.as_view())
]
