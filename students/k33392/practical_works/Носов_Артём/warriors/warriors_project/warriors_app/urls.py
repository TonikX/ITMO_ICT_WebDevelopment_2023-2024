from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/<str:pk>/', WarriorGETAPIView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('warriors/delete/<str:pk>/', WarriorDestroyAPIView.as_view()),
   path('warriors/update/<str:pk>/', WarriorUpdateAPIView.as_view()),

   path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
   path('skills_of_warrior/', SkillOfWarriorAPIView.as_view()),
   path('skill_of_warrior/create/', SkillOfWarriorCreateView.as_view()),


]