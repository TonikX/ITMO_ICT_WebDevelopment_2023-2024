from django.urls import path
from django.views.generic import TemplateView
from .views import (
    WarriorWithProfessionAPIView,
    ProfessionCreateView,
    WarriorWithSkillsAPIView,
    WarriorDetailsAPIView,
    WarriorDeleteAPIView,
    WarriorUpdateAPIView,
)

app_name = "warriors_app"

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('warriors_with_professions/', WarriorWithProfessionAPIView.as_view(), name='warriors_with_professions'),
    path('warriors/', WarriorWithProfessionAPIView.as_view(), name='warrior_list'),  # Изменил путь, чтобы избежать конфликта
    path('profession/create/', ProfessionCreateView.as_view(), name='create_profession'),
    path('warriors-with-skills/', WarriorWithSkillsAPIView.as_view(), name='warriors_with_skills'),
    path('warriors/<int:pk>/', WarriorDetailsAPIView.as_view(), name='warrior_details'),
    path('warriors/<int:pk>/delete/', WarriorDeleteAPIView.as_view(), name='warrior_delete'),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view(), name='warrior_update'),
]
