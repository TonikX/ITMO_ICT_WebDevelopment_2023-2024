from django.urls import path
from . import views


app_name = 'warriors_app'
urlpatterns = [
    path("warriors/", views.WarriorAPIView.as_view()),
    path('profession/create/', views.ProfessionCreateView.as_view()),
    path("warrior-with-profession", views.ListAPIWariorWithProfession.as_view()),
    path("warrior-with-skill", views.ListAPIWariorWithSkill.as_view()),
    path("warriors/<int:pk>", views.RetriveAPIWarriorwithSkillsAndProfession.as_view()),
]
