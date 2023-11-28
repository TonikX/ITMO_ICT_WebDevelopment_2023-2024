from django.urls import path
from .views import (
    WarriorList,
    WarriorDetail,
    ProfessionCreateView,
    SkillAPIView,
    SkillCreateView,
)

urlpatterns = [
    path("warriors/", WarriorList.as_view(), name="warriors_list"),
    path("warriors/<int:pk>/", WarriorDetail.as_view(), name="warriors_detail"),
    path("profession/create/", ProfessionCreateView.as_view()),
    path("skills/", SkillAPIView.as_view()),
    path("skill/create/", SkillCreateView.as_view()),
]
