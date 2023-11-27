from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skills/create/', SkillCreateView.as_view()),
   path('warriors/listprofession/', WarriorListProfessionAPIView.as_view()),
   path('warriors/listskill/', WarriorListSkillAPIView.as_view()),
   path('warriors/<int:pk>/', WarriorOneAPIView.as_view()),
   path('warriors/<int:pk>/delete', WarriorDeleteAPIView.as_view()),
   path('warriors/<int:pk>/edit', WarriorEditAPIView.as_view()),
]
