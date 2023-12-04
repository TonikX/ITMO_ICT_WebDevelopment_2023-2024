from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('professions/', ProfessionListView.as_view()),
    path('skills/create/', SkillCreateView.as_view(), name='skill-create'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('warriors/full-info/professions/', WarriorProfessionsView.as_view(), name='warriors-professions'),
    path('warriors/full-info/skills/', WarriorSkillsView.as_view(), name='warriors-skills'),
    path('warriors/full-info/<int:pk>/', WarriorFullInfoByIdView.as_view(), name='warrior-full-info-by-id'),
    path('warriors/delete/<int:pk>/', WarriorDeleteView.as_view(), name='warrior-delete'),
    path('warriors/edit/<int:pk>/', WarriorEditView.as_view(), name='warrior-edit'),
]